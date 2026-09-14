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
content_sha256: 9f6562ad5828d6212b9bea988b10c6386637a74b4cd1be70d566677234528f95
translated_from: content/en/goodfellow-2014-gan/01_introduction.md
source_content_sha256: 8cff2016cc5d3b4dd011b7208fdc0d32f9d8fa354a6c940d4eeb6be58318d257
translation_model: gpt-5
translation_run: 20260914T064759Z
glossary_version: 5
glossary_terms_sha256: 95f35b8eeca7e5d682ff5338deefc303c320897501e75661c72974f88e8865d4
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Lời hứa của học sâu là khám phá các mô hình phong phú, có cấu trúc phân cấp [2] biểu diễn các phân phối xác suất trên những loại dữ liệu gặp trong các ứng dụng trí tuệ nhân tạo, chẳng hạn như ảnh tự nhiên, dạng sóng âm thanh chứa tiếng nói và các ký hiệu trong các kho ngữ liệu ngôn ngữ tự nhiên. Cho đến nay, những thành công nổi bật nhất của học sâu liên quan đến các mô hình phân biệt, thường là những mô hình ánh xạ một đầu vào cảm nhận giàu thông tin có số chiều cao thành một nhãn lớp [14], [[krizhevsky-2012-imagenet]]. Những thành công nổi bật này chủ yếu dựa trên các thuật toán backpropagation và dropout, sử dụng các đơn vị tuyến tính từng phần [19, 9, 10] có gradient đặc biệt ổn định. Các mô hình *sinh* sâu có tác động ít hơn, do khó khăn trong việc xấp xỉ nhiều phép tính xác suất không thể xử lý tường minh phát sinh trong ước lượng hợp lý cực đại và các chiến lược liên quan, cũng như do khó khăn trong việc tận dụng lợi ích của các đơn vị tuyến tính từng phần trong bối cảnh sinh dữ liệu. Chúng tôi đề xuất một thủ tục ước lượng mô hình sinh mới giúp tránh được những khó khăn này. [^4]

Trong khung *adversarial nets* được đề xuất, mô hình sinh được đặt đối đầu với một đối thủ: một mô hình phân biệt học cách xác định liệu một mẫu đến từ phân phối của mô hình hay từ phân phối dữ liệu. Mô hình sinh có thể được xem như tương tự một nhóm làm tiền giả, cố gắng tạo ra tiền giả và sử dụng nó mà không bị phát hiện, trong khi mô hình phân biệt tương tự như lực lượng cảnh sát, cố gắng phát hiện tiền giả. Sự cạnh tranh trong trò chơi này thúc đẩy cả hai bên cải thiện phương pháp của mình cho đến khi hàng giả không thể phân biệt được với hàng thật.

[^1]: Jean Pouget-Abadie đang thăm Université de Montréal từ Ecole Polytechnique.
[^2]: Sherjil Ozair đang thăm Université de Montréal từ Indian Institute of Technology Delhi
[^3]: Yoshua Bengio là CIFAR Senior Fellow.
[^4]: Toàn bộ mã nguồn và các siêu tham số có tại [http://www.github.com/goodfeli/adversarial](http://www.github.com/goodfeli/adversarial)

Khung này có thể tạo ra các thuật toán huấn luyện cụ thể cho nhiều loại mô hình và thuật toán tối ưu hóa. Trong bài báo này, chúng tôi khảo sát trường hợp đặc biệt khi mô hình sinh tạo các mẫu bằng cách truyền nhiễu ngẫu nhiên qua một perceptron nhiều lớp, và mô hình phân biệt cũng là một perceptron nhiều lớp. Chúng tôi gọi trường hợp đặc biệt này là *adversarial nets*. Trong trường hợp này, chúng tôi có thể huấn luyện cả hai mô hình chỉ bằng các thuật toán backpropagation và dropout rất thành công [17], đồng thời lấy mẫu từ mô hình sinh chỉ bằng lan truyền thuận. Không cần suy luận xấp xỉ hay các chuỗi Markov.
