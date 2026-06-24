# Image-Render Invocation — How to Actually Call the Drawing Program

**Purpose**: the concrete mechanics of generating a raster figure (teaser, architecture, conceptual diagram) through the **Codex `codex-image2` app-server bridge** — preflight, render, poll, finalize, verify.

This file is the *plumbing* the teaser playbook keeps out of its prose: `teaser-figure-playbook.md` Step 5 supplies the **brief** (`teaser-prompt.yaml`) and the **acceptance bar**, and points here for the **call**. It is self-contained — the helper script ships in this repo at [`tools/figure_render_helper.py`](../tools/figure_render_helper.py) (pure Python standard library; no external skill or runtime required).

**Requirements**: the `mcp__codex-image2__*` MCP bridge (the renderer) and the `codex` CLI on `PATH` (used by `preflight`). If the bridge is unavailable, this is not the renderer to use — hand the prompt to another image tool or draw by hand, and say so plainly.

---

## Constants

| Name | Value | Meaning |
|---|---|---|
| `RENDERER` | `codex-image2` | Native image-generation bridge via local Codex app-server (`mcp__codex-image2__generate_start` / `generate_status`) |
| `OPTIONAL_TEXT_CRITIC` | `mcp__codex__codex` | Optional text-only second opinion for layout/style checks |
| `HELPER` | `tools/figure_render_helper.py` | This repo's `preflight` / `finalize` / `verify` helper |
| `OUTPUT_DIR` | `figures/ai_generated/` | Where renders and receipts land |
| `TEXT_LANGUAGE` | `English` | Default figure-text language unless the user asks otherwise |
| `NATIVE_IMAGE_REQUIREMENT` | `strict` | Accept ONLY native `imageGeneration` output; reject shell/Python/manual-bitmap fallbacks masquerading as generation |

All helper calls below are `python3 tools/figure_render_helper.py <subcommand>` (adjust the path if you run from outside the repo root).

---

## Step A — Preflight (gate before rendering)

```bash
python3 tools/figure_render_helper.py preflight \
  --workspace <cwd> \
  --json-out figures/ai_generated/preflight.json
```

- Creates `figures/ai_generated/` if it does not exist.
- Pings the `codex` app-server. Confirm the JSON says `ok=true` **before** calling the renderer; if not `ok=true` (codex CLI missing, ping failed/timed out), stop and say so clearly.

---

## Step B — Render through the bridge

Call `mcp__codex-image2__generate_start` with:

| Param | Example | Notes |
|---|---|---|
| `prompt` | the final image prompt (your `generation_prompt`) | fully specified: components, layout, flow, labels, style, what to avoid |
| `cwd` | project root / paper workspace | |
| `outputPath` | `figures/ai_generated/figure_v1.png` | bump `_vN` per round |
| `system` | `Academic paper figure. Prefer crisp English labels.` | short renderer instruction |
| `timeoutSeconds` | `180` | bounded render timeout |

Then poll `mcp__codex-image2__generate_status` with bounded waits until either:

- `done=true` and `status=completed`, or
- `done=true` and `status=failed`.

If generation fails, surface the bridge error directly — do not hide it or substitute a fallback bitmap.

---

## Step C — Finalize and verify (on acceptance)

When a render is accepted (quick mode: the first good one; loop mode: score ≥ target):

```bash
python3 tools/figure_render_helper.py finalize \
  --workspace <cwd> \
  --best-image figures/ai_generated/figure_vN.png \
  --caption "Replace with a paper-ready caption." \
  --label fig:teaser \
  --score 9 \
  --review-summary "Accepted; labels and arrows are paper-ready."

python3 tools/figure_render_helper.py verify \
  --workspace <cwd> \
  --json-out figures/ai_generated/verify.json
```

`finalize` promotes the best image to `figure_final.png` and writes `latex_include.tex` + `review_log.json` (`--caption` / `--label` default to placeholders if omitted). Always run `verify` before claiming success.

**Repair path** — if rendering succeeded but the final artifacts were skipped, re-run `finalize` then `verify` (same commands) to emit them.

`finalize` writes this LaTeX include for you (`tools/figure_render_helper.py` → `latex_include.tex`):

```latex
\begin{figure*}[t]
    \centering
    \includegraphics[width=0.95\textwidth]{figures/ai_generated/figure_final.png}
    \caption{Replace with a paper-ready caption.}
    \label{fig:teaser}
\end{figure*}
```

---

## Output structure

```text
figures/ai_generated/
├── preflight.json     # preflight receipt (ok=true gate)
├── figure_v1.png      # iteration 1 (quick mode stops here)
├── figure_v2.png      # iteration 2 (loop mode)
├── figure_final.png   # accepted version (copy of best)
├── latex_include.tex  # LaTeX snippet
├── review_log.json    # review notes / refinement history
└── verify.json        # verification diagnostic
```

---

## Invocation rules

1. Use the `codex-image2` bridge **only for native image generation**; reject any shell/Python/manual-bitmap fallback dressed up as generation.
2. If the bridge says native generation is unavailable, surface that honestly — do not fake an image.
3. Gate on `preflight` `ok=true` before rendering; run `verify` before claiming success.
4. Keep figure text in **English** unless the user requested another language.
5. Report bridge errors directly instead of hiding them.
6. The helper and bridge are wiring; the figure's **content/style brief and acceptance bar live in `teaser-figure-playbook.md`** (Steps 2 & 5) and `teaser-prompt.yaml`.
