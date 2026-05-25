# 03 — Experiments + Results Craft

Scope: rhetorical and structural conventions for the Experiments/Results section of award-winning embodied-AI papers. Initial draft built on 5 papers; final corpus targets 15 (ICRA, IROS, CoRL, RSS, Science Robotics; 2023–2025). Focus is on HOW experiments are STRUCTURED IN PROSE and HOW results are NARRATED — not on what experiments were run.

---

## A. Experiments section structure and opening

### A1. Open with a "we aim to answer" / "experiments answer X questions" framing, then enumerate the questions
**Pattern**: The first paragraph of the Experiments section almost never begins with setup detail. Instead, it states the *purpose of the section* in one sentence and then enumerates 2–4 research questions in a numbered list ("(1)... (2)... (3)..."). The questions become the de facto sub-section structure, with each later subsection often answering one of them.

**Evidence**:
- "Our experiments answer three questions about the effect of X-embodiment training: (1) Can policies trained on our X-embodiment dataset effectively enable positive transfer, such that co-training on data collected on multiple robots improves performance on the training task? (2) Does co-training models on data from multiple platforms and tasks improve generalization to new, unseen tasks? (3) What is the influence of different design dimensions, such as model size, model architecture or dataset composition, on performance and generalization capabilities of the resulting policy? To answer these questions we conduct the total number of 3600 evaluation trials across 6 different robots." [arxiv:2310.08864]
- "The goal of our experimental evaluations is to test OpenVLA's ability to serve as a powerful multi-robot control policy out of the box, as well as be a good initialization for fine-tuning to new robot tasks. Concretely, we aim to answer the following questions: 1. How does OpenVLA compare to prior generalist robot policies, when evaluating on multiple robots and various types of generalization? 2. Can OpenVLA be effectively fine-tuned on a new robot setup and task...? 3. Can we use parameter-efficient fine-tuning and quantization to reduce the computational requirements...?" [arxiv:2406.09246]
- Table-tennis paper opens its evaluation with two anchor questions about the human user study: "(1) how much adaptation occurred during the matches? (2) Did the agent develop different strategies depending on the skill level of the opponent?" — questions later directly addressed as "(1) How much adaptation occurred..." and "(2) Did the agent develop different strategies..." paragraph leads [arxiv:2408.03906]

**Why it works**: A numbered list of questions makes evaluation goals legible in 5 seconds. It also gives the reviewer permission to skim — they know exactly which subsection answers which question. The total-trial-count "3600 evaluation trials across 6 different robots" sentence simultaneously primes scale (this is rigorous) and gives reviewers a defense-line citation.

---

### A2. Mark the section transition with a one-line setup-context anchor
**Pattern**: Right after the question list, papers drop a one-sentence anchor that names the *evaluation arena* (sim vs real, # robots, # tasks, # rollouts) BEFORE detailing any baseline or metric. This lets the reader file the upcoming numbers into a mental container.

**Evidence**:
- "We evaluated our method on Daily Mobile Manipulation Task Suite both in simulation and in the real world. We deployed the policy (learned in simulation) in a real apartment with multiple rooms without any adaptation or fine-tuning." [arxiv:2312.06639]
- "To answer these questions we conduct the total number of 3600 evaluation trials across 6 different robots." [arxiv:2310.08864]
- "Overall, we evaluated each method in 170 rollouts (17 tasks with 10 trials each) for BridgeData V2 experiments and 60 rollouts (12 tasks with 5 trials each) for Google robot experiments." [arxiv:2406.09246]

**Why it works**: Reviewers reflexively look for "how many trials" before believing any percentage. Putting the count adjacent to the question list short-circuits skepticism early.

---

### A3. The "Compared Methods" / "Comparisons" / "Baselines" lead-paragraph
**Pattern**: Baselines are introduced under an explicit named heading or paragraph lead ("Comparisons.", "Compared Methods.", "Baselines."). Each baseline gets ONE short paragraph or numbered bullet that does three things in order: (1) name + reference, (2) one-line summary of the mechanism, (3) optional one-line note on what variant is implemented for fair comparison.

**Evidence**:
- "For a comparative evaluation, we compared the following algorithms with access to proprioceptions only: 1) Baseline [12]: The policy was trained without any adaptation mechanism. 2) AdaptationNet [20], [21]: The policy was trained with an implicit environmental factor encoder using the student-teacher training framework... 3) EstimatorNet [24]: The policy was concurrently trained with an estimator network that explicitly estimates the body state without a context estimation..." [arxiv:2301.10602]
- "We compare OpenVLA's performance to three prior generalist manipulation policies: RT-1-X [1], RT-2-X [1], and Octo [5]. RT-1-X (35M parameters) and Octo (93M parameters) are transformer policies trained from scratch on subsets of the OpenX dataset; Octo is the state-of-the-art model among open-source manipulation policies. RT-2-X (55B parameters) is a state-of-the-art, closed-source VLA that leverages Internet-pretrained vision and language backbones." [arxiv:2406.09246]
- "We propose two sets of baselines to experimentally verify different parts of our system. First, we test our reward design and overall pipeline (Tab. 2): • Noisy: This simulates a system that uses an elevation map... • No inner product reward (NoInner): This replaces the inner product reward... • No feet clearance penalty (NoClear): Removes the penalization for stepping near the edges..." [arxiv:2309.14341]

**Why it works**: The reader needs to map names → mechanisms in their head. A bullet/sentence-per-baseline form lets them look up any name later by glance. The "parameters count" addendum (35M / 93M / 55B / 7B) is a reviewer-armor move: it preempts "is this a fair comparison" skepticism.

---

### A4. The fair-comparison sentence is stated explicitly
**Pattern**: Somewhere in the setup, a single sentence promises that all methods were evaluated under identical conditions. Stock formulations: "For a fair comparison, we used the same network architecture and...", "All evaluations are conducted as A/B evaluations, using the same tasks with the same sets of initial robot and object states...", "we use the same network architecture stated in Sec IV and the same hyperparameters for baselines."

**Evidence**:
- "For a fair comparison, we used the same network architecture and fixed the initial random seeds for all methods." [arxiv:2301.10602]
- "All evaluations in this and the following sections are conducted as A/B evaluations, using the same tasks with the same sets of initial robot and object states, to ensure fair comparison." [arxiv:2406.09246]
- "For a fair comparison, we use the same network architecture stated in Sec IV and the same hyperparameters for baselines." [arxiv:2312.06639]

**Why it works**: This is a one-sentence vaccine against the most common reviewer attack ("you tuned your method but not the baselines"). Reviewers tick the box and move on.

---

### A5. Sub-section naming follows a question → answer or a stage convention
**Pattern**: Sub-headings rarely name techniques. Instead they either (a) name a *question* the subsection answers, or (b) name a *stage* of evaluation. Common patterns: "In-distribution performance...", "Improved generalization to out-of-distribution settings", "Design decisions", "Comparison with the previous approaches", "[Method] is Efficient.", "[Method] transfers to the real world."

**Evidence**:
- RT-X uses question-style heads: "A. In-distribution performance across different embodiments / B. Improved generalization to out-of-distribution settings / C. Design decisions" [arxiv:2310.08864]
- Harmonic MM uses outcome-style heads: "Comparison with the previous approaches" then "H ARMONIC MM is Efficient." then "H ARMONIC MM transfers to the real world." then "Ablation Study of H ARMONIC MM" [arxiv:2312.06639]
- OpenVLA splits by *what is being evaluated*: "5.1 Direct Evaluations on Multiple Robot Platforms / 5.2 Data-Efficient Adaptation to New Robot Setups / 5.3 Parameter-Efficient Fine-Tuning / 5.4 Memory-Efficient Inference via Quantization" [arxiv:2406.09246]

**Why it works**: Subsection titles become a second table of contents. A reader scanning only the sub-heads should be able to recite the headline claims.

---

## B. Baselines, metrics, tasks introductions

### B1. Metric introduction = "we measured X (formal name + symbol) as the performance metric"
**Pattern**: Each metric is introduced with a single sentence that names it, often abbreviates it, and indicates which direction is good (↑ or ↓). Multi-metric papers put them in a table caption row.

**Evidence**:
- "We measured absolute tracking error (ATE) as the performance metric and constructed a barplot..." [arxiv:2301.10602]
- "we report the mean maximum number of waypoints reached normalized to [0, 1] indicating the policy's capability on different terrains, and the mean edge violation computed by taking the average of feet contact counts on edges." (and table headers: "Mean X-Displacement (MXD) ↑" / "Mean Edge Violation (MEV) ↓") [arxiv:2309.14341]
- "We also measured the survival rate, i.e., the percentage of the robot's survival time within 30 minutes of a random walk." [arxiv:2301.10602]
- "The primary measure of agent performance was how well the robot scored in the matches against the human players." [arxiv:2408.03906]

**Why it works**: Naming the metric, abbreviating, and indicating the desired direction lets the reader interpret every subsequent number without re-reading. The ↑/↓ glyph in headers is a reviewer-friendly hand-rail.

---

### B2. Tasks are introduced with a count, a list, and a difficulty rationale
**Pattern**: Tasks are introduced as a SET, not individually. Form: "We test on N tasks: A, B, C, D. These tasks span [axis 1] and [axis 2], with [feature]." When tasks vary in difficulty, the paper explicitly names which is hardest and why.

**Evidence**:
- "We define a comprehensive set of evaluation tasks in each environment that covers various axes of generalization, such as visual (unseen backgrounds, distractor objects, colors/appearances of objects); motion (unseen object positions/orientations); physical (unseen object sizes/shapes); and semantic (unseen target objects, instructions, and concepts from the Internet) generalization." [arxiv:2406.09246]
- "Manually segmenting the dataset into 7 non-mutually exclusive categories — Fast, Normal speed, Slow, Topspin, No spin, Underspin, Lob." [arxiv:2408.03906]
- "The success rates across tasks vary due to how the robot interacts with its environment. Opening Door (Push) has a high success rate as it's less affected by environmental factors... However, Opening Door (Pull) and Opening Fridge are more challenging. These tasks reduce the available space as they progress, especially in narrow areas, leading to lower success rates despite significant progress." [arxiv:2312.06639]

**Why it works**: Listing tasks along *axes of variation* (visual / motion / physical / semantic) tells the reader the evaluation is principled. Naming the hardest task and explaining why it's hardest gives the reader an a-priori expectation that protects against later "but you only did easy tasks" critiques.

---

### B3. Sim-vs-real distinction is announced once, then re-tagged in every subsection
**Pattern**: Papers that evaluate in both sim and real almost always introduce the distinction in the opening anchor sentence, then re-tag with "in simulation" / "in the real world" / "in the lab" / "in a real apartment" throughout. They rarely interleave sim and real numbers in the same sentence without explicit labels.

**Evidence**:
- "We evaluated our method on Daily Mobile Manipulation Task Suite both in simulation and in the real world. We deployed the policy (learned in simulation) in a real apartment with multiple rooms without any adaptation or fine-tuning." [arxiv:2312.06639]
- DreamWaQ marks sub-headings "B. Simulation" and "C. Real-World Experimental Setup" and later "In the real world, DreamWaQ's policy is robust against unstructured terrains." [arxiv:2301.10602]
- "The difference between simulations and study comes from both sim-to-real gap as well as the difference in incoming balls. In simulations, we use a diverse set of incoming balls, but during the study, the players are competitive..." [arxiv:2408.03906]

**Why it works**: The sim/real distinction is the single most contested axis in robotics reviews. Foregrounding it once, then never letting the reader forget, builds trust and pre-empts misreading.

---

### B4. The "without any adaptation/fine-tuning/calibration" sim-to-real flex
**Pattern**: When a sim-trained policy works in the real world, papers emphasize the zero-shot nature with a participial qualifier ("without any adaptation", "without any fine-tuning", "with no modification"). This is almost always inserted INTO a sentence that already describes a positive result.

**Evidence**:
- "We deployed the policy (learned in simulation) in a real apartment with multiple rooms without any adaptation or fine-tuning." [arxiv:2312.06639]
- "Our pipeline significantly outperforms previous baselines in simulation and has successfully transferred to real-world apartments with novel layouts, without any fine-tuning." [arxiv:2312.06639]
- Table-tennis paper notes "This step proved crucial for achieving high sim-to-real zero-shot transfer." [arxiv:2408.03906]

**Why it works**: The zero-shot tag converts a single number into a stronger claim ("look, no hands"). Embedded inside an existing claim it costs no extra real estate.

---

### B5. Hardware and compute specs land in a dedicated "Experimental Setup" or "Real-World Experimental Setup" sub-paragraph
**Pattern**: Specific hardware details (robot model, sensor model, control frequency, GPU model) live in a single dense paragraph rather than scattered through. Stock structure: robot name → core sensors → control rates → onboard compute → training compute.

**Evidence**:
- "We use the Unitree A1 robot with 12 joints. When standing, height of the thigh joint is 26cm and body length is 40cm. For exteroception, we use the Intel RealSense D435 inside the head of the robot which captures images at 10 ± 2Hz. We run both depth backbone (10Hz) and the base policy (50Hz) on the Jetson NX and communicate via UDP... The deployable policy can be trained on a single 3090 GPU in less than 20 hours." [arxiv:2309.14341]
- "Real-world experiments were conducted using a Unitree A1 [26] robot. All estimation and control processes were run on an Intel NUC mounted on top of the robot... During inference, the policy runs synchronously with the CENet at 50 Hz. The desired joint angles were tracked using a PD controller with proportional and derivative gains of Kp = 28 and Kd = 0.7, respectively at 200 Hz." [arxiv:2301.10602]
- "Both platforms have been extensively used in prior works for evaluating generalist robot policies [1, 2, 5, 7]." [arxiv:2406.09246] (this is the reuse-of-known-setup variant — leverages prior baselines to dodge setup description)

**Why it works**: Compactness saves words and is also a credibility signal — "we know what gear and frequencies matter." The "X hours on Y GPU" sentence is appreciated by reviewers checking reproducibility.

---

## C. Main-result reporting prose

### C1. Table/figure references include the headline number in the same sentence
**Pattern**: A main-result table is introduced with a one-sentence pointer that ALSO names the most important takeaway, not just "Table 2 shows results." Form: "Table/Fig. X reports [metric] across [conditions]; [our method] [verb] [comparator] by [number] / on [N tasks]."

**Evidence**:
- "Table I shows that H ARMONIC MM makes 32.2% more progress towards completing the task at each step compared to the baselines on Cleaning Table, 113.4% on Opening Door (Push), and 27.6% on Opening Door (Pull)." [arxiv:2312.06639]
- "We find that our method outperforms the baselines in terms of both metrics." (followed by Table 2 which is referenced from the prior sentence's "Tab. 2") [arxiv:2309.14341]
- "The results are summarized in Fig. 3 for BridgeData V2 evaluations and Fig. 4 for Google robot evaluations (per-task breakdown in Appendix, Table 4 and Table 6). We find that both RT-1-X and Octo struggle on the tested tasks, often failing to manipulate the correct object..." [arxiv:2406.09246]
- "Fig. 3 compares the learning curves of DreamWaQ against those of all the other methods for learning the locomotion policy of a Unitree A1 robot. It can be seen that even though EstimatorNet initially has a higher mean episodic reward than AdaptationNet, its performance plummets after more iterations because it encounters more difficult terrains..." [arxiv:2301.10602]

**Why it works**: Stating the headline number in the same sentence as the table reference primes the reader before they parse the table — most reviewers will only glance at one number per table, and the prose has already chosen which.

---

### C2. Deltas / relative numbers are preferred over raw absolutes
**Pattern**: Wins are reported as deltas over a named comparator ("outperforms X by Y%", "an absolute improvement of N pp", "Z× higher than baseline") rather than standalone numbers. When absolutes are given, they are immediately followed by a comparative clause.

**Evidence**:
- "OpenVLA performs comparably to RT-2-X on Google robot evaluations and significantly outperforms RT-2-X on BridgeData V2 evaluations despite being an order of magnitude smaller (7B vs. 55B parameters)." [arxiv:2406.09246]
- "Our results showed that the RT-1-X policy has a 50% higher success rate than the original, state-of-the-art methods contributed by different collaborating institutions, while the bigger vision-language-model-based version (RT-2-X) demonstrated ∼ 3× generalization improvements over a model trained only on data from the evaluation embodiment." [arxiv:2310.08864]
- "Comparing rows (1) and (2), we find that RT-2-X outperforms RT-2 by ∼ 3×, suggesting that incorporating data from other robots into the training improves the range of tasks that can be performed even by a robot that already has large amounts of data available." [arxiv:2310.08864]
- "there is still a significant 17.6% (37% relative) drop in success rate compared to H ARMONIC MM." [arxiv:2312.06639]
- "we find that ours has 20-80% higher success rate on the most difficult instance of each terrain." [arxiv:2309.14341]

**Why it works**: A raw number ("we get 71.3%") tells the reader nothing unless they know the prior. A delta ("16.5% better than RT-2-X") lands the claim and the context in one bite. The "absolute" vs "relative" parenthetical ("17.6% (37% relative)") is a sophisticated move that pre-empts the "but relative percentages are misleading" critique.

---

### C3. Multi-baseline wins are summarized with parallel structure
**Pattern**: When a method beats several baselines, the sentence uses parallel grammar — "outperforms A by X%, B by Y%, and C by Z%" — rather than a bulleted list. Each comparator stays adjacent to its own number.

**Evidence**:
- "H ARMONIC MM makes 32.2% more progress towards completing the task at each step compared to the baselines on Cleaning Table, 113.4% on Opening Door (Push), and 27.6% on Opening Door (Pull)." [arxiv:2312.06639]
- "outperforming closed models such as RT-2-X (55B) by 16.5% in absolute task success rate across 29 tasks and multiple robot embodiments, with 7x fewer parameters." [arxiv:2406.09246]
- DreamWaQ: "DreamWaQ is significantly more robust than all the other methods, as quantitatively verified by the high survival rate and maximum push that it can withstand." [arxiv:2301.10602]

**Why it works**: Parallel grammar makes the comparison visually scannable. A reader can stop after the first delta and still get the gist; a list would break flow.

---

### C4. The "we observe / we find that..." sentence converts a number into a claim
**Pattern**: After a table reference and a number, the next sentence almost always begins "We observe that / We find that / This indicates that / This suggests that...". This grammatical move turns the raw datum into a thesis the rest of the section defends.

**Evidence**:
- "We find that our method outperforms the baselines in terms of both metrics." [arxiv:2309.14341]
- "We find that both RT-1-X and Octo struggle on the tested tasks, often failing to manipulate the correct object, especially when distractors are present..." [arxiv:2406.09246]
- "we observed that the improvement of H ARMONIC MM over the baseline becomes larger as the initial distance to the target object increases. This trend underscores H ARMONIC MM's enhanced efficiency, particularly in tasks with longer horizons..." [arxiv:2312.06639]
- "we find that RT-2 and RT-2-X perform roughly on par (Table II, rows (1) and (2), last column). This is not unexpected, since RT-2 already generalizes well..." [arxiv:2310.08864]
- "Interestingly, we observed that H ARMONIC MM exhibited two distinct styles of pulling the door to adapt to the layout differences in each room." [arxiv:2312.06639]

**Why it works**: A bare number is a piece of evidence; a "We find" sentence is a CLAIM. Papers earn their argument by repeatedly making this transition explicit. The reader is being told what to take away from the table.

---

### C5. Variance is reported with ± and standard error / std-dev convention is stated once
**Pattern**: Numbers are usually reported as "mean ± stderr" or "mean ± std" with the convention disclosed in the table caption or once in the methods. Standalone numbers without variance are reserved for headline takeaways in the abstract.

**Evidence**:
- "Mean success ± StdErr computed across 33 rollouts per approach (see Table 8 for details)." [arxiv:2406.09246]
- "Average success rates ± StdErr are computed across 60 total rollouts per approach. See Table 6 for detailed results." [arxiv:2406.09246]
- DreamWaQ table values: "0.511 ± 0.053", "1.121 ± 0.164", and curves show "mean and standard deviation of the reward over ten different seeds" [arxiv:2301.10602]
- Extreme Parkour table entries: "0.99±0.05", "0.78±0.26" with caption explaining mean over 256 randomly spawned robots [arxiv:2309.14341]

**Why it works**: A reviewer's first question on a percentage is "across how many trials and what's the spread." Disclosing the convention once and applying it consistently is the cleanest way to ship that information.

---

### C6. Negative or par results are reported with a contextual rationale
**Pattern**: When the proposed method does not win on a particular axis, the paper explicitly says so AND provides a reason. The combination of acknowledgment + rationale is what protects the headline claim elsewhere.

**Evidence**:
- "In the large-dataset setting, the RT-1-X model does not outperform the RT-1 baseline trained on only the embodiment-specific dataset, which indicates underfitting for that model class." [arxiv:2310.08864]
- "we find that RT-2 and RT-2-X perform roughly on par (Table II, rows (1) and (2), last column). This is not unexpected, since RT-2 already generalizes well (see [9]) along these dimensions due to its VLM backbone." [arxiv:2310.08864]
- "RT-2-X achieves higher performance in semantic generalization tasks, as shown in Fig. 3, which is expected given that it uses larger-scale Internet pretraining data and is co-fine-tuned with both robot action data and Internet pretraining data to better preserve the pretraining knowledge, rather than being fine-tuned solely on robot data, like OpenVLA." [arxiv:2406.09246]
- "both versions of Diffusion Policy are competitive with or outperform the generalist policies Octo and OpenVLA on narrower single-instruction tasks like 'Put Carrot in Bowl' and 'Pour Corn into Pot', but the pretrained generalist policies perform better in more diverse fine-tuning tasks..." [arxiv:2406.09246]

**Why it works**: Acknowledging a loss with a reason ("this is expected because...") inoculates the paper against reviewers who would otherwise weaponize the loss. The candor is also a credibility signal that strengthens the wins.

---

### C7. The "X is the only/first/best across all..." rhetorical anchor
**Pattern**: Headline claims are framed with strong quantifiers — "only", "first", "best across all", "highest aggregate" — that turn a numerical lead into a categorical claim.

**Evidence**:
- "OpenVLA is the only approach that achieves at least 50% success rate across all tested tasks, suggesting that it can be a strong default option for imitation learning tasks, particularly if they involve a diverse set of language instructions." [arxiv:2406.09246]
- "Overall, we find that OpenVLA achieves the highest average performance." [arxiv:2406.09246]
- "The architecture and framework proposed in this paper leverages a combination of these skills in order to tackle the full competitive game for the first time." [arxiv:2408.03906]

**Why it works**: A "the only X that achieves Y" framing creates a sortable position that subsequent papers must beat. It's a citation-bait move that also makes the claim memorable.

---

### C8. Statistical significance, when reported, is folded into the prose, not a separate sentence
**Pattern**: When p-values are reported, they appear in parentheses inside the claim sentence, never as a stand-alone "we ran a t-test" disclosure. This treats significance as a property of the claim, not a procedural footnote.

**Evidence**:
- "players that mentioned 'downspin', 'backspin','chops', or 'underspin' (synonyms for weakness 1) in their game 2 and 3 comments were significantly more likely to have won their match (p < 0.05) and also to be of a higher skill level (p < 0.001)." [arxiv:2408.03906]
- "The significance of the improvement obtained by DreamWaQ against other methods was measured using paired t-test, as shown in Fig. 4, indicating that DreamWaQ consistently outperforms the baselines." (with figure annotation "**** indicate measurements with p-value < 10−4") [arxiv:2301.10602]

**Why it works**: Embedding (p < 0.05) inside the claim costs three characters and earns full statistical credit. It also reads as scientific rigor without slowing the narrative.

---

## D. Ablation study patterns

### D1. Ablation purpose is stated with "To understand the contribution of X / To measure the influence of Y"
**Pattern**: Ablation sub-sections open with an explicit purpose sentence using a stock formulation: "To understand the impact of...", "We perform ablations to measure the influence of...", "We ablate the necessity of...". The proposed mechanism is *named*, not vaguely gestured at.

**Evidence**:
- "Lastly, we perform ablations to measure the influence of different design decisions on the generalization capabilities of our most performant RT-2-X model, which are presented in Table II." [arxiv:2310.08864]
- "Proprioception Ablation: We ablate the necessity of proprioception information on Opening Door tasks. Proprioception information is necessary for tasks requiring precise placement of the end-effector and helpful for other tasks." (Table II caption) [arxiv:2312.06639]
- "We propose two sets of baselines to experimentally verify different parts of our system. First, we test our reward design and overall pipeline (Tab. 2)..." [arxiv:2309.14341]

**Why it works**: An ablation without a stated purpose looks like fishing. Naming what is being ablated ("design decisions on the generalization capabilities") and tying it to a specific table makes the table read as a deliberate test.

---

### D2. Ablations are typically organized as a table with rows-as-conditions and a row-comparison narration
**Pattern**: An ablation table has one row per ablated condition and the prose narrates pairwise row comparisons: "Comparing rows (A) and (B), we find...". When >3 rows, the prose typically picks 2-3 most informative pairs to discuss.

**Evidence**:
- "We note that including a short history of images significantly improves generalization performance (row (4) vs row (5)). Similarly to the conclusions in the RT-2 paper [9], Web-based pre-training of the model is critical to achieving a high performance for the large models (row (4) vs row (6)). We also note that the 55B model has significantly higher success rate in the Emergent Skills compared to the 5B model (row (2) vs row (4))..." [arxiv:2310.08864]
- "Comparing rows (1) and (2), we find that RT-2-X outperforms RT-2 by ∼ 3×, suggesting that incorporating data from other robots into the training improves the range of tasks..." [arxiv:2310.08864]
- DreamWaQ contrasts rows in Table III: "DreamWaQ is significantly more robust than all the other methods, as quantitatively verified by the high survival rate and maximum push that it can withstand." [arxiv:2301.10602]

**Why it works**: Tables with many rows are unreadable in linear order. Highlighting specific row-pair comparisons gives the reader a guided tour and makes each ablation conclusion locally provable.

---

### D3. Ablation results end with a takeaway sentence using "suggesting that / demonstrating that / underscoring..."
**Pattern**: After numbers, the closing sentence of each ablation paragraph translates the numerical result into a mechanistic claim — almost always with a "suggesting / demonstrating / indicating / showing" verb.

**Evidence**:
- "demonstrating that higher model capacity enables higher degree of transfer across robotic datasets." [arxiv:2310.08864]
- "This variation significantly reduces performance on the hold-out tasks, suggesting that transfer from the WidowX data may indeed be responsible for the additional skills that can be performed by RT-2-X with the Google Robot." [arxiv:2310.08864]
- "we find that only fine-tuning the network's last layer or freezing the vision encoder leads to poor performance, suggesting that further adaptation of the visual features to the target scene is crucial." [arxiv:2406.09246]
- "This indicates that complex tasks require simultaneous visual input for both navigation and manipulation, validating our approach of integrated navigation and manipulation." [arxiv:2312.06639]
- "underscoring the critical role of a pretrained visual encoder" [arxiv:2312.06639]

**Why it works**: Numbers don't argue; sentences do. The "X, suggesting Y" form is the bridge from datum to design lesson, which is the actual purpose of an ablation.

---

### D4. Pre-emptive negative ablations: "without X, we observe..."
**Pattern**: When a removal causes failure, papers often frame the ablation as "Without X, performance drops to N (vs. baseline M)" rather than "X improves performance by N". The negative framing makes the necessity of the component sharper.

**Evidence**:
- "No Pretrained DINOv2: 0% (success rate)" — "We substituted the DINOv2 encoder with a trainable CNN. This modification led to a significant drop in success rate and progress (Tab.IV), underscoring the critical role of a pretrained visual encoder" [arxiv:2312.06639]
- "Manip Cam Only: 0% — We had initial experiments with a single-camera setup showing a significant performance drop compared with multi-camera ones (provided in Table IV)." [arxiv:2312.06639]
- "NoInner's behavior on hurdle terrain is to walk around the obstacle instead of getting over it... It struggles especially on step terrain because there is no way to get around the obstacle and still get to the next waypoint. All it learns is a colliding and retrying behavior..." [arxiv:2309.14341]

**Why it works**: A 0% (or near-zero) row in an ablation table is the strongest possible evidence that a component is load-bearing. Highlighting it in prose is a structural move that recoups some of the credit normally given to additive baselines.

---

### D5. Ablation prose interleaves *what was changed* with *why it failed*
**Pattern**: When an ablation underperforms, the paper adds a mechanistic story for the failure — not just "X performed worse" but "X performed worse because Y." This is what differentiates an ablation from a sweep.

**Evidence**:
- "It performs poorly, likely due to the low-sample efficiency of training a large transformer with a ResNet18 encoder from scratch (following the original paper), which is unsuitable for our online RL setting. The original paper trains different low-level skills separately and uses a skill transformer for coordinating skills, which is significantly different from our task setting." [arxiv:2312.06639]
- "even though EstimatorNet initially has a higher mean episodic reward than AdaptationNet, its performance plummets after more iterations because it encounters more difficult terrains after longer training iterations." [arxiv:2301.10602]
- "Both and Mask work poorly because the noisy yaw angle leads to large drift." [arxiv:2309.14341]

**Why it works**: Mechanistic stories are what reviewers remember. "X performed worse because of the curriculum-coupling effect" travels better than "X performed worse."

---

## E. Analysis / Discussion prose moves

### E1. Number → mechanism hypothesis: "We hypothesize this is due to..."
**Pattern**: When a result is unexpected, the analysis explicitly marks the move from data to interpretation with "We hypothesize", "We attribute this to", "This is likely because". Multiple hypotheses can be enumerated.

**Evidence**:
- "We hypothesize that during the first game, the human is getting used to the novel situation they find themselves in: playing a sport against a robot, using an unfamiliar paddle, pressure from the competitive setting, and so on." [arxiv:2408.03906]
- "We hypothesize this is due to two factors. First, we had strict collision avoidance protocols built into the agent to avoid the paddle colliding into the table... Additionally, we were not able to train a single LLC that could handle a broad range of spin..." [arxiv:2408.03906]
- "We hypothesize that jointly learning and executing navigation and manipulation for mobile manipulation tasks achieves better performance than considering them disjointly." [arxiv:2312.06639]
- "which we attribute to the fact that the robotics data used in RT-2-X is much more diverse than the previously used robotics datasets." [arxiv:2310.08864]

**Why it works**: Reviewers tolerate any number if the paper has a story that explains it. Marking the explanation explicitly — instead of letting it merge with the result — converts unexpected numbers from liabilities into puzzles the paper has solved.

---

### E2. "Interestingly" / "Notably" / "Surprisingly" flags reader-worthy results
**Pattern**: Results that the authors want the reader to dwell on get a single-adverb hook at sentence start. This is rationed — usually 1–3 times in a whole experiments section.

**Evidence**:
- "Interestingly, we observed that H ARMONIC MM exhibited two distinct styles of pulling the door to adapt to the layout differences in each room." [arxiv:2312.06639]
- "Notably, OpenVLA performs comparably to RT-2-X on Google robot evaluations and significantly outperforms RT-2-X on BridgeData V2 evaluations despite being an order of magnitude smaller (7B vs. 55B parameters)." [arxiv:2406.09246]
- "Notably, 4-bit quantization results in similar performance as bfloat16 half-precision inference despite requiring less than half the amount of GPU memory." [arxiv:2406.09246]
- "When playing against beginner and intermediate skill levels, there was an intriguing trend — the robot always won the first game (see Fig. 9, Games Won (%))." [arxiv:2408.03906]

**Why it works**: A reader skimming for highlights uses these adverbs as bookmarks. Overuse devalues them; one or two per section is the sweet spot.

---

### E3. Headline summary sentence that compresses the experiments into one claim
**Pattern**: Either at the end of the Experiments section or at the beginning of the Discussion, papers include a one-sentence summary of the experimental verdict, often re-quantified: "We presented... that... demonstrating N% improvement."

**Evidence**:
- "We presented a consolidated dataset that combines data from 22 robotic embodiments collected through a collaboration between 21 institutions, demonstrating 527 skills (160266 tasks)... Our results showed that the RT-1-X policy has a 50% higher success rate than the original, state-of-the-art methods contributed by different collaborating institutions, while the bigger vision-language-model-based version (RT-2-X) demonstrated ∼ 3× generalization improvements over a model trained only on data from the evaluation embodiment." [arxiv:2310.08864]
- "In this work, we developed a simulation for complex mobile manipulation tasks... Our HARMONIC MM enables robots to solve these tasks using only RGB visual observation and proprioception of the robot through end-to-end learning. Our pipeline significantly outperforms previous baselines in simulation and has successfully transferred to real-world apartments with novel layouts, without any fine-tuning." [arxiv:2312.06639]

**Why it works**: A reader who skips experiments can still walk away with a citation-grade sentence. Reviewers also reuse this sentence when summarizing the paper to colleagues.

---

### E4. The "this suggests that X may transfer to Y" generalization move
**Pattern**: Late in the analysis, papers project from observed results to a broader claim. The verb hedge ("may", "suggests", "indicates") keeps the projection safe while still planting the flag.

**Evidence**:
- "OpenVLA is the only approach that achieves at least 50% success rate across all tested tasks, suggesting that it can be a strong default option for imitation learning tasks, particularly if they involve a diverse set of language instructions." [arxiv:2406.09246]
- "Our results suggest that co-training with data from other platforms imbues the RT-2-X controller with additional skills for the platform that are not present in that platform's original dataset." [arxiv:2310.08864]
- "incorporating action chunking and temporal smoothing, as implemented in Diffusion Policy, may help OpenVLA attain the same level of dexterity and may be a promising direction for future work (see Section 6 for a detailed discussion of current limitations)." [arxiv:2406.09246]

**Why it works**: The hedge ("may", "suggests") makes the projection plausible without committing to a stronger claim that future work might falsify.

---

### E5. "Confirming our hypothesis" / "Validating our approach" closes the loop with the intro
**Pattern**: Mid-experiments, papers tie a specific result back to a hypothesis or claim made in the introduction or method section. This is a structural move that rewards a reader who has been tracking the thesis since page 1.

**Evidence**:
- "H ARMONIC MM is Efficient. Confirming our hypothesis, H ARMONIC MM not only boosts performance but also enhances efficiency." [arxiv:2312.06639]
- "This indicates that complex tasks require simultaneous visual input for both navigation and manipulation, validating our approach of integrated navigation and manipulation." [arxiv:2312.06639]
- "These emergent behaviors showcase the spatial reasoning and scene-understanding abilities of our controller." [arxiv:2312.06639]

**Why it works**: A confirm-loop closes a rhetorical contract opened in the intro and gives the paper a unified narrative arc. The reader feels the experiments were *designed*, not assembled.

---

## F. Real-world / qualitative results

### F1. Real-world results lead with a count + setting sentence
**Pattern**: Real-world subsections begin with one sentence describing where and how many trials happened, then dive into qualitative observations. Numbers come second.

**Evidence**:
- "Our learned policies were evaluated in a real apartment for Opening Door (Pull), Opening Door (Push), and Cleaning Table tasks, showing promising outcomes as in Table III and Fig. 4." [arxiv:2312.06639]
- "Our controller successfully pulled the door fully open in 9 out of 15 attempts in three different rooms." [arxiv:2312.06639]
- "For the cleaning table task, we placed the table in four different locations across two rooms, with evenly distributed paper pieces on it for the robot to clean... Out of 12 trials, our controller successfully cleaned 66.6% of the table's surface area in eight instances." [arxiv:2312.06639]
- DreamWaQ: "We deployed the robot on two challenging outdoor courses to demonstrate the robustness of DreamWaQ. Course A was an on-campus yard consisting of many slopes and deformable terrains. Course B was an on-campus hill with an elevation gain of up to 22 m. Courses A and B have a total length of 430 m and 465 m, respectively." [arxiv:2301.10602]

**Why it works**: Real-world results inherently have small N; framing them as "N out of M attempts in K locations" front-loads the credibility (real-world setting, multiple sites) before the percentage that follows.

---

### F2. Behavioral observations are narrated as a sequence of agent actions
**Pattern**: Qualitative results — what the robot did and why it impressed — are written as a step-by-step narrative of agent behavior, often in present tense with strong action verbs. The robot is the protagonist.

**Evidence**:
- "As the robot approaches the obstacle the stride length reduces and the robot aligns its front feet and rear feet at the correct distance from the obstacle. Next, it kicks out its rear feet with high torque and velocity to propel itself upwards. Simultaneously, it extends its front feet to clear the top of the obstacle. As soon as the front feet touch the top of the obstacle, it uses them to pull itself up. Next, it tucks its rear legs close to the body so they are able to clear the object boundary and then finally shifts to a stable walking pose." [arxiv:2309.14341]
- "When there was enough open space around the door, it continued pulling until the door was fully opened, as shown in the 1st row in Fig. 4. However, when the door was located next to a wall, the agent first pulled the door to start the opening process and then switched to pushing to fully open it (2nd row, Fig. 4). These emergent behaviors showcase the spatial reasoning and scene-understanding abilities of our controller." [arxiv:2312.06639]
- "In Fig. 6(a), the robot exhibits different gaits for going downstairs and upstairs. When going downstairs, the robot tends to tilt its body closer to the ground and maintain its front foot far from the body, which is a key gait pattern for quickly finding a stable foothold." [arxiv:2301.10602]

**Why it works**: A blow-by-blow narrative tags the robot as an *agent with strategy*, not a policy that emits actions. It gives the reader something to picture and to point to in a presentation.

---

### F3. Failure modes are described concretely, often with operative cause
**Pattern**: Failure modes are catalogued in a numbered or comma-separated list, each tied to a specific operating regime where the policy fails and a brief operative cause.

**Evidence**:
- "we identified several weaknesses in the robot's capabilities, most notably (1) difficulty dealing with large amounts of underspin, (2) very fast balls, (3) very low balls due to a hard-coded constraint that prevented the paddle from getting too close to the table, and (4) that the robot was physically unable to reach balls that landed very close to the net." [arxiv:2408.03906]
- "the robot missed many underspin serves... Additionally, we were not able to train a single LLC that could handle a broad range of spin, and in a serve, there is a higher chance of getting high spin compared to rallying." [arxiv:2408.03906]
- "The Opening Fridge task is not evaluated since the magnetic seal of the fridge is too strong for our robot to pull. To compensate for the simulation's simplified magnetic gripper grasping, a heuristic function for doorknob grasping was implemented in the real world..." [arxiv:2312.06639]

**Why it works**: Concrete failure modes are *information*; they tell the reader exactly the operating boundary. Reviewers rarely punish acknowledged failures; they punish denied ones.

---

### F4. Emergent / unscripted behaviors are flagged as a distinct class of evidence
**Pattern**: When the policy does something the authors did not explicitly reward or program, papers tag it as "emergent" and report it with a separate paragraph. This is a signal that the method generalizes beyond its training signal.

**Evidence**:
- "Our simple reward functions impose no priors and the robot is free to learn emergent behaviors that would be impossible to heuristically define. We illustrate three such examples in Fig. 4, 5, 6." (followed by sub-subsections "4.2.1 High jump", "4.2.2 Long jump", "4.2.3 Handstand") [arxiv:2309.14341]
- "These emergent behaviors showcase the spatial reasoning and scene-understanding abilities of our controller." [arxiv:2312.06639]
- "even recovering from mistakes such as insecurely grasping objects (see https://openvla.github.io for qualitative rollout examples)." [arxiv:2406.09246]

**Why it works**: Emergent behavior is the most compelling form of qualitative result — it shows the policy has internalized something general. Naming the class explicitly lets readers cite it and lets future papers measure against it.

---

## Cross-cutting observations (initial draft)

- **The "We find / We observe" backbone**: The Experiments section is structurally a chain of "we find that..." sentences. Each major result, each ablation, each surprise is wrapped in this construction. It is the prose form of a labeled finding.
- **Numbers always have a comparator**: Almost no number stands alone — it is either a delta, paired with a baseline, or labelled with a target (e.g., "0% success without DINOv2"). Standalone absolutes are reserved for headline summary sentences.
- **Tables and figures are referenced *before* being narrated**: Stock form is "Table X reports Y. We find Z." The reference comes first; the prose then directs reader gaze.
- **Sim/real and trained/zero-shot are the two axes papers most often re-tag** because they are the two axes reviewers most often question.
- **Failure-mode catalogues are short** (3–5 items) and structured by *operating regime*, not by component. The reader leaves with a map, not a list.
- **Ablations always close with a "suggesting / underscoring / validating" sentence**: numbers don't argue; sentences do.

## Sample size (initial)
5 papers fully analyzed (RT-X [arxiv:2310.08864], DreamWaQ [arxiv:2301.10602], Extreme Parkour [arxiv:2309.14341], Table Tennis [arxiv:2408.03906], Harmonic MM [arxiv:2312.06639]) + partial OpenVLA [arxiv:2406.09246]. Final corpus target: 15 papers. This file will be expanded as the remaining papers are read.
