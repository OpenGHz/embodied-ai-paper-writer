# Titles — Operational Playbook

**Purpose**: How to construct a paper title for an embodied-AI / robot-learning submission.

Use this when the user asks: "Help me title my paper", "Is this title good?", "What's a better title for {description}?"

---

## Step 1 — Pick the title architecture

Five proven architectures, listed by usage frequency in the 63-paper corpus:

| ID | Architecture | Form | Use when |
|---|---|---|---|
| **A1** | SystemName: Descriptor | `OpenVLA: An Open-Source Vision-Language-Action Model` | You have a named system to promote |
| **A3** | Pure Descriptive (no system name) | `Robot Parkour Learning` / `Learning Agile Soccer Skills for a Bipedal Robot with Deep Reinforcement Learning` | You're presenting a method/result, not a named artifact |
| **A2** | Action-first colon | `Scaling Up and Distilling Down: Language-Guided Robot Skill Acquisition` | The work's contribution is a process/approach (not a system) |
| **A4** | Descriptor (SystemName) | `Equivariant Diffusion Policy` / `Distilled Feature Fields enable few-shot manipulation` | System name flows naturally inside a phrase |
| **A5** | Two-part explainer colon | `EUREKA: Human-Level Reward Design via Coding Large Language Models` | You want to name the system AND explain how it works |

**Architecture decision tree**:
1. Have a memorable system name? → **A1** or **A5** (use A5 if you need the "via X" mechanism to be in the title)
2. No named system, but a clear technique? → **A3** or **A2** (A2 if the leading word is a verb/gerund)
3. System name is itself descriptive (e.g., "Equivariant Diffusion Policy")? → **A4**

---

## Step 2 — Choose your power words

These adjectives and gerunds carry signal weight in the embodied-AI subfield. Pick 1-2, not more.

**Scope adjectives** (signal "we did the hard thing"):
- `Robust`, `Generalist`, `Generalizable`, `General-Purpose`, `Scalable`, `Long-Horizon`, `Real-World`, `Open-Source`, `Foundation`, `Dexterous`, `Agile`, `Multi-Task`, `Cross-Embodiment`

**Action gerunds** (signal "we tackled the problem"):
- `Learning`, `Scaling`, `Solving`, `Achieving`, `Distilling`, `Bootstrapping`, `Mimicking`, `Composing`

**"via" construction** — connects what was achieved to how:
- `{Achievement} via {Mechanism}` — e.g., "Human-Level Reward Design **via** Coding Large Language Models"

**Avoid**: `Novel`, `New`, `Improved`, `Better`, `Optimal`, `Best`. These are weak — reviewers strip them mentally.

---

## Step 3 — Hit the length sweet spot

- **5-8 words**: sweet spot. Most cited papers in the corpus land here.
- **9-12 words**: acceptable if you have a colon (A1, A2, A5).
- **13+ words**: only if you absolutely need both a system name AND an explanatory clause. Be ready to defend it.
- **<5 words**: too cryptic unless the system name is iconic (`ALOHA`, `RoboCat`, `EUREKA`).

Mobile ALOHA pattern: `Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation` — 11 words but balanced by colon.

---

## Step 4 — Naming strategies (if using a system name)

Six strategies that work in this subfield:

1. **Pronounceable acronym**: `OpenVLA`, `ALOHA`, `ACT`, `CLIPort`, `BC-Z`. Aim for 5-letter or shorter.
2. **`Robo-` / `Dex-` / `Bi-` prefix**: `RoboCook`, `RoboFlamingo`, `RoboCat`, `DexCap`, `BiPlay`. Signals robotics-specific.
3. **Mythology / pop culture**: `EUREKA`, `Voltron`, `Hermes`, `Atlas`. Memorable, but only if the metaphor fits.
4. **Animal metaphor**: `ANYmal`, `Cheetah`, `Cassie`. Common for legged platforms.
5. **Numeric series**: `RT-1`, `RT-2`, `RT-X`, `π0`. Use only if you're a major lab that earned a series identity.
6. **Pure descriptive (no name)**: best if your contribution is a technique rather than a system.

---

## Step 5 — Title-abstract coupling

The title and the first sentence of the abstract must share at least 3 content words. Reviewers form their first impression from this pair.

**Strong coupling example** (OpenVLA):
- Title: `OpenVLA: An Open-Source Vision-Language-Action Model`
- Abstract opener: `We introduce **OpenVLA**, a 7B-parameter **open-source vision-language-action** (VLA) model...`

**Weak coupling** (avoid): title says "scalable", abstract opens "we propose a method to..." — the scalability claim is dropped.

---

## Step 6 — Anti-patterns

Reject titles that match any of these:

| Anti-pattern | Bad example | Fix |
|---|---|---|
| "Towards X" without urgency | `Towards Generalist Manipulation` | Drop "Towards"; commit. Or use as A2 if the body really IS preliminary |
| Question titles | `Can Robots Learn from Videos?` | Replace with declarative |
| Buzzword salad | `A Novel Deep Learning Framework for Robust Generalizable...` | Pick ONE scope adjective |
| Mystery system name | `XYZ: A New Approach` | If the system name is uninformative, drop it (use A3) |
| Reviewer-baiting hyperbole | `The Definitive Solution to Manipulation` | Replace with a specific claim |
| Boring participle-stack | `Learning Generalizable Robust Adaptive Policies` | Pick the strongest one |

---

## Step 7 — Venue calibration

| Venue | Title tendency |
|---|---|
| **CoRL** | A1 (system-colon) heavily favored; system papers dominate |
| **RSS** | A3 (pure descriptive) more common; method papers favored |
| **ICRA / IROS** | Either A1 or A3; system names slightly less iconic on average |
| **Science Robotics** | Sentence-case capitalization; longer titles (10-15 words) acceptable; less reliance on system names; e.g., `Reinforcement learning from human videos for humanoid locomotion control` |

Match the journal/conference modal style — it signals you've read the venue.

---

## Step 8 — Special claim suffixes

If your paper has one of these contributions, add a relevant phrase to the title:

- **Open-source**: include `Open-Source` (OpenVLA model)
- **Low-cost / accessible**: include `Low-Cost` (Mobile ALOHA hardware)
- **New dataset**: end with `: A Dataset for X` or `: An Open Dataset of X`
- **New benchmark**: end with `: A Benchmark for X`
- **Preliminary / scoping**: lead with `Towards` (rare; mostly Science Robotics)

---

## Construction workflow (use when generating a title from scratch)

1. **Write the one-sentence abstract first**, then derive the title from it.
2. **List 3 candidate system names** (if any). Pick the most pronounceable.
3. **Identify the 1-2 power words** that capture your contribution.
4. **Draft 3 candidate titles** using different architectures (A1, A3, A4 — try at least three).
5. **Run the abstract-coupling check**: do title and abstract opener share ≥3 content words?
6. **Word-count**: 5-8 words ideal; 9-12 acceptable with colon.
7. **Reject** any title hitting an anti-pattern.
8. **Read aloud**: if it sounds clunky or hyped, simplify.

---

## Examples (verified from corpus, with architecture annotations)

| Title | Architecture | Power words |
|---|---|---|
| `OpenVLA: An Open-Source Vision-Language-Action Model` | A1 | Open-Source |
| `Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation` | A1 | Bimanual, Low-Cost |
| `Robot Parkour Learning` | A3 | Parkour |
| `Learning Agile Soccer Skills for a Bipedal Robot with Deep Reinforcement Learning` | A3 | Agile |
| `Equivariant Diffusion Policy` | A4 | Equivariant |
| `EUREKA: Human-Level Reward Design via Coding Large Language Models` | A5 | Human-Level, via |
| `Scaling Up and Distilling Down: Language-Guided Robot Skill Acquisition` | A2 | Scaling, Distilling |
| `Distilled Feature Fields Enable Few-Shot Language-Guided Manipulation` | A4 | Few-Shot, Language-Guided |

---

## Quick-reference

**User says** | **Action**
---|---
"I have a system named X" | Use A1 or A5
"My contribution is a technique, not a system" | Use A3 or A2
"My title is over 12 words" | Cut to ≤12; add colon if needed
"Should I include 'Novel'/'New'?" | No
"Should I include 'Towards'?" | Only if work is preliminary
"My title and abstract don't share words" | Rewrite one to match the other
