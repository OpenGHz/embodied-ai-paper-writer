# Flow & Transitions — Operational Playbook

**Purpose**: How to manage the rhetorical arc of the whole paper, the opening of each section, the topic sentence of each paragraph, and the connectors between paragraphs.

Use this when the user asks: "How do I open this section?", "How do I transition between paragraphs?", "Why does my paper feel choppy?", "How do I keep the contribution consistent across the paper?", "What pivot word should I use here?"

---

## Step 1 — Plan the 6-move arc that spans the whole paper

A well-flowing embodied-AI paper traces ONE arc through all sections. The arc has six moves; every section reprises whichever moves it owns.

| Move | What it does | Where it lives |
|---|---|---|
| **1. HOOK** | Name the capability / pain / dream | Abstract S1, Intro ¶1 |
| **2. GAP** | Pivot to what's missing | Abstract S2, Intro ¶2-3 |
| **3. APPROACH** | Name the system + headline mechanism | Abstract S3, Intro ¶4, Method ¶1 |
| **4. MECHANISM** | Spell out how it works | Method body |
| **5. EVIDENCE** | Numbers, plots, tasks | Experiments + Results |
| **6. IMPLICATION** | What it means for the field | Conclusion + Limitations |

**Rule**: every section opens by reprising one of these moves and closes by handing off to the next.

---

## Step 2 — Pick the right section opener for each section

Each section has a canonical opener taxonomy. Drift away from these openers and reviewers say "the writing feels off."

### Abstract S1 — capability statement (10/12 papers)

> `{Capability noun} {has the potential to / hold promise for / are capable of} {goal}.`

### Intro ¶1 — pick from 5 hook families

| ID | Hook style | Template | Venue tendency |
|---|---|---|---|
| **B1a** | Capability statement | `{Capability} has emerged as ...` | All venues; safest default |
| **B1b** | Rhetorical question | `How can we {capability}?` | CoRL, RSS |
| **B1c** | Recent-progress | `Recent advances in {X} have ...` | ICRA, IROS |
| **B1d** | Direct goal | `Our goal is to {capability}.` | Compact venues |
| **B1e** | Affective stakes | `{Activity} is a fundamental part of {human life}.` | System / HRI papers |

### Method ¶1 — system-name commitment

> `In this section, we describe {SystemName}, a {descriptor} that {value prop}.`
> or `We introduce {SystemName}, a {N}-parameter {category} trained on {data}.`

### Experiments ¶1 — question list

> `Our experiments answer {N} questions about {subject}:` followed by `(1) {question 1} (2) {question 2} ...`

### Conclusion ¶1 — past-tense restatement

> `We presented {SystemName}, a {descriptor} that {what it did} {on what}.`

The conclusion opener uses the SAME noun phrase as Abstract S3 and Intro ¶4 — never synonymize.

---

## Step 3 — Use the pivot family for gap-statements

The "pivot" is the load-bearing sentence that turns the reader from prior-work-praise to your-contribution. Pick from the family:

| Pivot | Force | Where it lives |
|---|---|---|
| **However,** | Standard, neutral | Abstract S2, Related-Work bucket closures, Results subsections |
| **Yet,** | Slightly more formal | Abstract S2 in award-winning papers (Science Robotics) |
| **Despite this progress,** | Soft, respectful | Related Work after a long citation run |
| **While X, Y** (participial) | Compresses pivot into 1 sentence | Abstract / Intro when space is tight |
| **In contrast,** | Direct, comparative | Related-Work bucket closures, ablation interpretation |
| **Unlike these methods,** | Stronger, distinguishing | Related-Work bucket closures |
| **On the other hand,** | Balanced comparison | Discussion / Limitations |
| **Conversely,** | Logical complement | Theoretical / ablation rebuttal |

**Anti-pattern**: stacking pivots. Two `However,`s in adjacent paragraphs reads like the author can't decide where the gap is. One pivot per gap.

**Double-pivot for nuanced contributions**:
> `However, {their X works} — but only when {condition Y holds}.`

Used when prior work works in narrow conditions and your contribution loosens the condition.

---

## Step 4 — Use the contribution-restatement spiral

A flagship contribution noun phrase appears **5–7 times** across the paper. Each restatement adds ONE new dimension. Track this consciously.

| Position | Restatement form | Adds dimension |
|---|---|---|
| Abstract S3 | `We introduce {Name}, a {short descriptor}.` | name only |
| Intro ¶4 | `We propose {Name}, a {descriptor} that {value prop}.` | + value prop |
| Method ¶1 | `In this section, we describe {Name}, ... trained on {data}.` | + training data |
| Experiments opener | `We evaluate {Name} against {baselines} on {tasks}.` | + benchmarks |
| Conclusion ¶1 | `We presented {Name}, a {descriptor} that {past-tense achievement}.` | + headline finding |

**Rule**: the noun phrase (`{Name}, a {descriptor}`) stays IDENTICAL across all positions; only the trailing clause expands.

**Anti-patterns**:
- Calling it `our system` in Intro and `OpenVLA` in Method — break the brand chain
- Adding two new dimensions per restatement — overstuffed
- Skipping a restatement (e.g., no name in Method opener) — reader loses anchor

---

## Step 5 — Open each paragraph with a topic sentence in the right shape

Paragraph topic-sentence shape depends on section:

| Section | Topic-sentence shape | Example |
|---|---|---|
| **Intro** | Capability / gap / contribution statement | `A key weakness of {X} is ...` |
| **Related Work** | Bucket header in **bold** ending in period | `**Vision-Language-Action Models.** Recent work has explored ...` |
| **Method** | Bold component label or numbered subsection | `**VLM Backbone.** We use {X}, a {descriptor}.` |
| **Experiments setup** | Recap of evaluation question in declarative form | `To assess {Q1}, we evaluate on {tasks}.` |
| **Results** | Bold scenario / dataset label | `**Small-scale dataset domains (Fig. 4).** Our method achieves ...` |
| **Ablation** | Comparison-purpose statement | `To understand the contribution of {component X}, we ablate ...` |
| **Conclusion** | Past-tense restatement | `We presented {Name}, ...` |

**Bolded-label convention** is most common in Method and Results. Reviewers scan these labels first.

---

## Step 6 — Use inter-paragraph connectors at pivot points

A connector at the start of a paragraph signals the logical relationship to the prior paragraph. Use them at TRUE pivots — not as filler.

### Forward chain (cause / consequence)

| Connector | Use when |
|---|---|
| **To this end,** | The new paragraph announces a contribution that addresses the prior paragraph's gap |
| **Towards this goal,** | The new paragraph names a method that pursues the prior paragraph's goal |
| **Building upon this,** | The new paragraph extends or refines the prior idea |
| **With these {tenets / insights / observations} in mind,** | The new paragraph announces a design that incorporates prior framing |
| **Following these results,** | The new paragraph announces a subsequent contribution / experiment |
| **As a result,** | The new paragraph reports the consequence of prior actions |

### Contrast / pivot

| Connector | Use when |
|---|---|
| **However,** | The new paragraph reverses the prior paragraph's direction |
| **Yet,** | Like However, but more formal |
| **In contrast,** | Direct comparison; the new paragraph claims a different approach |
| **Unlike** [these methods / X], | New paragraph distinguishes from prior class |
| **On the other hand,** | The new paragraph offers a complementary perspective |

### Continuation (same direction)

| Connector | Use when |
|---|---|
| **Moreover,** | Adds a parallel finding |
| **Furthermore,** | Stronger "moreover" — adds a load-bearing finding |
| **Additionally,** | Adds another item to an enumerated list |
| **Beyond this,** | Extends scope of the prior claim |

### Particularization

| Connector | Use when |
|---|---|
| **Specifically,** | Drills into the prior claim |
| **Concretely,** | Like Specifically; preferred in Method sections |
| **In particular,** | Highlights one element of the prior claim |
| **For example,** / **For instance,** | Adds an illustration |

### Surprise / emphasis (1–3 per section, max)

| Connector | Use when |
|---|---|
| **Notably,** | Result surprises in a positive direction |
| **Crucially,** | Reader should weight this heavily |
| **Importantly,** | Stakes are higher than usual |
| **Interestingly,** | Result raises a question worth flagging |
| **Surprisingly,** | Result contradicts expectation |

**Anti-pattern**: starting every paragraph with a connector. Reserve them for true pivots; use implicit transitions (pronominal anaphora) for continuation.

---

## Step 7 — Use implicit transitions (pronominal anaphora) for smooth continuation

When two paragraphs flow naturally, do NOT add a connector. Instead use a demonstrative phrase that points back to the prior paragraph's content.

Templates:
- `This {prior-noun} ...`
- `These {prior-objects} ...`
- `Such {prior-class} ...`
- `The above {prior-claim} ...`
- `This iterative process led to ...`

**Example**:
> [End of ¶N]: `... a five-day in-home evaluation in January 2025.`
> [Start of ¶N+1]: `This iterative process led to ...`

Implicit anaphora is the dominant transition style WITHIN a section (Method, Results, Discussion). Explicit connectors dominate ACROSS sections (Intro → Related Work, Results → Discussion).

---

## Step 8 — Use bucket closures in Related Work

Every Related-Work bucket ends with a contrast sentence that names the paper's position. The closure sentence ALWAYS begins with a pivot:

> `**Visually-Conditioned Language Models.** [3-5 sentences surveying prior work] ... **In contrast,** {Name} {does X differently / removes Y / adds Z}.`

Closure starter options:
- `In contrast,`
- `Unlike these {methods / works / approaches},`
- `Notably, our work ...`
- `Our work differs from {X} in {N} aspects: (1) ..., (2) ..., (3) ...`
- `However, our work ...`
- `Therefore, we propose ...`

**Disjunctive closure** (when prior work splits into two camps and you transcend both):
> `Existing works on {Y} either {camp 1} or {camp 2}, [whereas / yet / but] our work ...`

---

## Step 9 — Use the result-anchor rhythm in every Results paragraph

Each Results paragraph follows a 4–5 sentence rhythm:

1. **Bold scenario label**: `**{Setting} (Fig. X / Table Y).**`
2. **Headline number + comparison**: `Our method achieves {N}% vs. {M}% for {baseline}.`
3. **Direction reading**: `This represents an absolute improvement of {N-M} percentage points / a relative gain of {(N-M)/M}%.`
4. **Interpretation**: `..., suggesting / demonstrating / indicating that {mechanism / capability}.`
5. **Bridge to next paragraph**: forward connector OR reference to next experiment.

**Anti-pattern**: a Results paragraph that's just numbers with no interpretation sentence. Reviewers translate "no interpretation" as "you don't understand your own result."

---

## Step 10 — Match sentence-length rhythm to load

Within a single paragraph, alternate long claim-carrying sentences (25-45 words) with short pivot sentences (5-15 words).

**Pattern**: long (technical claim) → short (pivot) → long (elaboration) → short (handoff).

**Example** (OpenVLA intro paragraph 1):
- `A key weakness of learned policies for robotic manipulation is their inability to generalize beyond their training data: while existing policies trained for individual skills or language instructions have the capacity to extrapolate behaviors to new initial conditions such as object positions or lighting, they lack robustness to scene distractors or novel objects and struggle to execute unseen task instructions.` [~55 words — long claim]
- `Yet beyond robotics, existing foundation models for vision and language ... are capable of these types of generalization and more.` [~25 words — pivot]
- `... this imbalance suggests an opportunity: using existing foundation models for vision and language as a core building block for training robotic policies that can generalize ...` [~40 words — opportunity]

The shortest sentences carry pivots. The longest carry the gap-statement and opportunity-statement.

---

## Step 11 — Match paragraph length to section role

| Section | Paragraph length | Why |
|---|---|---|
| **Intro** | 5–8 sentences (~150–200 words) | Rhetorical framing requires room |
| **Related Work** | 5–8 sentences per bucket | Bucket needs survey + contrast |
| **Method** | 3–6 sentences | Uses bold-label structure |
| **Results** | 3–5 sentences | Scannable; one claim per paragraph |
| **Discussion** | 4–6 sentences | Reflective; mid-length |
| **Conclusion** | 3–5 sentences | Short, sharp |

Paragraph length **contracts** as the reader moves deeper into the paper. This mirrors the shift from rhetorical framing to scannable technical content.

---

## Step 12 — Handle the Intro → Related Work transition silently

Modern CoRL / NeurIPS-adjacent papers transition from Intro to Related Work SILENTLY. No bridge sentence at the end of Intro. No "We now survey related work" opener.

Instead:
- Intro ends with the contributions list.
- Section 2 opens with its own bolded subheading.

**Exception**: IEEE-style venues (ICRA, IROS, RSS) sometimes keep an Organization paragraph at the END of Intro that names the section order. Use only if your venue has this convention.

---

## Step 13 — Use the "Lastly," / "Finally," connector to signal section close

The last paragraph or subsection of every major section often starts with `Lastly,` / `Finally,` to signal the close.

Examples:
- Experiments: `Lastly, we perform ablations to measure ...`
- Results: `Finally, we examine generalization to unseen tasks ...`
- Limitations: `Finally, due to compute limitations, ...`

This is the easiest cue for a reviewer scanning the structure: when they see `Finally,` they know they're reading the last beat of the section.

---

## Step 14 — Use forward and backward cross-references for cohesion

### Forward (foreshadow upcoming evidence)
- `as we will show in Section X`
- `as shown in Section 5.4`
- `we discuss key design decisions in Section 3.4`
- `we provide an extension in Appendix A3`

Use 2–4 forward references in the Method section so reviewers know where to look.

### Backward (reuse prior content)
- `Following {prior work / Section X}, we ...`
- `Recall that {prior claim}...`
- `As noted earlier, ...`
- `Similar to the conclusions in {X}, ...`

Use backward references in Results / Discussion to remind the reader of definitions or hypotheses.

---

## Step 15 — Use the bold-label paragraph for technical sub-blocks

In Method and Results, replace topic sentences with **bold labels** when the section enumerates components / scenarios:

> `**VLM Backbone.** We use {LLaMA-2 / Llava-1.5}, a 7B-parameter ...`
> `**Action Tokenization.** We discretize each dimension ...`
> `**Training Recipe.** We train on {dataset} with {hyperparams} ...`

The bolded label IS the topic sentence. The rest of the paragraph elaborates.

**Anti-pattern**: bold label `**VLM Backbone.**` followed by a paragraph that doesn't talk about the backbone — reader expects exactly what's promised by the label.

---

## Step 16 — Recap evaluation questions at the start of each Experiments subsection

The Experiments opener lists 2–4 numbered questions. Each subsequent subsection opens by RESTATING the matching question in declarative form.

**Example flow**:
- Experiments opener: `(1) Can policies trained on our X-embodiment dataset effectively enable positive transfer?`
- V-A opener: `To assess the ability of RT-X models to learn from X-embodiment data, we evaluate performance on in-distribution tasks.`

The reader can match (Q1 ↔ V-A) by visual scanning. Reviewers love this scaffolding.

---

## Step 17 — Use "We hypothesize / We find / We observe" verbs to mark cognitive moves

In Results and Discussion, mark each cognitive move with a verb of intellectual stance:

| Verb | Cognitive move | Force |
|---|---|---|
| `We hypothesize that ...` | Prediction before experiment | Pre-hoc |
| `We find that ...` | Empirical observation | Neutral |
| `We observe that ...` | Empirical observation | Neutral |
| `We confirm that ...` | Validation of hypothesis | Pre-hoc match |
| `We discover that ...` | Surprising finding | Surprise |
| `Our results suggest that ...` | Interpretation, hedged | Soft claim |
| `Our results indicate that ...` | Interpretation, firmer | Medium claim |
| `Our results demonstrate that ...` | Interpretation, strong | Hard claim |

**Calibration**: use `suggest` for results from one experiment, `indicate` for results that replicate, `demonstrate` only for results with strong baselines + statistical aggregation.

---

## Step 18 — Conclusion closure: hope / aspiration sentence

10/12 papers end the conclusion with a hope-sentence about the field-level implication.

Templates:
- `We hope that {release / contribution} will enable {downstream goal}.`
- `Our results pave the way for / hint at {broader trajectory}.`
- `{System} underscores the promising potential of {paradigm} in advancing {field}.`
- `We hope that our work will encourage future exploration of {direction}.`

This is the moral-close move — the last sentence the reader takes away. Spend time on it.

---

# Anti-patterns to reject

| Anti-pattern | Fix |
|---|---|
| Two `However`s in adjacent paragraphs | Combine into one pivot or convert one to `In contrast,` |
| Bold label `**X.**` followed by content not about X | Rewrite label to match content, or rewrite content |
| Synonymizing the system name across sections | Lock to one canonical phrase |
| No interpretation sentence in Results paragraph | Add `..., suggesting / indicating / demonstrating that ...` |
| Connector overuse: every paragraph starts with `Moreover,` `Furthermore,` `Additionally,` | Reserve connectors for true pivots; use implicit anaphora otherwise |
| Stacking `Notably,` `Crucially,` `Importantly,` in one section | 1–3 emphasis connectors per section, max |
| `In this section, we present X. We first ... Then ... Finally ...` followed by another roadmap in next subsection | One roadmap per section |
| Conclusion opens with `In conclusion,` | Open with `We presented ...` (past-tense restatement) |
| Bridge sentence at end of Intro: `We now describe related work.` | Delete; transition silently |
| Section close has no `Finally,` or `Lastly,` cue | Add the close-signal connector |

---

# Construction workflow

1. **Sketch the 6-move arc** (Step 1). Write the HOOK noun phrase, the GAP statement, the APPROACH name, the MECHANISM verb, the EVIDENCE delta, the IMPLICATION hope.
2. **Pick each section opener** (Step 2). Abstract = capability statement. Intro = one of B1a–B1e. Method = system-name commitment. Experiments = question list. Conclusion = past-tense restatement.
3. **Lock the contribution noun phrase** (Step 4). Write it once; reuse 5–7 times.
4. **For each paragraph, pick a topic-sentence shape** (Step 5). Bold-label for Method/Results; capability/gap for Intro; question recap for Experiments subsections.
5. **At each paragraph junction, pick connector OR implicit anaphora** (Steps 6–7). Connector for true pivots; anaphora for smooth continuation.
6. **For each Related-Work bucket, write the closure pivot** (Step 8). Always end with `In contrast,` / `Unlike` / `Notably, our work ...`.
7. **For each Results paragraph, apply the result-anchor rhythm** (Step 9). Label → number → direction → interpretation → bridge.
8. **Mark cognitive moves with stance verbs** (Step 17). `We hypothesize / find / observe / demonstrate.`
9. **Close the Conclusion with a hope sentence** (Step 18).
10. **Pass through and verify**: same noun phrase 5–7 times, one pivot per gap, `Finally,` cue at each section close.

---

# Quick-reference

| User says | Action |
|---|---|
| "How do I open this Method section?" | `In this section, we describe {Name}, a {descriptor} that {value prop}.` |
| "How do I open this Results subsection?" | Restate matching evaluation question in declarative form |
| "How do I transition from this paragraph to the next?" | If pivot: pick from `However / In contrast / To this end / Building upon this`. If continuation: use pronominal `This/These {prior-noun}`. |
| "How many `However`s can I have?" | One per gap. Two adjacent reads as indecisive. |
| "How do I make sure my contribution is consistent?" | Lock the noun phrase; reuse 5–7 times with the same words. |
| "How do I close my Related-Work bucket?" | End with `In contrast,` / `Unlike these works,` / `Notably, our work ...`. |
| "How do I open my Conclusion?" | `We presented {Name}, a {descriptor} that {past-tense achievement}.` |
| "My paragraphs feel disconnected." | Check connectors at pivots; use implicit anaphora between flowing paragraphs. |
| "When should I use `Notably,` / `Crucially,`?" | 1–3 per section. Reserve for results that surprise or have high stakes. |
| "When should I add a roadmap sentence?" | First paragraph of Method, only if there are 3+ subsections. |
| "Where does the system name first appear in Method?" | First sentence of Method, in the system-name commitment opener. |
| "Should I bridge from Intro to Related Work?" | No — silent transition. Section 2 opens with its own subheading. |
| "Where does `Finally,` go?" | At the start of the last paragraph or subsection of each major section. |
