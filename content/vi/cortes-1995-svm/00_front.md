---
paper: cortes-1995-svm
title: Support-Vector Networks
authors:
  - Corinna Cortes
  - Vladimir Vapnik
year: 1995
venue: Machine Learning
field: ai-ml
section_title: Front Matter
tag: "0064"
kind: front
lang: vi
source: https://doi.org/10.1023/a:1022627411411
pdf_sha256: 561361e49eb22df6f5e14f8c19d681c6b596891f07057fc43703394383233002
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 0390daf2bfa717d2d30d93a0158a59513eb1172032e3115a1158845a30ec9e2e
translated_from: content/en/cortes-1995-svm/00_front.md
source_content_sha256: 78a8484e3ad84a3e88b417a42fbd297fbdfeb99d0dec79dc6a4a8e98b9e5d7a8
translation_model: gpt-6-astra
translation_run: 20260915T022520Z
glossary_version: 6
glossary_terms_sha256: 0d0a9334a40352952769479a6ad339487dd551fe3d836bae9914ea196d2f4310
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Mạng vectơ hỗ trợ (Support-Vector Networks)

CORINNA CORTES

VLADIMIR VAPNIK

AT&T Bell Labs., Holmdel, NJ 07733, USA

Biên tập viên: Lorenza Saitta

Tóm tắt. Mạng vectơ hỗ trợ là một máy học mới dành cho các bài toán phân loại hai nhóm. Về mặt khái niệm, máy thực hiện ý tưởng sau: các vectơ đầu vào được ánh xạ phi tuyến vào một không gian đặc trưng có số chiều rất lớn. Trong không gian đặc trưng này, một mặt quyết định tuyến tính được xây dựng. Các tính chất đặc biệt của mặt quyết định bảo đảm khả năng khái quát hóa (generalization) cao của máy học. Ý tưởng nền tảng của mạng vectơ hỗ trợ trước đây đã được hiện thực hóa cho trường hợp hạn chế khi dữ liệu huấn luyện có thể được phân tách mà không có lỗi. Ở đây, chúng tôi mở rộng kết quả này cho dữ liệu huấn luyện không thể phân tách.

Khả năng khái quát hóa cao của các mạng vectơ hỗ trợ sử dụng các phép biến đổi đa thức trên đầu vào được chứng minh. Chúng tôi cũng so sánh hiệu năng của mạng vectơ hỗ trợ với nhiều thuật toán học cổ điển, tất cả đều đã tham gia một nghiên cứu phép đo chuẩn về nhận dạng ký tự quang học (Optical Character Recognition).

Từ khóa: nhận dạng mẫu, thuật toán học hiệu quả, mạng nơ-ron, bộ phân loại hàm cơ sở xuyên tâm, bộ phân loại đa thức.

1. Giới thiệu

Hơn 60 năm trước, R.A. Fisher (Fisher, 1936) đã đề xuất thuật toán đầu tiên cho nhận dạng mẫu. Ông xem xét một mô hình gồm hai tổng thể có phân phối chuẩn, $N(\mathbf{m}_1, \Sigma_1)$ và $N(\mathbf{m}_2, \Sigma_2)$, của các vectơ $\mathbf{x}$ có $n$ chiều với các vectơ trung bình $\mathbf{m}_1$ và $\mathbf{m}_2$ và các ma trận hiệp phương sai $\Sigma_1$ và $\Sigma_2$, đồng thời chỉ ra rằng nghiệm tối ưu (Bayes) là một hàm quyết định bậc hai:

$$

F_{sq}(\mathbf{x}) = \operatorname{sign}\left[ \frac{1}{2} (\mathbf{x} - \mathbf{m}_1)^T \Sigma_1^{-1} (\mathbf{x} - \mathbf{m}_1) - \frac{1}{2} (\mathbf{x} - \mathbf{m}_2)^T \Sigma_2^{-1} (\mathbf{x} - \mathbf{m}_2) + \ln \frac{|\Sigma_2|}{|\Sigma_1|} \right].

$$
