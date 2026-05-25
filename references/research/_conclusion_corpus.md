

========== CoRL_2306.14447.txt ==========

--- [display] Conclusion and Limitations ---
5   Conclusion and Limitations

RoboCook demonstrates its effectiveness, robustness, and generalizability in elasto-plastic object
manipulation with a general-purpose robotic arm and everyday tools. The main contributions of
RoboCook include (1) tool-aware GNNs to model long-horizon soft body dynamics accurately
and efficiently, (2) a tool selection module combined with dynamics models to learn tool functions
through self-exploratory trials, and (3) a self-supervised policy learning framework to improve the
performance and speed significantly. RoboCook pioneers solutions for tool usage and long-horizon
elasto-plastic object manipulation in building a generic cooking robot.
One limitation of RoboCook is the occasional failure of dough sticking to the tool. A solution is to
design an automatic error correction system. RoboCook also relies on human priors of tool action
spaces to simplify planning. But these simplifications do not constrain generalization as they can be
easily specified for new tools. Section 6.4.1 provides more justifications for this. Another limitation
is that humans define the subgoals. Higher-level temporal abstraction and task-level planning are
required to get rid of them. Finally, RoboCook requires additional topology estimation to apply to
cables and cloths [56], which is beyond the focus of this work.


========== CoRL_2307.01928.txt ==========

--- [display] Discussion ---
6 Discussion
Summary: We propose KNOWNO, a framework that applies conformal prediction (CP) to address the
problem of uncertainty alignment for language-instructed robots, which we formalize as providing statistical
guarantees of task completion while minimizing human help. Experiments across a variety of simulated
and hardware setups demonstrate that KNOWNO achieves user-specified task completion levels consistently
while reducing human help by 10−24% compared to baseline approaches that lack formal assurances.
Limitations and future work: The primary limitation of our work is that the task completion guarantee
assumes environments (objects) are fully grounded in the text input to the LLM, and the actions proposed
by the LLM planner can be executed successfully. In the future, we are looking to incorporate uncertainty
of the perception module (e.g., vision-language model) and the low-level action policy (e.g., language-
conditioned affordance prediction) into the CP calibration. Another limitation is that, for the task guarantee
to hold, the human needs to faithfully provide help when the robot needs it. Future work could also
incorporate human modeling/error in the conformal prediction framework. Another exciting direction is to
combine our methods with active preference learning [56, 57, 58, 59] to generate open-ended queries that
maximally reduce uncertainty about human preferences. On the theoretical front, modifying CP to optimize
different metrics for human help (e.g., minimizing human intervention rate by maximizing number of
singleton sets) would be of practical interest. Overall, we hope that the work presented here spurs further
efforts towards uncertainty alignment for safe and reliable language-instructed robots.


========== CoRL_2308.07931.txt ==========

--- [display] Conclusion ---
6   Conclusion
We have illustrated a way to combine 2D visual priors with 3D geometry to achieve open-ended
scene understanding for few-shot and language-guided robot manipulation. Without fine-tuning,
Distilled Feature Fields enable out-of-the-box generalization over variations in object categories,
material, and poses. When the features are sourced from vision-language models, distilled feature
fields offer language-guidance at various levels of semantic granularity.
Limitations. Our system takes 1m 40s to collect 50 images of the scene, and 90s to model the
NeRF and feature field. This highlights the need to develop generalizable NeRFs that can recover
geometry quickly with just a few views [9, 43], opening the possibility for closed-loop dynamic ma-
nipulation. More generally, novel view synthesis is a generative process not too different from image
generation with GANs [52] and diffusion models [53]. These alternatives, to which our philosophy
equally applies, hold promise for solving general-purpose visual and geometric understanding.


========== CoRL_2406.09246.txt ==========

--- [display] Discussion and Limitations ---
6   Discussion and Limitations
In this work, we presented OpenVLA, a state-of-the-art, open-source vision-language-action model
that obtains strong performance for cross-embodiment robot control out-of-the-box. We also demon-
strated that OpenVLA can be easily adapted to new robot setups via parameter-efficient fine-tuning
techniques.
The current OpenVLA model has several limitations. First, it currently only supports single-image
observations. In reality, real-world robot setups are heterogeneous, with a wide range of possible
sensory inputs [5]. Expanding OpenVLA to support multiple image and proprioceptive inputs as well
as observation history is an important avenue for future work. Exploring the use of VLMs pretrained
on interleaved image and text data may facilitate such flexible-input VLA fine-tuning.
Secondly, improving the inference throughput of OpenVLA is critical to enable VLA control for
high-frequency control setups such as ALOHA [90], which runs at 50Hz. This will also enable
testing VLAs on more dexterous, bi-manual manipulation tasks than what we investigated in this
work. Exploring the use of action chunking or alternative inference-time optimization techniques
such as speculative decoding [91] offer potential remedies.
Additionally, there is room for further performance improvements. While OpenVLA outperforms
prior generalist policies, it does not yet offer very high reliability on the tested tasks, typically
achieving <90% success rate.
Finally, due to compute limitations, many VLA design questions remain underexplored: What
effect does the size of the base VLM have on VLA performance? Does co-training on robot action
prediction data and Internet-scale vision-language data substantially improve VLA performance?
What visual features are best-suited for VLA models? We hope that the release of the OpenVLA
model and codebase will enable the community to jointly investigate these questions.


========== CoRL_2406.20083.txt ==========

--- [display] Discussion ---
5   Discussion
Limitations: Training RL agents for long-horizon tasks with a large search space requires extensive
compute and demands careful reward shaping. While we believe P OLI F ORMER is capable of scaling
to other tasks, it requires crafting new reward models for novel tasks such as manipulation. More
discussion on limitations in App. E. Conclusion: In this paper we provide a recipe for scaling RL for
long-horizon navigation tasks. Our model, P OLI F ORMER, achieves SoTA results on four simulation
benchmarks and two real-world benchmarks across two different embodiments. We also show that
P OLI F ORMER has remarkable potential for use in downstream everyday tasks.


========== CoRL_2407.01812.txt ==========

--- [display] Conclusion ---
6    Conclusion

This paper studies the leveraging of symmetries in visuomotor policy learning. We propose the novel
Equivariant Diffusion Policy method and provide a theoretical analysis identifying the conditions
under which diffusion processes are equivariant. We also demonstrate a general framework for
using SO(2)-equivariance in the 6DoF control for robotic manipulation. We evaluate our method in
both simulation and the real world and show in both cases that our method outperforms the baseline
Diffusion Policy by a large margin.
One limitation of this work is the partial utilization of the power of equivariance due to the symmetry
mismatch in the vision system. Even with the voxel input, Factors like the arm’s occasional presence
in the voxel grid and camera noise could break symmetry. Future work could address this by design-
ing a vision system free of symmetry corruption. Additionally, “incorrect equivariance”, as shown in
prior work [57], may harm performance when the model’s symmetry conflicts with the demonstra-
tion. Another limitation is that although the theory in Section 4.2 is not limited to diffusion policies
and can apply to other policy learning pipelines as well, this is not demonstrated. Specifically, given
the good performance of BC RNN with the relative pose control in Table 1, experimenting with an
equivariant version of BC RNN could be beneficial. Finally, extending our method to other robotic
tasks like navigation, locomotion, and mobile manipulation is a key future direction.


========== CoRL_2408.14037.txt ==========

--- [display] Limitations and Future Work ---
5            Limitations and Future Work
    In this work we present Re-Mix, a method for automatically curating robotics datasets using distri-
    butionally robust optimization. We find that Re-Mix is able generate dataset mixes that outperform
    both uniform and human-curated weights on the challenging RT-X data mix, even when subsetting
    datasets to 25% of their original scale.
    Evaluation. While we train on large, diverse robot datasets, the need for real world trials makes it
    difficult to exhaustively evaluate trained generalist policies on many robot embodiments and setups.
    While our evaluations capture two widely used robot arms from prior works [4, 7, 25], WidowX
    and Franka, future work should extend to more embodiments, perhaps via simulated environments
    [68].
    Abnormal Action Distributions. We have noticed that Re-Mix upweights datasets with abnormal
    action distributions such as the Toto dataset. While resulting data mixes performed well, such up-
    weighting is not necessarily desirable. We hope to achieve less sensitivity to such irregularities in
    future work.
    Computational Cost. Using our pre-computed weights can significantly reduce the compute re-
    quired to train generalist policies. However, our approach for computing Re-Mix weights requires
    training policies on the full data twice, once for the reference model and once for Group DRO
    optimization. Future work can instead strive to curate datasets “on-the-fly”within one run.
    Scaling Up. While we have demonstrated improvements on two large datasets, Bridge V2 and RT-
    X, scaling up to even larger ones such as the entire OpenX dataset [7] (>2M episodes) is an exciting
    extension.


========== CoRL_2505.03729.txt ==========

--- [display] Conclusion ---
6     Conclusion

We introduced V IDEO M IMIC, a real-to-sim-to-real pipeline that converts everyday human videos
into environment-conditioned control policies for humanoids. The system (i) reconstructs humans
and surrounding geometry from monocular clips, (ii) retargets the motion to a kinematically feasible
humanoid, and (iii) uses the recovered scene as task terrain for dynamics-aware RL. The result
is a single policy that delivers robust, repeatable contextual control—e.g., stair ascents/descents
and chair sit-stand—all driven only by the environment geometry and a root direction command.
V IDEO M IMIC offers a scalable path for teaching humanoids contextual skills directly from videos.
We expect future work to extend the system to richer human–environment interactions, multi-modal
sensor-based context learning, and multi-agent behavior modeling, among other directions.


                                                    8

--- [display] Limitations ---
7   Limitations

Our pipeline delivers encouraging real-world results, yet several practical weaknesses remain.
Reconstruction. Monocular 4D human–scene recovery is still brittle in the wild. Camera pose
drift in MegaSaM often yields duplicate “ghost” layers of the same surface. Due to its inability to re-
fine the dynamic points, the dynamic points from the person are mistakenly fused into the static point
cloud or inaccurately placed (e.g., feet buried beneath the environment). In particular, we found that
MegaSaM performs poorly on images with low texture. Depth filtering and spatio-temporal subsam-
pling remove many outlier points, but aggressive thresholds leave holes that hinder meshing. NKSR
mitigates noise, yet may oversmooth fine geometry (e.g., narrow stair treads); such high-frequency
details are crucial for robot control, and we discard videos where these details are missing after re-
construction. Also, during point-to-mesh conversion, spiky artifacts may appear due to stray points.
Retargeting. The kinematic optimizer assumes every reference pose can be made feasible once
scaled to the robot. In cluttered scenes, this is not always true, and conflicting costs—strict
foot-contact matching versus collision avoidance—can trap the solver in poor local minima that
the RL controller must subsequently “clean up.”
Sensing and policy input. At test time, the controller receives only proprioception and an 11 × 11
LiDAR height-map. This coarse grid is adequate for terrain and chairs but lacks the resolution
for precise contacts, manipulation, or reasoning about overhanging obstacles. Incorporating richer
perceptual inputs—such as RGB-D data or learned occupancy grids—would likely broaden the
method’s applicability and improve its semantic understanding of the environment.
Simulation fidelity. We assume the scene can be represented as a single rigid mesh. Scaling to
articulated or deformable objects will require more expressive simulators and object-level recon-
struction pipelines—open problems for future work.
Data scale and motion quality. The distilled policy is trained on only 123 video clips and occa-
sionally relies on recovery behaviors, leading to jerky motions. Larger, more diverse video corpora
and iterative real-world fine-tuning should improve smoothness and robustness.
Moving beyond these limitations—through better dynamic static separation, hole-resistant meshing,
adaptive retargeting costs, richer perception, and larger datasets—is a key direction for future work.


========== CoRL_2505.20829.txt ==========

--- [display] Conclusion ---
5     Conclusion
We propose a unified force-position control policy for legged robots, enabling contact-rich loco-
manipulation tasks without explicit force sensors. Using reinforcement learning, our policy esti-
mates external forces from historical states and compensates for them through position and velocity
adjustments. This approach supports diverse behaviors like position tracking, force application, and
compliance. Additionally, integrating force estimation into imitation learning improves task suc-
cess in contact-rich environments. Experiments on quadrupedal and humanoid robots validate the
policy’s adaptability and robustness in real-world scenarios.


                                                   8

--- [display] Limitations and Future Work ---
6   Limitations and Future Work

First, while the policy successfully estimates external forces without direct force sensing, its ac-
curacy tends to degrade in high-frequency interactions and at the edges of the robot’s workspace.
Future work could focus on improving force estimation in these corner cases. One possible direction
is to incorporate velocity and acceleration terms from Eq. (2) to enhance force estimation, allowing
the model to better capture dynamic interactions.
Second, while our policy generalizes well from simulation to real-world deployment, discrepancies
remain due to the sim-to-real gap, particularly in force accuracy along different coordinate axes.
These differences likely stem from mismatches in actuator dynamics and contact modeling between
simulation and real hardware. Future work could explore techniques such as domain randomization
and real-to-sim corrections to improve robustness across varying real-world conditions.
Additionally, our current framework primarily focuses on estimating force at a single interaction
point. Future work could explore multi-point force estimation and whole-body force interaction
tasks. For example, in scenarios such as a quadrupedal robot opening a heavy door, the robot could
use its body to brace against the door while simultaneously using its manipulator to press down on
the handle. Developing policies that coordinate multiple contact forces across different body parts
could enable more complex and effective real-world interactions.


========== CoRL_2509.01746.txt ==========

--- [display] Conclusion ---
7    Conclusion

This work addresses the problem of learning from failures in long-horizon manipulation tasks using
learned skill effect models. We propose generating additional, targeted simulation datasets based on
observed failures to fine-tune the pre-trained skill effect model. We formalize the task as a probabilistic
inference problem that maximizes the information gain of the datasets while ensuring the datasets
remain close to the observed failure. To solve it, we introduce Fail2Progress, an approach that leverages
SVI to approximate multi-modal posterior distributions. Through experiments, we demonstrate that
Fail2Progress can generate failure-driven simulation datasets to improve the skill effect model more
effectively and efficiently compared to six baselines. Furthermore, we deploy Fail2Progress on a mobile
manipulator, showcasing its ability to perform diverse real-world tasks, such as packing groceries,
packing a constrained shelf, and organizing a table.


                                                        8

--- [display] Limitations ---
8   Limitations

Our approach has several limitations. First, although Fail2Progress significantly improves performance,
it still falls short of perfect reliability, achieving around an 80% success rate in the real world shown in
Fig. 3a. This is because, even after fine-tuning, some scenarios remain out-of-distribution, leading to
incorrect symbolic predictions. Indeed, one can think of the results presented in this paper as ”1-shot”
Fail2Progress and that further refinement on the observed failures would lead to higher future success
rates. To continuously improve the performance as a lifelong learning system, the framework needs to
be deployed in a real environment over several days, where we allow Fail2Progress to update as needed
when failures are detected and classified as being caused by incorrect symbol predictions. Safely
deploying Fail2Progress in such open environments remains an open research question. Furthermore,
our framework needs to be evaluated under more diverse conditions, including more complex and
dexterous manipulation tasks involving varied objects, such as deformable objects and liquids.
Second, we do not investigate correcting for failures caused by the Sim2Real gap in this work. The
Sim2Real gap could potentially be mitigated by methods that explicitly address this challenge [6, 7, 8].
Showing how to integrate Sim2Real improvements alongside symbolic prediction failures is an
important next step.
Third, we rely on Real2Sim to classify failures and generate high-quality fine-tuning datasets. Though
our experiments show that our Real2Sim solution is effective in classifying failures and improving
model performance, our Real2Sim itself is not perfect, especially when modeling complex object
geometries and deformable objects.
Fourth, our failure classification scheme, which includes two categories, does not explicitly reason about
the environmental disturbances caused by other agents (human users or other robots). It additionally
does not account for hardware breaking or changing over time (e.g., cable or belt stretch in a robot arm
drivetrain), which might occur over long deployment times. Hypothesizing these scenarios as failure
causes is also an interesting future direction.
Fifth, we consider only object poses as the simulation state. Incorporating additional simulation states,
such as object friction and center of mass [33], into our framework would be a possible next step.
Sixth, we assume a fixed set of relations. While our large-scale experiments show that these relations
are sufficient, there are always relations outside the predefined set. Discovering new relations [65, 66]
during robot exploration could enhance the open-world planning capability of our framework.
Finally, although we demonstrate mobile manipulation in diverse environments, extending the system
to building-wide open spaces [67] remains an open research question. To achieve this, our method
could integrate with scene graph construction and online updating [68, 69, 70, 71].


========== ICRA_2309.14341.txt ==========

--- [display] Discussion ---
5   Discussion
In this work, we show how an end-to-end data-driven approach can scale to the challenging task of
precise and extreme parkour, even on a robot with imprecise sensing and actuation. This is possible
because of unified and general reward structure that allows emergent behavior. While our robot is
an expert at moving around in the world, it should also be able to manipulate objects. A promising
direction for future research is to extend this same basic approach for mobile manipulators.


========== ICRA_2402.13442.txt ==========

--- [display] DISCUSSION ---
VI. DISCUSSION
tend to either avoid making changes or make huge changes to
the canvas, whereas CoFRIDA makes updates that are more             Limitations and Ethical Considerations CoFRIDA
reasonable for the robot to achieve and integrate naturally      stands out as a successful collaborative painting system,
with prior work.                                                 but is limited to discrete turn-taking interactions. While
                                                                 our self-supervised training data creation method (Fig. 4)
C. Text Conditioned Paintings                                    was informed by real co-painting data, a more end-to-end
   FRIDA’s text-to-painting method relies on feedback            approach where the system learns how to form the partial
through CLIP which results in noisy, unclear imagery. We         paintings could result in even better results.
                                        No Fine-Tuning                                                                     CoFRIDA
   Generated
    Simulated




                 Details too small to    Cannot represent           Too complex to            In CoFRIDA, images are generated such that when they are painted,
                  represent with the      face with robot’s      represent with robot’s      there is little loss in meaning. The image generating model learns the
                 robot’s large brush     fixed color palette          stroke limit            robot’s constraints and abilities during Self-Supervised Fine-Tuning.

Fig. 8. Learning Robotic Constraints. We compare images generated by a pre-trained Stable Diffusion model (left) to those generated by our proposed
CoFRIDA module (right) with the prompt “A dog and a cat sitting next to each other on the beach” in three different painting settings (Sec.IV-B). The
top row shows the images generated by each of the models and the bottom row shows the corresponding FRIDA simulation.

                   Large Brush          4 Fixed Paint Colors   35 Sharpie Strokes
                                                                                          indicates that CoFRIDA’s fine-tuning technique is not solely
                                                                                          changing the low-level appearance (akin to style-transfer)
                                                                                          over the output of its base model. It appears that CoFRIDA
FRIDA




                                                                                          is learning the robot’s abilities, as seen in Fig. 8 where
                                                                                          CoFRIDA’s Co-Painting Module produces images with (1)
                                                                                          very prominent and clear content, when the robot’s brush is
CoFRIDA (Ours)




                                                                                          large (2) select and limited colors, when the robot paints with
                                                                                          fixed palettes or markers, and (3) sparse, concise drawings
                                                                                          when the number of strokes is limited.

--- [display] CONCLUSIONS ---
VII. CONCLUSIONS
Fig. 9.    Comparing CoFRIDA’s fine-tuned pre-trained image generator                        An end-to-end approach, like FRIDA, that optimizes the
versus FRIDA’s CLIP-guided method for generating paintings from the text                  brush strokes towards the text goal tends to produce noisy
“A sad, frog ballerina doing an arabesque” in three painting settings.                    looking paintings that only loosely resemble the text because
                                                                                          it operates in a low-level space without a global context.
   In light of recent discoveries of harmful content in the                               Additionally, it is hard to incorporate interactivity beyond an
LAION dataset, we have inspected the subset of data used                                  initial input. We present Collaborative FRIDA (CoFRIDA),
to fine-tune the models used in this paper and have not                                   a hierarchical approach for interactive human-robot co-
found harmful content. We have changed the code to use                                    painting where semantic planning via pre-trained models
the COCO dataset [36] and have not seen a degradation in                                  happens in a high-level, pixel space before being transferred
the quality of results. CoFRIDA is subject to the biases of                               to a low-level brush stroke planner. Pre-trained models do
Stable Diffusion [21] and its training data [37], and so we                               not immediately provide the requirements for co-painting,
recommend the usage of CoFRIDA with caution and solely                                    as they do not know the capabilities of the robot. Whereas
for research purposes.                                                                    the Real2Sim2Real methodology improves low-level action-
   Learning Robotic Abilities Our self-supervised fine-                                   space planning in FRIDA, the proposed self-supervised fine-
tuning procedure guided the pre-trained model to generate                                 tuning procedure provides a method for adapting powerful
images that, at a pixel-level, appeared similar to what FRIDA                             pre-trained models for high-level robotic planning. CoFRIDA
can paint, but is it learning the actual robot constraints or just                        uses this hierarchical approach for reducing the Sim2Real
a low-level style transfer? We computed the Sim2Real gap                                  gap, achieving enhanced performance over the baselines.
measurements between the LAION images and their FRIDA
simulations (as seen in Fig. 4) along with the CLIPScore of                                                  VIII. ACKNOWLEDGMENTS
the simulation and text prompt. We found that ∆pix had                                      This work was partly supported by NSF IIS-2112633, the
a small, insignificant Pearson correlation (−0.08, 0.08 p-                                Packard Fellowship, and the Technology Innovation Program
value) with the CLIPScore of the painting whereas ∆sem                                    (20018295, Meta-human: a virtual cooperation platform for
had a significant, negative correlation (−0.48, 2.4e − 31 p-                              a specialized industrial services) funded By the Ministry of
value). Because CoFRIDA gre
[...truncated...]


========== Science_Robotics_2201.08117.txt ==========

--- [display] DISCUSSION ---
3. DISCUSSION
                                                                            4. MATERIALS AND METHODS
We have presented a fast and robust quadrupedal locomotion controller
for challenging terrain. The controller seamlessly integrates extero-       Overview
ceptive and proprioceptive input. Exteroceptive perception enables          We train a neural network policy in simulation and then perform zero-
the robot to traverse the environment quickly and gracefully by antic-      shot sim-to-real transfer. Our method consists of three stages, illus-
ipating the terrain and adapting its gait accordingly before contact is     trated in Figure 6.
made. When exteroceptive perception is misleading, incomplete, or               First, a teacher policy is trained with RL to follow a random target
missing altogether, the controller smoothly transitions to proprioceptive   velocity over randomly generated terrain with random disturbances.
 Research Article                                                                                                        ETH Zurich and Intel   9




   A soft obstacle                                                         B transparent obstacle




   C sensor uncovered                                                      D sensor covered




   E slippery step




   a                           b                            c                           d                            e




                                              b       c
                                   a                                 d                   e




Fig. 4. Internal belief state inspection during perceptive failure using a learned belief decoder. Red dots indicate height samples given as input
to the policy. Blue dots show the controller’s internal estimate of the terrain profile. (A) After stepping on a soft obstacle that cannot support a
foothold, the policy correctly revises its estimate of the terrain profile downwards. (B) A transparent obstacle is correctly incorporated into the
terrain profile after contact is made. (C) With operational sensors, the robot swiftly and gracefully climbs the stairs, with no spurious contacts.
(D) When the robot is blinded by covering the sensors, the policy can no longer anticipate the terrain but remains robust and successfully tra-
verses the stairs. (E) When stepping onto a slippery platform, the policy identifies low friction and compensates for the induced pose estimation
drift. The graph shows a decoded friction coefficient.
 Research Article                                                                                                                          ETH Zurich and Intel   10



                    1. Teacher policy training

                                                                                              Teacher Policy                     Action
                    Environment
                                                                     Command
                                                                     Proprioception                              MLP

                                                                     Height scan
                                                                                       exteroceptive
                                                                                       encoder                              joint diﬀerence
                                                                  
[...truncated...]


========== Science_Robotics_2303.03381.txt ==========

--- [display] Discussion ---
Discussion

We present a learning-based controller for full-sized humanoid locomotion. Our controller is
a causal transformer that takes the history of past observations and actions as input and pre-

dicts future actions. We train our model using large-scale simulation and deploy it to the real
world in a zero-shot fashion. We show that our policy enables reliable outdoor walking with-
out falls, is robust to external disturbances, can traverse different terrains, and carry payloads

of varying mass. Our policy exhibits natural walking behaviors, including following different
commands, high-speed locomotion, and an emergent arm swing motion. Moreover, we find
that our controller can adapt to novel scenarios at test time by changing its behavior based on

context, including gait changes based on the terrain and recovery from foot-trapping.



                                                 14
Limitations. Our approach shows promising results in terms of adaptability and robustness
to different terrains and external disturbances. However, it still has some limitations that need

to be addressed in future work. One limitation is that our policy is not perfectly symmetrical, as
the motors on two sides do not produce identical trajectories. This results in a slight asymmetry
in movement, with the controller being better at lateral movements to the left compared to the

right. Additionally, our policy is not perfect at tracking the commanded velocity. Finally, under
excessive external disturbances, like a very strong pull of a cable attached to the robot, can
cause the robot to fall.


Possible extensions.       Our neural network controller is a general transformer model. Com-
pared to alternate model choices, like TCN and LSTM, this has favorable properties that can be

explored in future work. For example, it should be easier to scale with additional data and com-
pute (46) and enable us to incorporate additional input modalities (47). Analogous to fields like
vision (48) and language (49), we believe that transformers may facilitate our future progress in

scaling learning approaches for real-world humanoid locomotion.


Materials and Methods

This section describes in detail the policy learning procedure, the simulation process, the sim-
to-real transfer deployment, and the analysis of the transformer-based controller. An overview

of our method is shown in Figure 7. The policy learning includes two steps: teacher state policy
training and student observation policy learning. We adopt a massively parallel simulation en-
vironment, where we introduce a simulation method that can simulate closed kinematic chains

enabling us to simulate the underactuated Digit humanoid robot. We explain the procedure for
sim-to-real transfer in detail. Finally, we provide analysis of our transformer policy.




                                                15
Policy learning

Problem formulation.         We formulate the control problem as a Markov Decision Process
(MDP), which provides a mathematical framework for modeling discrete-time decision-making

processes. The MDP comprises the following elements: a state space S, an action space A, a
transition function P (st+1 |st , at ) that determines the probability of transitioning from state st
to st+1 after taking action at at time step t, and a scalar reward function R(st+1 |st , at ), which

assigns a scalar value to each state-action-state transition, serving as feedback to the agent on
the quality 
[...truncated...]


========== Science_Robotics_2304.13653.txt ==========

--- [display] Discussion ---
Discussion

Comparison to Robot Learning Literature

Reinforcement learning for robots has been studied for decades (see [6, 5] for an overview), but has
only recently gained more popularity due to the development of better hardware and algorithms
[4, 37]. In particular, high-quality quadrupedal robots have become widely available, which have
been used to demonstrate robust, efficient, and practical locomotion in a variety of environments
[12, 38, 13, 39]. For example, Lee et al. [12] applied zero-shot sim-to-real deep RL to deploy
learned locomotion policies in natural environments, including mud, snow, vegetation, and streaming
water. Our work similarly relies on zero-shot sim-to-real transfer and model randomization, but
instead focuses on a range of dynamic motions, stability, long horizon tasks, object manipulation, and
multi-agent competitive play. Indeed, the vast majority of recent work in this area relies on some
form of sim-to-real transfer [40, 15, 27, 41, 17, 19, 14, 17, 42], which can help to reduce the safety
and data efficiency concerns associated with training directly on hardware. A common theme is that
a surprisingly small number of techniques can be sufficient to reduce the sim-to-real gap[37, 43],
which is also supported by our results. However, there have also been successful attempts at training
legged robots to walk with deep RL directly on hardware [44, 45, 46, 47, 48]. Training on hardware
can lead to better performance, but the range of behaviors that can be learned has so far been limited
due to safety and data efficiency concerns. Similar to our work, prior work has shown that learned
gaits can achieve higher velocities compared to scripted gaits [49, 50, 51]. However, the gaits have
been specifically trained to attain high speeds, instead of emerging as a result of optimizing for a
higher level goal.
    Quadrupedal platforms constitute the majority of legged locomotion research, but an increasing
number of works consider bipedal platforms. Recent works have produced behaviors including walking
and running [24, 25], stair climbing [26], and jumping [27]. Most recent works have focused on
high-quality, full-sized bipeds and humanoids, with a much smaller number [52, 53, 54, 48] targeting
more basic platforms whose simpler and less precise actuators and sensors pose additional challenges
in terms of sim-to-real transfer. Additionally, there is a growing interest in whole body control, that is,
tasks in which the whole body is used in flexible ways to interact with the environment. Examples
include getting-up from the ground [55] and manipulation of objects with legs [23, 56]. Recently,
reinforcement learning has been applied to learn simple soccer skills, including goalkeeping [21],
ball manipulation [19, 18], and shooting [20]. These works focus on a narrower set of skills than the
1v1 soccer game, and the quadrupedal platform is inherently more stable and therefore presents an
easier learning challenge.


Comparison to RoboCup

Robot soccer has been a longstanding grand challenge for AI and robotics, since at least the formation
of the RoboCup competition [30, 29] in 1996, and it has also inspired our 1v1 soccer task. The OP3
robot has been used for the humanoid RoboCup league, but our environment and task are substantially
simpler than the full RoboCup problem. The main differences are that we focused on 1v1 soccer
instead of multi-player teams; our environment does not align with the field or ball specific
[...truncated...]

--- [display] Limitations ---
Limitations

Our work provides a step towards practical use of deep RL for agile control of humanoid robots in
a dynamic multi-agent setting. However, there are several topics that could be addressed further.
First, our learning pipeline relies on some domain-specific knowledge and domain randomization,
as is common in the robot learning literature [12, 37, 6, 5, 43]. Domain-specific knowledge is used
for reward function design and for training the get-up skill, which requires access to hand-designed
key poses, which can be difficult or impractical to choose for more dynamic platforms. In addition,
the distillation step assumes we can manually choose the correct skill (either get-up or soccer) for
each state, although a method in which the distillation target is automatically selected has been
demonstrated in prior work [11], which we anticipate would work in this application. Second, we
do not leverage real data for transfer; instead, our approach relies solely on sim-to-real transfer.
Fine-tuning on real robots or mixing in real data during training in simulation could help improve
transfer and enable an even wider spectrum of stable behaviors. Third, we applied our method to a
small robot and did not consider additional challenges that would be associated with a larger form
factor.
    Our current system could be improved in a number of ways. We found that tracking a ball with
motion capture was particularly challenging: detection of the reflective tape markers is sensitive to
the angle at which they face the motion capture cameras; only the markers on the upper hemisphere
of the ball can be registered; and the walls of the soccer pitch can occlude the markers, especially
near the corners. We believe moving away from motion capture is an important avenue for future
work and discuss potential avenues for this in Future Work. We also found that the performance
of the robots degraded quickly over time, mainly due to the hip joints becoming loose or the joint
position encoders becoming miscalibrated; thus we needed to regularly perform robot maintenance
routines. Further, our control stack was not optimized for speed. Our nominal control time step was
25 ms, but in practice the agent often failed to produce an action within that time. The time step was
selected as a compromise between speed and consistency, but we believe that a higher control rate
would result in improved performance. Finally, we did not model the servo motors in simulation, but
instead approximated them with ideal actuators that can produce the exact torque requested by a
position feedback controller. As a consequence, for example, we found that the agent’s behaviors are
very sensitive to the battery charge level, limiting the operation time per charge to 5 to 10 minutes in


                                                                                                         12
                    Learning Agile Soccer Skills for a Bipedal Robot with Deep Reinforcement Learning13



practice.
    On the training side, we found our self-play setup sometimes resulted in unstable learning. A
population-based training scheme [11] could have improved stability and led to better multi-agent
performance. Second, our method includes several auxiliary reward terms, some of which are needed
for improved transfer (for example, upright reward and knee torque penalty), and some for better
exploration (for example, forward speed). We chose to use a weighted average of the differ
[...truncated...]

--- [inline] Future Work ---
Future Work

Multi-agent Soccer: An exciting direction of future work would be to train teams of two or more
agents. It is straightforward to apply our proposed method to train agents in this setting. In our
preliminary experiments for 2v2 soccer, we saw that the agent learned division of labor, a simple form
of collaboration: if its teammate was closer to the ball, the agent did not approach the ball. However,
it also learned less agile behaviors. Insights from prior work in simulation [11] could be applied to
improve performance in this setting.
    Playing Soccer from Raw Vision: Another important direction for future work is learning
from on-board sensors only, without external state information from a motion capture system. In
comparison to state-based agents that have direct access to the ball, goal, and opponent locations,
vision-based agents need to infer information from a limited history of high-dimensional egocentric
camera observations, and integrate the partial state information over time, which makes the problem
significantly harder [73].
    As a first step, we investigated how to train vision-based agents that only use onboard RGB camera
and proprioception. We created a visual rendering of our lab using a Neural Radiance Field (NeRF)
model [74] based on the approach introduced by Byravan et al. [75]. The robot learned behaviors
including ball tracking and situational awareness of the opponent and goal. See Suppl. Playing Soccer
from Raw Vision for our preliminary results with this approach.


Materials and Methods

Environment

We trained the agent in simulation in a custom soccer environment and then transferred to a cor-
responding real environment as shown in Figure 1. The simulation environment uses the MuJoCo
physics engine [76] and is based on the DeepMind Control Suite [77]. The environment consists of a
soccer pitch that is 5 m long by 4 m wide, and two goals that each have an opening width of 0.8 m. In
both the simulated and real environments, the pitch is bordered by ramps, which ensures that the
ball returns to the bounds of the pitch. The real pitch is covered with rubber floor tiles to reduce the
risk of falls damaging the robots and to increase the ground friction.
    The agent acts at 40 Hz. The action is 20-dimensional and corresponds to the joint position set
points of the robot. The actions are clipped to a manually selected range (see Suppl. Environment
Details) and passed through an exponential action filter to remove high frequency components:
𝒖𝑡 = 0.8𝒖𝑡 −1 + 0.2𝒂𝑡 , where 𝒖𝑡 is the filtered control applied to the robot at time step 𝑡 , and 𝒂𝑡 is the
action output by the policy. The filtered actions are fed to PID controllers that then drive the joints
(torques in simulation and voltages on the real robot) to attain the desired positions.
    The agent’s observations consist of proprioception and game state information. The proprioception


                                                                                                          13
                    Learning Agile Soccer Skills for a Bipedal Robot with Deep Reinforcement Learning14



consists of joint positions, linear acceleration, angular velocity, gravity direction, and the state of the
exponential action filter. The game state information, obtained via a motion capture setup in the real
environment, consists of the agent’s velocity, ball location and velocity, opponent location and velocity,
and location of the two goals, whic
[...truncated...]


========== Science_Robotics_2306.11706.txt ==========

--- [inline] Future work ---
Future work could look into enabling flexible and multi-modal task specification. Incorporating relevant
existing, freely-available datasets with language annotations would be a first good step. Task specification
via language offers complementary benefits to visual goals, and different tasks may be better specified by
either modality. In addition, while this work focused on visual goal-conditioning and VFM baselines, which
may be able to reason well over images; language-conditioning and LLM/VLM baselines may offer better
temporal reasoning capabilities.

Another research avenue could explore improving both training and fine-tuning capabilities of such a model
with reinforcement learning (RL), since RoboCat in its current form only employs behaviour cloning. While
visual goal specification already allows the agent to learn from failures and sub-optimal data, incorporating
RL would enable both learning with rewards and learning online with real-world interaction. Finally, while
RoboCat aims to tackle behavioural diversity in manipulation tasks, the different embodiments are all in a
controlled lab setting with visually-similar backgrounds. We hope that next-generation foundation agents
will demonstrate robustness to different basket textures and operate in more visually-diverse environments
in the wild.




                                                       20
Published in Transactions on Machine Learning Research (12/2023)




Broader Impact
This work presents progress on training generalist agents for robotic manipulation. Our work presents a
recipe, and first steps, in an emerging area, with experiments in a controlled lab environment demonstrating
promising but imperfect performance. Nonetheless, the potential impact on society from generalist robotic
agents calls for increased interdisciplinary research into their risks and benefits. Thus, we discuss the broader
impact of this line of research, beyond the specific contributions of this paper. To provide an easily accessible


========== Science_Robotics_2309.01918.txt ==========

--- [display] Discussion and Limitations ---
6    Discussion and Limitations

We developed a framework for sample-efficient and generalizable multi-task robot manipulation in
the real world. Our framework is based on rapidly multiplying a small robotics dataset through se-
mantic scene augmentations, and training a multi-task language-conditioned policy that can ingest
the diverse multi-modal data obtained through augmentations. We combine and adapt several de-
sign choices like action chunking and temporal aggregation proposed in the context of single-task
policies, and show that they yield significant boosts in performance even in the multi-task settings
we consider.
Finally, we release one of the largest robot manipulation datasets to date involving over 12 skills in
kitchen environments which we hope will facilitate further research in developing robot manipula-
tion systems with diverse real-world generalization. An important limitation of our work is that all
the tasks consist of individual skills, and an interesting direction for future work would be to develop
approaches for composing skills automatically for solving long-horizon tasks. Another limitation
is that we do not explore the axes of language generalization, and use language embeddings from
pre-trained encoders as is, without any modifications. Future work could investigate better language
conditioning that is more flexibly adaptable to changes in task descriptions.


========== Science_Robotics_2410.21845.txt ==========

--- [display] Discussion ---
6. Discussion
The presented results substantially advance the published state-of-the-art in robotic manipulation. Our
research demonstrates that with the right design choices, model-free RL can actually effectively tackle a
variety of complex manipulation tasks using perception inputs, directly training in the real world within a
practical timeframe. Trained policies from this approach are highly performant, achieving nearly perfect
success rates that substantially exceed those of alternative approaches, such as imitation learning, along
with cycle times that are also considerably faster.
     Beyond the results themselves, the approach presented in this work can have significant broader impact.
It can serve as a general framework for acquiring a wide range of manipulation skills with high performance
and adapt to variations. This is particularly valuable in High-Mix Low-Volume (HMLV) manufacturing,
or “make-to-order" production (Jina et al., 1997; Shah and Ward, 2003; Gan et al., 2023). Such production
methods have substantial potential in major industries such as electronics, semiconductors, automotive, and
aerospace due to their need for shorter product life cycles, customization, agility, and flexibility.
     We see a number of opportunities for future work. First, our approach can serve as an effective tool for
generating high-quality data to train robot foundation models (Brohan et al., 2023b;a; Collaboration et al.,
2024; Team et al., 2024; Kim et al., 2024). Given that each task requires a relatively short time to train and
the training process is largely autonomous, this framework can be employed to develop a variety of skills.
Subsequently, data can be collected by executing the converged policies, which can then be distilled into
these generalist models. Second, although the current training time is relatively short, each task still requires
training from scratch. We can further reduce this time by pretraining a value function that encapsulates
the general manipulation capabilities of solving a range of different tasks with distinct robot embodiments.
This pretrained value function can then be quickly fine-tuned to address specific tasks.
     We also see some limitations of our approach. Although we successfully address a variety of challenging
tasks, it remains uncertain whether this method can be further extended to tasks with significantly longer
horizons, where the sample complexity issue becomes more pronounced. However, this challenge might be
alleviated through improved pretraining techniques or by employing methods that automatically segment a
long-horizon task into a series of shorter sub-tasks, such as a vision-language model. It’s also important to
note that we did not perform extensive randomization in our experiments, nor did we test the method’s
generalization capability in unstructured environments. The primary focus of this paper is to demonstrate
that the approach can be general-purpose in acquiring a wide range of manipulation skills with high
performance. We believe that the randomization issue could be addressed by extending the training duration
of the policies with the desired randomization level as in Luo et al. (2021). Additionally, the generalization
issue might be resolved by incorporating vision foundation models that are pretrained on large-scale diverse
datasets.
     We hope this work will pave the way for the use of reinforcement learning in solving robotic manipulation
problems, achieving hig
[...truncated...]