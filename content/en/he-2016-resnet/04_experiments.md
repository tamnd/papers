---
paper: he-2016-resnet
title: Deep Residual Learning for Image Recognition
authors:
  - Kaiming He
  - Xiangyu Zhang
  - Shaoqing Ren
  - Jian Sun
year: 2016
venue: CVPR
field: ai-ml
section: "4"
section_title: Experiments
tag: "0100"
kind: section
lang: en
source: arxiv:1512.03385
pdf_sha256: 1e0651b6810ecba34a3dbc5b5b0209226f889004607c1f203540a48d64e5a93a
pdf_pages: 4-8
extraction: vision
extraction_model: gpt-5
content_sha256: 64c0ae63181a41965fc6a87fa1a460a2063bb45fbad28f910f4836d1220e131b
prompt_sha256: 329630a0b9175a55e4af1b8e281a3e67eeab250f8d643953b7dcde99743c7628
---

### 4.1. ImageNet Classification {#he-2016-resnet-s4-1 .section tag=0101}

We evaluate our method on the ImageNet 2012 classification dataset [36] that consists of 1000 classes. The models are trained on the 1.28 million training images, and evaluated on the 50k validation images. We also obtain a final result on the 100k test images, reported by the test server. We evaluate both top-1 and top-5 error rates.

Plain Networks. We first evaluate 18-layer and 34-layer plain nets. The 34-layer plain net is in Fig. 3 (middle). The 18-layer plain net is of a similar form. See Table 1 for detailed architectures.

The results in Table 2 show that the deeper 34-layer plain net has higher validation error than the shallower 18-layer plain net. To reveal the reasons, in Fig. 4 (left) we compare their training/validation errors during the training procedure. We have observed the degradation problem - the

```text
layer name     output size     18-layer              34-layer              50-layer                         101-layer                          152-layer
-------------------------------------------------------------------------------------------------------------------------------
conv1          112×112                                7×7, 64, stride 2
                                              3×3 max pool, stride 2
conv2_x        56×56           [3×3, 64            [3×3, 64            [1×1, 64                         [1×1, 64                          [1×1, 64
                                3×3, 64] ×2         3×3, 64] ×3         3×3, 64                          3×3, 64                           3×3, 64
                                                                        1×1, 256] ×3                    1×1, 256] ×3                     1×1, 256] ×3

conv3_x        28×28           [3×3, 128           [3×3, 128           [1×1, 128                        [1×1, 128                         [1×1, 128
                                3×3, 128] ×2        3×3, 128] ×4        3×3, 128                         3×3, 128                          3×3, 128
                                                                        1×1, 512] ×4                    1×1, 512] ×4                     1×1, 512] ×8

conv4_x        14×14           [3×3, 256           [3×3, 256           [1×1, 256                        [1×1, 256                         [1×1, 256
                                3×3, 256] ×2        3×3, 256] ×6        3×3, 256                         3×3, 256                          3×3, 256
                                                                        1×1, 1024] ×6                   1×1, 1024] ×23                   1×1, 1024] ×36

conv5_x        7×7             [3×3, 512           [3×3, 512           [1×1, 512                        [1×1, 512                         [1×1, 512
                                3×3, 512] ×2        3×3, 512] ×3        3×3, 512                         3×3, 512                          3×3, 512
                                                                        1×1, 2048] ×3                   1×1, 2048] ×3                    1×1, 2048] ×3
                1×1                                   average pool, 1000-d fc, softmax
FLOPs                                  1.8×10^9             3.6×10^9             3.8×10^9                         7.6×10^9                         11.3×10^9
```

Table 1. Architectures for ImageNet. Building blocks are shown in brackets (see also Fig. 5), with the numbers of blocks stacked. Down-sampling is performed by conv3_1, conv4_1, and conv5_1 with a stride of 2. {#he-2016-resnet-tab-1 .table tag=00E9}

Figure 4. Training on ImageNet. Thin curves denote training error, and bold curves denote validation error of the center crops. Left: plain networks of 18 and 34 layers. Right: ResNets of 18 and 34 layers. In this plot, the residual networks have no extra parameter compared to their plain counterparts. {#he-2016-resnet-fig-4 .figure tag=00EA}

|  | plain | ResNet |
|---|---:|---:|
| 18 layers | 27.94 | 27.88 |
| 34 layers | 28.54 | **25.03** |

Table 2. Top-1 error (%, 10-crop testing) on ImageNet validation. Here the ResNets have no extra parameter compared to their plain counterparts. Fig. 4 shows the training procedures. {#he-2016-resnet-tab-2 .table tag=00EB}

34-layer plain net has higher *training* error throughout the whole training procedure, even though the solution space of the 18-layer plain network is a subspace of that of the 34-layer one.

We argue that this optimization difficulty is *unlikely* to be caused by vanishing gradients. These plain networks are trained with BN [16], which ensures forward propagated signals to have non-zero variances. We also verify that the backward propagated gradients exhibit healthy norms with BN. So neither forward nor backward signals vanish. In fact, the 34-layer plain net is still able to achieve competitive accuracy (Table 3), suggesting that the solver works to some extent. We conjecture that the deep plain nets may have exponentially low convergence rates, which impact the reducing of the training error[^1]. The reason for such optimization difficulties will be studied in the future.

### Residual Networks. {#he-2016-resnet-s-residual-networks .section tag=011C}

Next we evaluate 18-layer and 34-layer residual nets (*ResNets*). The baseline architectures are the same as the above plain nets, except that a shortcut connection is added to each pair of 3×3 filters as in Fig. 3 (right). In the first comparison (Table 2 and Fig. 4 right), we use identity mapping for all shortcuts and zero-padding for increasing dimensions (option A). So they have *no extra parameter* compared to the plain counterparts.

We have three major observations from Table 2 and Fig. 4. First, the situation is reversed with residual learning – the 34-layer ResNet is better than the 18-layer ResNet (by 2.8%). More importantly, the 34-layer ResNet exhibits considerably lower training error and is generalizable to the validation data. This indicates that the degradation problem is well addressed in this setting and we manage to obtain accuracy gains from increased depth.

Second, compared to its plain counterpart, the 34-layer

[^1]: We have experimented with more training iterations (3×) and still observed the degradation problem, suggesting that this problem cannot be feasibly addressed by simply using more iterations.

```text
model                 top-1 err.   top-5 err.
VGG-16 [41]           28.07        9.33
GoogLeNet [44]        -            9.15
PReLU-net [13]        24.27        7.38
---------------------------------------------
plain-34              28.54        10.02
ResNet-34 A           25.03        7.76
ResNet-34 B           24.52        7.46
ResNet-34 C           24.19        7.40
---------------------------------------------
ResNet-50             22.85        6.71
ResNet-101            21.75        6.05
ResNet-152            21.43        5.71
```

Table 3. Error rates (%, 10-crop testing) on ImageNet validation. VGG-16 is based on our test. ResNet-50/101/152 are of option B that only uses projections for increasing dimensions. {#he-2016-resnet-tab-3 .table tag=00EC}

```text
method                top-1 err.   top-5 err.
VGG [41] (ILSVRC’14)  -            8.43†
GoogLeNet [44] (ILSVRC’14)
                       -            7.89
---------------------------------------------
VGG [41] (v5)         24.4         7.1
PReLU-net [13]        21.59        5.71
BN-inception [16]     21.99        5.81
---------------------------------------------
ResNet-34 B           21.84        5.71
ResNet-34 C           21.53        5.60
ResNet-50             20.74        5.25
ResNet-101            19.87        4.60
ResNet-152            19.38        4.49
```

Table 4. Error rates (%) of single-model results on the ImageNet validation set (except † reported on the test set). {#he-2016-resnet-tab-4 .table tag=00ED}

```text
method                         top-5 err. (test)
VGG [41] (ILSVRC’14)           7.32
GoogLeNet [44] (ILSVRC’14)     6.66
---------------------------------------------
VGG [41] (v5)                  6.8
PReLU-net [13]                4.94
BN-inception [16]             4.82
---------------------------------------------
ResNet (ILSVRC’15)            3.57
```

Table 5. Error rates (%) of ensembles. The top-5 error is on the test set of ImageNet and reported by the test server. {#he-2016-resnet-tab-5 .table tag=00EE}

ResNet reduces the top-1 error by 3.5% (Table 2), resulting from the successfully reduced training error (Fig. 4 right vs. left). This comparison verifies the effectiveness of residual learning on extremely deep systems.

Last, we also note that the 18-layer plain/residual nets are comparably accurate (Table 2), but the 18-layer ResNet converges faster (Fig. 4 right vs. left). When the net is “not overly deep” (18 layers here), the current SGD solver is still able to find good solutions to the plain net. In this case, the ResNet eases the optimization by providing faster convergence at the early stage.

### Identity vs. Projection Shortcuts. {#he-2016-resnet-s-identity-vs-projection-shortcuts .section tag=011D}

We have shown that parameter-free, identity shortcuts help with training. Next we investigate projection shortcuts (Eqn.(2)). In Table 3 we compare three options: (A) zero-padding shortcuts are used for increasing dimensions, and all shortcuts are parameter-free (the same as Table 2 and Fig. 4 right); (B) projection shortcuts are used for increasing dimensions, and other shortcuts are identity; and (C) all shortcuts are projections.

Figure 5. A deeper residual function $\mathcal{F}$ for ImageNet. Left: a building block (on 56×56 feature maps) as in Fig. 3 for ResNet-34. Right: a “bottleneck” building block for ResNet-50/101/152. {#he-2016-resnet-fig-5 .figure tag=011E}

Table 3 shows that all three options are considerably better than the plain counterpart. B is slightly better than A. We argue that this is because the zero-padded dimensions in A indeed have no residual learning. C is marginally better than B, and we attribute this to the extra parameters introduced by many (thirteen) projection shortcuts. But the small differences among A/B/C indicate that projection shortcuts are not essential for addressing the degradation problem. So we do not use option C in the rest of this paper, to reduce memory/time complexity and model sizes. Identity shortcuts are particularly important for not increasing the complexity of the bottleneck architectures that are introduced below.

### Deeper Bottleneck Architectures. {#he-2016-resnet-s-deeper-bottleneck-architectures .section tag=011F}

Next we describe our deeper nets for ImageNet. Because of concerns on the training time that we can afford, we modify the building block as a bottleneck design.^4 For each residual function $\mathcal{F}$, we use a stack of 3 layers instead of 2 (Fig. 5). The three layers are 1×1, 3×3, and 1×1 convolutions, where the 1×1 layers are responsible for reducing and then increasing (restoring) dimensions, leaving the 3×3 layer a bottleneck with smaller input/output dimensions. Fig. 5 shows an example, where both designs have similar time complexity.

The parameter-free identity shortcuts are particularly important for the bottleneck architectures. If the identity shortcut in Fig. 5 (right) is replaced with projection, one can show that the time complexity and model size are doubled, as the shortcut is connected to the two high-dimensional ends. So identity shortcuts lead to more efficient models for the bottleneck designs.

### 50-layer ResNet: {#he-2016-resnet-s-50-layer-resnet .section tag=0120}

We replace each 2-layer block in the

[^1]: Deeper non-bottleneck ResNets (e.g., Fig. 5 left) also gain accuracy from increased depth (as shown on CIFAR-10), but are not as economical as the bottleneck ResNets. So the usage of bottleneck designs is mainly due to practical considerations. We further note that the degradation problem of plain nets is also witnessed for the bottleneck designs.

34-layer net with this 3-layer bottleneck block, resulting in a 50-layer ResNet (Table 1). We use option B for increasing dimensions. This model has 3.8 billion FLOPs.

**101-layer and 152-layer ResNets:** We construct 101-layer and 152-layer ResNets by using more 3-layer blocks (Table 1). Remarkably, although the depth is significantly increased, the 152-layer ResNet (11.3 billion FLOPs) still has *lower complexity* than VGG-16/19 nets (15.3/19.6 billion FLOPs).

The 50/101/152-layer ResNets are more accurate than the 34-layer ones by considerable margins (Table 3 and 4). We do not observe the degradation problem and thus enjoy significant accuracy gains from considerably increased depth. The benefits of depth are witnessed for all evaluation metrics (Table 3 and 4).

**Comparisons with State-of-the-art Methods.** In Table 4 we compare with the previous best single-model results. Our baseline 34-layer ResNets have achieved very competitive accuracy. Our 152-layer ResNet has a single-model top-5 validation error of 4.49%. This single-model result outperforms all previous ensemble results (Table 5). We combine six models of different depth to form an ensemble (only with two 152-layer ones at the time of submitting). This leads to **3.57%** top-5 error on the test set (Table 5). *This entry won the 1st place in ILSVRC 2015.*

### 4.2. CIFAR-10 and Analysis {#he-2016-resnet-s4-2 .section tag=0129}

We conducted more studies on the CIFAR-10 dataset [20], which consists of 50k training images and 10k testing images in 10 classes. We present experiments trained on the training set and evaluated on the test set. Our focus is on the behaviors of extremely deep networks, but not on pushing the state-of-the-art results, so we intentionally use simple architectures as follows.

The plain/residual architectures follow the form in Fig. 3 (middle/right). The network inputs are 32×32 images, with the per-pixel mean subtracted. The first layer is 3×3 convolutions. Then we use a stack of $n$ layers with 3×3 convolutions on the feature maps of sizes {32, 16, 8} respectively, with $2n$ layers for each feature map size. The numbers of filters are {16, 32, 64} respectively. The subsampling is performed by convolutions with a stride of 2. The network ends with a global average pooling, a 10-way fully-connected layer, and softmax. There are totally $6n+2$ stacked weighted layers. The following table summarizes the architecture:

| output map size | 32×32 | 16×16 | 8×8 |
|---|---:|---:|---:|
| # layers | 1+2n | 2n | 2n |
| # filters | 16 | 32 | 64 |

When shortcut connections are used, they are connected to the pairs of 3×3 layers (totally 3$n$ shortcuts). On this dataset we use identity shortcuts in all cases (*i.e.*, option A),

```text
                         method                 error (%)
                         Maxout [10]            9.38
                         NIN [25]               8.81
                         DSN [24]               8.22

                         # layers   # params
FitNet [35]                 19        2.5M      8.39
Highway [42, 43]            19        2.3M      7.54 (7.72±0.16)
Highway [42, 43]            32        1.25M     8.80
ResNet                      20        0.27M     8.75
ResNet                      32        0.46M     7.51
ResNet                      44        0.66M     7.17
ResNet                      56        0.85M     6.97
ResNet                     110        1.7M      6.43 (6.61±0.16)
ResNet                    1202       19.4M      7.93
```

Table 6. Classification error on the CIFAR-10 test set. All methods are with data augmentation. For ResNet-110, we run it 5 times and show “best (mean±std)” as in [43]. {#he-2016-resnet-tab-6 .table tag=00EF}

so our residual models have exactly the same depth, width, and number of parameters as the plain counterparts.

We use a weight decay of 0.0001 and momentum of 0.9, and adopt the weight initialization in [13] and BN [16] but with no dropout. These models are trained with a mini-batch size of 128 on two GPUs. We start with a learning rate of 0.1, divide it by 10 at 32k and 48k iterations, and terminate training at 64k iterations, which is determined on a 45k/5k train/val split. We follow the simple data augmentation in [24] for training: 4 pixels are padded on each side, and a 32×32 crop is randomly sampled from the padded image or its horizontal flip. For testing, we only evaluate the single view of the original 32×32 image.

We compare $n=\{3,5,7,9\}$, leading to 20, 32, 44, and 56-layer networks. Fig. 6 (left) shows the behaviors of the plain nets. The deep plain nets suffer from increased depth, and exhibit higher training error when going deeper. This phenomenon is similar to that on ImageNet (Fig. 4, left) and on MNIST (see [42]), suggesting that such an optimization difficulty is a fundamental problem.

Fig. 6 (middle) shows the behaviors of ResNets. Also similar to the ImageNet cases (Fig. 4, right), our ResNets manage to overcome the optimization difficulty and demonstrate accuracy gains when the depth increases.

We further explore $n = 18$ that leads to a 110-layer ResNet. In this case, we find that the initial learning rate of 0.1 is slightly too large to start converging[^1]. So we use 0.01 to warm up the training until the training error is below 80% (about 400 iterations), and then go back to 0.1 and continue training. The rest of the learning schedule is as done previously. This 110-layer network converges well (Fig. 6, middle). It has *fewer* parameters than other deep and thin

[^1]: With an initial learning rate of 0.1, it starts converging (<90% error) after several epochs, but still reaches similar accuracy.

Figure 6. Training on CIFAR-10. Dashed lines denote training error, and bold lines denote testing error. **Left:** plain networks. The error of plain-110 is higher than 60% and not displayed. **Middle:** ResNets. **Right:** ResNets with 110 and 1202 layers. {#he-2016-resnet-fig-6 .figure tag=00F0}

Figure 7. Standard deviations (std) of layer responses on CIFAR-10. The responses are the outputs of each $3 \times 3$ layer, after BN and before nonlinearity. **Top:** the layers are shown in their original order. **Bottom:** the responses are ranked in descending order. {#he-2016-resnet-fig-7 .figure tag=012A}

networks such as FitNet [35] and Highway [42] (Table 6), yet is among the state-of-the-art results (6.43%, Table 6).

**Analysis of Layer Responses.** Fig. 7 shows the standard deviations (std) of the layer responses. The responses are the outputs of each $3 \times 3$ layer, after BN and before other nonlinearity (ReLU/addition). For ResNets, this analysis reveals the response strength of the residual functions. Fig. 7 shows that ResNets have generally smaller responses than their plain counterparts. These results support our basic motivation (Sec.3.1) that the residual functions might be generally closer to zero than the non-residual functions. We also notice that the deeper ResNet has smaller magnitudes of responses, as evidenced by the comparisons among ResNet-20, 56, and 110 in Fig. 7. When there are more layers, an individual layer of ResNets tends to modify the signal less.

**Exploring Over 1000 layers.** We explore an aggressively deep model of over 1000 layers. We set $n = 200$ that leads to a 1202-layer network, which is trained as described above. Our method shows *no optimization difficulty*, and this $10^3$-layer network is able to achieve *training error* $< 0.1\%$ (Fig. 6, right). Its test error is still fairly good (7.93%, Table 6).

But there are still open problems on such aggressively deep models. The testing result of this 1202-layer network is worse than that of our 110-layer network, although both

| training data | 07+12 | 07++12 |
|---|---:|---:|
| test data | VOC 07 test | VOC 12 test |
| VGG-16 | 73.2 | 70.4 |
| ResNet-101 | **76.4** | **73.8** |

Table 7. Object detection mAP (%) on the PASCAL VOC 2007/2012 test sets using **baseline** Faster R-CNN. See also Table 10 and 11 for better results. {#he-2016-resnet-tab-7 .table tag=00F1}

| metric | mAP@.5 | mAP@[.5, .95] |
|---|---:|---:|
| VGG-16 | 41.5 | 21.2 |
| ResNet-101 | **48.4** | **27.2** |

Table 8. Object detection mAP (%) on the COCO validation set using **baseline** Faster R-CNN. See also Table 9 for better results. {#he-2016-resnet-tab-8 .table tag=00F2}

have similar training error. We argue that this is because of overfitting. The 1202-layer network may be unnecessarily large (19.4M) for this small dataset. Strong regularization such as maxout [10] or dropout [14] is applied to obtain the best results ([10, 25, 24, 35]) on this dataset. In this paper, we use no maxout/dropout and just simply impose regularization via deep and thin architectures by design, without distracting from the focus on the difficulties of optimization. But combining with stronger regularization may improve results, which we will study in the future.

### 4.3. Object Detection on PASCAL and MS COCO {#he-2016-resnet-s4-3 .section tag=0103}

Our method has good generalization performance on other recognition tasks. Table 7 and 8 show the object detection baseline results on PASCAL VOC 2007 and 2012 [5] and COCO [26]. We adopt *Faster R-CNN* [32] as the detection method. Here we are interested in the improvements of replacing VGG-16 [41] with ResNet-101. The detection implementation (see appendix) of using both models is the same, so the gains can only be attributed to better networks. Most remarkably, on the challenging COCO dataset we obtain a 6.0% increase in COCO’s standard metric (mAP@[.5, .95]), which is a 28% relative improvement. This gain is solely due to the learned representations.

Based on deep residual nets, we won the 1st places in several tracks in ILSVRC & COCO 2015 competitions: ImageNet detection, ImageNet localization, COCO detection, and COCO segmentation. The details are in the appendix.
