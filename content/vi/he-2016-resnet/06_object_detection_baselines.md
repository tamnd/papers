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
section: A
section_title: Các đường cơ sở phát hiện đối tượng
tag: 01A1
kind: appendix
lang: vi
source: arxiv:1512.03385
pdf_sha256: 1e0651b6810ecba34a3dbc5b5b0209226f889004607c1f203540a48d64e5a93a
pdf_pages: "10"
extraction: vision
extraction_model: gpt-5
content_sha256: d76c37bdd016e8dc1d55e2b6ca6db1a7f88784d3028dd638355470591eda53ef
translated_from: content/en/he-2016-resnet/06_object_detection_baselines.md
source_content_sha256: b25b4dc40110d5ad5f1b8834b52f1e7b3bdc8aa53eb91b3ed62416c15db4df26
translation_model: gpt-5
translation_run: 20260915T013833Z
glossary_version: 6
glossary_terms_sha256: 0d0a9334a40352952769479a6ad339487dd551fe3d836bae9914ea196d2f4310
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Trong phần này, chúng tôi giới thiệu phương pháp phát hiện dựa trên hệ thống đường cơ sở Faster R-CNN [32]. Các mô hình được khởi tạo bởi các mô hình phân loại ImageNet, sau đó được tinh chỉnh trên dữ liệu phát hiện đối tượng. Chúng tôi đã thử nghiệm với ResNet-50/101 vào thời điểm diễn ra các cuộc thi phát hiện ILSVRC & COCO 2015.

Khác với VGG-16 được sử dụng trong [32], ResNet của chúng tôi không có các lớp fc ẩn. Chúng tôi áp dụng ý tưởng “Networks on Conv feature maps” (NoC) [33] để giải quyết vấn đề này. Chúng tôi tính toán các bản đồ đặc trưng conv được chia sẻ trên toàn ảnh bằng cách sử dụng các lớp có stride trên ảnh không lớn hơn 16 pixel (tức là conv1, conv2_x, conv3_x, và conv4_x, tổng cộng 91 lớp conv trong ResNet-101; Bảng 1). Chúng tôi xem các lớp này tương tự như 13 lớp conv trong VGG-16, và bằng cách này, cả ResNet và VGG-16 đều có các bản đồ đặc trưng conv với cùng stride tổng (16 pixel). Các lớp này được chia sẻ bởi một mạng đề xuất vùng (RPN, tạo ra 300 đề xuất) [32] và một mạng phát hiện Fast R-CNN [7]. RoI pooling [7] được thực hiện trước conv5_1. Trên đặc trưng được RoI-pooled này, tất cả các lớp của conv5_x trở lên được áp dụng cho từng vùng, đóng vai trò của các lớp fc của VGG-16. Lớp phân loại cuối cùng được thay thế bằng hai lớp song song (phân loại và hồi quy hộp [7]).

Đối với việc sử dụng các lớp BN, sau khi tiền huấn luyện, chúng tôi tính toán các thống kê BN (trung bình và phương sai) cho mỗi lớp trên tập huấn luyện ImageNet. Sau đó, các lớp BN được cố định trong quá trình tinh chỉnh cho phát hiện đối tượng. Như vậy, các lớp BN trở thành các kích hoạt tuyến tính với các độ lệch và tỷ lệ không đổi, và các thống kê BN không được cập nhật bởi quá trình tinh chỉnh. Chúng tôi cố định các lớp BN chủ yếu để giảm mức tiêu thụ bộ nhớ trong quá trình huấn luyện Faster R-CNN.

### PASCAL VOC {#he-2016-resnet-s-pascal-voc .section tag=012C}

Theo [7, 32], đối với tập *test* PASCAL VOC 2007, chúng tôi sử dụng 5k ảnh *trainval* trong VOC 2007 và 16k ảnh *trainval* trong VOC 2012 để huấn luyện (“07+12”). Đối với tập *test* PASCAL VOC 2012, chúng tôi sử dụng 10k ảnh *trainval+test* trong VOC 2007 và 16k ảnh *trainval* trong VOC 2012 để huấn luyện (“07++12”). Các siêu tham số cho việc huấn luyện Faster R-CNN giống như trong [32]. Bảng 7 cho thấy các kết quả. ResNet-101 cải thiện mAP hơn >3% so với VGG-16. Sự cải thiện này hoàn toàn là do các đặc trưng được cải thiện được học bởi ResNet.

### MS COCO {#he-2016-resnet-s-ms-coco .section tag=012D}

Tập dữ liệu MS COCO [26] bao gồm 80 loại đối tượng. Chúng tôi đánh giá theo độ đo PASCAL VOC (mAP @ IoU = 0.5) và độ đo COCO tiêu chuẩn (mAP @ IoU = .5:.05:.95). Chúng tôi sử dụng 80k ảnh trong tập train để huấn luyện và 40k ảnh trong tập val để đánh giá. Hệ thống phát hiện của chúng tôi cho COCO tương tự như hệ thống cho PASCAL VOC. Chúng tôi huấn luyện các mô hình COCO bằng một triển khai 8-GPU, do đó bước RPN có kích thước mini-batch là 8 ảnh (*i.e.*, 1 trên mỗi GPU) và bước Fast R-CNN có kích thước mini-batch là 16 ảnh. Bước RPN và bước Fast R-CNN đều được huấn luyện trong 240k vòng lặp với tốc độ học là 0.001 và sau đó trong 80k vòng lặp với 0.0001.

Bảng 8 cho thấy các kết quả trên tập kiểm thử MS COCO. ResNet-101 có mức tăng 6% của mAP@[.5, .95] so với VGG-16, tương đương với cải thiện tương đối 28%, hoàn toàn do các đặc trưng được học bởi mạng tốt hơn đóng góp. Đáng chú ý, mức tăng tuyệt đối của mAP@I.5, .95] (6.0%) gần lớn bằng mức tăng của mAP@.5 (6.9%). Điều này cho thấy một mạng sâu hơn có thể cải thiện cả nhận dạng và định vị.
