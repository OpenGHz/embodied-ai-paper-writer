# 01 — Abstract + Introduction Craft

Scope: rhetorical and structural conventions for writing the abstract and introduction of top-venue embodied-AI papers. 14 award-winning/notable papers analyzed (ICRA, IROS, CoRL, RSS, Science Robotics; 2022–2025). Focus is on HOW the openings are written, not what the techniques are.

---

## A. Abstract patterns

### A1. The five-move abstract: Domain frame → Gap → "We propose/introduce" → Method gist → Result + (optional) release
**Pattern**: Nearly every abstract follows a five-beat structure compressed into 6–12 sentences. (1) Open with a one-sentence framing of the subfield's broad capability, problem class, or recent trend. (2) Identify a specific gap or unresolved tension ("However...", "Yet...", "remains challenging"). (3) Mark the contribution explicitly with a verb of introduction — "We propose / We present / We introduce". (4) Give one-paragraph mechanism summary. (5) End with quantitative results and (often) a link/release statement.

**Evidence**:
- "Robots with the ability to balance time against the thoroughness of search have the potential to provide time-critical assistance in applications such as search and rescue. Current advances in ergodic coverage-based search methods have enabled robots to completely explore and search an area in a fixed amount of time. However, optimizing time against the quality of autonomous ergodic search has yet to be demonstrated. In this paper, we investigate solutions to the time-optimal ergodic search problem..." [arxiv:2305.11643]
- "Recent advancements in robotics have enabled robots to navigate complex scenes or manipulate diverse objects independently. However, robots are still impotent in many household tasks requiring coordinated behaviors such as opening doors... To address this challenge, we introduce, HARMONIC MM, an end-to-end learning method..." [arxiv:2312.06639]
- "Foundation models, e.g., large language models (LLMs), trained on internet-scale data possess zero-shot generalization capabilities that make them a promising technology towards detecting and mitigating out-of-distribution failure modes of robotic systems. Fully realizing this promise, however, poses two challenges: (i)... (ii)... In this work, we present a two-stage reasoning framework..." [arxiv:2407.08735]
- "The current paradigm for motion planning generates solutions from scratch for every new problem, which consumes significant amounts of time and computational resources... We seek to do the same by applying data-driven learning at scale..." [arxiv:2409.05864]

**Variants/exceptions**: Science Robotics paper [arxiv:2303.03381] uses a more journalistic frame ("Humanoid robots that can autonomously operate in diverse environments have the potential to help address labour shortages in factories, assist elderly at homes, and colonize new planets.") and skips an explicit gap clause, but still hits all five beats.

**Why it works**: The five-beat shape lets a busy reviewer extract problem, novelty, and evidence in under a minute, in exactly the order a reviewer scans for them.

---

### A2. Opening sentence frames a *broad class*, not a niche
**Pattern**: First sentence of the abstract names a CAPABILITY ("policies that..."), CLASS OF METHOD ("foundation models..."), or PROBLEM CLASS ("contact-rich manipulation often involves...") rather than the paper's specific contribution. The narrowing happens in sentences 2–3.

**Evidence**:
- "Large policies pretrained on a combination of Internet-scale vision-language data and diverse robot demonstrations have the potential to change how we teach robots new skills..." [arxiv:2406.09246]
- "Large, high-capacity models trained on diverse datasets have shown remarkable successes on efficiently tackling downstream applications. In domains from NLP to Computer Vision, this has led to a consolidation of pretrained models..." [arxiv:2310.08864]
- "Robotic loco-manipulation often involves contact-rich interactions with the environment, requiring the joint modeling of contact force and robot position." [arxiv:2505.20829]
- "Foundation models, e.g., large language models (LLMs), trained on internet-scale data possess zero-shot generalization capabilities..." [arxiv:2407.08735]
- "Physical caregiving robots hold promise for improving the quality of life of millions worldwide who require assistance with feeding." [arxiv:2506.14968]

**Variants/exceptions**: Two papers open with method-name-first instead of frame-first: "We propose MAC-VO, a novel learning-based stereo visual odometry (VO) framework..." [arxiv:2409.09479] and "Understanding how humans leverage semantic knowledge to navigate unfamiliar environments and decide where to explore next is pivotal..." [arxiv:2312.03275]. The latter still frames via a *capability humans have* before introducing the method.

**Why it works**: Reviewers and area chairs need to file a paper into a familiar slot within ~10 seconds; broad-frame openings let them anchor on the subfield before evaluating the contribution.

---

### A3. The "However" / "Yet" hinge sentence
**Pattern**: The transition from "what the field has done" to "what is missing" is almost always marked by a single short conjunction-led sentence using "However,", "Yet,", or a participial like "Despite...". This hinge is rarely longer than one sentence.

**Evidence**:
- "...have enabled robots to completely explore and search an area in a fixed amount of time. However, optimizing time against the quality of autonomous ergodic search has yet to be demonstrated." [arxiv:2305.11643]
- "Recent advancements in robotics have enabled robots to navigate complex scenes or manipulate diverse objects independently. However, robots are still impotent in many household tasks requiring coordinated behaviors..." [arxiv:2312.06639]
- "Yet, widespread adoption of VLAs for robotics has been challenging as 1) existing VLAs are largely closed and inaccessible to the public, and 2) prior work fails to explore methods for efficiently fine-tuning VLAs..." [arxiv:2406.09246]
- "However, recent visuomotor policies often focus solely on learning position or force control, overlooking their co-learning." [arxiv:2505.20829]
- "Fully realizing this promise, however, poses two challenges: (i) mitigating the considerable computational expense... and (ii) incorporating their judgement..." [arxiv:2407.08735]

**Variants/exceptions**: When the hinge enumerates >1 problem, it folds an inline list with "(i) / (ii)" or "1) / 2)" (see [arxiv:2406.09246], [arxiv:2407.08735]).

**Why it works**: The hinge is the load-bearing sentence in the abstract — it is the contract that the rest of the paper claims to fulfill. Marking it with a one-word transition makes it findable in seconds.

---

### A4. Contribution is signalled by a single verb phrase, not a buried claim
**Pattern**: After the gap, the contribution is announced with one of a small set of stock verb phrases: "we propose", "we introduce", "we present", or "we [show / demonstrate]". The phrase typically also embeds the contribution NAME ("we introduce X, a Y that...").

**Evidence**:
- "We introduce a zero-shot navigation approach, Vision-Language Frontier Maps (VLFM), which is inspired by human reasoning..." [arxiv:2312.03275]
- "We propose MAC-VO, a novel learning-based stereo visual odometry (VO) framework that trains a metrics-aware uncertainty model..." [arxiv:2409.09479]
- "In this work, we present KNOWNO, which is a framework for measuring and aligning the uncertainty of LLM-based planners..." [arxiv:2307.01928]
- "Addressing these challenges, we introduce OpenVLA, a 7B-parameter open-source VLA trained on a diverse collection of 970k real-world robot demonstrations." [arxiv:2406.09246]
- "We propose the first unified policy for legged robots that jointly models force and position control..." [arxiv:2505.20829]
- "Here, we present a fully learning-based approach for real-world humanoid locomotion." [arxiv:2303.03381]

**Variants/exceptions**: When the method has no catchy name, papers fall back to "we present a [method type]" (e.g., [arxiv:2305.11643]: "we investigate solutions to..."). When the contribution is a dataset / consortium, "we provide" is preferred ("we provide datasets in standardized data formats" [arxiv:2310.08864]).

**Why it works**: A single canonical signal verb tells the reviewer where the contribution claim begins; embedding the system name in the same clause anchors it for later citation.

---

### A5. Numeric results arrive late and are "deltas, not absolutes"
**Pattern**: Numeric claims (success rates, error metrics) appear in the last 2–3 sentences of the abstract and are almost always expressed as DELTAS over a named baseline (e.g., "+12% over X") or AS-OF claims ("state of the art on three benchmarks"). Raw absolute numbers without comparison are rare.

**Evidence**:
- "...absolute increases in success rates weighted by path length over prior state-of-the-art approaches of 12% on Gibson, 5% on Matterport 3D (MP3D) and 3% on Habitat-Matterport 3D (HM3D) datasets." [arxiv:2312.03275]
- "...demonstrating an improvement of 23%, 17% and 79% motion planning success rate over state of the art sampling, optimization and learning based planning methods." [arxiv:2409.05864]
- "OpenVLA demonstrates strong results for generalist manipulation, outperforming closed models such as RT-2-X (55B) by 16.5% in absolute task success rate across 29 tasks and multiple robot embodiments, with 7x fewer parameters." [arxiv:2406.09246]
- "...achieving approximately ∼39.5% higher success rates in four challenging contact-rich manipulation tasks over position-control policies." [arxiv:2505.20829]
- "...reducing the amount of help required by 10−24% as compared to baseline approaches." [arxiv:2307.01928]

**Variants/exceptions**: Methods-heavy papers without explicit numeric headlines use evaluative phrasing instead ("achieves state-of-the-art results" [arxiv:2312.03275]; "outperforms existing VO algorithms and even some SLAM systems in difficult scenarios" [arxiv:2409.09479]).

**Why it works**: Reviewers want to know "is this better than what I already know?" Deltas frame the paper as a competitive entry against a known baseline, which is the form reviewers find easiest to evaluate.

---

### A6. The closing-line "release / link" coda
**Pattern**: Abstracts of award-winning embodied papers very often close with a project page, code, dataset, or video URL — usually as the final sentence and often without preamble. This is treated as a sixth move appended to the five-beat structure.

**Evidence**:
- "The project website is robotics-transformer-x.github.io." [arxiv:2310.08864]
- "Videos of real world deployment can be viewed at naoki.io/vlfm." [arxiv:2312.03275]
- "Video results available at mihdalal.github.io/neuralmotionplanner." [arxiv:2409.05864]
- "Finally, we release model checkpoints, fine-tuning notebooks, and our PyTorch codebase with built-in support for training VLAs at scale on Open X-Embodiment datasets." [arxiv:2406.09246]
- "Supplementary materials and videos can be found at: emprise.cs.cornell.edu/feast." [arxiv:2506.14968]
- "Project website: https://f3rm.csail.mit.edu" [arxiv:2308.07931]
- "Videos illustrating our approach in both simulation and real-world experiments are available on our project page: https://sites.google.com/view/aesop-llm." [arxiv:2407.08735]

**Variants/exceptions**: Closed/non-systems papers without an artifact (e.g., [arxiv:2211.06917], [arxiv:2305.11643]) skip the coda or fold the link into the introduction figure caption.

**Why it works**: A URL in the abstract converts a paper into a product the reviewer can interact with; it also primes the reviewer that artifacts will be released, which weighs positively for community impact.

---

### A7. Abstract closes with "this approach / this work / these results suggest..." moral
**Pattern**: A subset of abstracts replace the result-delta sentence with a normative closing — a higher-level statement about what the contribution means for the field. This is more common in venue-prestige papers (Science Robotics, RSS, CoRL outstanding-paper tier).

**Evidence**:
- "The accomplishments of VLFM underscore the promising potential of vision-language models in advancing the field of semantic navigation." [arxiv:2312.03275]
- "KNOWNO can be used with LLMs out of the box without model-finetuning, and suggests a promising lightweight approach to modeling uncertainty that can complement and scale with the growing capabilities of foundation models." [arxiv:2307.01928]
- "Our results suggest that simple and general learning-based controllers are capable of complex, high-dimensional humanoid control in the physical world." (from intro tail, same paper) [arxiv:2303.03381]
- "These experimental results underscore the potential of our learned policy as a general framework for curating contact-rich robot interaction data, particularly in the absence of explicit force sensors." (intro tail) [arxiv:2505.20829]

**Why it works**: For high-profile venues, reviewers and program chairs look not just for novelty but for "agenda-setting" — papers that gesture at a research direction beyond their own contribution. The moralized closing signals that ambition without making unverifiable promises.

---

### A8. Length and density: 6–12 sentences, single paragraph
**Pattern**: All 14 abstracts are 1 paragraph, length 6–12 sentences (roughly 120–250 words), without subheadings. Within that envelope, density follows a U-shape: short opening, dense middle (method + experiment scope in 3–5 sentences), short close.

**Evidence**: All 14 papers analyzed follow this geometry. The longest abstract is OpenVLA at ~250 words [arxiv:2406.09246]; shortest is Science Robotics humanoid at ~155 words [arxiv:2303.03381].

**Variants/exceptions**: CoRL abstracts begin with the literal label "Abstract:" inline ("Abstract: Large policies pretrained..." [arxiv:2406.09246]; "Abstract: Self-supervised and language-supervised image models..." [arxiv:2308.07931]). Conference IEEE papers use "Abstract—" with em dash ([arxiv:2310.08864], [arxiv:2312.03275]).

**Why it works**: The abstract is a venue-style genre; deviation reads as either pretentious (too short, "we propose X. We achieve Y." paper) or undisciplined (too long, multi-paragraph). 6–12 sentences signals fluency in the genre.

---

## B. Introduction patterns

### B1. The Hook: an open question, a vivid scenario, or a "grand statement"
**Pattern**: Introductions open with one of three rhetorical hooks rather than diving into definitions: (a) a research question posed to the reader ("How can we...?"), (b) an evocative scenario or use-case ("Consider a warehouse robot..."), or (c) a grand declaration about the field ("The dream of robotics has always been..."). The vivid-scenario hook is especially common in CoRL and RSS papers; the grand-statement hook is the Science Robotics signature.

**Evidence**:
- "How can we endow our robots with the ability to know when they don't know? Accurately modeling and accounting for uncertainty is a longstanding challenge..." [arxiv:2307.01928]
- "What form of scene representation would facilitate open-set generalization for robotic manipulation systems? Consider a warehouse robot trying to fulfill an order by picking up an item from cluttered storage bins filled with other objects." [arxiv:2308.07931]
- "How do humans navigate in novel environments? The process of human navigation in unfamiliar environments is complex..." [arxiv:2312.03275]
- "The dream of robotics has always been that of general purpose machines that can perform many tasks in diverse, unstructured environments. Examples include moving boxes, changing tires, ironing shirts, and baking cakes." [arxiv:2303.03381]
- "Eating is a fundamental part of human life, deeply intertwined with identity and social interaction." [arxiv:2506.14968]

**Variants/exceptions**: ICRA papers more often use a methods-frame hook ("A central lesson from advances in machine learning... is that large-scale learning from diverse datasets can enable capable AI systems..." [arxiv:2310.08864]). Highly technical papers may open by naming the formal problem ("VISUAL Odometry (VO) predicts the relative camera pose from image sequences..." [arxiv:2409.09479]).

**Why it works**: The hook earns the reviewer's attention on sentence one. Reviewers report fatigue mid-conference; an opening that does WORK rather than warming up earns goodwill.

---

### B2. Funnel structure: broad capability → field state → specific gap → "we" sentence
**Pattern**: After the hook (1 sentence or so), the intro funnels through three or four widening-to-narrowing moves: (a) state of the field/world (1–2 sentences), (b) recent progress citing key references (1 paragraph), (c) "however" pivot to a specific unsolved problem (1 paragraph), (d) "in this paper / to address this, we propose..." sentence. The "we propose" sentence is reliably in paragraph 3 or 4 of the intro.

**Evidence**:
- OpenVLA: broad ("A key weakness of learned policies for robotic manipulation is their inability to generalize beyond their training data...") → recent progress ("Yet beyond robotics, existing foundation models for vision and language...") → narrow gap ("Yet, there are two key reasons preventing the widespread use of existing VLAs: 1) current models... are closed... 2) existing works do not provide best practices...") → contribution ("To this end, we introduce OpenVLA, a 7B-parameter open-source VLA...") [arxiv:2406.09246]
- Harmonic MM: broad ("The field of robot learning has traditionally treated robot navigation and manipulation as separate domains...") → recent progress ("agents have been trained to efficiently explore and navigate...") → pivot ("However, in household settings, many tasks require coordinated body movements...") → "To address these challenges, we introduce an approach that efficiently coordinates..." [arxiv:2312.06639]
- KNOWNO: broad ("Accurately modeling and accounting for uncertainty is a longstanding challenge...") → field ("Recently, approaches that leverage large language models (LLMs) for planning...") → gap ("However, one of the major challenges with current LLMs is their tendency to hallucinate...") → contribution ("Statement of contributions. We propose KNOWNO...") [arxiv:2307.01928]

**Why it works**: The funnel matches reviewer reading order — they want to know "is this problem important? is the field stuck? what does this paper add?" in that exact sequence. Inverting the funnel (jumping to the contribution first) reads as either bragging or as a workshop paper.

---

### B3. Prior work is cited as "the field has done X [n,m,...] but..."
**Pattern**: In the intro (not Section 2), prior work is referenced in dense bracketed citation clusters appended to capability claims. The grammatical form is almost always "[Group] have demonstrated/achieved/shown X [n, m, o]" or "Recent work in Y has Z [n–m]", followed by a "however" pivot. Individual prior papers are rarely named in the intro (that is deferred to Section 2 / Related Work).

**Evidence**:
- "agents have been trained to efficiently explore and navigate environments ([1], [2], [3], [4]), while on the other, substantial progress has been made in performing complex manipulation tasks, such as handling articulated objects with static arms in tabletop settings ([5], [6], [7], [8])." [arxiv:2312.06639]
- "Recently, there has been a concerted effort to scale up data collection for robot tasks [18], [19]. However, the level of diversity of scenes and arrangement of objects is still limited..." [arxiv:2409.05864]
- "learning-based approaches have proven very effective in dexterous manipulation (13–15), quadrupedal locomotion (16–18), and bipedal locomotion (19–23)." [arxiv:2303.03381]
- "Towards this goal, existing work has explored integrating pretrained language and vision-language models for robotic representation learning [12–14] and as a component in modular systems for task planning and execution [15, 16]." [arxiv:2406.09246]

**Variants/exceptions**: When the contribution stands directly against ONE prior paper, the intro will name that paper (e.g., OpenVLA naming RT-2-X for the contrast it leverages [arxiv:2406.09246]; Neural MP naming MπNets [arxiv:2409.05864]). The named-prior-work move is reserved for direct contrast, not lit-survey.

**Why it works**: The intro is for positioning; Section 2 is for crediting individuals. Bracketed clusters convey "I know the literature" without slowing the funnel.

---

### B4. The "Statement of contributions" / "Our contributions are" bullet list
**Pattern**: The intro ends (or nearly ends) with an explicit enumeration of 3–5 contributions, signposted by a heading-like phrase: "Our contributions are:", "Statement of contributions.", "Specifically, our contributions are:", "Overall, our contributions can be summarized as follows:", or "In summary, the main contributions are:". Each bullet is one sentence, starts with a noun phrase or "We", and embeds a verb like "propose / introduce / present / demonstrate / show / release."

**Evidence**:
- "Our primary contributions are: • An end-to-end learning approach that jointly optimizes navigation and manipulation, achieving an absolute improvement of 17.6%... • Adding the support for more complex tasks... • Successful transfer of agents trained in simulation to real-world... • Introducing a new benchmark..." [arxiv:2312.06639]
- "In summary, the main contributions are: • We present a learning-based 2D uncertainty network with metrics awareness... • This paper introduces a novel metrics-aware 3D covariance model... • We propose the MAC-VO, a stereo VO pipeline..." [arxiv:2409.09479]
- "Statement of contributions. We propose KNOWNO... We make the following contributions: (1) Given a language instruction, we utilize... (2) We prove theoretical guarantees on calibrated confidence... (3) We evaluate KNOWNO in both simulation and hardware..." [arxiv:2307.01928]
- "Overall, our contributions can be summarized as follows: 1. We propose the first model for learning unified force and position control in legged loco-manipulation... 2. Through 7 experiments... we demonstrate the effectiveness and robustness of our learned policy... 3. We develop a force-aware robot imitation learning data collection pipeline..." [arxiv:2505.20829]
- "In summary, our contributions are as follows: 1) A novel time-optimal ergodic trajectory optimization method... 2) Proof of analytical conditions of optimality... 3) Demonstration of time-optimal search trajectories on a drone system..." [arxiv:2305.11643]
- "Overall, our contributions include: • FEAST: A flexible mealtime-assistance system... • A user study involving 21 care recipients... • A personalization framework built on three key tenets... • A five-day in-the-wild system evaluation... • An evaluation with an Occupational Therapist..." [arxiv:2506.14968]
- "as such, our contributions are threefold: 1) Fast reasoning with embeddings:... 2) Slow reasoning through autoregressive generation:... 3) Hierarchical multi-contingency planning:..." [arxiv:2407.08735]

**Variants/exceptions**: A few papers fold the contribution list into running prose rather than a bullet list (Science Robotics: "We hypothesize that..." → "We train..." → "We show..." [arxiv:2303.03381]); CoRL outstanding paper OpenVLA enumerates inline with "(1)... (2)... (3)... (4)..." rather than a visual bullet list [arxiv:2406.09246]. The bullet variant is the modal form for ICRA/IROS/RSS; CoRL leans toward "(i)/(ii)/(iii)" inline numbering.

**Why it works**: The contribution list is the paper's "score card" — reviewers can verify each bullet against the experiments section. Making it visually findable saves reviewer time and reduces the risk that a contribution is overlooked.

---

### B5. The contribution bullet's anatomy: "Capability noun + verb of newness + quantified result"
**Pattern**: Inside a contribution bullet, the canonical anatomy is: (a) a noun phrase naming what is delivered (a "framework", "policy", "benchmark", "method", "evaluation"), (b) a participial or relative clause describing what it does ("that jointly optimizes...", "that achieves..."), (c) optionally a quantified result. Bullets that don't quantify usually compensate with strong positioning words ("first", "novel", "general").

**Evidence**:
- "An end-to-end learning approach that jointly optimizes navigation and manipulation, achieving an absolute improvement of 17.6% in average success rate across tasks compared to previous methods." [arxiv:2312.06639]
- "We develop a force-aware robot imitation learning data collection pipeline using our learned force estimator, improving position-based imitation learning baselines by ∼39.5% on three challenging contact-rich manipulation tasks..." [arxiv:2505.20829]
- "We propose the first model for learning unified force and position control in legged loco-manipulation, enabling diverse control behaviors such as position tracking, force control, and compliance with a single policy." [arxiv:2505.20829]
- "Fast reasoning with embeddings: We propose a real-time anomaly detection method that, using relatively small FMs (e.g., 120M parameters) and the robot's previous nominal experiences, surpasses generative chain-of-thought (CoT) reasoning with high-capacity LLMs such as GPT-4." [arxiv:2407.08735]

**Why it works**: Reviewers grade contributions on "specificity × novelty × evidence." This three-part anatomy hits all three slots in a single sentence. Vague bullets ("we contribute insights into X") consistently underperform in reviewer impressions.

---

### B6. "First to demonstrate / first work to" positioning
**Pattern**: When the contribution is a precedent claim (new artifact, first method of its kind), papers stake "first" claims clearly and conservatively. Usual phrasings: "To our knowledge,...", "the first work to", "we are the first to demonstrate".

**Evidence**:
- "To our knowledge, Neural MP is the first work to demonstrate that such a neural policy can generalize to a broad set of out-of-distribution of real-world environments..." [arxiv:2409.05864]
- "we are the first to demonstrate the effectiveness of compute-efficient fine-tuning methods leveraging low-rank adaptation [LoRA; 26] and model quantization [27] to facilitate adapting OpenVLA models on consumer-grade GPUs..." [arxiv:2406.09246]
- "FEAST is the first to consider personalized gesture detection for those with mobility limitations." [arxiv:2506.14968]
- "To our knowledge, this is the first application of FM embeddings to the task of runtime monitoring, enabling safe and real-time control of an agile robotic system." [arxiv:2407.08735]
- "We propose the first unified policy for legged robots that jointly models force and position control learned without relying on force sensors." [arxiv:2505.20829]

**Variants/exceptions**: When the claim is incremental rather than novel-genre, papers prefer "Unlike prior works, we...", "In contrast to...", or "Our work differs from X in three aspects: (1)... (2)... (3)..." [arxiv:2406.09246, RT-2-X contrast].

**Why it works**: "First" claims signal novelty to reviewers but are risky if overreached. The hedge "to our knowledge" buys insurance against missed prior work and is the venue-correct way to make a precedence claim.

---

### B7. The teaser-figure reference in the first or second paragraph
**Pattern**: Most papers reference their Figure 1 (the "teaser") within the first one or two paragraphs of the introduction, usually with a parenthetical "(see Fig. 1)" or "(Figure 1)". The teaser figure typically shows the end-to-end use case, the high-level method diagram, or a hero photo of the real-world deployment.

**Evidence**:
- "As an example (Fig. 1), a robot tasked with heating food may be asked to 'place the bowl in the microwave'..." [arxiv:2307.01928]
- "Figure 1 illustrates how our system works. The robot first scans a tabletop scene by taking a sequence of photos using an RGB camera mounted on a selfie stick (Figure 1, left)." [arxiv:2308.07931]
- "In this paper, we propose a learning-based approach for real-world humanoid locomotion (Figure 1)." [arxiv:2303.03381]
- "These assets are combined to create complex scenes resembling real world scenarios (Fig. 2), as described in Alg. 1." [arxiv:2409.05864]
- "As shown in Fig. 1, AESOP splits the monitoring task into two separate stages..." [arxiv:2407.08735]
- "We develop FEAST using community-based participatory research [28] in collaboration with two CRs (Figure 1)." [arxiv:2506.14968]

**Variants/exceptions**: Theory-heavy or formalism-first papers may defer the Figure 1 reference until after the contribution statement ([arxiv:2305.11643]: Figure 1 referenced in contribution 3 only).

**Why it works**: A reviewer who reads only the abstract + Figure 1 + contributions list should still come away with a correct mental model of the paper. The early teaser reference invites that scan path explicitly.

---

### B8. Footnote / project-page link drop in the intro
**Pattern**: When the abstract includes a release link, the intro often repeats or extends it via a footnote on first mention of the method name. The footnote attaches to the "we introduce X" sentence and contains the URL.

**Evidence**:
- "we introduce OpenVLA, a 7B-parameter open-source VLA that establishes a new state of the art for generalist robot manipulation policies.¹" with footnote 1 detailing model openness and release commitments [arxiv:2406.09246]
- "AESOP¹ ... ¹This name is inspired by the author of 'The Tortoise and the Hare,' in reference to our slow and fast reasoners." [arxiv:2407.08735]
- "Webpage with additional information, videos, and code: https://robot-help.github.io" [arxiv:2307.01928] (as footnote 1)
- "More results on https://rchalyang.github.io/HarmonicMM" [arxiv:2312.06639] (as author-affiliation footnote)

**Why it works**: Re-asserting the URL in the intro footnote ensures readers who skipped the abstract still find the artifact, and signals confidence in release.

---

### B9. The end-of-intro "paper overview" or "organization" paragraph (optional)
**Pattern**: Some papers — especially RSS and theoretical / control papers — end the intro with a short paragraph that maps the rest of the paper: "Section II reviews related work. Section III presents the method. Section IV evaluates..." Other papers omit this entirely, jumping directly from the contribution bullet to Section 2.

**Evidence**:
- "The paper is structured as follows: Section II overviews related work. Section III describes preliminary information on ergodic search and time-optimal control. Section IV poses the time-optimal ergodic search problem and presents solutions to the problem. Section V then presents various simulated and experimental results for the proposed solution... Last, Section VI provides conclusions and an outlook on future work." [arxiv:2305.11643]
- "Organization: We first discuss related work in §II and formalize the problem setup in §III. Then, we present our approach in §IV and evaluate our method in §V. Finally, we conclude and provide a future outlook in §VI." [arxiv:2407.08735]
- (Counter-example, no overview) OpenVLA jumps from contribution paragraph directly to "2 Related Work" with no roadmap [arxiv:2406.09246].
- (Counter-example) Harmonic MM ends with bullets, no roadmap, transitions straight to Section II [arxiv:2312.06639].

**Variants/exceptions**: The roadmap paragraph is fading in ML-flavored venues (CoRL, NeurIPS-adjacent) but still standard in IEEE-style ICRA/IROS/RSS papers. When present, it is one short paragraph or one short sentence as a section label ("Organization:").

**Why it works**: When the paper is long, theoretical, or has unusual section order (e.g., experiments before related work), the roadmap protects the reader from getting lost. When the paper follows standard order, the roadmap is redundant and can be omitted.

---

### B10. Intro → Section 2 handoff: silent transition, no bridging sentence
**Pattern**: The last paragraph of the intro is almost always the contribution bullet list (or its prose equivalent). The transition to Section 2 ("Related Work") is then silent: no bridging sentence, no "We now review...". Section 2 begins with a topical subheading and a fresh general statement.

**Evidence**:
- Intro ends "...In summary, the main contributions are: • ... • ... • ..." then immediately "II. RELATED WORKS" → "Existing geometric-based methods optimize the camera pose..." [arxiv:2409.09479]
- Intro ends with "Our primary contributions are: • ... • ... • ... • ..." then "II. RELATED WORK" → "Embodied AI Benchmark. Over the past few years, a variety of standard benchmarks have emerged..." [arxiv:2312.06639]
- Intro ends "we open-source all models, deployment and fine-tuning notebooks, and the OpenVLA codebase for training VLAs at scale..." then "2 Related Work" → "Visually-Conditioned Language Models Visually-conditioned language models (VLMs), which are trained on Internet-scale data..." [arxiv:2406.09246]
- Intro ends "We demonstrate these facts across... LLMs... simulated and real-world closed-loop quadrotor experiments... and... real-world failure modes..." then "II. RELATED WORK" → "Out-of-Distribution Robustness: The fact that learning-based systems often behave unreliably..." [arxiv:2407.08735]

**Variants/exceptions**: The KNOWNO paper inserts an "Overview: Robots that Ask for Help" section between the intro and conventional related work — a hybrid "what-the-paper-does-in-one-page" section that absorbs both contributions and method overview before Section 3 [arxiv:2307.01928]. F3RM uses "2 Problem Formulation" rather than "2 Related Work" as its first post-intro section, deferring related-work to Section 5 [arxiv:2308.07931].

**Why it works**: Bridging sentences ("Now we discuss prior work") add length without information. The convention of silent transition lets each section open with maximum signal density.

---

### B11. Section 2 opening pattern: topical subheading + broad capability sentence
**Pattern**: The first paragraph of Section 2 typically opens with a TOPICAL SUBHEADING (bolded or italicized noun phrase ending in a period or bold), followed immediately by a sentence describing the broader subarea. The subheading lets the reviewer skim the related-work coverage at a glance.

**Evidence**:
- "II. RELATED WORK / A. Multi-Agent Systems / Multi-Agent systems have been a major area of research, particularly in the context of cooperative manipulation..." [arxiv:2211.06917]
- "II. RELATED WORK / Embodied AI Benchmark. Over the past few years, a variety of standard benchmarks have emerged..." [arxiv:2312.06639]
- "2 Related Work / Visually-Conditioned Language Models Visually-conditioned language models (VLMs), which are trained on Internet-scale data to generate natural language..." [arxiv:2406.09246]
- "II. RELATED WORK / Out-of-Distribution Robustness: The fact that learning-based systems often behave unreliably on data that is dissimilar from their training data has been extensively documented..." [arxiv:2407.08735]
- "II. RELATED WORKS / ObjectNav. Object Goal Navigation (ObjectNav) involves executing semantic target-driven navigation in a novel environment..." [arxiv:2312.03275]

**Variants/exceptions**: Papers with a single homogeneous prior-work cluster (rare in embodied AI) may omit subheadings and run one continuous paragraph; this is uncommon among the analyzed sample.

**Why it works**: Subheadings turn the related-work section into a quick coverage audit — reviewers verify that each major sub-topic is acknowledged. The opening sentence under each subheading restates the subarea so the reviewer doesn't have to remember definitions from the intro.

---

### B12. Acknowledging-but-distinguishing closing of intro paragraphs
**Pattern**: Inside the funnel, paragraphs that survey prior work end with a "however / in contrast / unlike" clause that explicitly differentiates the present work. This sentence is usually short and tight, with parallel verb structure.

**Evidence**:
- "In contrast, our work proposes a zero-shot method that can take in an open-set of object categories, uses models that were trained on large amounts of real-world data, and demonstrates successful semantic navigation in the real world." [arxiv:2312.03275]
- "Unlike previous methods [9] that handle force and position control independently, we train a single control policy using RL in Isaac Gym..." [arxiv:2505.20829]
- "Unlike these works, OpenVLA adopts a more end-to-end approach, directly fine-tuning VLMs to generate robot actions by treating them as tokens in the language model vocabulary." [arxiv:2406.09246]
- "However, our work differs from RT-2-X in multiple important aspects: (1) by combining a strong open VLM backbone with a richer robot pretraining dataset, OpenVLA outperforms RT-2-X in our experiments while being an order of magnitude smaller; (2)..." [arxiv:2406.09246]
- "Notably, our work proposes a unified learning framework that integrates navigation and manipulation in a seamless manner, addressing the limitations of predefined primitives..." [arxiv:2312.06639]

**Why it works**: Reviewers expect every related-work paragraph to end with "and here's why we're different." Not delivering it leaves the paragraph reading as a defense of prior work rather than a positioning of the current paper.

---

## Cross-cutting observations

1. **Authorial pronoun**: All 14 papers use "we" exclusively. None use "the authors" or passive avoidance. "We propose / we introduce / we present" is the universal authorial voice.

2. **Tense**: Abstracts are mostly present-tense ("we propose", "X achieves", "the model demonstrates"). Past-tense appears only for completed experiments ("we evaluated", "we conducted"). Introductions follow the same rule.

3. **Method-naming**: Award-winning papers consistently brand their contribution with a memorable acronym or name (OpenVLA, KNOWNO, VLFM, MAC-VO, AESOP, FEAST, F3RM, Neural MP, HARMONIC MM, RT-X). The name is introduced on first contribution mention and uppercased / formatted consistently throughout. Two analyzed papers do NOT brand the method (the distributed MPC paper [arxiv:2211.06917]; the time-optimal ergodic paper [arxiv:2305.11643]) — both are theory-leaning and rely on the technique name itself for identity.

4. **Hedging in claims**: "To our knowledge", "to the best of the authors' knowledge", "may", "could", and "suggests" appear frequently in precedence and impact claims. Overly confident claims without hedges are rare and tend to be confined to direct comparison ("outperforms" with a specific number).

5. **Footnote density**: The intro footnote is a load-bearing element. It typically carries: (a) the project URL, (b) equal-contribution notes, (c) acronym backstory or naming rationale ([arxiv:2407.08735] AESOP-as-Tortoise-and-Hare), (d) caveats on what "open-source" means ([arxiv:2406.09246] re component licenses).

6. **What is NOT in the intro**: experimental detail, technical formalism, complete prior-work survey. Those are reserved for Sections 2, 3+. Papers that pollute the intro with formalism (very rare in this sample) feel front-loaded and dense to a reviewer.

7. **The "two-challenges" template**: A frequently observed micro-structure: the gap is enumerated as "two challenges: (i)..., (ii)...". This appears in [arxiv:2406.09246], [arxiv:2407.08735], and KNOWNO's "two desiderata" [arxiv:2307.01928]. It primes the contribution list to also be enumerated.

8. **Closing-line of the intro is rarely a "we open-source X" but often is**: Half the analyzed papers conclude the intro with a release-flavored sentence ("we release model checkpoints..." [arxiv:2406.09246]; "we open-source all models..." [arxiv:2406.09246]; "FEAST: A flexible mealtime-assistance system... all hardware and software components... are open-sourced" [arxiv:2506.14968]). For non-release papers, the closing line is the last contribution bullet.

9. **Equal-contribution and corresponding-author footnotes**: Always on the first page, attached to author names rather than the title. Conventionally an asterisk for equal contribution, dagger for corresponding author.

---

## Sample size

N papers analyzed: 14

arXiv IDs (with venue tags from filenames):
- 2310.08864 — ICRA 2024 Best (Open X-Embodiment / RT-X)
- 2312.03275 — ICRA 2024 Best Cognitive (VLFM)
- 2409.09479 — ICRA 2025 Best (MAC-VO)
- 2211.06917 — ICRA 2023 Best (Distributed DDPC)
- 2312.06639 — IROS 2024 Best Mobile (Harmonic MM)
- 2409.05864 — IROS 2025 Best Student (Neural MP)
- 2308.07931 — CoRL 2023 Best (F3RM / Distilled Feature Fields)
- 2307.01928 — CoRL 2023 Best Student (KNOWNO / Robots That Ask For Help)
- 2406.09246 — CoRL 2024 Outstanding (OpenVLA)
- 2505.20829 — CoRL 2025 Best (Unified Force/Position Policy)
- 2305.11643 — RSS 2023 Outstanding (Time-Optimal Ergodic Search)
- 2407.08735 — RSS 2024 Outstanding (AESOP / RT Anomaly Detection)
- 2506.14968 — RSS 2025 Outstanding (FEAST)
- 2303.03381 — Science Robotics 2024 (Real-World Humanoid)
