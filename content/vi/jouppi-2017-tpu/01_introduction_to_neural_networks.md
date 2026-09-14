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
content_sha256: 3f2e28a582ddda8f2ae880d59a8868595bc2124a7dd222ec4d9e28793b27b57a
translated_from: content/en/jouppi-2017-tpu/01_introduction_to_neural_networks.md
source_content_sha256: 374710ce6408937f7af94eed2da42a1089d99a9a0b702990b4f0325b2cc51c28
translation_model: gpt-5
translation_run: 20260914T201546Z
glossary_version: 6
glossary_terms_sha256: 1f83355a83baacb04f1185b8bd47b133f28d2f764f5d7ae919d5d9d0d7e083ee
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Sự cộng hưởng giữa các tập dữ liệu lớn trên đám mây và vô số máy tính cung cấp năng lực tính toán cho chúng đã tạo nên một thời kỳ phục hưng của học máy. Đặc biệt, các mạng nơ-ron sâu (DNN) đã tạo ra những đột phá như giảm tỷ lệ lỗi từ trong nhận dạng tiếng nói 30% so với các phương pháp truyền thống, mức cải thiện lớn nhất trong 20 năm [Dea16]; giảm tỷ lệ lỗi trong một cuộc thi nhận dạng ảnh từ 26% xuống 3.5% kể từ năm 2011 [Kri12] [Sze15] [He16]; và đánh bại một nhà vô địch con người trong cờ vây [Sil16]. Không giống một số đích phần cứng khác, DNN có thể áp dụng cho nhiều loại bài toán, vì vậy chúng ta có thể tái sử dụng một ASIC chuyên dụng cho DNN để giải quyết các bài toán về tiếng nói, thị giác, ngôn ngữ, dịch thuật, xếp hạng tìm kiếm và nhiều bài toán khác.

Mạng nơ-ron (NN) hướng tới chức năng tương tự não bộ và dựa trên một nơ-ron nhân tạo đơn giản: một hàm phi tuyến (chẳng hạn $\max(0, \text{ value})$) của tổng có trọng số của các đầu vào. Các nơ-ron nhân tạo này được tập hợp thành các lớp, trong đó đầu ra của một lớp trở thành đầu vào của lớp tiếp theo trong chuỗi. Phần “sâu” của DNN xuất phát từ việc vượt quá một vài lớp, vì các tập dữ liệu lớn trên đám mây cho phép xây dựng các mô hình chính xác hơn bằng cách sử dụng thêm các lớp lớn hơn để nắm bắt các mức cao hơn của mẫu hoặc khái niệm, còn GPU cung cấp đủ năng lực tính toán để phát triển chúng.

Hai giai đoạn của NN được gọi là huấn luyện (hoặc học) và suy luận (hoặc dự đoán), tương ứng với phát triển và sản xuất. Nhà phát triển lựa chọn số lớp và kiểu NN, còn quá trình huấn luyện xác định các trọng số. Hầu như toàn bộ quá trình huấn luyện ngày nay đều sử dụng số dấu phẩy động, đây là một trong những lý do GPU trở nên phổ biến đến vậy. Một bước gọi là lượng tử hóa chuyển đổi các số dấu phẩy động thành các số nguyên có độ rộng nhỏ — thường chỉ 8 bit — vốn thường đủ tốt cho suy luận. Phép nhân số nguyên 8 bit có thể tiêu tốn ít hơn 6X năng lượng và ít hơn 6X diện tích so với phép nhân số dấu phẩy động 16 bit IEEE 754, và lợi thế đối với phép cộng số nguyên là 13X về năng lượng và 38X về diện tích [Dal16].

Ba loại NN hiện nay phổ biến:
1. Multi-Layer Perceptrons (MLP): Mỗi lớp mới là một tập các hàm phi tuyến của tổng có trọng số của tất cả đầu ra (kết nối đầy đủ) từ lớp trước đó, qua đó tái sử dụng các trọng số.
2. Convolutional Neural Networks (CNN): Mỗi lớp tiếp theo là một tập các hàm phi tuyến của các tổng có trọng số của những tập con đầu ra gần nhau về không gian từ lớp trước đó, đồng thời tái sử dụng các trọng số.
3. Recurrent Neural Networks (RNN): Mỗi lớp tiếp theo là một tập hợp các hàm phi tuyến của các tổng có trọng số của các đầu ra và trạng thái trước đó. RNN phổ biến nhất là Long Short-Term Memory (LSTM). Nghệ thuật của LSTM nằm ở việc quyết định điều gì cần quên và điều gì cần truyền tiếp dưới dạng trạng thái tới lớp tiếp theo. Các trọng số được tái sử dụng qua các bước thời gian.

Bảng 1 cho thấy hai ví dụ của mỗi trong ba loại NN — đại diện cho 95% tải công việc suy luận NN trong các trung tâm dữ liệu của chúng tôi — được chúng tôi sử dụng làm các phép đo chuẩn. Thường được viết bằng TensorFlow [Aba16], chúng ngắn đáng ngạc nhiên: chỉ từ 100 đến 1500 dòng mã. Các phép đo chuẩn của chúng tôi là những phần nhỏ của các ứng dụng lớn hơn chạy trên server máy chủ, có thể gồm từ hàng nghìn đến hàng triệu dòng mã C++. Các ứng dụng thường hướng tới người dùng, dẫn đến các giới hạn nghiêm ngặt về thời gian đáp ứng.

Mỗi mô hình cần từ 5M đến 100M trọng số (cột thứ 9 của Bảng 1), việc truy cập chúng có thể tốn nhiều thời gian và năng lượng. Để phân bổ chi phí truy cập, cùng một trọng số được tái sử dụng trên một lô các mẫu độc lập trong quá trình suy luận hoặc huấn luyện, qua đó cải thiện hiệu năng.

Bài báo này mô tả và đo lường Tensor Processing Unit (TPU), đồng thời so sánh hiệu năng và công suất của nó cho suy luận với các CPU và GPU cùng thời. Dưới đây là phần xem trước các điểm nổi bật:
• Các ứng dụng suy luận thường ưu tiên thời gian đáp ứng hơn thông lượng vì chúng thường hướng tới người dùng.
• Do các giới hạn về độ trễ, GPU K80 không được tận dụng đầy đủ cho suy luận và chỉ nhanh hơn một chút so với CPU Haswell.
• Mặc dù có chip nhỏ hơn nhiều và công suất thấp hơn, TPU có số lượng MAC nhiều gấp 25 lần và bộ nhớ trên chip lớn gấp 3.5 lần so với GPU K80.
• TPU nhanh hơn khoảng 15X - 30X trong suy luận so với GPU K80 và CPU Haswell.
• Bốn trong sáu ứng dụng NN bị giới hạn bởi băng thông bộ nhớ trên TPU; nếu TPU được sửa đổi để có cùng hệ thống bộ nhớ như GPU K80, nó sẽ nhanh hơn GPU và CPU khoảng 30X - 50X.
• Hiệu năng/Watt của TPU cao hơn 30X - 80X so với các sản phẩm cùng thời; TPU được sửa đổi với bộ nhớ K80 sẽ tốt hơn 70X - 200X.
• Trong khi hầu hết các kiến trúc sư đã tăng tốc CNN, chúng chỉ chiếm 5% tải công việc trung tâm dữ liệu của chúng tôi.

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

Bảng 1. Sáu ứng dụng NN (hai ứng dụng cho mỗi loại NN) đại diện cho 95% tải công việc của TPU. Các cột là tên NN; số dòng mã; các kiểu và số lượng lớp trong NN (FC là kết nối đầy đủ, Conv là tích chập, Vector có ý nghĩa rõ ràng, Pool là pooling, thực hiện việc thu nhỏ phi tuyến trên TPU; và mức độ phổ biến của ứng dụng TPU vào tháng 7 năm 2016. Một DNN là RankBrain [Cla15]; một LSTM là một tập con của GNM Translate [Wu16]; một CNN là Inception; và CNN còn lại là DeepMind AlphaGo [Sil16][Jou15]. {#jouppi-2017-tpu-tab-1 .table tag=017E}
