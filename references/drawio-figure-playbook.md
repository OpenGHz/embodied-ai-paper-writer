# draw.io Figures — Vector Diagram Playbook

**Purpose**: conventions for building **vector diagrams** — architecture (F2), pipeline, and conceptual figures — in draw.io, and exporting them cleanly for a LaTeX paper.

Use this when the user asks: "build my architecture figure", "make a pipeline diagram", "draw the method overview in draw.io", "export my .drawio for the paper", "why do my math symbols show as boxes / why is my PDF off-center / two pages?"

> Source: lessons learned building a real method-architecture figure. Distilled into reusable conventions.

---

## When draw.io (vector) vs. the AI raster renderer

| Use **draw.io** (this file) | Use the **AI raster renderer** (`image-render-invocation.md`) |
|---|---|
| Architecture / system diagrams (F2), pipelines, conceptual diagrams, taxonomy trees | Teaser photos, deployment montages, capability collages, single dramatic shots |
| Modules + labeled arrows + math, must be exact and re-editable | Photo-real or stylized scenes you describe in prose |
| Vector PDF, fonts embedded, crisp at any zoom | Raster PNG |

A **pipeline+punchline teaser** can mix both: schematic drawn in draw.io, punchline photo from the raster renderer, composited. The visual-style standards in `teaser-figure-playbook.md` Step 2 (restrained palette, thick dark arrows, grayscale-safe, paper-ready) apply here too — this file is the draw.io-specific way to satisfy them.

---

## 1. Export (most important)

```bash
# For the paper: export PDF only, crop to content, even border, page 1 only
export HOME=${HOME:-/tmp}
drawio -x -f pdf -e --crop --border 10 --page-index 0 \
  -o method_architecture.pdf method_architecture.drawio --no-sandbox
```

- **You only need two files: `.drawio` (source) + `.pdf` (for the paper).** SVG/PNG are redundant in a LaTeX workflow:
  - **PDF** — used directly by `\includegraphics`; vector, fonts embedded.
  - **SVG** — only if you want to re-edit in Inkscape or embed in a web page.
  - **PNG** — raster; preview/self-check only.
- **Self-check by reading the PDF directly** — a single-page vector figure renders the same as a PNG, so there's no need to also export a PNG.
- **`--crop --border 10` is mandatory**: the canvas `pageWidth` is usually larger than the content and the content sits off-center, so without cropping you get a big blank strip on one side and asymmetric margins. Cropping outputs to the content bounding box.
- **`--page-index 0` is recommended**: guards against stray extra pages in the file (see §5) producing a multi-page PDF.
- On Linux/headless: put `--no-sandbox` **at the very end** of the command; `export HOME` first.
- `-e` embeds the source XML into the PDF, so the file stays editable in draw.io.
- Avoid exporting `-e` PNG: draw.io truncates the IEND chunk and strict decoders / vision APIs reject it. The LaTeX/PDF workflow doesn't need PNG, so prefer PDF and sidestep the issue.

---

## 2. Math symbols: use MathJax, not combining characters

- **Symptom**: `K̂` (K + combining circumflex U+0302), calligraphic `𝒦/𝒟/𝓜/𝒰`, etc. render as **empty boxes** after export — the export font can't compose combining marks / lacks astral-plane glyphs.
- **Fix**: add `math="1"` to `<mxGraphModel>` and use LaTeX delimiters in labels:
  - `\(\hat{K}\)`, `\(c(\hat{K})=0\)`, `\(\mathcal{D}: (\xi, g) \mapsto \hat{K} \in \mathcal{K}\)`, `\(\mathcal{M}[\phi(x)] \leftarrow \hat{K}\)`
- BMP Greek letters `π φ ξ` and symbols `↦ ⇒ ∈` render fine as plain text — no need to wrap them in `\( \)`.
- **Note**: once `math="1"` is on, keep **Extras → Mathematical Typesetting** enabled when editing later in the desktop app, otherwise `\( \)` shows up as raw text.

---

## 3. Typography tiers (font / size / weight / color)

| Tier | Size | Bold | Color |
|---|---|---|---|
| Region / phase caption | 14 | yes | grey `#595959` |
| Module title ×N | 14 | yes | black |
| Body / sub-module | 12 | no (sub-module title bold) | black |
| Edge label / floating small text | 11 | no | black |

- **One global font** (default Helvetica). Copy/paste in the desktop app often sneaks in `font-family: "Google Sans"` and the like — strip it.
- Don't color **only part of a line** (manual edits often leave a stray `<span style="color:...">`).
- Checklist: are size / weight / color / font consistent across same-tier elements? Is any single label accidentally bolded or recolored?

---

## 4. Color logic: color by ROLE category — no clashes, no overloading

Example semantic palette (adapt the roles to your method):

| Color | Meaning | Examples |
|---|---|---|
| Grey (solid `#666666`) | External given | object instance, task prior |
| Blue `#dae8fc/#6c8ebf` | Observation / perceptual data | observation, history |
| Green `#d5e8d4/#82b366` | Produced output | distilled result, execution |
| Purple `#e1d5e7/#9673a6` | Core module | the method's main module |
| Yellow `#fff2cc/#d6b656` | Storage | memory + write edge |
| Orange `#ffe6cc/#d79b00` | Learned controller | policy |
| Grey dashed box `#f7f7f7/#b3b3b3` | Phase grouping background | region containers |

Principles:
- **Map color to a "role category"** (external input / data / module / output / storage), not a random color per box, so the reader can infer role from color.
- **Avoid clashes**: don't give a grouping container the same border color as a functional module, or the background frame reads as a module. **Backgrounds/grouping always use neutral grey; reserve saturated colors for actual functional modules.**
- **Same category, same style**: e.g. two external givens should both be solid grey, not one solid + one dashed.
- **Don't overload one cue**: if dashing means three things at once ("external input / grouping container / write op"), narrow it to one or two clear meanings (e.g. just "grouping container" and "write edge").

---

## 5. Pitfalls introduced by desktop-app editing

Each save in the draw.io desktop app (`host="Electron"`) tends to introduce:
- **An extra page**: exporting the figure to SVG and pasting it back as "page 2" makes the PDF two pages → delete the stray page, or export with `--page-index 0`.
- **Reordered attributes / rewritten labels**: a label like `De-redundified` once got fat-fingered into `e-redundified`, and half a line got wrapped in a coloring `<span>` — **always re-Read the file before doing exact source-string replacements.**
- **Injected `font-family` and `light-dark(...)` colors**: the desktop app writes dark-mode-aware `light-dark(light, dark)` colors and explicit fonts; keep them consistent.

---

## 6. Architecture-figure design principles

- **Reuse modules, don't duplicate**: if a "first time" and "repeat" path each redraw the same Policy/instance with an empty middle, rework into a **single shared hub + single Policy + a loop**, with the two phases as branches off the hub — more compact and more accurate.
- **Don't invert causality (chicken-and-egg)**: if a policy "observes first, then acts," observations must flow from the **environment** into the policy — not be fed back from its own output, which creates a false cycle. Draw multiple inputs (e.g. `\(o_t, h_t, \hat{K}\)`) explicitly converging into the module.
- **Put the signature formula on the box**: place a module's formal signature under its title (e.g. `\(\mathcal{D}: (\xi,g)\mapsto\hat{K}\in\mathcal{K}\)`) — high information density and faithful to the paper.
- **Balance the layout**: put one entity bottom-left and one bottom-right so neither side feels empty.
- Keep components to **3–4 main modules** (the F2 sweet spot in `figures-tables-playbook.md`); 5+ overflows working memory.

---

## 7. Arrow (edge) conventions

- **Uniform width**: all edges `strokeWidth=2`. The default 1px makes both lines and arrowheads look thin in print; 2px reads cleaner and more solid.
- Distinguish special edges by **color/dashing**, not thickness (e.g. write edge = yellow `#d6b656` + dashed), **not** by being thicker.
- Give every edge `edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto` for tidy orthogonal routing.
- When a node has multiple connections, spread the connection points around its perimeter via `exitX/Y` and `entryX/Y` so lines don't stack.
- Arrows must point in the **correct causal direction** and ideally not cross (reorganize the layout to avoid crossings).

---

## 8. One-line cheat sheet

> After editing → export single-page PDF with `--crop --border 10 --page-index 0` → self-check by reading the PDF; math via `math=1` + `\( \)`; color by role category, backgrounds neutral grey; 4 unified typography tiers; all arrows 2px; always re-Read the source before editing it.
