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
section_title: Cải thiện phát hiện đối tượng
tag: 01A2
kind: appendix
lang: vi
source: arxiv:1512.03385
pdf_sha256: 1e0651b6810ecba34a3dbc5b5b0209226f889004607c1f203540a48d64e5a93a
pdf_pages: 10-12
extraction: vision
extraction_model: gpt-5
content_sha256: 040a900f796edbcd34696daf663900e4f646ad8cbba01a1a8fb2a4bd4d8e85d4
translated_from: content/en/he-2016-resnet/07_object_detection_improvements.md
source_content_sha256: adbbada8f0b42db4c970874899c4595e64b3c52c159c2ba84a2a594728107baf
translation_model: gpt-5
translation_run: 20260915T060234Z
glossary_version: 6
glossary_terms_sha256: 0d0a9334a40352952769479a6ad339487dd551fe3d836bae9914ea196d2f4310
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Để hoàn thiện, chúng tôi báo cáo các cải tiến được thực hiện cho các cuộc thi. Những cải tiến này dựa trên các đặc trưng sâu và do đó nên được hưởng lợi từ học dư.

### MS COCO {#he-2016-resnet-s-ms-coco-2 .section tag=0148}

\*Tinh chỉnh hộp.\* Việc tinh chỉnh hộp của chúng tôi phần nào tuân theo định vị lặp trong [6]. Trong Faster R-CNN, đầu ra cuối cùng là một hộp được hồi quy, khác với hộp đề xuất của nó. Vì vậy, đối với suy luận, chúng tôi gom nhóm một đặc trưng mới từ hộp được hồi quy và thu được một điểm số phân loại mới cùng một hộp được hồi quy mới. Chúng tôi kết hợp 300 dự đoán mới này với 300 dự đoán ban đầu. Non-maximum suppression (NMS) được áp dụng trên tập hợp hợp nhất của các hộp được dự đoán bằng cách sử dụng ngưỡng IoU là 0.3 [8], tiếp theo là bỏ phiếu hộp [6]. Tinh chỉnh hộp cải thiện mAP khoảng 2 điểm (Bảng 9).

\*Ngữ cảnh toàn cục.\* Chúng tôi kết hợp ngữ cảnh toàn cục trong bước Fast R-CNN. Với bản đồ đặc trưng conv của toàn bộ ảnh, chúng tôi gom nhóm một đặc trưng bằng Spatial Pyramid Pooling toàn cục [12] (với kim tự tháp “một mức”) có thể được triển khai như gom nhóm “RoI” bằng cách sử dụng hộp bao của toàn bộ ảnh làm RoI. Đặc trưng được gom nhóm này được đưa vào các lớp sau RoI để thu được một đặc trưng ngữ cảnh toàn cục. Đặc trưng toàn cục này được nối với đặc trưng ban đầu theo từng vùng, tiếp theo là các lớp phân loại song sinh và hồi quy hộp. Cấu trúc mới này được huấn luyện end-to-end. Ngữ cảnh toàn cục cải thiện mAP\@.5 khoảng 1 điểm (Bảng 9).

\*Kiểm thử đa tỷ lệ.\* Trong phần trên, tất cả kết quả thu được bằng huấn luyện/kiểm thử đơn tỷ lệ như trong [32], trong đó cạnh ngắn hơn của ảnh là $s = 600$ pixel. Huấn luyện/kiểm thử đa tỷ lệ đã được phát triển trong [12, 7] bằng cách chọn một tỷ lệ từ một kim tự tháp đặc trưng, và trong [33] bằng cách sử dụng các lớp maxout. Trong triển khai hiện tại, chúng tôi đã thực hiện \*kiểm thử\* đa tỷ lệ theo [33]; chúng tôi chưa thực hiện huấn luyện đa tỷ lệ vì thời gian hạn chế. Ngoài ra, chúng tôi chỉ thực hiện kiểm thử đa tỷ lệ cho bước Fast R-CNN (nhưng chưa cho bước RPN). Với một mô hình đã được huấn luyện, chúng tôi tính toán các bản đồ đặc trưng conv trên một kim tự tháp ảnh, trong đó các cạnh ngắn hơn của ảnh là $s \in \{200, 400, 600, 800, 1000\}$.

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

Bảng 9. Các cải thiện phát hiện đối tượng trên MS COCO sử dụng Faster R-CNN và ResNet-101. {#he-2016-resnet-tab-9 .table tag=00F4}

```text
system      net         data         mAP  areo  bike  bird  boat  bottle  bus  car  cat  chair  cow  table  dog  horse  mbike  person  plant  sheep  sofa  train  tv
baseline    VGG-16      07+12        73.2 76.5  79.0  70.9  65.5  52.1    83.1 84.7 86.4 52.0   81.9 65.7   84.8 84.6   77.5   76.7    38.8   73.6   73.9  83.0   72.6
baseline    ResNet-101  07+12        76.4 79.8  80.7  76.2  68.3  55.9    85.1 85.3 89.8 56.7   87.8 69.4   88.3 88.9   80.9   78.4    41.7   78.6   79.8  85.3   72.0
baseline+++ ResNet-101  COCO+07+12   85.6 90.0  89.6  87.8  80.8  76.1    89.9 89.9 89.6 75.5   90.0 80.7   89.6 90.3   89.1   88.7    65.4   88.1   85.6  89.0   86.8
```

Bảng 10. Các kết quả phát hiện trên tập kiểm thử PASCAL VOC 2007. Đường cơ sở là hệ thống Faster R-CNN. Hệ thống “baseline+++” bao gồm tinh chỉnh hộp, ngữ cảnh và kiểm thử đa tỷ lệ trong Bảng 9. {#he-2016-resnet-tab-10 .table tag=00F5}

```text
system      net         data         mAP  areo  bike  bird  boat  bottle  bus  car  cat  chair  cow  table  dog  horse  mbike  person  plant  sheep  sofa  train  tv
baseline    VGG-16      07++12       70.4 84.9  79.8  74.3  53.9  49.8    77.5 75.9 88.5 45.6   77.1 55.3   86.9 81.7   80.9   79.6    40.1   72.6   60.9  81.2   61.5
baseline    ResNet-101  07++12       73.8 86.5  81.6  77.2  58.0  51.0    78.6 76.6 93.2 48.6   80.4 59.0   92.1 85.3   84.8   80.7    48.1   77.3   66.5  84.7   65.6
baseline+++ ResNet-101  COCO+07++12  83.8 92.1  88.4  84.8  75.9  71.4    86.3 87.8 94.2 66.8   89.4 69.2   93.9 91.9   90.9   89.6    67.9   88.2   76.8  90.3   80.0
```

Bảng 11. Các kết quả phát hiện trên tập kiểm thử PASCAL VOC 2012 (http://host.robots.ox.ac.uk:8080/leaderboard/displaylb.php?challengeid=11&compid=4). Đường cơ sở là hệ thống Faster R-CNN. Hệ thống “baseline+++” bao gồm tinh chỉnh hộp, ngữ cảnh và kiểm thử đa tỷ lệ trong Bảng 9. {#he-2016-resnet-tab-11 .table tag=00F6}

Chúng tôi chọn hai tỷ lệ liền kề từ kim tự tháp theo [33]. Gom nhóm RoI và các lớp tiếp theo được thực hiện trên các bản đồ đặc trưng của hai tỷ lệ này [33], được hợp nhất bằng maxout như trong [33]. Kiểm thử đa tỷ lệ cải thiện mAP hơn 2 điểm (Bảng 9).

\*Sử dụng dữ liệu xác thực.\* Tiếp theo, chúng tôi sử dụng tập trainval 80k+40k để huấn luyện và tập test-dev 20k để đánh giá. Tập test-dev không có ground truth công khai và kết quả được báo cáo bởi server đánh giá. Trong thiết lập này, các kết quả là mAP\@.5 là 55.7% và mAP@[.5, .95] là 34.9% (Bảng 9). Đây là kết quả của mô hình đơn của chúng tôi.

\*Tổ hợp.\* Trong Faster R-CNN, hệ thống được thiết kế để học các đề xuất vùng và cả các bộ phân loại đối tượng, vì vậy một tổ hợp có thể được sử dụng để tăng cường cả hai tác vụ. Chúng tôi sử dụng một tổ hợp để đề xuất vùng, và tập hợp hợp nhất của các đề xuất được xử lý bởi một tổ hợp các bộ phân loại theo từng vùng. Bảng 9 cho thấy kết quả của chúng tôi dựa trên một tổ hợp gồm 3 mạng. mAP là 59.0% và 37.4% trên tập test-dev. \*Kết quả này giành vị trí thứ 1 trong tác vụ phát hiện trong COCO 2015.\*

### PASCAL VOC {#he-2016-resnet-s-pascal-voc-2 .section tag=0149}

Chúng tôi xem xét lại tập dữ liệu PASCAL VOC dựa trên mô hình ở trên. Với mô hình đơn trên tập dữ liệu COCO (55.7% mAP\@.5 trong Table 9), chúng tôi tinh chỉnh mô hình này trên các tập PASCAL VOC. Các cải tiến về tinh chỉnh hộp, ngữ cảnh và kiểm thử đa tỷ lệ cũng được áp dụng. Bằng cách này

```text
                                   val2   test
GoogLeNet [44] (ILSVRC’14)         -      43.9
our single model (ILSVRC’15)       60.5   58.8
our ensemble (ILSVRC’15)           63.6   62.1
```

Table 12. Các kết quả của chúng tôi (mAP, %) trên tập dữ liệu phát hiện ImageNet. Hệ thống phát hiện của chúng tôi là Faster R-CNN [32] với các cải tiến trong Table 9, sử dụng ResNet-101. {#he-2016-resnet-tab-12 .table tag=00F7}

chúng tôi đạt được 85.6% mAP trên PASCAL VOC 2007 (Table 10) và 83.8% trên PASCAL VOC 2012 (Table 11)[^1]. Kết quả trên PASCAL VOC 2012 cao hơn 10 điểm so với kết quả tiên tiến nhất trước đó [6].

### Phát hiện ImageNet {#he-2016-resnet-s-imagenet-detection .section tag=0130}

Tác vụ Phát hiện ImageNet (DET) bao gồm 200 loại đối tượng. Độ chính xác được đánh giá bằng mAP\@.5. Thuật toán phát hiện đối tượng ImageNet DET của chúng tôi giống với thuật toán dành cho MS COCO trong Table 9. Các mạng được huấn luyện trước trên tập phân loại ImageNet 1000 lớp, và được tinh chỉnh trên dữ liệu DET. Chúng tôi chia tập xác thực thành hai phần (val1/val2) theo [8]. Chúng tôi tinh chỉnh các mô hình phát hiện bằng cách sử dụng tập huấn luyện DET và tập val1. Tập val2 được sử dụng để xác thực. Chúng tôi không sử dụng dữ liệu ILSVRC 2015 khác. Mô hình đơn của chúng tôi với ResNet-101 có

[^1]: http://host.robots.ox.ac.uk:8080/anonymous/3OJ4OJ.html, được gửi vào ngày 2015-11-26.

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

Table 13. Lỗi định vị (%) trên tập xác thực ImageNet. Trong cột “LOC error on GT class” ([41]), lớp chân lý thực được sử dụng. Trong cột “testing”, “1-crop” biểu thị kiểm thử trên một crop trung tâm gồm 224×224 pixel, “dense” biểu thị kiểm thử dày đặc (hoàn toàn tích chập) và đa tỷ lệ. {#he-2016-resnet-tab-13 .table tag=00F8}

58.8% mAP và tổ hợp của 3 mô hình của chúng tôi có 62.1% mAP trên tập kiểm thử DET (Table 12). *Kết quả này giành vị trí thứ 1 trong tác vụ phát hiện ImageNet tại ILSVRC 2015*, vượt qua vị trí thứ hai 8.5 điểm (tuyệt đối).
