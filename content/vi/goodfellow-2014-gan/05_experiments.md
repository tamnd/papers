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
section: "5"
section_title: Thực nghiệm
tag: 00C9
kind: section
lang: vi
source: arxiv:1406.2661
pdf_sha256: ff5819e3a7b713c3bd3107b7de3d51fe0a347aa5d8444f0efdcf2345ef0a8b63
pdf_pages: 5-7
extraction: vision
extraction_model: gpt-6-astra
content_sha256: 2bbe7549c5807ac0ab0fcf705c2280e1b81466c7c72290ea5bfe6d8e866ae0b0
translated_from: content/en/goodfellow-2014-gan/05_experiments.md
source_content_sha256: 6e9e71cdcb721694c83f39a82661c91c3b69837dd0335f7d11ec5fea5de12d9a
translation_model: gpt-5
translation_run: 20260914T064759Z
glossary_version: 5
glossary_terms_sha256: 95f35b8eeca7e5d682ff5338deefc303c320897501e75661c72974f88e8865d4
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Chúng tôi đã huấn luyện các mạng đối kháng trên một loạt tập dữ liệu, bao gồm MNIST[[lecun-1998-lenet]], Toronto Face Database (TFD) [28] và CIFAR-10 [21]. Các mạng sinh sử dụng sự kết hợp giữa các hàm kích hoạt tuyến tính chỉnh lưu [19, 9] và các hàm kích hoạt sigmoid, trong khi mạng phân biệt sử dụng các hàm kích hoạt maxout [10]. Dropout [17] được áp dụng trong quá trình huấn luyện mạng phân biệt. Mặc dù khung lý thuyết của chúng tôi cho phép sử dụng dropout và các nhiễu khác tại các lớp trung gian của bộ sinh, chúng tôi chỉ sử dụng nhiễu làm đầu vào cho lớp thấp nhất của mạng bộ sinh.

Chúng tôi ước lượng xác suất của dữ liệu tập kiểm thử dưới $p_g$ bằng cách khớp một cửa sổ Parzen Gaussian với các mẫu được sinh bởi $G$ và báo cáo log-likelihood dưới phân phối này. Tham số $\sigma$

| Mô hình | MNIST | TFD |
|---|---|---|
| DBN [3] | $138 \pm 2$ | $1909 \pm 66$ |
| Stacked CAE [3] | $121 \pm 1.6$ | $\mathbf{2110 \pm 50}$ |
| Deep GSN [6] | $214 \pm 1.1$ | $1890 \pm 29$ |
| Mạng đối kháng | $\mathbf{225 \pm 2}$ | $\mathbf{2057 \pm 26}$ |

Bảng 1: Các ước lượng log-likelihood dựa trên cửa sổ Parzen. Các số được báo cáo trên MNIST là log-likelihood trung bình của các mẫu trên tập kiểm thử, với sai số chuẩn của trung bình được tính trên các ví dụ. Trên TFD, chúng tôi tính sai số chuẩn trên các fold của tập dữ liệu, với một $\sigma$ khác nhau được chọn bằng tập xác thực của mỗi fold. Trên TFD, $\sigma$ được xác thực chéo trên mỗi fold và log-likelihood trung bình trên mỗi fold được tính. Đối với MNIST, chúng tôi so sánh với các mô hình khác của phiên bản tập dữ liệu có giá trị thực (thay vì nhị phân). {#goodfellow-2014-gan-tab-1 .table tag=00CA}

của các Gaussian được xác định bằng xác thực chéo trên tập xác thực. Thủ tục này được giới thiệu trong Breuleux *et al.* [8] và được sử dụng cho nhiều mô hình sinh khác nhau mà likelihood chính xác không khả tính [25, 3, 5]. Kết quả được báo cáo trong Bảng 1. Phương pháp ước lượng likelihood này có phương sai tương đối cao và không hoạt động tốt trong các không gian có số chiều cao, nhưng theo hiểu biết của chúng tôi, đây là phương pháp tốt nhất hiện có. Những tiến bộ trong các mô hình sinh có thể lấy mẫu nhưng không thể ước lượng likelihood trực tiếp thúc đẩy nghiên cứu sâu hơn về cách đánh giá các mô hình như vậy.

Trong Hình 2 và 3, chúng tôi trình bày các mẫu được lấy từ mạng bộ sinh sau khi huấn luyện. Mặc dù chúng tôi không khẳng định rằng các mẫu này tốt hơn các mẫu được sinh bởi các phương pháp hiện có, chúng tôi tin rằng các mẫu này ít nhất có khả năng cạnh tranh với những mô hình sinh tốt hơn trong tài liệu và làm nổi bật tiềm năng của khung đối kháng.

Hình 2: Trực quan hóa các mẫu từ mô hình. Cột ngoài cùng bên phải cho thấy ví dụ huấn luyện gần nhất của mẫu lân cận, nhằm chứng minh rằng mô hình không ghi nhớ tập huấn luyện. Các mẫu là những phép lấy ngẫu nhiên công bằng, không được chọn lọc. Không giống như hầu hết các phép trực quan hóa khác của các mô hình sinh sâu, các ảnh này cho thấy các mẫu thực tế từ các phân phối của mô hình, chứ không phải các trung bình có điều kiện khi cho trước các mẫu của các đơn vị ẩn. Hơn nữa, các mẫu này không tương quan vì quá trình lấy mẫu không phụ thuộc vào sự trộn của chuỗi Markov. a) MNIST b) TFD c) CIFAR-10 (mô hình kết nối đầy đủ) d) CIFAR-10 (bộ phân biệt tích chập và bộ sinh “tích chập ngược”) {#goodfellow-2014-gan-fig-2 .figure tag=00CB}

Hình 3: Các chữ số thu được bằng cách nội suy tuyến tính giữa các tọa độ trong không gian $z$ của mô hình đầy đủ. {#goodfellow-2014-gan-fig-3 .figure tag=00CC}

|  | Các mô hình đồ thị sâu có hướng | Các mô hình đồ thị sâu vô hướng | Autoencoder sinh | Các mô hình đối kháng |
|---|---|---|---|---|
| Huấn luyện | Cần suy luận trong quá trình huấn luyện. | Cần suy luận trong quá trình huấn luyện. Cần MCMC để xấp xỉ gradient của hàm phân hoạch. | Áp đặt sự đánh đổi giữa sự trộn và năng lực của quá trình tái tạo sinh | Đồng bộ hóa bộ phân biệt với bộ sinh. Helvetica. |
| Suy luận | Suy luận xấp xỉ được học | Suy luận biến phân | Suy luận dựa trên MCMC | Suy luận xấp xỉ được học |
| Lấy mẫu | Không có khó khăn | Yêu cầu chuỗi Markov | Yêu cầu chuỗi Markov | Không có khó khăn |
| Đánh giá $p(x)$ | Không khả tính, có thể được xấp xỉ bằng AIS | Không khả tính, có thể được xấp xỉ bằng AIS | Không được biểu diễn tường minh, có thể được xấp xỉ bằng ước lượng mật độ Parzen | Không được biểu diễn tường minh, có thể được xấp xỉ bằng ước lượng mật độ Parzen |
| Thiết kế mô hình | Gần như mọi mô hình đều gặp khó khăn cực lớn | Cần thiết kế cẩn thận để bảo đảm nhiều tính chất | Về lý thuyết, mọi hàm khả vi đều được phép | Về lý thuyết, mọi hàm khả vi đều được phép |

Bảng 2: Những thách thức trong mô hình hóa sinh: tóm tắt những khó khăn gặp phải bởi các cách tiếp cận khác nhau đối với mô hình hóa sinh sâu cho từng phép toán chính liên quan đến một mô hình. {#goodfellow-2014-gan-tab-2 .table tag=00CD}
