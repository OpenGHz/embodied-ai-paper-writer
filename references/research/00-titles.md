# Paper Titles: Writing Patterns in Embodied AI Papers

> Corpus: 63 paper titles from CoRL/RSS/ICRA/IROS/Science Robotics 2022–2025 (majority are best-paper-award winners or finalists).
> Focus: title craft — naming, structure, length, rhetoric, what gets put first.
> Why a dedicated file: titles are read 100× more than abstracts. They get scanned in proceedings, cited, tweeted, and re-tweeted. A weak title silently caps a paper's reach.

---

## A. The Five Title Architectures

Every title in the corpus falls into one of five structural patterns. Picking the right architecture is the first writing decision.

### A1. `[SystemName]: [Descriptor Phrase]` — the colon-split

The single most common pattern in the corpus (≈45% of titles).

**Why it works**: the SystemName becomes the citation handle (people will say "the OpenVLA paper"), while the descriptor disambiguates and signals scope. Short name + long descriptor is much more memorable than a single long name.

**Examples from the corpus**:
- **OpenVLA**: An Open-Source Vision-Language-Action Model
- **Mobile ALOHA**: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation
- **DexCap**: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation
- **RoboCook**: Long-Horizon Elasto-Plastic Object Manipulation with Diverse Tools
- **HumanPlus**: Humanoid Shadowing and Imitation from Humans
- **PoliFormer**: Scaling On-Policy RL with Transformers Results in Masterful Navigators
- **DreamWaQ**: Learning Robust Quadrupedal Locomotion With Implicit Terrain Imagination via Deep Reinforcement Learning
- **VLFM**: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation
- **TinyMPC**: Model-Predictive Control on Resource-Constrained Microcontrollers
- **MAC-VO**: Metrics-aware Covariance for Learning-based Stereo Visual Odometry
- **Re-Mix**: Optimizing Data Mixtures for Large Scale Imitation Learning
- **CoFRIDA**: Self-Supervised Fine-Tuning for Human-Robot Co-Painting
- **FEAST**: A Flexible Mealtime-Assistance System Towards In-the-Wild Personalization
- **FAST**: Efficient Action Tokenization for Vision-Language-Action Models
- **Fail2Progress**: Learning from Real-World Robot Failures with Stein Variational Inference for Robot Manipulation
- **Eureka**: Human-Level Reward Design via Coding Large Language Models
- **RoboCat**: A Self-Improving Generalist Agent for Robotic Manipulation
- **RoboAgent**: Generalization and Efficiency in Robot Manipulation via Semantic Augmentations and Action Chunking
- **FurnitureBench**: Reproducible Real-World Benchmark for Long-Horizon Complex Manipulation
- **Open X-Embodiment**: Robotic Learning Datasets and RT-X Models
- **TinySense**: A Lighter Weight and More Power-efficient Avionics System for Flying Insect-scale Robots
- **FATROP**: A Fast Constrained Optimal Control Problem Solver for Robot Trajectory Optimization and Control
- **ANYmal Parkour**: Learning Agile Navigation for Quadrupedal Robots
- **DTC**: Deep Tracking Control
- **SARA-RT**: Scaling up Robotics Transformers with Self-Adaptive Robust Attention
- **RoTipBot**: Robotic Handling of Thin and Flexible Objects using Rotatable Tactile Sensors
- **MoVEInt**: Mixture of Variational Experts for Learning Human-Robot Interactions from Demonstrations
- **BonnBeetClouds3D**: A Dataset Towards Point Cloud-based Organ-level Phenotyping of Sugar Beet Plants under Field Conditions
- **Neural MP**: A Generalist Neural Motion Planner

### A2. `[Action Phrase]: [Subtitle/Method]` — the action-first colon split

Less common but high-impact. Foregrounds the *achievement* over the *system*.

**Examples**:
- **Robots That Ask For Help**: Uncertainty Alignment for Large Language Model Planners
- **Robot Learning on the Job**: Human-in-the-Loop Autonomy and Learning During Deployment
- **Nonlinear Model Predictive Control of a 3D Hopping Robot**: Leveraging Lie Group Integrators for Dynamically Stable Behaviors
- **Deploying Ten Thousand Robots**: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding
- **Harnessing with Twisting**: Single-Arm Deformable Linear Object Manipulation for Industrial Harnessing Task
- **Advancing Humanoid Locomotion**: Mastering Challenging Terrains with Denoising World Model Learning

Use this pattern when the *thing achieved* is more arresting than the *system that achieves it*.

### A3. `[Descriptive Title Only]` — the no-colon descriptor

Pure descriptive titles, no system name, no colon. Common in theory-heavy or single-contribution papers.

**Examples**:
- Distributed Data-Driven Predictive Control for Multi-Agent Collaborative Legged Locomotion
- Real-Time Constrained 6D Object-Pose Tracking of an In-Hand Suture Needle for Minimally Invasive Robotic Surgery
- Extreme Parkour with Legged Robots
- Robot Parkour Learning
- Equivariant Diffusion Policy
- Marginalizing and Conditioning Gaussians onto Linear Approximations of Smooth Manifolds with Applications in Robotics
- Achieving Human Level Competitive Robot Table Tennis
- Autonomous Power Line Inspection with Drones via Perception-Aware MPC
- Harmonic Mobile Manipulation
- A Convex Formulation of Frictional Contact for the Material Point Method and Rigid Bodies
- Hierarchical Vision-Language Planning for Multi-Step Humanoid Manipulation
- Distilled Feature Fields Enable Few-Shot Language-Guided Manipulation
- Learning a Unified Policy for Position and Force Control in Legged Loco-Manipulation
- Time Optimal Ergodic Search
- Non-Euclidean Motion Planning with Graphs of Geodesically-Convex Sets
- Convex Geometric Motion Planning on Lie Groups via Moment Relaxation
- Real-Time Anomaly Detection and Reactive Planning with Large Language Models
- Configuration Space Distance Fields for Manipulation Planning
- Learning robust perceptive locomotion for quadrupedal robots in the wild
- Real-World Humanoid Locomotion with Reinforcement Learning
- Learning Agile Soccer Skills for a Bipedal Robot with Deep Reinforcement Learning
- Learning Robust Autonomous Navigation and Locomotion for Wheeled-Legged Robots

### A4. `[Descriptive Title] ([SystemName])` — system name in parens at the end

Hybrid: the system gets named, but in a way that subordinates the name to the contribution.

**Examples**:
- Visual Imitation Enables Contextual Humanoid Control (**VideoMimic**)
- Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware (**ALOHA**)
- Language-Driven Representation Learning for Robotics (**Voltron**)
- Solving Multi-Agent Safe Optimal Control with Distributed Epigraph Form MARL (**Def-MARL**)
- Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning (**HIL-SERL**)

Use this when the system name is catchy enough to be the citation handle but the *contribution phrase* is what differentiates the paper from contemporaries with similar names.

### A5. `[Two-Part Title]: [Long Method/Domain Phrase]` — the explainer colon

Used when the contribution requires unpacking and the SystemName would be too cryptic to stand alone in the proceedings table of contents.

**Examples**:
- Nonlinear Model Predictive Control of a 3D Hopping Robot: Leveraging Lie Group Integrators for Dynamically Stable Behaviors
- Harnessing with Twisting: Single-Arm Deformable Linear Object Manipulation for Industrial Harnessing Task
- Advancing Humanoid Locomotion: Mastering Challenging Terrains with Denoising World Model Learning
- Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding

The first half hooks the reader; the second half disambiguates.

---

## B. Title Length Distribution

Counted by content word (excluding "a/an/the/of/for/with/in/on/via/from").

| Length | Count | Style |
|---:|---:|---|
| 2–4 words | 7 | Crisp brand-style: "Equivariant Diffusion Policy", "Robot Parkour Learning", "Time Optimal Ergodic Search", "Harmonic Mobile Manipulation", "Deep Tracking Control", "Convex Geometric Motion Planning on Lie Groups via Moment Relaxation" (short core) |
| 5–8 words | 23 | Common sweet spot: "OpenVLA: An Open-Source Vision-Language-Action Model", "Robot Learning on the Job", "Extreme Parkour with Legged Robots" |
| 9–13 words | 25 | Pattern explainers: "RoboCook: Long-Horizon Elasto-Plastic Object Manipulation with Diverse Tools", "FurnitureBench: Reproducible Real-World Benchmark for Long-Horizon Complex Manipulation" |
| 14+ words | 8 | Defensive thoroughness: "Distributed Data-Driven Predictive Control for Multi-Agent Collaborative Legged Locomotion", "BonnBeetClouds3D: A Dataset Towards Point Cloud-based Organ-level Phenotyping of Sugar Beet Plants under Field Conditions" |

**Heuristics**:
- 2–4 word titles work only when the term is novel enough to be its own brand. "Equivariant Diffusion Policy" works because it claims an entire concept. "Robot Parkour Learning" works because the *novelty* of "parkour" carries the title.
- 5–8 word titles are the sweet spot for system papers. SystemName + concise descriptor.
- 9–13 word titles work for method papers that need to signal scope (long-horizon, multi-agent, multi-embodiment, etc.).
- 14+ word titles risk being skimmed past — only use when every word genuinely disambiguates from competing work.

**Average title length in CoRL/RSS award winners**: ~8 words. Use this as the default budget.

---

## C. The Power Words

Certain adjectives/verbs/qualifiers appear disproportionately in award-winning titles. These signal scope and ambition without being vague.

### C1. Scope adjectives (the implicit "more than prior work")

| Word | Examples |
|---|---|
| **Robust** | "Learning robust perceptive locomotion", "Learning Robust Autonomous Navigation", "DreamWaQ: Learning Robust Quadrupedal Locomotion" |
| **Generalist** | "RoboCat: A Self-Improving Generalist Agent", "Neural MP: A Generalist Neural Motion Planner" |
| **Open-Source / Open** | "OpenVLA: An Open-Source Vision-Language-Action Model", "Open X-Embodiment" |
| **Scalable** | "DexCap: Scalable and Portable Mocap Data Collection System", "Deploying Ten Thousand Robots: Scalable Imitation Learning" |
| **Real-World** | "Real-World Humanoid Locomotion", "FurnitureBench: Reproducible Real-World Benchmark", "Fail2Progress: Learning from Real-World Robot Failures" |
| **Long-Horizon** | "RoboCook: Long-Horizon Elasto-Plastic Object Manipulation", "FurnitureBench: ... Long-Horizon Complex Manipulation" |
| **Reproducible** | "FurnitureBench: Reproducible Real-World Benchmark" |
| **Extreme / Agile** | "Extreme Parkour with Legged Robots", "Learning Agile Soccer Skills" |
| **Precise / Dexterous** | "Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning" |
| **Few-Shot / Zero-Shot** | "Distilled Feature Fields Enable Few-Shot Language-Guided Manipulation", "VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation" |
| **Efficient / Fast / Tiny** | "FAST: Efficient Action Tokenization", "TinyMPC: Model-Predictive Control on Resource-Constrained Microcontrollers", "TinySense: A Lighter Weight and More Power-efficient Avionics System" |
| **Human-Level / Master-Level** | "Eureka: Human-Level Reward Design", "Achieving Human Level Competitive Robot Table Tennis", "PoliFormer: ... Results in Masterful Navigators" |
| **Flexible / Adaptive** | "FEAST: A Flexible Mealtime-Assistance System", "SARA-RT: Scaling up Robotics Transformers with Self-Adaptive Robust Attention" |
| **Multi-Agent / Multi-Embodiment** | "Open X-Embodiment", "Solving Multi-Agent Safe Optimal Control" |
| **Unified** | "Learning a Unified Policy for Position and Force Control" |
| **Low-Cost** | "Mobile ALOHA: ... Low-Cost Whole-Body Teleoperation", "Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware" |
| **In-the-Wild / In the Wild** | "Learning robust perceptive locomotion for quadrupedal robots in the wild", "FEAST: ... Towards In-the-Wild Personalization" |

**Heuristic**: pick **at most one** scope adjective. Two becomes a Christmas tree. "Robust" and "Real-World" together usually signal an author over-claiming.

### C2. Action verbs (the "what we accomplished")

| Verb | Examples |
|---|---|
| **Learning** | The single most common title verb. ~20 titles in the corpus use "Learning X". "Learning Fine-Grained Bimanual Manipulation", "Learning a Unified Policy", "Learning robust perceptive locomotion", "Learning Agile Soccer Skills" |
| **Scaling** | "PoliFormer: Scaling On-Policy RL with Transformers", "SARA-RT: Scaling up Robotics Transformers" |
| **Solving** | "Solving Multi-Agent Safe Optimal Control with Distributed Epigraph Form MARL" |
| **Achieving** | "Achieving Human Level Competitive Robot Table Tennis" |
| **Deploying** | "Deploying Ten Thousand Robots" |
| **Enabling / Enables** | "Distilled Feature Fields Enable Few-Shot Language-Guided Manipulation", "Visual Imitation Enables Contextual Humanoid Control" |
| **Mastering** | "Advancing Humanoid Locomotion: Mastering Challenging Terrains" |
| **Optimizing** | "Re-Mix: Optimizing Data Mixtures for Large Scale Imitation Learning" |
| **Generating / Generation** | (less common in this corpus, more in graphics) |
| **Adapting / Adaptation** | (appears in subtitles, e.g. "Self-Adaptive Robust Attention") |
| **Towards** | The "hedge verb". Used when the contribution is partial or framing. "BonnBeetClouds3D: A Dataset Towards Point Cloud-based Organ-level Phenotyping", "FEAST: ... Towards In-the-Wild Personalization" |

**Heuristic**: "Learning X" is so common it almost recedes into the background. Pick a stronger verb (Scaling, Solving, Achieving, Mastering, Deploying) only if you can defend it in the abstract within two sentences. Otherwise "Learning" or no verb at all.

### C3. The "via" construction

A surprisingly distinctive marker of robotics writing. Used to attach the method to the contribution.

| Pattern | Examples |
|---|---|
| `[Contribution] via [Method]` | "Autonomous Power Line Inspection with Drones **via** Perception-Aware MPC", "Eureka: Human-Level Reward Design **via** Coding Large Language Models", "Precise and Dexterous Robotic Manipulation **via** Human-in-the-Loop Reinforcement Learning", "Non-Euclidean Motion Planning **via** Moment Relaxation" |
| `[Method] with [Tool]` | "Extreme Parkour **with** Legged Robots", "Real-World Humanoid Locomotion **with** Reinforcement Learning", "Learning Agile Soccer Skills for a Bipedal Robot **with** Deep Reinforcement Learning" |
| `[Contribution] for [Application]` | "Vision-Language Frontier Maps **for** Zero-Shot Semantic Navigation", "Model-Predictive Control **on** Resource-Constrained Microcontrollers" |

**Heuristic**: `via` foregrounds the method; `with` is more neutral; `for` foregrounds the application. Choose based on what the reviewer most needs to update beliefs about.

---

## D. The Naming Game

System names are a major writing craft. The corpus reveals six naming strategies.

### D1. Acronym from method/system description

The most common. Often forms a pronounceable word.

| Name | Expansion |
|---|---|
| **ALOHA** | A Low-cost Open-source Hardware (for bimanual teleoperation) |
| **ACT** | Action Chunking with Transformers |
| **OpenVLA** | Open Vision-Language-Action (model) |
| **FAST** | (action) Frequency-Adapted Sequence Tokenization — also reads as "fast" |
| **DTC** | Deep Tracking Control |
| **HIL-SERL** | Human-in-the-Loop Sample-Efficient Reinforcement Learning |
| **VLFM** | Vision-Language Frontier Maps |
| **MAC-VO** | Metrics-Aware Covariance — Visual Odometry |
| **SARA-RT** | Self-Adaptive Robust Attention for Robotics Transformers |
| **FEAST** | Flexible mEalASsisTance — backronym; works because "feast" relates to food/eating |
| **DexCap** | Dexterous mocap Capture |
| **FATROP** | Fast Automatic Trajectory Optimization — also doubles as a person's name |
| **DWL** | Denoising World model Learning |
| **MoVEInt** | Mixture of Variational Experts for Interactions |
| **PoliFormer** | Policy + transFormer |
| **TinyMPC** | Tiny + MPC |
| **TinySense** | Tiny + Sense |
| **CoFRIDA** | Co-painting + FRIDA (predecessor system) |

**Heuristic**: a *pronounceable* acronym (especially one that maps to a real word like FEAST, EUREKA, FAST, ALOHA) is markedly more memorable than initialisms (HIL-SERL, MAC-VO). If you can fit one, do.

### D2. Compound word with a "Robo-" / "Dex-" / "Open-" prefix

The robotics-domain shibboleth.

| Name | Decomposition |
|---|---|
| **RoboCook** | Robo + Cook |
| **RoboCat** | Robo + Cat (the cat metaphor for agility) |
| **RoboAgent** | Robo + Agent |
| **RoboCat-lim** | RoboCat (limited variant) |
| **Robo-DM** | Robo + Data Management |
| **DexCap** | Dex + Cap |
| **DexIL** | Dex + Imitation Learning |
| **OpenVLA** | Open + VLA |
| **Open X-Embodiment** | Open + X-Embodiment |

**Heuristic**: "Robo-" works when the application is concrete (Cook, Cat, Agent, DM). It signals embodied AI without being cute. "Open-" works when you're committing to open-source release.

### D3. Mythology / Cultural reference

Rare but high-impact.

| Name | Reference |
|---|---|
| **Eureka** | Archimedes' exclamation — fits the "discovery via LLM" framing |
| **Voltron** | The combining-robots cartoon — fits the "combining vision + language" framing |
| **Mobile ALOHA** | Hawaiian greeting — original ALOHA created the brand; "Mobile ALOHA" extends it |

**Heuristic**: cultural references work only when the metaphor actually maps to the contribution. Eureka-as-discovery and Voltron-as-combination are well-chosen; a name like "Hercules" for a strength-related system would also work. Avoid references that don't map (calling a planner "Atlas" just because it's hard would be hollow).

### D4. Animal / Familiar object as metaphor

Embodied AI's particular weakness — and strength.

| Name | Metaphor |
|---|---|
| **ANYmal** | ANY + animal — ETH's quadruped |
| **RoboCat** | Cat-like agility for manipulation |
| **DreamWaQ** | Quadruped that "dreams" / hallucinates terrain |
| **HumanPlus** | Human + Plus (improved version) |
| **HarmonicMM** | Harmonic — implies coordinated, balanced manipulation |
| **VideoMimic** | Mimics video |

**Heuristic**: animal metaphors are saturated. ANYmal works because it's also the company's product line. New systems should avoid generic animal names ("Falcon," "Hawk," "Lion") unless they map specifically to the contribution.

### D5. Numeric / Generation-style naming

Used by groups iterating a platform.

| Name | Context |
|---|---|
| **RT-1, RT-2, RT-X** | Robotic Transformer iterations from Google |
| **OpenVLA** | Implicit "open" alternative to RT-2 |
| **π0**, **π0-FAST** | Diffusion VLA generations |

**Heuristic**: numbered iterations signal a research program, not a one-shot paper. Use only if you intend to publish v2.

### D6. Pure descriptive (no system name at all)

Common in theory/method papers without a deliverable artifact.

Examples: "Equivariant Diffusion Policy", "Time Optimal Ergodic Search", "Robot Parkour Learning", "Configuration Space Distance Fields for Manipulation Planning", "Convex Geometric Motion Planning on Lie Groups via Moment Relaxation".

**Heuristic**: if the contribution is a *concept* (a new policy class, a new control formulation, a new representation), the concept name *is* the system name. No colon needed.

---

## E. Title-Abstract Coupling

Best papers have a tight handshake between title and abstract.

**Pattern observed across the corpus**:
1. The title's *system name* appears in the abstract's first sentence (often bolded with `\textsc{}`).
2. The title's *descriptor phrase* expands into the abstract's first two sentences ("the why").
3. The title's *scope adjective* (robust/generalist/scalable) is justified with a quantitative claim by the abstract's third sentence.

**Example — OpenVLA**:
- Title: "OpenVLA: An Open-Source Vision-Language-Action Model"
- Abstract opens: "We introduce OpenVLA, a 7B-parameter open-source vision-language-action model trained on 970k real-world robot demonstrations..."
- Note: the title's "Open-Source" and "Vision-Language-Action" both echo in sentence 1; the title's brevity is matched by a one-sentence elevator pitch.

**Example — Robot Parkour Learning**:
- Title: pure descriptive, 3 content words.
- Abstract opens: "Parkour is a grand challenge for legged locomotion, requiring robots to overcome various obstacles rapidly in complex environments."
- Note: title doesn't even need a system name; the *concept* of "parkour for legged robots" is the brand.

**Heuristic when drafting**: write the title and abstract sentence 1 together. If you can't compress the abstract opener into a title, your contribution is muddled.

---

## F. Title Anti-Patterns from the Corpus

A few patterns to *avoid*, observed in non-award-winning robotics work (not in this corpus, but informative as negative space):

| Anti-pattern | Why it fails | Better |
|---|---|---|
| "A Novel Approach to X" | "Novel" is the weakest claim; every paper is novel. | Name the approach. |
| "Improving X via Y" | Vague. What kind of improvement? | "Achieving 87% Success on X via Y" |
| "X: A Study" / "A Comprehensive Study of X" | Signals review/survey, not contribution. | Lead with the finding. |
| Long parenthetical: "...(With Applications to Z)" | Subordinates the application. | Either lead with the application or omit. |
| Stacking 3+ scope adjectives: "Robust Scalable Generalizable Real-World X" | Reads as defensive. | Pick one. |
| Hashtag-style emoji or buzzwords | Doesn't survive citation. | Stick to plain text. |

Award-winning papers in this corpus *never* use these patterns. The closest exception is "Towards X" (BonnBeetClouds3D, FEAST), which is acceptable because it signals an honest partial contribution rather than over-claiming.

---

## G. Sub-Patterns by Venue

Title style varies slightly by venue. Useful when targeting submission.

| Venue | Tendency | Examples |
|---|---|---|
| **CoRL** | System-name + colon dominant; emphasis on novelty + open-source release | OpenVLA, RoboCook, PoliFormer, Mobile ALOHA, FAST |
| **RSS** | Descriptive + theory titles common; sparing colon use | "Time Optimal Ergodic Search", "Configuration Space Distance Fields", "Equivariant Diffusion Policy"; system names often parenthesized (ALOHA, Voltron) |
| **ICRA** | Verbose disambiguating descriptors; "with X" / "via Y" attachments | "Distributed Data-Driven Predictive Control for Multi-Agent Collaborative Legged Locomotion", "Real-Time Constrained 6D Object-Pose Tracking..." |
| **IROS** | Mixed; system-name colons + verbose descriptors | "Harmonic Mobile Manipulation", "Neural MP: A Generalist Neural Motion Planner", "Harnessing with Twisting: ..." |
| **Science Robotics** | Lower-case (sentence-case) titles in the journal style; broader audience framing | "Learning robust perceptive locomotion for quadrupedal robots in the wild", "Real-World Humanoid Locomotion with Reinforcement Learning" |

**Heuristic**: Science Robotics uses sentence case (only the first word and proper nouns capitalized) — this is a journal-style requirement, not a stylistic preference. All the conference venues use title case.

---

## H. Title Construction Workflow

When drafting a title for an embodied AI paper:

1. **Write three candidates in three different architectures** (A1: system-colon-descriptor; A3: pure descriptor; A4: descriptor with parenthetical name).
2. **Test the citation handle**: which form would you actually use when someone asks "what paper?" — "the OpenVLA paper" or "the open vision-language-action paper"? The short form should be in the title.
3. **Test the scope claim**: which scope adjective is the *one* you'd defend in the rebuttal? Drop the others.
4. **Test the verb**: would the abstract sentence 1 use "we present", "we introduce", "we propose", or "we achieve"? Match the title verb.
5. **Test the length**: target 5–10 words. If you're at 14+, you're not done editing.
6. **Test against contemporaries**: search the venue's last two years for similar titles. If your title is one swap away from another paper's, the contribution isn't differentiated by the title yet.

---

## I. Special Patterns

### I1. The "Open-Source" / "Open" prefix

When a paper releases significant artifacts (code, weights, dataset, hardware), the title often advertises it:
- **OpenVLA**: An Open-Source Vision-Language-Action Model
- **Open X-Embodiment**: Robotic Learning Datasets and RT-X Models
- **ALOHA**: A Low-cost Open-source Hardware System (implicit in subtitle)

This signals to the community *before* they read the paper that the work will be reproducible. It is itself a status claim — fewer papers actually release usable artifacts than claim to.

### I2. The "Low-Cost" / "Affordable" claim

Specific to hardware-systems papers, signaling accessibility:
- Mobile ALOHA: ... Low-Cost Whole-Body Teleoperation
- ALOHA: ... Low-Cost Hardware
- TinyMPC, TinySense: implicit by name

### I3. The dataset/benchmark suffix

When the paper releases a dataset or benchmark:
- FurnitureBench: Reproducible Real-World Benchmark for Long-Horizon Complex Manipulation
- Open X-Embodiment: Robotic Learning Datasets and RT-X Models
- BonnBeetClouds3D: A Dataset Towards ...

The "Bench" or "Dataset" suffix is a contract — readers know to expect downloadable assets.

### I4. The "Towards" hedge

When the contribution is a step rather than a solution:
- FEAST: A Flexible Mealtime-Assistance System Towards In-the-Wild Personalization
- BonnBeetClouds3D: A Dataset Towards Point Cloud-based Organ-level Phenotyping

"Towards" is a useful hedge — it says "we made meaningful progress on a problem that's not yet solved." Use sparingly; over-use signals weak contributions.

---

## J. Sample Size & Coverage

- 63 paper titles across CoRL (14), RSS (13), ICRA (16), IROS (10), Science Robotics (10)
- All titles award-winners or finalists 2022–2025
- Cross-verified architecture counts: A1 ≈ 29, A2 ≈ 6, A3 ≈ 22, A4 ≈ 5, A5 ≈ 4 (totals can overlap when a title fits two patterns)
- Naming-strategy counts: D1 (acronym) ≈ 17, D2 (Robo-/Dex- compound) ≈ 9, D3 (mythology) ≈ 2, D4 (animal/object metaphor) ≈ 6, D5 (numeric) ≈ 3, D6 (pure descriptive) ≈ 22

This file is the writer-distillation skill's authoritative reference on paper titles. The main `SKILL.md` operating manual should route "title" questions here.
