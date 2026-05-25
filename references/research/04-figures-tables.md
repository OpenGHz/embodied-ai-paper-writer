# Figures & Tables: Writing Patterns in Embodied AI Papers

> Corpus: 614 captions extracted from 63 top-conference papers (CoRL/RSS/ICRA/IROS/Science 2022–2025).
> Focus: caption craft, figure-type conventions, table conventions, prose↔figure reference patterns.
> Method: pattern induction from `_captions_corpus.md` + sampled in-text references.

This file is for the writer-distillation skill, not technical reasoning. Every pattern below is grounded in actual phrasing from the papers.

---

## A. Figure Type Taxonomy

Embodied AI papers cluster figures into ~8 recurring roles. Recognizing the role determines caption length, sentence structure, and prose reference style.

### A1. The Teaser (Figure 1)

**Role**: Sell the paper in one image. Almost always full-width, near the top of page 1, sometimes spanning columns.

**Variants observed**:
- **Deployment montage** — robot performing the headline behavior in 2–6 environments. Examples: Mobile ALOHA Fig. 1 (food-from-fridge + long-horizon task), Extreme Parkour Fig. 1 (long jump + high jump + handstand), ANYmal-locomotion Fig. 1 ("Robust locomotion in the wild" — slippery, steep, snow, cave).
- **Pipeline diagram with a punchline image** — split layout, system schematic on the left, deployment photo on the right. RoboCook Fig. 1 (9-step dumpling sequence), VideoMimic Fig. 1 (real-to-sim-to-real pipeline).
- **Capability collage** — small grid of qualitatively diverse tasks. OpenVLA Fig. 1, RoboCat Fig. 1, RoboAgent Fig. 1.
- **Single dramatic shot** — one image of the most striking behavior. EUREKA Fig. 1 ("for the first time, unlocks rapid pen-spinning capabilities on an anthropomorphic five-finger hand").

**Caption ingredients (in this order)**:
1. System/method name in bold or small caps (often). Examples: "**P OLI F ORMER**, a transformer-based policy ...", "**D EX C AP** facilitates ...", "**Mobile ALOHA**. We introduce ..."
2. One-sentence value proposition.
3. (Optional) sub-letter pointers if the figure has panels: "Left: ... Right: ..."
4. (Optional) website/video URL: "Parkour videos at https://...", "Videos are on the project website."

### A2. The System / Architecture Diagram

**Role**: Show method components and information flow.

**Caption conventions**:
- Title with method name: "OpenVLA model architecture.", "Method Overview.", "P OLI F ORMER is a fully transformer-based policy model.", "Overview of HIL-SERL."
- Enumerate components inline with explicit numbering: "The architecture consists of three key components: (1) a vision encoder ..., (2) a projector ..., and (3) the LLM backbone ..." (OpenVLA Fig. 2).
- Use letters (a)/(b)/(c) for sub-panels, often parenthesized: "(a) Architecture of the unified position-force policy ... (b) Force-aware imitation learning ..." (force-position policy Fig. 2).
- Describe **data flow** with active verbs: "takes ... as input", "extracts ...", "maps ...", "encodes ...", "predicts ..."

**Length**: 2–6 sentences. The richest architecture captions (HIL-SERL Fig. 2, OpenVLA Fig. 2) read as standalone mini-abstracts of the method.

### A3. The Hardware Photo

**Role**: Document robot platform, sensors, mounting, dimensions.

**Caption conventions**:
- "Hardware Details." / "Hardware setup and coordinates." as a brisk title.
- Left/Middle/Right or Top/Bottom labels: "Left: Mobile ALOHA has two wrist cameras and one top camera ... Middle: The teleoperation setup ... Right: Technical specifications of Mobile ALOHA."
- Specs inline with units: "65cm/200cm", "100cm from the base", "$32k including onboard power and compute", "6 DoF ABB 1100 arm mounted on top of two Festo linear gantries".
- Component lists, often numbered: "(1) large roller, (2) circle press, (3) circle punch, ..." (RoboCook Fig. 4 lists 15 tools).

### A4. Task Definitions / Initial States

**Role**: Show what tasks exist, how they're randomized.

**Caption conventions**:
- "Task Definitions." or "Experimental Tasks." as title.
- "We illustrate N tasks..." opener.
- Per-task one-liners describing randomization: "For each task, we describe randomization and sub-task definitions." (Mobile ALOHA Fig. 3).
- For "before/after" task visualizations: "The left image in each subfigure shows the initial state of the environment; the right image shows the goal state." (Equivariant Diffusion Policy Fig. 4, Fig. 6).
- Often appears as a 2×N or 3×N grid; caption explicitly tells reader how to read it: "These images are arranged sequentially in time from top to bottom." (Mobile ALOHA Fig. 7).

### A5. Qualitative Rollouts / Sequences

**Role**: Show robot executing a task step by step.

**Caption conventions**:
- Frame indices or arrow directions: "(left to right)", "(top to bottom)", "key frames", "snapshots".
- Each row = one trajectory, each column = one timestep: "Each row shows a single trajectory (from left to right) corresponding to Opening Door (Pull), ..." (HarmonicMM Fig. 4).
- Use color overlays as proxies: "The trajectory of the target is shown in green and that of the agents is shown in blue." (Def-MARL Fig. 1).
- Often combined with a system label: "Top: ... Bottom: ..." compares conditions.

### A6. Quantitative Plots (curves, bars, boxes)

**Role**: Report numbers visually.

**Caption ingredients**:
1. **What's plotted**: "Success and failure rates of DTC, recorded for different update rates of the optimizer." (DTC Fig. 7A).
2. **How aggregated**: "Mean ± StdErr across 4 tasks, 10 evaluations each." (Re-Mix Fig. 1). "Results averaged over three seeds." (Equivariant Diffusion Table 1). "The curves and shaded regions indicate the mean and standard deviation of the reward over ten different seeds, respectively." (DreamWaQ Fig. 3).
3. **The takeaway** (one sentence): "Our parkour policy shows the best performance using only sensors that are available in the real world." (Extreme Parkour Table 2). "Our method outperforms all baseline methods in these metrics by a large margin." (RoboCook Table 1).

**Embodied-AI specific conventions**:
- Success rate (%) is the dominant y-axis.
- Cycle time, intervention rate, throughput, tracking error are secondary axes (HIL-SERL Fig. 5).
- Learning curves: x-axis is "experiences", "training steps", "demonstrations", "training rollouts", "iterations".
- Shaded regions = mean ± std or mean ± 95% CI, **always disclosed in caption**: "shaded areas indicate variance measured across 5 different end-effector positions" (force-position policy Fig. 3).

### A7. Ablation Visualizations

**Role**: Show component-by-component impact.

**Caption conventions**:
- "Ablation studies." or "Ablation Results" or "Ablations for design choices in X." as title.
- Often a multi-panel: each panel ablates one factor.
- Variant naming: "w/o CovKP", "NoDir", "NoClear", "Ours" (Extreme Parkour Fig. 7), "OpenVLA-Bridge", "OpenVLA-Bridge-SigLIP" (OpenVLA Table 9).
- Explicit framing in caption: "We ablate the effects of left: reference model overfitting ... and right: using continuous actions for Re-Mix." (Re-Mix Fig. 4).

### A8. Failure Cases

**Role**: Show what fails — required by many top venues as a sign of intellectual honesty.

**Caption conventions**:
- "Visualisation of Failures Cases." (RoTipBot Fig. 16), "Failure Case Reasoning" (Fail2Progress Fig. 1).
- Describe **why** it failed, not just the visual: "The first row shows that the printer paper with wrinkles is hard to squeeze and stops the next page's movement, eventually leading to a feeding failure." (RoTipBot Fig. 16).
- Two-row layout is common: nominal vs. failure, or two distinct failure modes.

---

## B. Caption Writing Patterns

### B1. The Title-First Convention

Almost every caption begins with a 1–6 word **bolded or italic title-like phrase** functioning as a mini-headline. Examples:

- "Hardware Details." — Mobile ALOHA Fig. 2
- "Method Overview." — force-position policy Fig. 2
- "Task Definitions." — Mobile ALOHA Fig. 3
- "Adaptive path selection." — quadruped-parkour Fig. 5
- "Robust locomotion in the wild." — ANYmal Fig. 1
- "Co-Painting." — CoFRIDA Fig. 2
- "Failure Case Reasoning." — Fail2Progress Fig. 1
- "RGB Stacking Mastery Benchmark." — RoboCat Table 2
- "Learning curves for experimental tasks." — HIL-SERL Fig. 5

This title functions as the **figure's verb-less topic sentence**. Reader can scan only titles and still navigate the paper.

### B2. The "We" Voice in Captions

Authors freely use first person inside captions, distinct from many older venues that forbid it:

- "**We** present a framework for learning parkour skills..." (Robot Parkour Fig. 1)
- "**We** introduce Co-Painting as a task in which a robot must add content..." (CoFRIDA Fig. 2)
- "**We** evaluate OpenVLA and prior state-of-the-art generalist robot policies on a comprehensive suite of tasks..." (OpenVLA Fig. 3)
- "**Our** parkour policy shows the best performance..." (Robot Parkour Table 2)
- "**Our** model reports the highest performance in all four tasks..." (Sirius Fig. 5)

The "we/our" voice signals **authorial perspective on results**, not neutral observation. It also lets the caption double as a self-contained mini-claim.

### B3. The Self-Contained Caption (Maximalist) vs. The Pointer Caption (Minimalist)

Both styles coexist in the same papers.

**Maximalist (self-contained)** — caption can be read without main text:
> "**Co-training improves ACT performance.** Across 7 challenging mobile manipulation tasks, co-training with static ALOHA dataset consistently improve the success rate (%) of ACT. It is particularly important for sub-tasks like Press Button in Call Elevator and Turn on Faucet in Rinse Pan, where precise manipulation is the bottleneck." (Mobile ALOHA Table 1)

**Minimalist (pointer)** — caption labels, prose explains:
> "Goalkeeper task in simulation." (CDF Fig. 5)
> "5 Beginner Sentiment 5 Intermediate Sentiment ..." (table-tennis Fig. 11 — almost a legend)
> "Robot placement." (FurnitureBench Fig. 22)

**Heuristic from the corpus**: Main results figures and tables are almost always maximalist (Table 1 is rarely a one-liner); appendix/hardware/setup figures and "obvious" sequences are minimalist. The minimalist style is acceptable when the prose immediately discusses the figure.

### B4. Sentence-Count Distribution

Sample of ~120 main-text figure captions:

| Sentence count | Typical figure role |
|---:|---|
| 1 sentence | Setup photos, simple plots, appendix figures |
| 2 sentences | Standard qualitative figures, ablation plots |
| 3–4 sentences | Main results figures, architecture diagrams |
| 5+ sentences | Teaser, complex multi-panel results (OpenVLA Fig. 3, EUREKA Fig. 14, HIL-SERL Fig. 7) |

**Pattern**: longer captions tend to **enumerate panels explicitly** using `(A)/(B)/(C)` or `(a)/(b)/(c)` markers. Without panel markers, captions stay ≤3 sentences.

### B5. Panel Notation Conventions

Three competing systems observed:

| System | Used by | Example |
|---|---|---|
| `(A)/(B)/(C)` (capital letters) | Science papers, ICRA | DTC Fig. 5, ANYmal Fig. 4, RoboCook Fig. 2 |
| `(a)/(b)/(c)` (lowercase) | CoRL, RSS, IROS papers | DexCap Fig. 2, Equivariant Diffusion Fig. 5 |
| `Left:/Right:/Top:/Bottom:` | Casual spatial layout | Mobile ALOHA Fig. 2, ALOHA Fig. 3 |

Within a single paper, one system is usually applied consistently. **Recommendation for new papers**: lowercase `(a)/(b)` is the dominant CoRL/RSS convention; mixed `Left:/Right:` is fine when there are only 2 panels.

### B6. Bolded Micro-Labels

Inside captions, authors bold short phrases to chunk the caption visually:

> "**Left**: A user teleoperates to obtain food from the fridge. **Right**: Mobile ALOHA can perform complex long-horizon tasks with imitation learning." (Mobile ALOHA Fig. 1)

> "**Top**: Trajectories estimated by our model and baselines. ... **Bottom left**: We collect data in the office using our own payload with the ZED-X camera. **Bottom right**: samples of TartanAir v2 test dataset, which simulates the exotic lunar environment." (MAC-VO Fig. 6)

> "**Method Overview.** (a) Architecture of the unified position-force policy trained via reinforcement learning... (b) Force-aware imitation learning enabled by demonstrations..." (force-position Fig. 2)

This pattern is especially common in **multi-row qualitative panels** where each row needs its own micro-explanation.

### B7. System Name Typesetting

Method/system names are typeset with deliberate visual weight. Observed conventions:

| Style | Examples |
|---|---|
| **Small caps with spaced letters** (LaTeX `\textsc{}` artifact when copied from PDF) | "P OLI F ORMER", "D EX C AP", "D EX IL", "H ARMONIC MM", "E UREKA", "KNOWNO" (rendered as "K NOW N O"), "V OLTRON" (rendered as "V – Gen"), "M OVE I NT" |
| **Bold mixed case** | "**HumanPlus**", "**RoboCat**", "**Mobile ALOHA**", "**ALOHA**", "**FAST**", "**Voltron**" |
| **All caps** | "DTC", "ACT", "MPC", "VLA", "VLFM", "DWL", "FEAST", "OpenVLA", "RoboCook" |
| **Italic** | rarer; mostly for emphasis ("Ours", "Oracle") |

**Practical implication when distilling**: when extracting a system name from caption text, the spaced-out small-caps form (e.g., "P OLI F ORMER" from PDF text) corresponds to a LaTeX `\textsc{Poliformer}`. The paper's actual typeset name is the contiguous lowercase form.

### B8. Sub-Caption Cross-References

Captions often reference each other to weave the figure narrative:

- "See Figure 8 in the Appendix for all environments." (Equivariant Diffusion Fig. 4)
- "Image style credits to [70]." (Mobile ALOHA Fig. 4)
- "See Appendix L for a detailed task description." (Equivariant Diffusion Fig. 6)
- "See Table 7 for detailed results." (OpenVLA Fig. 5)
- "See Fig. 9 for illustrations of all tasks." (OpenVLA Table 6)
- "Demo rack is cylindrical (cf. Fig.4d)." (DFF Fig. 5)

This is a deliberate "**bidirectional** linking strategy" — the figure points down into details and into related views, never abandoning the reader.

### B9. Color & Legend Disclosure

When figures use color encoding, captions explicitly translate:

- "The black arrows denote the moving direction." (RoboCook Fig. 1)
- "Dashed white circles: four RGB-D cameras mounted at four corners of the table. Red square: dough location and manipulation area. Dashed white square: tool racks." (RoboCook Fig. 4)
- "Red dots indicate height samples given as input to the policy. Blue dots show the controller's internal estimate of the terrain profile." (ANYmal Fig. 4)
- "Blue environments are high-equivariance tasks; green environments are intermediate-equivariance tasks; red environments are low-equivariance tasks." (Equivariant Diffusion Fig. 5)
- "The blue lines represent the errors of the estimated trajectories, and the red envelopes represent the estimated 3σ bounds." (InCOpt Fig. 4)
- "Solid line: human-in-the-loop; dashed line: offline learning on data from our method." (Sirius Fig. 5)

**Pattern**: color/line-style encoding is **never left for the reader to infer**. Even when the figure has its own legend, the caption duplicates the mapping in prose.

### B10. The "Mean ± StdErr" / Statistical Annotation Phrase

Embodied AI papers consistently disclose statistical aggregation in captions:

- "Mean ± StdErr across 4 tasks, 10 evaluations each." (Re-Mix Fig. 1)
- "Average success rates ± StdErr are computed across 129 rollouts per approach (99 for Franka-Tabletop tasks and 30 for Franka-DROID tasks)." (OpenVLA Fig. 5)
- "Results averaged over three seeds. ± indicates standard error." (Equivariant Diffusion Table 6)
- "We plot the mean and shade the ±1 standard deviation." (Def-MARL Fig. 6)
- "Reported: mean and 95% CI." (FAST Fig. 6)
- "The shaded area represents the standard deviation of the throughput. We run each setting with 8 different seeds." (Learnable PIBT Fig. 8)
- "Error bars show the maximum and minimum time per iteration over all MPC steps executed for a given problem." (TinyMPC Fig. 3)
- "We trained using three random seeds for each method to measure the standard deviations." (Robot Parkour Fig. 7)

**Required disclosure elements** (when applicable):
1. Statistic being shown (mean, median).
2. Variability measure (StdErr, std, 95% CI, min/max, IQR).
3. Sample size (rollouts, seeds, evaluations, tasks).

If any of these is missing, peer review will ask. Top venues expect all three.

### B11. The Numbered-Steps Caption (Pipeline Walkthroughs)

When the figure shows a sequential pipeline, the caption walks through it with numbered steps:

> "(1) Robot uses a selfie stick to scan RGB images of the scene (camera frustums shown). (2) Extract patch-level dense features for the images from a 2D foundation model, and distill them into a feature field (PCA shown) along with modeling a NeRF. (3) We can query CLIP feature fields with language to generate heatmaps and infer 6-DOF grasps on novel objects given only ten demonstrations." (DFF Fig. 1)

> "The robot (1) cuts the dough to an appropriate volume, (2) pinches the dough and regularizes the shape, (3) presses to flatten the dough, (4) rolls to flatten the dough further, (5) cuts a circular dumpling skin, (6) removes the excess dough, (7) picks and places the skin onto the mold, (8) adds the filling, and (9) closes and opens the mold." (RoboCook Fig. 1)

> "We first reconstruct per-frame human motion and 2D keypoints, along with a dense scene point cloud. An efficient optimization jointly aligns the motion and point cloud, recovers statistically accurate metric scale using a human height prior, and registers the human trajectory based on human-associated points. The point cloud is then converted to a mesh, aligned with gravity, and the motion is retargeted to a humanoid in the reconstructed scene." (VideoMimic Fig. 2)

### B12. Sequenced Storytelling (Multi-Row Qualitative)

For multi-row figures showing different trajectories or conditions:

> "Top row: the policy stands from a seated position after sitting down. Second row: the policy walks up a flight of stairs. Third row: the policy walks down a flight of stairs. Bottom row: the policy walks over a kerb and onto a rough terrain." (VideoMimic Fig. 5)

> "The first row illustrates data collection conducted in a laboratory setting, and the second row depicts in-the-wild data collection. (a) Initially, the human data collector moves around in the environment to track 6-DoF wrist poses with SLAM. (b)-(d) Subsequently, the data collector detaches the two cameras from the chest mount and secures them onto the glove mount. (e) With this setup, the human is prepared to begin data collection." (DexCap Fig. 13)

**Template**: `[Row identifier]: [what's happening]. [Row identifier]: [what's happening]. ...`

### B13. Symbol Definitions Inside Captions

For figures with mathematical notation, captions define symbols inline:

- "We denote vx as linear x velocity, vy as linear y velocity, vyaw as angular yaw velocity, q as joint positions, q̇ as joint velocities, r as roll, p as pitch, vfeet as feet velocities, c as feet contact indicator, Ffeet as forces on feet, and ·tg as targets." (HumanPlus Table 1)
- "O represents the fixed wire origin. E is the robot end-effector (gripper) to bend and twist the wire. The state space consists of (x, y, θ, f ) denotes the robot position and rotation relative to O and the tension force." (wire-harnessing Fig. 2)
- "Here ndof = 23 for the Unitree G1." (VideoMimic Table 3)

This eliminates the need to flip between figure and method section. Especially common in **reward tables** and **state-space diagrams**.

---

## C. Table Conventions

### C1. Caption as Takeaway

The strongest tables have a caption that **states the headline finding**, not just labels the columns:

> "**Co-training improves ACT performance.** Across 7 challenging mobile manipulation tasks, co-training with static ALOHA dataset consistently improve the success rate (%) of ACT." (Mobile ALOHA Table 1)

> "**Our perception-aware MPC improves the line visibility on average by 40%.**" (power-line MPC Table IV)

> "**RoboCat performs, on average, similarly to prior works** BC-IMP and Gato on this stacking benchmark, despite also being able to solve many other manipulation tasks." (RoboCat Table 2)

> "**The comparisons demonstrate that Fail2Progress outperforms baselines by a large margin.**" (Fail2Progress Table 3)

> "**Our method outperforms all baseline methods in these metrics by a large margin.**" (RoboCook Table 1)

**Pattern**: Lead with the takeaway in bold (or italicized), then provide context. Reader who scans only table captions still gets the paper's claims.

### C2. The "Ours" Marking Convention

Within tables, the authors' method is marked to stand out:

- "**Ours**" as a row label is universal: Robot Parkour Tables 2/3, HumanPlus Table 5 ("Humanoid Imitation Transformer (Ours)"), HIL-SERL ("HIL-SERL (Ours)"), MAC-VO Fig. 7, ALOHA Fig. 8.
- Some papers use the system name where "Ours" would go ("OpenVLA", "RoboCat", "DTC"), but mark it with bold or a separator row above.
- Variants and ablations are named relative to the main method: "OpenVLA-Bridge", "OpenVLA-Bridge-SigLIP", "NoDir", "NoClear", "w/o CovKP", "w/o CA".

### C3. Bold-the-Best Convention

Standard practice:
- **Best result per column/row is bolded.** OpenVLA Table 1 ("we bold the mean success rate for both due to overlapping error bars" — RT-2-X and OpenVLA both bolded when statistically tied).
- "Bold performance indicates the best, bold difference is greater than 10%." (Equivariant Diffusion Table 1)
- Underlines occasionally mark second-best.
- When error bars overlap, **multiple entries may be bolded** with a footnote explaining why.

### C4. Parenthetical Deltas

When comparing two methods, the difference is shown in parentheses, often color-coded:

> "Number in parentheses shows the difference between our method and the best baseline (with increment colored in blue and decrement in red). Bold performance indicates the best, bold difference is greater than 10%." (Equivariant Diffusion Table 1)

> "We color relative increases of more than 25% from uniform green and relative decreases of more than 25% red." (Re-Mix Table 2)

This lets the reader scan deltas without doing arithmetic.

### C5. Header Arrows ↑/↓

Columns indicate optimization direction:
- ↑ for "higher is better" (success rate, return, accuracy, throughput)
- ↓ for "lower is better" (tracking error, cycle time, latency, memory)

Not universally used, but appearing in increasingly many CoRL/RSS papers (MAC-VO, Neural MP, FAST).

### C6. Baseline Ordering Convention

Common orderings:
1. **Chronological / prior-work first, ours last** — invites the reader to read the table top-down and see the progression. ALOHA, Mobile ALOHA, ACT-related tables.
2. **Worst-to-best, ours last/best** — narrative builds to "ours". HIL-SERL Table 1a.
3. **By method family** (model-based, then learned, then ours). DTC Fig. 5.
4. **Alphabetical** — rare, but appears in benchmark papers.

**Implication**: the last row is usually "ours" and bolded. The reader's eye trains to look there for the headline number.

### C7. Multi-Block Tables with Horizontal Separators

For ablation tables, results split into blocks separated by `\midrule` (visible as a thin horizontal line). Each block ablates a different design axis. Caption explicitly enumerates the blocks:

> "(a) HIL-SERL against imitation learning baselines. (b) HIL-SERL against various other baselines." (HIL-SERL Table 1)

> "(a) ablation studies on design choices for scaling up model capacity; and (b) the real-world results, on two different embodiments." (PoliFormer Table 2)

> "(a) Results on the C HORES-S ObjectNav benchmark... (b) On three LoCoBot-embodiment test suites, P OLI F ORMER outperforms all prior work." (PoliFormer Table 1)

This pattern is essential for **multi-axis ablation tables** that would otherwise become unreadable.

### C8. Statistical Notation in Tables

- `±` notation universal: "1.14 ± 0.30" (RoTipBot Table III).
- Error bars in cells often labeled in caption: "We report mean success rate ± StdErr for each policy." (OpenVLA Table 6).
- N/A for cells where method failed (RoTipBot wo/CA at 7-9 sheets — "N/A" because system fails beyond 6 sheets).
- Missing entries (—, dash) when comparison was not performed; caption notes why.
- Significance markers (*, **, †, ‡) much less common than in ML theory papers; embodied AI tends to rely on visual bolding + error bars.

### C9. Hyperparameter Tables (Appendix-Only)

Almost every paper has a hyperparameter table in the appendix:

- "Hyperparameters for co-training." (Mobile ALOHA Table 5)
- "Hyperparameters for training and model architecture." (PoliFormer Table 3)
- "PPO Hyperparameters" (Robot Parkour Table 10)
- "Policy training details for the RAM insertion task." (HIL-SERL Table 2)
- "Domain-randomization and noise settings used during training." (VideoMimic Table 5)

**Caption length**: typically 1 sentence; minimum required is just the title. Acceptable for appendix.

### C10. Reward Term Tables

Specific to RL-heavy papers. List reward components with weights:

- "Reward terms, corresponding weights, and scaling factors k." (VideoMimic Table 4)
- "Reward Scales for Climbing Purposes" (Robot Parkour Table 3) — bare phrase as caption.
- "Rewards in Simulation. We denote vx as linear x velocity, ..." (HumanPlus Table 1) — includes symbol definitions.

**Structure**: Term name | Formula or description | Weight. Often grouped by purpose (locomotion, manipulation, task-specific, regularization).

### C11. Dataset / Benchmark Tables

Used in dataset papers and tables comparing benchmarks:

- "**Open-source real-world manipulation dataset landscape**: RoboSet (ours) is one of the largest open-source robotics datasets." (RoboAgent Table 1)
- "OpenVLA training data mixture using datasets from the Open X-Embodiment dataset." (OpenVLA Table 3)
- "Categorization and distribution of our 123 self-collected training clips." (VideoMimic Table 6)

These tables read more like documentation than results — caption mostly labels.

---

## D. Prose ↔ Figure / Table Reference Patterns

### D1. The Forward Reference

Standard pattern from the corpus: introduce figure number **before** describing what it shows.

- "We illustrate 6 real-world tasks that Mobile ALOHA can perform autonomously **in Fig. 3**."
- "**Fig. 2** shows the network architecture..."
- "**As shown in Fig. 5**, the policy adapts to..."
- "**See Fig. 7 for** illustrations of all tasks."

### D2. The Parenthetical Reference

When the figure is supporting evidence rather than the focus of the sentence:

- "...resulting in a ground sampling distance (GSD) of 1 mm/px (**see Fig. 3**)..."
- "...the robot adjusts the orientation in the first few steps and then starts to move to the origin (**Fig. 6**)..."
- "...demonstrates that our method achieves 80% success rate (**Table 3**)..."

### D3. The Backward Reference

After describing a result, cite the figure as confirmation:

- "Our parkour policy can achieve the best performance, compared with a blind policy and built-in MPC controllers (Fig. 6)."
- "The robot is moving from left to right following target velocity commands given by the joystick (Fig. 6A)."

### D4. The Multi-Figure Sweep

When discussing multiple figures together:

- "**As detailed in Figs. 3–5**, the policy progressively improves..."
- "**Tables 1 and 2** together show that..."
- "**Figs. 4 and 5** compare the controller's behavior..."

### D5. The Panel-Level Reference

Reference specific sub-panels for precision:

- "We see this clearly in **Fig. 7A**."
- "**Fig. 3(b)** shows the after-optimization view."
- "As shown in **Fig. 9 (left)**..."
- "**Table 1(a)** compares against imitation learning baselines..."

### D6. The Side-by-Side Comparison Reference

For figures showing before/after or method/baseline:

- "Compared with the baseline (**Fig. 6, top**), our method (**Fig. 6, bottom**) achieves..."
- "Without grasping constraints, PF often estimates the needle pose with inaccurate depth and orientation (**Fig. 5, left**), whereas cPFrp provides a more realistic, feasible reconstructed pose (**Fig. 5, right**)."

### D7. The Result-Anchor Pattern

In Results/Experiments sections, a typical paragraph follows this rhythm:

1. **Claim**: "Our method outperforms all baselines by a large margin..."
2. **Quantitative anchor**: "...with a success rate of 85% compared to 42% for the next-best baseline."
3. **Figure pointer**: "(see Table 2)."
4. **Mechanism**: "The improvement is most pronounced on tasks requiring precise contact-rich manipulation, where..."
5. **Caveat or extension**: "Notably, the method also generalizes to unseen objects (Fig. 7), suggesting..."

Found in: OpenVLA §5, RoboCat §4, ALOHA §4, HIL-SERL §VI.

### D8. The Vague vs. Specific Cite

**Vague**: "Our method works well (see plots)." — Almost never seen in top papers.

**Specific**: "Our method achieves 87.2% success rate (Fig. 5, blue line) vs. 61.4% for the strongest baseline (orange line)." — Standard.

Specificity in citation correlates strongly with venue: CoRL/RSS/Science papers reference exact panels and line colors; weaker venues often cite figure numbers alone.

---

## E. Cross-Cutting Observations

### E1. Self-Containment Spectrum

Papers fall on a spectrum:

| End | Style | Implication |
|---|---|---|
| **Maximalist captions** | OpenVLA, RoboCat, Mobile ALOHA, HIL-SERL | Captions are 3–6 sentences. Caption + figure = readable without main text. Strong for venues where reviewers skim. |
| **Balanced** | Most CoRL/RSS papers | Captions are 2–3 sentences. Caption introduces, prose elaborates. |
| **Minimalist captions** | Some IROS/ICRA papers, especially appendix | Captions are 1 sentence or a phrase. Prose carries the burden. |

**Recommendation for new papers in top venues**: lean maximalist. Reviewers often skim main results figures first; a self-contained caption increases the chance the claim lands.

### E2. The Teaser is a Promise

Figure 1 captions across the corpus share a structure:
1. Name the system (often bolded/small-caps).
2. State the headline capability.
3. (Optional) mention scale: "trained on 970k robot episodes", "21 institutions across the globe", "$32k including onboard power and compute".
4. (Optional) mention novelty: "for the first time, unlocks...", "the first open-source...".
5. (Optional) link to videos/website.

Examples that exemplify this structure: OpenVLA Fig. 1, Mobile ALOHA Fig. 1, ALOHA Fig. 1, RoboCat Fig. 1, EUREKA Fig. 1, RoboAgent Fig. 1, Open X-Embodiment Fig. 1, ANYmal Fig. 1.

### E3. Architecture Figures are Method-Section Anchors

The architecture figure (typically Fig. 2 or Fig. 3) is **referenced more often** than any other figure in the paper — typically 5–15 times across §3-§5. Caption is verbose because it doubles as a method summary.

### E4. Hardware Figures are Reproducibility Anchors

Every embodied paper has at least one hardware figure. Caption is verbose about:
- Specific products/SKUs ("Realsense L515 LiDAR camera", "Rokoko gloves", "ViperX 300", "Intel NUC").
- Dimensions in metric units.
- Camera placement (count, location, FOV).

This is the **reproducibility contract** with the community: another lab should be able to rebuild the rig.

### E5. Task-Definition Figures are Evaluation Contracts

Task figures lock in evaluation:
- Initial state randomization is shown explicitly.
- Sub-tasks are decomposed.
- Each task is named identically across figure, table, and prose.

Example: Mobile ALOHA defines 7 tasks in Fig. 3, then every subsequent table uses those exact names ("Wipe Wine", "Cook Shrimp", "Rinse Pan", "Push Chairs", "Call Elevator", "Use Cabinet", "High Five").

### E6. Color is a Naming Device

In ablation/comparison plots, color = method name. The convention:
- **Ours** = bold, saturated color (often blue or red).
- Baselines = lighter colors, often gray for the weakest.
- Best baseline = bold but different hue.

Then in the **caption**: "We compare our method (blue) against Baseline-X (orange) and Baseline-Y (gray)..."

**Pattern**: when a paper has 4+ baselines, the caption explicitly lists colors. When 2–3, the legend in the figure suffices.

### E7. Failure Cases Earn Reviewer Trust

CoRL/RSS/Science papers often dedicate a figure to failure cases. The figure's job is **not** to confess weakness — it's to demonstrate intellectual honesty and to discriminate the method's failure modes from its successes.

Caption pattern: name the failure mode, describe what triggered it, gesture at when it occurs in practice.

> "The first row shows that the printer paper with wrinkles is hard to squeeze and stops the next page's movement, eventually leading to a feeding failure. The second row demonstrates a failure case when grasping objects with a high friction coefficient, where two layers of fabrics are squeezed together." (RoTipBot Fig. 16)

### E8. Captions are Where Plots Get Their Statistical Voice

Every plot has a hidden statistical commitment. Captions are where those commitments become legible:
- What's plotted? (mean, median, individual runs)
- What's the variability? (std, StdErr, 95% CI, IQR)
- How many samples? (N rollouts, N seeds, N tasks)
- What's compared? (vs. baseline X, vs. ablation Y)

Skipping any of these in a CoRL/RSS submission is a near-guaranteed reviewer flag.

### E9. The "Three-Layer" Caption

The richest captions in the corpus have three layers:
1. **Title** — what the figure is.
2. **Mechanism** — how to read it / what each part shows.
3. **Claim** — what the reader should conclude.

> [Layer 1] "**Co-training improves ACT performance.** [Layer 3] Across 7 challenging mobile manipulation tasks, co-training with static ALOHA dataset consistently improve the success rate (%) of ACT. [Layer 3] It is particularly important for sub-tasks like Press Button in Call Elevator and Turn on Faucet in Rinse Pan, where precise manipulation is the bottleneck." (Mobile ALOHA Table 1)

Note this caption is **all title + claim**, with mechanism implicit (the table itself shows success rates). For figures with non-obvious encoding, mechanism becomes essential.

### E10. Hidden Conventions for Embodied AI

Versus general ML papers, embodied AI captions have unique conventions:
- Frequent mention of **video links** ("Videos are on the project website", "video examples are shown in Movie 5").
- Frequent mention of **embodiment** ("on a Franka Emika robot", "Unitree G1", "Stretch RE-1", "Sawyer", "ANYmal-D") — embodiment is part of the experimental claim.
- Frequent mention of **deployment context** ("indoor and outdoor", "in-the-wild", "real-world", "zero-shot transfer", "Sim2Real gap") — every claim is implicitly conditioned on transfer.
- Frequent mention of **safety / robustness** ("disturbance rejection", "without falling", "without getting stuck") — robotics-specific quality dimensions.

---

## F. Sample Size & Coverage

This file synthesizes patterns from:
- 614 captions across 63 papers (CoRL: 28, RSS: 9, ICRA: 12, IROS: 8, Science: 6)
- Sampled in-text figure references from a subset of papers (OpenVLA, Mobile ALOHA, Robot Parkour, HIL-SERL, ALOHA, RoboCat, DexCap, MAC-VO, EUREKA, force-position policy, FAST, VideoMimic, Def-MARL)
- Direct caption inspection for ~25 of the 63 papers' figure naming conventions and the use of small-caps system names

Patterns rated by frequency:
- **Universal** (90%+ of papers): A1–A8 figure types, B1 title-first, B2 "we" voice, B5 panel notation, B10 statistical disclosure, C1 caption-as-takeaway for main results, C2 "Ours" marking, C3 bold-best, D1 forward references, E1 self-containment, E4 hardware as reproducibility.
- **Very common** (60–90%): B4 sentence-count distribution, B6 bolded micro-labels, B7 system name typesetting, B11 numbered-steps, B12 sequenced storytelling, B13 symbol definitions, C4 parenthetical deltas, C7 multi-block tables, D7 result-anchor pattern, E2 teaser as promise, E7 failure cases.
- **Common** (30–60%): B8 sub-caption cross-references, C5 header arrows, C9 hyperparameter tables (universal in appendix), C10 reward tables (specific to RL papers), D5 panel-level references, E6 color as naming device.
- **Style-dependent** (paper- or author-specific): exact form of system-name typesetting (B7), maximalist vs. minimalist captions (B3), use of significance markers (C8).

---

## G. Author's Note on Patterns Not Distilled

A few patterns observed but not formalized into rules:
- **Video links in captions**: 80%+ of papers include them, but URL-style citation varies wildly (full URL vs. shortened, with vs. without "https://").
- **Movie / Supplementary Video numbering**: Science papers number them ("Movie 1", "Movie 3"); CoRL/RSS papers prefer project-website pointers.
- **Inset figures**: Common in MAC-VO, OpenVLA, RoboCook — small image embedded inside a larger figure. Caption acknowledges the inset ("Inset shows the top 10 inferred grasps").
- **Pull-out callouts**: arrows pointing from a thumbnail to a zoomed view. Caption may or may not describe the callout; depends on author style.

These are stylistic choices rather than learnable patterns. The skill should default to whatever the target venue's recent best papers do.
