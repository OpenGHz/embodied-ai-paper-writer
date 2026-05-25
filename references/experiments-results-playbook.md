# Experiments + Results — Operational Playbook

**Purpose**: How to structure and narrate experiments in an embodied-AI submission. Covers section opener, baselines, metrics, main-result reporting, ablation prose, analysis moves, real-world / qualitative results.

Use this when the user asks: "How do I structure my experiments section?", "How should I report results?", "How do I write an ablation?", "How do I describe failure modes?", "How do I narrate qualitative behaviors?"

---

## Step 1 — Open with a "we aim to answer" question list

The Experiments section opens with a 1-sentence statement of evaluation purpose followed by a numbered list of 2–4 research questions.

**Stock template**:

> `The goal of our experimental evaluation is to {test ability A} as well as {test ability B}. Concretely, we aim to answer the following questions:`
> `(1) Does {SystemName} {claim 1}, compared to {prior approach}?`
> `(2) Can {SystemName} {claim 2 under setting X}?`
> `(3) What is the influence of {design dimension} on performance?`

**Rules**:
- 2–4 questions, never more.
- Each question should map to one later subsection.
- Questions are *what we test*, NOT *what we found*. (E.g., "Can OpenVLA be effectively fine-tuned on a new robot setup?" not "OpenVLA can be fine-tuned.")

---

## Step 2 — Add a one-line setup-context anchor right after the questions

Immediately after the question list, drop a single sentence naming the *evaluation arena*: simulation vs real, # robots, # tasks, total trials.

Examples:
- `To answer these questions we conduct a total of 3600 evaluation trials across 6 different robots.`
- `Overall, we evaluated each method in 170 rollouts (17 tasks with 10 trials each) for BridgeData V2 and 60 rollouts (12 tasks with 5 trials each) for Google robot.`
- `We evaluated our method on the Daily Mobile Manipulation Task Suite both in simulation and in the real world.`

This pre-empts the reviewer's "how many trials?" instinct before any specific result lands.

---

## Step 3 — Introduce baselines under an explicit lead

Use a named heading or paragraph lead: `**Compared Methods.**` / `**Baselines.**` / `**Comparisons.**`

**Vocabulary lock**: use `baseline` / `baselines`. The words `comparator` / `comparators` / `comparative method` are virtually absent from CoRL/RSS/ICRA/IROS corpora and read as off-venue — they sound like trial-protocol writing, not robotics-paper writing. See language-phrasebank.md Section J for the substitution rule.

For EACH baseline, provide three elements in one paragraph or numbered bullet:

| Element | Content |
|---|---|
| 1. Name + citation | `RT-1-X [1]`, `Octo [5]` |
| 2. One-line mechanism summary | "a transformer policy trained from scratch on subsets of OpenX" |
| 3. (Optional) Fair-comparison note | "we use the same network architecture stated in Sec. IV" |

**Always disclose parameter counts** when comparing models of different sizes: `(35M parameters)`, `(7B vs. 55B)`. This is reviewer armor against "your model is just bigger."

---

## Step 4 — Plant the fair-comparison sentence

Somewhere in setup (typically end of "Baselines" paragraph), one sentence:

- `For a fair comparison, we used the same network architecture and fixed the initial random seeds for all methods.`
- `All evaluations are conducted as A/B evaluations, using the same tasks with the same sets of initial robot and object states.`
- `For a fair comparison, we use the same network architecture stated in Sec. IV and the same hyperparameters for baselines.`

This is the single-sentence vaccine against the most common reviewer attack: "you tuned your method but not the baselines."

---

## Step 5 — Pick subsection naming convention

Sub-headings should name *what is being evaluated* or *what claim is being made*, NOT techniques.

| Convention | Example sub-headings |
|---|---|
| **Question-style** | "In-distribution performance", "Improved generalization to OOD settings", "Design decisions" |
| **Outcome-style** | "HARMONIC MM is Efficient.", "HARMONIC MM transfers to the real world." |
| **What-is-evaluated** | "Direct Evaluations on Multiple Robot Platforms", "Data-Efficient Adaptation", "Memory-Efficient Inference via Quantization" |

A reader scanning only sub-heads should be able to recite the headline claims.

---

## Step 6 — Introduce each metric with name + symbol + direction

Stock form: `We measured {metric} ({symbol}) as the performance metric.` Always indicate which direction is good (↑ or ↓), either inline or in the table caption.

Examples:
- `We measured absolute tracking error (ATE) as the performance metric.`
- `Mean X-Displacement (MXD) ↑` / `Mean Edge Violation (MEV) ↓` (table headers)
- `We also measured the survival rate, i.e., the percentage of the robot's survival time within 30 minutes of a random walk.`

---

## Step 7 — Introduce tasks as a SET with axes of variation

Tasks are introduced collectively, framed by what axes they span.

Template:
> `We test on N tasks: A, B, C, D. These tasks span {axis 1 (e.g., visual generalization)}, {axis 2 (e.g., motion)}, {axis 3 (e.g., physical)}, and {axis 4 (e.g., semantic)} generalization.`

When tasks vary in difficulty, explicitly name the hardest and explain why — this preempts "you only did easy tasks" critiques.

---

## Step 8 — Handle sim-vs-real with persistent re-tagging

Announce the sim/real distinction in the opening anchor sentence, then **re-tag in every subsection**. Never interleave sim and real numbers in the same sentence without explicit labels.

The "zero-shot transfer" flex — used when sim-trained policy works in real — is a participial qualifier inserted into a positive-result sentence:
- `We deployed the policy (learned in simulation) in a real apartment with multiple rooms **without any adaptation or fine-tuning**.`
- `Our pipeline ... has successfully transferred to real-world apartments with novel layouts, **without any fine-tuning**.`

---

## Step 9 — Pack hardware & compute into one dense paragraph — venue-gated

Hardware specs are concentrated, not scattered. **Whether they belong in the main body or the appendix depends on the venue** (see SKILL.md rule 17).

### Step 9a — At venues that support an in-PDF appendix (CoRL / RSS / NeurIPS / ICML / ICLR / Science Robotics / Nature Robotics)

**Default**: the dense paragraph lives in the **appendix** (`Implementation Details` or `Hardware Information` subsection). The main-body Experimental Setup keeps only a 1-line pointer:

> `Hardware, control rates, training compute, and wall-clock training time are in Appendix~\ref{app:hardware}.`

Reasoning: every line spent in the main body on `single H200 in bfloat16` is a line not spent on the argument. CoRL/RSS appendix sections are explicitly designed to absorb this load.

Keep inline (in the main body) only the **load-bearing** numbers — those a reader needs to interpret the headline results:
- The robot name (`Unitree A1`) when results are robot-specific
- Sample size denominators (`n=21`, `15 held-out test`) that appear in result fractions
- Anything cited later as `(n=...)` or referenced in a table

### Step 9b — At venues without an in-PDF appendix (ICRA / IROS / RA-L / T-RO / IEEE Letters)

Cannot relegate to an `\appendix` section because there isn't one. Two options:

1. **Inline dense paragraph** (canonical structure below) — compress to ONE tight paragraph in the Experimental Setup section:

```
robot name → core sensors → control rates → onboard compute → training compute → training time
```

> `We use the Unitree A1 robot with 12 joints. For exteroception, we use the Intel RealSense D435 inside the head of the robot which captures images at 10 ± 2 Hz. We run both depth backbone (10 Hz) and the base policy (50 Hz) on the Jetson NX. The deployable policy can be trained on a single 3090 GPU in less than 20 hours.`

2. **Code-release pointer** — for the not-load-bearing config (token caps, optimizer hyperparameters, random seeds, augmentation lists):

> `Full hyperparameters, augmentation pipeline, and random seeds are in the code release at \url{https://github.com/...}.` (anonymize the URL for blind submission)

**DO NOT** write `see Appendix~\ref{app:X}` if your venue does not allow `\appendix` — reviewers will flag a dead pointer.

The "X hours on Y GPU" sentence is appreciated by reviewers checking reproducibility — keep it inline at no-appendix venues, move it to the appendix (with the rest of compute) at appendix-supporting venues.

---

## Step 10 — Reference table/figure WITH the headline number

Do not write `Table 2 shows results.` Instead, the table/figure reference and the headline number appear in the SAME sentence.

**Stock template**:
> `Table X reports {metric} across {conditions}; {our method} {verb} {baseline} by {number}.`

Examples:
- `Table I shows that HARMONIC MM makes 32.2% more progress towards completing the task at each step compared to the baselines on Cleaning Table, 113.4% on Opening Door (Push), and 27.6% on Opening Door (Pull).`
- `Fig. 3 compares the learning curves of DreamWaQ against those of all the other methods; it can be seen that even though EstimatorNet initially has a higher mean episodic reward, its performance plummets after more iterations.`

---

## Step 11 — Report deltas, not raw absolutes

Numbers should be deltas over a named baseline: `X% better than Y`, `Z× higher`, `an absolute improvement of N pp`. When you must give an absolute, immediately pair it with a baseline number.

| Form | Status |
|---|---|
| ✓ "outperforms RT-2-X by 16.5% in absolute task success rate" | Good |
| ✓ "demonstrated ∼3× generalization improvements over a model trained only on data from the evaluation embodiment" | Good |
| ✓ "17.6% (37% relative) drop in success rate compared to HARMONIC MM" | Excellent — pre-empts the "relative is misleading" critique |
| ✗ "We get 71.3%." | Bad — no context |

---

## Step 12 — Use parallel structure for multi-baseline wins

When beating several baselines, use parallel grammar in ONE sentence, not a bulleted list:

> `outperforms A by X%, B by Y%, and C by Z%`

Example: `HARMONIC MM makes 32.2% more progress on Cleaning Table, 113.4% on Opening Door (Push), and 27.6% on Opening Door (Pull).`

A reader can stop after the first delta and still get the gist; a list breaks flow.

---

## Step 13 — Always close a number with "we find / we observe"

After a table reference and a number, the NEXT sentence converts the datum into a claim:

| Trigger phrase | Function |
|---|---|
| `We find that ...` | Default — direct claim |
| `We observe that ...` | Light hedge, often before a multi-clause finding |
| `This indicates that ...` | Hand-off to interpretation |
| `This suggests that ...` | Hedged interpretation, safer than "indicates" |

**Rule**: Every numerical result paragraph must contain at least one "we find / we observe / this suggests" sentence. Without it, the paper has a data dump, not an argument.

---

## Step 14 — Report variance with ± and disclose the convention once

Stock form: `mean ± stderr` or `mean ± std`. Disclose in the methods or table caption:

> `Mean success ± StdErr computed across 33 rollouts per approach.`
> `mean and standard deviation of the reward over ten different seeds`

Standalone numbers without variance are reserved for headline takeaways in the abstract — anywhere else, include ±.

---

## Step 15 — Acknowledge negative / par results with a contextual rationale

When the proposed method does NOT win on an axis, say so AND give a reason. Pattern: `X performed as well as / worse than Y on Z, which is expected because {mechanism}.`

Examples:
- "In the large-dataset setting, the RT-1-X model does not outperform the RT-1 baseline trained on only the embodiment-specific dataset, which indicates underfitting for that model class."
- "RT-2-X achieves higher performance in semantic generalization tasks ... which is expected given that it uses larger-scale Internet pretraining data and is co-fine-tuned with both robot action data and Internet pretraining data."

Acknowledging a loss with a reason inoculates the paper against reviewers who would otherwise weaponize it.

---

## Step 16 — Use rhetorical anchors sparingly

`only / first / best across all / highest aggregate` create sortable, citable positions. **Use 0–2 of these per paper.** Overuse devalues them.

Examples:
- `OpenVLA is the only approach that achieves at least 50% success rate across all tested tasks.`
- `the only system to tackle the full competitive game for the first time.`

---

## Step 17 — Fold statistical significance INTO the claim

When p-values are reported, embed `(p < 0.05)` inside the claim sentence — never as a stand-alone "we ran a t-test" disclosure.

Example: `players who mentioned 'downspin' in their game 2 and 3 comments were significantly more likely to have won their match (p < 0.05) and also to be of a higher skill level (p < 0.001).`

---

# Ablation patterns

## Step 18 — Open each ablation with a purpose statement

Use a stock phrase: `To understand the contribution of X` / `We perform ablations to measure the influence of Y` / `We ablate the necessity of Z`.

NEVER write "We ran the following ablations." Always name what is being ablated AND tie it to a specific table.

---

## Step 19 — Organize ablations as a table with rows-as-conditions; narrate pairwise comparisons

For ablation tables with >3 rows, the prose picks 2–3 most informative pairs to discuss explicitly:

Pattern: `Comparing rows (A) and (B), we find {result}, suggesting {mechanism}.`

Examples:
- "Comparing rows (1) and (2), we find that RT-2-X outperforms RT-2 by ∼3×, suggesting that incorporating data from other robots into the training improves the range of tasks ..."
- "including a short history of images significantly improves generalization performance (row (4) vs row (5))."

---

## Step 20 — End each ablation paragraph with a "suggesting / demonstrating" sentence

| Verb | When to use |
|---|---|
| `suggesting that ...` | Default — moderate confidence |
| `demonstrating that ...` | Strong claim, when the data clearly shows the mechanism |
| `indicating that ...` | Light, factual |
| `underscoring ...` / `validating ...` | When the result confirms a hypothesis stated earlier |
| `showing that ...` | Most direct, when result is unambiguous |

Numbers don't argue; sentences do. Every ablation paragraph must end with one of these.

---

## Step 21 — Use negative framing for ablations of critical components

For load-bearing components, frame ablation as `Without X, performance drops to N (vs. M baseline)` rather than `X improves by N%`.

A 0% (or near-zero) row in an ablation table is the strongest possible evidence that a component is critical:
- `No Pretrained DINOv2: 0%` — `We substituted the DINOv2 encoder with a trainable CNN. This modification led to a significant drop in success rate ..., underscoring the critical role of a pretrained visual encoder.`

---

## Step 22 — Tell mechanistic failure stories, not just numbers

When an ablation underperforms, add WHY:

> `X performed worse, likely because Y.`
> `It performs poorly, likely due to the low-sample efficiency of training a large transformer with a ResNet18 encoder from scratch.`
> `even though EstimatorNet initially has a higher mean episodic reward, its performance plummets after more iterations because it encounters more difficult terrains after longer training iterations.`

Mechanistic stories are what reviewers remember and what differentiate an ablation from a sweep.

---

# Analysis / Discussion moves

## Step 23 — Mark every interpretive leap with "We hypothesize / We attribute"

When moving from data to interpretation, mark the move explicitly:

- `We hypothesize that ...`
- `We attribute this to ...`
- `This is likely because ...`

Multiple hypotheses can be enumerated. The marker tells the reviewer: "I know this is interpretation, not data."

---

## Step 24 — Use `Interestingly / Notably / Surprisingly` as reader bookmarks (≤3 per section)

Reserve these adverbs for results you want the reader to dwell on. Examples:
- `Interestingly, we observed that HARMONIC MM exhibited two distinct styles of pulling the door ...`
- `Notably, OpenVLA performs comparably to RT-2-X despite being an order of magnitude smaller (7B vs. 55B parameters).`
- `Surprisingly, 4-bit quantization results in similar performance as bfloat16 half-precision inference despite requiring less than half the amount of GPU memory.`

**Frequency**: 1–3 per Experiments section. Overuse devalues them.

---

## Step 25 — Close the section with a one-sentence experiments verdict

At the end of Experiments (or start of Discussion), include ONE sentence that compresses the whole experimental evaluation:

> `We presented {X} that {Y}, demonstrating {N% improvement / specific quantitative claim}.`

This sentence is citation-grade — reviewers reuse it when summarizing the paper to colleagues.

---

## Step 26 — Hedge late-stage generalization claims with `may / suggests / indicates`

When projecting from observed results to broader claims, use verb hedges:
- `... suggesting that it can be a strong default option for imitation learning tasks.`
- `Our results suggest that co-training with data from other platforms imbues the RT-2-X controller with additional skills.`
- `This may help OpenVLA attain the same level of dexterity and may be a promising direction for future work.`

The hedge plants the flag without committing to a claim that future work might falsify.

---

## Step 27 — Close the loop with the introduction

Mid-experiments, explicitly tie a specific result back to a hypothesis from the intro or method:

- `Confirming our hypothesis, HARMONIC MM not only boosts performance but also enhances efficiency.`
- `This indicates that complex tasks require simultaneous visual input for both navigation and manipulation, validating our approach of integrated navigation and manipulation.`

This rewards readers who have been tracking the thesis since page 1 — the paper feels designed, not assembled.

---

# Real-world / qualitative results

## Step 28 — Lead real-world subsections with a count + setting sentence

Real-world results inherently have small N. Front-load credibility:

> `Our learned policies were evaluated in a real apartment for {tasks}, showing promising outcomes as in Table III and Fig. 4.`
> `Our controller successfully pulled the door fully open in 9 out of 15 attempts in three different rooms.`
> `Course A was an on-campus yard ... Course B was an on-campus hill with an elevation gain of up to 22 m. Courses A and B have a total length of 430 m and 465 m, respectively.`

Pattern: `N out of M attempts in K locations` before the percentage that follows.

---

## Step 29 — Narrate behaviors as a step-by-step agent story

Qualitative results are written as step-by-step narratives of agent behavior, present tense, strong action verbs. The robot is the protagonist.

Example:
> `As the robot approaches the obstacle the stride length reduces and the robot aligns its front feet and rear feet at the correct distance from the obstacle. Next, it kicks out its rear feet with high torque and velocity to propel itself upwards. Simultaneously, it extends its front feet to clear the top of the obstacle. As soon as the front feet touch the top of the obstacle, it uses them to pull itself up.`

A blow-by-blow narrative tags the robot as an *agent with strategy*, not a policy that emits actions.

---

## Step 30 — Catalogue failure modes concretely (3–5 items)

Failure modes appear as a short numbered or comma-separated list, each tied to a specific operating regime and a brief operative cause:

> `We identified several weaknesses in the robot's capabilities, most notably (1) difficulty dealing with large amounts of underspin, (2) very fast balls, (3) very low balls due to a hard-coded constraint that prevented the paddle from getting too close to the table, and (4) that the robot was physically unable to reach balls that landed very close to the net.`

**Rules**:
- 3–5 items, no more.
- Each item names the failure regime + the operative cause.
- Reviewers rarely punish acknowledged failures; they punish denied ones.

---

## Step 31 — Tag unscripted behaviors as "emergent"

When the policy does something the authors did not explicitly reward or program, tag it as `emergent` in a separate paragraph:

> `Our simple reward functions impose no priors and the robot is free to learn emergent behaviors that would be impossible to heuristically define.`
> `These emergent behaviors showcase the spatial reasoning and scene-understanding abilities of our controller.`

Emergent behavior is the most compelling form of qualitative result — it shows the policy has internalized something general.

---

# Anti-patterns to reject

| Anti-pattern | Fix |
|---|---|
| `Table 2 shows results.` | Add the headline number: `Table 2 shows that X outperforms Y by Z%` |
| Standalone absolute numbers (`we get 71.3%`) | Pair with a baseline (`71.3%, a 16.5% improvement over Y`) |
| No "we find" sentence after a table | Insert one; without it, the paper has no argument |
| Bulleted list of multi-baseline wins | Convert to parallel-grammar sentence |
| `We ran a t-test for significance.` | Embed `(p < 0.05)` in the claim sentence |
| Listing failures only in the appendix | Acknowledge 3–5 failures in the main text |
| Mixing sim and real numbers without re-tagging | Re-tag in every subsection |
| Skipping fair-comparison sentence | Add it once in setup |
| Ablation table with no narrated pairs | Pick 2–3 row-pair comparisons; explain each |

---

# Construction workflow

1. **Draft the 2–4 research questions** (Step 1). These dictate subsection structure.
2. **Add the setup-context anchor**: count of trials, sim/real, # robots, # tasks (Step 2).
3. **List baselines** with name + mechanism + parameter count (Step 3).
4. **Plant the fair-comparison sentence** (Step 4).
5. **List metrics with direction tags** (↑/↓) (Step 6).
6. **List tasks as a set with axes of variation** (Step 7).
7. **Write hardware & compute paragraph** (Step 9).
8. **For each main result**: table-reference-with-number + we-find-sentence + delta-vs-baseline (Steps 10–13).
9. **For each ablation**: purpose statement + row-pair narration + suggesting-sentence + mechanistic-story-for-failures (Steps 18–22).
10. **Add 1–3 `Interestingly` / `Notably` flags** for results worth dwelling on (Step 24).
11. **For real-world results**: count + setting sentence, then step-by-step narrative, then emergent-behavior tag (Steps 28–31).
12. **Close with verdict sentence** (Step 25).
13. **Confirm-loop with intro** at least once (Step 27).

---

# Quick-reference

| User says | Action |
|---|---|
| "How do I open my experiments section?" | 1-sentence purpose + 2–4 numbered questions |
| "Where do I put baseline descriptions?" | First, under "Compared Methods" lead; name + mechanism + param count |
| "Should I just say 71.3%?" | No — always pair with delta/baseline |
| "How many ablation rows should I narrate?" | 2–3 pairs; not all rows |
| "How do I write failure modes?" | 3–5 items, each with operating regime + cause |
| "Where do I put sim vs real distinction?" | Opening anchor + re-tag in every subsection |
| "Is `Notably` overused?" | Yes if >3 per Experiments section |
| "How do I report p-values?" | Embed `(p < 0.05)` inside the claim sentence |
| "My ablation has no clear winner" | Use mechanistic failure story; acknowledge with rationale |
