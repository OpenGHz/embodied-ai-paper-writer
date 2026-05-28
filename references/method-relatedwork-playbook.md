# Method + Related Work — Operational Playbook

**Purpose**: How to write the Related Work and Method sections for an embodied-AI submission. These two sections together set up the technical reading.

Use this when the user asks: "Help me write related work", "How should I structure my method section?", "How do I introduce my system?", "Where do I put preliminaries?", "How do I position against prior work?"

---

# PART 1 — Related Work

## Step 1 — Decide whether you have a Related Work section at all

| Venue / Paper type | Section convention |
|---|---|
| **CoRL / ICRA / IROS / RSS** | Standalone "Related Work" section, placed AFTER Introduction and BEFORE Method (or after Method in some RSS papers) |
| **Science Robotics / Nature-family** | No standalone Related Work; prior-work discussion interleaved through Introduction and Discussion |
| **CVPR-adjacent robotics papers** | Standalone Related Work, typically after Intro |

**Rule of thumb**: If your venue is a conference page-budgeted robotics venue, you need a Related Work section. Skip it only if you have explicit precedent in the target journal.

---

## Step 2 — Partition into 2–4 topical subsections

Pick exactly **2–4 topical subsections**, never more (reviewers stop reading after 4). Each subsection covers ONE prior-work theme that your contribution either builds on or differs from.

**Naming convention**: subsections are **noun phrases naming the research class** that the surveyed work belongs to. Four anti-patterns to avoid:

| Anti-pattern | Example (bad) | Fix |
|---|---|---|
| Technique-named instead of theme-named | `**PPO-based methods.**`, `**Diffusion-model-based policies.**` | `**Reinforcement-Learning Manipulation.**`, `**Generative Visuomotor Policies.**` |
| I/O-described instead of class-named | `**Manipulation-trace inputs, divergent prediction targets.**`, `**Trajectory inputs, action outputs.**` | `**VLM/VLA Models for Manipulation.**`, `**Action-Conditioned Trajectory Models.**` |
| Complete sentence with verb (header is doing the bucket's argumentation) | `**Failure reasoning and probe-as-signal differ on what to do with the failed sub-attempt.**` | Strip the verb. Keep `**Failure Reasoning Systems.**`; move the contrast into the paragraph body. |
| Shared redundant tail across headers (universal qualifier) | `**VLM/VLA Models on Manipulation Traces.**` + `**Failure Reasoning on Manipulation Traces.**` + ... | Drop the universal qualifier (`on Manipulation Traces` is the paper's subject — every bucket has it implicitly). Keep only what *distinguishes* this bucket: `**VLM/VLA Models for Manipulation.**`, `**Failure Reasoning Systems.**` |

**Distinctness rule**: each bucket header must carry only the *distinguishing* information against the other 2–3 headers in the same Related Work. Compute the longest common suffix across your headers; if it's more than one word, that suffix is the paper's universal scope — remove it from all headers.

**Case-consistency rule**: pick Title Case OR sentence-case and use it for **every** bucket header in the section. Never mix.
- Title Case (CoRL most common): `**Whole-Body Control.**`, `**Manipulation with Foundation Models.**` — virtually all content words capitalized; lowercase only short function words (`for`, `and`, `on`, `of`, `in`).
- Sentence-case: `**Whole-body control.**`, `**Manipulation with foundation models.**`
- Mixed (e.g., ¶1 ¶2 Title Case + ¶3 ¶4 sentence-case) is a tell that the section was assembled in two passes — reviewers notice.

Good examples (corpus):
- ✓ `**Whole-Body Control.**` · `**Manipulation with Foundation Models.**` · `**Sim-to-Real Transfer.**` · `**Vision-Language-Action Models.**`
- ✓ `**VLM/VLA Models for Manipulation.**` · `**Failure Reasoning Systems.**` (distinct, no shared tail, Title Case)

Two common layouts:

| Layout | Use when |
|---|---|
| **Bold inline subsection leads** — `**Whole-body Control.**` starts each paragraph; no numbering | Conference papers with tight page budgets (most CoRL/RSS) |
| **Numbered subsections** — `2.1 Whole-body Control` | Slightly looser pages, or when subsections run >1 paragraph each |

---

## Step 3 — Write each subsection as a 3-act mini-narrative

Each subsection follows the same internal arc:

### Act 1 — "Recent advances in X have ..." (1–2 sentences)
Open with the field-state opener. Common variants:
- `Recent advances in X have demonstrated ...`
- `Prior work on X has explored ...`
- `A growing body of work has investigated ...`
- `Existing approaches to X largely fall into two categories: ...`

**Pack citations as ranges**: `[10–22]` or `[Smith et al., 2022; Lee et al., 2023; ...]`. The corpus shows clusters of 5–10 citations per opening sentence is normal.

### Act 2 — "Despite this progress ..." (1–2 sentences) — the pivot
Introduce the gap your work addresses. Canonical pivot words:
- `Despite this progress, ...`
- `However, ...`
- `Yet existing methods often ...`
- `These approaches typically assume ...`
- `A common limitation is that ...`

The pivot identifies a *specific* shortcoming that your paper will address — not a generic "more work is needed."

### Act 3 — "Unlike these methods, we ..." (1 sentence) — the positioning closer
Distinguish your contribution. Canonical positioning closers:
- `Unlike these methods, we ...`
- `In contrast, our approach ...`
- `In this work, we instead ...`
- `Our work complements these by ...` (for adjacent/non-competitive work)
- `To the best of our knowledge, we are the first to ...` (use sparingly; see "First claims" below)

---

## Step 4 — Pick the right framing for adjacent work

Not all prior work is competition. The corpus shows three framings:

| Framing | When to use | Closing sentence template |
|---|---|---|
| **Competing** | Prior work tackles the same problem and you outperform | "Unlike these methods, we achieve X without Y." |
| **Complementary** | Prior work tackles an adjacent problem; you build on or compose with it | "Our work is complementary to these and could be combined with ..." |
| **Foundational** | Prior work provides building blocks you use | "We build on these advances by ..." or "We leverage X from [Y]." |

Mis-framing competing work as complementary signals you're hiding from comparisons. Mis-framing complementary work as competing creates unnecessary enemies in the reviewer pool.

---

## Step 5 — Calibrate citation density

The 5:1 rule observed in the corpus:
- **Related Work**: ~5 citations per paragraph (citation-dense; this is the section's job)
- **Method**: ~1 citation per paragraph (citation-sparse; introduce mainly building blocks)
- **Experiments**: ~1 citation per baseline mentioned
- **Conclusion**: 0–1 citations (almost never)

If your Related Work has only 2 citations per paragraph, you are under-citing — reviewers will assume you haven't read the field. If your Method has 5+ citations per paragraph, the work doesn't feel novel.

---

## Step 6 — Handle "First" claims with care

`To the best of our knowledge, we are the first to ...` is a load-bearing sentence. The corpus shows three calibrations:

| Form | Risk level | When safe to use |
|---|---|---|
| **Bare**: "We are the first to do X." | High — invites a single contradicting citation to demolish the claim | Avoid unless absolutely certain |
| **Knowledge-hedged**: "To the best of our knowledge, we are the first ..." | Medium — acceptable if X is specific | Default form |
| **Scope-hedged**: "To the best of our knowledge, we are the first to do X *on Y / in setting Z / with constraint C*." | Low — the scope is the firewall | Use when there's any doubt |

Add scope qualifiers (`on real hardware`, `under partial observability`, `for high-DoF systems`) to make a first-claim defensible.

---

## Step 7 — Anti-patterns to avoid

| Anti-pattern | Fix |
|---|---|
| Annotated bibliography ("Smith [12] proposed X. Lee [13] proposed Y. ...") | Group works that share a theme; cite as a range |
| Encyclopedia syndrome (5 subsections + 200 citations) | Cut to 2–4 subsections |
| Strawman opener ("Most prior work fails to handle ...") | Replace with neutral state-of-field opener |
| No positioning closer | Every subsection MUST end with a positioning sentence |
| Citing yourself without flagging it | Use `Our prior work [X] showed ...` to disclose |
| "Many works have ..." with no citation | Cite or delete |
| Bucket header describes the surveyed work's I/O (`Trajectory inputs, action outputs.`) | Rename as the research-class noun phrase (`Action-Conditioned Trajectory Models.`) |
| Bucket header is a complete sentence with a verb | Strip the verb; keep only the noun phrase. Move the argumentation into the paragraph body. |
| Bucket headers share a redundant trailing phrase (`... on Manipulation Traces.` in every header) | Drop the universal qualifier; headers carry only distinguishing info |
| Mixed case across bucket headers (some Title Case, some sentence-case) | Lock to one convention; Title Case is the CoRL default |

---

## Step 8 — Special case: comparison table instead of prose

When you have 5+ comparable methods and 4+ clean comparison axes, replace the prose Related Work with a comparison table. Rows are prior methods; columns are capabilities (input modality, action space, real-world tested, open-source, etc.); the last row is your method, with the most check-marks.

**Use when**: comparison axes are unambiguous AND prior methods are well-defined.
**Avoid when**: the comparison is about *kind* (different problem formulations) rather than *capability*.

---

# PART 2 — Method Section

## Step 1 — Open with the system-name commitment

The first sentence of Method follows a near-canonical template:

> `In this section, we describe {SystemName}, a {short noun-phrase descriptor} that {one-sentence value proposition}.`

Examples from the corpus:
- "In this section, we describe TinyMPC, an alternating-direction-method-of-multipliers (ADMM) based MPC solver that ..."
- "We present OpenVLA, a 7B-parameter open-source vision-language-action model trained on ..."
- "AESOP is a runtime monitoring framework that combines fast anomaly detection with slow generative reasoning ..."

**Three elements** the opener must contain:
1. System name (bolded or in italics on first use is optional)
2. Short noun-phrase descriptor (≤10 words)
3. Differentiating clause (what makes it different)

---

## Step 2 — Choose your canonical section order

The corpus shows a near-universal four-stage order:

```
Overview → Components → Training → Inference
```

Concretely:
| Stage | Subsection title (typical) | Length |
|---|---|---|
| Overview | "Overview", "System Architecture", "Approach" | 1 paragraph + 1 figure |
| Components | One subsection per component (3–4 components is the sweet spot) | 1–2 paragraphs each |
| Training | "Training", "Training Procedure", "Learning Setup" | 1–3 paragraphs |
| Inference | "Inference", "Deployment", "Runtime Behavior" | 0–1 paragraph |

**Deviation rule**: skip stages only when they don't exist. Solver / theoretical papers may skip Training+Inference entirely. Policy-learning papers may collapse Inference into Training.

---

## Step 3 — Decide whether to include Preliminaries / Background

**Decision rule** (from corpus C2):

| Your contribution is ... | Preliminaries? |
|---|---|
| Fusing 2+ established techniques (e.g., ADMM + LQR, VAE + MDN) | **YES** — one subsection per building block |
| A single new mechanism (novel architecture / loss / constraint) | **NO** — dive straight into Method |

Section title variants: "Preliminaries", "Background", "Foundations" — all equivalent. May be a top-level section (II. BACKGROUND) or an unnumbered subsection at the start of Method.

**Writing style for Preliminaries**: textbook-pedagogical. Definitions, standard equations, citations to canonical references. The writer's voice disappears — it reads like quoted course material.

---

## Step 4 — Write a clean Problem Formulation (four-paragraph template)

When you include a "Problem Formulation" or "Problem Statement" subsection, structure it in four short paragraphs:

| ¶ | Content | Length |
|---|---|---|
| 1 | Input variables and domains (state, observation, ...) | 3–5 sentences |
| 2 | Output (action, policy, plan) | 2–4 sentences |
| 3 | Assumptions (what is given, what is unknown) | 2–4 sentences |
| 4 | Goal as optimization problem or natural-language objective | 2–4 sentences |

**State assumptions explicitly**: `We assume X.` / `We do not assume Y.` / `Note that Z is given.` Each assumption is one less reviewer question.

For RL papers, the MDP/POMDP tuple should appear in ¶1 or ¶2. Variants:
- Formal: `The environment is a POMDP (S, A, R, P, O, γ) where ...`
- Verbal: `We define the observation o_t = (...) and action a_t = ... The policy π is trained to maximize ...`

---

## Step 5 — Use the equation sandwich

For every numbered equation in Method, surround it with:

```
[Lead-in sentence: setting up what the equation expresses]
[Numbered equation]
[Interpretation sentence: what the symbols mean / why it's chosen]
```

Example:

> We train the policy by minimizing the behavior cloning loss:
>
>     L(θ) = E_(o,a)~D [ ||π_θ(o) − a||² ]      (3)
>
> where π_θ is the policy parameterized by θ, and (o, a) are observation-action pairs from the demonstration dataset D.

**Anti-patterns**:
- Equation with no lead-in → reads as ambushing the reader
- Equation with no interpretation → reads as showing off
- Equation that's never referenced again → cut it; it adds friction

---

## Step 6 — Use "we" voice for design choices, passive for mechanics

| Voice | When to use | Example |
|---|---|---|
| **We-voice** | Design choices, decisions, contributions | "We use a ResNet-50 backbone because it provides ..." |
| **Passive** | Mathematical / mechanical descriptions | "The loss is computed as ..." / "Trajectories are sampled from ..." |
| **System-as-subject** | Describing what the system does at runtime | "The policy outputs an action ..." / "TinyMPC iterates between ..." |

Mixing all three is correct and natural. Pure passive feels distant; pure we-voice feels like a personal blog.

---

## Step 7 — Use intuition sentences alongside formal claims

After every non-trivial equation or definition, add an "Intuitively, ..." sentence. The corpus shows reviewers respond strongly to this — it's the load-bearing technique for making technical Method sections approachable.

Patterns:
- `Intuitively, {equation} says that ...`
- `In other words, {claim} means ...`
- `This formulation captures the idea that ...`
- `Concretely, {abstract claim} corresponds to ...`

**Frequency**: roughly 1 intuition sentence per numbered equation, 1 per definition block. Don't skip these in pursuit of formality — reviewers fail papers whose Method they couldn't follow.

---

## Step 8 — Match figure–equation–prose triangulation

For every important Method claim, provide **all three**: a figure that depicts it, equation(s) that formalize it, prose that explains both. If two of the three are missing, the claim is under-supported.

The architecture figure is referenced in the **first paragraph** of Method (not later). Standard wording:
- `Figure 2 illustrates the overall architecture of {SystemName}.`
- `As shown in Fig. 2, our system consists of three components: ...`

Match the figure decomposition to your section decomposition: if Figure 2 shows 3 blocks, Method should have 3 component subsections (one per block).

---

## Step 9 — Use the "Algorithm 1" box when there's a procedural sequence

Algorithm boxes appear when:
- The method has a clear loop or iteration (training algorithm, inference algorithm)
- Multiple steps interact in a non-trivial order
- A diagram would obscure the sequencing

Format conventions:
- `\textbf{Algorithm 1}: {Concise name}` on top
- Input/Output lines first
- Numbered or `\For ... \EndFor` pseudo-code
- One sentence in the prose referencing it: `Algorithm 1 summarizes our training procedure.`

**Don't** use Algorithm boxes for trivially linear pipelines (a 3-step pipeline is better as a figure + prose).

---

## Step 10 — Use the appendix-relegation pattern aggressively — venue-gated

**This step applies only at venues that support an in-PDF appendix** (CoRL / RSS / NeurIPS / ICML / ICLR / AAAI / Science Robotics / Nature Robotics). At those venues, every page-budgeted paper relegates extensively to appendix. Marker sentences:

| Content type | Marker sentence template |
|---|---|
| Hyperparameters | "Full hyperparameters are provided in Appendix X." |
| Architecture details | "Architecture details are deferred to Appendix Y." |
| Proofs | "We defer the proof to Appendix Z." |
| Extended results | "See Appendix W for additional results." |
| Notation tables | "A full notation glossary is provided in Appendix V." |
| Hardware / compute | "Hardware, precision, and token caps are in Appendix~\ref{app:hardware}." |

**Rule (appendix-supporting venues)**: the Method in main text is the *minimum sufficient* description. The appendix is the *complete* description. A first-draft Method is almost always too long — trim by relegating.

### Step 10b — At venues without in-PDF appendix (ICRA / IROS / RA-L / T-RO / IEEE Letters)

These venues have **no `\appendix` section**, so you cannot use `see Appendix X` pointers (reviewers will flag a dead reference). Two options for excess content:

| Content type | Where it goes |
|---|---|
| Hyperparameters, optimizer config, augmentation lists | Code release (`available at \url{...}`, anonymized for blind review) |
| Full algorithm details | Compress into Algorithm 1 box inline; cut decorative steps |
| Extended results, ablations | Supplementary video (for behavior) or omit entirely; reviewers know the venue is tight |
| Proofs | If the proof is non-trivial, cite a tech report (`Proof in our companion arXiv preprint at \url{...}`). If short, inline it |
| Hardware / compute | Compress to ONE inline sentence per Step 9b |

**Rule (no-appendix venues)**: compress, do not relegate. Every claim must survive in the main body or in an external pointer (code repo, project page, separate supplementary PDF if the venue accepts one). NEVER write a `see Appendix X` pointer that resolves nowhere.

See SKILL.md rule 17 for the venue list and the config-dump anti-pattern.

---

## Step 11 — Use roadmap sentences when you have 3+ subsections

If Method has 3 or more subsections, open the section with a roadmap:

> `The rest of this section is organized as follows. Section 3.1 describes the {component A}. Section 3.2 presents the {training procedure for B}. Section 3.3 details the {inference behavior}.`

For shorter Method sections (2 subsections), the roadmap is unnecessary.

---

## Step 12 — Name your method consistently

Once chosen, the system name must be used consistently:
- Same capitalization across abstract, intro, method, conclusion (`OpenVLA` ≠ `Openvla` ≠ `OpenVLa`)
- Defined with a parenthetical expansion on first use in each major section: `OpenVLA (Open Vision-Language-Action)`
- Never substituted with "our method" once introduced — use the name

---

## Step 13 — Match your rhetoric to your paper's sub-corpus

The corpus has three sub-types; matching the wrong vibe is a tell that you haven't read the venue:

| Sub-corpus | Rhetorical signature |
|---|---|
| **Solver / algorithm** (TinyMPC, SARA-RT, Time-Optimal Ergodic) | Heavy on equations, lemmas, propositions. Preliminaries mandatory. Method reads like a textbook chapter. |
| **Policy learning** (OpenVLA, Equivariant Diffusion Policy, MoVEInt) | Reduced equations (typically 1 loss + 1 i/o equation). Heavy on data emphasis. Big architecture figure carries weight. |
| **System / integration** (ANYmal Parkour, AESOP, Open X-Embodiment) | Multiple components, each its own subsection. Block diagrams central. Longer prose, lower equation density. |

A policy-learning paper that reads like a solver paper feels over-formal. A solver paper that reads like a system paper feels under-rigorous.

---

## Step 14 — Theorem / Proposition / Lemma / Claim — size the label to the load

| Label | Use for | Size of claim |
|---|---|---|
| **Theorem** | The paper's headline formal result | Big — load-bearing for the contribution |
| **Proposition** | Supporting results that follow from theorem-level work | Medium |
| **Lemma** | Intermediate technical results, often with proof inline | Small / technical |
| **Claim** | Results stated without proof or with deferred proof | Variable; signals less rigor |

Overclaiming (calling everything a Theorem) reads as posturing. Underclaiming (calling the headline a Lemma) reads as undersold.

---

# Construction workflow (use when drafting Method + Related Work from scratch)

1. **Decide section count**: Will you have Preliminaries? (use Step 3 rule). Will you have a separate Problem Formulation?
2. **Choose 2–4 Related Work themes**. Name each as a noun phrase. List the 5–10 most relevant works per theme.
3. **For each Related Work subsection**: write Act-1 opener, Act-2 pivot, Act-3 positioning closer.
4. **Open Method with the system-name commitment** (Step 1 template).
5. **Insert architecture figure reference in the first paragraph**.
6. **Decompose into components matching the figure** (3–4 component subsections).
7. **For each component subsection**: prose intro → numbered equations with sandwich → intuition sentence.
8. **Add Training subsection** with loss / optimizer / data / hyperparameters / hardware sentences (relegate details to appendix).
9. **Add roadmap sentence** if 3+ subsections.
10. **Match label rigor to your sub-corpus** (Step 13).
11. **Pass through and mark every "we propose X" — make sure X is named consistently across the paper.**

---

# Quick-reference

| User says | Action |
|---|---|
| "How many Related Work subsections?" | 2–4 |
| "Should I have a Preliminaries section?" | Only if fusing 2+ existing techniques |
| "Where does my system name first appear in Method?" | First sentence of Method |
| "My Method section is too long" | Relegate hyperparameters, proofs, ablations to appendix |
| "Should I use 'we' in Method?" | For design choices yes; passive for mechanics |
| "I have only 2 citations in Related Work" | Cite more — aim for ~5 per paragraph |
| "How do I write 'first to do X'?" | Use scope-hedged form: "first to do X *under constraint Y*" |
| "Where do I put the architecture figure reference?" | First paragraph of Method |
| "Algorithm 1 vs. figure?" | Algorithm box for loops/iteration; figure for spatial decomposition |
