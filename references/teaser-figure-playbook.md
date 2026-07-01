# Teaser Figure (Figure 1) — How to Draw It

**Purpose**: How to design, lay out, caption, and reference the teaser — the single image (Fig. 1) that sells an embodied-AI paper.

Use this when the user asks: "How do I design my Figure 1?", "What should my teaser show?", "How do I make a good teaser figure?", "How do I make a graphical abstract / visual abstract?", "What goes in the Figure 1 caption?", "Where do I put / reference the teaser?"

> Scope: this file is about F1 (the teaser) only. For all other figure roles (architecture, hardware, tasks, rollouts, plots, ablations, failures) and for table conventions, see `figures-tables-playbook.md`.

---

## A note on naming: "teaser" vs. "graphical abstract"

**"Teaser"** is the informal community term, dominant in robotics / vision / ML venues (CoRL, RSS, CVPR, NeurIPS) for the Figure 1 that sells the paper. The more formal, **journal-facing name is "graphical abstract"** (also "visual abstract" or "graphical TOC entry") — the term Elsevier, Cell Press, IEEE journals, and Science/Nature-family venues use for the single image that visually summarizes a paper's contribution.

They denote the **same artifact** — a self-contained image conveying the paper's headline at a glance — so this playbook applies to both. A few differences in emphasis worth knowing:

- **Where it appears**: a teaser is in-paper (top of page 1). A graphical abstract is often *also* a separate submission asset shown in the table of contents, the article landing page, and search results — so it must read at thumbnail size, outside the paper's context.
- **Formatting constraints**: journals that require a graphical abstract usually impose hard specs (fixed dimensions/aspect ratio, e.g. Elsevier's 1328×531 px or square; minimum font size; no unexplained abbreviations). Check the target venue's author guide before drawing.
- **Self-containment**: because it travels outside the paper, a graphical abstract leans even more maximalist — it should be legible with zero surrounding prose.

**Practical rule**: design the image once using the variants and composition rules below. If the target venue asks for a "graphical abstract," reuse the teaser but re-check it against the venue's size/font specs and confirm it survives at thumbnail scale.

---

## Why the teaser matters

The teaser is **read first by every reviewer** — often before the abstract is finished and almost always before the method. A reviewer who reads only the abstract + Figure 1 + the contributions list should come away with a correct mental model of the paper. The teaser is a **promise**: it states the headline capability the rest of the paper must deliver.

Placement: top of page 1, almost always full-width, sometimes spanning columns. Caption length: **3–6 sentences** (one of the two longest captions in the paper, alongside the architecture figure).

**Universal expectation**: every embodied-AI paper has at least F1 (teaser), F2 (architecture), F3 (hardware), F4 (tasks), and either F6 (plot) or a results table.

---

## Step 1 — Pick the visual variant

The teaser's composition follows one of four recurring layouts. Pick by what carries the paper.

| Variant | When to use | Corpus examples |
|---|---|---|
| **Deployment montage** — the robot performing the headline behavior in 2–6 environments | Capability **generalizes across scenes** | Mobile ALOHA Fig. 1 (food-from-fridge + long-horizon task), Extreme Parkour Fig. 1 (long jump + high jump + handstand), ANYmal Fig. 1 ("Robust locomotion in the wild" — slippery, steep, snow, cave) |
| **Pipeline diagram + punchline image** — split layout: system schematic on one side, deployment photo on the other | Method **needs explanation AND** a "look, it works" shot | RoboCook Fig. 1 (9-step dumpling sequence), VideoMimic Fig. 1 (real-to-sim-to-real pipeline) |
| **Capability collage** — small grid of qualitatively diverse tasks | The contribution is a **generalist policy / system** | OpenVLA Fig. 1, RoboCat Fig. 1, RoboAgent Fig. 1 |
| **Single dramatic shot** — one image of the most striking behavior | **One iconic behavior** carries the paper | EUREKA Fig. 1 ("for the first time, unlocks rapid pen-spinning capabilities on an anthropomorphic five-finger hand") |

**Decision heuristic**:
- Generalist system across many tasks → capability collage.
- Single hero behavior → single dramatic shot.
- Capability that travels across environments → deployment montage.
- Method whose pipeline is itself a selling point → pipeline + punchline.

---

## Step 2 — Compose the image (visual-style standards)

### Core principles

- **Complementarity with the architecture figure.** The teaser builds intuition; the architecture figure (F2) shows technical completeness. Avoid content overlap — the teaser is not a shrunken architecture diagram. See "Teaser vs. architecture" below.
- **One reading path.** The eye should land on the hero behavior first, then optionally trace the pipeline/montage. Avoid a layout where the reader doesn't know where to look.
- **Show the embodiment.** Embodiment is part of the experimental claim — the robot (Franka, Unitree G1, ANYmal-D, Stretch RE-1…) should be visible and recognizable, not abstracted away.
- **Show the deployment context.** Real-world / in-the-wild / indoor-and-outdoor framing signals that every claim is conditioned on transfer. Make the environment legible.
- **Multi-panel → label the panels.** If the teaser splits into regions, use a single panel-notation system (`Left:/Right:`, `(a)/(b)`) and decode it in the caption. Pick one notation system for the whole paper.
- **Numbered steps for pipelines.** When the teaser walks through a sequential procedure, number the steps in the image and mirror them in the caption (e.g., RoboCook's 9-step dumpling sequence).

### Visual complexity rule: minimal text, at most 1 formula

**❌ Do not include:**
- Large block titles or dense paragraphs
- Dense formula derivations or multiple equations
- Technical detail stacks (module internals, data-flow minutiae)
- Architecture-diagram module boxes and arrows (those belong in the F2 architecture figure, not the teaser)

**✅ Keep only:**
- **A single core formula** (only when that formula *is* the method's unique identifier — e.g. a one-line update rule that captures the whole contribution). If you're unsure whether it's "the core formula," omit it.
- Visual, vivid concept illustration
- Linear narrative structure (problem → method → effect)
- Concrete visual example scenarios

### Mandatory negative constraints — write these into the `generation_prompt` verbatim

Image models render *whatever text they see in the prompt*: leave a long descriptive clause, a heading, or a stray `[cite: 12]` in the brief and it gets **painted into the figure** as literal text (observed failure: an entire teaser overrun by prompt sentences and citation markers). So the `generation_prompt` must not only describe the picture — it must **explicitly forbid** the model from adding text the figure should not contain. Include all three of these instructions, near the top of the prompt, in these words or close to them:

1. **Pure English only.** `ALL text in the figure must be in ENGLISH — no Chinese or any other language, anywhere.` (The paper is English; the renderer may otherwise drift to the language of the surrounding conversation. This restates `image-render-invocation.md` rule 4 *inside the prompt* so the model obeys it, not just the operator.)
2. **No title text baked into the image.** `Do NOT render any title inside the figure — no paper title, no figure/caption heading, no section header. The title and caption live in the LaTeX, not in the raster.` (A title drawn into the teaser duplicates the `\caption{}` and cannot be edited later; it is the single most common leak.)
3. **No prose, no prompt text, no metadata.** `Use only short label words on the objects and arrows — no sentences, no paragraph descriptions, no bullet lists, and never transcribe these instructions, notes, or citation markers (e.g. "[cite: N]") into the image.` (Keep every in-figure label to a few words; move all explanation to the caption.)

**Keep the brief itself lean.** The more descriptive prose and the more embedded label strings the `generation_prompt` carries, the more the model treats as text to paint. Give the *layout and the short label words*, not full sentences the model can copy. If you must list exact label strings, keep each to ≤4 words and mark them clearly as labels — do not wrap them in explanatory clauses the model will render verbatim.

### Results in the teaser: show comparison visually, not numerically

**❌ Do not write numeric results by default** — no `Accuracy: 92.3%`, `Operations: 150 → 90`, or table-style performance summaries. The teaser is not a mini-results section.

**✅ Show advantages through visual contrast:**
- Baseline vs. Ours side-by-side screenshots
- Operation-count reduction shown via fewer arrows or a shorter pipeline
- Success/failure states in direct visual comparison
- Before/after juxtaposition

### Image style: 3D photoreal rendering

For the **pipeline+punchline** and **single-shot** variants, use high-quality 3D-rendered robots and objects with realistic lighting/textures. Place abstract concepts into concrete interaction scenes.

- **3D photoreal rendering**: the robot, objects, and environment use high-quality 3D models with rich detail, realistic surface materials, and lighting/shadows.
- **Scenario-based presentation**: situate the abstract concept in a specific interaction scene (e.g., a robot manipulating a cabinet, not a floating abstract box labeled "cabinet").
- **Detail-rich**: preserve object realism, textures, and lighting cues — avoid simplistic clip-art or stick-figure schematics.

For schematic/pipeline regions that must stay diagrammatic (e.g. a flow overlay or a conceptual decomposition), the draw.io vector path (`drawio-figure-playbook.md`) is the clean alternative — but keep schematics minimal and favor the photoreal scene for the main narrative.

### Represent meaningful modules with evocative icons, not plain boxes

A module that carries a **specific meaning** — the perception encoder, a frozen VLM, the memory store, the policy, the camera/observation stream — must be drawn as an **icon that depicts what it does**, not as an anonymous labeled rectangle. A row of identical boxes reading `VLM` / `Memory` / `Policy` forces the reader to parse text to recover meaning the picture should have carried; it also reads as a shrunken architecture diagram (F2 leak). An evocative icon is understood pre-linguistically, survives thumbnail scale, and keeps the teaser at the *intuition* altitude.

Map each meaningful module to a **conventional, instantly-legible glyph**, then keep the short text label *beside* the icon (not replacing it):

| Module / concept | Evocative icon (examples) |
|---|---|
| Frozen / off-the-shelf model | a snowflake ❄ on the model glyph (frozen), a padlock for "not trained" |
| VLM / LLM / neural encoder | a small chip / brain / network glyph — not a bare box |
| Memory / store / database | a database cylinder, a labeled drawer, a card-index |
| Camera / observation / video | a lens/aperture, a filmstrip, an eye |
| Policy / controller | a robot-arm silhouette, a joystick, a gamepad |
| Retrieval / key-match | a magnifier over a key, two puzzle pieces meeting |
| Reward / score | a target, a gauge, a trophy |

**Exceptions** (plain rectangles are fine): a **neutral grouping container** (a grey background region that just bundles a stage — ⬜ per the 5-color system), and a **short action/data token** on an arrow (`[open-door]`) whose job is to be read as text. The rule targets *semantic modules* masquerading as generic boxes, not every rectangle on the canvas.

This composes with the photoreal rule above: the robot/objects are photoreal, and the light schematic overlay uses **meaningful icons** for its modules — neither should collapse to plain boxes.

### 5-color semantic system (status + structure)

Use a **multi-color status tagging system** with fixed role-to-color mapping (disclosed in the caption per Step 3, ingredient 7):

| Color | Meaning | Examples |
|---|---|---|
| 🟠 **Orange** | Failure, error operation, parts needing improvement | failed grasp, incorrect trajectory, redundant step |
| 🔵 **Blue** | Intermediate step, processing, data flow | observation stream, in-progress module, trace |
| 🟢 **Green** | Success, final result, optimized state | successful execution, final distilled output |
| ⬜ **Grey** | Title bars, background regions, grouping containers | phase labels, section dividers |
| 🟡 **Yellow** | Highlight key element, storage/memory module | the distilled knowledge, the memory lookup |

Principles:
- **Color maps to role category** (input / processing / success / failure / storage), not a random hue per panel, so the reader can infer meaning from color.
- **Survives grayscale + scaling** — don't let color be the *only* carrier of a distinction; reinforce with shape, position, or label.
- **Avoid clashes**: backgrounds/grouping always use neutral grey; reserve saturated colors for functional states.

### Arrows (for pipeline/schematic regions) — the most error-prone element

- **Thick strokes, large arrowheads, dark color** — the default 1px thin arrow looks weak in print; use ≥2px.
- **Label important arrows** with what flows through them (e.g., `observation`, `\(\hat{K}\)`).
- **Route to avoid crossings** — reorganize layout to keep flow paths clear.
- **Point in the correct direction** — arrows must respect causality (observation → policy, not policy → observation).

### Tasteful, paper-ready styling

- **Clean background, clean type** — white/near-white background, sans-serif labels (Arial/Helvetica) at a readable size with a clear size hierarchy (main modules larger, secondary smaller). No tiny unreadable text.
- Subtle same-family gradients and restrained rounded corners are fine.
- **Avoid**: rainbow gradients, heavy drop shadows, 3D perspective text, glow effects, clip-art icons, and slide-deck styling. Aim for *paper-ready, not slide-ready*.

### Visual layout hierarchy

Use these cues to distinguish primary vs. secondary information:
- Color contrast (status colors vs. grey backgrounds)
- Size difference (larger = more important)
- Position (center = core innovation; edges = input/output; corners = supplementary notes)
- Visual weight (bold vs. regular, filled vs. outlined)

**Visual flow**: linear (left → center → right, or top → down) guides the reader's eye along the method's logic. **White space**: ensure key information isn't drowned; maintain clear visual gaps between modules; avoid information overload.

### Teaser vs. architecture figure (F2)

| Dimension | Teaser | Architecture (F2) |
|---|---|---|
| **Goal** | Build intuition, attract readers | Show technical completeness |
| **Content** | Core concept + visual example | Module details + data flow + formulas |
| **Style** | Photoreal rendering, vivid, concrete | Box-and-arrow diagrams, abstract, rigorous |
| **Formulas** | At most 1 core formula | Full mathematical derivation |
| **Results** | Optional visual comparison | Experimental data table when needed |
| **Detail level** | High-level concept | Implementation details |

**互补原则 (complementarity rule)**: the teaser and the architecture figure must *complement*, not duplicate. If your teaser draft looks like a miniature architecture diagram (many boxes, many arrows, data-flow annotations), you're leaking F2 content into F1 — pull back to the high-level concept and leave the technical breakdown for the method figure.

---

## Step 3 — Write the caption as a promise

The teaser caption shares a fixed structure across the corpus. Include these ingredients **in this order** (items 3–7 are optional, used as the figure warrants):

1. **System name** in bold or small caps — `**OpenVLA**`, `**Mobile ALOHA**`, `EUREKA`. (In PDFs, `\textsc{Poliformer}` renders as spaced small caps "P OLI F ORMER"; the real name is the contiguous form.)
2. **One-sentence value proposition** — `We introduce {SystemName}, a {short noun phrase} that {headline capability}.`
3. **Panel pointers** if multi-image — `Left: ... Right: ...`, `(a) ... (b) ...`
4. **Scale flex** — `trained on 970k robot episodes`, `21 institutions across the globe`, `$32k including onboard power and compute`.
5. **Novelty flag** — `for the first time, unlocks ...`, `the first open-source ...`. (When making a precedence claim in prose, hedge with `To our knowledge`; in the caption the flag can be terser.)
6. **Video / website URL** — `Parkour videos at https://...`, `Videos are on the project website.`
7. **Color / legend disclosure** — if the image color-codes anything: `our method (blue)`, `green = high-equivariance tasks`, etc.

**Caption skeleton**:

> **{SystemName}.** We introduce {SystemName}, a {noun phrase} that {headline capability}. **Left**: {what the left region shows}. **Right**: {what the right region shows}. {Scale flex}. {Novelty flag}. {Video/website pointer}.

**Worked examples from the corpus**:

> "**Left**: A user teleoperates to obtain food from the fridge. **Right**: Mobile ALOHA can perform complex long-horizon tasks with imitation learning." (Mobile ALOHA Fig. 1)

> "EUREKA … for the first time, unlocks rapid pen-spinning capabilities on an anthropomorphic five-finger hand." (EUREKA Fig. 1)

**The "promise" structure** (E2 in the research corpus) — every strong Fig. 1 caption does, in order: (1) name the system, (2) state the headline capability, (3) optionally mention scale, (4) optionally mention novelty, (5) optionally link to videos.

---

## Step 4 — Consolidate everything into `teaser-prompt.yaml`, then gate on approval

**Never jump straight to drawing.** Once the variant (Step 1), composition (Step 2), and caption (Step 3) are decided, write **all** of it into one file — `teaser-prompt.yaml` — that becomes the **single reference** for the teaser. It holds not just the drawing brief but everything the rest of the pipeline needs: the caption, the image output path, the figure label, and the ready-to-paste Intro pointer. The goal: after the image is drawn, you (or another agent) can hand over *just this YAML* and the downstream work — placing the figure, writing the Intro reference (Step 6) — falls out of it with nothing to re-derive.

This is the teaser-specific instance of the skill's PRE-DRAFT CHECKPOINT discipline: lock the whole plan in one cheap-to-edit place before spending effort on pixels.

**Why YAML** (not JSON / prose): structured enough to separate variant / layout / caption / output / generation-prompt fields, yet human-readable and quick to hand-edit during the review loop, and it supports `#` comments for guidance. JSON has no comments and is clumsy to tweak; free prose is hard to revise field-by-field.

**Template**: copy [`teaser-prompt.template.yaml`](teaser-prompt.template.yaml) to `teaser-prompt.yaml` next to the paper (or wherever the user keeps drafts) and fill it in. Every field carries an inline `#` comment explaining it. The fields, in brief:

- `variant`, `rationale` — the Step 1 choice and why.
- `system_name`, `headline_capability` — what the image must convey.
- `layout` (`composition` + per-panel `shows`), `embodiment`, `environment`, `color_coding`, `style` — the Step 2 composition and visual-style standards.
- `generation_prompt` — the actual text handed to the image model or designer.
- `output_path`, `figure_label`, `placement` — where the drawn image lives and how it sits in the paper.
- `caption` — the paste-ready Step 3 promise caption.
- `intro_reference` — the paste-ready Intro pointer (its `\ref{}` must match `figure_label`).
- `render` — the preferred renderer + its availability mode (filled by the check below).
- `venue_constraints`, `review`, `open_questions` — graphical-abstract specs, the draw→review→refine acceptance bar, and anything to confirm first.

**Check the renderer here (before the gate).** Don't wait until Step 5 to discover the API isn't configured — run the config check now and record the result in the YAML's `render` block, so the gate can report whether drawing is actually possible:

```bash
RENDER="${CLAUDE_SKILL_DIR:-$(pwd)}/tools/images_api_render.py"; [ -f "$RENDER" ] || RENDER="tools/images_api_render.py"  # see SKILL.md → Bundled tools
python3 "$RENDER" check --json-out figures/ai_generated/render_check.json
```

Map the `mode` from the verdict into `render:` in the YAML:

- `env` / `codex` / `mixed` → set `render.renderer: images_api_render` and `render.mode: <mode>` (default REST path is usable).
- `unavailable` → set `render.mode: unavailable`. Either switch `render.renderer: codex-image2` (if the MCP bridge is installed) or flag at the gate that the user must configure `GPT_IMAGE2_API_KEY` + `GPT_IMAGE2_API_URL` (or draw by hand). See [`image-render-invocation.md`](image-render-invocation.md) for the full table.

**Then gate**: present the artifact and ask explicitly —

> "Here's the teaser brief (`teaser-prompt.yaml`) — it holds the drawing prompt, caption, output path, Intro pointer, and the renderer status (`render.mode: <mode>`). **Start drawing from this, or adjust first?** Tell me what to change, or say 'draw it'." *(If `render.mode` is `unavailable`, say so here and ask how to proceed.)*

- Wait for `draw it` / `go` / `looks good` before generating any image.
- If the user edits fields or asks for changes, update the YAML and re-present — loop until approval.
- If the user says "you decide" / "use your defaults", proceed, but still write the artifact so the plan is on record.

---

## Step 5 — Draw the teaser from the YAML (quick by default)

Generate the image from `generation_prompt`, honoring `layout`, `embodiment`, `environment`, `color_coding`, `style`, and any `venue_constraints`. Use the renderer recorded in `render` (renderer/model/size/quality) — its availability was already confirmed at the Step 4 gate, so there's no surprise here. Save it to `output_path`. (This playbook supplies the brief and the acceptance bar; the image tool executes the render.)

**To actually call the renderer** (default: the REST adapter `tools/images_api_render.py` → render → finalize → verify; Codex `codex-image2` bridge as alternative), see [`image-render-invocation.md`](image-render-invocation.md). If `render.mode` was `unavailable` and not resolved at the gate, hand the `generation_prompt` to whatever image tool you have, or draw by hand.

**Default: one quick render.** Produce a single image and hand it back — do **not** spin a review-and-refine loop unless asked. Most teasers go through manual tweaking anyway, so a fast first draft is usually what the user wants. Still apply the Step 2 style standards in the prompt so the one shot lands close.

**Opt-in: the review-and-refine loop.** When the user asks to "polish", "iterate", "make it submission-ready", or sets `review.loop: true` in the YAML, run a tight generate → review → refine loop:

1. **Render** a version (`teaser_v1`, `teaser_v2`, …).
2. **Review strictly** against the checklist below and **score 1–10**. Be a hard grader: reject a figure that looks attractive but is logically wrong or unreadable.
3. **Refine** if the score is below `review.target_score` (default **≥ 9**; cap at `review.max_rounds`, ~5). Write *specific, actionable* feedback — say what's wrong, what to preserve, and what to change — never a vague "make it better". Then re-render.

Strict review checklist (use when looping; also a handy one-pass sanity check):

- **10-second understanding test**: can a reader grasp the core innovation in 10 seconds?
- **Complementarity check**: does the teaser avoid duplicating the architecture figure's content (module boxes, data-flow arrows)? Is it high-level concept, not implementation detail?
- All major components / panels present, and the **hero behavior reads first**?
- Embodiment recognizable and deployment context legible?
- Labels readable (and in the right language), with a clear size hierarchy?
- **At most 1 formula** (and only if it's the method's unique identifier — if uncertain, omit)?
- **No numeric results** (Accuracy: X%, Operations: Y → Z) in the teaser body — advantages shown visually via before/after or baseline-vs-ours comparison?
- **No title/caption text baked into the image** (no paper title, figure heading, or section header drawn in the raster — those belong to the LaTeX `\caption{}`)?
- **No leaked prose or metadata** — labels are short words only, with no sentences, paragraph descriptions, or stray prompt text / citation markers (`[cite: N]`) painted into the figure?
- **All in-figure text is English** (no Chinese or other-language drift)?
- **3D photoreal rendering** (not stick-figure or clip-art) for robots/objects/scenes, or clean draw.io vector diagram for the schematic region?
- **Meaningful modules drawn as evocative icons**, not anonymous labeled rectangles (frozen model → snowflake, memory → database cylinder, observation → filmstrip/lens, policy → arm/joystick)? Plain boxes only for neutral grouping containers or short data/action tokens on arrows?
- **5-color semantic system** followed (🟠 failure, 🔵 processing, 🟢 success, ⬜ grey background, 🟡 highlight/memory)?
- For pipeline/schematic regions: arrows thick (≥2px), dark, labeled, non-crossing, and pointing the **right** way?
- Palette survives grayscale and column-width / thumbnail scaling?
- Looks **paper-ready, not slide-ready** — no glow / rainbow / 3D-text / clip-art decoration?
- **Information density**: avoids overload, preserves white space, key info not drowned?
- Matches the `caption`'s promise and the venue's `venue_constraints`?

Example refinement feedback (concrete beats vague):

- `Increase spacing between the teleop panel and the autonomous panel; they read as one scene.`
- `Make the baseline trajectory thinner and gray so ours (blue) dominates.`
- `Relabel "long-horizon manip." → "long-horizon household tasks" to match the caption.`

**The YAML stays the source of truth**: if a render diverges from the brief, fix the brief (or the `generation_prompt`) first, then re-render — never let an off-brief image silently redefine the plan.

---

## Step 6 — Drive the Intro reference (and placement) from the YAML

With the image at `output_path`, the rest is mechanical and reads straight off the YAML — this is the payoff of consolidating in Step 4. Hand the YAML to an agent (or do it yourself) to:

1. **Place the figure** — assemble the figure environment from `output_path` + `caption` + `figure_label`, positioned per `placement`.
2. **Reference it in the Intro** — paste `intro_reference` into Introduction paragraph 1 or 2. The teaser must be **pointed to from prose** early — the reference invites the reviewer's abstract → Fig. 1 → contributions scan path explicitly.

Phrasing options for the Intro pointer (whichever you store in `intro_reference`):

- `(see Fig. 1)` — most terse
- `As an example (Fig. 1), ...`
- `Figure 1 illustrates how our system works.`
- `In this paper, we propose ... (Figure 1).`

Forward reference (figure number **before** the description) is the default everywhere in the paper. The pointer's `\ref{...}` must match `figure_label`.

---

## Anti-patterns to reject

| Anti-pattern | Fix |
|---|---|
| Teaser that only labels (`Goalkeeper task.`) | Add the value-proposition sentence + (if applicable) scale/novelty. The teaser caption is never a bare label. |
| No reading path — reviewer can't tell where to look | Establish one focal hero behavior; arrange panels around it. |
| Embodiment / deployment context hidden or abstracted | Show the actual robot in the actual environment. |
| Color or panels in the image, none decoded in the caption | Add panel pointers and the color→meaning mapping to the caption. |
| Mixed panel notation (`(A)` and `(a)`) vs. the rest of the paper | Pick one notation system and apply it paper-wide. |
| Teaser duplicates a later results figure/table verbatim | The teaser sells the capability; the results figure proves it. Keep them distinct. |
| Unhedged precedence claim in the intro reference (`We are the first ...`) | Hedge with `To our knowledge` in prose; keep the caption novelty flag terse. |
| Promising a capability the paper never demonstrates | The teaser is a contract — only show what the experiments deliver. |
| Accepting a pretty figure that is logically wrong / mislabeled | Score strictly (Step 5); reject on logic/labels/arrows regardless of how attractive it looks. |
| Slide-deck decoration (glow, 3D, rainbow gradients, clip-art, heavy shadows) | Strip to paper-ready: restrained palette, clean type, tasteful at most (Step 2 style standards). |
| A title / caption heading drawn *inside* the image (duplicates the LaTeX `\caption{}`, uneditable) | Add `Do NOT render any title inside the figure` to the prompt; the title/caption live in LaTeX only (Step 2 mandatory constraints). |
| Prompt prose or `[cite: N]` markers painted into the figure as literal text | Keep the brief lean; add `no sentences, never transcribe these instructions or citation markers` to the prompt; labels are short words only (Step 2 mandatory constraints). |
| Non-English text drift (e.g. Chinese labels) when the conversation isn't English | Put `ALL text in ENGLISH only` *inside the prompt*, not just in operator config (Step 2 mandatory constraints; `image-render-invocation.md` rule 4). |
| Thin/hairline or wrong-direction arrows in a schematic region | Thick dark labeled arrows, no crossings, pointing the correct way. |
| Meaningful modules drawn as anonymous labeled rectangles (a row of `VLM`/`Memory`/`Policy` boxes) | Give each semantic module an evocative icon (snowflake=frozen, cylinder=memory, filmstrip/lens=observation, arm/joystick=policy); reserve plain boxes for grey grouping containers and short data/action tokens (Step 2 "evocative icons, not plain boxes"). |

---

## Quick-reference

| User says | Action |
|---|---|
| "What should my teaser show?" | Pick a variant (Step 1): montage / pipeline+punchline / collage / single shot. |
| "How long is the Fig. 1 caption?" | 3–6 sentences. |
| "What goes in the caption?" | Name → value prop → panel pointers → scale → novelty → video → color (Step 3). |
| "Where do I reference it?" | Intro paragraph 1–2, e.g. `(see Fig. 1)` (Step 6). |
| "My contribution is a generalist policy." | Capability collage. |
| "One iconic behavior carries the paper." | Single dramatic shot. |
| "Is `we` allowed in the caption?" | Yes — modern convention (`We introduce …`). |
| "Draw / generate my teaser." | First consolidate `teaser-prompt.yaml` and confirm before drawing (Step 4). |
| "I have the YAML — now what?" | Draw one quick render (Step 5), then drive figure placement + Intro reference off it (Step 6). |
| "Polish / iterate until it's submission-ready." | Opt into the review loop: score 1–10, specific feedback, re-render; accept at ≥ 9 (Step 5). |
| "What style should the figure be?" | Restrained palette, clean sans-serif labels, grayscale-safe, paper-ready not slide-ready (Step 2 style standards). |

---

## Construction checklist

1. **Identify what sells the paper** — one behavior, a generalist suite, a cross-environment capability, or a pipeline.
2. **Pick the variant** (Step 1) that matches.
3. **Compose** with a single reading path, visible embodiment, and legible deployment context. **Apply the visual-complexity rule**: minimal text, at most 1 core formula, no numeric results (show comparison visually instead). **Use 3D photoreal rendering** for robots/objects/scenes, or draw.io vector diagrams for schematic regions. **Follow the 5-color semantic system** (🟠 failure, 🔵 processing, 🟢 success, ⬜ grey background, 🟡 highlight/memory). **Ensure complementarity** with the architecture figure (F2) — the teaser is high-level concept, not a shrunken module diagram (Step 2).
4. **Write the caption** as a promise: name + value prop + optional scale/novelty/video/color (Step 3).
5. **Consolidate `teaser-prompt.yaml`** — variant, layout, caption, generation prompt, output path, figure label, Intro pointer — as the single reference; **run the renderer `check` and record `render.mode`**; then gate on user approval before drawing (Step 4).
6. **Draw** from the YAML to `output_path` — one quick render by default; loop to review-score-refine only on request. Review against the checklist: 10-second understanding, complementarity with F2, no numeric results, 3D photoreal or vector, 5-color system, ≥2px arrows pointing correctly, survives grayscale, paper-ready not slide-ready (Step 5).
7. **Drive the downstream off the YAML** — place the figure, then reference it from Intro ¶1–2 (Step 6).
8. **Sanity check** against the anti-pattern table — especially: no bare label, no undecoded color, no over-promise.
</content>
</invoke>
