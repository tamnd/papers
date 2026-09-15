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
content_sha256: 1c723edb9855feb47259feff3a5f205577633cb6c5c2f2e5c5707e1f15609084
translated_from: content/en/goodfellow-2014-gan/05_experiments.md
source_content_sha256: 6e9e71cdcb721694c83f39a82661c91c3b69837dd0335f7d11ec5fea5de12d9a
translation_model: gpt-6-astra
translation_run: 20260915T022520Z
glossary_version: 6
glossary_terms_sha256: 0d0a9334a40352952769479a6ad339487dd551fe3d836bae9914ea196d2f4310
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Chúng tôi đã huấn luyện các mạng đối kháng (adversarial nets) trên nhiều tập dữ liệu, bao gồm MNIST[[lecun-1998-lenet]], Toronto Face Database (TFD) [28] và CIFAR-10 [21]. Các mạng sinh sử dụng kết hợp các hàm kích hoạt tuyến tính chỉnh lưu [19, 9] và các hàm kích hoạt sigmoid, trong khi mạng phân biệt sử dụng các hàm kích hoạt maxout [10]. Dropout [17] được áp dụng khi huấn luyện mạng phân biệt. Mặc dù khung lý thuyết của chúng tôi cho phép sử dụng dropout và các dạng nhiễu khác tại các lớp trung gian của bộ sinh, chúng tôi chỉ đưa nhiễu vào lớp dưới cùng của mạng sinh.

Chúng tôi ước lượng xác suất của dữ liệu tập kiểm thử theo $p_g$ bằng cách khớp một cửa sổ Parzen Gauss với các mẫu được sinh bằng $G$ và báo cáo log hợp lý (log-likelihood) theo phân phối này. Tham số $\sigma$

| Mô hình | MNIST | TFD |
|---|---|---|
| DBN [3] | $138 \pm 2$ | $1909 \pm 66$ |
| CAE xếp chồng [3] | $121 \pm 1.6$ | $\mathbf{2110 \pm 50}$ |
| GSN sâu [6] | $214 \pm 1.1$ | $1890 \pm 29$ |
| Mạng đối kháng | $\mathbf{225 \pm 2}$ | $\mathbf{2057 \pm 26}$ |

Bảng 1: Các ước lượng log hợp lý dựa trên cửa sổ Parzen. Các số được báo cáo trên MNIST là log hợp lý trung bình của các mẫu trong tập kiểm thử, với sai số chuẩn của trung bình được tính trên các mẫu. Trên TFD, chúng tôi tính sai số chuẩn trên các phần chia của tập dữ liệu, với một $\sigma$ khác nhau được chọn bằng tập thẩm định của từng phần chia. Trên TFD, $\sigma$ được thẩm định chéo trên từng phần chia và log hợp lý trung bình trên từng phần chia được tính toán. Với MNIST, chúng tôi so sánh với các mô hình khác trên phiên bản có giá trị thực (thay vì nhị phân) của tập dữ liệu. {#goodfellow-2014-gan-tab-1 .table tag=00CA}

của các phân phối Gauss được xác định bằng thẩm định chéo trên tập thẩm định. Thủ tục này được giới thiệu bởi Breuleux *và cộng sự* [8] và được sử dụng cho nhiều mô hình sinh mà việc tính chính xác hợp lý là bất khả thi [25, 3, 5]. Kết quả được báo cáo trong Bảng 1. Phương pháp ước lượng hợp lý này có phương sai tương đối cao và hoạt động không tốt trong các không gian nhiều chiều, nhưng theo hiểu biết của chúng tôi, đây là phương pháp tốt nhất hiện có. Những tiến bộ trong các mô hình sinh có thể lấy mẫu nhưng không thể trực tiếp ước lượng hợp lý thúc đẩy việc nghiên cứu thêm về cách đánh giá các mô hình như vậy.

Trong Hình 2 và 3, chúng tôi trình bày các mẫu được lấy từ mạng sinh sau khi huấn luyện. Mặc dù chúng tôi không khẳng định rằng các mẫu này tốt hơn các mẫu được sinh bằng những phương pháp hiện có, chúng tôi tin rằng các mẫu này ít nhất có thể cạnh tranh với các mô hình sinh tốt hơn trong tài liệu nghiên cứu và cho thấy tiềm năng của khung đối kháng.

Hình 2: Trực quan hóa các mẫu từ mô hình. Cột ngoài cùng bên phải hiển thị mẫu huấn luyện gần nhất với mẫu ở bên cạnh, nhằm chứng minh rằng mô hình chưa ghi nhớ tập huấn luyện. Các mẫu được lấy ngẫu nhiên một cách công bằng, không được chọn lọc có chủ đích. Khác với phần lớn các hình trực quan hóa mô hình sinh sâu khác, những hình ảnh này thể hiện các mẫu thực sự từ các phân phối của mô hình, không phải các giá trị trung bình có điều kiện khi cho trước các mẫu của các đơn vị ẩn. Hơn nữa, các mẫu này không tương quan vì quá trình lấy mẫu không phụ thuộc vào sự trộn của chuỗi Markov. a) MNIST b) TFD c) CIFAR-10 (mô hình kết nối đầy đủ) d) CIFAR-10 (bộ phân biệt tích chập và bộ sinh “giải tích chập”) {#goodfellow-2014-gan-fig-2 .figure tag=00CB}

Hình 3: Các chữ số thu được bằng cách nội suy tuyến tính giữa các tọa độ trong không gian $z$ của mô hình đầy đủ. {#goodfellow-2014-gan-fig-3 .figure tag=00CC}

|  | Mô hình đồ thị có hướng sâu | Mô hình đồ thị vô hướng sâu | Bộ tự mã hóa sinh | Mô hình đối kháng |
|---|---|---|---|---|
| Huấn luyện | Cần suy luận trong quá trình huấn luyện. | Cần suy luận trong quá trình huấn luyện. Cần MCMC để xấp xỉ gradient của hàm phân hoạch. | Buộc phải đánh đổi giữa sự trộn và khả năng sinh tái tạo | Đồng bộ hóa bộ phân biệt với bộ sinh. Helvetica. |
| Suy luận | Suy luận xấp xỉ được học | Suy luận biến phân | Suy luận dựa trên MCMC | Suy luận xấp xỉ được học |
| Lấy mẫu | Không có khó khăn | Cần chuỗi Markov | Cần chuỗi Markov | Không có khó khăn |
| Đánh giá $p(x)$ | Không thể tính toán khả thi, có thể xấp xỉ bằng AIS | Không thể tính toán khả thi, có thể xấp xỉ bằng AIS | Không được biểu diễn tường minh, có thể xấp xỉ bằng ước lượng mật độ Parzen | Không được biểu diễn tường minh, có thể xấp xỉ bằng ước lượng mật độ Parzen |
| Thiết kế mô hình | Gần như mọi mô hình đều gặp khó khăn cực lớn | Cần thiết kế cẩn thận để bảo đảm nhiều tính chất | Về lý thuyết, cho phép mọi hàm khả vi | Về lý thuyết, cho phép mọi hàm khả vi |

Bảng 2: Những thách thức trong mô hình hóa sinh: tóm tắt các khó khăn mà những cách tiếp cận khác nhau đối với mô hình hóa sinh sâu gặp phải trong từng thao tác chính liên quan đến một mô hình. {#goodfellow-2014-gan-tab-2 .table tag=00CD}
