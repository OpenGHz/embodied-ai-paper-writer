# Language Phrasebank

**Purpose**: A rhetorical-function phrasebook for embodied-AI papers. Use this when you're stuck mid-sentence: look up the rhetorical move, copy a template, fill the slots.

Use this when the user asks: "How do I phrase X?", "What's a better way to say Y?", "Give me an opener / pivot / contribution sentence", "How do I report a result?", "What connector should I use?"

**How to read templates**: `[SLOT]` = mandatory fill-in. `[A/B/C]` = pick one. `(optional)` = sometimes omitted.

---

## A. Openers (Introduction first sentence)

### A1. Broad-challenge opener
For first or second sentence of Intro — identify an accepted weakness in the status quo.

Templates:
- `A key [weakness / limitation / challenge] of [SUBJECT] is [their / its] inability to [DO X].`
- `[SUBJECT] is a long-standing [challenge / problem] (in [FIELD]).`
- `A [persistent / major / fundamental] challenge is that [CLAUSE].`
- `Despite [RECENT PROGRESS], [GAP CLAUSE].`

Verbatim examples (corpus):
- "A key weakness of learned policies for robotic manipulation is their inability to generalize beyond their training data..."
- "Dexterous manipulation has been a long-standing research challenge..."
- "However, a persistent challenge is that the finite datasets used to develop these systems are unlikely to capture the limitless variety of the real world..."

### A2. Deployment-promise opener
Optimistic, momentum-establishing first sentence. Best for foundation-model / scaling / position papers.

Templates:
- `[Large / Foundation] [MODELS / POLICIES] [trained / pretrained] on [SCALE / DATA] have the [potential / promise] to [CHANGE / ENABLE X].`
- `Recent advances in [FIELD] have [led to / enabled / produced] [NEW CAPABILITY].`
- `[FIELD] has seen [rapid / considerable / remarkable] [progress / advances] in [RECENT YEARS].`

Examples:
- "Large policies pretrained on a combination of Internet-scale vision-language data and diverse robot demonstrations have the potential to change how we teach robots new skills..."
- "Foundation models ... trained on internet-scale data possess zero-shot generalization capabilities that make them a promising technology towards detecting OOD failures..."

### A3. Scenario / concrete-failure opener
When the abstract problem is hard to grok without an image.

Templates:
- `Consider [SCENARIO]: [the robot must DO X], (yet/but) [PROBLEM].`
- `[SCENARIO DESCRIPTION—2-3 sentences]. Undertaking such tasks in [CONDITION] — where [VARIATION] — underscores the critical need for [CAPABILITY].`
- `For example, a [robot] cannot [DO X] even if [Y].`

Use when: scenario is *evocative but technical* — name a specific failure mode (sensor noise, distractors, clutter, occlusion). Avoid generic "imagine a robot that...".

### A4. The "Yet / However" pivot (the all-important second move)
After A1/A2/A3, you almost always need a pivot. This is THE most reliable rhetorical structure in embodied-AI papers.

Templates:
- `[OPTIMISTIC SETUP]. Yet / However / Nevertheless, [PROBLEM / GAP].`
- `While [PRIOR WORK X], [LIMITATION].`
- `Despite [PROGRESS], [GAP].`
- `Fully realizing this promise, however, poses two challenges: (i) [C1], and (ii) [C2].`

Examples:
- "Yet, widespread adoption of VLAs for robotics has been challenging as (1) existing VLAs are largely closed and inaccessible to the public, and (2) prior work fails to explore methods for efficiently fine-tuning..."
- "Fully realizing this promise, however, poses two challenges: (i) mitigating the considerable computational expense of these models such that they may be applied online, and (ii) incorporating their judgement regarding potential anomalies into a safe control framework."

**Pick `Yet`** (terser, slightly more literary) **or `However`** (more formal). `Nevertheless` reads as overformal.

---

## B. Stating contributions

### B1. Enumerated contributions (canonical)
Templates:
- `Our contributions are [threefold / fourfold / as follows]: (1) ...; (2) ...; (3) ...`
- `In summary, our contributions are: (1) ...; (2) ...; (3) ...`
- `The main contributions of this paper are: 1) ...; 2) ...; 3) ...`

Examples:
- "As such, our contributions are threefold: 1) Fast reasoning with embeddings: ...; 2) Slow reasoning through autoregressive generation: ...; 3) Hierarchical multi-contingency planning: ..."
- "Our contributions are as follows: 1) we propose Equivariant Diffusion Policy, a novel BC approach..."

**Each item starts with a verb-noun**: "We introduce X", "We demonstrate Y", "We release Z".

### B2. The "To this end, we [verb] [SYSTEM]" bridge sentence
Templates:
- `To this end, we [introduce / propose / present] [SYSTEM NAME], a / an [DESCRIPTOR] for [TASK].`
- `To address [CHALLENGES / GAP], we [present / propose] [SYSTEM NAME].`
- `Addressing these challenges, we [introduce / present] [SYSTEM NAME].`

Examples:
- "To this end, we introduce OpenVLA, a 7B-parameter open-source VLA that establishes a new state of the art for generalist robot manipulation policies."
- "To address these challenges, we present AESOP, an anomaly detection and reactive planning framework..."

### B3. Verb family for introducing the work — pick deliberately

| Verb | Register | Use when |
|---|---|---|
| **present** | Formal, neutral | Unveiling a whole system or framework |
| **propose** | Slightly more conservative | The contribution is a method/algorithm |
| **introduce** | Mid-formal, signals novelty | New dataset, benchmark, formulation |
| **develop** | Engineering tone | Required substantial engineering |
| **build** | Casual, hardware-flavored | Hardware artifact |
| **demonstrate** | Strong, result-claim | Claiming an empirical outcome |
| **show** | Mid-strength | Same as demonstrate, slightly less formal |

Be consistent: if the abstract says "present", the introduction's bridge should also say "present" (or one well-chosen synonym).

### B4. Descriptor adjective clusters (after the verb)

After `We {verb} {SystemName}, a/an ___ ___ ___ for ___,` choose 2 (max 3) adjectives that **do work**:

| Cluster | Examples |
|---|---|
| **Scale-first** | `7B-parameter`, `970k-trajectory`, `large-scale`, `low-cost`, `open-source` |
| **Capability-first** | `generalist`, `general-purpose`, `zero-shot`, `real-time`, `bimanual`, `dexterous` |
| **Style-first** | `simple yet scalable`, `end-to-end`, `closed-loop`, `unified` |
| **Substrate-first** | `transformer-based`, `diffusion-based`, `RL-based` |

**Avoid**: `Novel`, `New`, `Simple`, `Powerful` alone — reviewers strip these mentally. Pair with a measurable claim if you use them ("simple yet scalable" works because *scalable* is measurable).

---

## C. Reviewing prior work

### C1. Topic-first section/paragraph openers
Templates:
- `[Topic Name]. [TOPIC-AREA] has seen [growing / considerable] interest in recent years.`
- `[Topic Name]. A recent trend in [FIELD] is [TREND DESCRIPTION].`
- `[Topic Name]. A number of recent works [VERB] [...].`
- `[Topic Name]. Prior work [in / on] [SUBTOPIC] [VERB] [DESCRIPTION].`

Topic name should appear bolded or italicized as a paragraph label (CoRL/RSS/ICRA/IROS convention).

### C2. Citation grouping ("[A,B,C] do X, while [D,E] do Y")
Templates:
- `[NUMERIC CITES] [VERB] [APPROACH X], while [CITES] [VERB] [APPROACH Y].`
- `Some methods [VERB] [X] [CITES]; others [VERB] [Y] [CITES].`
- `A number of works [VERB] [X] [CITES]. In contrast, [OTHER WORKS] [VERB] [Y] [CITES].`

Workhorse: lets you cite 5–10 papers without listing them mechanically.

### C3. The positioning pivot ("Unlike these works, ...")
Templates:
- `Unlike [PRIOR APPROACH / WORKS], [OUR WORK / WE] [DIFFERENTIATOR].`
- `In contrast (to [REF]), [OUR WORK] [VERB] [DIFFERENT THING].`
- `A key difference between [these approaches] and [OUR SYSTEM] is [DIFFERENCE].`
- `By contrast, with [OUR METHOD], [PROPERTY].`

Required in every related-work paragraph. Place at the END (after grouping cites in C2).

### C4. Gap-naming verbs ("remain limited", "fail to", "do not address")
Templates:
- `[PRIOR WORK] [remains limited / falls short / fails to / does not address / has not explored] [THING].`
- `Existing works do not [VERB] [...].`
- `(However,) the [adoption / scaling / deployment / grounding] of [X] [has not been a focal point / remains open].`

Pair C4+C3 as the standard refrain: "Prior work X is limited because Y. Unlike these works, we Z."

### C5. "Recent work has shown" (citing as evidence, not as comparator)
Templates:
- `Recent work has shown that [CLAIM] [CITES].`
- `[CITES] [demonstrate / show] that [CLAIM].`
- `It has been [shown / demonstrated / established] that [CLAIM].`

When the cited work is NOT a competitor — you're leveraging prior results.

---

## D. Introducing the method

### D1. Architectural roadmap
Templates:
- `Our [approach / method / system / framework] consists of [N] [components / modules / stages]: [LIST WITH SHORT DESCRIPTIONS].`
- `[SYSTEM] introduces [N] [technical innovations / key components]. First, [...]. Second, [...]. Third, [...].`
- `At a high level, [SYSTEM] [VERB] [INPUT] and [VERB] [OUTPUT] via [PIPELINE DESCRIPTION].`

Always pair with a figure reference (`Figure X illustrates our approach.`). The enumeration must match the figure boxes.

### D2. Temporal walk-through ("We first... then... finally...")
Templates:
- `We first [VERB] [STEP 1]. Then, we [VERB] [STEP 2]. Finally, we [VERB] [STEP 3].`
- `The pipeline proceeds as follows: [VERB] [...], [VERB] [...], and [VERB] [...].`

Use "first / then / finally" — NOT "secondly / thirdly" (sounds undergraduate). One per Method section.

### D3. Problem formulation ("Given X, we aim to...")
Templates:
- `Given [INPUT], we aim to [OUTPUT].`
- `We consider the [problem / setting / class] of [DESCRIPTION].`
- `Our goal is to [VERB] [...].`
- `In each [scene / episode / trial], the [agent / robot] is given [INPUT]. The agent's goal is to [OUTPUT].`

### D4. Notation setup ("Let X denote...")
Templates:
- `Let [SYMBOL] denote / be [DESCRIPTION].`
- `We denote [DESCRIPTION] by [SYMBOL].`
- `[SYMBOL] ∈ [SPACE] [represents / denotes] [DESCRIPTION].`
- `In what follows, [SYMBOL_1] is [...], and [SYMBOL_2] is [...].`

Two rules: define before first use; one symbol per concept (no overloading).

### D5. Design rationale ("To address X, we...")
Templates:
- `To [enable / handle / address / tackle] [PROBLEM], we [VERB] [SOLUTION].`
- `Our solution is to [VERB] [...].`
- `We choose to [VERB] [...] because [REASON].`

2–3 of these per Method section is plenty.

### D6. Building-on prior components
Templates:
- `We build [on / upon] [PRIOR WORK / COMPONENT].`
- `Our [SYSTEM] [adopts / borrows / inherits] [TECHNIQUE] from [REF].`
- `Following [REF], we [VERB] [...].`
- `[SYSTEM] follows the same standard architecture as [REF] ... with [MODIFICATION].`

"We build on X" is NOT a weakness — it's good scholarship.

---

## E. Reporting results

### E1. Evidence pointers ("Table X reports..." / "Figure X shows...")
Templates:
- `Table [N] [reports / shows / summarizes / presents] [WHAT].`
- `Figure [N] [illustrates / shows / depicts / visualizes / plots] [WHAT].`
- `We [report / present] [WHAT] in [Table / Figure N].`
- `As [shown / illustrated / depicted] in [Table / Figure N], [CLAIM].`

Vary the verbs to avoid monotony.

### E2. Headline-result verb family

| Verb | Strength | Use |
|---|---|---|
| **achieves** | Mid-strong, neutral | "achieves 75% success" — workhorse |
| **outperforms** | Strong, comparative | "outperforms X by Y%" |
| **improves over** | Strong, comparative | Like outperforms, slightly softer |
| **surpasses** | Strong, formal | "surpasses chain-of-thought reasoning..." |
| **matches** | Equivalent claim | "matches a 10× larger model" |
| **exceeds** | Strong, formal | "exceeds prior state-of-the-art" |
| **boosts / improves** | Process verb | "boosts performance by X" |
| **reduces** | Inverse direction | "reduces error by X%" |
| **establishes** | Very strong | "establishes a new state of the art" — use sparingly |
| **sets** | Strong | "sets a new state of the art" |

Templates:
- `[SYSTEM] achieves [METRIC] of [VALUE] [on / across] [TASKS].`
- `[SYSTEM] outperforms [BASELINE] by [DELTA] (absolute / relative).`
- `[SYSTEM] [improves / reduces] [METRIC] by [VALUE]% over [BASELINE].`
- `[SYSTEM] establishes a new state of the art [on / for] [TASK].`

### E3. Quantitative phrasings (deltas, units, hedges)

Templates:
- `by [X]% [absolute / relative]`
- `by a margin of [X]%`
- `by a [large / significant / substantial] margin`
- `[N]× faster / smaller / cheaper than [B]`
- `[X]-fold improvement / reduction`
- `with [N]× fewer parameters / smaller dataset / less compute`
- `on average, [X]`
- `Mean ± StdErr across [N] tasks, [N] seeds`
- `across [N] [seeds / trials / tasks / episodes]`

**Always specify absolute vs. relative** explicitly. Confusing 16% absolute with 16% relative is a credibility-destroyer.

### E4. Interpretation verbs ("We observe..." / "We find...")

| Verb | Strength | Use |
|---|---|---|
| **We find that** | Mid; common | Confirmed empirical claim |
| **We observe that** | Mid; observational | Descriptive pattern in the data |
| **We show that** | Strong | Result-claim with experiment |
| **We demonstrate that** | Strong | Result-claim with behavior |
| **This suggests that** | Hedged | Tentative implication |
| **This confirms that** | Strong | Validation of prior hypothesis |
| **This indicates that** | Mid | Drawing an implication |
| **Importantly, we observe** | Emphatic | Unexpected / critical finding |
| **Surprisingly, we find** | Emphatic | Counterintuitive finding |
| **Interestingly, we find** | Mid emphatic | Noteworthy finding |
| **Notably,** | Highlighting | Pointing at a key result |

Each results paragraph should contain at least one interpretation sentence.

### E5. The standard results paragraph (template)

Most strong Results paragraphs follow this 4-sentence schema:

1. **Pointer**: `Table 2 reports the success rates across N tasks.`
2. **Headline**: `Our method achieves Y% success, outperforming [BASELINE] by Z% absolute.`
3. **Detail**: `In particular, on [HARD TASK], we observe a [larger / smaller] gap of W%.`
4. **Interpretation**: `This suggests that [MECHANISM] [is responsible for / underlies] the improvement.`

### E6. Real-vs-sim / generalization claims
Templates:
- `[SYSTEM] generalizes to [UNSEEN X] without [adaptation / retraining].`
- `[SYSTEM] [transfers / deploys] zero-shot to [REAL ROBOT / NEW SCENE].`
- `Despite being trained purely in simulation, [SYSTEM] [VERB] [...].`

Generalization claims must be quantified ("on N unseen categories", "in K novel scenes") — never abstract.

---

## F. Ablations

### F1. Setting up the ablation
Templates:
- `To understand the contribution of [COMPONENT], we [ablate / remove / replace] [COMPONENT].`
- `We perform an ablation study [regarding / on] [TARGET].`
- `In this section, we ablate [several / key] design choices [used] in [SYSTEM].`
- `To investigate [QUESTION], we [VERB] [...].`

### F2. Reporting the ablation delta
Templates:
- `Removing [COMPONENT] [results in / leads to / causes] [Y] [degradation / drop].`
- `Without [COMPONENT], [SYSTEM] [VERB] [...].`
- `Replacing [A] with [B] [VERB] [...].`
- `[Component A] contributes [X]% [absolute / relative] [improvement].`

### F3. Ablation inference verbs (closing sentence)
Templates:
- `This [confirms / suggests / indicates / demonstrates] that [INTERPRETATION].`
- `This validates [DESIGN CHOICE].`
- `These results [highlight / emphasize] the importance of [COMPONENT].`
- `In line with [PRIOR WORK], we find [...].`

- **confirms**: ablation matches a prior hypothesis
- **suggests**: result is consistent with an explanation but doesn't prove it
- **indicates / demonstrates**: when the gap is large and clear

---

## G. Limitations & failure modes

### G1. Naming the limitation
Templates:
- `A key limitation [of our work] is [DESCRIPTION].`
- `One limitation of [SYSTEM] is [DESCRIPTION].`
- `Another limitation is that [DESCRIPTION].`
- `While [STRENGTH], [SYSTEM] [VERB] [LIMITATION].`

Be specific. "Our method may not generalize" is weak; "Our method requires 50 demonstrations per task" is useful.

### G2. Failure modes (concrete claims)
Templates:
- `Failure cases include [LIST].`
- `The main failure modes are [LIST].`
- `[SYSTEM] [fails / struggles] [in / to / when] [SETTING / CONDITION].`
- `[SYSTEM] cannot [VERB] [WHEN CONDITION].`

For every named limitation, give one concrete failure example.

### G3. Future-work formulations
Templates:
- `We leave [TOPIC / EXTENSION] for future work.`
- `Future work [will / could / can / should] [VERB] [...].`
- `An interesting [direction / area] for future work is [...].`
- `A promising direction for future work is [...].`
- `We hope [FUTURE WORK] will [VERB] [...].`

2–4 directions, each tied to a specific limitation. Avoid generic "we will scale up" lines.

### G4. Hedging the contribution ("while X, ...")
Templates:
- `While [STRENGTH], [LIMITATION].`
- `Despite [STRENGTH], [LIMITATION].`
- `Although [STRENGTH], [LIMITATION].`
- `[SYSTEM] [achieves X], but [PROBLEM].`

---

## H. Transitions / discourse connectors

### H1. Single-word connector reference table

| Connector | Function | Example |
|---|---|---|
| **Specifically** | Narrowing from general to particular | "Specifically, we concatenate the 14-dim observation..." |
| **Concretely** | Narrowing to a concrete instance | "Concretely, our main contributions are:" |
| **In particular** | Highlighting a sub-case | "In particular, every step of our policy relies only on observations available on-board." |
| **Notably** | Flagging a surprising/important detail | "Notably, Octo trains a generalist policy..." |
| **Crucially** | Strong emphasis on load-bearing detail | "Crucially, we carefully control the loss magnitudes between domains." |
| **Importantly** | Flagging important observation | "Importantly, we observe that OpenVLA can..." |
| **Surprisingly** | Counterintuitive finding | "Surprisingly even outperforming the human-expert-curated data mix..." |
| **Interestingly** | Noteworthy finding | "More interestingly, we find that weighting datasets..." |
| **Moreover** | Adding a second supporting point | "Moreover, we find that selecting a reference model..." |
| **Furthermore** | Adding another point (formal) | "Furthermore, the target root reference during train time..." |
| **In addition** | Adding evidence (neutral) | "In addition, we include a baseline that uses Y." |
| **Additionally** | Adding evidence (colloquial) | "Additionally, our method takes 10s on average." |
| **However** | Contrast / counter-evidence | "However, OpenVLA performs comparably or better in..." |
| **Yet** | Mild contrast (literary) | "Yet, widespread adoption of VLAs has been challenging..." |
| **In contrast** | Strong contrast | "In contrast, we found it important for VLA training to iterate..." |
| **On the other hand** | Symmetric two-sided contrast | "On the other hand, CLIP struggles far more..." |
| **Conversely** | Strong logical inversion | "Conversely, the latter methods either operate offline..." |
| **Consequently** | Logical consequence | "Consequently, it copies them directly from the specialized skill." |
| **Hence** | Logical consequence (concise) | "Hence, no penetrations between the robots and obstacles are possible." |
| **Thus** | Logical consequence (math) | "Thus, at frame t, a human is defined by:" |
| **Therefore** | Logical consequence (explicit) | "Therefore, we propose a closed-loop control framework..." |
| **As such** | Setting up a contribution | "As such, our contributions are threefold:" |
| **As a result** | Causal outcome | "As a result, performance dropped." |
| **For example / e.g.** | Concrete instance | "For example, a quadrotor cannot safely land..." |
| **For instance** | Concrete instance (formal) | "For instance, the policy can fail when X." |
| **First / Second / Third** | Enumeration | "First, we apply a data-driven approach... Second, ..." |
| **To this end** | Bridge to your solution | "To this end, we introduce OpenVLA..." |
| **Instead** | Replacement of prior approach | "Instead, recent work showed that LLMs may provide..." |
| **Indeed** | Confirmation of prior claim | "Indeed, our experiments confirm..." |
| **Beyond X** | Extension move (broadening scope) | "Beyond robotics, existing foundation models..." |
| **In line with** | Aligning with prior result | "In line with prior work, we find..." |

### H2. Inter-paragraph transitions
Templates:
- `Building on [PRIOR PARAGRAPH'S RESULT], we [...].`
- `Beyond [PRIOR TOPIC], we [...].`
- `Having [VERBED] [TOPIC], we now turn to [NEW TOPIC].`
- `[Earlier / In the previous section], we [VERBED] [...]. Here, we [...].`

Avoid: "Also," / "Another thing is," — read as conversational.

---

## I. Hedging — calibrated confidence

| Hedge | Meaning | Use when |
|---|---|---|
| `may / could / can` | Modal possibility | Speculating about extensions |
| `likely` | Probabilistic | One-off observation with reasonable mechanism |
| `suggests / indicates` | Inferential | Drawing implication from data |
| `appears to / seems to` | Observational hedge | Behavior not yet measured |
| `tends to` | Frequency hedge | Common but not universal |
| `often / typically` | Frequency claim | Common case |
| `to the best of our knowledge` | Coverage hedge | First-claim preface |
| `presumably / arguably` | Argumentative hedge | When introducing a contestable point |

Overuse of hedges reads as evasive; absence reads as overclaiming. Aim for hedges *only* on claims that aren't directly supported by your numbers.

---

## J. Word substitutions (avoid these defaults)

| Weak / overused | Stronger alternative |
|---|---|
| Very large / huge | (give the number, or a comparison) |
| Novel | (describe what's new) |
| Powerful | (describe the capability that makes it powerful) |
| Simple | (describe what's simpler than what) |
| Effective | (state the effect) |
| Promising | (state the result) |
| Robust | (give the noise/disturbance range tolerated) |
| Significant | (state the delta) |
| Multiple | (give the number) |
| Many | (give the number, or "5+") |
| Outperforms | (specify by how much, absolute or relative) |
| State-of-the-art | (cite the prior best) |

**Test**: if you delete the adjective, does the sentence say less? If not, delete it.

---

## K. Anti-patterns to reject

| Anti-pattern | Fix |
|---|---|
| `Our method works well.` | Replace with: `Our method achieves Y% on N tasks, outperforming the best baseline by Z%.` |
| `We propose a novel approach.` | Name the approach, drop "novel". |
| `Towards solving X...` | Drop "Towards" unless work is genuinely preliminary. |
| `Many works have...` | Cite or delete. |
| `It is well known that...` | Cite the prior work that established it. |
| `In future work, we will explore X.` | Tie to a specific limitation in the previous paragraph. |
| `We achieve impressive results.` | Replace "impressive" with the number. |
| `The result is significant.` | Replace "significant" with the delta and (if applicable) p-value. |
| Stacked weak adjectives: `a novel, robust, scalable, end-to-end pipeline` | Pick the strongest one. |

---

## Quick-reference

| User says | Reference section |
|---|---|
| "How do I open my intro?" | A1–A4 |
| "Where does my pivot sentence go?" | A4 |
| "Help me list my contributions" | B1 |
| "How do I introduce my system?" | B2, B3 |
| "How do I describe prior work?" | C1–C5 |
| "How do I position my method?" | C3 |
| "How do I set up my method section?" | D1–D5 |
| "How do I describe an equation / variable?" | D4 |
| "How do I report a result?" | E1–E5 (the 4-step paragraph) |
| "How do I report a number with no comparator?" | E3 — always pair with delta |
| "How do I close an ablation paragraph?" | F3 |
| "How do I write limitations?" | G1–G4 |
| "Which connector should I use?" | H1 table |
| "Is `novel` / `significant` weak?" | J — yes, replace with the measurable |
