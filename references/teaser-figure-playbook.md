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

## Step 2 — Compose the image

Design rules that hold across variants:

- **One reading path.** The eye should land on the hero behavior first, then optionally trace the pipeline/montage. Avoid a layout where the reader doesn't know where to look.
- **Show the embodiment.** Embodiment is part of the experimental claim — the robot (Franka, Unitree G1, ANYmal-D, Stretch RE-1…) should be visible and recognizable, not abstracted away.
- **Show the deployment context.** Real-world / in-the-wild / indoor-and-outdoor framing signals that every claim is conditioned on transfer. Make the environment legible.
- **Multi-panel → label the panels.** If the teaser splits into regions, use a single panel-notation system (`Left:/Right:`, `(a)/(b)`) and decode it in the caption. Pick one notation system for the whole paper.
- **Color is a naming device.** If the teaser color-codes method vs. baseline or task categories, that mapping must be disclosed in the caption (see Step 3, ingredient 7).
- **Numbered steps for pipelines.** When the teaser walks through a sequential procedure, number the steps in the image and mirror them in the caption (e.g., RoboCook's 9-step dumpling sequence).

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

## Step 4 — Reference the teaser in the Intro

The teaser must be **pointed to from prose**, in paragraph 1 or 2 of the Introduction — the early reference invites the reviewer's abstract → Fig. 1 → contributions scan path explicitly. Use one of:

- `(see Fig. 1)` — most terse
- `As an example (Fig. 1), ...`
- `Figure 1 illustrates how our system works.`
- `In this paper, we propose ... (Figure 1).`

Forward reference (figure number **before** the description) is the default everywhere in the paper.

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

---

## Quick-reference

| User says | Action |
|---|---|
| "What should my teaser show?" | Pick a variant (Step 1): montage / pipeline+punchline / collage / single shot. |
| "How long is the Fig. 1 caption?" | 3–6 sentences. |
| "What goes in the caption?" | Name → value prop → panel pointers → scale → novelty → video → color (Step 3). |
| "Where do I reference it?" | Intro paragraph 1–2, e.g. `(see Fig. 1)` (Step 4). |
| "My contribution is a generalist policy." | Capability collage. |
| "One iconic behavior carries the paper." | Single dramatic shot. |
| "Is `we` allowed in the caption?" | Yes — modern convention (`We introduce …`). |

---

## Construction checklist

1. **Identify what sells the paper** — one behavior, a generalist suite, a cross-environment capability, or a pipeline.
2. **Pick the variant** (Step 1) that matches.
3. **Compose** with a single reading path, visible embodiment, and legible deployment context (Step 2).
4. **Write the caption** as a promise: name + value prop + optional scale/novelty/video/color (Step 3).
5. **Reference it** from Intro paragraph 1–2 (Step 4).
6. **Sanity check** against the anti-pattern table — especially: no bare label, no undecoded color, no over-promise.
</content>
</invoke>
