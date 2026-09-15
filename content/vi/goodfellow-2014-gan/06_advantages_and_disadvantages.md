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
content_sha256: ee1fae0934f364d354577f4c07feeb1f4025ebfb797684960cfc27348ae09fe8
translated_from: content/en/goodfellow-2014-gan/06_advantages_and_disadvantages.md
source_content_sha256: 38ce85b3fe3c89d51c7062535a10ebc800c4286b1991da131096aa15c4f7b192
translation_model: gpt-5
translation_run: 20260915T022520Z
glossary_version: 6
glossary_terms_sha256: 0d0a9334a40352952769479a6ad339487dd551fe3d836bae9914ea196d2f4310
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Khung mới này đi kèm với các ưu điểm và nhược điểm so với các khung mô hình hóa trước đây. Các nhược điểm chủ yếu là không có biểu diễn tường minh của $p_g(x)$, và $D$ phải được đồng bộ tốt với $G$ trong quá trình huấn luyện (đặc biệt, $G$ không được huấn luyện quá nhiều mà không cập nhật $D$, nhằm tránh “kịch bản Helvetica”, trong đó $G$ thu gọn quá nhiều giá trị của $\mathbf{z}$ thành cùng một giá trị của $\mathbf{x}$ đến mức không có đủ tính đa dạng để mô hình hóa $p_{\text{data}}$), tương tự như các chuỗi âm của máy Boltzmann phải được cập nhật kịp thời giữa các bước học. Các ưu điểm là không bao giờ cần đến các chuỗi Markov, chỉ sử dụng backprop để thu được các gradient, không cần suy luận trong quá trình học, và có thể tích hợp nhiều loại hàm vào mô hình. Bảng 2 tóm tắt sự so sánh giữa các mạng đối nghịch sinh và các phương pháp mô hình hóa sinh khác.

Các ưu điểm nêu trên chủ yếu mang tính toán học. Các mô hình đối nghịch cũng có thể đạt được một số lợi thế thống kê từ việc mạng sinh không được cập nhật trực tiếp bằng các ví dụ dữ liệu, mà chỉ bằng các gradient truyền qua bộ phân biệt. Điều này có nghĩa là các thành phần của đầu vào không được sao chép trực tiếp vào các tham số của bộ sinh. Một ưu điểm khác của các mạng đối nghịch là chúng có thể biểu diễn các phân phối rất sắc nét, thậm chí suy biến, trong khi các phương pháp dựa trên chuỗi Markov yêu cầu phân phối phải hơi mờ để các chuỗi có thể trộn giữa các mode.
