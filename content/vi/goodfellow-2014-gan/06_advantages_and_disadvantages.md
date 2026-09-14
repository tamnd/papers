---
paper: goodfellow-2014-gan
title: Generative Adversarial Nets
authors:
  - Ian J. Goodfellow
  - Jean Pouget-Abadie
  - Mehdi Mirza
  - Bing Xu
  - David Warde-Farley
  - Sherjil Ozair
  - Aaron Courville
  - Yoshua Bengio
year: 2014
venue: NIPS
field: ai-ml
section: "6"
section_title: Ưu điểm và nhược điểm
tag: 00CE
kind: section
lang: vi
source: arxiv:1406.2661
pdf_sha256: ff5819e3a7b713c3bd3107b7de3d51fe0a347aa5d8444f0efdcf2345ef0a8b63
pdf_pages: "7"
extraction: vision
extraction_model: gpt-6-astra
content_sha256: ebd651c5627bb60befa1ebe10cdb5b40ef7be595e341634fc3b867e5f8aad06b
translated_from: content/en/goodfellow-2014-gan/06_advantages_and_disadvantages.md
source_content_sha256: 38ce85b3fe3c89d51c7062535a10ebc800c4286b1991da131096aa15c4f7b192
translation_model: gpt-5
translation_run: 20260914T064759Z
glossary_version: 5
glossary_terms_sha256: 95f35b8eeca7e5d682ff5338deefc303c320897501e75661c72974f88e8865d4
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Khung mới này có cả ưu điểm và nhược điểm so với các khung mô hình hóa trước đây. Nhược điểm chủ yếu là không có biểu diễn tường minh của $p_g(x)$, và $D$ phải được đồng bộ tốt với $G$ trong quá trình huấn luyện (cụ thể, $G$ không được huấn luyện quá nhiều mà không cập nhật $D$, nhằm tránh “kịch bản Helvetica”, trong đó $G$ làm sụp đổ quá nhiều giá trị của $\mathbf{z}$ về cùng một giá trị của $\mathbf{x}$ khiến không đủ tính đa dạng để mô hình hóa $p_{\text{data}}$), tương tự như việc các chuỗi âm của máy Boltzmann phải được cập nhật giữa các bước học. Ưu điểm là không bao giờ cần các chuỗi Markov, chỉ sử dụng backprop để thu được gradient, không cần suy luận trong quá trình học, và có thể đưa nhiều loại hàm khác nhau vào mô hình. Bảng 2 tóm tắt sự so sánh giữa các mạng đối sinh và các phương pháp mô hình hóa sinh khác.

Các ưu điểm nói trên chủ yếu mang tính tính toán. Các mô hình đối sinh cũng có thể đạt được một số lợi thế về mặt thống kê nhờ mạng sinh không được cập nhật trực tiếp bằng các ví dụ dữ liệu, mà chỉ bằng các gradient truyền qua bộ phân biệt. Điều này có nghĩa là các thành phần của đầu vào không được sao chép trực tiếp vào các tham số của bộ sinh. Một ưu điểm khác của các mạng đối sinh là chúng có thể biểu diễn các phân phối rất sắc nét, thậm chí suy biến, trong khi các phương pháp dựa trên các chuỗi Markov yêu cầu phân phối phải tương đối mờ để các chuỗi có thể trộn lẫn giữa các mode.
