# Closing Sections + Appendix — Operational Playbook

**Purpose**: How to write the Conclusion, Limitations, Future Work, Discussion, and Appendix of an embodied-AI submission.

Use this when the user asks: "How do I write my Conclusion?", "How do I list limitations without sounding defensive?", "What goes in the appendix?", "Do I need a Future Work section?", "Should I include Author Contributions?"

---

# PART 1 — Conclusion / Discussion

## Step 1 — Pick a header style based on item count and venue

Eight observed header styles. Pick by counting your limitations items and matching your venue.

| Items | Venue | Header style |
|---|---|---|
| 0–2 limitations | Any | **`Conclusion and Limitations`** (combined, one section) |
| 3–5 limitations | CoRL / RSS | **`Conclusion`** + **`Limitations`** (separate sections) |
| 5+ limitations | CoRL high-stakes | Same + bold mini-label per limitation |
| Science Robotics | Any count | **`Discussion`** (replaces Conclusion entirely) |
| ICRA / IROS at page limit | Any count | **`Limitations:`** + **`Conclusion:`** as inline mini-headers within Discussion's last paragraph |

**Numbering**:
- CoRL / RSS / IROS: arabic (`5 Conclusion`, `6 Limitations`)
- ICRA: roman (`VII. CONCLUSIONS`, `VI. DISCUSSION`)
- Science Robotics: no numbers OR top-level `3. DISCUSSION`

---

## Step 2 — Write the Conclusion using the 3-move recap structure

The Conclusion is **short** (60–180 words, 5–12 sentences). It states what the paper did and what's next. It does NOT introduce new claims, report new numbers, or explain.

### 3-move structure: *what we did → what we showed → what this enables*

> `We {present/propose/introduce} {SystemName}, a {one-line descriptor}. The {key innovation/contribution} is {X}. {Empirical claim}, {comparison to baseline}. {Forward-looking sentence about implications}.`

**Verified example** (Equivariant Diffusion Policy):
> "This paper studies the leveraging of symmetries in visuomotor policy learning. We propose the novel Equivariant Diffusion Policy method and provide a theoretical analysis identifying the conditions under which diffusion processes are equivariant. We also demonstrate a general framework for using SO(2)-equivariance in the 6DoF control for robotic manipulation. We evaluate our method in both simulation and the real world and show in both cases that our method outperforms the baseline Diffusion Policy by a large margin."

**Tense rule**: Abstract uses present ("we introduce"), Conclusion uses **past** ("we have presented" / "we presented"). Reviewers notice.

---

## Step 3 — Add a sign-off sentence for venue-agnostic safe close

When you do not have a separate Future Work section, end the Conclusion with one hope/aspiration sentence:

- `We hope that {release / contribution} will enable the community to {downstream goal}.`
- `We expect future work to extend the system to {X}, {Y}, and {Z}, among other directions.`
- `We hope this work will pave the way for {field-level trajectory}.`
- `{SystemName} pioneers solutions for {problem} in building a {long-term vision}.`
- `{SystemName} underscores the promising potential of {paradigm} in advancing {field}.`

**Anti-pattern**: opening the Conclusion with `In conclusion, ...`. Modern embodied-AI papers do not. Lead with `We presented ...` or `{SystemName} demonstrates ...`.

---

## Step 4 — Use the Discussion structure for Science Robotics

Discussion replaces Conclusion entirely. Three paragraphs, 200–400 words total:

| ¶ | Content |
|---|---|
| 1 | Recap: `We have presented {SystemName}, a {descriptor} that {one-line claim}.` |
| 2 | Contextualization: `Compared to {alternative-approach-class}, our method {key-difference}.` Acknowledge prior approaches. |
| 3 | Broader impact / opportunities: `We see a number of opportunities for future work. First, ... Second, ...` |

**Discussion ≠ Conclusion ×2**: Discussion must do *more* than recap — contextualize, project, situate. Reviewers reject Discussions that are just elongated Conclusions.

When positioning against an iconic system (RoboCup, RT-1, Diffusion Policy), use a bold sub-header:
> `**Comparison to RoboCup**` — followed by 1 paragraph of comparison.

Use sparingly — only when the named comparison is iconic.

---

# PART 2 — Limitations

## Step 5 — Pick the limitations format by item count

| Items | Format | Connectors |
|---|---|---|
| **1–2** | Single paragraph | `One limitation is that ...`, `Another limitation is ...`, `Finally, ...` |
| **3–4** | Prose with sequential connectors | `First, ... Second, ... Third, ... Finally, ...` |
| **4+** | Bold mini-label per item, one paragraph each | `**Reconstruction.**`, `**Retargeting.**`, `**Sensing.**`, ... |
| **Page-limited** | Inline `**Limitations:**` within Discussion's last paragraph | `+ More discussion on limitations in App. X.` pointer |

---

## Step 6 — Apply the admit-and-propose pairing rule (mandatory)

**Every limitation sentence must be followed (in the same paragraph) by a future-work mitigation sentence.** Reviewers reward this dual structure; naked admission ("we cannot do X") without forward-looking mitigation reads as defeatist.

**Template**:
> `[Limitation]: {Honest statement of weakness}.`
> `[Mitigation]: Future work could {address this by X / focus on Y / explore Z}.`

**Verified example** (OpenVLA):
> "**First**, it currently only supports single-image observations. In reality, real-world robot setups are heterogeneous, with a wide range of possible sensory inputs. **Expanding OpenVLA to support multiple image and proprioceptive inputs as well as observation history is an important avenue for future work**."

**Future-work mitigation connectors**:
- `Future work could / will / might {verb}.`
- `A promising direction for future research is to {verb-phrase}.`
- `An important avenue for future work is {gerund-phrase}.`
- `Exploring the use of {technique} {may/offer} potential remedies.`
- `One possible direction is to incorporate {technique}.`

---

## Step 7 — Name limitations as domain-nouns, not complaints

When using bold mini-label format (4+ items), label each limitation with a domain-noun in **Title Case** ending in period — NOT a complaint or confession.

✓ Good (Title Case domain nouns):
- `**Reconstruction.**`
- `**Computational Cost.**`
- `**Scaling Up.**`
- `**Sim-to-Real Gap.**`
- `**Evaluation.**`

✗ Bad (complaint confessions):
- `**Slow inference.**`
- `**Doesn't work in clutter.**`
- `**Limited training data.**`

Domain-nouns frame the limitation as a *research framing the field will work on*; complaints frame it as a personal failure.

---

## Step 8 — Sequence limitations by importance (most significant first)

The reader should not feel that you're hiding the worst limitation behind smaller ones. Lead with the most consequential.

**Anti-patterns**:
- **Empty Limitations**: "Our method has longer training time" — trivial. Include at least one methodological limitation (assumption, scope restriction, failure mode).
- **Pure-confession Limitations**: listing without future-work pairing.
- **Promotional Limitations**: disguised praise ("Our method may be too generalizable for some narrow applications"). Reviewers see through this.

---

## Step 9 — Use the "While X, Y" hedging structure for safe introduction

The `While X, Y` structure is the safest limitation-introduction sentence — concede a weakness while affirming a strength in the same breath.

- `While our method achieves {X-positive-claim}, {Y-honest-limitation}.`
- `While the policy successfully {achievement}, its accuracy tends to degrade in {failure scenario}.`
- `Our system delivers encouraging real-world results, yet several practical weaknesses remain.`
- `Our approach shows promising results, however, it still has some limitations that need to be addressed in future work.`

---

# PART 3 — Future Work

## Step 10 — Pick a Future Work location

Three locations:

| Location | When |
|---|---|
| **Inline within each limitation** | C1/C2 default — every limitation paired with a "Future work could ..." sentence |
| **Conclusion sign-off** | One-sentence hope-statement at end of Conclusion (B2 style) |
| **Standalone section after Limitations** | Heavy submissions, Science Robotics, when you have 3+ distinct future directions |

For standalone Future Work, use 2–4 named sub-directions, each with a noun-phrase title + colon:

> `**Multi-agent Soccer:** An exciting direction of future work would be to train teams of two or more agents.`
> `**Playing Soccer from Raw Vision:** Another important direction for future work is learning from on-board sensors only.`

**Anti-pattern (CoRL / RSS / ICRA)**: at page-limited venues, do NOT close the Limitations section with a standalone `\textbf{Future work.}` mini-paragraph that re-lists every limitation's mitigation. Reviewers read this as duplicated material and as Future Work "promoted" out of its source limitation paragraph. If a future-work direction maps onto an existing limitation paragraph, fold it in as the closing sentence of that paragraph (D1). Reserve a standalone block only for directions that are genuinely orthogonal to every limitation you raised.

---

# PART 4 — Coupling closing sections to the rest of the paper

## Step 11 — Match closing verbs and noun phrases to abstract and intro

The Conclusion must echo the contributions in Abstract and Introduction. Pick the same 3–4 verbs:

| Section | Verb form |
|---|---|
| Title | "Open-Source ... Vision-Language-Action Model" (noun-phrase) |
| Abstract | "We **introduce** OpenVLA, ..." (present) |
| Intro last paragraph | "We **present** OpenVLA, ..." (present) |
| Conclusion | "We **presented** OpenVLA, ..." (past) |

**Drift rule**: if Abstract says "introduce", Conclusion says "presented" or "introduced". If Abstract says "present", Conclusion says "presented".

**No new content in Conclusion**: no new acronyms, no new system names, no new numbers. If the Conclusion mentions something not in the body, reviewers will accuse you of moving the goalposts.

---

## Step 12 — Apply length budget by venue

| Section style | Words | Paragraphs |
|---|---|---|
| Standalone Conclusion (CoRL) | 60–180 | 1–2 |
| Combined Conclusion+Limitations | 150–300 | 2–3 |
| Discussion (Science Robotics) | 300–600 | 3–4 |
| Standalone Limitations (4+ items) | 250–500 | 4–7 (one per item) |
| Inline `Limitations:` + `Conclusion:` | 80–150 | 1 |
| Standalone Future Work | 200–400 | 2–4 |

**Total closing block (CoRL)**: 250–600 words ≈ half a column to one column.

---

# PART 5 — Appendix

## Step 13 — Pick appendix header by venue

| Venue | Header |
|---|---|
| CoRL most common | `Appendix` (no letter prefix) |
| When sub-sections are letter-numbered | `A    Appendix` |
| ICRA / IROS | `APPENDIX` (all-caps) |
| Science Robotics | `Supplementary Materials` + `Supplementary Methods` |

---

## Step 14 — Open with an overview paragraph + supplementary video pointer

Best-practice opener at strong CoRL/RSS papers:

> `**Overview**`
> `The appendix provides additional details, experiments, and results. Please refer to the supplemental video for real-world robot executions available at {URL}.`

**Template**: `The appendix provides {what kinds of content}. Please refer to {supplementary URL} for {what}.`

The supplementary-video pointer is near-universal. Almost every embodied-AI paper hosts videos on a Google Sites or GitHub Pages URL.

---

## Step 15 — Add a Table of Contents at ≥5 sub-sections

Dotted-leader TOC, two layout styles:

**Decimal under letter** (Fail2Progress, 17 sub-sections):
```
A.1  Qualitative Analysis ............................ A2
A.2  Detailed Experimental Tasks .................... A3
A.3  Efficiency Experiments ......................... A3
...
A.17 Hardware Information ........................... A10
```

**Letter-only with nesting** (Eureka):
```
A    Full Prompts                                       16
B    Environment Details                               16
C    Baseline Details                                  20
     C.1  L2R Reward Examples
D    EUREKA Details                                    23
     D.1  Pen Spinning Tasks
     ...
```

Below 5 sub-sections, ordering can be inferred from headers alone.

---

## Step 16 — Pick a numbering scheme and apply consistently

Three observed schemes:

| Scheme | Use when |
|---|---|
| **D1 Decimal under letter** (`A.1`, `A.2`, `A.2.1`) | CoRL/RSS default — clearest cross-referencing |
| **D2 Letter-only** (`A`, `B`, `C` with nested `C.1`) | Science Robotics style |
| **D3 Roman continuing from main body** (`VII.`, `VIII.`) | ICRA legacy |

Figure/table numbering:
- **Prefixed** (`Figure A1, A2, ...`) when ≥5 appendix figures
- **Continuous** (`Figure 6, 7, 8, ...`) when 1–3 appendix figures
- **S-prefixed** (`Suppl. Figure S1, S2, ...`) Science Robotics always

Pick one scheme; never mix.

---

## Step 17 — Include the must-haves (reviewer expectation)

These are the appendix sections reviewers will check for. Missing any of these signals irreproducibility:

| Must-have | What to include |
|---|---|
| **Hyperparameters** | One table per algorithm (method + every baseline). Two-column: name (left), value (right). |
| **Compute budget** | GPU type + count + training hours. One paragraph or table. |
| **Random seeds statement** | `All experiments use 3 random seeds. We report mean and standard error.` |
| **Real-world setup** | Photo or diagram, with SKUs / dimensions / control rates. |
| **Failure cases** | At least one figure or example with diagnostic prose. |
| **Per-task descriptions** | One paragraph per task: success criterion + randomization. |
| **Dataset license / source** | If using or releasing a custom dataset. |

---

## Step 18 — Use the hyperparameter-table conventions

Conventions for hyperparameter tables (one per algorithm):

- **Two-column** layout: parameter name (left), value (right)
- **Bold not used** in table body — only column headers
- **`#` prefix for counts**: `# encoder layers`, NOT `Number of encoder layers`
- **Scientific notation for learning rates**: `2e-5`, NOT `0.00002`
- **Cite architecture sources inline**: `pretrained ResNet18[40]`, NOT `ResNet18`
- **Compact augmentation lists**: `RandomCrop(ratio=0.95) & ColorJitter(brightness=0.3, contrast=0.4, saturation=0.5) & RandomRotation(degrees=[-5.0, 5.0])`

Caption: terse two-word `Hyperparameters of {AlgorithmName}.`

---

## Step 19 — Order appendix sub-sections to put strongest evidence first

Recommended ordering (CoRL modal):

1. **Qualitative Analysis** (failures + successes) — strongest reviewer-bait
2. **Detailed Experimental Tasks**
3. **Implementation Details**
4. **Hyperparameters**
5. **Additional Ablations**
6. **Hardware Information**
7. **Author Contributions** (if multi-institution)
8. **Broader Impact** (if venue mandates)

Move Failures and Qualitative Analysis to the top — these are what skeptical reviewers will read first.

---

## Step 20 — Write the appendix sub-section types in their canonical forms

### Implementation Details (C1)
> Data preprocessing → training hyperparameters → optimizer → schedule → hardware → wall-clock training time.

### Network Architecture (C3)
Walk through the network in **input-to-output order**, with explicit tensor dimensions at each stage:
> `Our RGB observations initially get processed by DinoV2 model, generating 768 × 16 × 16 features which pooled to a reduced dimension of 768 × 7 × 7. ...`

### Reward / Loss formulation (C4)
**Math first**, then prose paragraph defining every variable:
> `R_manip = δ w_manip_shaping R_manip_shaping + w_progress ΔP + γ R_finish_task`
> `The variable δ is 1 if the end effector has not reached the target region, and 0 otherwise.`

### Visual Augmentation (C5)
One paragraph, bold transform name + colon + parenthetical hyperparameters + semicolon separator:
> `**ColorJitter**: Adjusts brightness (0.4), contrast (0.4), saturation (0.2), and hue (0.05); **GaussianBlur**: Applies a blur effect with a kernel size of (5,9) and sigma range of (0.1,2); ...`

### Qualitative Analysis / Failure Cases (C6)
Pattern: bold task name (with figure-row indicator) + colon + 3–4 sentence narrative (task → failure mode → fix):
> `**Hierarchical Tabletop Organization task (First row)**: The robot is tasked with organizing the cups and capsules ... In the failure case, the robot fails to recognize the correlation between cups and capsules. After learning from this failure, Fail2Progress successfully completes this task by understanding that ...`

### Per-task descriptions (C8)
**TaskName** + present-tense verb + description + success criterion. One paragraph per task:
> `**Multi-object Transport** tasks the robot to transport multiple objects within a container using a single skill. To succeed, the robot has to understand that all objects inside the container move together when the container is moved.`

### Prompts (C10, for LLM-based methods)
Numbered `Prompt 1:`, `Prompt 2:` with a noun-phrase descriptor + verbatim prompt content in code-block:
> `Prompt 1: Initial system prompt`
> `You are a reward engineer trying to write reward functions to solve reinforcement learning tasks ...`

### Compute Resources (C11)
> `Our models are trained on servers with 72 vCPU AMD EPYC 9754 128-Core Processor, 4 RTX 4090D (24GB), and 240 GB memory. Training on each map takes less than 12 hours.`

### Author Contributions (C12)
Bold author name + superscript affiliation/role markers + colon + 1–3 sentences starting with past-tense verbs (Developed, Built, Wrote, Conceived, Implemented):
> `**David B. D'Ambrosio**¹,∗: Worked on all parts of the system over the course of many years. Developed the policy architecture and training approach. Conceived, wrote, and edited this paper.`

Footer pattern explains role markers:
```
¹Primary contributors
∗Corresponding authors (order randomized, equal contributions)
²Core contributors (Alphabetized)
```

### Broader Impact (C14)
3-move structure — what we did → why it matters → what the community should consider. 1–2 paragraphs.

---

## Step 21 — Use canonical sentence patterns specific to the appendix

### Section-opening sentences
- `In this section, we provide {what}.`
- `In this section, we {verb} {what}.`
- `Here, we {verb} {what}.`
- `This section describes / presents / provides {what}.`

### Figure-referencing sentences
- `Figure {N} shows {what}.`
- `We visualize {what} in Figure {N}.`
- `Fig. {N} shows {what}.` (IROS/ICRA terse)
- `See Figure {N} for {what}.`

### Table-referencing sentences
- `Table {N} contains {what}.`
- `The hyperparameters are listed in Table {N}.`
- `We report {metric} in Table {N}.`

### Forward-pointer from main body to appendix
- `See Appendix X for more details.`
- `See Sec. A.{N} for {what}.`
- `(see App. {N})` / `(App. {N})` — most space-saving
- `(more discussion on limitations in App. E)` — PoliFormer pattern

**ALWAYS include forward-pointers** — reviewers need to know where to look.

### Verbatim-data sentences (parameter dumps)
- `For all tasks, we use w_nav = 1, R_reach = 2, ...`
- `For opening door/fridge tasks, we use w_progress = 80. For the cleaning table task, we use w_progress = 100.`

---

## Step 22 — Cross-references must specify "main paper" vs "appendix"

When the appendix discusses something analyzed in the main body, use:
- `(see also Sec. {N} in the main paper)`
- `as discussed in Sec. {N}`
- `(see Fig. {N})`

**Never use bare `Section 3`** — always indicate whether it's in the main body or the appendix.

---

## Step 23 — Apply the page-budget rule

| Venue | Typical appendix length |
|---|---|
| **CoRL** | 5–15 pages (9 pages main + 5–15 supplementary is modal) |
| **RSS** | 3–10 pages |
| **ICRA** | 1–4 pages (heavy compression) |
| **IROS** | 1–4 pages |
| **Science Robotics** | 15–30 pages (strict structure) |

**Rule**: appendix should NOT exceed **1.5× main body length**. An appendix that runs 30+ pages signals lack of editing.

---

# Appendix anti-patterns

| Anti-pattern | Fix |
|---|---|
| No TOC at 7+ sub-sections | Add dotted-leader TOC |
| `Section X` without `in the main paper` or `in the appendix` | Specify; ambiguity confuses reviewers |
| Missing hyperparameters for baselines | Add a table per baseline — implies you ran weak baselines otherwise |
| No compute statement | Add CPU/GPU + memory + training time |
| Failure cases buried at end | Move Failures to A.1 or A.2 — show you analyzed them |
| Appendix that's just rejected main-body sections pasted in | Refactor for appendix audience |
| **Writing-process archaeology** — `\paragraph{Within-run baseline sanity check.}` or similar, reporting baselines that were considered then dropped, internal experiment codenames (`E02`, `Phase 1`, `Attempt 001`), candidate Δs that were superseded, "originally we used X but switched to Y" justifications, or even softer hedges like "the most conservative of the candidates we considered" | **Delete the paragraph entirely.** In the main-body Baselines paragraph, define the baseline as the *maximum over a named set* — `The Naked-Modality VLM is the strongest of {video, proprio, video+proprio} rows from the modality ablation` — and stop. The upper-bound construction is the anti-cherry-picking signal; commentary about "candidates we considered" reintroduces the suspicion you just defused. If the comparison across baseline choices is load-bearing, promote it to a full named ablation subsection + table — never bury it in the appendix. See SKILL.md rule 19. |
| Inconsistent figure-prefix convention (mixing `Figure A1` and `Figure 8`) | Pick one and apply throughout |
| Bolding every value in hyperparameter tables | Bold only column headers, never values |
| New claims in the appendix | Move to main body or delete |
| Section A.4 with no forward-pointer from main body | Either delete A.4 or insert `(see App. A.4)` in main body |
| Restating abstract / contributions in appendix opening | Open with structural content (TOC, overview, video URL) only |

---

# Construction workflow — Closing sections

1. **Pick header style** (Step 1) based on venue + limitations item count.
2. **Draft Conclusion recap** (Step 2) in 5–12 sentences. Past tense. No new numbers.
3. **List limitations in scratch** — raw items, 3–5 typical (Step 5).
4. **Pair each limitation with future-work mitigation** (Step 6). If you cannot write the mitigation, re-frame the limitation or drop it.
5. **Sequence limitations by importance** (Step 8). Most significant first.
6. **Choose connector style** (Step 5): `First/Second/Finally` for 3–4 items in prose; bold mini-labels for 4+ items.
7. **Add sign-off sentence** (Step 3) to Conclusion: `We hope ...` / `We expect future work to extend ...`
8. **Verify coupling** (Step 11): same verbs and noun phrases as Abstract / Intro contributions list. Past tense in Conclusion.

# Construction workflow — Appendix

1. **List forward-pointers from main body** — search main paper for `(see App.`, `Appendix`, `see Sec. A`. Collect every section the main body promises. This is your TOC seed.
2. **Add must-haves** (Step 17): hyperparameters, compute, failures, real-world setup, per-task descriptions, dataset license.
3. **Order sub-sections** (Step 19): Qualitative → Tasks → Implementation → Hyperparameters → Ablations → Hardware → Author Contributions → Broader Impact.
4. **Write overview paragraph + video URL** (Step 14).
5. **Add TOC** if ≥5 sub-sections (Step 15).
6. **Apply canonical sentence patterns** for each sub-section type (Step 20).
7. **Pre-check cross-references** run both ways: main → app, app → main.
8. **Page-budget check** (Step 23): cut if appendix > 1.5× main body.
9. **Naming consistency**: all figures `Figure A{N}` or all `Figure {N}`; all tables likewise; all sub-sections `A.1, A.2` or all `A, B, C`.

---

# Quick-reference

| User says | Action |
|---|---|
| "Write a CoRL Conclusion" | 3-move recap, 80–150 words, past tense, no new numbers, end with hope sentence |
| "Write a Limitations section with 4 items" | Bold mini-label per item, domain-noun labels in Title Case, each paragraph = limitation + future-work mitigation |
| "I'm at page limit, where do I cut Limitations?" | Inline `**Limitations:**` then `**Conclusion:**` in one paragraph + `(more discussion in App. X)` pointer |
| "Science Robotics is asking for Discussion" | 3-paragraph structure: recap → contextualize → opportunities. 300–500 words. |
| "How do I end the Conclusion?" | `We hope that {release/method} will enable {community-level goal}.` OR `We expect future work to extend to X, Y, Z, among other directions.` |
| "Reviewer says my limitations sound defensive" | Pair each limitation with `Future work could ...` mitigation in the same paragraph |
| "How long should the closing block be?" | CoRL: 250–400 words. ICRA/IROS: 100–200. Science Robotics: 400–700. |
| "Do I need a Future Work section?" | Only if Discussion is short OR you have 3+ distinct future directions. Otherwise fold into Limitations (per-item) or Conclusion sign-off. |
| "Structure my CoRL appendix" | TOC + Overview (video URL) → Qualitative → Tasks → Hyperparameters → Ablations → Hardware → Broader Impact |
| "Hyperparameter table for {Algorithm}" | Two-column, `# {param}` prefix for counts, `2e-5` notation, cite architectures inline |
| "Should I include Author Contributions?" | Yes if ≥3 authors from different institutions OR any junior author needs visible credit |
| "Do I need a TOC?" | Yes if ≥5 sub-sections; dotted-leader style |
| "How long should the appendix be?" | ≤1.5× main body. CoRL 5–15 pages. ICRA 1–4 pages. Science Robotics 15–30 pages. |
| "Should I include the supplementary video URL?" | Yes — in Overview paragraph; near-universal practice |
| "Where do failure cases go in the appendix?" | A.1 or A.2 — strongest reviewer-bait first |
| "Tense for Abstract vs Conclusion?" | Abstract: present (`we introduce`). Conclusion: past (`we presented`). |
| "Should I include a Model Card?" | At TMLR / Science Robotics / Nature Robotics: yes. Other venues: optional polish. |
| "Should I include Broader Impact?" | ICLR-adjacent: yes. CoRL: increasingly yes. ICRA / IROS: rare. |
