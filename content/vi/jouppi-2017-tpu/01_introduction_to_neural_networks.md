---
paper: jouppi-2017-tpu
title: In-Datacenter Performance Analysis of a Tensor Processing Unit
authors:
  - Norman P. Jouppi
  - Cliff Young
  - Nishant Patil
  - David Patterson
  - Gaurav Agrawal
  - Raminder Bajwa
  - Sarah Bates
  - Suresh Bhatia
  - Nan Boden
  - Al Borchers
year: 2017
venue: ISCA
field: architecture
section: "1"
section_title: Giới thiệu về mạng nơ-ron
tag: 017D
kind: section
lang: vi
source: arxiv:1704.04760
pdf_sha256: 19793e4ae1486630ac45a12facabc0e80609dd679db8ca7a3a040f8bf0d8e0be
pdf_pages: 1-2
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 4cd042217e8fd5633afe60faf96f64412d4b8ffaabbff7d2fb866bc6dd6a2e25
translated_from: content/en/jouppi-2017-tpu/01_introduction_to_neural_networks.md
source_content_sha256: 374710ce6408937f7af94eed2da42a1089d99a9a0b702990b4f0325b2cc51c28
translation_model: gpt-6-astra
translation_run: 20260914T212037Z
glossary_version: 6
glossary_terms_sha256: 1f83355a83baacb04f1185b8bd47b133f28d2f764f5d7ae919d5d9d0d7e083ee
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Sự kết hợp giữa các tập dữ liệu lớn trên đám mây và số lượng lớn máy tính vận hành đám mây đã tạo nên sự hồi sinh của học máy. Đặc biệt, các mạng nơ-ron sâu (deep neural networks, DNN) đã mang lại những đột phá như giảm tỷ lệ lỗi từ trong nhận dạng tiếng nói xuống 30% so với các phương pháp truyền thống, mức cải thiện lớn nhất trong 20 năm [Dea16]; giảm tỷ lệ lỗi trong một cuộc thi nhận dạng ảnh từ 26% xuống 3.5% kể từ năm 2011 [Kri12] [Sze15] [He16]; và đánh bại một nhà vô địch cờ vây là con người [Sil16]. Khác với một số đối tượng ứng dụng của phần cứng, DNN có thể áp dụng cho nhiều bài toán, nên chúng tôi có thể tái sử dụng một ASIC chuyên dụng cho DNN để xây dựng các giải pháp về tiếng nói, thị giác, ngôn ngữ, dịch thuật, xếp hạng tìm kiếm và nhiều lĩnh vực khác.

Mạng nơ-ron (NN) hướng tới chức năng tương tự bộ não và dựa trên một nơ-ron nhân tạo đơn giản: một hàm phi tuyến (chẳng hạn như $\max(0, \text{ giá trị})$) của tổng có trọng số của các đầu vào. Các nơ-ron nhân tạo này được tập hợp thành các lớp, với đầu ra của một lớp trở thành đầu vào của lớp tiếp theo trong chuỗi. Phần “sâu” trong DNN xuất phát từ việc sử dụng nhiều hơn một vài lớp, vì các tập dữ liệu lớn trên đám mây cho phép xây dựng các mô hình chính xác hơn bằng cách dùng thêm các lớp và tăng kích thước lớp để nắm bắt các mẫu hoặc khái niệm ở cấp độ cao hơn, còn GPU cung cấp đủ năng lực tính toán để phát triển chúng.

Hai giai đoạn của NN được gọi là huấn luyện (hay học) và suy luận (hay dự đoán), tương ứng với phát triển và vận hành thực tế. Nhà phát triển chọn số lớp và kiểu NN, còn quá trình huấn luyện xác định các trọng số. Hiện nay, hầu như toàn bộ quá trình huấn luyện đều sử dụng số dấu phẩy động, đây là một lý do khiến GPU trở nên phổ biến. Một bước gọi là lượng tử hóa (quantization) chuyển số dấu phẩy động thành số nguyên có độ rộng nhỏ—thường chỉ 8 bit—vốn thường đủ tốt cho suy luận. Phép nhân số nguyên tám bit có thể tiêu thụ năng lượng ít hơn 6X và chiếm diện tích nhỏ hơn 6X so với phép nhân số dấu phẩy động 16 bit theo IEEE 754, còn lợi thế của phép cộng số nguyên là 13X về năng lượng và 38X về diện tích [Dal16].

Hiện nay có ba loại NN phổ biến:
1. Perceptron đa lớp (MLP): Mỗi lớp mới là một tập hợp các hàm phi tuyến của tổng có trọng số của tất cả đầu ra (kết nối đầy đủ) từ một lớp trước đó, trong đó các trọng số được tái sử dụng.
2. Mạng nơ-ron tích chập (CNN): Mỗi lớp kế tiếp là một tập hợp các hàm phi tuyến của các tổng có trọng số của những tập con đầu ra gần nhau trong không gian từ lớp trước đó, trong đó các trọng số cũng được tái sử dụng.
3. Mạng nơ-ron hồi quy (RNN): Mỗi lớp tiếp theo là một tập hợp các hàm phi tuyến của các tổng có trọng số của đầu ra và trạng thái trước đó. RNN phổ biến nhất là bộ nhớ dài ngắn hạn (Long Short-Term Memory, LSTM). Điểm tinh tế của LSTM nằm ở việc quyết định thông tin nào cần quên và thông tin nào cần truyền sang lớp tiếp theo dưới dạng trạng thái. Các trọng số được tái sử dụng qua các bước thời gian.

Bảng 1 trình bày hai ví dụ cho mỗi kiểu trong ba kiểu NN—đại diện cho 95% tải công việc suy luận NN trong các trung tâm dữ liệu của chúng tôi—mà chúng tôi dùng làm các phép đo chuẩn. Thường được viết bằng TensorFlow [Aba16], chúng ngắn đến ngạc nhiên: chỉ từ 100 đến 1500 dòng mã. Các phép đo chuẩn của chúng tôi là những phần nhỏ của các ứng dụng lớn hơn chạy trên server chủ, có thể gồm hàng nghìn đến hàng triệu dòng mã C++. Các ứng dụng thường phục vụ trực tiếp người dùng, dẫn đến những giới hạn nghiêm ngặt về thời gian phản hồi.

Mỗi mô hình cần từ 5M đến 100M trọng số (cột thứ 9 của Bảng 1), và việc truy cập chúng có thể tốn nhiều thời gian và năng lượng. Để phân bổ chi phí truy cập, cùng một bộ trọng số được tái sử dụng cho cả một lô ví dụ độc lập trong quá trình suy luận hoặc huấn luyện, qua đó cải thiện hiệu năng.

Bài báo này mô tả và đo lường Bộ xử lý Tensor (TPU), đồng thời so sánh hiệu năng và công suất tiêu thụ của nó trong suy luận với các CPU và GPU cùng thời. Dưới đây là các điểm nổi bật:
• Các ứng dụng suy luận thường chú trọng thời gian phản hồi hơn thông lượng vì chúng thường phục vụ trực tiếp người dùng.
• Do các giới hạn về độ trễ, GPU K80 chưa được khai thác hết khi thực hiện suy luận và chỉ nhanh hơn CPU Haswell một chút.
• Mặc dù có chip nhỏ hơn nhiều và công suất tiêu thụ thấp hơn, TPU có số lượng MAC gấp 25 lần và dung lượng bộ nhớ trên chip gấp 3.5 lần GPU K80.
• TPU thực hiện suy luận nhanh hơn GPU K80 và CPU Haswell khoảng 15X - 30X.
• Bốn trong sáu ứng dụng NN bị giới hạn bởi băng thông bộ nhớ trên TPU; nếu TPU được sửa đổi để có cùng hệ thống bộ nhớ như GPU K80, nó sẽ nhanh hơn GPU và CPU khoảng 30X - 50X.
• Hiệu năng/Watt của TPU gấp 30X - 80X các sản phẩm cùng thời; TPU được sửa đổi với bộ nhớ K80 sẽ tốt hơn 70X - 200X.
• Trong khi phần lớn các nhà thiết kế kiến trúc tập trung tăng tốc CNN, chúng chỉ chiếm 5% tải công việc trong trung tâm dữ liệu của chúng tôi.

```text
Name  LOC  Layers  Nonlinear function  Weights  TPU Ops / Weight Byte  TPU Batch Size  % of Deployed TPUs in July 2016
FC  Conv  Vector  Pool  Total
MLP0  100  5        5  ReLU  20M  200  200  61%
MLP1  1000  4        4  ReLU  5M  168  168
LSTMO  1000  24    34    58  sigmoid, tanh  52M  64  64  29%
LSTM1  1500  37    19    56  sigmoid, tanh  34M  96  96
CNN0  1000    16      16  ReLU  8M  2888  8  5%
CNN1  1000  4  72    13  89  ReLU  100M  1750  32
```

Bảng 1. Sáu ứng dụng NN (hai ứng dụng cho mỗi kiểu NN) đại diện cho 95% tải công việc của TPU. Các cột là tên NN; số dòng mã; các kiểu và số lượng lớp trong NN (FC là kết nối đầy đủ, Conv là tích chập, Vector là vectơ như tên gọi, Pool là phép gộp, thực hiện giảm kích thước phi tuyến trên TPU; và mức độ phổ biến của ứng dụng TPU vào tháng 7 năm 2016. Một DNN là RankBrain [Cla15]; một LSTM là một phần của GNM Translate [Wu16]; một CNN là Inception; và CNN còn lại là DeepMind AlphaGo [Sil16][Jou15]. {#jouppi-2017-tpu-tab-1 .table tag=017E}
