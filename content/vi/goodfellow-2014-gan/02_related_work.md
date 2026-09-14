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
content_sha256: 7dc99c9951c36d1f68048bfd92cd10005cebf3a7dd4bb7f3ac79dc3be9d39738
translated_from: content/en/goodfellow-2014-gan/02_related_work.md
source_content_sha256: 3c6ee40c3e5f0c541f155a1beac7058d33fb1fcee27693716f53a966e99ae912
translation_model: gpt-5
translation_run: 20260914T064759Z
glossary_version: 5
glossary_terms_sha256: 95f35b8eeca7e5d682ff5338deefc303c320897501e75661c72974f88e8865d4
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
roundtrip: differs-materially
roundtrip_run: 20260914T070941Z
---

Một phương án thay thế cho các mô hình đồ thị có hướng với các biến tiềm ẩn là các mô hình đồ thị vô hướng với các biến tiềm ẩn, chẳng hạn như restricted Boltzmann machines (RBMs) [27, 16], deep Boltzmann machines (DBMs) [26] và nhiều biến thể của chúng. Các tương tác bên trong những mô hình như vậy được biểu diễn dưới dạng tích của các hàm thế chưa được chuẩn hóa, được chuẩn hóa bằng một phép tổng hóa/tích phân hóa toàn cục trên mọi trạng thái của các biến ngẫu nhiên. Đại lượng này ( *hàm phân hoạch* ) và gradient của nó là bất khả trị đối với tất cả các trường hợp ngoại trừ những trường hợp tầm thường nhất, mặc dù chúng có thể được ước lượng bằng các phương pháp Markov chain Monte Carlo (MCMC). Sự hòa trộn đặt ra một vấn đề đáng kể đối với các thuật toán học phụ thuộc vào MCMC [3, 5].

Deep belief networks (DBNs) [16] là các mô hình lai chứa một lớp vô hướng duy nhất và nhiều lớp có hướng. Mặc dù tồn tại một tiêu chuẩn huấn luyện xấp xỉ theo từng lớp nhanh, DBN phải gánh chịu những khó khăn về tính toán gắn liền với cả mô hình vô hướng và mô hình có hướng.

Các tiêu chuẩn thay thế không xấp xỉ hoặc không đặt cận cho log-likelihood cũng đã được đề xuất, chẳng hạn như score matching [18] và noise-contrastive estimation (NCE) [13]. Cả hai đều yêu cầu mật độ xác suất đã học được phải được đặc tả dưới dạng giải tích đến một hằng số chuẩn hóa. Lưu ý rằng trong nhiều mô hình sinh thú vị với nhiều lớp biến tiềm ẩn (chẳng hạn như DBN và DBM), thậm chí không thể suy ra một mật độ xác suất chưa được chuẩn hóa có thể xử lý được. Một số mô hình như denoising auto-encoders [30] và contractive autoencoders có các quy tắc học rất giống với score matching được áp dụng cho RBM. Trong NCE, cũng như trong công trình này, một tiêu chuẩn huấn luyện phân biệt được sử dụng để khớp một mô hình sinh. Tuy nhiên, thay vì khớp một mô hình phân biệt riêng biệt, chính mô hình sinh được sử dụng để phân biệt dữ liệu được tạo ra với các mẫu từ một phân bố nhiễu cố định. Do NCE sử dụng một phân bố nhiễu cố định, việc học chậm lại đáng kể sau khi mô hình đã học được ngay cả một phân bố gần đúng đúng trên một tập con nhỏ các biến được quan sát.

Cuối cùng, một số kỹ thuật không liên quan đến việc định nghĩa tường minh một phân bố xác suất, mà thay vào đó huấn luyện một máy sinh để rút ra các mẫu từ phân bố mong muốn. Cách tiếp cận này có ưu điểm là những máy như vậy có thể được thiết kế để được huấn luyện bằng lan truyền ngược. Các công trình nổi bật gần đây trong lĩnh vực này bao gồm khung generative stochastic network (GSN) [5], mở rộng generalized denoising auto-encoders [4]: cả hai có thể được xem như định nghĩa một chuỗi Markov có tham số hóa, tức là người ta học các tham số của một máy thực hiện một bước của một chuỗi Markov sinh. So với GSN, khung adversarial nets không yêu cầu một chuỗi Markov để lấy mẫu. Vì adversarial nets không yêu cầu các vòng phản hồi trong quá trình sinh, chúng có khả năng tận dụng tốt hơn các đơn vị tuyến tính từng đoạn [19, 9, 10], vốn cải thiện hiệu năng của lan truyền ngược nhưng gặp vấn đề với kích hoạt không bị chặn khi được sử dụng trong một vòng phản hồi. Các ví dụ gần đây hơn về việc huấn luyện một máy sinh bằng cách lan truyền ngược vào chính nó bao gồm các công trình gần đây về auto-encoding variational Bayes [20] và stochastic backpropagation [24].
