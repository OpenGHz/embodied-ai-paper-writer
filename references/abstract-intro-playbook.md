# Abstract + Introduction — Operational Playbook

**Purpose**: How to write or critique the abstract and introduction of an embodied-AI paper.

Use when the user asks: "Draft my abstract", "Help me write the intro", "Is this opening strong?", "Where should the contribution list go?"

---

## Part 1 — Abstract

### The 5-move structure (6–12 sentences, 1 paragraph, 120–250 words)

Every abstract hits these moves in this order:

| Move | What it does | Typical length |
|---|---|---|
| **1. Frame** | Name the broad capability / problem class | 1 sentence |
| **2. Gap** | Pivot with "However," / "Yet," / "Despite,..." | 1 sentence |
| **3. Contribution** | Verb of introduction + system name | 1 sentence |
| **4. Method gist** | Mechanism in ≤3 sentences | 2–4 sentences |
| **5. Results** | Delta-form numbers + optional release | 1–2 sentences |

Optional 6th move: **release coda** (`Code: github.com/...`) or **moral close** (`These results suggest...`).

### Move 1 — Frame (broad opener)

Open with a CAPABILITY, METHOD CLASS, or PROBLEM CLASS — NOT your specific contribution.

**Templates** (pick one):
- `{Capability noun} {has the potential to} / {hold promise for} {societal-or-application goal}.`
- `Recent advances in {field} have enabled {what}.`
- `{Class of method} trained on {data type} have shown {capability}.`
- `{Problem class} often involves {challenge}, requiring {capability}.`

**Verified examples**:
> "Large policies pretrained on a combination of Internet-scale vision-language data and diverse robot demonstrations have the potential to change how we teach robots new skills..." — OpenVLA
> "Robotic loco-manipulation often involves contact-rich interactions with the environment, requiring the joint modeling of contact force and robot position." — CoRL_2505.20829
> "Foundation models, e.g., large language models (LLMs), trained on internet-scale data possess zero-shot generalization capabilities..." — AESOP

**Avoid**: opening with your method name. ("We propose XYZ..." is too narrow for sentence 1.)

### Move 2 — Gap (the hinge)

ONE short sentence using `However,`, `Yet,`, `Despite,`, or a participial. This is the load-bearing sentence of the abstract.

**Templates**:
- `However, {what's missing} has yet to be {achieved/demonstrated}.`
- `Yet, widespread adoption of {X} has been challenging as 1) {Y1}, and 2) {Y2}.`
- `Fully realizing this promise, however, poses {N} challenges: (i) ..., and (ii) ....`

**Variation**: when enumerating multiple sub-problems, use inline `(i) / (ii)` or `1) / 2)`.

### Move 3 — Contribution (the verb)

Use exactly one of: `We propose`, `We introduce`, `We present`, `We show`, `We demonstrate`. Embed the system name on first mention.

**Templates**:
- `In this work, we present {SystemName}, a {one-line descriptor}.`
- `Addressing these challenges, we introduce {SystemName}, a {parameter-count}-parameter {category} trained on {data}.`
- `Here, we present a {method type} for {task}.`

**Avoid**: `we propose a novel ...` (drop "novel"). `we tackle ...` (vague). `the authors present ...` (no third person).

### Move 4 — Method gist (2–4 sentences)

Walk the mechanism in **input→processing→output** order. Keep formalism out of the abstract. Use simple verbs: `Our method consists of...`, `The model takes {input} and produces {output}.`, `We train via {paradigm}.`

**Stop at the level of "what comes out", not "how the loop commits".** Abstract readers (including reviewers skimming arXiv listings) need the mechanism's *outcome shape*, not its *internal control flow*. The following are training-loop-internal terms and **do not belong in the abstract**:

| Method-internal term (avoid in abstract) | Why it's too detailed |
|---|---|
| `committed only after a held-out training-group gate` | Gate / commit / training-group are Stage-1 internals |
| `converges after N iterations` | Convergence criterion |
| `trained for N epochs with early stopping at validation loss X` | Optimizer details |
| `the K-group gate at threshold 0.85` | Hyperparameter exposure |
| `each candidate is revised on failure and committed on gate pass` | Loop-iteration mechanics |
| `we cache the prompt and reuse the lookup table at inference` | Implementation plumbing |

**Fix**: state the *artifact* the loop produces, not the criterion for producing it.
- ✗ `... distills the discovery into a one-line \addprompt{} committed only after a held-out training-group gate.`
- ✓ `... distills the discovery into a one-line \addprompt{}.` (the loop's commit criterion is method-section material)

**Calibration test**: read your method-gist sentence aloud as if to a reader who has never opened the paper. If a term requires the reader to picture the training loop's control flow to interpret, move it to the Method section.

### Move 5 — Results (delta-form, late in the abstract)

Numeric claims arrive in the last 2–3 sentences and are expressed as **deltas vs. a named baseline**, NOT absolutes.

**Templates**:
- `... outperforms {Baseline} by {X%} in absolute task success across {N} tasks.`
- `... improves upon state-of-the-art {Baseline1, Baseline2} by {X%, Y%} respectively.`
- `... reduces the amount of {Z} required by {X–Y%} as compared to baseline approaches.`
- `... achieves approximately ∼{X%} higher success rates in {N} challenging {task type} over {baseline class}.`

**Avoid**: `we achieve 87.3% success rate` without a comparison. Reviewers need the delta to judge.

### Optional Move 6 — Release coda

Final sentence is a URL or release statement. Near-universal in award-winning papers.

**Templates**:
- `Project website: {url}`
- `Videos are available at {url}.`
- `We release {model checkpoints / fine-tuning notebooks / codebase} at {url}.`
- `Supplementary materials and videos can be found at: {url}.`

### Optional Move 6′ — Moral close

For Science Robotics / RSS outstanding-paper tier: replace the delta with a normative statement about field-level implications.

**Templates**:
- `These results suggest that {high-level claim about the field}.`
- `{System} underscores the promising potential of {paradigm} in advancing {field}.`
- `Our results {pave the way for / hint at} {broader trajectory}.`

---

## Part 2 — Introduction (typical structure: 4 paragraphs, 1–1.5 pages)

### Paragraph 1: The hook

Open with one of three rhetorical hooks (pick by venue and tone):

| Hook style | Form | Venue tendency |
|---|---|---|
| **Question hook** | `How can we {capability}?` / `What form of {X} would {Y}?` | CoRL, RSS |
| **Scenario hook** | `Consider a {robot} trying to {task}.` | CoRL, RSS |
| **Grand-statement hook** | `The dream of robotics has always been ...` | Science Robotics, Nature Robotics |
| **Methods-frame hook** | `A central lesson from advances in {field} is that ...` | ICRA, IROS |

**Verified hooks**:
> "How can we endow our robots with the ability to know when they don't know?" — KNOWNO
> "What form of scene representation would facilitate open-set generalization for robotic manipulation systems? Consider a warehouse robot trying to fulfill an order..." — F3RM
> "The dream of robotics has always been that of general purpose machines that can perform many tasks in diverse, unstructured environments." — Science_Robotics_2303.03381

### Paragraph 2: Field state (1 paragraph)

Cite the recent progress in dense bracketed citation clusters — `[1, 2, 3]`, NOT named papers. Use the grammatical form:

- `Recent advances in {X} have demonstrated {capability} [n, m, o].`
- `Agents have been trained to {do X} [n, m], while substantial progress has been made in {Y} [p, q].`
- `Learning-based approaches have proven very effective in {A} (n–m), {B} (p–q), and {C} (r–s).`

### Paragraph 3: The pivot to the gap

Use `However`, `Yet`, `Despite`, `In contrast`. Often enumerates 2 specific problems:

> "Yet, there are two key reasons preventing the widespread use of existing VLAs: 1) current models are closed... 2) existing works do not provide best practices..." — OpenVLA

### Paragraph 4: Contribution + bullet list

End with **"we propose / we introduce {SystemName}, ..."** followed by an enumerated contribution list (3–5 bullets).

**Contribution-list signposts** (any of):
- `Our contributions are:`
- `Our primary contributions are:`
- `Statement of contributions.`
- `Specifically, our contributions are:`
- `Overall, our contributions can be summarized as follows:`
- `In summary, the main contributions are:`

### Anatomy of a single contribution bullet

`{Capability noun} + {verb of newness} + {quantified result}`

| Component | Examples |
|---|---|
| Capability noun | `framework`, `policy`, `benchmark`, `dataset`, `system`, `evaluation`, `pipeline` |
| Verb of newness | `propose`, `introduce`, `present`, `develop`, `release`, `demonstrate`, `show` |
| Quantified result | `improving by X%`, `achieving Y on Z benchmark`, `the first to do W` |

**Strong examples**:
- "An end-to-end learning approach that jointly optimizes navigation and manipulation, achieving an absolute improvement of 17.6% in average success rate across tasks compared to previous methods." — Harmonic MM
- "We propose the first model for learning unified force and position control in legged loco-manipulation, enabling diverse control behaviors such as position tracking, force control, and compliance with a single policy." — CoRL_2505.20829

**Weak example to fix**: `We contribute insights into manipulation.` → no specificity, no novelty signal, no evidence.

### "First" claims

When making a precedence claim, ALWAYS hedge with `To our knowledge` or `to the best of our knowledge`.

- `To our knowledge, {SystemName} is the first {category} to {achievement}.`
- `We are the first to demonstrate {claim}.`
- `{SystemName} is the first to consider {scope}.`

**Avoid**: bare `We are the first ...` (unhedged = reviewer-bait).

### Teaser figure reference

Reference `Figure 1` somewhere in paragraphs 1–2 of the intro (e.g. `(see Fig. 1)`). For the phrasing options and the full teaser playbook, see `teaser-figure-playbook.md` (Step 6 — Drive the Intro reference from the YAML).

### Acknowledging-but-distinguishing transitions

Every prior-work paragraph in the intro must end with a `however / in contrast / unlike` clause:

- `In contrast, our work {action} ..., uses {alternative} ..., and demonstrates {scope}.`
- `Unlike previous methods [X], we {alternative approach}.`
- `Our work differs from {NamedSystem} in {N} aspects: (1)..., (2)..., (3)....`

### Roadmap paragraph (optional; ICRA/IROS/RSS only)

End the intro with an organization paragraph if (a) venue is IEEE-style, (b) paper is theoretical or long, OR (c) the section order is unconventional:

> "The paper is structured as follows: Section II overviews related work. Section III describes preliminary information ... Section IV poses the time-optimal ergodic search problem ..."

**Skip the roadmap** in CoRL / NeurIPS-adjacent submissions. The transition Intro → Section 2 should be SILENT (no bridge sentence). Section 2 starts with its own subheading.

---

## Part 3 — Voice & style rules (apply to both abstract and intro)

| Rule | Right | Wrong |
|---|---|---|
| **Pronoun** | `We propose / We introduce / We present` | `The authors propose / It is shown` |
| **Tense in abstract** | Present (`we propose`, `the model achieves`) | Past (`we proposed`, `the model achieved`) |
| **Tense for completed experiments** | Past (`we evaluated`, `we conducted`) | Present (`we evaluate the method`) — only in method section |
| **Method-naming** | Capitalize / Small-caps consistently: `OpenVLA`, `KNOWNO`, `F3RM` | Inconsistent: `Openvla` once, `OpenVLA` next |
| **Hedging precedence** | `To our knowledge, we are the first to ...` | `We are the first to ...` (bare) |
| **Hyperbole adjectives** | Strip them: `Novel`, `New`, `Optimal`, `Best`, `Definitive` | Keep | drop or replace |
| **Numbers in abstract** | Deltas (`+12% over X`) or as-of claims (`SOTA on three benchmarks`) | Absolutes (`87.3%`) without baseline |
| **Cross-references** | None — abstract is self-contained | `(\S\ref{sec:X})`, `see Section 4`, `as in Fig. 2`, `Table 1 reports ...` |
| **Method-internal jargon** | State the artifact: `distills into a one-line prompt`. State the I/O: `takes video + proprio, outputs an action chain`. | `committed only after a held-out training-group gate`, `converges after N iterations`, `trained for N epochs with early stopping`, `the K-group gate at threshold 0.85`, `each candidate is revised on failure`. Training-loop internals belong in Method, not Abstract. |

**Why no cross-refs in the abstract**: the abstract is read in isolation — in arXiv listings, search results, program books, citation indexes. A `\S\ref{sec:supervised_baselines}` renders as "§ 4.4" (or worse, "§ ??" if compilation fails) to a reader who has never opened the PDF. Body-anchored references inside the abstract are noise to ~80% of the readership. The single exception: a project-page or release URL in the optional Move 6 coda is fine because the URL resolves anywhere; section/figure refs do not.

---

## Part 4 — Common micro-structures

### M1. The "two-challenges" enumeration

Common opening for the contribution paragraph when the gap is bi-fold:

> "Yet, there are two key reasons preventing the widespread use of existing VLAs: 1) current models are closed... 2) existing works do not provide best practices for deploying VLAs..."

If the gap is enumerated, the contribution list usually mirrors the same count.

### M2. Footnote on first method-mention

When the abstract mentions a release link, the intro should footnote the first method mention with:
- Project URL
- Equal-contribution markers
- Acronym backstory (if the name has one — e.g., AESOP = slow + fast reasoners like the Tortoise and Hare)
- Open-source license note

### M3. Section 2 silent transition

After the contribution bullets, jump DIRECTLY to `2 Related Work` or `II. RELATED WORK`. No "We now review" bridge.

Section 2's first paragraph opens with a **topical subheading** (bold, ending with period or italicized noun phrase) + a broad-capability sentence under that subheading. See `method-relatedwork-playbook.md` for full Related Work patterns.

---

## Quick-reference scenarios

| User asks | Action |
|---|---|
| "My abstract opens with my method name" | Rewrite opener as broad capability/problem-class frame |
| "My abstract has no 'However' hinge" | Insert an explicit pivot sentence at Move 2 |
| "My abstract has no numeric results" | Add delta-form results (Move 5) or replace with moral close (Move 6′) |
| "My abstract references a section / figure / table" | Delete the `\ref` — the abstract must be self-contained for off-paper readers (arXiv listings, search snippets). Body-pointers belong in the Intro. |
| "My abstract uses `gate` / `epoch` / `converges` / `commits` / training-loop verbs" | Move that to the Method section. Abstract method-gist stops at the artifact's I/O shape, not the loop's control flow. See Move 4 method-internal table above. |
| "My intro is 7+ paragraphs" | Compress prior-work survey; move detail to Related Work section |
| "Where do I put 'Our contributions'?" | Last paragraph of intro, bulleted/numbered |
| "Should I include a roadmap paragraph?" | Only for IEEE-style venues OR theory papers with unusual section order |
| "How do I reference Figure 1?" | Within paragraphs 1–2; use `(see Fig. 1)` or `As shown in Fig. 1, ...` |
| "I want to claim 'first work to X'" | Hedge with `To our knowledge` |
| "Do I bridge from intro to Related Work?" | No — silent transition; Section 2 opens with its own subheading |

---

## Construction workflow

1. **Title first**, then abstract — see `titles.md`.
2. **Write the 5 abstract moves as 5 separate sentences**, then expand.
3. **Run the verb check**: Move 3 uses exactly one of `propose / introduce / present / show / demonstrate`. No "novel".
4. **Run the delta check**: Move 5 has comparative numbers, not absolutes.
5. **Intro paragraph 1 — pick a hook**: question / scenario / grand-statement / methods-frame, by venue.
6. **Intro paragraph 4 ends with contribution bullets**: 3–5 bullets, each with capability+verb+quantified-result.
7. **Reference Figure 1** by paragraph 2.
8. **Strip hyperbole**: search for `novel`, `new`, `improved`, `optimal`, `best`, `cutting-edge`. Replace each.
9. **Silent transition** to Related Work.
