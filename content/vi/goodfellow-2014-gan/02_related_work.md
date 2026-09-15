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
section: "2"
section_title: Công trình liên quan
tag: 00C2
kind: section
lang: vi
source: arxiv:1406.2661
pdf_sha256: ff5819e3a7b713c3bd3107b7de3d51fe0a347aa5d8444f0efdcf2345ef0a8b63
pdf_pages: "2"
extraction: vision
extraction_model: gpt-6-astra
content_sha256: 934a22426680d58b497334786b248e3f52c596094c2eec2f8d2c13c43430f719
translated_from: content/en/goodfellow-2014-gan/02_related_work.md
source_content_sha256: 3c6ee40c3e5f0c541f155a1beac7058d33fb1fcee27693716f53a966e99ae912
translation_model: gpt-5
translation_run: 20260915T022520Z
glossary_version: 6
glossary_terms_sha256: 0d0a9334a40352952769479a6ad339487dd551fe3d836bae9914ea196d2f4310
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Một phương án thay thế cho các mô hình đồ thị có hướng với các biến ẩn là các mô hình đồ thị vô hướng với các biến ẩn, chẳng hạn như restricted Boltzmann machines (RBMs) [27, 16], deep Boltzmann machines (DBMs) [26] và nhiều biến thể của chúng. Các tương tác bên trong những mô hình như vậy được biểu diễn dưới dạng tích của các hàm thế chưa chuẩn hóa, được chuẩn hóa bởi một phép tổng/tích phân toàn cục trên tất cả các trạng thái của các biến ngẫu nhiên. Đại lượng này (*hàm phân hoạch*) và gradient của nó là không thể tính toán được đối với tất cả các trường hợp ngoài những trường hợp tầm thường nhất, mặc dù chúng có thể được ước lượng bằng các phương pháp Markov chain Monte Carlo (MCMC). Việc trộn tạo ra một vấn đề đáng kể đối với các thuật toán học dựa vào MCMC [3, 5].

Deep belief networks (DBNs) [16] là các mô hình lai chứa một lớp vô hướng duy nhất và một số lớp có hướng. Mặc dù tồn tại một tiêu chuẩn huấn luyện xấp xỉ nhanh theo từng lớp, DBNs phải chịu các khó khăn về tính toán liên quan đến cả mô hình vô hướng và mô hình có hướng.

Các tiêu chuẩn thay thế không xấp xỉ hoặc chặn log-likelihood cũng đã được đề xuất, chẳng hạn như score matching [18] và noise-contrastive estimation (NCE) [13]. Cả hai phương pháp này đều yêu cầu mật độ xác suất đã học được đặc tả về mặt giải tích đến một hằng số chuẩn hóa. Lưu ý rằng trong nhiều mô hình sinh thú vị với nhiều lớp biến ẩn (chẳng hạn như DBNs và DBMs), thậm chí không thể suy ra một mật độ xác suất chưa chuẩn hóa có thể tính toán được. Một số mô hình như denoising auto-encoders [30] và contractive autoencoders có các quy tắc học rất giống với score matching được áp dụng cho RBMs. Trong NCE, cũng như trong công trình này, một tiêu chuẩn huấn luyện phân biệt được sử dụng để khớp một mô hình sinh. Tuy nhiên, thay vì khớp một mô hình phân biệt riêng biệt, chính mô hình sinh được dùng để phân biệt dữ liệu được sinh ra với các mẫu từ một phân phối nhiễu cố định. Vì NCE sử dụng một phân phối nhiễu cố định, việc học chậm đi đáng kể sau khi mô hình đã học được ngay cả một phân phối gần đúng chính xác trên một tập con nhỏ của các biến quan sát.

Cuối cùng, một số kỹ thuật không liên quan đến việc định nghĩa rõ ràng một phân phối xác suất, mà thay vào đó huấn luyện một máy sinh để lấy các mẫu từ phân phối mong muốn. Phương pháp này có ưu điểm là các máy như vậy có thể được thiết kế để được huấn luyện bằng back-propagation. Các công trình gần đây nổi bật trong lĩnh vực này bao gồm khung generative stochastic network (GSN) [5], mở rộng các denoising auto-encoders tổng quát [4]: cả hai có thể được xem như định nghĩa một chuỗi Markov được tham số hóa, tức là người ta học các tham số của một máy thực hiện một bước của một chuỗi Markov sinh. So với GSN, khung adversarial nets không yêu cầu một chuỗi Markov để lấy mẫu. Vì adversarial nets không yêu cầu các vòng lặp phản hồi trong quá trình sinh, chúng có khả năng tận dụng tốt hơn các đơn vị tuyến tính từng phần [19, 9, 10], vốn cải thiện hiệu năng của backpropagation nhưng gặp vấn đề với kích hoạt không bị chặn khi được sử dụng trong một vòng lặp phản hồi. Các ví dụ gần đây hơn về việc huấn luyện một máy sinh bằng cách lan truyền ngược vào nó bao gồm các công trình gần đây về auto-encoding variational Bayes [20] và stochastic backpropagation [24].
