# Conclusion & Limitations — Research Notes

**Corpus**: Closing sections extracted from 63 embodied-AI papers (CoRL, RSS, ICRA, IROS, Science Robotics). Direct hits via regex: 18 papers with a clean display-header section. Forensic keyword search shows 50/63 mention "Limitations", 43/63 mention "Future Work", 33/63 mention "Discussion", 31/63 mention "Conclusion". Many papers fold these together into a single "Discussion and Limitations" block; a minority (mostly venue-page-limited ICRA/IROS submissions) collapse everything into a 3-sentence "Conclusion" or drop the limitations into the appendix.

Source corpus: `_conclusion_corpus.md` (53KB, 18 papers with clean extraction).

---

## A. Section-header taxonomy

Eight observed header styles, with rough venue tendencies:

| # | Header style | Example papers | Venue tendency |
|---|---|---|---|
| H1 | `Conclusion` (standalone) | OpenVLA prequel CoRL_2308.07931, CoRL_2407.01812 (Equivariant Diffusion), CoRL_2505.03729 (VideoMimic), CoRL_2509.01746 (Fail2Progress) | CoRL most common |
| H2 | `Conclusion and Limitations` (combined) | RoboCook (CoRL_2306.14447) | CoRL when limitations are short |
| H3 | `Discussion` (standalone, replaces Conclusion) | KnowNo (CoRL_2307.01928), PoliFormer (CoRL_2406.20083), Science_Robotics_2303.03381, Science_Robotics_2410.21845 | Science Robotics standard; some CoRL |
| H4 | `Discussion and Limitations` (combined) | OpenVLA (CoRL_2406.09246), Science_Robotics_2309.01918 | Science Robotics fallback |
| H5 | `Limitations and Future Work` (no Conclusion at all) | Re-Mix (CoRL_2408.14037), CoRL_2505.20829 (force-position) | CoRL when Conclusion was absorbed into final Experiments paragraph |
| H6 | `Limitations` (standalone, AFTER a separate Conclusion) | VideoMimic (CoRL_2505.03729), Fail2Progress (CoRL_2509.01746), Science_Robotics_2303.03381 | Two-section pattern common at top venues |
| H7 | `Concluding Remarks` | rare; mostly older IROS | IROS/legacy |
| H8 | Inline mini-headers (no display header) | "Limitations:" / "Future Work" paragraphs woven into Discussion | Page-limited ICRA/IROS; PoliFormer style |

**Picking your header**: count your limitations items first.
- 0-2 short items → fold into one section as **H2 Conclusion and Limitations**
- 3-5 items → use **H6** (separate Conclusion + Limitations) — this is the modal pattern at strong CoRL submissions
- 5+ items → use **H6** and bold each limitation as a mini-label sub-paragraph
- Science Robotics / Nature-format → use **H3 Discussion** (replaces Conclusion entirely)
- ICRA/IROS with 1 page over the limit → use **H8 inline** to save vertical space

**Numbering**:
- CoRL/RSS/IROS submissions usually arabic: `5 Conclusion`, `6 Limitations`
- ICRA: roman numerals `VII. CONCLUSIONS`, `VI. DISCUSSION`
- Science Robotics: no numbers OR top-level `3. DISCUSSION`

---

## B. Conclusion section — content patterns

The Conclusion in modern embodied-AI papers is **short and recap-first**, averaging 5-12 sentences (60-180 words). It does NOT introduce new claims, does NOT report new numbers, and does NOT explain. It states what the paper did and what's next.

### B1. The recap-only Conclusion (most common — ≈55% of corpus)

3-move structure: **what we did → what we showed → what this enables**.

> "We have illustrated a way to combine 2D visual priors with 3D geometry to achieve open-ended scene understanding for few-shot and language-guided robot manipulation. Without fine-tuning, Distilled Feature Fields enable out-of-the-box generalization over variations in object categories, material, and poses. When the features are sourced from vision-language models, distilled feature fields offer language-guidance at various levels of semantic granularity."
> — F3RM (CoRL_2308.07931)

> "RoboCook demonstrates its effectiveness, robustness, and generalizability in elasto-plastic object manipulation with a general-purpose robotic arm and everyday tools. The main contributions of RoboCook include (1) tool-aware GNNs to model long-horizon soft body dynamics accurately and efficiently, (2) a tool selection module combined with dynamics models to learn tool functions through self-exploratory trials, and (3) a self-supervised policy learning framework to improve the performance and speed significantly. RoboCook pioneers solutions for tool usage and long-horizon elasto-plastic object manipulation in building a generic cooking robot."
> — RoboCook (CoRL_2306.14447)

> "This paper studies the leveraging of symmetries in visuomotor policy learning. We propose the novel Equivariant Diffusion Policy method and provide a theoretical analysis identifying the conditions under which diffusion processes are equivariant. We also demonstrate a general framework for using SO(2)-equivariance in the 6DoF control for robotic manipulation. We evaluate our method in both simulation and the real world and show in both cases that our method outperforms the baseline Diffusion Policy by a large margin."
> — Equivariant Diffusion Policy (CoRL_2407.01812)

**Template**:
> `[We {present/propose/introduce} {SystemName}, a {one-line descriptor}.] [The {key innovation/contribution} is {X}.] [{Empirical claim}, {comparison to baseline}.] [{Forward-looking sentence about implications}.]`

### B2. The recap + sign-off Conclusion (≈30% of corpus)

Same as B1, plus a final sentence inviting community follow-up or expressing hope.

Sign-off sentence patterns:
- "We expect future work to extend the system to **{X}**, **{Y}**, and **{Z}**, among other directions." — VideoMimic
- "We hope that the release of the {model and codebase} will enable the community to jointly investigate these questions." — OpenVLA
- "We hope this work will pave the way for {broader-direction}, achieving {high-level-goal}." — Science_Robotics_2410.21845
- "{SystemName} pioneers solutions for {problem} in building a {long-term-vision}." — RoboCook
- "We hope that the work presented here spurs further efforts towards {field-level-goal}." — KnowNo

The "We hope..." sentence is a venue-agnostic safe close. Use it when you do not have a separate "Future Work" section.

### B3. The contribution-list Conclusion (≈10%, mostly CoRL system papers)

Lists 3-4 enumerated contributions, restating the abstract's claim list. Used when the paper is a system paper with multiple discrete artifacts (model + dataset + benchmark).

> "The main contributions of RoboCook include (1) tool-aware GNNs..., (2) a tool selection module..., and (3) a self-supervised policy learning framework..."

Use only if your abstract had an explicit numbered contributions list — symmetry between abstract and conclusion is important.

### B4. The discussion-style Conclusion (Science Robotics)

Science Robotics papers replace "Conclusion" with **"Discussion"** and write 2-4 paragraphs instead of 1. The first paragraph recaps; subsequent paragraphs contextualize against prior work, situate the work in a longer-term arc, or discuss broader-impact / limitations.

> "We have presented a fast and robust quadrupedal locomotion controller for challenging terrain. The controller seamlessly integrates exteroceptive and proprioceptive input. Exteroceptive perception enables the robot to traverse the environment quickly and gracefully by anticipating the terrain and adapting its gait accordingly before contact is made. When exteroceptive perception is misleading, incomplete, or missing altogether, the controller smoothly transitions to proprioceptive locomotion."
> — Science_Robotics_2201.08117

> "The presented results substantially advance the published state-of-the-art in robotic manipulation. Our research demonstrates that with the right design choices, model-free RL can actually effectively tackle a variety of complex manipulation tasks using perception inputs, directly training in the real world within a practical timeframe..."
> — Science_Robotics_2410.21845

**Discussion-style is ≥1.5× the length of Conclusion-style.** Budget 200-400 words.

---

## C. Limitations section — content patterns

This is the most stereotyped genre in the paper. Failure to write a Limitations section is a strong reject signal at CoRL/RSS — reviewers are explicitly instructed to check.

### C1. The enumerated-prose pattern (CoRL/RSS most common)

Use `First, ...`, `Second, ...`, `Third, ...`, `Finally, ...` as connectors. Each limitation is a complete sentence or two. Each limitation MUST be paired with a future-work hint.

> "The current OpenVLA model has several limitations. **First**, it currently only supports single-image observations. In reality, real-world robot setups are heterogeneous, with a wide range of possible sensory inputs [5]. Expanding OpenVLA to support multiple image and proprioceptive inputs as well as observation history is an important avenue for future work. ... **Secondly**, improving the inference throughput of OpenVLA is critical to enable VLA control for high-frequency control setups such as ALOHA [90]... Exploring the use of action chunking or alternative inference-time optimization techniques such as speculative decoding [91] offer potential remedies. **Additionally**, there is room for further performance improvements. While OpenVLA outperforms prior generalist policies, it does not yet offer very high reliability on the tested tasks, typically achieving <90% success rate. **Finally**, due to compute limitations, many VLA design questions remain underexplored..."
> — OpenVLA (CoRL_2406.09246)

> "**First**, while the policy successfully estimates external forces without direct force sensing, its accuracy tends to degrade in high-frequency interactions and at the edges of the robot's workspace. Future work could focus on improving force estimation in these corner cases... **Second**, while our policy generalizes well from simulation to real-world deployment, discrepancies remain due to the sim-to-real gap... **Additionally**, our current framework primarily focuses on estimating force at a single interaction point. Future work could explore multi-point force estimation..."
> — CoRL_2505.20829

**Six-item escalation** (Fail2Progress, CoRL_2509.01746) demonstrates that you can scale up to `First, Second, Third, Fourth, Fifth, Sixth, Finally,` if the paper is high-stakes and reviewers will demand exhaustive disclosure.

Pairing rule: every "limitation" sentence must be followed (in the same paragraph) by a "future work / mitigation" sentence. This dual structure — admit-and-propose — is what reviewers reward. Naked admission ("we cannot do X") without a forward-looking mitigation reads as defeatist.

### C2. The bold mini-label pattern (modern CoRL/RSS for 4+ items)

Each limitation gets its own paragraph with a **bold topical mini-header** (subject-noun, period-terminated). This scales better than `First, Second, ...` past 4 items.

> "**Reconstruction.** Monocular 4D human–scene recovery is still brittle in the wild...
> **Retargeting.** The kinematic optimizer assumes every reference pose can be made feasible once scaled to the robot...
> **Sensing and policy input.** At test time, the controller receives only proprioception and an 11 × 11 LiDAR height-map...
> **Simulation fidelity.** We assume the scene can be represented as a single rigid mesh...
> **Data scale and motion quality.** The distilled policy is trained on only 123 video clips..."
> — VideoMimic (CoRL_2505.03729)

> "**Evaluation.** While we train on large, diverse robot datasets, the need for real world trials makes it difficult to exhaustively evaluate trained generalist policies on many robot embodiments and setups...
> **Abnormal Action Distributions.** We have noticed that Re-Mix upweights datasets with abnormal action distributions such as the Toto dataset...
> **Computational Cost.** Using our pre-computed weights can significantly reduce the compute required to train generalist policies...
> **Scaling Up.** While we have demonstrated improvements on two large datasets, Bridge V2 and RT-X..."
> — Re-Mix (CoRL_2408.14037)

**Mini-label naming rule**: Use a domain-noun, NOT a complaint. Good: `Reconstruction.`, `Computational Cost.`, `Scaling Up.`. Bad: `Slow inference.`, `Doesn't work in clutter.` — these read as confessions rather than research framings.

Capitalize Title Case for the mini-header (`Computational Cost.`), single capital for short labels (`Reconstruction.`).

### C3. The one-paragraph limitations (short / inline)

When you have 1-2 limitations or are page-pressed, write a single paragraph using "One limitation" / "Another limitation" / "Finally" connectors.

> "**One limitation** of RoboCook is the occasional failure of dough sticking to the tool. A solution is to design an automatic error correction system. RoboCook also relies on human priors of tool action spaces to simplify planning. But these simplifications do not constrain generalization as they can be easily specified for new tools. Section 6.4.1 provides more justifications for this. **Another limitation** is that humans define the subgoals. Higher-level temporal abstraction and task-level planning are required to get rid of them. **Finally**, RoboCook requires additional topology estimation to apply to cables and cloths [56], which is beyond the focus of this work."
> — RoboCook (CoRL_2306.14447)

> "**One limitation of this work** is the partial utilization of the power of equivariance due to the symmetry mismatch in the vision system... **Another limitation** is that although the theory in Section 4.2 is not limited to diffusion policies and can apply to other policy learning pipelines as well, this is not demonstrated... **Finally**, extending our method to other robotic tasks like navigation, locomotion, and mobile manipulation is a key future direction."
> — Equivariant Diffusion Policy (CoRL_2407.01812)

### C4. The inline-paragraph compressed form (ICRA/IROS page-limited)

When the body has run long and there is no room for a display-header Limitations section, the limitations are folded into the Discussion's last paragraph using inline mini-labels.

> "**Limitations:** Training RL agents for long-horizon tasks with a large search space requires extensive compute and demands careful reward shaping. While we believe P OLI F ORMER is capable of scaling to other tasks, it requires crafting new reward models for novel tasks such as manipulation. More discussion on limitations in App. E. **Conclusion:** In this paper we provide a recipe for scaling RL for long-horizon navigation tasks..."
> — PoliFormer (CoRL_2406.20083)

When using this style, **always add `More discussion on limitations in App. E.`** or equivalent appendix pointer — reviewers will check.

---

## D. Future Work — patterns

Future Work appears in three locations:
1. **Inline within each limitation** (most common — see C1, C2 above)
2. **As a sub-paragraph of Conclusion** (B2 sign-off)
3. **As its own section after Limitations** (heavy submissions like Science Robotics)

### D1. Per-limitation future-work pairing (C1/C2 default)

Each limitation sentence is followed by a future-work mitigation sentence. Connectors:
- "**Future work** could address this by {mitigation}."
- "**Future work** can instead strive to {goal}."
- "**Future work** could focus on improving {X} in these corner cases."
- "**Exploring the use of** {technique} {may/offer} potential remedies."
- "**One possible direction** is to incorporate {technique}."

### D2. Standalone Future Work section (Science Robotics + comprehensive papers)

When Future Work gets its own section, it usually has 2-4 named sub-directions, each with a bold inline title.

> "**Multi-agent Soccer:** An exciting direction of future work would be to train teams of two or more agents. It is straightforward to apply our proposed method to train agents in this setting...
> **Playing Soccer from Raw Vision:** Another important direction for future work is learning from on-board sensors only, without external state information from a motion capture system..."
> — Science_Robotics_2304.13653 (Bipedal Soccer)

Sub-direction labels: noun phrase + colon. Not a sentence.

### D3. Conclusion sign-off Future Work (B2)

One-sentence: "We expect future work to extend the system to **X**, **Y**, and **Z**, among other directions." Or: "We hope that {release/method} will enable the community to {community-level goal}."

---

## E. Discussion section (Science Robotics & top-tier submissions)

Discussion ≠ Conclusion. Discussion contextualizes contributions against prior work and field-level trajectories. It is the place to make **claims you cannot defend with numbers**: long-term implications, why this approach matters beyond the immediate metric.

### E1. Discussion structure (3 paragraphs)

**Paragraph 1: Recap** — "We have presented {SystemName}, a {descriptor} that {one-line claim}." Restate the headline result.

**Paragraph 2: Contextualization** — Compare to prior work in field. "Compared to {alternative-approach-class}, our method {key-difference}." Acknowledge that prior work has tackled some of the same problems.

**Paragraph 3: Broader impact / next steps** — "We see a number of opportunities for future work. First, ... Second, ..."

> Example structure from Science_Robotics_2410.21845:
> Para 1 — "The presented results substantially advance the published state-of-the-art in robotic manipulation."
> Para 2 — "Beyond the results themselves, the approach presented in this work can have significant broader impact. It can serve as a general framework..."
> Para 3 — "We see a number of opportunities for future work. First, our approach can serve as an effective tool for generating high-quality data..."

### E2. Comparison-to-X sub-headers

When the Discussion needs to position against a famous prior system (RoboCup, RT-1, Diffusion Policy), use a bold sub-header:

> "**Comparison to RoboCup**
> Robot soccer has been a longstanding grand challenge for AI and robotics, since at least the formation of the RoboCup competition [30, 29] in 1996..."
> — Science_Robotics_2304.13653

Use sparingly — only when the named comparison is iconic enough that readers will expect to see it.

---

## F. Standard lexicon (verbs, connectors, qualifiers)

### Recap verbs (Conclusion opening)

Strong: `present`, `propose`, `introduce`, `develop`, `demonstrate`, `study`.
Slightly weaker: `show`, `address`, `explore`, `investigate`.
Avoid: `make`, `do`, `try`. (Too colloquial.)

Construction: `We {verb} {SystemName}, a {one-line-descriptor}.` OR `We have {past-participle} {object}.`

### Limitations connectors

Sequential: `First, ... Second, ... Third, ... Finally, ...`
Additive: `Additionally,`, `Furthermore,`, `Moreover,`.
Numbered cap-out: `Sixth, ... Finally, ...` (used by Fail2Progress with 7 items; the "Finally" is the closer regardless of how many came before).
Conjunctive: `One limitation is that {X}.`, `Another limitation is that {Y}.`, `A further limitation is {Z}.`.

### Future-work connectors

`Future work could / will / might {verb}.`
`A promising direction for future research is to {verb-phrase}.`
`An important avenue for future work is {gerund-phrase}.`
`We anticipate that {X} would work in this application.`
`We are looking to incorporate {Y} in the future.`

### Hedging the limitation (downplays severity)

- "Our approach **shows promising results**, however, **it still has some limitations** that **need to be addressed in future work**."
- "Our system delivers **encouraging** real-world results, **yet several practical weaknesses remain**."
- "**Beyond the results themselves**, there is room for further improvements."
- "While {X-positive-claim}, {Y-honest-limitation}."

The `While X, Y` structure is the safest limitation-introduction sentence — you concede a weakness while affirming a strength in the same breath.

### Sign-off phrases

- "We hope that {X} will enable the community to {community-goal}."
- "We hope this work will pave the way for {field-level-trajectory}."
- "We expect future work to extend the system to {X}, {Y}, and {Z}, among other directions."
- "{SystemName} offers a scalable path for {long-term-goal}."
- "We believe that {speculative-claim} would result in {improvement}."

---

## G. Length budget (corpus statistics)

| Section style | Word count range | Paragraph count |
|---|---|---|
| H1 standalone Conclusion (CoRL) | 60-180 | 1-2 |
| H2 Conclusion + Limitations combined | 150-300 | 2-3 |
| H3/H4 Discussion (Science Robotics) | 300-600 | 3-4 |
| H6 standalone Limitations (with 4+ items, C2 style) | 250-500 | 4-7 paragraphs (one per item) |
| H8 inline Limitations: + Conclusion: in single paragraph | 80-150 | 1 |
| D2 standalone Future Work | 200-400 | 2-4 |

Total closing-section budget across all closing genres in a CoRL submission: 250-600 words (≈half a column to one column at CoRL formatting).

---

## H. Coupling with other sections

The Conclusion must **echo the contributions in the Abstract and the contributions in the Introduction's `Our contributions:` list**. Pick the same 3-4 verbs:

| Section | Verb the work is described by |
|---|---|
| Title | "Open-Source ... Vision-Language-Action Model" (OpenVLA) |
| Abstract | "We introduce OpenVLA, ..." |
| Introduction last paragraph | "We present OpenVLA, ..." |
| Conclusion | "we presented OpenVLA, ..." |

The tense shifts: Abstract uses **present** (we introduce), Conclusion uses **past** (we have presented / we presented). This is a tense-marker reviewers notice — get it right.

The Conclusion should **not introduce new acronyms, new system names, or new datasets**. If you mention something the body did not, it reads as a sloppy revision.

---

## I. Anti-patterns to avoid

- **"In conclusion, ..."** as the opening word. Modern embodied-AI papers do not start the Conclusion section with this filler. Lead with `We presented ...` or `{SystemName} demonstrates ...`.
- **Empty Limitations**: writing "While our method achieves strong performance, there are several limitations..." then listing trivial issues like "longer training time" or "we used a fixed seed." Reviewers see through this. The list must include at least one **methodological** limitation (assumption, scope restriction, failure mode), not just engineering complaints.
- **Pure-confession Limitations**: listing limitations without pairing each with a future-work hint. Comes across defeatist.
- **Promotional Limitations**: writing limitations that are actually disguised praise ("Our method may be too generalizable for some narrow applications"). Reviewers see through this too.
- **Restating numbers in the Conclusion**: never write "Our method achieves 87.3% success rate" again in the Conclusion. Numbers belong in Experiments. Conclusion claims should be qualitative ("substantially outperforms baselines", "achieves strong real-world performance").
- **Introducing new contributions in the Conclusion**: if the Conclusion mentions something not in the body, reviewers will accuse you of moving the goalposts.
- **Forgetting the appendix pointer**: when using H8 inline-compressed style, always include `(more discussion in App. X)` — without it, reviewers will assume you have no limitations analysis.
- **Discussion that's just Conclusion ×2**: Science Robotics submissions sometimes write a Discussion that is 4 paragraphs of recap. The Discussion must do *more* than the Conclusion would — contextualize, project, situate.

---

## J. Construction workflow

Given that the body of your paper is drafted, build the closing sections in this order:

1. **Pick header style** based on (a) venue (ICRA → roman numbered; CoRL → arabic; Science Robotics → no numbers, "Discussion"); (b) number of limitations items (0-2: combined; 3+: separate; 4+ with C2 bold-label style).
2. **Draft the Conclusion recap** in 5-12 sentences. Mirror the abstract verbs (present/introduce/develop). Past tense. No new numbers.
3. **List the limitations as bullet points** in a scratch draft — just the raw items (e.g., "single-image input", "no multi-finger", "sim2real gap on slippery surfaces"). Aim for 3-5.
4. **For each limitation, write a future-work mitigation** next to it. If you cannot write one, the limitation is either wrong-framed (re-frame it as something the field will work on) or trivial (drop it).
5. **Sequence the limitations** by importance: most-significant first. The reader should not feel that you're hiding the worst one behind smaller ones.
6. **Choose connector style**: First/Second/Finally for 3-4 items in prose; bold mini-labels for 4+ items in clear paragraphs.
7. **Add a sign-off sentence** to the Conclusion: "We hope that ..." or "We expect future work to extend ..." — gives the paper a forward-looking close.
8. **Sanity check coupling**: open Abstract and Introduction side-by-side with Conclusion. Same verbs? Same system name typesetting? Same contribution count? Fix any drift.

---

## K. Venue-specific tendencies (corpus observations)

| Venue | Modal closing structure | Notable habits |
|---|---|---|
| **CoRL** | H1 Conclusion + H6 Limitations (separate sections), C2 bold-label limitations | Most explicit + comprehensive Limitations. Reviewers expect it. |
| **RSS** | H1 Conclusion + inline Limitations within Discussion | More compressed; Limitations often woven into final Discussion paragraph |
| **ICRA** | VII. CONCLUSIONS (Roman, short, often just 3-5 sentences) | Page-limited; Limitations frequently dropped or moved to last Discussion paragraph |
| **IROS** | Similar to ICRA but slightly longer; "CONCLUSIONS" or "CONCLUDING REMARKS" | Future Work often gets its own sub-section |
| **Science Robotics** | H3 Discussion (replaces Conclusion entirely); H6 Limitations + D2 Future Work as separate sections | Longest closing block; Discussion contextualizes against field history; numbers ≤300 words |

---

## L. Sample size and confidence

- Direct extraction: 18/63 papers with clean display-header sections.
- Forensic keyword presence: 50/63 ("Limitations" word), 43/63 ("Future Work"), 33/63 ("Discussion"), 31/63 ("Conclusion").
- Manually verified examples from 18 papers across 5 venues.
- Most reliable patterns: enumerated `First, Second, ... Finally,` connectors (10+ direct examples), bold mini-label C2 pattern (3 strong examples + many half-matches), "We hope ..." sign-off (5+ direct examples).
- Less reliable: Discussion structure for Science Robotics (only 4 strong examples; venue is heterogeneous).

---

## M. Quick-reference cheatsheet (for Phase 2 synthesis)

| User asks for | Use this |
|---|---|
| "Write a CoRL Conclusion" | B1 recap-only, 3-move structure, past tense, no new numbers, 80-150 words |
| "Write a Limitations section with 4 items" | C2 bold-label pattern (Reconstruction. / Retargeting. / ...). Each label = domain noun + period. Each paragraph = limitation + future-work mitigation. |
| "I'm at page limit, where do I cut Limitations?" | Use H8 inline style: `Limitations:` then `Conclusion:` in one paragraph. Add `More discussion in App. X.` pointer. |
| "Science Robotics is asking for Discussion" | E1 3-paragraph structure: recap → contextualize → opportunities. ~300-500 words. |
| "How do I end the Conclusion?" | B2 sign-off: "We hope that {release/method} will enable {community-level goal}." OR "We expect future work to extend to X, Y, and Z, among other directions." |
| "Reviewer says my limitations sound defensive" | Each limitation must be paired with a future-work mitigation in the SAME paragraph. Use `Future work could / will / might {verb}.` |
| "How long should the closing block be?" | CoRL: 250-400 words total. ICRA/IROS: 100-200 words. Science Robotics: 400-700 words. |
| "Do I need a Future Work section?" | Only if Discussion is short or you have 3+ distinct future directions. Otherwise fold into Limitations (D1) or Conclusion sign-off (B2). |
