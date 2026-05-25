# Appendix / Supplementary Material — Research Notes

**Corpus**: Appendix sections extracted from 63 embodied-AI papers. Direct extractions: 20/63 with clean appendix-start markers. Keyword presence: 35/63 mention `Appendix` or `Supplementary`. The appendix is unevenly used across venues: CoRL/RSS/IROS submissions almost always have one; ICRA submissions often skip it (page-budget pressure); Science Robotics uses `Supplementary Materials` with strict structure imposed by the journal.

Source corpus: `_appendix_corpus.md` (120KB from 20 papers, first 6000 chars of each).

---

## A. Header taxonomy

Six observed appendix-start styles:

| # | Header style | Example | Venue tendency |
|---|---|---|---|
| Ap1 | `Appendix` (no letter prefix) | F3RM (CoRL_2308.07931), Mobile ALOHA (CoRL_2401.02117), VideoMimic | CoRL most common |
| Ap2 | `A    Appendix` (letter-prefixed) | Fail2Progress (CoRL_2509.01746), Eureka (Science_Robotics_2310.12931) | When sub-sections are letter-numbered |
| Ap3 | `APPENDIX` (all-caps) | ICRA papers (Robot Table Tennis ICRA_2408.03906, ICRA_2410.21415) | ICRA / IROS standard |
| Ap4 | `Supplementary Materials` (journal style) | Science Robotics papers (2304.13653 Bipedal Soccer, 2306.11706 RoboCat) | Science Robotics mandatory |
| Ap5 | `Supplementary Methods` (Nature-style sub-section) | Science_Robotics_2304.13653 | Nature/Science Robotics |
| Ap6 | No `Appendix` header — content begins directly with `A. Section Name` | rare; some IROS | Page-saving |

**Picking your header**: defer to venue. CoRL/RSS/IROS → Ap1 or Ap2. ICRA → Ap3 (all-caps). Science Robotics → Ap4 + Ap5 split.

---

## B. Top-level appendix organization

### B1. Overview paragraph (best-practice opener)

Strong CoRL/RSS papers open the appendix with a 1-2 sentence overview pointing to the supplemental video and previewing what readers will find:

> "**Overview**
> The appendix provides additional details, experiments, and results. Please refer to the supplemental video for real-world robot executions available at sites.google.com/view/fail2progress."
> — Fail2Progress (CoRL_2509.01746)

**Template**: `The appendix provides {what kinds of content}. Please refer to {supplementary URL} for {what}.`

The supplementary-video pointer is near-universal. Almost every embodied-AI paper hosts videos on a Google Sites or GitHub Pages URL — make sure your appendix opener points to it.

### B2. Table of Contents (strongly recommended at 5+ sub-sections)

Top-tier submissions (especially long ones at CoRL 2025) include a dotted-leader TOC at the appendix opening. Two real examples:

**Fail2Progress** (17 sub-sections):
```
A.1  Qualitative Analysis ............................ A2
A.2  Detailed Experimental Tasks .................... A3
A.3  Efficiency Experiments ......................... A3
A.4  Key Findings ................................... A3
A.5  Ablation Study ................................. A4
...
A.17 Hardware Information ........................... A10
```

**Eureka** (8 lettered sub-sections + nested):
```
A    Full Prompts                                          16
B    Environment Details                                   16
C    Baseline Details                                      20
     C.1  L2R Reward Examples
D    EUREKA Details                                        23
     D.1  Pen Spinning Tasks
     D.2  EUREKA from Human Initialization
     D.3  EUREKA from Human Feedback
     D.4  Computation Resources
E    EUREKA on Mujoco Environments                         25
F    Additional Results                                    28
G    EUREKA Reward Examples                                31
     G.1  Reward Reflection Examples
     G.2  Negatively Correlated EUREKA Reward Examples
     ...
H    Limitations and Discussion                            45
```

**Rule of thumb**: TOC needed at ≥5 sub-sections. Below that, sub-section ordering can be inferred from the headers alone.

### B3. Page numbering

Three conventions:
- **Continuous arabic** (most common): main body ends at page 14, appendix continues from page 15
- **Letter-prefixed** (Fail2Progress style): `A1, A2, A3, ...` — clearly separates supplementary content
- **Independent supplementary** (Science Robotics): supplement is its own document with `S1, S2, ...`

CoRL/RSS papers usually use continuous arabic. ICLR-flavored / arXiv-first papers sometimes use letter-prefixed. Science Robotics strictly uses S-prefixed supplements.

---

## C. Sub-section naming taxonomy

Across 20 papers, the modal appendix sub-sections fall into ~12 recurring topic categories. Naming conventions for each:

### C1. Implementation Details / Experiment Details

The most common appendix section. Names:
- `Experiment Details and Hyperparameters of {Baseline1}, {Baseline2}, {Baseline3}` (Mobile ALOHA)
- `Experimental Details` (PoliFormer, Fail2Progress)
- `Implementation Details` (Equivariant Diffusion Policy)
- `Detailed Experimental Tasks` (Fail2Progress)
- `Policy Training Details` (HumanPlus precision insertion paper)

Content: data preprocessing, training hyperparameters, optimizer choice, learning rate, batch size, num-steps, hardware details.

### C2. Hyperparameter tables

Almost every appendix contains one. Naming conventions for Tables:
- `Table 5: Hyperparameters of co-training.` (one per training stage)
- `Table 6: Hyperparameters of ACT.` (one per baseline)
- `Table 7: Hyperparameters of Diffusion Policy.`
- `Table 8: Hyperparameters of BYOL, the feature extractor of VINN.`
- `Suppl. Table S4 Hyperparameters` (Science Robotics)

Pattern: one table per algorithm. Two-column layout: parameter name (left), value (right). Bold not used in the table body. Caption is two-word terse: `Hyperparameters of {AlgorithmName}.`

Example structure (verbatim from Mobile ALOHA):
```
learning rate                          2e-5
batch size                             16
# encoder layers                       4
# decoder layers                       7
feedforward dimension                  3200
hidden dimension                       512
# heads                                8
chunk size                             45
beta                                   10
dropout                                0.1
backbone                               pretrained ResNet18[40]
```

**Conventions**:
- Use `#` prefix for counts (`# encoder layers`, not `Number of encoder layers`)
- Scientific notation for learning rates (`2e-5`, not `0.00002`)
- Cite the architecture source inline (`pretrained ResNet18[40]`, not `ResNet18`)
- Image augmentation values listed compactly: `RandomCrop(ratio=0.95) & ColorJitter(brightness=0.3, contrast=0.4, saturation=0.5) & RandomRotation(degrees=[-5.0, 5.0])`

### C3. Network Architecture

Naming:
- `Network Architecture` (IROS_2312.06639)
- `Architecture Details`
- `Model Architecture`

Content: per-encoder dimension breakdowns. Often paired with a small figure showing tensor shapes.

Example sentence pattern:
> "Our RGB observations initially get processed by DinoV2 model, generating 768 × 16 × 16 features which pooled to a reduced dimension of 768 × 7 × 7. The processed features are passed through separate visual encoders. This results in two distinct sets of 16 × 7 × 7 latent visual features corresponding to each camera view."
> — IROS_2312.06639

The pattern: walk through the network in input-to-output order, with explicit tensor dimensions at each stage.

### C4. Reward / Loss formulation

Naming:
- `Reward Function`
- `Reward Components`  
- `Loss Function Details`

Content: full math derivations of reward shaping terms, often with sub-component equations. Example from IROS_2312.06639:

> "Manipulation Reward Rmanip:
> Rmanip = δwmanip shaping Rmanip shaping + wprogress ∆P + γRfinish task
> Rmanip shaping = exp(−5 × dee current) × 1000 × max(dee cloest − dee current, 0))
> The variable δ is 1 if the end effector has not reached the target region, and 0 otherwise."

Pattern: math first, then prose paragraph defining every variable.

### C5. Visual Augmentation / Data Augmentation

Naming:
- `Visual Augmentation`  
- `Data Augmentation`

Content: terse comma-separated list of transforms with hyperparameter values. Example from IROS_2312.06639:

> "Our applied augmentations include: **ColorJitter**: Adjusts brightness (0.4), contrast (0.4), saturation (0.2), and hue (0.05); **GaussianBlur**: Applies a blur effect with a kernel size of (5,9) and sigma range of (0.1,2); **RandomResizedCrop**: Resizes the input with a scale range of (0.9,1); **RandomPosterize**: Reduces color depth, applied with varying bits (7,6,5,4) and a probability of 0.2 for each setting; **RandomAdjustSharpness**: Enhances or reduces the sharpness with a factor of 2, applied with a probability of 0.5."

Pattern: bold transform name, colon, terse description with parenthetical hyperparameters, semicolon separator. No bullet list — one paragraph.

### C6. Qualitative Analysis / Failure Cases

Naming:
- `Qualitative Analysis`
- `Failure Cases`
- `Qualitative Examples`

Content: large multi-panel figures showing successful and failed rollouts, paired with prose narratives. Example structure from Fail2Progress:

> "We present qualitative results in Fig. 4. **Hierarchical Tabletop Organization task (First row)**: The robot is tasked with organizing the cups and capsules on another table while keeping them in a row. It first places several capsules into their corresponding cups. In the failure case, the robot fails to recognize the correlation between cups and capsules, resulting in the wrong organization. After learning from this failure, Fail2Progress successfully completes this task by understanding that the capsules will move with their corresponding cups. **Multi-object Transport task (Second row)**: ..."

Pattern: bold task name (with figure row indicator), colon, 3-4 sentence narrative covering: task → failure mode → fix.

### C7. Additional Ablations

Naming:
- `Additional Ablations`
- `Ablation Study`  
- `{ComponentName} Ablation`  
- `Ablation on {ComponentName}` (e.g., `Ablation on Feature Field Architecture`)

Content: extra ablation tables that didn't fit in the main paper. Usually one ablation per sub-section.

### C8. Dataset / Task Details

Naming:
- `Detailed Experimental Tasks`  
- `Task families`  
- `Task Definitions`
- `Dataset Details`

Content: per-task descriptions. Example structure from Fail2Progress:

> "**Multi-object Transport** tasks the robot to transport multiple objects within a container using a single skill (e.g., carrying multiple fruits in a grocery bag). To succeed, the robot has to understand that all objects inside the container move together when the container is moved. **Hierarchical Tabletop Organization** tasks the robot to organize a table by arranging objects into a hierarchical structure (e.g., multiple objects in different cups). Success requires the robot to understand the relationships between these objects and how its skills impact future relations based on the hierarchical structure. **Constrained Packing** tasks the robot to organize objects in a constrained environment (e.g., a bookshelf). Success involves using a non-prehensile push skill to create space and then packing the remaining objects onto the shelf."

Pattern: **TaskName** + present-tense verb + description + success criterion. Each task gets one paragraph.

### C9. Hardware / System Setup

Naming:
- `Hardware Information`
- `System Hardware`
- `Real-World Setup`
- `Tool-Change Apparatus` (when novel hardware is part of the contribution)

Content: robot model, gripper specifics, camera placement, mount design, computational hardware (GPU servers).

Example from FEAST (CoRL_2505.20829 vicinity):
> "FEAST (see Figure 4) uses a Kinova Gen3 7-DoF robot arm [85] and a Robotiq 2F-85 gripper [86]. It can be flexibly mounted either on the user's ROVI wheelchair [87], powered by the wheelchair's battery, or on a movable Vention stand [88], powered by a wall outlet."

Pattern: specific model number + citation [X] + brief functional description.

### C10. Prompts (for LLM-based methods)

Naming:
- `Full Prompts`
- `LLM Prompts`
- `Prompts and Templates`

Content: verbatim copy-pasted LLM prompts. Critical for reproducibility in any paper using GPT-4 / Claude / Gemini as a tool.

Example pattern from Eureka:
```
A    FULL PROMPTS
In this section, we provide all EUREKA prompts.

Prompt 1: Initial system prompt
You are a reward engineer trying to write reward functions to solve reinforcement learning
tasks as effective as possible.
Your goal is to write a reward function for the environment that will help the agent learn the
task described in text.
...
```

Pattern: numbered "Prompt 1:", "Prompt 2:" with a noun-phrase descriptor (`Initial system prompt`, `Reward reflection prompt`, etc.). Verbatim prompt content in a code-block or differently-styled font.

### C11. Computation Resources

Naming:
- `Computation Resources`
- `Compute Details`
- `Training Time`

Content: GPU model + count + training duration. One paragraph or table.

Example from ICRA_2410.21415:
> "**E. Computation Resources**
> Our models are trained on servers with 72 vCPU AMD EPYC 9754 128-Core Processor, 4 RTX 4090D (24GB), and 240 GB memory. Training on each map takes less than 12 hours."

Pattern: CPU/GPU model + memory + per-experiment training time. Sometimes paired with a `Suppl. Table` (Science Robotics).

### C12. Author Contributions

Naming:
- `Author Contributions`  
- `Contribution Statements`

Content: per-author bullet listing their role. Always present in Science Robotics + many large-collab CoRL papers. Format:

> "**David B. D'Ambrosio**¹,∗: Worked on all parts of the system over the course of many years. Developed the policy architecture and training approach. Conceived, wrote, and edited this paper. Helped run and analyze the user study.
> **Saminda Abeyruwan**¹,∗: Worked on all parts of the system over the course of many years. Developed the policy architecture and training approach. Conceived, wrote, and edited this paper. Helped run and analyze the user study.
> **Laura Graesser**¹,∗: ..."
> — Robot Table Tennis (ICRA_2408.03906)

Pattern: bold author name + superscript affiliation/role markers + colon + 1-3 sentence contribution statement starting with past-tense action verbs (Developed, Built, Wrote, Conceived, Investigated, Implemented).

**Footer pattern**: numbered footnotes after the list explain role markers:
```
¹Primary contributors
∗Corresponding authors (order randomized, equal contributions)
²Core contributors (Alphabetized)
†Work done at Google DeepMind via Stickman Skills Center LLC
§Work done at Google DeepMind via Hoku Labs.
```

### C13. Model Card (Science Robotics / TMLR best practice)

Naming: `Model Card` (always literal — this is now a standardized practice from ML community)

Content: 8-row table covering Model Details, Intended Uses, Factors, Metrics, Evaluation, Training Data, Quantitative Analyses, Ethical Considerations, Caveats and Recommendation. RoboCat's model card (Science_Robotics_2306.11706 / TMLR) follows the Mitchell et al. 2019 template:

```
Model details        Organisation | Google DeepMind
                     Model date | June 2023
                     Model type | Transformer with VQ-GAN encoder ...
                     Model version | Initial release.
                     Feedback on the model | konstantinos@google.com, ...

Intended uses        Primary intended uses | Research into learning ...
                     Primary intended users | Google DeepMind Researchers.
                     Out-of-scope uses | Not intended for commercial ...
```

If you're at a venue that values reproducibility (TMLR, Science Robotics, Nature Robotics), include a model card. Otherwise optional.

### C14. Broader Impact / Ethical Considerations

Naming:
- `Broader Impact`
- `Ethical Considerations`
- `Limitations and Discussion` (when combined)

Content: 1-2 paragraph discussion of societal risks, dual-use concerns, dataset bias. ICLR style mandates this; CoRL increasingly does too.

Example from RoboCat:
> "**Broader Impact**
> This work presents progress on training generalist agents for robotic manipulation. Our work presents a recipe, and first steps, in an emerging area, with experiments in a controlled lab environment demonstrating promising but imperfect performance. Nonetheless, the potential impact on society from generalist robotic agents calls for increased interdisciplinary research into their risks and benefits..."

Pattern: 3-move structure — what we did → why it matters → what the community should consider.

---

## D. Sub-section numbering conventions

Three observed schemes:

### D1. Decimal under letter (most common)
`A.1`, `A.2`, `A.2.1`, `A.3`, `B.1`, ...
- Example: F3RM uses `A.1 NeRFs`, `A.2 Dense Feature Extraction`, `A.3 Feature Fields`, `A.3.1 Ablation`
- Example: Fail2Progress uses `A.1` through `A.17`

### D2. Letter-only (Science Robotics style)
`A`, `B`, `C`, `D` as top-level appendix sections; each is a major topic.
- Example: Eureka uses `A Full Prompts`, `B Environment Details`, `C Baseline Details` with `C.1` nested under

### D3. Roman numerals (ICRA legacy)
`VII. Visual Augmentation`, `VIII. Network Architecture`
- Example: IROS_2312.06639 continues roman numbering from main body into appendix

Use D1 (decimal under letter) for CoRL/RSS submissions — clearest cross-referencing.

---

## E. Figure & table conventions in appendix

### E1. Figure numbering

Two schemes:
- **Continuous**: appendix figures continue from main body (Figure 6, 7, 8, ...) — Mobile ALOHA, Fail2Progress
- **Prefixed**: appendix figures get `A` prefix (`Figure A8`, `Figure A9`, ...) — F3RM, Eureka
- **S-prefixed**: supplementary figures get `S` prefix (`Suppl. Figure S1, S2, ...`) — Science Robotics

CoRL/RSS modal practice: prefixed `Figure A1, A2, ...` when there are 5+ appendix figures; continuous numbering when only 1-3.

### E2. Table numbering

Same options as figures. Most common: appendix tables get `A` prefix (`Table A1, A2, ...`) when there are 5+; continuous numbering when only 1-3.

Science Robotics: `Suppl. Table S1, S2, ...` always.

### E3. Cross-references back to main body

When the appendix discusses something analyzed in the main body, use:
- "(see also Sec. {N} in the main paper)"
- "as discussed in Sec. {N}"
- "(see Fig. {N})"

Never use just bare `Section 3` — always indicate whether it's in the main body or the appendix.

---

## F. Sentence patterns specific to the appendix

### F1. Section-opening sentence patterns

- "**In this section, we provide** {what}." → "In this section, we provide all EUREKA prompts."
- "**In this section, we** {verb} {what}." → "In this section, we compare Learnable PIBT and PIBT with different global guidance..."
- "**Here, we** {verb} {what}." → "Here, we describe the data preprocessing pipeline in detail."
- "**This section describes / presents / provides** {what}." → "This section compares different decentralized methods on the Learn-to-Follow Benchmark."

### F2. Figure-referencing sentence patterns

- "**Figure {N} shows** {what}." → "Figure 8 shows the spread of end-effector error at the end of replaying a 300 steps (6s) demonstration."
- "**We visualize** {what} **in Figure {N}**." → "We visualize all the large maps for evaluation in Figure 6 and all the down-scaled small maps for training in Figure 7."
- "**Fig. {N} shows** {what}." (saves space; common in IROS/ICRA)
- "**See Figure {N} for** {what}." (most terse)

### F3. Table-referencing sentence patterns

- "**Table {N} contains** {what}." → "Table V contains the MuJoCo simulator parameters and Table VI lists..."
- "**The hyperparameters are listed in Table {N}.**"
- "**We report {metric} in Table {N}.**"

### F4. Forward-pointer from main body to appendix

In the main body, point to appendix sections like this:
- "**See Appendix X for more details.**"
- "**See Sec. A.{N} for** {what}."
- "**(see App. {N})**" / "**(App. {N})**" — most space-saving
- "**(more discussion on limitations in App. E)**" — PoliFormer pattern

ALWAYS include such pointers — reviewers need to know where to look.

### F5. Verbatim-data sentence pattern

When dumping a list of values:
- "**For all tasks, we use** $w_{nav} = 1$, $R_{reach} = 2$, ..."
- "**For opening door/fridge tasks, we use** $w_{progress} = 80$. **For the cleaning table task, we use** $w_{progress} = 100$."

Pattern: condition clause + we use + parameter list. Repeat for each conditional setting.

---

## G. What to include vs. what to cut

### G1. Must include (reviewer expectation)

- **Hyperparameters** for your method and every baseline. Without this, reviewers reject for irreproducibility.
- **Compute budget** (GPU type, count, training hours).
- **Dataset license / source** if you released or used a custom dataset.
- **Random seeds** statement — typically: "All experiments use 3 random seeds. We report mean and standard error."
- **Real-world setup** photo or diagram (if claims involve real-robot).
- **Failure cases** — at least one figure or example. Reviewers explicitly check.

### G2. Strongly recommended

- **TOC** (≥5 sub-sections).
- **Overview paragraph** with link to supplementary video.
- **Additional ablations** that didn't fit in the main body.
- **Prompts** verbatim (if using LLMs).
- **Per-task descriptions** (≥3 tasks).
- **Network architecture** dimensions walkthrough.

### G3. Optional but adds polish

- **Model Card** (Mitchell et al. 2019 template).
- **Author Contributions** statement.
- **Broader Impact** paragraph.
- **Computation Resources** sub-section.
- **Cross-platform analysis** (CPU/GPU benchmarks if relevant).

### G4. Cut these (waste of appendix space)

- Restatement of method already covered in main body without new detail.
- Long literature reviews redundant with related work section.
- Marketing-style "potential applications" paragraphs.
- Generic ML background (gradient descent, transformers, NeRFs) unless directly weighted by something novel.

---

## H. Length budget

| Venue | Typical appendix length | Notes |
|---|---|---|
| **CoRL** | 5-15 pages | 9 pages main + 5-15 supplementary is modal |
| **RSS** | 3-10 pages | RSS has 12 pages main → less appendix pressure |
| **ICRA** | 1-4 pages | 6 pages main → heavy appendix pressure |
| **IROS** | 1-4 pages | Similar to ICRA |
| **Science Robotics** | 15-30 pages | Strict structure: Materials and Methods → Supplementary Materials |

**Page-allocation rule of thumb**: appendix should NOT exceed 1.5× the main body length. Reviewers are unpaid; an appendix that runs 30+ pages signals lack of editing.

---

## I. Coupling with main body

The appendix is read AFTER reviewers form their opinion. Its job is to (1) answer reviewer questions before they ask, (2) provide reproducibility material, (3) house overflow content that doesn't fit in the main 8-9 pages.

### I1. Forward-pointer rule

EVERY appendix section should be referenced from the main body. If section A.4 is never mentioned in the main paper, either delete it or insert a `(see App. A.4)` pointer somewhere.

### I2. Don't introduce new claims

The appendix is for *details* and *evidence*, not for new arguments. If you find yourself making a novel claim in the appendix, move it to the main body.

### I3. Notation consistency

Variable names, function names, system names must match the main body exactly. Avoid `θ` in the main body and `\theta` in the appendix unless the formatting renders identically.

### I4. Don't repeat the abstract

The appendix should not recap the abstract or restate the contributions. It opens with structural content (TOC, overview pointer to video) and goes straight into details.

---

## J. Anti-patterns to avoid

- **No TOC at 7+ sub-sections**: reviewers will skim the appendix; without a TOC they will skip your strongest evidence.
- **Citing "Section X" without "in the main paper" or "in the appendix"**: ambiguous.
- **Missing hyperparameters for baselines**: implies you ran weak baselines.
- **No compute statement**: implies your method is too expensive to be reproduced.
- **Failure cases buried at the end**: put failures at A.1 or A.2 — show you analyzed them.
- **Appendix that's just the rejected version of the main body**: don't paste in sections you cut from the main body wholesale; refactor for the appendix audience.
- **Numbered figures that don't match between PDF and source**: re-check figure numbering after every revision pass.
- **Inconsistent figure-prefix convention**: pick `A1, A2, ...` OR continuous `6, 7, 8, ...`; never mix.
- **Bolding everything in the hyperparameter tables**: makes the table impossible to scan. Bold only the column headers, not the values.

---

## K. Construction workflow

Given that the main body is drafted, build the appendix in this order:

1. **List forward-pointers in the main body**: search the main paper for `(see App.`, `Appendix`, `see Sec. A`. Collect every appendix section the main body promises. This is your TOC.
2. **Add missing must-haves** (Section G1): hyperparameters tables, compute statement, failure cases, real-world setup.
3. **Order sub-sections**: typical ordering is (a) Qualitative Analysis → (b) Detailed Experimental Tasks → (c) Implementation Details → (d) Hyperparameters → (e) Additional Ablations → (f) Hardware → (g) Author Contributions → (h) Broader Impact. Move Failures and Qualitative to the top — strongest reviewer-bait first.
4. **Write the overview paragraph** with supplementary-video URL.
5. **Add TOC** if ≥5 sub-sections.
6. **Pre-check every cross-reference** runs both ways: main → app, app → main (when discussing).
7. **Page-budget check**: if appendix > 1.5× main body, cut.
8. **Naming convention check**: figures all `Figure A{N}` or all `Figure {N}`; tables all `Table A{N}` or all `Table {N}`; sub-sections all `A.1, A.2` or all `A, B, C`.

---

## L. Venue-specific tendencies

| Venue | Modal appendix structure |
|---|---|
| **CoRL** | TOC + Overview → Qualitative → Tasks → Hyperparameters → Ablations → Hardware → Broader Impact (5-15 pages, letter-prefixed figures common) |
| **RSS** | Less structured; often just Implementation Details + Hyperparameters + Additional Results (3-10 pages) |
| **ICRA** | APPENDIX (caps) → A. Author Contributions / B. Simulation Details / C. Evaluation / D. Real-World — compressed, often 1-4 pages |
| **IROS** | Similar to ICRA but roman-numbered continuing from main body (VII., VIII., IX.) |
| **Science Robotics** | Materials and Methods + separate Supplementary Materials with S-prefixed figures/tables; Model Card; Author Contributions are mandatory |

---

## M. Sample size and confidence

- Direct extraction: 20/63 papers with clean appendix-start markers.
- Forensic keyword presence: 35/63 mention `Appendix` or `Supplementary`.
- Manually verified examples from ~12 papers across all 5 venues.
- Most reliable patterns: hyperparameter tables (one per baseline), Author Contributions in collab papers (universal in Google DeepMind / large-team submissions), TOC at ≥5 sub-sections (consistent across 4+ examples), supplementary-video pointer (near-universal).
- Less reliable: Model Card adoption (only 1 confirmed example in corpus; pattern is normative best-practice from outside corpus); Broader Impact (only 2 confirmed examples; ICLR-imported norm).

---

## N. Quick-reference cheatsheet (for Phase 2 synthesis)

| User asks for | Use this |
|---|---|
| "Structure my CoRL appendix" | TOC + Overview (B1-B2) → Qualitative → Tasks → Hyperparameters → Ablations → Hardware → Broader Impact |
| "Hyperparameter table for {Algorithm}" | C2 pattern: two-column, `# {param}` prefix for counts, `2e-5` scientific notation, cite architectures inline `pretrained ResNet18[40]` |
| "Should I include Author Contributions?" | Yes if ≥3 authors from different institutions OR if any author is junior and needs credit visibility |
| "What goes in 'Implementation Details'?" | C1: data preprocessing → training hyperparameters → optimizer → schedule → hardware → wall-clock training time |
| "How do I write a failure case section?" | C6 pattern: bold task name (with figure-row indicator) + colon + 3-4 sentence narrative (task → failure → fix) |
| "Do I need a TOC?" | Yes if ≥5 sub-sections; B2 dotted-leader style |
| "How long should the appendix be?" | ≤1.5× main body length; CoRL 5-15 pages; ICRA 1-4 pages |
| "Should I include the supplementary video URL?" | Yes — in the Overview paragraph of section A; near-universal practice |
