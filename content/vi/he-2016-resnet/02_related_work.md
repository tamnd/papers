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
section: "2"
section_title: Công trình liên quan
tag: 00FA
kind: section
lang: vi
source: arxiv:1512.03385
pdf_sha256: 1e0651b6810ecba34a3dbc5b5b0209226f889004607c1f203540a48d64e5a93a
pdf_pages: 2-3
extraction: vision
extraction_model: gpt-5
content_sha256: d482c4b3bf7d663860808ed65fcdebc0196ec32855b14571b8c6ac5af08d0ddf
translated_from: content/en/he-2016-resnet/02_related_work.md
source_content_sha256: 1120ad3d7c0d5520eac1d7f5f9def52541a3bf84e93e039850248a72467ac255
translation_model: gpt-5
translation_run: 20260915T013833Z
glossary_version: 6
glossary_terms_sha256: 0d0a9334a40352952769479a6ad339487dd551fe3d836bae9914ea196d2f4310
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

**Biểu diễn phần dư.** Trong nhận dạng ảnh, VLAD [18] là một biểu diễn mã hóa bằng các vectơ phần dư đối với một từ điển, và Fisher Vector [30] có thể được xây dựng như một phiên bản xác suất [18] của VLAD. Cả hai đều là các biểu diễn nông mạnh mẽ cho truy hồi ảnh và phân loại [4, 48]. Đối với lượng tử hóa vectơ, việc mã hóa các vectơ phần dư [17] được cho thấy hiệu quả hơn so với việc mã hóa các vectơ gốc.

Trong thị giác mức thấp và đồ họa máy tính, để giải các Phương trình Vi phân Riêng phần (PDEs), phương pháp Multigrid được sử dụng rộng rãi [3] cải tổ hệ thống thành các bài toán con ở nhiều tỷ lệ, trong đó mỗi bài toán con chịu trách nhiệm cho nghiệm phần dư giữa một tỷ lệ thô hơn và một tỷ lệ mịn hơn. Một phương án thay thế cho Multigrid là tiền điều kiện hóa cơ sở phân cấp [45, 46], dựa trên các biến biểu diễn các vectơ phần dư giữa hai tỷ lệ. Đã được chứng minh [3, 45, 46] rằng các bộ giải này hội tụ nhanh hơn nhiều so với các bộ giải tiêu chuẩn không nhận biết bản chất phần dư của các nghiệm. Các phương pháp này cho thấy rằng một cách cải tổ hoặc tiền điều kiện hóa tốt có thể đơn giản hóa quá trình tối ưu hóa.

**Kết nối tắt.** Các thực hành và lý thuyết dẫn đến các kết nối tắt [2, 34, 49] đã được nghiên cứu trong một thời gian dài. Một thực hành ban đầu trong việc huấn luyện các perceptron nhiều lớp (MLPs) là thêm một lớp tuyến tính được kết nối từ đầu vào mạng đến đầu ra [34, 49]. Trong [44, 24], một vài lớp trung gian được kết nối trực tiếp với các bộ phân loại phụ để xử lý các gradient biến mất/bùng nổ. Các bài báo [39, 38, 31, 47] đề xuất các phương pháp căn giữa các phản hồi của lớp, các gradient và các lỗi được lan truyền, được triển khai bằng các kết nối tắt. Trong [44], một lớp “inception” được cấu thành từ một nhánh tắt và một vài nhánh sâu hơn.

Đồng thời với công trình của chúng tôi, “mạng đường cao tốc” [42, 43] đưa ra các kết nối tắt với các hàm cổng [[hochreiter-1997-lstm]]. Các cổng này phụ thuộc vào dữ liệu và có các tham số, trái ngược với các kết nối tắt ánh xạ đồng nhất của chúng tôi không có tham số. Khi một kết nối tắt có cổng bị “đóng” (tiến gần đến không), các lớp trong mạng đường cao tốc biểu diễn các hàm *không phần dư*. Ngược lại, công thức của chúng tôi luôn học các hàm phần dư; các kết nối tắt ánh xạ đồng nhất của chúng tôi không bao giờ bị đóng, và mọi thông tin luôn được truyền qua, cùng với các hàm phần dư bổ sung cần được học. Ngoài ra, mạng đường cao tốc chưa chứng minh được sự tăng độ chính xác với độ sâu tăng cực lớn ($e.g.$, trên 100 lớp).
