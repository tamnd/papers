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
section: B
section_title: Object Detection Improvements
tag: 01A2
kind: appendix
lang: en
source: arxiv:1512.03385
pdf_sha256: 1e0651b6810ecba34a3dbc5b5b0209226f889004607c1f203540a48d64e5a93a
pdf_pages: 10-12
extraction: vision
extraction_model: gpt-5
content_sha256: adbbada8f0b42db4c970874899c4595e64b3c52c159c2ba84a2a594728107baf
prompt_sha256: 329630a0b9175a55e4af1b8e281a3e67eeab250f8d643953b7dcde99743c7628
---

For completeness, we report the improvements made for the competitions. These improvements are based on deep features and thus should benefit from residual learning.

### MS COCO {#he-2016-resnet-s-ms-coco-2 .section tag=0148}

*Box refinement.* Our box refinement partially follows the iterative localization in [6]. In Faster R-CNN, the final output is a regressed box that is different from its proposal box. So for inference, we pool a new feature from the regressed box and obtain a new classification score and a new regressed box. We combine these 300 new predictions with the original 300 predictions. Non-maximum suppression (NMS) is applied on the union set of predicted boxes using an IoU threshold of 0.3 [8], followed by box voting [6]. Box refinement improves mAP by about 2 points (Table 9).

*Global context.* We combine global context in the Fast R-CNN step. Given the full-image conv feature map, we pool a feature by global Spatial Pyramid Pooling [12] (with a “single-level” pyramid) which can be implemented as “RoI” pooling using the entire image’s bounding box as the RoI. This pooled feature is fed into the post-RoI layers to obtain a global context feature. This global feature is concatenated with the original per-region feature, followed by the sibling classification and box regression layers. This new structure is trained end-to-end. Global context improves mAP@.5 by about 1 point (Table 9).

*Multi-scale testing.* In the above, all results are obtained by single-scale training/testing as in [32], where the image’s shorter side $s = 600$ pixels. Multi-scale training/testing has been developed in [12, 7] by selecting a scale from a feature pyramid, and in [33] by using maxout layers. In our current implementation, we have performed multi-scale *testing* following [33]; we have not performed multi-scale training because of limited time. In addition, we have performed multi-scale testing only for the Fast R-CNN step (but not yet for the RPN step). With a trained model, we compute conv feature maps on an image pyramid, where the image’s shorter sides are $s \in \{200, 400, 600, 800, 1000\}$.

```text
training data                           COCO train                COCO trainval
test data                               COCO val                  COCO test-dev
mAP                                     @.5      @[.5, .95]       @.5      @[.5, .95]
baseline Faster R-CNN (VGG-16)          41.5     21.2
baseline Faster R-CNN (ResNet-101)      48.4     27.2
+box refinement                         49.9     29.9
+context                                51.1     30.0             53.3     32.2
+multi-scale testing                    53.8     32.5             55.7     34.9
ensemble                                                     59.0     37.4
```

Table 9. Object detection improvements on MS COCO using Faster R-CNN and ResNet-101. {#he-2016-resnet-tab-9 .table tag=00F4}

```text
system      net         data         mAP  areo  bike  bird  boat  bottle  bus  car  cat  chair  cow  table  dog  horse  mbike  person  plant  sheep  sofa  train  tv
baseline    VGG-16      07+12        73.2 76.5  79.0  70.9  65.5  52.1    83.1 84.7 86.4 52.0   81.9 65.7   84.8 84.6   77.5   76.7    38.8   73.6   73.9  83.0   72.6
baseline    ResNet-101  07+12        76.4 79.8  80.7  76.2  68.3  55.9    85.1 85.3 89.8 56.7   87.8 69.4   88.3 88.9   80.9   78.4    41.7   78.6   79.8  85.3   72.0
baseline+++ ResNet-101  COCO+07+12   85.6 90.0  89.6  87.8  80.8  76.1    89.9 89.9 89.6 75.5   90.0 80.7   89.6 90.3   89.1   88.7    65.4   88.1   85.6  89.0   86.8
```

Table 10. Detection results on the PASCAL VOC 2007 test set. The baseline is the Faster R-CNN system. The system “baseline+++” include box refinement, context, and multi-scale testing in Table 9. {#he-2016-resnet-tab-10 .table tag=00F5}

```text
system      net         data         mAP  areo  bike  bird  boat  bottle  bus  car  cat  chair  cow  table  dog  horse  mbike  person  plant  sheep  sofa  train  tv
baseline    VGG-16      07++12       70.4 84.9  79.8  74.3  53.9  49.8    77.5 75.9 88.5 45.6   77.1 55.3   86.9 81.7   80.9   79.6    40.1   72.6   60.9  81.2   61.5
baseline    ResNet-101  07++12       73.8 86.5  81.6  77.2  58.0  51.0    78.6 76.6 93.2 48.6   80.4 59.0   92.1 85.3   84.8   80.7    48.1   77.3   66.5  84.7   65.6
baseline+++ ResNet-101  COCO+07++12  83.8 92.1  88.4  84.8  75.9  71.4    86.3 87.8 94.2 66.8   89.4 69.2   93.9 91.9   90.9   89.6    67.9   88.2   76.8  90.3   80.0
```

Table 11. Detection results on the PASCAL VOC 2012 test set (http://host.robots.ox.ac.uk:8080/leaderboard/displaylb.php?challengeid=11&compid=4). The baseline is the Faster R-CNN system. The system “baseline+++” include box refinement, context, and multi-scale testing in Table 9. {#he-2016-resnet-tab-11 .table tag=00F6}

We select two adjacent scales from the pyramid following [33]. RoI pooling and subsequent layers are performed on the feature maps of these two scales [33], which are merged by maxout as in [33]. Multi-scale testing improves the mAP by over 2 points (Table 9).

*Using validation data.* Next we use the 80k+40k trainval set for training and the 20k test-dev set for evaluation. The test-dev set has no publicly available ground truth and the result is reported by the evaluation server. Under this setting, the results are an mAP@.5 of 55.7% and an mAP@[.5, .95] of 34.9% (Table 9). This is our single-model result.

*Ensemble.* In Faster R-CNN, the system is designed to learn region proposals and also object classifiers, so an ensemble can be used to boost both tasks. We use an ensemble for proposing regions, and the union set of proposals are processed by an ensemble of per-region classifiers. Table 9 shows our result based on an ensemble of 3 networks. The mAP is 59.0% and 37.4% on the test-dev set. *This result won the 1st place in the detection task in COCO 2015.*

### PASCAL VOC {#he-2016-resnet-s-pascal-voc-2 .section tag=0149}

We revisit the PASCAL VOC dataset based on the above model. With the single model on the COCO dataset (55.7% mAP@.5 in Table 9), we fine-tune this model on the PASCAL VOC sets. The improvements of box refinement, context, and multi-scale testing are also adopted. By doing so

```text
                                   val2   test
GoogLeNet [44] (ILSVRC’14)         -      43.9
our single model (ILSVRC’15)       60.5   58.8
our ensemble (ILSVRC’15)           63.6   62.1
```

Table 12. Our results (mAP, %) on the ImageNet detection dataset. Our detection system is Faster R-CNN [32] with the improvements in Table 9, using ResNet-101. {#he-2016-resnet-tab-12 .table tag=00F7}

we achieve 85.6% mAP on PASCAL VOC 2007 (Table 10) and 83.8% on PASCAL VOC 2012 (Table 11)[^1]. The result on PASCAL VOC 2012 is 10 points higher than the previous state-of-the-art result [6].

### ImageNet Detection {#he-2016-resnet-s-imagenet-detection .section tag=0130}

The ImageNet Detection (DET) task involves 200 object categories. The accuracy is evaluated by mAP@.5. Our object detection algorithm for ImageNet DET is the same as that for MS COCO in Table 9. The networks are pre-trained on the 1000-class ImageNet classification set, and are fine-tuned on the DET data. We split the validation set into two parts (val1/val2) following [8]. We fine-tune the detection models using the DET training set and the val1 set. The val2 set is used for validation. We do not use other ILSVRC 2015 data. Our single model with ResNet-101 has

[^1]: http://host.robots.ox.ac.uk:8080/anonymous/3OJ4OJ.html, submitted on 2015-11-26.

```text
LOC         LOC         testing   LOC error   classification   top-5 LOC error
method      network               on GT CLS   network          on predicted CLS

VGG’s [41]  VGG-16      1-crop    33.1 [41]
RPN         ResNet-101  1-crop    13.3
RPN         ResNet-101  dense     11.7

RPN         ResNet-101  dense                  ResNet-101      14.4
RPN+RCNN    ResNet-101  dense                  ResNet-101      10.6
RPN+RCNN    ensemble    dense                  ensemble        8.9
```

Table 13. Localization error (%) on the ImageNet validation. In the column of “LOC error on GT class” ([41]), the ground truth class is used. In the “testing” column, “1-crop” denotes testing on a center crop of 224×224 pixels, “dense” denotes dense (fully convolutional) and multi-scale testing. {#he-2016-resnet-tab-13 .table tag=00F8}

58.8% mAP and our ensemble of 3 models has 62.1% mAP on the DET test set (Table 12). *This result won the 1st place in the ImageNet detection task in ILSVRC 2015*, surpassing the second place by 8.5 points (absolute).
