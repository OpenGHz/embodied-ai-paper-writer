# Figures & Tables — Operational Playbook

**Purpose**: How to design, caption, and reference figures and tables in an embodied-AI submission.

Use this when the user asks: "Help me write a figure caption", "What figures should my paper have?", "How do I caption a table?", "How do I reference a figure?", "How long should my caption be?"

---

## Step 1 — Pick the right figure type for the role

Embodied-AI papers cluster figures into 8 recurring roles. The role determines caption length, prose style, and reference pattern.

| ID | Figure type | Role | Page placement | Sentence count |
|---|---|---|---|---|
| **F1** | Teaser (Fig. 1) | Sell the paper in one image | Top of page 1, often full-width | 3–6 |
| **F2** | System / architecture diagram | Show method components and information flow | First page of Method | 3–6 |
| **F3** | Hardware photo | Document robot, sensors, dimensions | Setup section or appendix | 1–3 |
| **F4** | Task definitions / initial states | Show evaluation tasks and randomization | Experiments section | 1–3 |
| **F5** | Qualitative rollouts / sequences | Show robot executing tasks step by step | Experiments / Results | 2–4 |
| **F6** | Quantitative plot (curves, bars) | Report numbers visually | Results section | 2–4 |
| **F7** | Ablation visualization | Show component impact | Results section | 2–3 |
| **F8** | Failure cases | Demonstrate intellectual honesty | Discussion or appendix | 2–3 |

**Universal expectation**: every embodied-AI paper has at least F1 (teaser), F2 (architecture), F3 (hardware), F4 (tasks), and either F6 (plot) or a results table — **never both for the same dataset**.

---

## Step 1b — One representation per dataset (dedup gate)

**Hard rule**: a single dataset (e.g., "5 tasks × 2 conditions × chain accuracy") must appear in exactly ONE of {figure, table} in the main body. Duplicating the same numbers as both a bar chart and a table wastes page budget and signals to reviewers that the authors padded the paper.

**Decision heuristic — figure vs table**:

| Choose **table** when | Choose **figure** when |
|---|---|
| Exact fractions matter (e.g., 14/15 = 0.933) | Trend/shape matters more than exact numbers |
| Downstream tables reference these numbers | The visual pattern (gap, non-monotonicity) is the claim |
| Few conditions (≤5 rows × ≤5 cols) | Many conditions where a heatmap/curve reveals structure |
| Per-condition annotations needed (e.g., "(proprio)") | Color/position encoding adds information text cannot |

**Corollary**: if a figure and a table show the same data with the same granularity, delete the figure (tables are more information-dense and serve as citable reference sources). Keep the figure only if it reveals a pattern that the table cannot (e.g., a training curve's shape, a spatial heatmap).

**Appendix exception**: an appendix may show a detailed table whose main-body counterpart is a summary figure — but only when the appendix table adds rows/columns not in the figure (e.g., per-seed breakdown). If the appendix table is a strict superset, the main-body figure is redundant.

---

## Step 2 — Write the teaser (Figure 1) as a promise

The teaser is read first by every reviewer; its caption names the system, states the headline capability, and optionally flags scale/novelty/video — 3–6 sentences.

**For the full teaser playbook, see `teaser-figure-playbook.md`** — the four visual variants (deployment montage / pipeline+punchline / capability collage / single dramatic shot), image composition, the caption-as-promise ingredient list, the Intro reference, and teaser-specific anti-patterns.

---

## Step 3 — Write architecture figure caption (F2) as a mini-method-abstract

The architecture figure is referenced 5–15 times across the paper. Its caption is dense:

**Caption template**:
> `{Method Overview / SystemName architecture}. The architecture consists of {N} key components: (1) a {component A} that {action verb}, (2) a {component B} that {action verb}, and (3) the {component C} that {action verb}. {How the components connect / data flow}. {Optional: training-time vs inference-time distinction}.`

**Active verbs for data flow**: `takes ... as input`, `extracts`, `maps`, `encodes`, `predicts`, `outputs`, `passes`, `aggregates`.

**Component count rule**: 3–4 components is the sweet spot. If you have 2, the diagram looks bare. If 5+, reviewers can't hold the diagram in working memory.

**To actually build the architecture diagram** (vector, in draw.io — export, MathJax labels, color-by-role, arrow conventions), see `drawio-figure-playbook.md`.

---

## Step 4 — Write hardware photo caption (F3) as a reproducibility contract

Captions for hardware photos:

- Title: `Hardware Details.` / `Hardware setup and coordinates.`
- Panel labels: `Left: ... Middle: ... Right: ...` or `Top: ... Bottom: ...`
- Specific SKUs, dimensions in metric units, control rates:
  - ✓ `Realsense L515 LiDAR camera`, `Unitree G1`, `Stretch RE-1`, `ViperX 300`, `Intel NUC`
  - ✓ `65 cm / 200 cm`, `100 cm from the base`, `$32k including onboard power and compute`
- Component lists, often numbered when there are many tools/parts: `(1) large roller, (2) circle press, (3) circle punch ...`

The hardware figure is the reproducibility contract — another lab should be able to rebuild your rig from this caption.

---

## Step 5 — Write task-definition caption (F4) as an evaluation contract

```
Task Definitions / Experimental Tasks. We illustrate {N} tasks: {task A}, {task B}, .... For each task, we describe randomization and sub-task definitions. {Optional: layout hint, e.g., "These images are arranged sequentially in time from top to bottom."}
```

**Critical rule**: every task name in the figure must appear identically across figure, table, and prose. Mobile ALOHA defines 7 tasks ("Wipe Wine", "Cook Shrimp", "Rinse Pan", "Push Chairs", "Call Elevator", "Use Cabinet", "High Five") in Fig. 3, and every later table uses these exact names.

**To build a task-gallery figure** (per-task init + operation screenshots in grouped rows, e.g. simulator vs. real-robot), use the config-driven generator `tools/task_gallery_figure.py` (YAML config: `tools/task_gallery.example.yaml`) — it lays out one row per task, init-first then operations, with sub-captions.

---

## Step 6 — Write qualitative rollout caption (F5) as a sequence story

Rollouts are multi-frame grids. Caption ingredients:

- **Frame-direction hint**: `(left to right)`, `(top to bottom)`, `key frames`, `snapshots`
- **Row identification** when comparing trajectories or conditions:
  > `Top row: the policy stands from a seated position. Second row: the policy walks up a flight of stairs. Third row: the policy walks down. Bottom row: the policy walks over a kerb.`
- **Color overlays decoded**: `The trajectory of the target is shown in green and that of the agents is shown in blue.`

When the rollout demonstrates emergent behavior, the caption explicitly names it: `These emergent behaviors showcase the spatial reasoning of our controller.`

---

## Step 7 — Write quantitative plot caption (F6) with mandatory statistical disclosure

A plot caption MUST disclose three things:

| Disclosure | Example |
|---|---|
| **What's plotted** | `Mean success rate of our method vs. four baselines.` |
| **How aggregated** | `Mean ± StdErr across 4 tasks, 10 evaluations each.` / `Results averaged over three seeds.` / `Shaded regions indicate ±1 standard deviation across 10 seeds.` |
| **Takeaway sentence** | `Our parkour policy shows the best performance using only sensors that are available in the real world.` |

**Required elements** (skip any and reviewers will flag):
1. Statistic shown (mean / median)
2. Variability measure (StdErr / std / 95% CI / IQR)
3. Sample size (rollouts / seeds / evaluations / tasks)

---

## Step 8 — Pick panel notation and use it consistently

Three competing systems coexist. **Pick one per paper.**

| System | Used by | When to pick |
|---|---|---|
| `(A)/(B)/(C)` capital letters | Science, ICRA | Formal venues |
| `(a)/(b)/(c)` lowercase | CoRL, RSS, IROS | Default for CoRL/RSS |
| `Left:/Right:/Top:/Bottom:` | Casual spatial layout | When 2 panels and layout is obvious |

Within a single paper, one system applies consistently. **Recommendation**: default to lowercase `(a)/(b)` for CoRL/RSS; reserve spatial labels for 2-panel figures.

---

## Step 9 — Use bolded micro-labels inside multi-row captions

When a caption has multiple sub-claims, bold short phrases to chunk it visually:

> `**Left**: A user teleoperates to obtain food from the fridge. **Right**: Mobile ALOHA can perform complex long-horizon tasks with imitation learning.`

> `**Top**: Trajectories estimated by our model and baselines. **Bottom left**: We collect data in the office using our own payload with the ZED-X camera. **Bottom right**: samples of TartanAir v2 test dataset.`

This pattern is especially common in multi-row qualitative panels where each row needs its own micro-explanation.

---

## Step 10 — Pick caption length to match figure role

| Figure role | Sentence count |
|---|---|
| F3 hardware setup, F4 task list, appendix | 1 sentence |
| F5 qualitative, F7 ablation | 2 sentences |
| F2 architecture, F6 main results plot | 3–4 sentences |
| F1 teaser, complex multi-panel results | 5+ sentences |

**Rule of thumb**: longer captions tend to enumerate panels with `(a)/(b)/(c)` markers. Without panel markers, captions stay ≤3 sentences.

---

## Step 11 — Decide self-contained vs pointer caption

Two coexisting styles:

| Style | Reads without prose? | When to use |
|---|---|---|
| **Maximalist (self-contained)** | YES | Main results, key contribution figures, anything reviewers might skim to first |
| **Minimalist (pointer)** | Needs prose | Setup photos, obvious sequences, appendix figures |

**Default recommendation**: lean maximalist for top venues. Reviewers often skim main results figures first — a self-contained caption increases the chance the claim lands.

---

## Step 12 — Disclose color and legend in prose

Even when the figure has its own legend, the caption duplicates the mapping in prose:

- `The black arrows denote the moving direction.`
- `Red dots indicate height samples given as input to the policy. Blue dots show the controller's internal estimate of the terrain profile.`
- `Blue environments are high-equivariance tasks; green environments are intermediate-equivariance tasks; red environments are low-equivariance tasks.`
- `Solid line: human-in-the-loop; dashed line: offline learning on data from our method.`

**Rule**: color/line-style encoding is never left for the reader to infer. When 4+ baselines, the caption explicitly lists colors. When 2–3, the figure legend suffices.

---

## Step 13 — Use "we" voice in captions

Authors freely use first person in modern embodied-AI captions:

- `**We** present a framework for learning parkour skills...`
- `**We** introduce Co-Painting as a task ...`
- `**We** evaluate OpenVLA and prior state-of-the-art generalist robot policies ...`
- `**Our** parkour policy shows the best performance...`

The we/our voice signals authorial perspective on results, NOT neutral observation. It also lets the caption double as a self-contained mini-claim.

---

## Step 14 — Define symbols inside captions (for math-heavy figures)

When the figure includes notation, define inline:

> `We denote v_x as linear x velocity, v_y as linear y velocity, v_yaw as angular yaw velocity, q as joint positions, q̇ as joint velocities, ... r as roll, p as pitch, c as feet contact indicator, F_feet as forces on feet, and ·^tg as targets.`

This eliminates flip-back to the method section. Common in reward tables and state-space diagrams.

---

## Step 15 — Walk through pipelines with numbered steps

For sequential pipelines, caption walks through with numbered steps:

> `The robot (1) cuts the dough to an appropriate volume, (2) pinches the dough and regularizes the shape, (3) presses to flatten the dough, (4) rolls to flatten the dough further, (5) cuts a circular dumpling skin, (6) removes the excess dough, (7) picks and places the skin onto the mold, (8) adds the filling, and (9) closes and opens the mold.`

---

# TABLES

## Step 16 — Write table caption as TAKEAWAY, not just label

The strongest tables have a caption that states the headline finding in bold:

- `**Co-training improves ACT performance.** Across 7 challenging mobile manipulation tasks, co-training with static ALOHA dataset consistently improves the success rate (%) of ACT.`
- `**Our perception-aware MPC improves the line visibility on average by 40%.**`
- `**Our method outperforms all baseline methods in these metrics by a large margin.**`

**Pattern**: lead with the takeaway in bold (or italicized), then provide context. A reader who scans only table captions should still get the claims.

---

## Step 17 — Mark your method in the table

Conventions for marking the author's method:

| Convention | When to use |
|---|---|
| Row label `**Ours**` | Most common; universal in CoRL/RSS |
| System name (`OpenVLA`, `RoboCat`) with bold | When you've established the brand earlier in the paper |
| Separator row above the method | When grouping with ablations |

**Rule**: the last row is usually "ours" and bolded. The reader's eye trains to look there for the headline number.

---

## Step 18 — Bold the best result per column/row

Standard practice:
- **Best result per column is bolded.**
- When error bars overlap, multiple entries may be bolded; explain in caption: `we bold the mean success rate for both due to overlapping error bars.`
- Underlines occasionally mark second-best.
- Convention disclosure: `Bold performance indicates the best, bold difference is greater than 10%.`

---

## Step 19 — Show parenthetical deltas

When comparing to a baseline, show the difference in parentheses, often color-coded:

> `Number in parentheses shows the difference between our method and the best baseline (with increment colored in blue and decrement in red). Bold performance indicates the best, bold difference is greater than 10%.`

> `We color relative increases of more than 25% from uniform green and relative decreases of more than 25% red.`

This lets the reader scan deltas without arithmetic.

---

## Step 20 — Add ↑/↓ arrows to column headers

For each metric column, add direction tag:
- ↑ for "higher is better" (success rate, return, accuracy, throughput)
- ↓ for "lower is better" (tracking error, cycle time, latency, memory)

Increasingly required in CoRL/RSS reviews.

---

## Step 21 — Order baselines for narrative effect

Three common orderings:

| Order | Effect |
|---|---|
| Chronological (oldest first, ours last) | Story of field progression |
| Worst-to-best (ours best, last) | Builds drama; reviewer's eye lands on ours |
| By method family (model-based → learned → ours) | Categorical comparison |

The last row should be "ours" — train the reader's eye there.

---

## Step 22 — Use multi-block tables with horizontal separators

For ablation tables with >5 rows, split into blocks separated by `\midrule`. Caption explicitly enumerates blocks:

> `(a) HIL-SERL against imitation learning baselines. (b) HIL-SERL against various other baselines.`

> `(a) ablation studies on design choices for scaling up model capacity; and (b) the real-world results, on two different embodiments.`

Essential for multi-axis ablation tables.

---

## Step 23 — Use ± notation universally

- Cells: `1.14 ± 0.30`, `0.99 ± 0.05`
- Caption: `We report mean success rate ± StdErr for each policy.`
- `N/A` for cells where method failed (with reason in caption)
- `—` (em dash) when comparison was not performed

---

# Prose ↔ Figure / Table reference patterns

## Step 24 — Use forward references for new figures

The default: introduce the figure number BEFORE describing what it shows.

- `We illustrate 6 real-world tasks that Mobile ALOHA can perform autonomously **in Fig. 3**.`
- `**Fig. 2** shows the network architecture...`
- `**As shown in Fig. 5**, the policy adapts to ...`
- `**See Fig. 7 for** illustrations of all tasks.`

---

## Step 25 — Use parenthetical references for supporting evidence

When the figure is supporting evidence rather than the focus:

- `...resulting in a ground sampling distance (GSD) of 1 mm/px (**see Fig. 3**)`
- `...the robot adjusts the orientation in the first few steps (**Fig. 6**)`
- `...demonstrates that our method achieves 80% success rate (**Table 3**)`

---

## Step 26 — Reference specific panels for precision

Top venues reward precise referencing:

- `We see this clearly in **Fig. 7A**.`
- `**Fig. 3(b)** shows the after-optimization view.`
- `As shown in **Fig. 9 (left)** ...`
- `**Table 1(a)** compares against imitation learning baselines ...`

Specificity in citation correlates strongly with venue: CoRL/RSS/Science papers reference exact panels and line colors.

---

## Step 27 — Use the result-anchor rhythm in Results section

In Results paragraphs, follow this rhythm:

1. **Claim**: `Our method outperforms all baselines by a large margin ...`
2. **Quantitative anchor**: `... with a success rate of 85% compared to 42% for the next-best baseline`
3. **Figure pointer**: `(see Table 2).`
4. **Mechanism**: `The improvement is most pronounced on tasks requiring precise contact-rich manipulation, where ...`
5. **Caveat or extension**: `Notably, the method also generalizes to unseen objects (Fig. 7), suggesting ...`

This 5-step rhythm is the standard structure of Results paragraphs in top embodied-AI papers.

---

# Anti-patterns to reject

| Anti-pattern | Fix |
|---|---|
| Same data shown as both figure AND table in main body | Pick one: table if exact numbers matter, figure if visual pattern is the claim. See Step 1b. |
| Vague reference: `Our method works well (see plots).` | Specific: `Our method achieves 87.2% success rate (Fig. 5, blue line) vs. 61.4% for the strongest baseline (orange line).` |
| Caption that only labels: `Goalkeeper task.` for a main results figure | Add takeaway sentence + statistical disclosure |
| Missing statistical aggregation in plot caption | Add `mean ± stderr`, sample size, and aggregation method |
| Mixed panel notation `(A)` and `(a)` within one paper | Pick one and apply consistently |
| Same task with two different names across figure/table | Use identical name everywhere |
| No `**Ours**` marking or bold-best in tables | Add both |
| Color in figure with no prose disclosure | Add `our method (blue)` etc. to caption |
| Failure-case figure presented without diagnostic prose | Add "why it failed" sentence per failure mode |
| Hardware figure missing SKUs/dimensions | List specific products, control rates, dimensions |

---

# Construction workflow

1. **Pick the figure type** (Step 1: F1–F8). Each role has its own length budget.
2. **For F1 (teaser)**: pick a visual variant, then caption as a promise — see `teaser-figure-playbook.md`.
3. **For F2 (architecture)**: decompose into 3–4 components, name each with action verb (Step 3).
4. **For F3 (hardware)**: list SKUs, dimensions, control rates (Step 4).
5. **For F4 (tasks)**: lock task names; use them identically in tables and prose (Step 5).
6. **For F5 (rollouts)**: name rows; provide frame-direction hint (Step 6).
7. **For F6 (plots)**: disclose mean/variability/sample-size triad (Step 7).
8. **For tables**: caption as takeaway (Step 16); bold the best (Step 18); ↑↓ arrows (Step 20).
9. **Choose panel notation system** and apply consistently (Step 8).
10. **For every figure**: write forward reference in prose before the figure (Step 24).
11. **For Results section**: use the 5-step result-anchor rhythm (Step 27).

---

# Quick-reference

| User says | Action |
|---|---|
| "How long should my caption be?" | F1/F2: 3–6 sentences. F5/F7: 2 sentences. F3/F4/appendix: 1 sentence. |
| "Should I bold the best result?" | Yes, per column. When tied, bold both with a footnote. |
| "Should I use `(A)` or `(a)`?" | CoRL/RSS: `(a)`. Science: `(A)`. Pick one per paper. |
| "How do I caption a plot with error bars?" | Disclose mean, variability, sample size — all three. |
| "Is `we` allowed in captions?" | Yes — modern convention. |
| "How do I reference a specific panel?" | `Fig. 7A` / `Fig. 3(b)` / `Fig. 9 (left)`. |
| "Should the caption have the takeaway?" | Yes for main results. Optional for setup figures. |
| "My method is called X — how do I mark it in tables?" | Last row labeled `**Ours**` or `**X**`; bolded headline number. |
| "Should I show a failure case?" | Yes, with diagnostic prose per failure mode. |
