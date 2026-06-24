#!/usr/bin/env python3
"""REST adapter for image generation via the OpenAI-compatible images/generations endpoint.

Standalone default renderer for the teaser / figure workflow (see
references/image-render-invocation.md): POSTs the prompt to an
`images/generations` endpoint and writes the resulting PNG. Needs only an API
key + endpoint (env vars below) — no Codex CLI or MCP bridge.

Also usable by the codex-image2 MCP bridge as a fallback when the Codex CLI
cannot invoke native imageGeneration (e.g. when the configured provider routes
coding-model traffic on `responses` but exposes image generation only via the
sibling `images/generations` REST endpoint).

Configuration precedence:

  1. Dedicated env vars (preferred — no Codex config needed):

        GPT_IMAGE2_API_KEY        bearer token for the images endpoint
        GPT_IMAGE2_API_URL        full URL of the images/generations endpoint
                                   (or a base URL — '/images/generations' is
                                   appended if not present)

  2. Codex config fallback (used only if the GPT_IMAGE2_* vars above are unset):

        ~/.codex/auth.json           must contain OPENAI_API_KEY
        ~/.codex/config.toml         active [model_providers.<name>].base_url
                                       + '/images/generations'

Optional overrides:

    GPT_IMAGE2_MODEL          image model (default: gpt-image-2)
    GPT_IMAGE2_SIZE           default size (default: 1024x1024)
    GPT_IMAGE2_QUALITY        default quality (default: high)
    GPT_IMAGE2_TIMEOUT_SEC    request timeout (default: 540)
    CODEX_HOME                Codex config dir override (default: ~/.codex)

Standalone CLI:

    python3 images_api_render.py generate \\
        --prompt-file prompt.txt \\
        --out figures/ai_generated/figure.png \\
        --size 1024x1024 --quality high

    python3 images_api_render.py check      # report config mode: env | codex | mixed | unavailable
    python3 images_api_render.py endpoint   # print the resolved URL
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

DEFAULT_MODEL = os.environ.get("GPT_IMAGE2_MODEL", "gpt-image-2")
DEFAULT_SIZE = os.environ.get("GPT_IMAGE2_SIZE", "1024x1024")
DEFAULT_QUALITY = os.environ.get("GPT_IMAGE2_QUALITY", "high")
DEFAULT_TIMEOUT = int(os.environ.get("GPT_IMAGE2_TIMEOUT_SEC", "540"))

CODEX_HOME = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex")))
AUTH_PATH = CODEX_HOME / "auth.json"
CONFIG_PATH = CODEX_HOME / "config.toml"

PNG_SIG = b"\x89PNG\r\n\x1a\n"


class FallbackError(RuntimeError):
    pass


def _env(name: str) -> str:
    value = os.environ.get(name, "")
    return value.strip() if value else ""


def read_api_key() -> tuple[str, str]:
    """Return (api_key, source) where source is 'env' or 'codex-auth'."""
    env_key = _env("GPT_IMAGE2_API_KEY")
    if env_key:
        return env_key, "env"
    if not AUTH_PATH.is_file():
        raise FallbackError(
            f"no GPT_IMAGE2_API_KEY env var set and no Codex auth file at {AUTH_PATH}"
        )
    try:
        data = json.loads(AUTH_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise FallbackError(f"could not parse {AUTH_PATH}: {exc}")
    key = data.get("OPENAI_API_KEY") or data.get("api_key")
    if not key:
        raise FallbackError(
            f"no GPT_IMAGE2_API_KEY env var and no OPENAI_API_KEY/api_key in {AUTH_PATH}"
        )
    return str(key), "codex-auth"


def _parse_config_provider() -> tuple[str | None, str | None]:
    """Return (provider_name, base_url) from ~/.codex/config.toml.

    Hand-rolled to avoid depending on tomllib (py3.11+) or tomli.
    """
    if not CONFIG_PATH.is_file():
        return None, None
    text = CONFIG_PATH.read_text(encoding="utf-8")

    provider_name: str | None = None
    current_section: str | None = None
    sections: dict[str, dict[str, str]] = {}

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("[") and line.endswith("]"):
            current_section = line[1:-1].strip()
            sections.setdefault(current_section, {})
            continue
        if "=" not in line:
            continue
        key, _, val = line.partition("=")
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        if current_section is None:
            if key == "model_provider":
                provider_name = val
        else:
            sections[current_section][key] = val

    if provider_name is None:
        return None, None
    base_url = sections.get(f"model_providers.{provider_name}", {}).get("base_url")
    return provider_name, base_url


def resolve_endpoint() -> tuple[str, str]:
    """Return (endpoint_url, source) where source is 'env' or 'codex-config'."""
    env_url = _env("GPT_IMAGE2_API_URL")
    if env_url:
        url = env_url.rstrip("/")
        if not url.endswith("/images/generations"):
            url = url + "/images/generations"
        return url, "env"
    _, base_url = _parse_config_provider()
    if not base_url:
        raise FallbackError(
            "no GPT_IMAGE2_API_URL env var set and could not derive base_url "
            f"from {CONFIG_PATH}; set GPT_IMAGE2_API_URL to the full "
            "images/generations endpoint (e.g. https://your.proxy/v1/images/generations)"
        )
    return base_url.rstrip("/") + "/images/generations", "codex-config"


def run_check() -> dict[str, Any]:
    """Resolve auth + endpoint and classify the config mode WITHOUT a network call.

    Returns a verdict dict. `mode` is one of:
      "env"          both API key and endpoint come from GPT_IMAGE2_* env vars
      "codex"        both come from the Codex config (~/.codex auth.json + config.toml)
      "mixed"        one from env, the other from Codex config (still usable)
      "unavailable"  key and/or endpoint could not be resolved (see `errors`)
    """
    auth_source: str | None = None
    endpoint_source: str | None = None
    endpoint_url: str | None = None
    errors: list[str] = []

    try:
        _, auth_source = read_api_key()
    except FallbackError as exc:
        errors.append(f"auth: {exc}")
    try:
        endpoint_url, endpoint_source = resolve_endpoint()
    except FallbackError as exc:
        errors.append(f"endpoint: {exc}")

    available = not errors
    if not available:
        mode = "unavailable"
    elif auth_source == "env" and endpoint_source == "env":
        mode = "env"
    elif auth_source == "codex-auth" and endpoint_source == "codex-config":
        mode = "codex"
    else:
        mode = "mixed"

    return {
        "ok": available,
        "available": available,
        "mode": mode,
        "authSource": auth_source,
        "endpointSource": endpoint_source,
        "endpoint": endpoint_url,
        "model": DEFAULT_MODEL,
        "errors": errors,
    }


def compose_prompt(prompt: str, system: str | None) -> str:
    body = (prompt or "").strip()
    if not body:
        raise FallbackError("empty prompt")
    sys_text = (system or "").strip()
    if sys_text:
        return f"{sys_text}\n\n{body}"
    return body


def download_image(url: str, timeout: int) -> bytes:
    """Fetch image bytes from a hosted-image `url` returned by some endpoints.

    OpenAI-compatible image endpoints may return either base64 (`b64_json`) or a
    hosted `url` in `data[0]`. For the url variant we download the bytes here.
    A browser-like User-Agent is required: some image hosts return HTTP 403 to a
    bare urllib request. Proxies in the environment are honored automatically.
    """
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0", "Accept": "image/*,*/*"},
        method="GET",
    )
    try:
        with urllib.request.urlopen(req, timeout=min(timeout, 180)) as resp:
            return resp.read()
    except urllib.error.HTTPError as exc:
        raise FallbackError(f"HTTP {exc.code} downloading image url {url[:120]}")
    except urllib.error.URLError as exc:
        raise FallbackError(f"network error downloading image url {url[:120]}: {exc}")


def generate_via_rest(
    *,
    prompt: str,
    output_path: Path,
    system: str | None = None,
    model: str = DEFAULT_MODEL,
    size: str = DEFAULT_SIZE,
    quality: str = DEFAULT_QUALITY,
    timeout: int = DEFAULT_TIMEOUT,
) -> dict[str, Any]:
    """POST to images/generations and write the resulting PNG.

    Returns a dict whose shape mirrors the codex-image2 native-path result so
    callers (including server.py) can treat both code paths uniformly.
    """
    api_key, key_source = read_api_key()
    endpoint, url_source = resolve_endpoint()
    full_prompt = compose_prompt(prompt, system)

    payload = {
        "model": model,
        "prompt": full_prompt,
        "size": size,
        "quality": quality,
        "n": 1,
    }
    req = urllib.request.Request(
        endpoint,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = json.loads(resp.read())
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:500]
        raise FallbackError(f"HTTP {exc.code} from {endpoint}: {detail}")
    except urllib.error.URLError as exc:
        raise FallbackError(f"network error calling {endpoint}: {exc}")

    data = body.get("data") or []
    if not data:
        raise FallbackError(
            f"unexpected response from {endpoint}: {json.dumps(body)[:400]}"
        )

    # Accept both standard image-response shapes: inline base64 (`b64_json`) or a
    # hosted `url` (which we then download). Endpoints differ in their default,
    # and forcing `response_format` is avoided — some providers reject it and
    # others slow down / time out under base64. So handle whatever comes back.
    item = data[0]
    img_source: str
    if item.get("b64_json"):
        png_bytes = base64.b64decode(item["b64_json"])
        img_source = "b64_json"
    elif item.get("url"):
        png_bytes = download_image(item["url"], timeout)
        img_source = "url"
    else:
        raise FallbackError(
            f"response from {endpoint} has neither b64_json nor url in data[0]: "
            f"{json.dumps(body)[:400]}"
        )

    if not png_bytes.startswith(PNG_SIG):
        raise FallbackError("downloaded/decoded payload is not a PNG image")

    output_path = output_path.expanduser().resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(png_bytes)

    return {
        "outputPath": str(output_path),
        "imageCount": 1,
        "model": body.get("model", model),
        "size": body.get("size", size),
        "quality": body.get("quality", quality),
        "revisedPrompt": item.get("revised_prompt"),
        "imageSource": img_source,
        "nativeToolConfirmed": True,
        "fallback": "rest",
        "endpoint": endpoint,
        "authSource": key_source,
        "endpointSource": url_source,
    }


def cli(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="GPT image2 REST adapter")
    sub = parser.add_subparsers(dest="cmd", required=True)

    gen = sub.add_parser("generate", help="Generate an image via images/generations")
    gen.add_argument("--prompt", help="Prompt text (use --prompt-file for long prompts)")
    gen.add_argument("--prompt-file", help="File containing the prompt")
    gen.add_argument("--system", help="Optional system / style preamble prepended to the prompt")
    gen.add_argument("--system-file", help="File containing the system preamble")
    gen.add_argument("--out", required=True, help="Output PNG path")
    gen.add_argument("--size", default=DEFAULT_SIZE)
    gen.add_argument("--quality", default=DEFAULT_QUALITY)
    gen.add_argument("--model", default=DEFAULT_MODEL)
    gen.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)

    sub.add_parser("endpoint", help="Print the resolved endpoint URL and config source")

    chk = sub.add_parser(
        "check",
        help="Pre-run check: report whether config resolves via env vars, Codex config, or is unavailable",
    )
    chk.add_argument("--json-out", help="Optional path to also save the JSON verdict")

    args = parser.parse_args(argv)

    if args.cmd == "check":
        verdict = run_check()
        text = json.dumps(verdict, indent=2, ensure_ascii=False)
        if args.json_out:
            out = Path(args.json_out).expanduser()
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(text + "\n", encoding="utf-8")
        print(text)
        return 0 if verdict["ok"] else 1

    if args.cmd == "endpoint":
        try:
            url, src = resolve_endpoint()
        except FallbackError as exc:
            sys.stderr.write(f"{exc}\n")
            return 1
        try:
            _, key_src = read_api_key()
        except FallbackError as exc:
            print(json.dumps({"endpoint": url, "endpointSource": src, "authError": str(exc)}, indent=2))
            return 1
        print(json.dumps({"endpoint": url, "endpointSource": src, "authSource": key_src}, indent=2))
        return 0

    if args.cmd == "generate":
        prompt = args.prompt
        if args.prompt_file:
            prompt = Path(args.prompt_file).read_text(encoding="utf-8")
        if not prompt or not prompt.strip():
            sys.stderr.write("error: empty prompt (--prompt or --prompt-file required)\n")
            return 2

        system = args.system
        if args.system_file:
            system = Path(args.system_file).read_text(encoding="utf-8")

        try:
            result = generate_via_rest(
                prompt=prompt,
                output_path=Path(args.out),
                system=system,
                model=args.model,
                size=args.size,
                quality=args.quality,
                timeout=args.timeout,
            )
        except FallbackError as exc:
            sys.stderr.write(f"{exc}\n")
            return 1
        print(json.dumps({"ok": True, **result}, indent=2, ensure_ascii=False))
        return 0

    parser.error(f"unknown command: {args.cmd}")
    return 2


if __name__ == "__main__":
    raise SystemExit(cli())
