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
section: "1"
section_title: Giới thiệu
tag: 00C1
kind: section
lang: vi
source: arxiv:1406.2661
pdf_sha256: ff5819e3a7b713c3bd3107b7de3d51fe0a347aa5d8444f0efdcf2345ef0a8b63
pdf_pages: 1-2
extraction: vision
extraction_model: gpt-6-astra
content_sha256: 1a20c258e872367badf0ffce98f8791c4798739ad5a30bdafe45df76d57a6588
translated_from: content/en/goodfellow-2014-gan/01_introduction.md
source_content_sha256: 8cff2016cc5d3b4dd011b7208fdc0d32f9d8fa354a6c940d4eeb6be58318d257
translation_model: gpt-6-astra
translation_run: 20260915T022520Z
glossary_version: 6
glossary_terms_sha256: 0d0a9334a40352952769479a6ad339487dd551fe3d836bae9914ea196d2f4310
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Triển vọng của học sâu (deep learning) là khám phá các mô hình phân cấp phong phú [2] biểu diễn các phân phối xác suất trên những loại dữ liệu gặp trong các ứng dụng trí tuệ nhân tạo, như ảnh tự nhiên, dạng sóng âm thanh chứa tiếng nói và các ký hiệu trong ngữ liệu ngôn ngữ tự nhiên. Cho đến nay, những thành công nổi bật nhất của học sâu gắn với các mô hình phân biệt, thường là những mô hình ánh xạ đầu vào cảm giác phong phú, có số chiều cao sang một nhãn lớp [14], [[krizhevsky-2012-imagenet]]. Những thành công nổi bật này chủ yếu dựa trên các thuật toán lan truyền ngược (backpropagation) và dropout, sử dụng các đơn vị tuyến tính từng khúc [19, 9, 10] có gradient với tính chất đặc biệt thuận lợi. Các mô hình *sinh* sâu có ít ảnh hưởng hơn, do khó xấp xỉ nhiều phép tính xác suất không khả thi về mặt tính toán xuất hiện trong ước lượng hợp lý cực đại và các chiến lược liên quan, cũng như do khó khai thác lợi ích của các đơn vị tuyến tính từng khúc trong bối cảnh sinh dữ liệu. Chúng tôi đề xuất một thủ tục ước lượng mô hình sinh mới tránh được những khó khăn này. [^4]

Trong khung *mạng đối kháng* (adversarial nets) được đề xuất, mô hình sinh được đặt vào thế đối đầu với một đối thủ: một mô hình phân biệt học cách xác định một mẫu đến từ phân phối của mô hình hay phân phối dữ liệu. Có thể hình dung mô hình sinh tương tự như một nhóm làm tiền giả, cố gắng tạo ra tiền giả và sử dụng mà không bị phát hiện, trong khi mô hình phân biệt tương tự như cảnh sát, cố gắng phát hiện tiền giả. Sự cạnh tranh trong trò chơi này thúc đẩy cả hai nhóm cải tiến phương pháp của mình cho đến khi không thể phân biệt tiền giả với tiền thật.

[^1]: Jean Pouget-Abadie đang làm việc với tư cách khách mời tại Université de Montréal, đến từ Ecole Polytechnique.
[^2]: Sherjil Ozair đang làm việc với tư cách khách mời tại Université de Montréal, đến từ Indian Institute of Technology Delhi
[^3]: Yoshua Bengio là nghiên cứu viên cao cấp của CIFAR.
[^4]: Toàn bộ mã và siêu tham số có tại http://www.github.com/goodfeli/adversarial

Khung này có thể tạo ra các thuật toán huấn luyện cụ thể cho nhiều loại mô hình và thuật toán tối ưu hóa. Trong bài báo này, chúng tôi khảo sát trường hợp đặc biệt khi mô hình sinh tạo các mẫu bằng cách truyền nhiễu ngẫu nhiên qua một perceptron nhiều lớp, và mô hình phân biệt cũng là một perceptron nhiều lớp. Chúng tôi gọi trường hợp đặc biệt này là *mạng đối kháng*. Trong trường hợp này, chúng tôi có thể huấn luyện cả hai mô hình chỉ bằng các thuật toán lan truyền ngược và dropout vốn rất thành công [17], đồng thời lấy mẫu từ mô hình sinh chỉ bằng lan truyền xuôi. Không cần suy luận xấp xỉ hay chuỗi Markov.
