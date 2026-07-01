# Image-Render Invocation — How to Actually Call the Drawing Program

**Purpose**: the concrete mechanics of generating a raster figure (teaser, architecture, conceptual diagram) — endpoint check, render, finalize, verify.

This file is the *plumbing* the teaser playbook keeps out of its prose: `teaser-figure-playbook.md` Step 5 supplies the **brief** (`teaser-prompt.yaml`) and the **acceptance bar**, and points here for the **call**. Both bundled scripts are pure Python standard library — no third-party packages.

**Default renderer**: the REST adapter [`tools/images_api_render.py`](../tools/images_api_render.py), which POSTs to an OpenAI-compatible `images/generations` endpoint (`gpt-image-2` by default) and writes the PNG directly. No MCP bridge or `codex` CLI required — only an API key + endpoint (below). The Codex `codex-image2` MCP bridge is kept as an **alternative** (see "Alternative renderer").

**Requirements (default path)**: an images endpoint reachable over HTTPS, configured via either —
- `GPT_IMAGE2_API_KEY` + `GPT_IMAGE2_API_URL` (preferred — explicit, no Codex needed), or
- a Codex install (`~/.codex/auth.json` `OPENAI_API_KEY` + the active provider `base_url` in `~/.codex/config.toml`), used only if the `GPT_IMAGE2_*` vars are unset.

If neither resolves, this is not the renderer to use — say so plainly and hand the prompt to another image tool or draw by hand.

---

## Constants

| Name | Value | Meaning |
|---|---|---|
| `RENDERER` | `tools/images_api_render.py` | Default: REST adapter → OpenAI-compatible `images/generations` |
| `HELPER` | `tools/figure_render_helper.py` | Renderer-agnostic `finalize` / `verify` (+ a Codex-bridge `preflight`) |
| `OUTPUT_DIR` | `figures/ai_generated/` | Where renders and receipts land (under the user's **workspace**, not the skill) |
| `IMAGE_MODEL` | `gpt-image-2` | Override via `GPT_IMAGE2_MODEL`; size/quality via `GPT_IMAGE2_SIZE` / `GPT_IMAGE2_QUALITY` |
| `TEXT_LANGUAGE` | `English` | Default figure-text language unless the user asks otherwise |
| `ALT_RENDERER` | `codex-image2` | Alternative: native bridge via `mcp__codex-image2__generate_start` / `generate_status` |

Both scripts are bundled tools, so they resolve like every other one — see **SKILL.md → "Bundled tools — Path resolution"**. Each command block below carries the one-line resolver inline (Bash tool calls don't share shell state). `<cwd>` / `--workspace` is always the user's **paper workspace**, never the skill dir.

---

## Step A — Preflight (check the endpoint resolves)

```bash
RENDER="${CLAUDE_SKILL_DIR:-$(pwd)}/tools/images_api_render.py"; [ -f "$RENDER" ] || RENDER="tools/images_api_render.py"  # see SKILL.md → Bundled tools
mkdir -p figures/ai_generated
python3 "$RENDER" check --json-out figures/ai_generated/render_check.json
```

`check` resolves the config **without making a network call** and reports `mode`:

| `mode` | Meaning | Action |
|---|---|---|
| `env` | key + endpoint from `GPT_IMAGE2_API_KEY` / `GPT_IMAGE2_API_URL` | proceed |
| `codex` | both from the Codex config (`~/.codex/auth.json` + `config.toml`) | proceed |
| `mixed` | one from env, one from Codex config | proceed (usable) |
| `unavailable` | key and/or endpoint unresolved (see `errors`) | configure the API, or use the alternative renderer / draw by hand |

Confirm `check` exits 0 (`available: true`) **before** rendering. On `unavailable`, the `errors` array says exactly what's missing. (`python3 "$RENDER" endpoint` is the quick variant — just prints the resolved URL + sources.)

> When driven from the teaser playbook, this check is already run at its Step 4 gate and its `mode` recorded in `teaser-prompt.yaml`'s `render` block — `check` is idempotent and network-free, so re-running it here is harmless, but you can skip it if the YAML already says `render.mode` is available.

---

## Step B — Render (default: REST adapter)

Write the prompt to a file (avoids shell-quoting issues with long, multi-line prompts), then generate:

```bash
RENDER="${CLAUDE_SKILL_DIR:-$(pwd)}/tools/images_api_render.py"; [ -f "$RENDER" ] || RENDER="tools/images_api_render.py"
# prompt body = your generation_prompt; system = short style preamble
python3 "$RENDER" generate \
  --prompt-file figures/ai_generated/prompt.txt \
  --system "Academic paper figure. Clean, paper-ready, crisp English labels." \
  --out figures/ai_generated/figure_v1.png \
  --size 1024x1024 --quality high
```

- Bump `figure_vN.png` per round (quick mode stops at v1; loop mode iterates — see playbook Step 5).
- On success it writes the PNG and prints a JSON receipt (`ok=true`, `outputPath`, `model`, `size`, `revisedPrompt`, `imageSource` (`b64_json`|`url`), …).
- On failure (HTTP error, network error, non-PNG payload) it prints the error and exits 1 — surface that directly, don't fake an image.
- `--size` / `--quality` / `--model` default to the `GPT_IMAGE2_*` env values; pass flags to override per render.

> **A render is slow — background it.** One high-quality render commonly takes **several minutes** and the adapter's own request timeout is **540 s (9 min)** by default (`GPT_IMAGE2_TIMEOUT_SEC`). When you drive this from an agent/harness whose per-command timeout is shorter (often 1–2 min), run the `generate` call **detached / in the background** (or raise the tool timeout to ≥ 10 min) and poll for the PNG — otherwise the command is killed mid-render with no output. It is not hung; it is waiting on the endpoint.

> **Both response shapes are handled.** OpenAI-compatible endpoints return the image either inline as base64 (`data[0].b64_json`) or as a hosted `url`; the adapter accepts both (downloading the `url` with a browser User-Agent when needed) and reports which via `imageSource`. It does **not** force `response_format` — some providers reject it, and some slow down or time out when forced to base64. If your endpoint times out only at high quality, try `--quality medium` or a smaller `--size` first.

---

## Step C — Finalize and verify (on acceptance)

When a render is accepted (quick mode: the first good one; loop mode: score ≥ target), use the renderer-agnostic helper:

```bash
HELPER="${CLAUDE_SKILL_DIR:-$(pwd)}/tools/figure_render_helper.py"; [ -f "$HELPER" ] || HELPER="tools/figure_render_helper.py"  # see SKILL.md → Bundled tools
python3 "$HELPER" finalize \
  --workspace <cwd> \
  --best-image figures/ai_generated/figure_vN.png \
  --caption "Replace with a paper-ready caption." \
  --label fig:teaser \
  --score 9 \
  --review-summary "Accepted; labels and arrows are paper-ready."

python3 "$HELPER" verify \
  --workspace <cwd> \
  --json-out figures/ai_generated/verify.json
```

`finalize` promotes the best image to `figure_final.png` and writes `latex_include.tex` + `review_log.json` (`--caption` / `--label` default to placeholders if omitted). Always run `verify` before claiming success. All artifacts land under the user's workspace (`<cwd>/figures/ai_generated/`), never inside the skill dir.

**Repair path** — if rendering succeeded but the final artifacts were skipped, re-run `finalize` then `verify` (same commands) to emit them.

`finalize` writes this LaTeX include for you (`figure_render_helper.py` → `latex_include.tex`):

```latex
\begin{figure*}[t]
    \centering
    \includegraphics[width=0.95\textwidth]{figures/ai_generated/figure_final.png}
    \caption{Replace with a paper-ready caption.}
    \label{fig:teaser}
\end{figure*}
```

---

## Alternative renderer — Codex `codex-image2` MCP bridge

Use this only when the REST endpoint is unavailable but the Codex bridge is installed. Preflight with the helper's Codex-aware check, then render through the MCP bridge:

```bash
HELPER="${CLAUDE_SKILL_DIR:-$(pwd)}/tools/figure_render_helper.py"; [ -f "$HELPER" ] || HELPER="tools/figure_render_helper.py"
python3 "$HELPER" preflight --workspace <cwd> --json-out figures/ai_generated/preflight.json   # pings the codex app-server; needs ok=true
```

Then call `mcp__codex-image2__generate_start` with `prompt` (your `generation_prompt`), `cwd`, `outputPath` (`figures/ai_generated/figure_v1.png`), `system` (`Academic paper figure. Prefer crisp English labels.`), `timeoutSeconds` (`180`); poll `mcp__codex-image2__generate_status` until `done=true` with `status=completed` (or `failed`). Accept only native `imageGeneration` output — reject any shell/manual-bitmap fallback. On acceptance, hand the PNG to Step C (finalize/verify) exactly as above.

---

## Output structure

```text
figures/ai_generated/
├── prompt.txt         # the generation prompt (default path, --prompt-file)
├── render_check.json  # default path: config-resolution verdict (mode: env|codex|mixed|unavailable)
├── preflight.json     # alt-path only: codex app-server ping receipt
├── figure_v1.png      # iteration 1 (quick mode stops here)
├── figure_v2.png      # iteration 2 (loop mode)
├── figure_final.png   # accepted version (copy of best)
├── latex_include.tex  # LaTeX snippet
├── review_log.json    # review notes / refinement history
└── verify.json        # verification diagnostic
```

---

## Invocation rules

1. Default to the REST adapter (`images_api_render.py`); fall back to the `codex-image2` bridge only when the endpoint is unconfigured but the bridge is installed.
2. Gate before rendering: REST path → `endpoint` exits 0; bridge path → `preflight` `ok=true`. Run `verify` before claiming success.
3. If neither renderer is available, say so honestly — do not fake an image or pass off a hand-built bitmap as a generated one.
4. Keep figure text in **English** unless the user requested another language. State this **inside the `generation_prompt` itself** (`ALL text in ENGLISH only, no other language`), not merely in the operator's `--system` preamble or config — the model renders text in the language it sees in the prompt and will otherwise drift to the surrounding conversation's language. Likewise put the "no title baked into the image" and "no sentences / no leaked prompt text or `[cite: N]` markers" guards in the prompt (teaser-figure-playbook.md Step 2, mandatory negative constraints).
5. Report renderer errors (HTTP/network/bridge) directly instead of hiding them.
6. The scripts are wiring; the figure's **content/style brief and acceptance bar live in `teaser-figure-playbook.md`** (Steps 2 & 5) and `teaser-prompt.yaml`.
