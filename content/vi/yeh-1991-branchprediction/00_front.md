---
paper: yeh-1991-branchprediction
title: Two-Level Adaptive Training Branch Prediction
authors:
  - Tse-Yu Yeh
  - Yale N. Patt
year: 1991
venue: MICRO
field: architecture
section_title: Front Matter
tag: 005D
kind: front
lang: vi
source: http://classweb.ece.umd.edu/enee646/yeh+patt-adaptive-training-1991.pdf
pdf_sha256: 31a1e6a4b5f27f0523a80a4f004afe037d8e698a56335242059eb2b3868d5669
pdf_pages: 2-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 8db359bf8dbddf30d44c7050494f8d8d72ae171725c5f8e911620e65d282459c
translated_from: content/en/yeh-1991-branchprediction/00_front.md
source_content_sha256: 77f01ba23f7fb2676aa3ab71579793567f744938bfe7faf7f122b68de788ffbc
translation_model: gpt-5
translation_run: 20260918T153717Z
glossary_version: 7
glossary_terms_sha256: cb514473400f65abfd1e5d09e5f82163f246175d67293cbba8eac7dbb7d7b890
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Có sự suy giảm nghiêm trọng về hiệu năng trong các máy có đường ống sâu và/hoặc siêu vô hướng do các lỗi dự đoán gây ra bởi lượng lớn công việc suy đoán phải bị loại bỏ [1, 8]. Đây là động lực để đề xuất một sơ đồ dự đoán nhánh động mới có độ chính xác cao hơn. Sơ đồ mới sử dụng hai mức thông tin lịch sử nhánh để đưa ra dự đoán. Mức thứ nhất là lịch sử của $n$ nhánh gần nhất. Mức thứ hai là hành vi nhánh đối với $s$ lần xuất hiện gần nhất của mẫu duy nhất đó trong lịch sử của $n$ nhánh gần nhất. Thông tin lịch sử được thu thập trực tiếp trong quá trình thực thi mà không cần thực thi chương trình trước đó, loại bỏ nhược điểm chính của Static Training Prediction. Sơ đồ được đề xuất ở đây được gọi là Two-Level Adaptive Training Branch Prediction, vì các dự đoán không chỉ dựa trên bản ghi của $n$ nhánh gần nhất, mà còn dựa trên bản ghi của $s$ lần xuất hiện gần nhất của bản ghi cụ thể của $n$ nhánh gần nhất.

Các mô phỏng dựa trên trace đã được sử dụng trong nghiên cứu này. Sơ đồ dự đoán nhánh Two-Level Adaptive Training cũng như các sơ đồ dự đoán nhánh động và tĩnh khác đã được mô phỏng trên bộ phép đo chuẩn SPEC. Bằng cách sử dụng Two-Level Adaptive Training Branch Prediction, độ chính xác dự đoán trung bình đối với các phép đo chuẩn đạt 97 phần trăm, trong khi hầu hết các sơ đồ khác đạt dưới 93 phần trăm. Điều này biểu thị sự giảm hơn 100 phần trăm số lần dự đoán sai khi sử dụng sơ đồ Two-Level Adaptive Training. Sự giảm này có thể trực tiếp dẫn đến mức tăng hiệu năng lớn trên một bộ xử lý hiệu năng cao.
