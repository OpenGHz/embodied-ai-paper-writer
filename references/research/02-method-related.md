# 02 — Method + Related Work Craft

Scope: rhetorical and structural conventions for writing the **Related Work**, **Preliminaries / Background**, and **Method / Approach** sections of top-venue embodied-AI papers. ~12 award-winning/notable papers analyzed (ICRA, IROS, CoRL, RSS, Science Robotics; 2023–2025). Focus is on HOW these sections are written, not what the techniques are. The full list of papers and the corpora sub-cuts are recorded at the end of this file.

This document is a sibling to `01-abstract-intro.md`. Where that file teaches the openings, this one teaches the body of the paper up through the method.

---

## A. Related Work patterns

### A1. Related Work is partitioned into 2–4 topical subsections, each a one-paragraph "family"
**Pattern**: Award-winning papers do not write Related Work as a flat block of citations. Instead they break it into 2–4 bolded or numbered subsections, each grouping a *family of prior approaches* relevant to the contribution. Each subsection is typically a single paragraph of 5–10 sentences, opens by naming the family, surveys 4–12 references with brief positioning, and (almost always) closes with a "we differ from these in..." sentence (see A2).

**Evidence**:
- Open X-Embodiment uses three italicized subsection labels: "*Transfer across embodiments.*", "*Large-scale robot learning datasets.*", and "*Language-conditioned robot learning.*" — each one paragraph, each ending with how this work differs. [arxiv:2310.08864]
- CoFRIDA uses two numbered/lettered subsections: "A. Computer-Based Image Co-Creation" and "B. Robotic Image Co-Creation" — splitting the literature by whether the prior work is computer-only or robotic. [arxiv:2402.13442]
- Distilled Feature Fields uses three bolded headers: "**Geometry-Aware Manipulation.**", "**Foundation Models for Robotics.**", and "**Pre-Trained Vision-Language Features for Robotics.**" — moving from older/narrower work to nearer-neighbor work. [arxiv:2308.07931]
- OpenVLA partitions Related Work into "**Visually-Conditioned Language Models**", "**Generalist Robot Policies**", and "**Vision-Language-Action Models**" — three families that compose into the contribution. [arxiv:2406.09246]

**Variants**: SARA-RT [arxiv:2312.01990] merges introduction and related work into a single section titled "I. INTRODUCTION & RELATED WORK" and uses inline citations rather than subsections — a compression technique used when the conference page budget is tight. TinyMPC [arxiv:2310.16985] omits Related Work as a separate section entirely, embedding prior-work discussion inside the Background section.

**Why it works**: Subsection labels let the reviewer immediately verify "have they covered the literature I think they should have?" Each label is a checkbox the reviewer can tick before reading the paragraph in detail. Grouping by family (not chronology, not author) also makes the positioning move at the end of each paragraph land harder — the reader has just absorbed what the family does, so the contrast is immediate.

---

### A2. Each Related Work subsection closes with a one-sentence positioning move
**Pattern**: The final sentence of nearly every Related Work paragraph names the gap THIS paper fills relative to that family. Stock forms: "Unlike these methods, we...", "In contrast, we...", "We differ from these in that...", "Our work is complementary in that...". Rarely longer than one sentence; rarely uses hedging language.

**Evidence**:
- "Unlike most of these prior works, we directly train a policy on X-embodiment data, without any mechanisms to reduce the embodiment gap, and observe positive transfer by leveraging that data." [arxiv:2310.08864]
- "These datasets contain data of robots of the same type, whereas we focus on data spanning multiple embodiments." [arxiv:2310.08864]
- "We train language-conditioned policies via imitation learning like many of these prior works but do so using large-scale multi-embodiment demonstration data." [arxiv:2310.08864]
- "However, Computer-based painting models do not transfer well out-of-the-box into the real world due to the Sim2Real gap." [arxiv:2402.13442]
- "While FRIDA plans based on current canvas state, it uses CLIP and gradient descent for planning which produces paintings that are very noisy and only loosely resemble the input text." [arxiv:2402.13442]

**Variants**: The positioning may be split across two sentences when (a) the gap is enumerated as multiple items, or (b) the contribution is partially shared with prior work — in which case the writer first acknowledges what is shared ("Like X, we use Y...") then states what is novel ("However, we additionally..."). Open X-Embodiment uses this two-step shape repeatedly.

**Why it works**: Reviewers form an "X did Y" mental model from each Related Work paragraph and then need a single decisive sentence telling them what's different. Without this sentence the paragraph reads as a literature dump; with it, the paragraph reads as principled positioning.

---

### A3. Numbered citation runs ("[10–22]", "[23–29]") signal "this is a known cluster, not the focus"
**Pattern**: When a paper wants to acknowledge a large literature without spending sentences on it, it cites a range or list of refs in a single bracket: "[10–22]", "[8, 86–95]", "[33–43]". This compresses 5–15 papers into a single signal that says "we know about this cluster, but it's not where we're contributing." Used heavily by papers with broad framing.

**Evidence**:
- "A number of prior works have studied methods for transfer across robot embodiments in simulation [10–22] and on real robots [23–29]." [arxiv:2310.08864]
- "...methods for transfer across human and robot embodiments also often employ techniques for reducing the embodiment gap, i.e. by translating between domains or learning transferable representations [33–43]." [arxiv:2310.08864]
- "The robot learning community has created open-source robot learning datasets, spanning grasping [60–71], pushing interactions [23, 72–74], sets of objects and models [75–85], and teleoperated demonstrations [8, 86–95]." [arxiv:2310.08864]
- "Linear attention mechanisms is an area of active research ([22], [23], [24], [25], [26], [27], [28], [29], [30])..." [arxiv:2312.01990]

**Variants**: When the cluster needs further sub-grouping, the writer lists sub-clusters inside the same sentence with semi-colons: "...grasping [60–71], pushing interactions [23, 72–74], sets of objects and models [75–85]..." [arxiv:2310.08864]. This shape lets the writer telegraph the *taxonomy* of the cluster within a single sentence.

**Why it works**: A reviewer skimming Related Work uses citation density as a proxy for thoroughness. Range citations achieve high density per sentence without forcing the reader to digest a sentence per reference. This is the bibliographic equivalent of a chart showing "here is the cluster; here is the gap."

---

### A4. The "complementary, not competitive" framing for adjacent work
**Pattern**: When the paper sits next to (rather than against) a body of related work — e.g., it builds on a prior system, or addresses an aspect the prior work didn't — writers use the words "complementary", "build on", "extend", "are inspired by". This is a softer move than "in contrast" and is reserved for the closest neighbors, often the writers' own prior work or work from the same lab.

**Evidence**:
- "The goal of our data repository is complementary to these efforts: we process and aggregate a large number of prior datasets into a single, standardized repository..." [arxiv:2310.08864]
- "We investigate complementary architectures and provide complementary analyses, and, in particular, study the interaction between X-embodiment transfer and web-scale pretraining." [arxiv:2310.08864]
- "Following previous works that leverage pre-trained language embeddings [...] and pre-trained vision-language models [...] in robotic imitation learning, we study both forms of pre-training in our experiments..." [arxiv:2310.08864]
- "Our approach, CoFRIDA shown in Fig. 3, is made up of three primary components: ... and (3) a self-supervised method for creating training data using FRIDA to fine-tune pre-trained models in the Co-Painting Module." (CoFRIDA explicitly builds on FRIDA, framed as extension rather than competition) [arxiv:2402.13442]

**Why it works**: Adjacent-work authors are often reviewers. The "complementary" framing acknowledges their contribution without conceding novelty — a diplomatic move that also lets the writer claim a different evaluation regime ("we study X they didn't study").

---

### A5. Related Work placement varies by venue and contribution type — Related Work after the Method is the conference default; after Intro is the journal default
**Pattern**: There are three placements for Related Work in this corpus, and the choice is not arbitrary. (1) **After the Intro, before the Method** — the standard CoRL/NeurIPS/RSS shape: helps the reader build intuition for the contribution before diving into details. (2) **After the Method, before Experiments** — common in IEEE conference papers (ICRA/IROS) and in solver/algorithm papers, where the contribution is technical and the writer wants the reader to understand the contribution before contextualizing it. (3) **Merged into the Intro** — used when page budget is tight, when the field is small enough that prior work can be discussed inline, or when the contribution is so novel that there is no obvious family to compare against.

**Evidence**:
- CoRL papers consistently place Related Work right after Intro, as Section 2: Equivariant Diffusion Policy [arxiv:2407.01812] has "2 Related Work" before "3 Background" and "4 Method"; Unified Policy [arxiv:2505.20829] places "2 Related Works" before "3 Method"; Robots Ask for Help [arxiv:2307.01928] places "5 Related Work" AFTER the experiments — a notable inversion done because the paper frames itself as a methodology contribution and the reader needs the framework before the comparisons.
- ICRA/IROS papers place Related Work as Section II right after Intro: Power Line MPC has "II. RELATED WORK" then "III. METHODOLOGY" [arxiv:2304.00959]; TinyMPC has Section II as "BACKGROUND" (functionally a hybrid related work + preliminaries) before Section III "THE TINYMPC SOLVER" [arxiv:2310.16985].
- RSS papers vary: Time-Optimal Ergodic Search uses the conference shape "II. RELATED WORK" then "III. PRELIMINARIES" then "IV. ..." [arxiv:2305.11643]; AESOP/RT Anomaly Detection follows the same shape with "II. RELATED WORK", "III. PROBLEM FORMULATION", "IV. PROPOSED APPROACH" [arxiv:2407.08735].
- SARA-RT [arxiv:2312.01990] *merges* "I. INTRODUCTION & RELATED WORK" into a single section because of ICRA page limits.

**Variants**: Science Robotics is a journal and follows a journal shape: II. Results, III. Discussion, IV. Materials and Methods — no separate Related Work section. Prior-work discussion is interleaved throughout Methods and Discussion as needed [arxiv:2306.14874]. KNOWNO [arxiv:2307.01928] uses the unusual "Related Work AFTER experiments" placement to preserve narrative momentum.

**Why it works**: Reviewers from a given venue expect the venue's conventional shape. CoRL reviewers expect Related Work before Method; ICRA reviewers tolerate either, but value early framing. Knowing the venue convention is part of writing for that venue.

---

### A6. The "Recent advances in X have ..." opener is the dominant first sentence of a Related Work subsection
**Pattern**: When a paper opens a Related Work subsection, the most common rhetorical move is a sentence that names the family and credits the recent surge in work: "Recent works have shown...", "Recent advances in X have...", "A growing body of work has...", "Existing literature on X..." This opener positions the family as active and warrants the rest of the paragraph. A near-cousin opener is the definitional move ("X is a class of methods that..."), used when the family is older or more textbook.

**Evidence**:
- "Recent works [9, 22, 23, 24, 25, 26, 27, 10, 28, 29, 30, 31, 32] compellingly show that improvement in sample efficiency and performance can be obtained by leveraging symmetries in policy leaning." [arxiv:2407.01812]
- "Recent work has shown that the internet-scale pretraining data provides FMs with strong zero-shot reasoning capabilities, which has enabled..." [arxiv:2407.08735]
- "Large language models have shown a wide range of capabilities: reasoning [19, 20], logic [21, 22], math [23], physics [24, 25], high-level planning [1, 26, 27, 28, 29, 30] with language feedback [31, 2], and writing robot code [5, 32, 33]." [arxiv:2307.01928]
- "More recently, RL with parallel simulators [19, 22] has become the mainstream approach for addressing complex control challenges in legged robots." [arxiv:2505.20829]
- "Recent extensions have moved away from the limited grid approximations and worked on continuous work-spaces using cellular decomposition or continuous potential-field methods [37, 12, 38]." [arxiv:2305.11643]
- "Hierarchical reinforcement learning has gained attention in the field of robotics as it enables robots to acquire, combine, and reuse versatile skills in order to solve complex tasks." [arxiv:2306.14874]

**Variants**: The definitional opener — "X is a..." or "X has been widely adopted..." — is used when the family is a textbook concept rather than a recent surge: "Whole body control (WBC) has been widely adopted to enhance robotic capabilities in mobile manipulation..." [arxiv:2505.20829]; "The linear-quadratic regulator (LQR) [33] is a widely used approach for solving robotic control problems." [arxiv:2310.16985]. Either form works; the trigger is whether the family is "established" or "emerging".

**Why it works**: Each subsection's first sentence sets a frame for how the family will be evaluated. "Recent" framing implicitly says "this is where the action is", which adds urgency to the gap the writer will later identify. The definitional framing implicitly says "this is textbook" — which adds gravity to the writer's claim of novelty against it.

---

### A7. The "Despite this progress, ..." pivot — explicit gap-naming after the literature survey
**Pattern**: After surveying 2–6 references in a Related Work paragraph, the writer pivots with a contrastive connective that names the gap: "However, ...", "Despite this progress, ...", "Yet, ...", "In contrast, ...", "Nevertheless, ...". This pivot comes ~60–80% of the way through the paragraph and is what makes a paragraph a *positioning* paragraph rather than a *summary* paragraph. The pivot sentence is structurally distinct from the closing positioning sentence (A2) — the pivot names the limitation in the literature; the closer states what THIS paper does about it.

**Evidence**:
- "However, the adoption of FMs in-the-loop of safety-critical robotic systems is immediately met with two challenges. First, [...] Second, [...]" — explicit gap pivot followed by enumeration [arxiv:2407.08735]
- "However, these works do not propose practical strategies to integrate them in closed-loop. Therefore, we propose a closed-loop control framework..." — pivot + closer in two adjacent sentences [arxiv:2407.08735]
- "However, the issue of response time associated with FMs has not been a focal point in these studies." [arxiv:2407.08735]
- "However, these methods optimize trajectories over a fixed time horizon, resulting in a lack of control over the granularity of how a robot searches an area. Therefore, in this paper, we pose and investigate solutions to..." [arxiv:2305.11643]
- "However, prior work typically has planning horizons that are fixed and are not considered part of the optimization." [arxiv:2305.11643]
- "However, these methods did not leverage the geometric symmetries underlying the task and the diffusion process." [arxiv:2407.01812]
- "However, these methods cannot represent the full 3D configuration of the world and cannot extrapolate beyond visible data..." [arxiv:2306.14874]
- "However, state-of-the-art methods [19], [20] cannot directly be applied to the power line inspection problem because they neglect the objective of tracking visual points of interest..." [arxiv:2304.00959]

**Variants**: When the gap is multi-part, the pivot may be followed by an enumeration ("Two challenges remain. First, ... Second, ..." as in AESOP [arxiv:2407.08735]) or by a colon and a list. When the writer wants softer language, "Nevertheless" or "Yet" replaces "However"; "While" can lead a clause that absorbs the gap into the same sentence ("While these methods achieve X, they cannot Y").

**Why it works**: The pivot is the rhetorical *machine* of a Related Work paragraph. Without it, the paragraph is a literature review. With it, the paragraph is an argument. Reviewers scanning for whether the paper has a thesis look for these pivots; their absence is a red flag.

---

### A8. Citation density is highest in Related Work and lowest in Method — a 5-to-1 rule of thumb
**Pattern**: Across the corpus, Related Work paragraphs average 1.5–3 citations per sentence; Method-section paragraphs average <0.5 citations per sentence. The density drops sharply at the Method-section boundary. When Method does cite, it cites for one of three reasons: (a) attributing a borrowed technique ("we use the Riccati recursion [33] to..."), (b) acknowledging an inherited dataset or simulator ("we use MimicGen [11]"), or (c) deferring a derivation to an appendix or canonical reference ("See [22] for details").

**Evidence**:
- Related Work paragraph in Equivariant Diffusion Policy: "Recent works [9, 22, 23, 24, 25, 26, 27, 10, 28, 29, 30, 31, 32] compellingly show that improvement in sample efficiency and performance can be obtained by leveraging symmetries in policy leaning. [33, 34, 35] show the efficiency of equivariant models for on-robot learning. [36, 37, 38, 39] learn an open-loop pick and place policy..." — three sentences with ~25 citations total [arxiv:2407.01812]
- Method paragraph from the same paper: "The main contribution of this paper is a method that incorporates equivariance in the diffusion process for policy learning. As theoretical justification, we first analyze the noise prediction function and show that it is equivariant any time the expert policy that is being modeled is equivariant." — two sentences, zero citations [arxiv:2407.01812]
- TinyMPC Related Work-equivalent paragraph cites OSQP [31], ADMM [39, 40, 41], LQR [33] — multiple citations per sentence; Method paragraph "TinyMPC trades generality for speed by exploiting the special structure of the MPC problem. Specifically, we leverage the closed-form Riccati solution to the LQR problem to compute the primal update in (10)." — one citation (to the equation, not external work) [arxiv:2310.16985]
- AESOP related work paragraph on Out-of-Distribution Robustness has ~12 citations spread across 7 sentences; the corresponding Method subsection "Fast Anomaly Detection" has ~2 citations [arxiv:2407.08735]
- ANYmal Parkour Related Work cites refs [1]-[40] heavily; Materials and Methods reuses only [2], [3] in the Perception subsection [arxiv:2306.14874]

**Variants**: When a paper's contribution is heavily methodological-derivative (e.g., a small modification to an existing framework), Method-section citation density rises because every modification points to what it modifies. CoFRIDA [arxiv:2402.13442] is an example: "we build on FRIDA [1] which..." appears in nearly every Method paragraph.

**Why it works**: The two sections do different rhetorical work. Related Work is about positioning (high citation density signals thoroughness); Method is about description (high citation density would clutter the technical narrative and suggest derivative work). Reviewers calibrate to these densities — a Method section with too many citations reads as "this paper is just stitching others together"; a Related Work section with too few reads as "this paper hasn't done its homework".

---

### A9. Italicized or bolded paragraph-leads name the family in one phrase ("*Whole-body Control.*")
**Pattern**: Subsection titles in Related Work are increasingly inline rather than headings. The standard form is to start a paragraph with the family name in italic or bold followed by a period or em-dash, then immediately launch into the survey. This compresses what would otherwise be a level-3 section heading into the first phrase of the paragraph, saving vertical space.

**Evidence**:
- "**Whole-body Control** Whole body control (WBC) has been widely adopted to enhance robotic capabilities..." [arxiv:2505.20829]
- "**Hybrid Force and Position Control** In contact-rich manipulation tasks..." [arxiv:2505.20829]
- "**Imitation Learning for Mobile Manipulation** Imitation learning [38, 39, 40, 41, 42] has recently become..." [arxiv:2505.20829]
- "Diffusion Models Diffusion models [12] learn distributions by modeling the reverse of a diffusion process..." [arxiv:2407.01812]
- "Equivariance in manipulation policies Robots operate within a three-dimensional Euclidean space..." [arxiv:2407.01812]
- "Closed-loop Visuomotor control Closed-loop visuomotor policies are more robust and responsive..." [arxiv:2407.01812]
- "*Out-of-Distribution Robustness:* The fact that learning-based systems often behave unreliably..." [arxiv:2407.08735]
- "*Foundation Models in Robotics:* The integration of large language models (LLMs)..." [arxiv:2407.08735]
- "LLMs for robot planning and interaction. Large language models have shown a wide range of capabilities..." [arxiv:2307.01928]

**Variants**: Some venues prefer numbered or lettered subsections ("II.A Coverage-Based and Ergodic Search Methods") with their own headings; this is older IEEE-conference style and is rarer in CoRL/RSS. The inline-bold form is now dominant in ML-flavored venues. The colon form ("*Out-of-Distribution Robustness:*") with a colon rather than period is slightly more common in journal-style RSS submissions.

**Why it works**: Inline bold leads do three things: (1) act as a scannable index for skimming reviewers, (2) save 1–2 lines of vertical space vs full headings, (3) signal that the paragraph that follows is *the* paragraph for that family — no further subdivision needed. A reviewer can quickly find "is there a Diffusion Models discussion?" without reading the section headings.

---

### A10. Self-citation in Related Work uses "In our previous work, [X]," then describes prior work in the first person
**Pattern**: When the current paper extends the authors' own earlier work, the writer marks this with explicit first-person framing rather than treating the prior work as third-party. The standard form is "In our previous work [X], we explore..." or "Our prior work [X] proposes..." — first-person verbs throughout, with the citation as a parenthetical pointer. This is distinct from neutral citation: "Smith et al. [X] propose...".

**Evidence**:
- "In our previous work, MILD [5], [6], we explore learning a shared latent space model using a Variational Autoencoder (VAE) wherein we learn a joint distribution over the trajectories of both the human and the robot using an HMM with underlying Gaussian States to represent the multimodality of the demonstrations." [arxiv:2407.07636]
- "Rather than extracting key poses as in [7], we generate the robot's motion using Gaussian Mixture Regression (GMR) from the underlying HMM based on the human's observations in a reactive manner. In doing so, we achieve better accuracy than using a recurrent representation of the shared latent dynamics [2]." [arxiv:2407.07636]
- "Our work builds on [1] but focuses on equivariance in the diffusion process." [arxiv:2407.01812]
- "Our MPC controller is inspired by [8]." [arxiv:2304.00959]
- "In this work, we take inspiration from [3] to reconstruct the environment in 3D from point cloud data. We augment the method with a multi-resolution scheme to have a higher resolution near the robot and a lower resolution further away to have a larger view of the scene." [arxiv:2306.14874]

**Variants**: When the prior work is not the writer's but is a close intellectual antecedent ("our approach is inspired by..."), the same first-person framing is used. When the prior work is a competing method by a different group, the writer reverts to neutral third-person framing ("Chi et al. [1] proposed Diffusion Policy to...").

**Why it works**: First-person framing acknowledges the prior contribution without forcing the writer to position-against it. The reader interprets this as continuity — the same authors solving a deeper problem — rather than the writer competing with themselves.

---

### A11. "To the best of our knowledge, this is the first..." — the novelty stake-out sentence
**Pattern**: A high-impact rhetorical move at the END of a Related Work paragraph (or as the closer of the entire Related Work section) is the explicit first-claim: "To the best of our knowledge, we are the first to...", "We propose the first...", "This is the first application of...". Used carefully — usually once per paper, sometimes twice. The phrase is bounded ("to the best of our knowledge") to avoid challenge.

**Evidence**:
- "To the best of our knowledge, this is the first application of FM embeddings to the task of runtime monitoring, enabling safe and real-time control of an agile robotic system." [arxiv:2407.08735]
- "To the best of our knowledge, we employ CP for language-based planning." (in context: "To the best of our knowledge, this work is the first to employ CP for language-based planning.") [arxiv:2307.01928]
- "To the best of the authors' knowledge, TinyMPC is the first MPC solver tailored for execution on these MCUs that has been demonstrated onboard a highly dynamic, compute-limited robotic system." [arxiv:2310.16985]
- "To the best of our knowledge, we propose the first system that can perform agile navigation with a quadrupedal robot in such challenging scenarios without a priori planning or mapping." [arxiv:2306.14874]
- "in light of the aforementioned challenges and observations, we propose the first unified policy for legged robots that seamlessly integrates force and position control without the need for force sensors." [arxiv:2505.20829]
- "our paper studies symmetries in an SE(3) closed-loop action space, and is the first one to study the symmetries in diffusion policy." [arxiv:2407.01812]

**Variants**: When the claim is bolder, the writer omits the "best of our knowledge" hedge: "we propose the first..." (Unified Policy [arxiv:2505.20829]). When the claim is narrower (a specific intersection rather than an absolute first), the writer adds qualifiers: "we are the first to study X in the context of Y." Some papers use the phrase in the Intro instead of Related Work to position the claim earlier — Robots Ask for Help [arxiv:2307.01928] uses it in Related Work because Related Work comes after experiments.

**Why it works**: The novelty claim is the contract between paper and reviewer. The hedge ("to the best of our knowledge") makes it socially safe for the reviewer to either agree or counter-cite without seeming antagonistic. The placement at the end of a positioning paragraph capitalizes on the paragraph's just-built contrast with the family.

---

## B. Method / Approach section patterns

### B1. Method-section opener: "[System name] [does what]. [Specifically/In particular], [how]."
**Pattern**: The first sentence of the Method section nearly always names the system, states the high-level mechanism in one clause, and is followed by a "Specifically" or "In particular" sentence that previews the technical move. This two-sentence opener does the same work the abstract does — it re-anchors the reader who skipped the intro.

**Evidence**:
- "TinyMPC trades generality for speed by exploiting the special structure of the MPC problem. Specifically, we leverage the closed-form Riccati solution to the LQR problem to compute the primal update in (10)." [arxiv:2310.16985]
- "Our approach, CoFRIDA shown in Fig. 3, is made up of three primary components: (1) The Co-Painting Module, ... (2) FRIDA [1], a robotic painting system for planning actions from given images, and (3) a self-supervised method for creating training data using FRIDA to fine-tune pre-trained models in the Co-Painting Module." [arxiv:2402.13442]
- "We introduce the Open X-Embodiment Repository (robotics-transformer-x.github.io) – an open-source repository which includes large-scale data along with pre-trained model checkpoints for X-embodied robot learning research." [arxiv:2310.08864]

**Variants**: A common variant pre-states the *contribution* before the system: "In this section we present...", "We propose...", "Our method, X, is...". When the paper has a Preliminaries section preceding Method, this two-sentence opener may be preceded by a single "We now describe..." transition.

**Why it works**: The first sentence of any section is the most-read sentence of that section. A reviewer who has scrolled past the intro re-enters via this sentence and must immediately understand both the *name* of what is being proposed and the *technical commitment* the rest of the section will deliver. The "Specifically" sentence converts an opaque headline into a verifiable claim.

---

### B2. Method section uses subsections in a fixed canonical order: Overview → Components → Training → Inference
**Pattern**: The internal structure of the Method section follows a near-universal four-stage order. (1) Overview / Architecture: one paragraph + a figure reference, summarizing the pipeline. (2) Component-by-component description: each subsection presents one block of the diagram. (3) Training procedure: loss, data, hyperparameters. (4) Inference / Deployment: how the trained system is run at test time. Some papers swap (3) and (4) or fold them together, but the Overview-first / Inference-last shape is rarely violated.

**Evidence**:
- TinyMPC method section: "III. THE TINYMPC SOLVER" opens with overview paragraph, then "A. Combining LQR and ADMM for MPC", "B. Pre-Computation", "C. Penalty Scaling" — each a component. [arxiv:2310.16985]
- CoFRIDA Method: opens with three-component overview (Sec III paragraph 1), then "A. Self-Supervised Data Creation", "B. Co-Painting Module", "C. FRIDA" — covering data, the trained module, and the inference-time system. [arxiv:2402.13442]
- Open X-Embodiment "III. THE OPEN X-EMBODIMENT REPOSITORY" opens with an "We introduce..." sentence and a bullet list of resources, then has "A. The Open X-Embodiment Dataset" and "B. Dataset Analysis" before the modelling section "IV. RT-X DESIGN" with its own "A. Data format consolidation", "B. Policy architectures", "C. Training and inference details" subsections. [arxiv:2310.08864]

**Variants**: When the contribution is primarily a *solver* or *algorithm*, the Training stage may be absent and Components stage instead presents derivations + an Algorithm box (TinyMPC follows this shape). When the contribution is primarily *data*, the Components stage is replaced by Dataset Analysis (Open X-Embodiment).

**Why it works**: Reviewers know this canonical shape and skim with it. A reviewer who can't find the Training subsection assumes the paper is sloppy, even if the same content is buried elsewhere. Adhering to the shape lowers cognitive load and signals competence.

---

### B3. Architecture figure is referenced in the FIRST paragraph of Method
**Pattern**: The figure that depicts the system architecture (typically Figure 2 or 3) is referenced in the opening paragraph of the Method section, usually in the form "Our approach, X, shown in Fig. Y, ...", "as illustrated in Fig. Y", or "(see Fig. Y)". This pairing creates a text-figure index where the reader knows from sentence one which diagram to look at.

**Evidence**:
- "Our approach, CoFRIDA shown in Fig. 3, is made up of three primary components..." [arxiv:2402.13442]
- "We briefly summarize the design of these models in this section, and discuss how we adapted them to the X-embodiment setting in our experiments." — followed by Fig. 3 caption: "RT-1-X and RT-2-X both take images and a text instruction as input and output discretized end-effector actions." [arxiv:2310.08864]
- "RT-1 [8] is a 35M parameter network built on a Transformer architecture [118] and designed for robotic control, as shown in Fig. 3." [arxiv:2310.08864]

**Variants**: When the architecture is non-trivial, the first paragraph may instead promise the figure ("see Fig. 2"), allowing more prose detail before the diagram. When the paper has multiple architecture diagrams (e.g., one for the data flow, one for the model), each is referenced at the start of its respective subsection.

**Why it works**: Reviewers read figures before prose. Anchoring Fig. Y in the first sentence ensures the reader is examining the right diagram by the time the prose dives into components. Failing to reference the figure leaves the reader either skipping the figure or losing the prose.

---

### B4. Notation introduced in a single dedicated paragraph or via Preliminaries
**Pattern**: When a paper requires non-trivial mathematical notation, that notation is introduced in a single block — either a Preliminaries / Background section before the Method, or in the first Method subsection. New symbols are bolded or italicized on first introduction; types are stated explicitly (e.g., "x ∈ R^n"); and the introduction sentence uses the verb "let" or "denote": "Let x_k ∈ R^n be the state at time k."

**Evidence**:
- "where x_k ∈ R^n, u_k ∈ R^m are the state and control input at time step k, N is the number of time steps (also referred to as the horizon), A ∈ R^{n×n} and B ∈ R^{n×m} define the system dynamics, Q ⪰ 0, R ≻ 0, and Q_f ⪰ 0 are symmetric cost matrices and q and r are linear cost vectors." [arxiv:2310.16985]
- "(1) N stands for the number of the patches of the patchified version of the input image, (2) {k_i}_{i=1,...,N} ⊆ R^{d_QK} is the set of their latent embeddings (keys), (3) q_i ∈ R^{d_QK} is the embedding of the target image..., (4) K : R^{d_QK} × R^{d_QK} → R is the kernel function..." [arxiv:2312.01990]

**Why it works**: Notation density is the single biggest barrier to reviewer comprehension. Concentrating it in one block lets the reader either skim past it (if they trust the formalism) or read it carefully once (if they need it), without having to re-discover what each symbol means three pages later.

---

### B5. Equations are framed with a one-clause prose lead and a one-sentence interpretation
**Pattern**: Equations are not dropped raw into the prose. The canonical shape is a three-part sandwich: (1) prose lead naming what the equation will express, ending with a colon; (2) the equation itself, on its own line, numbered; (3) one or two sentences of *interpretation*, telling the reader what to take from the equation. The lead and interpretation together make the equation a *claim* rather than a definition.

**Evidence**:
- "LQR optimizes a quadratic cost function subject to a set of linear dynamics constraints: ... [equation (1)] ... where x_k ∈ R^n, u_k ∈ R^m are the state and control input at time step k..." — lead + equation + symbol interpretation [arxiv:2310.16985]
- "Equation (1) has a closed-form solution in the form of an affine feedback controller: u*_k = -K_k x_k - d_k. The feedback gain K_k and feedforward d_k are found by solving the discrete Riccati equation backward in time..." — lead + equation + procedural interpretation [arxiv:2310.16985]
- "The augmented Lagrangian of the transformed problem (8) is as follows, where λ is a Lagrange multiplier and ρ is a scalar penalty weight: [equation (9)]. If we alternate minimization over x and z, rather than simultaneously minimizing over both, we arrive at the three-step ADMM iteration, ..." — lead + equation + verbal explanation of consequence [arxiv:2310.16985]
- "Variational Autoencoders (VAEs) [24], [25] are a class of neural networks that learn to reconstruct inputs via latent representations in an unsupervised, probabilistic way. ... The goal is to estimate the true posterior p(z|x) using a neural network q(z|x), which is trained by minimizing the Kullback-Leibler (KL) divergence between them [equation (1)] which can be re-written as [equation (2)]." [arxiv:2407.07636]
- "To achieve this goal, we adopt the impedance control formulation: F = K(x − x_des) + D(ẋ − ẋ_des) + M(ẍ − ẍ_des), (1) where x denotes the actual position of the robot. x_des, ẋ_des, and ẍ_des denotes the desired goal position, velocity, and acceleration of the robot." [arxiv:2505.20829]
- "Specifically, CP uses a held-out calibration set of example plans in different scenarios to generate a reduced prediction set of plans among {y_i} (Fig. 2). ... CP first uses the LLM's confidence f̂ (cf. Section 2) to evaluate the set of nonconformity scores {κ_i = 1 − f̂(x̃_i)y_i}^N_{i=1} over the calibration set — the higher the score is, the less each data in the calibration set conforms to the data used for training f̂." — equation embedded in prose, plain-language interpretation in same sentence [arxiv:2307.01928]

**Variants**: For complex multi-line equations (e.g., MPC optimization problems with several constraints), the writer may omit the interpretive sentence and instead use a *named-display* shape: write "Time-Optimal Ergodic Trajectory Optimization:" as a label above the equation, then the full optimization problem (objective + s.t. constraints) [arxiv:2305.11643]. The label *replaces* the prose lead in this case. The interpretation is then deferred to the next paragraph.

**Why it works**: Equations are dense. Without a prose lead, the reader sees the equation before understanding what claim it makes. Without an interpretive follow-up, the reader is left to derive the takeaway. The sandwich shape ensures every equation contributes to the paper's argument, not just its formalism.

---

### B6. The "we" voice is canonical in the Method section, even for derivations
**Pattern**: The Method section is written in the active first-person plural — "we use", "we adopt", "we train", "we derive", "we observe" — even when describing derivations or standard procedures. This is in contrast to the Preliminaries / Background section (where passive or third-person voice dominates: "LQR is a widely used approach") and to the Related Work section (where the third-person "X et al. propose" dominates). The first-person "we" in Method signals authorial decisions and design choices.

**Evidence**:
- "We solve the following problem, introducing slack variables as in (9)..." [arxiv:2310.16985]
- "We observe that, because (14) exhibits the same LQR problem structure as in (1), it can be solved efficiently with the Riccati recursion in (3)." [arxiv:2310.16985]
- "We propose 'MoVEInt', a novel framework that employs a Mixture of Variational Experts for learning Human-Robot Interactions from demonstrations through a shared latent representation of a human and a robot." [arxiv:2407.07636]
- "We aim to learn a policy for reactively generating the robot's latent trajectory based on human observations p(z^r_t|x^h_t). We do so in a Behavior Cloning Paradigm by maximizing the probability..." [arxiv:2407.07636]
- "We begin by introducing the general problem formulation of our approach." [arxiv:2505.20829]
- "We detail the learning of the proposed unified force-position control policy by first defining the space of observations, commands, and actions." [arxiv:2505.20829]
- "We follow [12] in using a VLM to convert the robot's current visual observation into a text description of the environment." [arxiv:2407.08735]
- "We first analyze the noise prediction function and show that it is equivariant any time the expert policy that is being modeled is equivariant." [arxiv:2407.01812]
- "We first begin by defining the continuous-time dynamics ẋ = f(x, u) as a discrete-time system over a sequence of N discretized 'knot' points..." [arxiv:2305.11643]

**Variants**: When a derivation step is general (not authorial), passive voice creeps in: "Equation (1) has a closed-form solution..." [arxiv:2310.16985]; "The KL divergence is always non-negative..." [arxiv:2407.07636]. The rule of thumb: use "we" when describing a *choice*; use passive when describing a *fact*.

**Why it works**: The "we" voice claims responsibility for each design choice. Reviewers reading "we adopt the impedance control formulation" know this is a decision the authors made and can be questioned; reviewers reading "the impedance control formulation is adopted" don't know whose decision it was, which makes evaluation harder.

---

### B7. The "Algorithm 1" box appears once per Method section and contains pseudocode at one consistent abstraction level
**Pattern**: Solver/policy papers include exactly one Algorithm box (sometimes two), titled "Algorithm 1: [name of procedure]". The pseudocode mixes high-level steps with mathematical operations, references back to numbered equations rather than re-derivating, and uses a consistent abstraction granularity throughout. Functions are named in small-caps or boldface. The box is referenced in the prose at the point where it summarizes ("The resulting [X] algorithm is summarized in Algorithm 1.").

**Evidence**:
- TinyMPC Algorithm 1 — function `TINY_SOLVE(input)` with: while not converged do, //Primal update, p_{1:N-1}, d_{1:N-1} ← Backward pass via (20), x_{1:N}, u_{1:N-1} ← Forward pass via (2), //Slack update, z_{1:N}, w_{1:N-1} ← Project to feasible set (17), //Dual update, y_{1:N}, g_{1:N-1} ← Gradient ascent (18). Each step references a prior equation; comment lines (//) label the three ADMM stages. [arxiv:2310.16985]
- MoVEInt "Algorithm 1: Learning a Reactive Latent Policy for Human-Robot Interaction" — Data, Result, while not converged loop with nested "for x^h_{1:T}, x^r_{1:T} ∈ X" loop and four prose-style steps (Compute the MDN policy p(z^r_t|x^h_t) (Eq. 6), Compute the robot VAE posterior..., Reconstruct samples..., Minimize the loss in Eq. 9). [arxiv:2407.07636]
- AESOP "Algorithm 1: AESOP" — Input section (State x_0..., fast anomaly detector h, slow reasoner w with latency ≤ K), numbered procedure with 23 lines including if/else branches, calls to procedures (`w.start()`, `h(o_t)`), and references to equation (3). [arxiv:2407.08735]

**Variants**: When the method is primarily a *training procedure* (rather than a runtime algorithm), some papers present it as "Training procedure" prose with subheadings rather than a boxed algorithm. When the method is split into a *training* algorithm and a *deployment* algorithm, papers may include two boxes labeled "Algorithm 1: Training" and "Algorithm 2: Inference" — Equivariant Diffusion Policy [arxiv:2407.01812] embeds the noise-prediction/denoising procedure into Eq. (1) and prose rather than using a box.

**Why it works**: Algorithm boxes give a single ground-truth representation that reviewers and implementers can both refer to. The eqn-reference pattern keeps the box compact; the prose-style steps make it human-readable; the comment markers make the conceptual blocks visible. The result is a Rosetta stone between formalism (equations) and code (forthcoming implementation).

---

### B8. The "training procedure" subsection has a fixed information template: loss, optimizer, data, hyperparameters
**Pattern**: Whether named "Training", "Policy Learning", "Implementation Details", or "Optimization" — the subsection covering how the model is trained follows a near-fixed information template: (1) the loss function, often called out as a numbered equation; (2) the optimizer or training algorithm choice (PPO, Adam, BGS); (3) the training data: source, size, preprocessing; (4) hyperparameters: learning rate, batch size, training steps, network sizes; (5) hardware/duration if relevant. Items appear in roughly this order, sometimes condensed or omitted.

**Evidence**:
- MoVEInt "B. Implementation Details" — Downsampling/data spec → time window for input → architecture: VAE with 2 hidden layers each in the encoder and decoder with a dimensionality of (40, 20) and (20, 40) respectively, with Leaky ReLU activations and a 5D latent space → loss notes → initialization scheme [arxiv:2407.07636]
- Unified Policy "Policy Learning" — "We adopt a two-stage training procedure: first focusing on whole-body reaching and locomotion, then introducing random force commands and external disturbances. This staged approach empirically yields more stable training... Policy learning is supervised by rewarding accurate tracking of the target end-effector position... Additionally, an MSE loss is used to improve the accuracy of the state estimator..." — training stages, supervision signals, losses [arxiv:2505.20829]
- TinyMPC IV "Experiments" hints at training-equivalent (here, problem-instance setup): "Experiments were performed on a Teensy 4.1 [43] development board, which has an ARM Cortex-M7 microcontroller operating at 600 MHz, 7.75 MB of flash memory, and 512 kB of RAM... Objective tolerances were set to 10^{-3} and constraint tolerances to 10^{-4}. The maximum number of iterations for both solvers was set to 4000..." — hyperparameter recipe in compact form [arxiv:2310.16985]
- SARA-RT "1) The setting" — Object set, observation space components (cloud, center, major axis), action representation, optimizer choice ("PCT policy training is conducted in the simulator (Fig. 3) via blackbox optimization ([32], [33], [34], [35]). The BGS variant ([34]) with l = 50 perturbation-directions, Gaussian smoothing parameter σ = 0.02, step size η = 0.02, τ = 30% top directions is applied."), training data scale ("an agent sees only k = 5 different objects"). [arxiv:2312.01990]
- Open X-Embodiment "C. Training and inference details" — fixed template instantiated to a large model: data format, optimizer, learning rate, training duration [arxiv:2310.08864]

**Variants**: Some venues require all hyperparameters in the main text (RSS, Science Robotics); others (CoRL, NeurIPS) allow them to be deferred to an Appendix. The phrase "See Appendix X for full hyperparameters" is a deferral-marker (B11).

**Why it works**: Reproducibility is a major review criterion. Reviewers know to scan for the canonical five items; their absence is a red flag for non-reproducibility. The fixed order means a reviewer can scan a paper in under a minute and check the boxes.

---

### B9. The "we use X for Y" template — terse architectural commitments
**Pattern**: When the writer commits to a specific component without deriving why, the canonical form is "We use X for Y" or "We adopt X as the Z". This is the workhorse sentence of any Method section — it makes a design choice cheap to state, links to a citation, and moves on. Repeated three or four times in a single Method paragraph, these sentences form the "ingredient list" of the system.

**Evidence**:
- "We use Nuitrack [40] for tracking the upper body skeleton joints in each frame at 30Hz." [arxiv:2407.07636]
- "For the dataset from [2] and the NuiSI dataset [6], we use a VAE with 2 hidden layers each in the encoder and decoder with a dimensionality of (40, 20) and (20, 40) respectively, with Leaky ReLU activations and a 5D latent space." [arxiv:2407.07636]
- "For the mixture coefficients α_i, to enable a recurrent nature of the predictions, the output of the MDN encoder is passed to a single-layer Gated Recurrent Unit (GRU) whose outputs are then passed through a linear layer followed by a softmax layer." [arxiv:2407.07636]
- "We implement this optimization problem in ACADO [29] and use the qpOASES solver [30]." [arxiv:2304.00959]
- "We compute the discrete-time version of it by using a Runge-Kutta method of 4th order with time step dt..." [arxiv:2304.00959]
- "TinyMPC is implemented in C++ using the Eigen matrix library [44]." [arxiv:2310.16985]
- "We implement our network using the escnn library [50]." [arxiv:2407.01812]
- "We use PaLM-2L [13] as the LLM in all examples unless otherwise noted." [arxiv:2307.01928]
- "We follow [12] in using a VLM to convert the robot's current visual observation into a text description of the environment." [arxiv:2407.08735]
- "We inherit the embeddings from the pre-trained CLIP model [7] with the ViT-B vision backend." [arxiv:2312.01990]

**Variants**: The same template appears in past tense ("we used X") in retrospective passages, or in passive voice ("X is used for Y") in older IEEE-conference papers. The clipped version omits "for Y" when it's obvious: "We use the qpOASES solver [30]." [arxiv:2304.00959]. The justification-attached version ("We use X because...") is rarer — typically reserved for choices the writer anticipates a reviewer will question.

**Why it works**: Each "we use X" sentence is one row of a design specification. The reader can scan them like a bill of materials. Citations turn each commitment into a verifiable link. The Method section becomes auditable: any reviewer can challenge any "we use" sentence by checking the citation.

---

### B10. The "intuition" sentence — informal explanation alongside formal statement
**Pattern**: Top-venue papers consistently pair formal mathematical claims with informal *intuitions*. The intuition is a sentence (sometimes set off as "Intuitively, ..." or "In effect, ..." or "This means that ...") that translates the formal claim into plain language about what is happening or why it works. Intuitions are most common around: (a) loss functions, explaining what each term encourages; (b) constraints, explaining the qualitative behavior; (c) theorems, explaining the practical takeaway.

**Evidence**:
- "Intuitively, this approach measures whether anything similar to the current observation has been seen before." [arxiv:2407.08735]
- "If we infer ε for all actions in the action space, we effectively acquire a gradient field towards the expert trajectory. The figure shows that such a gradient field is equivariant when the expert policy is equivariant, thus the function ε is also equivariant." [arxiv:2407.01812]
- "We observe that, because (14) exhibits the same LQR problem structure as in (1), it can be solved efficiently with the Riccati recursion in (3)." — verbal observation framing a formal result [arxiv:2310.16985]
- "A careful analysis of the Riccati equation then reveals that only the linear terms need to be updated as part of the ADMM iteration..." [arxiv:2310.16985]
- "The emergent behavior of Algorithm 1 is that once the fast anomaly detector issues a warning regarding an unusual observation, the robot will balance progress along the nominal trajectory and jointly maintaining dynamic feasibility of the fallback options available at t_anom. This generally leads the robot to slow down to preserve its options, thereby providing the slow reasoner with time to think." [arxiv:2407.08735]
- "In effect, retrieves the most similar prior experience from D_e to construct the score." [arxiv:2407.08735]
- "This sampling strategy exposes the policy to a variety of control conditions, echoing the different desired control behavior discussed in Section 3.1 and enabling a single policy to adapt to varying control task demands." [arxiv:2505.20829]
- "Our separation loss can be written as ... [equation] ... The first term... [interpretation]. The second term... [interpretation]. The third term... [interpretation]." [arxiv:2407.07636]

**Variants**: When the intuition is non-trivial enough to merit its own paragraph, the writer might lead with "Conceptually, ..." or "At a high level, ...". When the intuition is in a footnote, it's because the writer judged it too distracting for the main flow but too important to omit (the famous "tortoise and hare" footnote in AESOP [arxiv:2407.08735]).

**Why it works**: Math expresses *what*; intuition expresses *why and how*. Reviewers read both: math for correctness, intuition for whether the design makes sense. A paper with only math is hard to evaluate; a paper with only intuition is unconvincing; a paper with both lets the reviewer triangulate.

---

### B11. The Method section "relegates to Appendix" pattern — naming what is deferred
**Pattern**: Modern Method sections frequently use sentences like "See Appendix X for details", "Full details are provided in Section Y", "We defer the proof to Appendix Z". This is not lazy writing — it's a deliberate compression. The author shows that they have done the work but spares the reader the depth. The relegation marker appears at the end of a derivation, after a notation block, or at the end of a hyperparameter listing.

**Evidence**:
- "See Appendix A for the proof." [arxiv:2407.01812]
- "See Appendix B for details." [arxiv:2407.01812]
- "See Appendix D for details." [arxiv:2407.01812]
- "See Appendix C." [arxiv:2407.01812]
- "We provide the full reward specifications in Table A.1." [arxiv:2505.20829]
- "Details of the teleoperation pipeline and training procedures are provided in Section B and Section D." [arxiv:2505.20829]
- "We refer to Appendix B for a brief introduction to anomaly detection used hereafter." [arxiv:2407.08735]
- "We investigate several simple score functions (see Appendix D3 for a full list)..." [arxiv:2407.08735]
- "The proofs are deferred to Section A2." [arxiv:2307.01928]
- "We extend our method and confidence guarantees to this setting for both single- and multi-step problems in Section A3 and Section A4." [arxiv:2307.01928]
- "Supplementary sections S1 and S2 define the observations, actions, and rewards of the locomotion and navigation policies and provide further implementation details." [arxiv:2306.14874]
- "We refer readers to [42] for more details." [arxiv:2310.16985]
- "Further information can be found in [24]–[26]." [arxiv:2407.07636]

**Variants**: Three kinds of deferral: (a) **proofs deferred to appendix** — most common, used for theorems; (b) **details deferred to appendix** — used for hyperparameters, ablations; (c) **standard derivations deferred to canonical reference** — used for textbook material, with citations like "We refer readers to [42] for more details." Each kind has a distinct social meaning: (a) shows the proof exists, (b) shows the work is reproducible, (c) shows the writer is not reinventing wheels.

**Why it works**: The main-paper Method section is a story; the appendix is a reference manual. Reviewers and readers serve themselves from the level of detail they want. The marker sentence is the menu — it tells the reader where to find each kind of detail without forcing them through it.

---

### B12. The Method section opens with a "subsection roadmap" sentence when there are 3+ subsections
**Pattern**: When the Method section has three or more subsections, the opening paragraph almost always includes a roadmap sentence: "We first ..., then ..., and finally ...", "We motivate X in Sec. A by ..., explain Y (Sec. B), and show Z (Sec. C)", "The remainder of this section is organized as follows: ...". This sentence acts as a table of contents within the section.

**Evidence**:
- "We motivate the use of MDNs in Sec. III-A by showing the equivalence of MDNs with Gaussian Mixture Regression (GMR) for HRI. We then explain learning the robot motion embeddings (Sec. III-B), and then show how to train reactive policies for HRI (Sec. III-C). We denote the human variables in red with the superscript h and the robot variables in blue with the superscript r." [arxiv:2407.07636]
- "Solutions to the problem are presented in two manners: 1) analytically through conditions of optimality; and 2) numerically through a direct transcription approach. The analytical approach is used to establish conditions of optimality (which can be seen as continuous time analogies of the KKT-conditions). ... The numerical approach provides a direct form of calculating robot trajectories and control solutions for the time-optimal ergodic search problem." [arxiv:2305.11643]
- "The paper is structured as follows: Section II overviews related work. Section III describes preliminary information on ergodic search and time-optimal control. Section IV poses the time-optimal ergodic search problem and presents solutions to the problem. Section V then presents various simulated and experimental results for the proposed solution to generate time-optimal ergodic search trajectories. Last, Section VI provides conclusions and an outlook on future work." [arxiv:2305.11643]
- "We first present our FM-based monitoring approach, after which we construct a planning algorithm that accounts for the latency that FM-based reasoning may induce." [arxiv:2407.08735]
- "Organization: We first discuss related work in §II and formalize the problem setup in §III. Then, we present our approach in §IV and evaluate our method in §V." [arxiv:2407.08735]
- "This paper proceeds as follows: Section II reviews linear-quadratic optimal control, convex optimization, and ADMM. Section III then derives the core TinyMPC solver algorithm. Benchmarking results and hardware experiments on a Crazyflie quadrotor are presented in Section IV." [arxiv:2310.16985]

**Variants**: The roadmap may appear at the END of the Introduction (especially in ICRA/IROS papers) or at the START of the Method (especially in CoRL papers). Some papers do both. When subsections are fewer than three, the roadmap is usually omitted as overkill.

**Why it works**: Reviewers don't read linearly. They jump. A roadmap sentence tells the jumping reviewer "if you want X, go here; if you want Y, go there". It also signals competence: a writer who has thought about the section's structure usually has thought about the technical content.

---

### B13. The "system-as-three-or-four-components" diagram convention
**Pattern**: Almost every paper depicts its method as a three-to-four-block diagram in its key figure (Figure 2 or 3), with bidirectional arrows or input/output flow between blocks. The Method-section text mirrors this: each block becomes a subsection. This text-diagram parallelism is not accidental; it is enforced.

**Evidence**:
- CoFRIDA Fig. 3: "three primary components: (1) The Co-Painting Module, ... (2) FRIDA, ... (3) a self-supervised method..." — Method has subsections A. Self-Supervised Data Creation, B. Co-Painting Module, C. FRIDA. [arxiv:2402.13442]
- ANYmal Parkour Fig. 2: "perception module ... locomotion module ... navigation module" — three blocks, three subsections "1) Perception Module ... 2) Locomotion Module ... 3) Navigation Module". [arxiv:2306.14874]
- Unified Policy Fig. 2: "(a) Architecture of the unified position-force policy ... (b) Force-aware imitation learning ... (c) Illustration of position and velocity compensation ... (d) Visualization of sampled force commands" — Method has 3.1 A Unified Formulation, 3.2 Learning a Unified Force-Position Control Policy, 3.3 Force-aware Imitation Learning. [arxiv:2505.20829]
- AESOP Fig. 1 (referenced): "splits the monitoring task into two separate stages: The first is rapid, real-time detection of anomalies ... The second stage is slower, methodical generative reasoning..." — Method "A. Runtime Monitor: Fast and Slow Reasoning" splits accordingly, then "B. Planning a Tree of Recovery Trajectories". [arxiv:2407.08735]
- MoVEInt Fig. 2: "MDN policy ... Robot VAE ... reactive policy" — Method has III-A GMR-based Interaction Dynamics with MDNs, III-B Robot Motion Embeddings, III-C Reactive Motion Generation. [arxiv:2407.07636]

**Variants**: When the method has more than four components, the diagram may collapse details into nested boxes (Open X-Embodiment Fig. 3 nests within a larger pipeline). When the method has two components, the diagram may simply be a left-right split. Most papers stay at three to four because that's the count human visual attention can hold.

**Why it works**: Reviewers and readers form a mental model of the method from the figure first, the section structure second, and the prose third. When all three reinforce the same N-block decomposition, comprehension is fast. When they diverge (figure says 3 blocks, text describes 5 components), the reviewer doubts whether the writer understands their own method.

---

## C. Preliminaries / Problem Formulation patterns

### C1. Preliminaries / Background section is a textbook tutorial of the building blocks
**Pattern**: When present, the Preliminaries (or Background) section presents 2–4 well-established techniques the paper builds on, each in its own subsection. The writing style is *textbook-pedagogical*: definitions, the standard formulation as equations, and citations to the canonical references. The writer's voice disappears — the section reads as if quoted from a course.

**Evidence**:
- TinyMPC "II. BACKGROUND" with subsections "A. The Linear-Quadratic Regulator", "B. Convex Model-Predictive Control", "C. The Alternating Direction Method of Multipliers" — each presenting the standard formulation with equations, no novel contribution. Opens with: "The linear-quadratic regulator (LQR) [33] is a widely used approach for solving robotic control problems. LQR optimizes a quadratic cost function subject to a set of linear dynamics constraints:" [arxiv:2310.16985]

**Why it works**: The Preliminaries section serves three audiences simultaneously: (a) the reviewer who doesn't know the building blocks needs a refresher; (b) the reviewer who does know them needs the *notation conventions* the paper will use; (c) the reviewer who skips this section needs to know it's there so they can verify the paper isn't reinventing wheels. The textbook voice signals "I am not claiming novelty here; please use this as a reference for what follows."

---

### C2. Preliminaries section appears IFF the paper fuses 2+ established techniques; absent when the contribution is a single new mechanism
**Pattern**: Whether a paper has a Preliminaries / Background section depends on a measurable rule of thumb: if the method *fuses two or more pre-existing techniques* (e.g., ADMM + LQR, VAE + MDN, ergodic search + time-optimal control), the paper has a Preliminaries section that introduces each technique in its own subsection. If the contribution is a *single new mechanism* — a novel architecture, a novel loss, a novel constraint — the paper skips Preliminaries and dives straight into Method.

**Evidence**:
- TinyMPC fuses three techniques (LQR + Convex MPC + ADMM) and has a three-subsection Background: "II. BACKGROUND" with "A. The Linear-Quadratic Regulator", "B. Convex Model-Predictive Control", "C. The Alternating Direction Method of Multipliers". [arxiv:2310.16985]
- MoVEInt fuses VAEs and Mixture Density Networks and has "II. FOUNDATIONS" with "A. Variational Autoencoders" and "B. Mixture Density Networks". [arxiv:2407.07636]
- Time-Optimal Ergodic Search fuses ergodic search and time-optimal control and has "III. PRELIMINARIES" with "A. Ergodic Search" and "B. Time-Optimal Control Problem Statement" — each presenting the standard formulation. [arxiv:2305.11643]
- Equivariant Diffusion Policy fuses Equivariance + Diffusion Policy and has "3 Background" with "Problem Statement", "Diffusion Policy", "Equivariance" — three sub-paragraphs for the three pillars. [arxiv:2407.01812]
- KNOWNO fuses LLM planning + Conformal Prediction and has "3.1 Background: Conformal Prediction" as its own section under "3 Calibrating LLM Confidence". [arxiv:2307.01928]
- AESOP fuses LLM monitors + MPC and has "III. PROBLEM FORMULATION" plus an Appendix B "brief introduction to anomaly detection" — the in-paper formulation handles the MPC side, the appendix handles the anomaly-detection side. [arxiv:2407.08735]
- *Counterexample*: Unified Policy [arxiv:2505.20829] proposes a single mechanism (a single RL policy that handles force + position) and skips Preliminaries — Method starts with "3.1 A Unified Formulation" directly. ANYmal Parkour [arxiv:2306.14874] is a multi-module system but is presented as a single learned approach, so Materials and Methods opens with "A. Overview" rather than a separate preliminaries.

**Variants**: Some papers use the title "Foundations" (MoVEInt [arxiv:2407.07636]) or "Background" (TinyMPC [arxiv:2310.16985]) instead of "Preliminaries"; the function is the same. When the building blocks are widely known, the section is brief (3 paragraphs); when they are more specialized, it can run a full page. The section may also be embedded as an unnumbered "Background" subsection at the start of the Method (Equivariant Diffusion Policy [arxiv:2407.01812], KNOWNO [arxiv:2307.01928]) rather than as a top-level numbered section.

**Why it works**: The Preliminaries section is a *contract* with the reviewer: "you may not be familiar with all the building blocks I'm fusing; here's a refresher of each so we share vocabulary before I show how I combine them." When the contribution is a single mechanism, no such contract is needed — the reviewer can pick up the vocabulary inline. Mis-deciding (writing a Preliminaries section for a single-mechanism paper) wastes space; the opposite (omitting it when fusing two techniques) leaves reviewers struggling to parse the Method.

---

### C3. Problem Formulation subsection states the inputs, outputs, assumptions, and goal in exactly four short paragraphs
**Pattern**: When a paper has a "Problem Formulation" (or "Problem Statement") subsection — distinct from Preliminaries — its structure is near-canonical: (1) one paragraph defining the input variables and their domains (state, observation, etc.); (2) one paragraph defining the output (action, policy, plan); (3) one paragraph stating the assumptions (what is given, what is unknown); (4) one paragraph stating the goal as an optimization problem or as natural-language objective. The total length is rarely more than half a column.

**Evidence**:
- AESOP "III. PROBLEM FORMULATION" — paragraph 1 defines state and dynamics ("In this work, we consider a robot with discrete time dynamics x_{t+1} = f(x_t, u_t), where x_t ∈ R^n represents the robot's state, and u_t ∈ R^m is the control input."); paragraph 2 introduces observations and semantic failures; paragraph 3 introduces the nominal dataset assumption D_nom = {o_i}^N_{i=1}; paragraph 4 defines the goal: select intervention strategies. [arxiv:2407.08735]
- Time-Optimal Ergodic Search "IV-A Problem Formulation" — paragraph 1: define robot state and control (x(t), u(t)) and bounded exploration space W; paragraph 2: state the goal (optimize search time t_f while minimizing ergodic metric); paragraph 3: notes ill-posedness and introduces the ergodic inequality constraint; paragraph 4: writes out the full optimization problem (8). [arxiv:2305.11643]
- Equivariant Diffusion Policy "Problem Statement" — one compact paragraph: "We study policy learning using behavior cloning. The agent is required to learn a mapping from the observation o to the action a that mimics an expert policy. Both o and a can contain a number of time steps..." — packs all four elements (inputs, outputs, assumptions, goal) into ~10 sentences. [arxiv:2407.01812]
- Unified Policy "3.1 A Unified Formulation for Force and Position Control" — paragraph 1: "We begin by introducing the general problem formulation of our approach. As shown in the upper part in Fig. 2(c), given the position command relative to the robot body frame and force command, x^cmd and F^cmd, our goal is to learn a RL policy that ensures the robot's behavior adheres to these commands under net force F." — input variables; paragraph 2 introduces the impedance control formulation; paragraph 3 specifies end-effector simplification; paragraph 4 multi-contact extension. [arxiv:2505.20829]
- KNOWNO "2 Overview: Robots that Ask for Help" — explicitly partitioned by subhead: "Language-based planners." → "Planning as multiple-choice Q&A." → "Robots that ask for help." → "Goal: uncertainty alignment." [arxiv:2307.01928]

**Variants**: When the paper has both a Preliminaries and a Problem Formulation, the Preliminaries handles the textbook material and the Problem Formulation handles the paper-specific instantiation. When only one is present, it absorbs both functions. The variable-domain shorthand ("x ∈ R^n", "u ∈ U ⊆ R^m") is canonical and appears in nearly every Problem Formulation.

**Why it works**: The Problem Formulation is the *interface* between the writer's vocabulary and the reviewer's mental model. If the writer says "policy", what is its type? If the writer says "observation", what does it contain? The four-paragraph template ensures these questions are all answered before the technical Method begins. A Method section preceded by a clean Problem Formulation reads cleanly; one without it reads tangled.

---

### C4. Assumptions are stated explicitly with "We assume" or "We do not assume", typically once per assumption
**Pattern**: Top-venue papers make their assumptions explicit. The canonical form is "We assume X", "We do not assume X", "Note that X is given / known / observable". The list of assumptions usually appears in the Problem Formulation paragraph 3 (per C3), but individual assumptions may also be flagged inline when introduced. Assumptions that are unusual or that other reviewers might miss are bolded or set off in their own sentence.

**Evidence**:
- "Importantly, we do not assume knowledge of D, except that we can sample a finite-size dataset of i.i.d. scenarios from it." [arxiv:2307.01928]
- "For experiments here, we assume that the human faithfully provides help." [arxiv:2307.01928]
- "Further, we assume that we have access to a dataset D_nom = {o_i}^N_{i=1} of nominal observations wherein the robot was safe and reliable." [arxiv:2407.08735]
- "we follow [46] and we assume that we are given a number of recovery regions X_R^1, X_R^2, ..., X_R^d ⊆ X, control invariant subsets of the state space..." [arxiv:2407.08735]
- "Assume g ∈ SO(2) acts upon the noise ε_k in the same way as it acts upon the action a." [arxiv:2407.01812]
- "Since the relation between x^h_t and z^h_t is deterministic, for ease of notation, we show the prediction of the MDN components with x^h_t." [arxiv:2407.07636]
- "Considering Neural Networks are powerful function approximations, we assume that our network can adequately approximate a diagonalized form of the covariance matrices Σ̂^r_i [15], [33]." [arxiv:2407.07636]
- "we drop the timestep superscript and consider a generic MCQA setup with pairs (x̃,y) consisting of input x̃ and true label y. Suppose there is a calibration set Z = {z_i = (x̃_i, y_i)}^N_{i=1} of such pairs drawn i.i.d. from an unknown distribution D over Z." [arxiv:2307.01928]
- "the inputs to the softmax-kernel have fixed length (e.g. CLIP embeddings that are by default L2-normalized)." [arxiv:2312.01990]

**Variants**: "We assume X" is the default. "Importantly, we do not assume X" emphasizes the *absence* of an assumption — usually framing a strength of the method. "Note that X" is a soft assumption, often used for minor technical conventions. "Suppose X" is the formal-proof variant, used when the assumption is local to a theorem rather than global to the method.

**Why it works**: Reviewers spend significant effort detecting *implicit* assumptions — i.e., the things the writer relies on but doesn't say. Each explicit assumption is one less thing the reviewer has to discover. The "we do not assume X" form is especially valuable because it preempts the obvious reviewer question ("don't you need to know X?") with a direct answer.

---

### C5. The MDP/POMDP formalization template — RL papers state the tuple (S, A, R, ...) in the first Problem Formulation paragraph
**Pattern**: When the paper trains an RL policy or otherwise uses Markov Decision Process formalism, the canonical convention is to define the MDP tuple in the first or second paragraph of the Problem Formulation. The variations are: (S, A, R, P, γ) for a fully observable MDP; (S, A, R, P, O, γ) for a POMDP; or a sentence-form variant when the paper wants to avoid notation clutter. The state and action spaces are defined verbally; the reward is described in a sentence or two; transitions are usually assumed implicit.

**Evidence**:
- KNOWNO "Robots that ask for help" — "The environment e can be formulated as a partially observable Markov decision process (POMDP): at any given state s_t at time t, given a user instruction ℓ, the robot executes an action a_t according to a policy π, then transitions to a new state s_{t+1}." [arxiv:2307.01928]
- Unified Policy — observation, command, action defined in sequence: "we define the robot's observation o_t with the robot's base orientation g^base_t, angular velocity ω^base_t, joint position q_t, joint velocities q̇_t, previous action a_{t-1}, command c^cmd_t, and the feet clock timings θ^feet_t: o_t = (g^base_t, ω^base_t, q_t, q̇_t, a_{t-1}, c^cmd_t, θ^feet_t) (5) where the input command c^cmd_t = [v^cmd_base, x^cmd_ee, F^cmd_ee, F^cmd_base] ... The output action a_t is a residual added to a predefined default pose..." [arxiv:2505.20829]
- AESOP — state and dynamics: "In this work, we consider a robot with discrete time dynamics x_{t+1} = f(x_t, u_t), where x_t ∈ R^n represents the robot's state, and u_t ∈ R^m is the control input. Nominally, we aim to minimize some control objective C that depends on the states and inputs, subject to safety constraints on the state x_t ∈ X ⊆ R^n and input u_t ∈ U ⊆ R^m." [arxiv:2407.08735]
- ANYmal Parkour navigation module — described as "an outer loop running the navigation policy at 5 Hz and an inner loop running the locomotion module at 50 Hz... the navigation policy receives the relative position of the final goal, the remaining time to accomplish the task, the robot's base velocity, orientation, and the latent tensor of the perception module. It then selects a locomotion skill and guides the latter with a local position, heading, and time command." — verbal MDP statement [arxiv:2306.14874]

**Variants**: Modern policy-learning papers often write the MDP in observation-action-reward form rather than explicitly invoking "MDP" or "POMDP", but the tuple structure remains. The reward function is typically described informally ("Policy learning is supervised by rewarding accurate tracking..." [arxiv:2505.20829]) with the precise weighting deferred to an appendix. Discount factor γ is rarely mentioned in the main text — almost always relegated to implementation details.

**Why it works**: An MDP/POMDP tuple is the universal shape of an RL problem. Reviewers parse the tuple to understand: what does the agent see? what can it do? how is it scored? Whether stated formally or verbally, this template ensures the answers are findable.

---

## D. Cross-cutting observations

### D1. Methods are named after either their core mechanism (transparent) or a marketing handle (memorable)
**Observation**: Two naming conventions coexist. The *transparent* naming convention uses an acronym that spells out the mechanism: TinyMPC ("Tiny Model Predictive Control"), KNOWNO ("Know When You Don't Know"), MoVEInt ("Mixture of Variational Experts for Interactions"), SARA-RT ("Self-Adaptive Robust Attention for Robotics Transformers"). The *marketing* naming convention uses a memorable word that hints at the method's character but does not describe it: AESOP (the fable author, hinting at fast/slow reasoning), CoFRIDA (the painting robot, evoking artistry).

**Why it matters for writing**: Once chosen, the name must be used consistently — "we present TinyMPC, ..." — and capitalized identically across abstract, intro, method, and conclusion. The Method section opener (B1) typically introduces the name with a parenthetical expansion: "TinyMPC (Tiny MPC)..." or "AESOP, [acronym definition]...". Transparent names give reviewers a quick mnemonic for the technique. Marketing names require investment in repetition for the name to stick.

---

### D2. The "describe in Appendix X" relegation pattern is the load-bearing compression trick for tight page budgets
**Observation**: Across the corpus, every paper that meets a strict page budget (ICRA 6 pages, IROS 6 pages, RSS 8 pages, CoRL 9 pages) makes extensive use of appendix relegation. The marker sentences appear in every section: hyperparameters → appendix; proofs → appendix; ablations → appendix; extended results → appendix; full notation tables → appendix. The Method section in the main text becomes the *minimum sufficient* description; the appendix is the *complete* description.

**Why it matters for writing**: A first-draft Method section is almost always too long. Trimming it to fit means tagging non-essential paragraphs and moving them to appendices with a marker sentence. Reviewers expect this and even appreciate it: a Method section that fits crisply on one page reads as polished; one that sprawls reads as undisciplined.

---

### D3. The figure–equation–prose triangulation
**Observation**: Top-venue papers triangulate every important claim across three modes: (a) a figure that visually depicts the claim, (b) one or more numbered equations that formalize it, (c) prose that explains both. The reader can enter through any of the three and find their way to the others. Papers that rely on only one mode (e.g., wall-of-text prose, or figures-with-no-explanation) read as incomplete.

**Examples**: Equivariant Diffusion Policy [arxiv:2407.01812] triangulates "denoising function is equivariant" via Figure 2 (visual gradient field), Proposition 1 (formal statement), and explanatory prose ("If we infer ε for all actions in the action space, we effectively acquire a gradient field..."). Unified Policy [arxiv:2505.20829] triangulates "unified force-position control" via Fig. 2 (system architecture), Eqs. (1)–(4) (the impedance formulation), and prose linking the two. AESOP [arxiv:2407.08735] triangulates "fast and slow reasoning" via Fig. 1 (system diagram), the MPC formulation in Eq. (3), and Algorithm 1 (procedural prose).

**Why it matters for writing**: When drafting, ask of every major claim: "Where is this in a figure? Where is this in an equation? Where is this in prose?" If two of the three are missing, the claim is under-supported.

---

### D4. The "we differ from these in X" closer can use a comparison table as its substitute
**Observation**: Some papers replace the standard A2 positioning closer with a *comparison table* in the Related Work section. The table lists prior methods as rows and capability axes as columns; the writer's method is the last row with the most check-marks. This is dense and effective but is harder to write than the prose closer; it works best when the comparison axes are unambiguous and the prior methods are well-defined enough to be classified.

**Why it matters for writing**: When the prior work has 5+ comparable methods and 4+ clean axes, consider the table; when the comparison is more about *kind* than *capability*, stick with prose closers.

---

### D5. Cross-paper sub-corpus differences: solver papers vs policy-learning papers vs system papers
**Observation**: Three sub-corpora exhibit distinct rhetorical patterns:
- **Solver / algorithm papers** (TinyMPC [arxiv:2310.16985], Time-Optimal Ergodic Search [arxiv:2305.11643], SARA-RT [arxiv:2312.01990]): Heavy on equations, lemmas, propositions, and theoretical analysis. Preliminaries section is mandatory. Method section reads like a textbook chapter — derivations, proofs, algorithm boxes. Citation density is lower in Method because few prior works share the same derivation.
- **Policy learning / imitation learning papers** (Equivariant Diffusion Policy [arxiv:2407.01812], MoVEInt [arxiv:2407.07636], Unified Policy [arxiv:2505.20829], CoFRIDA [arxiv:2402.13442], OpenVLA [arxiv:2406.09246]): Equations are reduced — typically one loss equation, one network input-output equation. Bigger emphasis on data: training set composition, augmentations, demonstrations. Big architecture figure carries more weight than equations.
- **System / integration papers** (ANYmal Parkour [arxiv:2306.14874], AESOP [arxiv:2407.08735], Power Line MPC [arxiv:2304.00959], Robots Ask for Help [arxiv:2307.01928], Open X-Embodiment [arxiv:2310.08864]): Multiple components, each its own subsection. Figures showing system architecture (block diagrams) carry the load. Method section is longer and more verbal than the other two sub-corpora; Implementation Details may be a major subsection.

**Why it matters for writing**: Match your paper's rhetoric to its sub-corpus. A policy-learning paper that reads like a solver paper feels over-formal; a solver paper that reads like a system paper feels under-rigorous. Identifying the sub-corpus is the first step in matching the conventions.

---

### D6. The "two-stage training procedure" is a load-bearing engineering trope in RL-flavored papers
**Observation**: Multiple RL/policy-learning papers in this corpus introduce a "two-stage" or "staged" training procedure as a key implementation detail: stage 1 trains on a simpler distribution; stage 2 fine-tunes on the full distribution. This pattern is presented as if it were a finding ("we adopt a two-stage training procedure: ... This staged approach empirically yields more stable training than a single-stage setup, as further analyzed in Section C." [arxiv:2505.20829]; ANYmal Parkour curriculum [arxiv:2306.14874]; KNOWNO calibration phase [arxiv:2307.01928]).

**Why it matters for writing**: When training is staged, *name the stages explicitly* — Stage 1, Stage 2, or with descriptive labels. Explain *why* the staging is needed: empirically it stabilizes training, or it warms up a hard objective, or it disentangles two learning signals. Reviewers who see "two-stage" without a stated reason will assume the writer is hiding a hyperparameter-sensitivity problem.

---

### D7. Theorems and Propositions are sized-to-fit: small claims get propositions, big claims get theorems, edge claims get lemmas
**Observation**: When a paper makes a formal claim in the Method, the choice of "Lemma", "Proposition", "Theorem", or "Claim" follows a soft convention: **Theorem** is reserved for the paper's headline formal result (TinyMPC convergence analysis [arxiv:2310.16985], SARA-RT main approximation theorem [arxiv:2312.01990], AESOP MPC feasibility theorem [arxiv:2407.08735], Time-Optimal Ergodic Search optimality conditions theorem [arxiv:2305.11643]); **Proposition** is used for supporting results that follow from Theorem-level work (Equivariant Diffusion Policy Propositions 1 and 2 [arxiv:2407.01812], KNOWNO single-step and multi-step uncertainty alignment propositions [arxiv:2307.01928]); **Lemma** is used for intermediate technical results, often with the proof inline (SARA-RT Lemmas 3.1 and 3.2 [arxiv:2312.01990]); **Claim** is used for results stated without proof or with deferred proof (KNOWNO Claim 1 [arxiv:2307.01928]).

**Why it matters for writing**: Overclaiming (calling everything a Theorem) reads as posturing. Underclaiming (calling the headline result a Lemma) reads as undersold. Match the formal-claim label to the claim's load-bearing-ness in your argument.

---

## Sample size and corpus details

Papers analyzed in this document (full list):

1. **Open X-Embodiment** [arxiv:2310.08864] — ICRA 2024 Best Paper. Multi-embodiment robot learning. System / integration paper.
2. **CoFRIDA** [arxiv:2402.13442] — ICRA 2024. Robot painting. System / integration paper.
3. **Distilled Feature Fields** [arxiv:2308.07931] — CoRL 2023. Few-shot manipulation. Policy learning paper.
4. **OpenVLA** [arxiv:2406.09246] — CoRL 2024. Open-source VLA. Policy learning paper.
5. **SARA-RT** [arxiv:2312.01990] — ICRA 2024. Robotics-Transformers linearization. Solver / algorithm paper.
6. **TinyMPC** [arxiv:2310.16985] — ICRA 2024 Best Student Paper finalist. MPC for microcontrollers. Solver / algorithm paper.
7. **MoVEInt** [arxiv:2407.07636] — IROS 2024. Human-Robot Interaction. Policy learning paper.
8. **Power Line MPC** [arxiv:2304.00959] — IROS 2023 Best Paper. Perception-aware MPC for quadrotors. System / integration paper.
9. **Equivariant Diffusion Policy** [arxiv:2407.01812] — CoRL 2024. SE(3)-equivariant diffusion policy. Policy learning paper.
10. **KNOWNO / Robots Ask for Help** [arxiv:2307.01928] — CoRL 2023 Best Student Paper. LLM uncertainty alignment. System / integration paper.
11. **Unified Policy** [arxiv:2505.20829] — CoRL 2025 Best Paper. Force-position legged manipulation. Policy learning paper.
12. **Time-Optimal Ergodic Search** [arxiv:2305.11643] — RSS 2023 Outstanding Paper. Trajectory optimization. Solver / algorithm paper.
13. **AESOP / RT Anomaly Detection** [arxiv:2407.08735] — RSS 2024 Outstanding Paper. LLM anomaly monitor. System / integration paper.
14. **ANYmal Parkour** [arxiv:2306.14874] — Science Robotics 2024. Quadruped parkour. System / integration paper.

Sub-corpora and their distinctive rhetorical patterns:

- **Conference page-budgeted papers** (ICRA, IROS, CoRL, RSS): heavy appendix relegation (D2), inline-bold Related Work subsection leads (A9), roadmap sentences (B12).
- **Journal papers** (Science Robotics): no separate Related Work section (A5 variant), prior-work discussion interleaved across Methods and Discussion, longer prose passages overall.
- **Solver / algorithm sub-corpus** (TinyMPC, Time-Optimal Ergodic Search, SARA-RT): mandatory Preliminaries (C2), heavy equation/theorem use (D7), textbook tutorial voice in Background.
- **Policy learning sub-corpus** (Equivariant Diffusion Policy, MoVEInt, Unified Policy, OpenVLA, Distilled Feature Fields, CoFRIDA): training-data emphasis (B8), big architecture figures (B13), MDP-style problem formulation (C5), two-stage training (D6).
- **System / integration sub-corpus** (Open X-Embodiment, ANYmal Parkour, AESOP, KNOWNO, Power Line MPC): three-to-four-block architecture diagrams (B13), per-component subsections in Method, lower equation density, more prose per square inch.

Patterns where sub-corpus matters most:
- A5 (Related Work placement) — strong venue dependency.
- A9 (Italicized vs numbered subsection leads) — strong venue dependency.
- C2 (whether Preliminaries appears) — strongest in solver papers; weakest in single-mechanism policy papers.
- D5 (sub-corpus rhetorical signature) — every sub-corpus pattern essentially asks "match your paper's vibe to its sub-corpus".

Patterns that are universal across the corpus:
- A1, A2 (Related Work partitioned with positioning closers).
- A3 (range citations).
- A7 (the "However" pivot).
- A8 (5-to-1 citation-density ratio).
- B1 (Method opener with system name).
- B5 (equation sandwich).
- B6 (we-voice in Method).
- B10 (intuition sentences).
- B11 (appendix relegation).
- C3 (Problem Formulation four-paragraph template).
- C4 (explicit assumption stating).
