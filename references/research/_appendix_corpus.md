

========== CoRL_2308.07931.txt ==========
Appendix
    A.1    Neural Radiance Fields (NeRFs)

    Neural radiance fields [12] model a scene as a 6D, vector-valued continuous function that maps from
    a position x = (x, y, z) and a normalized viewing direction d = (dx , dy , dz ), to the differential
    density σ and emitted color (r, g, b). In practice, this is achieved via two neural networks which
    partially share parameters: 1) the density network σ(x) which depends only on the position x; and
    2) the color network c(x, d) which depends on both the position x and viewing direction d.

    Novel-View Synthesis. NeRF synthesizes an image by casting a ray r from the camera origin o
    through the center of each pixel. Points along the ray are parameterized as rt = o + td, where t is
    the distance of the point to the camera origin o. The color C(r) of the ray r between the near and
    far scene bounds tn and tf is given by the volume rendering integral [54]
                            Z tf                                       Z t           
                   C(r) =         T (t)σ(rt )c(rt , d) dt, T (t) = exp −     σ(rs ) ds ,            (5)
                             tn                                             tn

    where T (t) is the accumulated transmittance along the ray from rtn to rt .

    Modeling a Scene with NeRFs. For a scene, we are given a dataset of N RGB images {I}N            i=1
    with camera poses {T}N   i=1 . At each iteration, we sample a batch of rays R ∼ {T} N
                                                                                        i=1 and optimize
    σ and c by minimizing the photometric loss Lrgb = r∈R ∥ Ĉ(r) − I(r)∥22 , where I(r) is the RGB
                                                           P

    value of the pixel corresponding to ray r ∈ R, and Ĉ(r) is the color estimated by the model using a
    discrete approximation of Equation 5 [12, 55].

    A.2    Dense 2D Feature Extraction via MaskCLIP

    We provide pseudo code for the MaskCLIP method [11] for extracting dense, patch-level features
    from the CLIP model [1] below. Algorithm 1 is the computation graph of the last layer of vanilla
    CLIP. Algorithm 2 is MaskCLIP’s modified graph. Note that the two linear transformations via Wv
    and Wout can be fused into a single convolution operation. We provide our feature extraction code
    in our GitHub repository (https://github.com/f3rm/f3rm).


    Algorithm 1 Image Feature (Original)                      Algorithm 2 Dense Features (MaskCLIP 11)
1   def forward(x):
2     q, k, v = W_qkv @ self.ln_1(x)                      1   def forward(x):
3     v = (q[:1] * k).softmax(dim=-1) * v                 2     v = W_v @ self.ln_1(x)
4     x = x + W_out @ v                                   3     z = W_out @ v
5     x = x + self.mlp(self.ln_2(x))                      4     return z[1:] # all but the CLS token
6     return x[:1]    # the CLS token


    A.3    Feature Fields

    Implementation Details. Memory for caching the 2D feature map is a significant system bottle-
    neck that does not appear with RGB reconstruction because high-dimensional features, up-scaled to
    the RGB image resolution, can grow to more than 40 GB for a standard NeRF dataset. We solve
    this issue by reconstructing patch-level feature maps without up-scaling them to pixel resolution.
    We speed up our feature distillation by building off newer NeRF implementations using hierarchical
    hash grids [8] based on Nerfacto [10].

    Feature Field Quality. F3RM benefits from neural feature fields’ ability to reconstruct detailed
    3D geometry. We offer such an example in Figure A8. Notice the difference in resolution, between
    the source 2D feature map (middle), and the final feature field.


                                                     14
                    (a) RGB Image                     (b) Raw DINO ViT Feat.                              (c) Distilled Feat.
Figure A8: Level of Detail. (a) Mesh strainer and whisk. (b) Raw feature map from DINO ViT,
very low in resolution. Colors correspond to PCA of the features. (c) 3D feature fields recover a
higher level of detail than the source 2D feature maps. Inset corresponds to (b) in its original size
for comparison.

                 (a) CLIP Feature Mean Squared Error                                      (b) DINO Feature Mean Squared Error
      0.27                                          MLP Head                                                                 MLP Head
                                                    Hash Grid                  0.18                                          Hash Grid
      0.26
                                                                               0.17
MSE




                                                                         MSE



      0.25                                                                     0.16

      0.24                                                                     0.15
             0        2000    4000          6000   8000     10000                     0        2000    4000          6000   8000     10000
                                     Step                                                                     Step
Figure A9: Feature Error During Feature Distillation. The mean squared error on a held-out
set of feature maps for (a) CLIP and (b) DINO using the MLP head and hash grid architectures
described in Section A.3.1. The hash grid architecture consistently achieves a lower error.


A.3.1             Ablation on Feature Field Architecture

We implement our feature field as a hierarchical hash grid [8] that takes a 3D position x as input, and
outputs the feature vector. We compare this against a MLP head that takes the intermediate features
output by NeRF as input, which is similar to the architectures in [5, 6]. We first train a NeRF on
images collected by the robot of a t
[...continues...]


========== CoRL_2401.02117.txt ==========
A. Appendix
A.1. High Five



                                                                                                                            Kitchen island


                               init.                                  #1                                   #2
 High Five: The robot base is initialized next to the kitchen island. The robot keeps moving around the kitchen island until a human is in front of
 it, then high five with the human. Each demo has 2000 steps or 40 seconds, and typically contains 3-4 high fives.

                                               Figure 6: Task Definition of High Five.

We include the illustration for the High Five task in Figure 6. The robot needs to go around the kitchen
island, and whenever a human approach it from the front, stop moving and high five with the human. After
the high five, the robot should continue moving only when the human moves out of its path. We collect data
wearing different clothes and evaluate the trained policy on unseen persons and unseen attires. While this
task does not require a lot of precision, it highlights Mobile ALOHA’s potential for studying human-robot
interactions.
A.2. Example Image Observations
Figure 7 showcases example images of Wipe Wine captured during data collection. The images, arranged
sequentially in time from top to bottom, are sourced from three different camera angles from left to right
columns: the top egocentric camera, the left wrist camera, and the right wrist camera. The top camera
is stationary with respect to the robot frame. In contrast, the wrist cameras are attached to the arms,
providing close-up views of the gripper in action. All cameras are set with a fixed focal length and feature
auto-exposure to adapt to varying light conditions. These cameras stream at a resolution of 480 × 640 and a
frame rate of 30 frames per second.




Figure 7: Example Image Observations of Wipe Wine. We show the observations from the top camera, left wrist
camera and right wrist camera from left to right columns. These images are arranged sequentially in time from top to
bottom.




                                                                           18
                            Mobile ALOHA: https://mobile-aloha.github.io

A.3. Experiment Details and Hyperparameters of ACT, Diffusion Policy and VINN
We carefully tune the baselines and include the hyperparameters for the baselines and co-training in
Table 5, 6, 7, 8, 9.

                        sample prob. from Mobile ALOHA data                     0.5
                        sample prob. from ALOHA data                            0.5

                                Table 5: Hyperparameters of co-training.


                     learning rate                          2e-5
                     batch size                             16
                     # encoder layers                       4
                     # decoder layers                       7
                     feedforward dimension                  3200
                     hidden dimension                       512
                     # heads                                8
                     chunk size                             45
                     beta                                   10
                     dropout                                0.1
                     backbone                               pretrained ResNet18[40]

                                    Table 6: Hyperparameters of ACT.


       learning rate                    1e-4
       batch size                       32
       chunk size                       64
       scheduler                        DDIM[85]
       train and test diffusion steps   50, 10
       ema power                        0.75
       backbone                         pretrained ResNet18[40]
       noise predictor                  UNet[73]
                                        RandomCrop(ratio=0.95) &
       image augmentation               ColorJitter(brightness=0.3, contrast=0.4, saturation=0.5) &
                                        RandomRotation(degrees=[-5.0, 5.0])

                              Table 7: Hyperparameters of Diffusion Policy.


                                    learning rate                3e-4
                                    batch size                   128
                                    epochs                       100
                                    momentum                     0.9
                                    weight decay                 1.5e-6

                    Table 8: Hyperparameters of BYOL, the feature extractor of VINN.


                k (nearest neighbour)                 selected with lowest validation loss
                chunk size                            100
                state weight                          5
                camera feature weight                 1:1:1 (for front, left and right wrist)

                             Table 9: Hyperparameters of VINN + Chunking.




                                                    19
                              Mobile ALOHA: https://mobile-aloha.github.io

A.4. Open-Loop Replaying Errors
Figure 8 shows the spread of end-effector error at the end of replaying a 300 steps (6s) demonstration. The
demonstration contains a 180 degree turn with radius of roughly 1m. At the end of the trajectory, the right
arm would reach out to a piece of paper on the table and tap it gently. The tapping position are then marked
on the paper. The red cross denotes the original tapping position, and the red dots are 20 replays of the
same trajectory. We observe significant error when replaying the base velocity profile, which is expected
due to the stochasticity of the ground contact and low-level controller. Specifically, all replay points are
biased to the left side by roughly 10cm, and spread along a line of roughly 20cm. We found our policy to be
capable of correcting such errors without explicit localiz
[...continues...]


========== CoRL_2406.09246.txt ==========
Appendix B. All evaluations in this and the following sections are conducted as A/B evaluations,
using the same tasks with the same sets of initial robot and object states, to ensure fair comparison.
Comparisons. We compare OpenVLA’s performance to three prior generalist manipulation policies:
RT-1-X [1], RT-2-X [1], and Octo [5]. RT-1-X (35M parameters) and Octo (93M parameters) are
transformer policies trained from scratch on subsets of the OpenX dataset; Octo is the state-of-the-art
model among open-source manipulation policies. RT-2-X (55B parameters) is a state-of-the-art,
closed-source VLA that leverages Internet-pretrained vision and language backbones.
The results are summarized in Fig. 3 for BridgeData V2 evaluations and Fig. 4 for Google robot
evaluations (per-task breakdown in Appendix, Table 4 and Table 6). We find that both RT-1-X and
Octo struggle on the tested tasks, often failing to manipulate the correct object, especially when
distractors are present, and in some cases causing the robot to wave its arm around aimlessly. Note
that our evaluations test even larger degrees of generalization than the evaluations performed in
those prior works to challenge the Internet-pretrained VLA models. Thus, lower performance of
models without Internet pretraining is expected. RT-2-X clearly outperforms both RT-1-X and Octo,
demonstrating the benefits of large, pretrained VLMs for robotics.
Notably, OpenVLA performs comparably to RT-
2-X on Google robot evaluations and signifi-                           78.3
                                                                            85.0                       88.0
                                                                                                                          82.9 82.9
cantly outperforms RT-2-X on BridgeData V2                                                      72.0

evaluations despite being an order of magni-
                                                                                         44.0
tude smaller (7B vs. 55B parameters). Qual-                  33.3
                                                                  26.7             32.0                        34.3

itatively, we find that both RT-2-X and Open-                                                                        14.3
VLA exhibit markedly more robust behaviors
than the other tested models, such as approach-
                                                                                 (Tasks & conditions seen in   (Unseen objects, tasks,
ing the correct object when distractor objects                                          training data)        backgrounds, & concepts)

are present, properly orienting the robot’s end-
effector to align with the orientation of the
target object, and even recovering from mis-                                                                 Move Coke Can
                                                                                 Pick Coke Can               to Taylor Swift
takes such as insecurely grasping objects (see
https://openvla.github.io for qualitative Figure 4: Google robot evaluation results. We evaluate
rollout examples). RT-2-X achieves higher per- generalist robot policies on in-distribution and out-of-
formance in semantic generalization tasks, as distribution (OOD) tasks on the mobile manipulator used
shown in Fig. 3, which is expected given that in RT-1 and RT-2 evaluations [2, 7]. We find that Open-
                                                       VLA and RT-2-X attain comparable performance and
it uses larger-scale Internet pretraining data and significantly outperform RT-1-X and Octo overall. Aver-
is co-fine-tuned with both robot action data and age success rates ± StdErr are computed across 60 total
Internet pretraining data to better preserve the rollouts per approach. See Table 6 for detailed results.
pretraining knowledge, rather than being fine-
tuned solely on robot data, like OpenVLA. However, OpenVLA performs comparably or better in
all other task categories in both BridgeData V2 and Google robot evaluations. The performance
difference can be attributed to a combination of factors: we curated a much larger training dataset
for OpenVLA with 970k trajectories (vs. 350k for RT-2-X); we performed more careful cleaning of
the training dataset and, e.g., filtered out all-zero actions in the Bridge dataset (see Appendix C for a
detailed discussion); and OpenVLA uses a fused vision encoder that combines pretrained semantic
and spatial features. See Appendix D for ablation analyses of these components.
5.2 Data-Efficient Adaptation to New Robot Setups
While prior works mainly focused on directly evaluating VLAs “out-of-the-box” [1, 7, 16], effective
fine-tuning of VLA models to new tasks and robot setups is largely unexplored, yet is key for their
widespread adoption. In this section, we investigate OpenVLA’s ability to be quickly adapted to a
new real-world robot setup. (See Appendix E for fine-tuning experiments in simulation.)
Robot setups and tasks. We test a simple fine-tuning recipe for the OpenVLA model: full fine-
tuning of all model parameters, using small datasets with 10–150 demonstrations of a target task (see
Fig. 5; we explore parameter-efficient fine-tuning approaches in Section 5.3). We test OpenVLA in
two setups: Franka-Tabletop, a stationary, table-mounted Franka Emika Panda 7-DoF robot arm;
and Franka-DROID, the Franka robot arm setup from the recently released DROID dataset [11],


                                                                 8
                                                                                                                                    Franka-Tabletop                                                                                                       Franka-DROID
                                                                            93.3                                                          93
[...continues...]


========== CoRL_2407.01812.txt ==========
Appendix for all environments.


shown in Figure 3, our network consists of three
main parts: encoding (white box), denoising (yel-
low box), and decoding (gray box). We implement
our network using the escnn library [50]. First, an
equivariant observation encoder and an equivariant
action encoder take inputs o and ak , respectively, to
create equivariant embeddings eo and eak . The em-
beddings will be in the form of a regular represen-
tation of the subgroup Cu ⊂ SO(2) (where u is the
number of discrete rotations in the group). The em-
beddings have shape eo ∈ Ru×do and eak ∈ Ru×da ,
where each of the do or da dimensional vectors en-
codes the features for a specific group element (i.e.,
a rotation angle). Second, in the denoising step, let
ego ∈ Rdo and egak ∈ Rda be a pair of partial em-
beddings corresponding to the same group element
g. We process each pair with a 1D Temporal U-Net
(adopted from the prior works [15, 1]) to calculate
an equivariant noise embedding. Specifically, letting
k be the denoising step, U the U-Net, and z its out- Figure 3: Overview of our Equivariant Dif-
put, we have z g = U (ego , egak , k). Since the same fusion Policy architecture.
network is applied for all g ∈ Cu , the output is an equivariant embedding of the noise in the regular
representation. Finally, an equivariant decoder will decode the noise εk . See Appendix D for details.

5         Experiments
5.1        Simulation Experiment

Experimental Settings We first evaluate our Equivariant Diffusion Policy (EquiDiff) with either
image (Im) or voxel (Vo) input on 12 manipulation tasks from MimicGen [11] (Figure 4). We define
the rotation of the observation as a voxel grid rotation or an image rotation. Notice that in the image
version of our method, there is a mismatch between the rotation of the agent view image and the
rotation of the ground truth state since the agent view is not orthogonally top-down. Although top-
down observations could be captured, we use the observation settings in the published dataset from
MimicGen [11] to demonstrate the generalizability of our method1 . On the other hand, the voxel
version eliminates this symmetry mismatch as the rotation of the voxel grid aligns with the rotation
of the ground truth state. To better leverage the equivariance, we also add a rotation augmentation in
the voxel version of our method following our analysis in Section 4.1-4.2. We compare our method
with the following baselines: 1) DiffPo-C: the original diffusion policy [1] trained with the 1D
Temporal UNet [15]. Notice that the baseline shares the same UNet architecture as our method, but
it does not have any equivariant structure. 2) DiffPo-T: same as above, but trained with a transformer.
3) DP3: the 3D diffusion policy [20] trained with a point net encoder. 4) ACT: the Action Chunking
      1
          Prior work [52] demonstrate that the equivariant CNN is still able to capture symmetry in such a scenario.


                                                            5
                                           Stack D1                         Stack Three D1                        Square D2                           Threading D2
Method          Ctrl   Obs       100         200        1000        100          200         1000        100         200          1000        100         200         1000

EquiDiff (Vo)          Voxel   99 (+23)    100 (+3)    100 (=)    75 (+37)     91 (+19)   91 (-3)      39 (+31)    48 (+29)   63 (+14)      39 (+22)    53 (+18)     55 (-4)
EquiDiff (Im)          RGB     93 (+17)    100 (+3)    100 (=)    55 (+17)      77 (+5)   96 (+2)      25 (+17)    41 (+22)   60 (+11)       22 (+5)     40 (+5)     59 (=)
DiffPo-C [1]           RGB        76         97         100          38           72        94             8          19         46            17          35          59
                Abs
DiffPo-T [1]           RGB        51         83          99          17           41        84             5          11         45            11          18          41
DP3 [20]               PCD        69         87          99           7           23        65             7           6         19            12          23          40
ACT [51]               RGB        35         73          96           6           37        78             6          18         49            10          21          35

EquiDiff (Vo)          Voxel   95 (+14)    100 (+5)    100 (=)    59 (+33)     76 (+24)      83 (-9)   25 (+17)    35 (+14)       52 (-7)   33 (+20)    39 (+13)     46 (-1)
EquiDiff (Im)          RGB      75 (-6)     96 (+1)    100 (=)     25 (-1)     63 (+11)      92 (=)     11 (+3)     21 (=)       48 (-11)    11 (-2)     22 (-4)     49 (+2)
                Rel
DiffPo-C [1]           RGB        81          93         99          26           52           86          6          13            37         13          26          40
BC RNN [2]             RGB        59          95        100          12           48           92          8          21            59          7          13          47

                                          Coffee D2                  Three Pc. Assembly D2                 Hammer Cleanup D1                        Mug Cleanup D1
Method          Ctrl   Obs       100         200        1000        100          200         1000        100         200          1000        100         200         1000

EquiDiff (Vo)          Voxel   65 (+18)     73 (+7)    76 (-3)    37 (+33)     58 (+52)   71 (+28)     70 (+16)     66 (-5)      73 (-14)   53 (+10)     65 (+6)     68 (+5)
EquiDiff (Im)          RGB     60 (+13)    79 (+13)    76 (-3)    15 (+11)     39 (+33)   69 (+26)     65 (+11)     63 (-8)      77 (-10)    49 (+6)     64 (+5)     67 (+2)
DiffPo-C [1]           RGB        44          66         79           4            6         30           52          59           73          43          59          65
                Abs
DiffPo-T [1]
[...continues...]


========== CoRL_2408.14037.txt ==========
Appendix A includes additional results for Bridge with 10% subsetting.

    4.5              What matters in Re-Mix?
    In this section, we ablate several design choices used in Re-Mix (see Section 3.1), including action
    discretization and early stopping. We run all ablations in the 25% subset setting (see Section 4.4),
    since subsetting further amplifies the effects of the domain weights. In Fig. 4, we first analyze the ef-
    fects of choosing a reference model checkpoint for Group DRO that is overfit to the training dataset.
    Empirically, we find that choosing a checkpoint just 50K steps after early stopping decreases perfor-
    mance by over 15% on average, likely because the reference model baseline used to determine the
    domain weights is less meaningful once it overfits. On the right half of Fig. 4, we show performance
    on Bridge when using continuous (Cont.) actions in Re-Mix instead of discrete for estimating α.
    We find that continuous actions lead to significantly worse performance, as their loss functions fail
    to fit outliers or multi-modal actions.

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



                                                                           10
Acknowledgments
Compute for this research was provided by a Google TPU Research Cloud Grant. This work was
supported by NSF #1941722, ONR project #N00014-22-1-2293, DARPA grant #W911NF2210214,
and TRI. JH is supported by an NDSEG Fellowship.

References
 [1] A. Radford, J. W. Kim, C. Hallacy, A. Ramesh, G. Goh, S. Agarwal, G. Sastry, A. Askell,
     P. Mishkin, J. Clark, et al. Learning transferable visual models from natural language supervi-
     sion. In International conference on machine learning, pages 8748–8763. PMLR, 2021.
 [2] A. Conneau, K. Khandelwal, N. Goyal, V. Chaudhary, G. Wenzek, F. Guzmán, E. Grave,
     M. Ott, L. Zettlemoyer, and V. Stoyanov. Unsupervised cross-lingual representation learning
     at scale. arXiv preprint arXiv:1911.02116, 2019.
 [3] A. Khazatsky, K. Pertsch, S. Nair, A. Balakrishna, S. Dasari, S. Karamcheti, S. Nasiriany,
     M. K. Srirama, L. Y. Chen, K. Ellis, et al. Droid: A large-scale in-the-wild robot manipulation
     dataset. arXiv preprint arXiv:2403.12945, 2024.
 [4] H. Walke, K. Black, A. Lee, M. J. Kim, M. Du, C. Zheng, T. Zhao, P. Hansen-Estruch,
     Q. Vuong, A. He, V. Myers, K. Fang, C. Finn, and S. Levine. Bridgedata v2: A dataset
     for robot learning at scale. In Conference on Robot Learning (CoRL), 2023.
 [5] H.-S. Fang, H. Fang, Z. Tang, J. Liu, J. Wang, H. Zhu, and C. Lu. Rh20t: A robotic dataset for
     learning diverse skills in one-shot. In RSS 2023 Workshop on Learning for Task and Motion
     Planning, 2023.
 [6] A. Brohan, N. Brown, J. Carbajal, Y. Chebotar, J. Dabis, C. Finn, K. Gopalakrishnan, K. Haus-
     man, A. Herzog, J. Hsu, J. Ibarz, B. Ichter, A. Irpan, T. Jackson, S. Jesmonth, N. Joshi, R. Ju-
     lian, D. Kalashnikov, Y. Kuang, I. Leal, K.-H. Lee, S. Levine, Y. Lu, U. Malla, D. Manjunath,
     I. Mordatch, O. Nachum, C. Parada, J. Peralta, E. Perez, K. Pertsch, J. Quiambao, K. Rao,
     M. Ryoo, G. Salazar, P. Sanketi, K. Sayed, J. Singh, S. Sontakke, A. Stone, C. Tan, H. Tran,
     V. Vanhoucke, S. Vega, Q. Vuong, F. Xia, T. Xiao, P. Xu, S. Xu, T. Yu, and B. Zitkovich. Rt-
     1: Robotics transformer for real-world control at scale. In arXiv preprint arXiv:2212.06817,
     2022.
 [7] Open X-Embodiment Collaboration, A. Padalkar, A. Pooley, A. Jain, A. Bewley, A. Herzog,
     A. Irpan, A. Khazatsky, A. Rai, A. Singh, A. Brohan, A. Raffin, A. Wahid, B. Burgess-
     Limerick, B. Kim, B. Schölkopf, B. Ichter, C. Lu, C. Xu, C. Finn, C. Xu, C. Chi, C. Huang,
     C. Chan, C. Pan, C. Fu, C. Devin, D. Driess, D. Pathak, D. Shah, D. Büchler, D. Kalash-
     nikov, D. Sadigh, E. Johns, F. Ceola, F. Xia, F. Stulp, G. Zhou, G. S. Sukhatme, G. Salhotra,
     G. Yan, G. Schiavi, H. Su, H.-S. Fang, H. Shi, H. B. Amor, H. I. Christensen, H. Furuta,
     H. Walke, H. Fang, I. Mordatch, I. Radosavovic, I. Leal, J. Liang, J. Kim, J. Schneider, J. Hsu,
     J. Bohg, J. Bingham, J. Wu, J. Wu, J. Luo, J. Gu, J. Tan, J. Oh, J. Malik, J. Tompson, J. Yang,
     J. J. Lim, J. Silvério, J. Han, K. Rao, K. Pertsch, K. Hausman, K. Go, K. Gopalakrishnan,
[...continues...]


========== CoRL_2509.01746.txt ==========
A    Appendix

Overview
The appendix provides additional details, experiments, and results. Please refer to the supplemental
video for real-world robot executions available at sites.google.com/view/fail2progress.
    A.1 Qualitative Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     A2
    A.2 Detailed Experimental Tasks . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        A3
    A.3 Efficiency Experiments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       A3
    A.4 Key Findings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       A3
    A.5 Ablation Study . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       A4
    A.6 Detailed Simulation Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      A4
    A.7 Detailed Sim2Real Gap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        A5
    A.8 Extra Related Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       A5
    A.9 Relations Definition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     A5
    A.10 Skills Definition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   A5
    A.11 Details of Skill Effect Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    A6
    A.12 Real-to-sim details . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     A8
    A.13 Stein Update Details . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    A8
    A.14 Detailed Generalization Experiments . . . . . . . . . . . . . . . . . . . . . . . . .       A9
    A.15 Experimental Details . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      A9
    A.16 Additional Baseline for Domain Randomization . . . . . . . . . . . . . . . . . . . A10
    A.17 Hardware Information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . A10




                                                  A1
A.1                 Qualitative Analysis



                                           …




 Hierarchical Tabletop Organization            Put capsules into the cups                  Failure     Success




                                           …




 Multi-object Transport                        Put four objects into the bag     Failure               Success




 Constrained Packing                                       Failure               Success               Success



Figure 4: Rollouts of real-world evaluations and corresponding failure cases. A detailed explanation of this figure
is provided in Sec. A.1.
   3objs (Seen)
 4objs (Unseen)
   5objs (Unseen)
 6objs (Unseen)




Figure 5: Real-world generalization visualizations. We show how Fail2Progress generalizes to different numbers
of objects (3-6), different object shapes, and different tables.

We present qualitative results in Fig. 4. Hierarchical Tabletop Organization task (First row): The
robot is tasked with organizing the cups and capsules on another table while keeping them in a row. It
first places several capsules into their corresponding cups. In the failure case, the robot fails to recognize
the correlation between cups and capsules, resulting in the wrong organization. After learning from this
failure, Fail2Progress successfully completes this task by understanding that the capsules will move
with their corresponding cups. Multi-object Transport task (Second row): The robot is tasked with
packing groceries and placing them on the table. It places all four groceries inside a bag. In the failure
case, the robot places the bag on the ground instead of the table, failing the task. After fine-tuning
the model with a targeted dataset, Fail2Progress moves the bag to the table. Constrained Packing


                                                                            A2
task (Third row): The robot is tasked with organizing a shelf by placing a stack of cups on a constrained
shelf. In the failure case, the robot fails to make all the wipes in contact to clear enough space. After
learning from the failure, Fail2Progress first pushes the wipes aside in contact to create sufficient space
for the cups, then places them on the shelf.
Furthermore, we demonstrate how our approach generalizes to different numbers and shapes of objects,
as well as different tables, in Fig. 5. Specifically, the model is fine-tuned only on failure cases with 3
objects but is able to generalize to scenarios involving 3-6 diverse objects on two tables.

A.2   Detailed Experimental Tasks

Multi-object Transport tasks the robot to transport multiple objects within a container using a single
skill (e.g., carrying multiple fruits in a grocery bag). To succeed, the robot has to understand that
all objects inside the container move together when the container is moved. Hierarchical Tabletop
Organization tasks the robot to organize a table by arranging objects into a hierarchical structure (e.g.,
multiple objects in different cups). Success requires the robot to understand the relationships between
these objects and how its skills impact future relations based on the hierarchical structure. Constrained
Packing tasks the robot to organize objects in a constrained environment (e.g., a bookshelf). Success
involves using a non-prehensile push skill to create space and then packing the remaining objects onto
the shelf. In this paper, we present quantitative results for the Multi-object Transport and Hierarchical
Tabletop Organization tasks, and qualitative results for the Constrained Packing task.

A.3   Efficiency Experiments


 We compare Fail2Progress with the two best-performing           10                      4
                                                                           SVGD
baselines, Gradient and Sampling, to assess opti-                          Gradient
                                                                 Optimization Time (s)
[...continues...]


========== ICRA_2408.03906.txt ==========
APPENDIX                                  Reza Mahjourian: Developed early hierarchical RL pol-
A. Contribution Statements                                       icy, defined the ball target skill, and built an initial version
                                                                 of the simulator.
    David B. D’Ambrosio1,∗ : Worked on all parts of the
                                                                    Sherry Moore: Contributed to a software or hardware
system over the course of many years. Developed the policy
                                                                 component that is in use today.
architecture and training approach. Conceived, wrote, and
                                                                    Kenneth Oslund: Wrote and integrated the control mid-
edited this paper. Helped run and analyze the user study.
                                                                 dleware layer, which provides a unified interface for the
    Saminda Abeyruwan1,∗ : Worked on all parts of the
                                                                 different types of robot hardware and connects the python
system over the course of many years. Developed the policy
                                                                 environment layer to the manufacturer’s C++ driver.
architecture and training approach. Conceived, wrote, and
                                                                    Anish Shankar: Worked on earlier version of the system’s
edited this paper. Helped run and analyze the user study.
    Laura Graesser1,∗ : Worked on all parts of the system        hardware and software infrastructure and system perfor-
over the course of many years. Developed the policy archi-       mance.
tecture and training approach. Conceived, wrote, and edited         Vikas Sindhwani: Initiated and developed ES research
this paper. Helped run and analyze the user study.               agenda for table tennis and catching. Supported and advised
    Atil Iscen1 : Worked on targeting policies, sim-to-real,     on an ongoing basis.
simulation modeling, results analysis. Helped run and an-           Vincent Vanhoucke: Executive support and research di-
alyze the user study.                                            rection.
    Heni Ben Amor2 : Investigated initial adapter and at-           Grace Vesom: Built the camera driver and an early ver-
tenuation models, evaluated LLCs and spin classifiers, data      sion of the ball detection pipeline. Built camera calibration
collection, general advisor, paper writing.                      software and hardened camera hardware stability.
    Alex Bewley2 : Led the design and implementation for the        Peng Xu: Robot cell design and build, prototypes for
vision system. Built components for data infrastructure and      generating data.
model training. Camera configuration analysis.                      Pannag R. Sanketi1 : Overall lead on the project
    Barney J. Reed2,† ,: Expert table tennis advisor, coaching   (Managed the project + team). Set the vision and the
engineers, human data collection. Evaluator and referee for      research direction. Coded technical components for the
user study. Feedback on robot progress and skill level.          project and wrote parts of the paper.
    Krista Reymann2 : Program Manager: organized opera-
tional support for the project; initiated and managed the user   Corresponding Authors: Saminda Abeyruwan, David
study and organized operational support during the study.        B. D’Ambrosio, Laura Graesser
    Leila Takayama2,§ : Experiment design, metrics develop-      {saminda, ddambro, lauragraesser}@google.com
ment, wrote methods section, wrote HRI related work.
                                                                 1
    Yuval Tassa2 : Contributed to modeling and system iden-        Primary contributors
                                                                 ∗
tification of both robot and ball-flight dynamics.                 Corresponding authors (order randomized, equal
    Krzysztof Choromanski: Developed Blackbox optimiza-          contributions)
                                                                 2
tion library and ES algorithms used for training table tennis      Core contributors (Alphabetized)
                                                                 †
policies over the course of many years.                            Work done at Google DeepMind via Stickman Skills
    Erwin Coumans: Helped setting up the initial physics         Center LLC
                                                                 §
simulations. Created initial virtual reality setup that allows     Work done at Google DeepMind via Hoku Labs.
to play tennis. Advise during research of simulation setup,
URDF files, constraints setup.
    Deepali Jain: Developed Blackbox optimization library
and ES algorithms used for training table tennis policies over
the course of many years.
    Navdeep Jaitly: Conceived, designed, and led the initial
stages of the project, built and sourced prototypes, founda-
tional designs of systems like control and vision. Created
initial vision pipeline and supervised algorithm development.
    Natasha Jaques: Initial brainstorming and ideation for
policy architecture design and opponent model and paper
writing.
    Satoshi Kataoka: Developed and maintained the custom
robotics module orchestration system. Initial consultation on
cameras and other infrastructure-related components.
    Yuheng Kuang: Develops and advises on data infrastruc-
ture.
    Nevena Lazic: Implemented the initial simulator and
training algorithms.
B. Simulation Details                                                 ABB axis, we define a target joint angle. This angle is set
  Table V contains the MuJoCo simulator parameters and                to -0.12 for forehands and 2.0 for backhands. The reward
Table VI
[...continues...]


========== ICRA_2410.21415.txt ==========
APPENDIX
A. Visualization of all maps
  We visualize all the large maps for evaluation in Figure 6
and all the down-scaled small maps for training in Figure 7,
which keep the obstacle patterns in the corresponding large
maps.                                                                     (a) Sortation                 (b) Warehouse




                          (a) Sortation




                                                                            (c) Paris                      (d) Berlin




                         (b) Warehouse




                                                                          (e) Random1                    (f) Random2

                                                                      Fig. 7: Small maps with 600 agents for training.

           (c) Paris                       (d) Berlin
                                                                 Also, different global guidance excels in different scenarios.
                                                                 An interesting observation is that in map Random2, Back-
                                                                 ward Dijkstra (BD) performs better with < 10, 000 agents,
                                                                 and Dynamic Guidance (DG) performs better with > 10, 000
                                                                 agents. The reason may be that with more agents, there is
                                                                 potentially more congestion, and DG addresses congestion
                                                                 better than BD.

                                                                 C. Evaluation on Learn-to-Follow Benchmark
                                                                    This section compares different decentralized methods
                                                                 on the Learn-to-Follow Benchmark [12] to validate the
         (e) Random1                      (f) Random2            superiority of our SILLM (Learnable PIBT) in Figure 9,
                                                                 as the experiment setting in the Learn-to-Follow paper is
  Fig. 6: Large maps with 10, 000 agents for evaluation.         quite different from ours. Specifically, we compare Learnable
                                                                 PIBT trained with imitation learning and with reinforcement
                                                                 learning, Follower [12], SCRIMP [10], and PIBT [5]. For
B. Evaluation with Different Numbers of Agents                   a simple comparison, we only use Backward Dijkstra as
  In this section, we compare Learnable PIBT and PIBT            global guidance. All the training settings are the same as the
with different global guidance and different numbers of          ones in the Follower paper [12]. Notably, Learnable PIBT
agents in Figure 8. The conclusions are similar to the ones in   and Follower are trained on 40 Maze maps and then tested
Section V. With the same global guidance, Learnable PIBT         on 10 different Maze maps and other types of maps. Our
consistently outperforms PIBT, proving the effect of learning.   Learnable PIBT trained with imitation learning consistently
performs the best across 4 different types of maps. Notably,     eliminate these errors, we implement an Action Dependency
Follower actually only outperforms PIBT in Mazes maps but        Graph (ADG) [33].
may fail to outperform PIBT in other maps, which means the          The video demo is available in the supplementary material.
generalization ability of Follower still needs improvement. In   From our experiment with 10 real agents, we observe that
contrast, our Learnable PIBT is much more generalizable.         agents can reach their goals quickly without collisions, and
                                                                 errors are eliminated by the ADG, demonstrating the poten-
D. Real-World Mini Example                                       tial of using our method in the real world. In our experiment
                                                                 with 100 virtual agents, we compare PIBT with Learnable
   Since during the planning process, our algorithm assumes      PIBT. We can observe that Learnable PIBT outperforms
the position of all agents to be perfectly known at all times,   PIBT with 50% more throughput.
we use ground truth positions for our virtual robots and
use external localization (here, the Optitrack Motion Capture    E. Computation Resources
System) to obtain accurate position information for our real       Our models are trained on servers with 72 vCPU AMD
robots. However, the planned path may not be executed            EPYC 9754 128-Core Processor, 4 RTX 4090D (24GB), and
accurately due to disturbances and control inaccuracies. To      240 GB memory. Training on each map takes less than 12
                                                                 hours.
                                                                 F. Baseline Methods Implementation
                                                                    1) WPPL: In Section V-A, we compare our methods
                                                                 with the winning solution of League of Robot Runner
                                                                 Competition [19], WPPL [7]. Our implementation is based
                                                                 on the public repo: https://github.com/DiligentPanda/MAPF-
                                                                 LRR2023. We remove the rotation action to align with the
                                                                 settings in other baselines. In addition, instead of limiting the
[...continues...]


========== IROS_2312.06639.txt ==========
Appendix                                            closest distance robot reached before, dcurrent is the current
                                                                                  distance between robot and target object. For all tasks, we
                                                                                  use wnav shaping = 2, Rreach target = 2, wnav = 1 .
                   VII. V ISUAL AUGMENTATION                                      Manipulation Reward Rmanip :
                                                                                                Rmanip =δwmanip shaping Rmanip shaping
   Our applied augmentations include: ColorJitter: Adjusts                                              +wprogress ∆P + γRfinish task
brightness (0.4), contrast (0.4), saturation (0.2), and hue
(0.05); GaussianBlur: Applies a blur effect with a kernel size                       Rmanip shaping =exp(−5 × dee current)
of (5,9) and sigma range of (0.1,2); RandomResizedCrop:                                               × 1000 × max(dee cloest − dee current , 0))
Resizes the input with a scale range of (0.9,1); Random-
Posterize: Reduces color depth, applied with varying bits                         The variable δ is 1 if the end effector has not reached the
(7,6,5,4) and a probability of 0.2 for each setting; Rando-                       target region, and 0 otherwise. Similarly, γ is 1 if the robot
mAdjustSharpness: Enhances or reduces the sharpness with                          completes the task at the current step, and 0 otherwise.
a factor of 2, applied with a probability of 0.5.                                    dclosest is the closest distance the end-effector reached before
                                                                                  towards the specified region of the target object, dcurrent is the
                                                                                  current distance between the end-effector and the specified
                                                                                  region of the target object, P is the task progress. For all tasks,
                 VIII. N ETWORK A RCHITECTURE                                     we use wmanip = 1, wmanip shaping = 0.02, Rfinish task = 20. For
                                                                                  opening door/fridge tasks, we use wprogress = 80. For the
                                                                                  cleaning table task, we use wprogress=100 . For opening the door
   Our RGB observations initially get processed by DinoV2                         (pull) and opening the fridge task, we provide an additional
model, generating 768 × 16 × 16 features which pooled to a                        wgrasp = 2 for grasping the door knob or the edge of the
reduced dimension of 768 × 7 × 7. The processed features are                      fridge. We consider the grasp successful if the agent has
passed through separate visual encoders. This results in two                      issued the grasp action and the distance between the end-
distinct sets of 16 × 7 × 7 latent visual features corresponding                  effector and object is smaller than 0.2m.
to each camera view. The key hyperparameters are as follows:                      Efficiency Reward Refficiency :

       Hyperparameter                               Value                                Refficiency =Rstep penalty
       RGB Input                                 384 × 224                                          +wee moved ||dee moved || + γRinvalid action
       Pretrained Visual Encoder                dinov2 vits14
       EN av                             2 Conv(1x1, 16 channels)                 where dee moved is the distance end-effector moved at the
       EM anip                           2 Conv(1x1, 16 channels)                 current step, and γ is 1 if the current action failed, and 0
       GRU                              1 GRU layer with 512 units                otherwise. Current action fails if the robot collides with seman-
       Policy(π)                            1 FC with 512 units
                                                                                  tic objects in the apartment in simulation, such as a wall or
       Value(v)                             1 FC with 512 units
       Proprioception dim                             5                           table. For all tasks, we use Rstep penalty = −0.01, wee moved =
       latent feature dim                7 ∗ 7 ∗ 16 ∗ 2 + 5 = 1573                −0.01, Rinvalid action = −0.01, wefficiency = 1
Hardware Platform: Our simulation and real-world exper-
iment are conducted with Stretch Robot [43] and we use
RealSense D455 for our RGB observation.
Future Works: In future work, we aim to enhance the
capabilities of H ARMONIC MM by integrating more complex
and dynamic tasks into our task suite. We aim to explore
the potential of H ARMONIC MM in environments with even
longer task horizons and more varied challenges.


========== IROS_2506.22827.txt ==========
Appendix A.                                                                                             limits, and degrees of freedom—a dedicated retargeting proce-
dure translates the human pose estimates into robot-compatible       involving picking a bag from a table and placing it onto
joint configurations. This retargeting procedure is outlined in      another. Only successful sequences (30 in total) are retained,
Appendix A.                                                          segmented into separate skill-specific datasets, i.e., picking and
   As a final step, the low-level tracking policy expects as input   placing, for training two policies. IL policy training employs
both joint-angle references and corresponding 3D keypoints           the demonstration data with hyperparameters specified in
representing the center-of-mass (CoM) positions of selected          Table VI. After training, we evaluated independently each skill
robot body links. To generate these keypoints, we apply              policy over 30 autonomous trials, which showed success rates
forward kinematics in simulation: we first set the robot to the      of 90% for picking and 83% for placing.
retargeted joint configuration, and then compute the spatial
coordinates of the predefined body positions. The resulting          C. Multi-Step Skill Planning and Execution Monitoring
joint angles and keypoints form the complete motion reference           While imitation-learned skills enable reliable execution
that can be directly executed by the tracking controller.            of short-term actions, real-world humanoid tasks frequently
   2) Imitation Learning Module: Building upon the estab-            require combining multiple skills into longer sequences to
lished teleoperation pipeline, we next develop the imitation         achieve complex goals. We address this by introducing a
learning (IL) module, the mid-level component responsible for        high-level planning and execution monitoring module, capable
generating autonomous motion targets from onboard sensory            of dynamically selecting and verifying the execution of skill
inputs.                                                              sequences. Our approach leverages pretrained vision-language
   While the low-level tracking policy executes externally           models (VLMs) embedded within a closed-loop planner-
provided motion references, the IL module produces these ref-        monitor architecture.
erences directly from sensory inputs, enabling robot autonomy.          To clearly distinguish conceptual terminology, we define:
Formally, the IL policy is defined as a function                         • A skill as an individual, short-duration manipulation

                          πIL : X → A,                                      capability (e.g., picking or placing an object).
                                                                         • A task as a higher-level objective involving at least
where the observation state at each timestep t is                           two skills executed sequentially that change the state of
                                    (1)    (2)                              objects in the world.
                      xt = (qt , It , It ),
                                                                        Our hierarchical system thus plans at the task-level while
comprising proprioceptive joint angles qt and binocular ego-         monitoring and executing at the skill-level.
                       (1)       (2)                                    1) Problem Formulation: Formally, a task is defined by a
centric RGB images It and It . The action space A consists
of future joint configurations q, directly interfacing with the      natural-language goal g (e.g., “Pick up the bag and place it
low-level tracking policy.                                           on the table”) and an initial visual observation o0 . The goal is
   For the IL policies, we adopt the Humanoid Imitation              to autonomously generate and reliably execute a sequence of
Transformer (HIT) [10], designed specifically for high-DoF           parameterized skills σ = [π (1) , π (2) , . . . , π (N ) ] to satisfy the
humanoids with binocular vision. It is based on the Ac-              conditions described by g.
tion Chunking Transformer (ACT) [31] model, which has                   2) System Architecture: Our high-level planning and mon-
demonstrated improved robotic control by predicting multi-           itoring module consists of two complementary components:
step future actions in one forward pass. At inference, HIT                 (a) VLM Planner (P): A GPT-4o model [22] generates
outputs action chunks of 50 joint-angle targets at 25 Hz.                      structured, interpretable skill sequences from visual
During training, an auxiliary L2 loss between predicted and                    and textual task inputs.
actual future visual embeddings improves visual grounding                 (b) VLM Skill Monitor (M): A lightweight Gemini-
and generalization. The predicted joint angles are subsequently                2.0-Flash-Lite model [28] continuously verifies the
transformed into corresponding 3D keypoints via forward                        completion of each executed skill at approximately
kinematics, matching the inputs required by the low-level                      1 Hz.
tracking controller.                                                    Together, these two components form an iterative planning-
   Instead of using the robot’s onboard Intel RealSense camera,      monitoring loop, ensuring coherent multi-step task execution.
we employ two externally mounted ELP high-speed RGB                     3) Skill Library and PDDL-like Representation: We rep-
cameras with wide-angle lenses. This binocular configuration         resent each skill available to the robot using structured,
provides consistent frame rates and explicit depth
[...continues...]


========== RSS_2302.12766.txt ==========
Appendix E and the open-source code repositories.
                                                                              Experimental Results. Most approaches perform similarly across
Experimental Results. Results for each model across the various               the various number of training demonstrations (Figure 5; right).
clutter splits are in Table 3. Voltron models are especially strong,          However, we see some promising trends; Voltron models perform
vastly outperforming R-MVP by 40% and R-R3M by over 25% on                    better than both baselines, with approaches that learn from mul-
all splits, showing that multimodal pretraining – even just condi-            tiple frame contexts V – Dual and V – Gen showing significant
tioning on language when optimizing for masked reconstruction –               improvements over single-frame approaches. Yet, the absolute suc-
can lead to substantial gains on downstream multimodal tasks. We              cess rates are low; learning for control is difficult, and while good
isolate the massive performance gains of Voltron models over prior            visual representations can help, learning closed-loop policies from
work due to the multimodal encoder that learns fused embeddings               limited data remains an open challenge.
of vision and language, allowing language to shape the visual rep-
resentations during pretraining. In contrast, R3M, and CLIP models            5.4    Language-Conditioned Imitation (Real)
learn independent text encodings that are only fused post-hoc, dur-           Given a dataset of language instructions (e.g. “throw the bag of
ing adaptation. This is even worse for MVP: these models need                 chips away”) paired with demonstrations (on a real robot in a real-
to learn to fuse their strong visual embeddings with the language             world tabletop setting), learn an instruction following policy via
embeddings from a completely different model (DistilBERT).                    behavioral cloning. Figure 6 depicts the real-world environment.
                                                                              Motivation. A large body of work looks at learning language-
5.3    Single-Task Visuomotor Control                                         conditioned policies for human-robot collaborative settings [Aru-
Motivation. Imitation learning for visuomotor control has been                mugam et al. 2017; Stepputtis et al. 2020; Lynch and Sermanet 2020;
the de-facto evaluation for prior work [Parisi et al. 2022; Nair et al.       Karamcheti et al. 2021b; Ahn et al. 2022]. This evaluation gets at
                                                                          8
V oltron: Language-Driven Representations for Robotics




Figure 6: Real-World Language-Conditioned Imitation Learning Results. The real-world “Study Desk” environment, with sample
language instructions corresponding to the five behaviors we evaluate. [Top] The challenging visual distractor split for evaluating robustness
to novel distractors, ranging from simple color swapping of background objects (e.g., purple to green textbook), to more drastic changes such
as playing a clip from “Voltron – the Animated Series” in the background [Bottom].


the robustness and reliability of learned representations, with the                              Experimental Results. Looking at success rates of the various
goal of validating different approaches in real-robot settings.                                  representations (Figure 6; top right) we see an exaggerated version
                                                                                                 of the trends exhibited in the single-task control setting; Voltron
Evaluation Details. We construct a “study desk” environment
                                                                                                 models obtain an extra boost in performance across the board given
(Figure 6) with five prototypical “tasks”: 1) closing the drawer, 2)
                                                                                                 that this task is language-conditioned, highlighting the strength of
throwing the green bag of chips in the trash can, 3) discarding the
                                                                                                 its fused representations. Similarly, R-R3M models exhibit the next
used coffee pods, 4) moving the cyan coffee mug to the purple plate,
                                                                                                 best performance. Due to time and shared resource constraints, we
and 5) moving the same mug to the yellow plate. For each task, we
                                                                                                 do not run out MVP (EgoSoup), R3M (Ego4D), or CLIP (ViT-B/16),
collect 20 teleoperated demonstrations at 10 Hz, randomly resetting
                                                                                                 though we expect similar trends as in the last evaluation.
the scene between episodes. We adopt the keyframe-based action
space proposed in James and Davison [2022] for learning. This
approach heuristically breaks a demonstration into 4-5 “waypoints”                               5.5    Qualitative: Zero-Shot Intent Scoring
(end-effector poses) that are used as action targets during behav-                               We perform a qualitative evaluation for the problem of language-
ior cloning; during policy execution, we plan min-jerk trajectories                              based intent scoring; given a language expression describing an
from the current position to the predicted waypoint, feeding the                                 intent or behavior (e.g., “opening the faucet”) and a corresponding
subsequent state and visual observation back to our policy [James                                vi
[...continues...]


========== RSS_2304.13705.txt ==========
Appendix C.                                                        two arms. For Put On Shoe, the goal is to put the shoe on a
   We summarize the training and inference of ACT in               fixed manniquin foot, and secure it with the shoe’s velcro strap.
Algorithms 1 and 2. The model has around 80M parameters,           The arms would first need to grasp the tongue and collar of
and we train from scratch for each task. The training takes        the shoe respectively, lift it up and approach the foot. Putting
around 5 hours on a single 11G RTX 2080 Ti GPU, and the            the shoe on is challenging because of the tight fitting: the arms
inference time is around 0.01 seconds on the same machine.         would need to coordinate carefully to nudge the foot in, and
                                                                   both grasps need to be robust enough to counteract the friction
                        V. E XPERIMENTS                            between the sock and shoe. Then, the left arm goes around to
    We present experiments to evaluate ACT’s performance on the bottom of the shoe to support it from dropping, followed by
fine manipulation tasks. For ease of reproducibility, we build the right arm flipping the velcro strap and pressing it against
two simulated fine manipulation tasks in MuJoCo [63], in the shoe to secure. The task is only considered successful if
addition to 6 real-world tasks with ALOHA. We provide videos the shoe clings to the foot after both arms releases. For the
for each task on the project website.                              simulated task Transfer Cube, the right arm needs to first pick
                                                                   up the red cube lying on the table, then place it inside the
A. Tasks                                                           gripper of the other arm. Due to the small clearance between
    All 8 tasks require fine-grained, bimanual manipulation, and the cube and the left gripper (around 1cm), small errors could
are illustrated in Figure 6. For Slide Ziploc, the right gripper result in collisions and task failure. For the simulated task
needs to accurately grasp the slider of the ziploc bag and open Bimanual Insertion, the left and right arms need to pick up
it, with the left gripper securing the body of the bag. For Slot the socket and peg respectively, and then insert in mid-air so
Battery, the right gripper needs to first place the battery into the peg touches the “pins” inside the socket. The clearance is
the slot of the remote controller, then using the tip of fingers around 5mm in the insertion phase. For all 8 tasks, the initial
to delicately push in the edge of the battery, until it is fully placement of the objects is either varied randomly along the
inserted. Because the spring inside the battery slot causes the 15cm white reference line (real-world tasks), or uniformly in
remote controller to move in the opposite direction during 2D regions (simulated tasks). We provide illustrations of both
insertion, the left gripper pushes down on the remote to keep the initial positions and the subtasks in Figure 6 and 7. Our
it in place. For Open Cup, the goal is to open the lid of a evaluation will additionally report the performance for each of
small condiment cup. Because of the cup’s small size, the these subtasks.
grippers cannot grasp the body of the cup by just approaching         In addition to the delicate bimanual control required to
it from the side. Therefore we leverage both grippers: the right solve these tasks, the objects we use also present a significant
fingers first lightly tap near the edge of the cup to tip it over, perception challenge. For example, the ziploc bag is largely
and then nudge it into the open left gripper. This nudging transparent, with a thin blue sealing line. Both the wrinkles
step requires high precision and closing the loop on visual on the bag and the reflective candy wrappers inside can vary
perception. The left gripper then closes gently and lifts the cup during the randomization, and distract the perception system.
off the table, followed by the right finger prying open the lid, Other transparent or translucent objects include the tape and
which also requires precision to not miss the lid or damage both the lid and body of the condiment cup, making them
the cup. The goal of Thread Velcro is to insert one end of hard to perceive precisely and ill-suited for depth cameras. The
a velcro cable tie into the small loop attached to other end. black table top also creates a low-contrast against many objects
The left gripper needs to first pick up the velcro tie from the of interest, such as the black velcro cable tie and the black
Real-World Task Definitions




                          init.                           #1                             #2                             #3
Slide Ziploc: Open the ziploc bag that is standing upright on the table. The bag is randomized along the 15cm white line. It is dropped from ~5cm
above the table to randomize the deformation, which affects the height and appearance of the bag. The left arm first grasps the bag body (Subtask#1
Grasp) followed by the right arm pinching the slider (Subtask #2 Pinch). Then the right arm moves right to unzip the bag (Subtask #3 Open).




                         init.                            #1                             #2                             #3
Slot Battery: Insert the battery into the remote controller. The controller is randomized along the 15cm white line. The battery is initialized in
roughly the same position with different rotations. The right arm first grasps the battery (Subtask#1 Grasp) then places it into the slot (Subtask#2
Place). The left arm presses onto the remote to prevent it from sliding, while the right arm pushes in the battery (Subtask#3 Insert).




                         init.                            #1                             #2
[...continues...]


========== RSS_2305.11643.txt ==========
Appendix B for more detail). We use the same 2-D point                              trajectory as being ergodic only at the limit of tf → ∞. What
mass dynamics but test only γ = 0.1 and γ = 0.001 which                             is interesting in the control trade-off
                                                                                                                       R t shown in Fig. 4. Plotted is
indicate a coarse search with an emphasis on optimizing time                        the time-normalized control t1f 0 f ku(t)kdt where the value
and a finer search with less emphasis on time respectively.                         of u(t) is bounded by umax through added constraints. In low
Trajectories illustrated in Fig. 3 show that even with a high                       γ values (large optimized tf ), less control effort is needed
γ, the generated trajectory still visits each Gaussian peak.                        to be ergodic. We suspect this is due to the robot leveraging
However, the trajectory does not spend too much time in                             its dynamics to slowly navigate an area without the need to
the area and brushes past the first peak. This is the result                        change direction abruptly. On the other spectrum of γ, control
of the ergodic inequality constraint and the balance of time                        actuation begins to fall as time is prioritized. This is due to γ
versus coverage. This can be seen in the difference in elapsed                      reaching an upper bound on the ergodic metric (as the metric
optimal times of 9.86s and 19.59 seconds respectively (almost                       is composed of only cosine functions). Therefore, there is
2× increase in time in response to 2 orders of magnitude of
                                                                                      3 There is a point where the solver does not provide solutions as t is
reduction on γ.                                                                                                                                               f
                                                                                    required to be significantly larger and is dependent on the initial trajectory
A3,4: Parameter Ablation Studies. Given the drastic change                          condition and the dynamic constraints.
                                                                             B. Time-Optimal Ergodic Search in a Cluttered Environment
                                                                                In this subsection, we investigate more realistic settings
                                                                             for which to use the proposed time-optimal ergodic search.
                                                                             Specifically, we consider the case of time-optimal exploration
                                                                             in a cluttered environment where the goal is for a robot to
                                                                             navigate around obstacles in the environment and cover the
                                                                             whole area. We first demonstrate the results in simulation
                                                                             and show that it is possible to add in safety-based collision
                                                                             constraints [30] without impeding the coverage performance.
                                                                             Then we execute the time-optimal trajectories on a drone.
                                                                             A5: Integrating Safety-Based Collision Constraints. To
                                                                             successfully navigate and explore in a cluttered environ-
Fig. 6. Time-Opt. Uniform Ergodic Search with Nonlinear Aircraft             ment in optimal time, safety-based constraints are required.
Dynamics. The proposed optimization method is capable of incorporating
nonlinear dynamics in W ⊂ R3 with safety-based collision avoidance           We introduce safety here through control-barrier functions
constraints [20]. Time-optimal coverage trajectories can be computed ahead   (CBFs) [30, 29]. CBFs provide an inequality constraint that,
of time and executed on the physical system. Collected information can be    when satisfied, guarantees state trajectories remain within a
used to update and bias search.
                                                                             predefined safe set of states. For more information, please
                                                                             see Appendix B. The constraints are integrated such that each
                                                                             CBF is centered around an object scattered in the environment
less emphasis to be ergodic and more emphasis to optimize                    (see [20]). In this example, we assume that we know the
time (less direct changes in actuation). The balance between                 location of each obstacle and the goal is to uniformly explore
optimizing time and being ergodic is then shown to require                   the cluttered area. We use a constrained 2-D single integrator
more actuation.                                                              system (kinematic system) as it closely matches the Crazyflie
   We further investigate the dependence of the optimized                    2.0 drone movements which have limits on how fast they
time against the initial condition as the discretizing knot                  can fly. The CBF constraints are integrated through h1 found
points N . Experimental runs are done using the same point-
[...continues...]


========== RSS_2407.08735.txt ==========
Appendix F, the two-stage detection approach is unaffected by
differences in visual appearance. Despite this, and noting that                               R EFERENCES
further work should examine how to disentangle semantic and          [1] Josh Achiam, Steven Adler, Sandhini Agarwal, Lama
visual features to increase robustness, we argue that our prelim-        Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo
inary findings on using multi-modal embeddings directly offers           Almeida, Janko Altenschmidt, Sam Altman, Shyamal
significant promise for streamlining the implementation of our           Anadkat, et al. Gpt-4 technical report. arXiv preprint
framework. This validates our fifth and final hypothesis H5.             arXiv:2303.08774, 2023.
 [2] Michael Ahn, Debidatta Dwibedi, Chelsea Finn,                      distribution shifts? In ICML, ICML’20. JMLR.org, 2020.
     Montse Gonzalez Arenas, Keerthana Gopalakrishnan,             [14] Robert Geirhos, Jörn-Henrik Jacobsen, Claudio Michaelis,
     Karol Hausman, Brian Ichter, Alex Irpan, Nikhil Joshi,             Richard Zemel, Wieland Brendel, Matthias Bethge, and
     Ryan Julian, et al. Autort: Embodied foundation models             Felix A Wichmann. Shortcut learning in deep neural net-
     for large scale orchestration of robotic agents. arXiv             works. Nature Machine Intelligence, 2(11):665–673, Nov
     preprint arXiv:2401.12963, 2024.                                   2020. ISSN 2522-5839. doi:10.1038/s42256-020-00257-z.
 [3] Anastasios N. Angelopoulos and Stephen Bates. A gentle             URL https://doi.org/10.1038/s42256-020-00257-z.
     introduction to conformal prediction and distribution-free    [15] Geoffrey Hinton, Oriol Vinyals, and Jeff Dean. Distilling
     uncertainty quantification, 2022.                                  the knowledge in a neural network. arXiv preprint
 [4] F. Borrelli, A. Bemporad, and M. Morari. Predictive                arXiv:1503.02531, 2015.
     control for linear and hybrid systems. 2017.                  [16] Judy Hoffman, Eric Tzeng, Taesung Park, Jun-Yan Zhu,
 [5] Anthony Brohan, Yevgen Chebotar, Chelsea Finn, Karol               Phillip Isola, Kate Saenko, Alexei Efros, and Trevor
     Hausman, Alexander Herzog, Daniel Ho, Julian Ibarz,                Darrell. CyCADA: Cycle-consistent adversarial domain
     Alex Irpan, Eric Jang, Ryan Julian, et al. Do as i can, not        adaptation. In Proceedings of the 35th International
     as i say: Grounding language in robotic affordances. In            Conference on Machine Learning, volume 80 of
     Conference on Robot Learning, pages 287–318. PMLR,                 Proceedings of Machine Learning Research, pages
     2023.                                                              1989–1998. PMLR, 10–15 Jul 2018.
 [6] Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie              [17] Cheng-Yu Hsieh, Chun-Liang Li, Chih-Kuan Yeh, Hootan
     Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind                   Nakhost, Yasuhisa Fujii, Alexander Ratner, Ranjay
     Neelakantan, Pranav Shyam, Girish Sastry, Amanda                   Krishna, Chen-Yu Lee, and Tomas Pfister. Distilling
     Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen             step-by-step! outperforming larger language models with
     Krueger, Tom Henighan, Rewon Child, Aditya Ramesh,                 less training data and smaller model sizes. arXiv preprint
     Daniel M. Ziegler, Jeffrey Wu, Clemens Winter,                     arXiv:2305.02301, 2023.
     Christopher Hesse, Mark Chen, Eric Sigler, Mateusz            [18] Wenlong Huang, Fei Xia, Ted Xiao, Harris Chan, Jacky
     Litwin, Scott Gray, Benjamin Chess, Jack Clark,                    Liang, Pete Florence, Andy Zeng, Jonathan Tompson,
     Christopher Berner, Sam McCandlish, Alec Radford,                  Igor Mordatch, Yevgen Chebotar, et al. Inner monologue:
     Ilya Sutskever, and Dario Amodei. Language models are              Embodied reasoning through planning with language
     few-shot learners. Arxiv eprint arXiv:2005.14165, 2020.            models. arXiv preprint arXiv:2207.05608, 2022.
 [7] Nicolas Carion, Francisco Massa, Gabriel Synnaeve,            [19] Wenlong Huang, Chen Wang, Ruohan Zhang, Yunzhu
     Nicolas Usunier, Alexander Kirillov, and Sergey                    Li, Jiajun Wu, and Li Fei-Fei. Voxposer: Composable
     Zagoruyko. End-to-end object detection with transformers.          3d value maps for robotic manipulation with language
     In European conference on computer vision, pages                   models. In Conference on Robot Learning, pages
     213–229. Springer, 2020.                                           540–562. PMLR, 2023.
 [8] Annie S. Chen, Govind Chada, Laura Smith, Archit              [20] Benoit Jacob, Skirmantas Kligys, Bo Chen, Menglong
     Sharma, Zipeng Fu, Sergey Levine, and Chelsea Finn.                Zhu, Matthew Tang, Andrew Howard, Hartwig Adam, and
     Adapt on-the-go: Behavior modulation for single-life               Dmitry Kalenichenko. Quantization and training of neural
     robot deployment, 2023.                                            networks for efficient integer-arithmetic-only inference.
 [9] Guojun Chen, Xiaojing Yu, and Lin Zhong. Typefly:                  In Proceedings of the IEEE conference on computer
     Flying drones with large language model. arXiv preprint            vision and pattern recognition, pages 2704–2713, 2018.
     arXiv:2312.14950, 2023.                                       [21] Albert Q Jiang, Alexandre Sablayrolles, Arthur Mensch,
[10] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina             Chris Bamford, Devendra Singh Chaplot, Diego de las
     Toutanova. Bert: Pre-training of deep bidirectional                Casas, Florian Bressand, Gianna Lengyel, Guillaume
     transformers for language understanding. arXiv preprint            Lample, Lucile Saulnier, et al. Mistral 7
[...continues...]


========== RSS_2501.09747.txt ==========
Appendix D). After training, we deploy the policy zero-
                                                                       80
shot in new scenes, with unseen scene background, camera
angles, and objects. For quantitative evaluation, we design an         60
evaluation suite with 16 tasks and 44 trials total per policy
                                                                       40
(see Table II). Each trial is scored with a task progress rubric
(e.g., 1 point for picking up the correct object, 1 point for          20
placing it in the correct receptacle). We show example scenes           0
from the quantitative evaluation in Figure 14. We further run
                                                                                     IN T





                                                                                                                   IN Y





                                                                                                                   TE T 
                                                                                                    IN E 




qualitative tests of the policy across various real-world setups
                                                                                   LD IR




                                                                                                                 GG ER




                                                                                                                 AS OU
                                                                                                  SS BL
                                                                                        G




                                                                                                                      G




                                                                                                                      R
                                                                                                      G




                                                                                                                                   AVERAGE
                                                                                 FO -SH




                                                                                                               BA ROC
                                                                                                BU TA




                                                                                                               TO ST




on three different university campuses (see Figure 7). We do
                                                                                   T




                                                                                                                 G



                                                                                                            OF TOA




not measure success rates during these evaluations, but provide
                                                                                             π0 FAST        π0 (compute matched)
numerous qualitative videos of successes and failures to help
readers get a sense of the policy’s capabilities.
                                                                     Fig. 15: Comparison of π0 -FAST and compute-matched
                                                                     diffusion π0 [7] generalist policies. π0 -FAST clearly outper-
                                                                     forms the diffusion VLA when trained with the same amount
                                                                     of training compute, due to its faster convergence. Reported:
                                                                     mean and 95% CI.
                                     TABLE III: Universal Tokenizer Evaluation Datasets.
Morphology       Dataset Name            Platform        Action Space   Action Dim   Control Frequency               Task
                  SOAR [74]              WidowX              EEF            7               5                      Pick/place
             DROID-Eval EEF [38]          Franka             EEF            7               15                     Pick/place
Single Arm   DROID-Eval Joint [38]        Franka            Joint           8               15                     Pick/place
                  SERL [46]               Franka             EEF            7               10                     Insertion
              π Table Bussing [7]          UR5              Joint           8               20                     Pick/place
              NYU DexHand [30]          ALLEGRO           Joint+EEF        30               16              Dexterous manipulation
             Berkeley DexHand [54]      ALLEGRO             Joint          16               20               In-hand manipulation
Dexterous
             Berkeley DexArm [58]    xArm+ALLEGRO           Joint          23               20                Dextrous pick/place
                  HATO [42]          UR5+Psyonic Hand     EEF+Joint        24               10                Dextrous pick/place
                   UMI [16]                UMI               EEF            7               20                     Pick/place
   UMI
               UMI on Legs [31]            UMI               EEF            7               20             Whole-body manipulation
                HumanPlus [26]          Unitree H1          Joint          40               50             Whole-body manipulation
Humanoid
             UCSD TeleVision [14]    Unitree H1 w/Neck      Joint          28               60           Manipulation+active perception
Navigation        Waymo [23]            Waymo Car          2D delta         2               10               Autonomous Driving


========== RSS_2506.14968.txt ==========
Appendix A. These diverse requests highlight the need for                In this section, we present FEAST, a mealtime-assistance
personalization in a mealtime-assistance system and suggest           system that enables users to personalize to in-the-wild
where we should focus our efforts to meet the needs of users.         eating scenarios commonly encountered in real-world set-
   Our second objective was to identify key tenets for person-        tings. All hardware and software components of FEAST are
alization. From our conversations, we identified three themes:        open-sourced on our website. In the following subsections,
adaptability, transparency, and safety.                               we describe our system hardware (Section IV-A), software
 1) Adaptability: The first clear tenet of personalization is         (Section IV-B), and user interface (Section IV-C), explaining
    adaptability: changing system behavior in response to             how each component can be personalized while adhering to
    user requests. Study participants highlighted the need for        the tenets of adaptability, transparency, and safety.
    adaptability beyond one-time system setup. For exam-
    ple, they requested the ability to customize the system           A. System Hardware
    depending on the feeding scenario—when watching TV,                  FEAST (see Figure 4) uses a Kinova Gen3 7-DoF robot
    controlling the robot with a button may be preferable             arm [85] and a Robotiq 2F-85 gripper [86]. It can be flexibly
    to verbal commands; or when dining socially, the robot            mounted either on the user’s ROVI wheelchair [87], pow-
    should retract to a resting position immediately after bite       ered by the wheelchair’s battery, or on a movable Vention
    transfer. Study participants also described how their pre-        stand [88], powered by a wall outlet.
   Tool-Change Apparatus. FEAST employs three custom               transfer the drink to the user. We next describe how skills
tools. First, a novel feeding utensil with integrated motors       are generally implemented, adapted, and sequenced together,
provides wrist-like degrees of freedom, enabling tasks such        before detailing the specific skills used in this work.
as twirling, scooping, and maintaining an upright orientation         Skills as Parameterized Behavior Trees. We imple-
when holding food. The utensil’s fork, made of compliant           ment skills as behavior trees [97]. As an extension of
silicone, is connected to a 6-axis Nano25 ATI force/torque         standard behavior trees, we expose node parameters that
sensor [89]. This default fork is detachable, allowing users       can be adapted in response to user requests (see below).
to exchange it with a metal fork if desired. To power and          For example, the behavior tree for bite acquisition includes
control the utensil without dangling wires, the robot’s gripper    three parameters: Speed, TimeToWaitBeforeAutocontinue,
fingertips are replaced with custom fingertips featuring mag-      and AskUserForConfirmation. Every parameter is associated
netic electrical connections that engage with complementary        with a domain of possible values. For example:
connectors on the utensil when grasped. Second, for drinking,         • Speed ∈ {low, medium, high}
FEAST uses an adaptable mug handle inspired by adaptable              • TimeToWaitBeforeAutocontinue ∈ [5, 100]
mug holders [90], which accommodates various cup shapes               • AskUserForConfirmation ∈ {true, false}.
without strict dimensional constraints and features an ArUco       All nodes and parameters are given human-readable names
marker [91] for autonomous grasping. Third, for mouth wip-         and descriptions to facilitate LLM-based adaptations.
ing, a custom tool with a removable microfiber cloth provides         Personalizing Skills from Natural Language. FEAST
gentle cleaning. Each tool is mounted and dismounted by the        users can make personalization requests through spoken or
robot opening and closing its finger tips (see Figure 4).          typed natural language. Our pipeline for processing these
   Novel Utensil Orientation and Camera Mount. Previous            requests is as follows:
state-of-the-art feeding systems use forward-facing in-hand
                                                                     1) The natural language request is converted into structured
cameras and similarly oriented utensils [11, 20, 23, 36].
                                                                         behavior tree updates using an LLM. (adaptability)
However, this design restricts the robot’s workspace, requires
                                                                     2) Each potential update is checked for safety. If the up-
large movements to transition between acquisition and transfer,
                                                                         dates are deemed safe, the behavior trees are updated.
and can obstruct the user’s view during feeding. Based on
                                                                         Otherwise, a failure is reported. (safety)
feedback from CRs, FEAST introduces a simple and effective
                                                                     3) The updates and outcomes are briefly summarized with
solution: positioning tools at a perpendicular angle, mimicking
                                                                         an LLM and reported back to the user. (transparency)
natural human wrist movements during eating. This change,
however, requires the camera to align accordingly. To address      We now describe these steps in more detail.
this, FEAST employs a custom camera mount with an RGB-D               1) Language → Structured Updates. We use an LLM (GPT-
Intel RealSense Camera [92], oriented perpendicularly away.        4o [98]) to translate natural language
[...continues...]


========== Science_Robotics_2304.13653.txt ==========
Supplementary Materials
Contents

 Suppl.   Methods
 Suppl.   Figure S1             The OP3 Robot
 Suppl.   Figure S2             Get-Up Skill Training Poses
 Suppl.   Figure S3             Learning Curves
 Suppl.   Figure S4             Reward Ablations
 Suppl.   Figure S5             Learned Gait
 Suppl.   Figure S6             Scripted Gait
 Suppl.   Figure S7             Vision Analysis
 Suppl.   Table S1              Joint Limits
 Suppl.   Table S2              Observations
 Suppl.   Table S3              Reward Components
 Suppl.   Table S4              Hyperparameters
 Suppl.   Table S5              Training Time
 Suppl.   Movie S1              Episodes from training in simulation of the skills and 1v1 policy.
 Suppl.   Movie S2              Compilation of several continuous real-world 1v1 matches.
 Suppl.   Movie S3              Compilation of penalty kick and get-up-and-shoot set pieces.
 Suppl.   Movie S4              Examples of recovery from pushes and falling.
 Suppl.   Movie S5              Description of training and set pieces for vision-based agents.




                                                                                                            28
                    Learning Agile Soccer Skills for a Bipedal Robot with Deep Reinforcement Learning29



Supplementary Methods

Related Work

Skill and Transfer Learning

Skill learning and transfer of learned behaviors has been a long-standing active area of research
[92, 93, 63, 64]. The data requirements for training neural networks as policies have recently
emphasized the requirement for increased data efficiency. Different mechanisms for transfer have been
proposed, ranging from direct reuse of parameters in flat or hierarchical agents [94, 95, 84, 96, 97, 98],
auxiliary objectives [99, 100, 11], to transfer via a skill’s generated experience [101, 102]. A related
line of work is kickstarting, which makes use of a trained teacher policy to enable a student policy
to learn more quickly and obtain better performance, on the same task [87, 86, 88, 103]. These
approaches transfer knowledge from the teacher to the student via a distillation loss, defined as either
the cross-entropy or KL-divergence between the output of the student and teacher networks [84, 83].
[88] frames kickstarting as a multi-objective problem, that must trade off between regularization to
the teacher policy versus the RL objective of maximizing expected return. Our approach builds on the
linear scalarization (or weighted-sum) approach to combining reward and kickstarting proposed in
[88], and we follow their proposal to adjust the level of regularization to the teacher depending on
the student’s performance. We extend this approach to work in our setting, where we have more than
one teacher, or skill policy. In particular on real robotics platforms, skill transfer has been critical for
increased data efficiency [104, 105].

Multi-agent Reinforcement Learning

Our approach to training against a mixture of previous opponents is motivated by established methods
for multi-agent training. Reinforcement learning with pure self-play can exhibit unstable or cyclic
behavior, since learning focuses on the exploitation of a single current policy [106], and by overfitting
can become exploitable. Therefore many applications of reinforcement learning to multi-agent
domains train against a mixture of opponents. In normal form games Fictitious Play [107]—in
which successive best responses to the mixture of previous policies are computed—converges to a
Nash equilibrium for two-player, zero-sum games, and it has been generalized to extensive form
games using reinforcement learning by, for example, [82, 81]. Alternatively, but similarly, [108]
achieved stability and robustness by playing against a league of opponents. Our work is an efficient
implementation of these ideas since we train against a mixture of previous opponents, but using one
continuous training epoch, rather than successive generations. This improves efficiency, but could
carry an increased risk of getting stuck in a local optima. Orthogonally, self-play provides a natural
auto-curriculum in multi-agent RL [8, 109], which can be important since finding the best response
to a set of strong opponents from scratch can be challenging for RL in some domains. For example, in
soccer, strong opponents could dominate play and a learner might get very little experience of ball
interaction. Our method effectively features a similar auto-curriculum property, since we trained in
one continuous epoch in which the opponents are initially weak, and, subsequently, are automatically
calibrated to the strength of the current agent as earlier agent checkpoints are successively added to
the opponent pool.


Environment Details

Suppl. Figure S1 shows one of the OP3 robots we used in our experiments. The robot has mechanical
improvements to reduce damage from testing different, potentially unsafe, policies on the robot,
including 3D printed bumpers and arms. We also installed a 3D printed vest for motion capture


                                                                                                          29
                                  Learning Agile Soccer Skills for a Bipedal Robot with Deep Reinforcement Learning30



markers for tracking. We limited the achievable joint range programmatically to reduce the risk of
self-collisions, as listed in Suppl. Table S1. The limits are applied to each joint independently. The
joints corresponding to the left and right side are prefixed with “l” and “r”, respectively. Zero joint
angles correspond to the T-pose. Note that these limits don’t completely eliminate collisions, as we
wanted to keep the limits wide enough to allow agile and dynamics behaviors. Suppl. Table S2 lists
all observations that are available for the agent.
[...continues...]


========== Science_Robotics_2306.11706.txt ==========
Appendix


                                                            Model details
Organisation             Google DeepMind
Model date               June 2023
Model type               Transformer with VQ-GAN encoder for multi-task, multi-embodiment behaviour cloning from human, agent
                         and self-generated data.
Model version            Initial release.
Feedback on the model    konstantinos@google.com, giuliavezzani@google.com

                                                            Intended uses
Primary intended uses    Research into learning to accomplish a wide variety of tasks from expert demonstrations or multiple real
                         robot embodiments for manipulation.
Primary intended         Google DeepMind Researchers.
users
Out-of-scope uses        Not intended for commercial or production use. Military uses are strictly prohibited.

                                                                Factors
Relevant factors         Salient factors that may alter model performance are: agent embodiment in control data, training data
                         token amount and diversity, performance of experts in training data and goal conditioning. Quality of
                         policy used for self-generated data collection. Quality of the VQ-GAN encoder. Zero-shot evaluation on
                         held-out robots.
Evaluation factors       Reported factors are: number of input tokens, importance of different tokenisation schemes, agent perfor-
                         mance.

                                                                Metrics
Model performance        We chose to report success at the task (measured as having solved the task at the end of an episode) in an
measures                 episodic evaluation setting. Held-out tasks are used to assess generalisation, ablations show importance of
                         different components.
Decision thresholds      N/A
Approaches to            The reported values do not take into consideration model uncertainty as they are evaluations of a single
uncertainty and          model and its ablations. It is prohibitive for us to evaluate models from multiple training runs as this would
variability              involve constantly training and evaluating robots. We account for noise in the evaluation by averaging
                         success across multiple episodes.

                                                              Evaluation
Tasks                    RoboCat is evaluated on in-distribution and out-of-distribution tasks, on both simulated and real-world
                         robot environments. See Section 3 for details on our tasks.

                                                            Training Data
Datasets                 We use a diverse and large number of datasets for training RoboCat. These include data from agent experi-
                         ence, human demonstrations and self-generated data, on both simulated and real-world robot environments.
                         See Section 3.4 for details on our datasets.
Motivation               Create a multi-modal, multi-task, multi-embodiment generalist policy by collecting as much, diverse, data as
                         possible. Joint training on all the datasets has produced a single network, RoboCat, capable of performing
                         these tasks.
Pre-processing           The multi-modal training data is tokenised into a stream of discrete embeddings. See Section 2.1.

                                                       Quantitative Analyses
Unitary results          We present several evaluations of RoboCat on a variety of manipulation tasks. See Section 5 for an analysis
                         of the model capabilities and ablations.

                                                       Ethical Considerations
 RoboCat is an early research model that has not yet been evaluated for deployment and safety of use outside a pure research setting.

                                                   Caveats and Recommendation
Future work              The interaction of diverse training data domains and the different affordances faced in evaluation is poorly
                         understood, and potential ethical and safety risks arise as the generalist’s capabilities grow.

                                                Table 4: RoboCat model card.




                                                                 30
Published in Transactions on Machine Learning Research (12/2023)




A       Model Card
We present a model card for RoboCat in Table 4.


B       Tasks and Data
In this section, we provide an extensive description of the tasks and data RoboCat has been trained and
fine-tuned on.

B.1       Task families

In total, we consider 253 different task variations, each of which can have an infinite number of state
configurations describing it (see Table 5) and can be grouped in different task families. Figure 12 collects
examples of the goal images used for each task family.

B.1.1       Lifting objects

We include a handful of lifting tasks performed in the physical world and three in simulation. A lifting task
is defined as grasping and lifting an object off the basket surface until the natural end of the episode. Our
aim with this task family is to primarily study goal understanding and generalisation to new embodiments
and tasks. This task family includes four variants for the YCB fruits (see Figure 12(n) for an example of
goal image), vegetable objects (see Figure 12(m)) and seven variants for NIST-i gears. For the three NIST-i
gears we include lifting in simulation (see Figure 12(h)) and in real with the Panda 7DoF (see Figure 12(o).
We also include lifting the large gear with the KUKA 14DoF (see Figure 12(v)).

B.1.2       Building structures

For the RGB-objects and NIST-i objects that are coloured in red, green, and blue4 , we use a set of structure-
buildi
[...continues...]


========== Science_Robotics_2310.12931.txt ==========
Appendix
Table of Contents
     A Full Prompts                                                                                                                             16

     B Environment Details                                                                                                                      16

     C Baseline Details                                                                                                                         20
       C.1 L2R Reward Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                      21

     D E UREKA Details                                                                                                                          23
       D.1 Pen Spinning Tasks . . . . . . . .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   24
       D.2 E UREKA from Human Initialization    .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   24
       D.3 E UREKA from Human Feedback .        .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   24
       D.4 Computation Resources . . . . . .    .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   25

     E E UREKA on Mujoco Environments                                                                                                           25

     F Additional Results                                                                                                                       28

     G E UREKA Reward Examples                                                                                                                  31
       G.1 Reward Reflection Examples. . . . . . . . . . . .                    .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   31
       G.2 Negatively Correlated E UREKA Reward Examples                        .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   34
       G.3 E UREKA from Human Initialization Examples . .                       .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   35
       G.4 E UREKA from Human Reward Reflection . . . . .                       .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   39
       G.5 E UREKA and Human Reward Comparison . . . .                          .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   43

     H Limitations and Discussion                                                                                                               45




                                                15
Published as a conference paper at ICLR 2024




A    F ULL P ROMPTS

In this section, we provide all E UREKA prompts.

                                  Prompt 1: Initial system prompt
You are a reward engineer trying to write reward functions to solve reinforcement learning
     tasks as effective as possible.
Your goal is to write a reward function for the environment that will help the agent learn the
       task described in text.
Your reward function should use useful variables from the environment as inputs. As an example
     ,
the reward function signature can be:
@torch.jit.script
def compute_reward(object_pos: torch.Tensor, goal_pos: torch.Tensor) -> Tuple[torch.Tensor,
     Dict[str, torch.Tensor]]:
    ...
    return reward, {}
Since the reward function will be decorated with @torch.jit.script,
please make sure that the code is compatible with TorchScript (e.g., use torch tensor instead
     of numpy array).
Make sure any new tensor or variable you introduce is on the same device as the input tensors.



                              Prompt 2: Reward reflection and feedback
We trained a RL policy using the provided reward function code and tracked the values of the
     individual components in the reward function as well as global policy metrics such as
     success rates and episode lengths after every {epoch_freq} epochs and the maximum, mean,
     minimum values encountered:
<REWARD REFLECTION HERE>

Please carefully analyze the policy feedback and provide a new, improved reward function that
     can better solve the task. Some helpful tips for analyzing the policy feedback:
    (1) If the success rates are always near zero, then you must rewrite the entire reward
     function
    (2) If the values for a certain reward component are near identical throughout, then this
     means RL is not able to optimize this component as it is written. You may consider
        (a) Changing its scale or the value of its temperature parameter
        (b) Re-writing the reward component
        (c) Discarding the reward component
    (3) If some reward components’ magnitude is significantly larger, then you must re-scale
     its value to a proper range
Please analyze each existing reward component in the suggested manner above first, and then
     write the reward function code.



                                   Prompt 3: Code formatting tip
The output of the reward function should consist of two items:
    (1) the total reward,
    (2) a dictionary of each individual reward component.
The code output should be formatted as a python code string: "‘‘‘python ... ‘‘‘".

Some helpful tips for writing the reward function code:
    (1) You may find it helpful to normalize the reward to a fixed range by applying
     transformations like torch.exp to the overall reward or its components
    (2) If you choose to transform a reward component, then you must also introduce a
     temperature parameter inside the transformation function; this parameter must be a named
     variable in the reward function and it must not be an input variable. Each transformed
     reward component should have its own temperature variable
    (3) Make sure the type of each input variable is correctly specified; a float input
[...continues...]


========== Science_Robotics_2410.21845.txt ==========
Supplementary Materials
A. Task Setup and Policy Training Details
In this section, we provide details regarding how each task is set up, including hardware and software; as
well as details on policy training.

A.1. RAM Insertion
Fig. 9 shows the hardware setup for the motherboard assembly task, which presents the robot, the camera
placements, and the task arrangement.




                          Figure 9: Hardware setup for the motherboard assembly task.


A.1.1. Cropped Images
We cropped the images to focus on the task-relevant parts of the scene, as shown in Fig. 10.




                   Figure 10: Sample input images from cameras used as inputs to the policy.




                                                             32
               HIL-SERL: Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning



A.1.2. Policy Training Details
In Table 2, we report additional details of the policy training for this task.

               Parameter                                  Value
               Observation space                          wrist_1, wrist_2, tcp_pose, tcp_vel, tcp_f/t
               Action space                               6D twist
               Reward function                            Binary classifier
               Classifier views                           wrist_1, wrist_2
               Classifier accuracy                        97%
               Initial offline demonstrations             20
               Environment update frequency               10 HZ
               Max episode length                         100 environment steps
               Reset method                               Scripted reset
               Randomization range                        4 cm in x and y, 6 deg in rz
               Proprio encoder size                       64
               Policy MLP size                            256x256
               Total number of RL transitions             32000
               Discount factor                            0.97
               Optimizer                                  Adam
               Learning rate                              3e-4
               Image augmentation                         Random crop

                             Table 2: Policy training details for the RAM insertion task.




                                                              33
               HIL-SERL: Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning



A.2. SSD Assembly
Fig. 9 shows the hardware setup for the motherboard assembly task, which presents the robot, the camera
placements, and the task arrangement.

A.2.1. Cropped Images
We cropped the images to focus on the task-relevant parts of the scene, as shown in Fig. 11.




                    Figure 11: Sample input images from cameras used as inputs to the policy.


A.2.2. Policy Training Details
In Table 3, we report additional details of the policy training for this task.

           Parameter                                 Value
           Observation space                         wrist_1, wrist_2, side_2, tcp_pose, tcp_vel, tcp_f/t
           Action space                              6D twist
           Reward function                           Binary classifier
           Classifier views                          wrist_1, wrist_2, side_2
           Classifier accuracy                       95%
           Initial offline demonstrations            20
           Environment update frequency              10 HZ
           Max episode length                        100 environment steps
           Reset method                              Scripted reset
           Randomization range                       2 cm in x and y, 1 deg in rz
           Proprio encoder size                      64
           Policy MLP size                           256x256
           Total number of RL transitions            21000
           Discount factor                           0.97
           Optimizer                                 Adam
           Learning rate                             3e-4
           Image augmentation                        Random crop

                             Table 3: Policy training details for the SSD assembly task.




                                                              34
               HIL-SERL: Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning



A.3. USB Grasp-Insertion
Fig. 9 shows the hardware setup for the motherboard assembly task, which presents the robot, the camera
placements, and the task arrangement.

A.3.1. Cropped Images
We cropped the images to focus on the task-relevant parts of the scene, as shown in Fig. 12.




                    Figure 12: Sample input images from cameras used as inputs to the policy.


A.3.2. Policy Training Details
In Table 4, we report additional details of the policy training for this task.

    Parameter                                Value
    Observation space                        wrist_1, wrist_2, side_1, tcp_pose, tcp_vel, tcp_f/t, gripper_pos
    Action space                             6D twist and 1D discrete gripper control
    Reward function                          Binary classifier
    Classifier views                         side_1
    Classifier accuracy                      96%
    Initial offline demonstrations           20
    Environment update frequency             10 HZ
    Max episode length                       120 environment steps
    Reset method                             Scripted reset
    Randomization range                      2 cm in x and y, 10 deg in rz
    Proprio encoder size                     64
    Motion policy MLP size                   256x256
    Grasp critic MLP size                    256x256
    Total number of RL transitions           50000
    Discount factor                          0.98
    Optimizer                                Adam
    Learning rate
[...continues...]