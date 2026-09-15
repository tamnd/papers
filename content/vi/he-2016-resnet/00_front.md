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
section_title: Front Matter
tag: "00E6"
kind: front
lang: vi
source: arxiv:1512.03385
pdf_sha256: 1e0651b6810ecba34a3dbc5b5b0209226f889004607c1f203540a48d64e5a93a
pdf_pages: "1"
extraction: vision
extraction_model: gpt-5
content_sha256: bdd6d7f4635a1d796eb21f9a23ec4958e36532697b968449fcc81f931251c37d
translated_from: content/en/he-2016-resnet/00_front.md
source_content_sha256: 15a376d10e8941e2a184856bbe25ab2517d2527cc11e73b8802fab5b17bff0d9
translation_model: gpt-5
translation_run: 20260915T013833Z
glossary_version: 6
glossary_terms_sha256: 0d0a9334a40352952769479a6ad339487dd551fe3d836bae9914ea196d2f4310
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

arXiv:1512.03385v1 [cs.CV] 10 Dec 2015

Học dư sâu cho nhận dạng ảnh

Kaiming He  Xiangyu Zhang  Shaoqing Ren  Jian Sun

Microsoft Research

{kahe, v-xiangz, v-shren, jiansun}@microsoft.com

### Tóm tắt {#he-2016-resnet-s-abstract .section tag=0115}

*Mạng nơ-ron sâu hơn khó huấn luyện hơn.* Chúng tôi trình bày một khung học dư để giúp việc huấn luyện các mạng sâu hơn đáng kể so với những mạng được sử dụng trước đây. Chúng tôi định dạng lại rõ ràng các lớp thành việc học các hàm dư với tham chiếu đến các đầu vào của lớp, thay vì học các hàm không có tham chiếu. Chúng tôi cung cấp bằng chứng thực nghiệm toàn diện cho thấy các mạng dư này dễ tối ưu hóa hơn, và có thể đạt được độ chính xác từ việc tăng độ sâu đáng kể. Trên tập dữ liệu ImageNet, chúng tôi đánh giá các mạng dư có độ sâu lên tới 152 lớp—sâu hơn 8× so với các mạng VGG [41] nhưng vẫn có độ phức tạp thấp hơn. Một tổ hợp các mạng dư này đạt được lỗi 3.57% trên tập kiểm thử ImageNet. Kết quả này giành vị trí thứ 1 trong nhiệm vụ phân loại ILSVRC 2015. Chúng tôi cũng trình bày phân tích trên CIFAR-10 với 100 và 1000 lớp.

Độ sâu của các biểu diễn có tầm quan trọng trung tâm đối với nhiều nhiệm vụ nhận dạng thị giác. Chỉ nhờ các biểu diễn cực kỳ sâu của chúng tôi, chúng tôi đạt được mức cải thiện tương đối 28% trên tập dữ liệu phát hiện đối tượng COCO. Các mạng dư sâu là nền tảng cho các bài nộp của chúng tôi tới các cuộc thi ILSVRC & COCO 2015[^1], nơi chúng tôi cũng giành các vị trí thứ 1 trong các nhiệm vụ phát hiện ImageNet, định vị ImageNet, phát hiện COCO, và phân đoạn COCO.
