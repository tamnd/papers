---
paper: he-2016-resnet
title: Deep Residual Learning for Image Recognition
authors:
  - Kaiming He
  - Xiangyu Zhang
  - Shaoqing Ren
  - Jian Sun
year: 2016
venue: CVPR
field: ai-ml
section: "3"
section_title: Học sâu dư thừa
tag: 00FB
kind: section
lang: vi
source: arxiv:1512.03385
pdf_sha256: 1e0651b6810ecba34a3dbc5b5b0209226f889004607c1f203540a48d64e5a93a
pdf_pages: 3-4
extraction: vision
extraction_model: gpt-5
content_sha256: a7f2b65cb960ec8e12375aa0eed774b23b4164e1cfbe3eb43394e3118c02fe2b
translated_from: content/en/he-2016-resnet/03_deep_residual_learning.md
source_content_sha256: a8ffc42a9d910b352d9bea0a63f2a8ee47c2b20194464960c752a22d7741e5d5
translation_model: gpt-5
translation_run: 20260915T013833Z
glossary_version: 6
glossary_terms_sha256: 0d0a9334a40352952769479a6ad339487dd551fe3d836bae9914ea196d2f4310
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

### 3.1. Học dư thừa {#he-2016-resnet-s3-1 .section tag=0126}

Xét $\mathcal{H}(x)$ là một ánh xạ nền tảng cần được khớp bởi một vài lớp xếp chồng (không nhất thiết là toàn bộ mạng), với $x$ biểu thị các đầu vào của lớp đầu tiên trong số các lớp này. Nếu giả thuyết rằng nhiều lớp phi tuyến có thể xấp xỉ tiệm cận các hàm phức tạp[^1], thì tương đương với việc giả thuyết rằng chúng có thể xấp xỉ tiệm cận các hàm dư thừa, $i.e.$, $\mathcal{H}(x)-x$ (giả sử đầu vào và đầu ra có cùng số chiều). Vì vậy, thay vì kỳ vọng các lớp xếp chồng xấp xỉ $\mathcal{H}(x)$, chúng tôi cho phép rõ ràng các lớp này xấp xỉ một hàm dư thừa $\mathcal{F}(x):=\mathcal{H}(x)-x$. Do đó, hàm ban đầu trở thành $\mathcal{F}(x)+x$. Mặc dù cả hai dạng đều có thể xấp xỉ tiệm cận các hàm mong muốn (như đã giả thuyết), mức độ dễ học có thể khác nhau.

Cách cải biến này được thúc đẩy bởi các hiện tượng phản trực giác liên quan đến vấn đề suy giảm (Hình 1, bên trái). Như chúng tôi đã thảo luận trong phần giới thiệu, nếu các lớp được thêm vào có thể được xây dựng dưới dạng các ánh xạ đồng nhất, một mô hình sâu hơn sẽ có lỗi huấn luyện không lớn hơn mô hình tương ứng nông hơn của nó. Vấn đề suy giảm cho thấy các bộ giải có thể gặp khó khăn trong việc xấp xỉ các ánh xạ đồng nhất bằng nhiều lớp phi tuyến. Với cách cải biến học dư thừa, nếu các ánh xạ đồng nhất là tối ưu, các bộ giải có thể đơn giản đưa các trọng số của nhiều lớp phi tuyến về gần bằng không để tiến gần đến các ánh xạ đồng nhất.

Trong các trường hợp thực tế, khó có khả năng các ánh xạ đồng nhất là tối ưu, nhưng cách cải biến của chúng tôi có thể giúp tiền điều kiện hóa vấn đề. Nếu hàm tối ưu gần với một ánh xạ đồng nhất hơn là một ánh xạ không, bộ giải sẽ dễ dàng tìm thấy các nhiễu động có tham chiếu đến một ánh xạ đồng nhất hơn là học hàm đó như một hàm mới. Chúng tôi chỉ ra bằng các thí nghiệm (Hình 7) rằng các hàm dư thừa được học nhìn chung có phản hồi nhỏ, cho thấy các ánh xạ đồng nhất cung cấp sự tiền điều kiện hóa hợp lý.

### 3.2. Ánh xạ đồng nhất bằng các đường tắt {#he-2016-resnet-s3-2 .section tag=0127}

Chúng tôi áp dụng học dư thừa cho mỗi vài lớp xếp chồng. Một khối xây dựng được minh họa trong Hình 2. Về mặt hình thức, trong bài báo này chúng tôi xem xét một khối xây dựng được định nghĩa như sau:

$$
y=\mathcal{F}(x,\{W_i\})+x.
\tag{1}
$$
{#he-2016-resnet-eq-1 .equation tag=0118}

Ở đây $x$ và $y$ là các vectơ đầu vào và đầu ra của các lớp được xem xét. Hàm $\mathcal{F}(x,\{W_i\})$ biểu diễn ánh xạ dư thừa cần được học. Đối với ví dụ trong Hình 2 có hai lớp, $\mathcal{F}=W_2\sigma(W_1x)$ trong đó $\sigma$ biểu thị ReLU [29] và các độ lệch được bỏ qua để đơn giản hóa ký hiệu. Phép toán $\mathcal{F}+x$ được thực hiện bởi một kết nối đường tắt và phép cộng theo từng phần tử. Chúng tôi áp dụng tính phi tuyến thứ hai sau phép cộng ($i.e.$, $\sigma(y)$, xem Hình 2).

Các kết nối đường tắt trong Eqn.(1) không đưa vào thêm tham số hay độ phức tạp tính toán nào. Điều này không chỉ hấp dẫn trong thực tế mà còn quan trọng trong các so sánh của chúng tôi giữa mạng thông thường và mạng dư thừa. Chúng tôi có thể so sánh công bằng các mạng thông thường/dư thừa đồng thời có cùng số lượng tham số, độ sâu, độ rộng và chi phí tính toán (ngoại trừ phép cộng theo từng phần tử không đáng kể).

Các số chiều của $x$ và $\mathcal{F}$ phải bằng nhau trong Eqn.(1). Nếu không phải vậy ($e.g.$, khi thay đổi các kênh đầu vào/đầu ra), chúng tôi có thể thực hiện phép chiếu tuyến tính $W_s$ thông qua các kết nối đường tắt để khớp các số chiều:

$$
y=\mathcal{F}(x,\{W_i\})+W_sx.
\tag{2}
$$
{#he-2016-resnet-eq-2 .equation tag=0119}

Chúng tôi cũng có thể sử dụng một ma trận vuông $W_s$ trong Eqn.(1). Nhưng chúng tôi sẽ chỉ ra bằng các thí nghiệm rằng ánh xạ đồng nhất là đủ để giải quyết vấn đề suy giảm và mang tính kinh tế, do đó $W_s$ chỉ được sử dụng khi khớp các số chiều.

Dạng của hàm dư thừa $\mathcal{F}$ rất linh hoạt. Các thí nghiệm trong bài báo này liên quan đến một hàm $\mathcal{F}$ có hai hoặc ba lớp (Hình 5), trong khi có thể có nhiều lớp hơn. Nhưng nếu $\mathcal{F}$ chỉ có một lớp đơn, Eqn.(1) tương tự như một lớp tuyến tính: $y=W_1x+x$, và chúng tôi chưa quan sát thấy ưu điểm nào đối với trường hợp này.

Chúng tôi cũng lưu ý rằng mặc dù các ký hiệu trên nói về các lớp kết nối đầy đủ để đơn giản hóa, chúng vẫn áp dụng được cho các lớp tích chập. Hàm $\mathcal{F}(x,\{W_i\})$ có thể biểu diễn nhiều lớp tích chập. Phép cộng theo từng phần tử được thực hiện trên hai bản đồ đặc trưng, theo từng kênh.

### 3.3. Các kiến trúc mạng {#he-2016-resnet-s3-3 .section tag=0128}

Chúng tôi đã kiểm thử nhiều mạng thông thường/dư thừa khác nhau và quan sát thấy các hiện tượng nhất quán. Để cung cấp các ví dụ cho việc thảo luận, chúng tôi mô tả hai mô hình cho ImageNet như sau.

**Mạng thông thường.** Các đường cơ sở thông thường của chúng tôi (Hình 3, giữa) chủ yếu được truyền cảm hứng bởi triết lý của các mạng VGG [41] (Hình 3, trái). Các lớp tích chập chủ yếu có các bộ lọc $3\times3$ và tuân theo hai quy tắc thiết kế đơn giản: (i) đối với cùng kích thước bản đồ đặc trưng đầu ra, các lớp có cùng số lượng bộ lọc; và (ii) nếu kích thước bản đồ đặc trưng giảm một nửa, số lượng bộ lọc tăng gấp đôi để duy trì độ phức tạp thời gian trên mỗi lớp. Chúng tôi thực hiện giảm mẫu trực tiếp bằng các lớp tích chập có bước chạy là 2. Mạng kết thúc với một lớp pooling trung bình toàn cục và một lớp kết nối đầy đủ 1000 chiều với softmax. Tổng số lớp có trọng số là 34 trong Hình 3 (giữa).

Đáng chú ý là mô hình của chúng tôi có *ít bộ lọc hơn và độ phức tạp thấp hơn* so với các mạng VGG [41] (Hình 3, trái). Đường cơ sở 34 lớp của chúng tôi có 3.6 tỷ FLOPs (multipy-adds), chỉ bằng 18% của VGG-19 (19.6 tỷ FLOPs).

[^1]: Tuy nhiên, giả thuyết này vẫn là một câu hỏi mở. Xem [28].

Hình 3. Ví dụ về các kiến trúc mạng cho ImageNet. Bên trái: mô hình VGG-19 [41] (19.6 tỷ FLOPs) làm tham chiếu. Ở giữa: một mạng thường với 34 lớp tham số (3.6 tỷ FLOPs). Bên phải: một mạng dư với 34 lớp tham số (3.6 tỷ FLOPs). Các đường tắt nét chấm làm tăng kích thước. Bảng 1 trình bày thêm chi tiết và các biến thể khác. {#he-2016-resnet-fig-3 .figure tag=00E8}

Mạng dư. Dựa trên mạng thường ở trên, chúng tôi chèn các kết nối tắt (Hình 3, bên phải) để biến mạng thành phiên bản dư tương ứng. Các kết nối tắt ánh xạ đồng nhất (Eqn.(1)) có thể được sử dụng trực tiếp khi đầu vào và đầu ra có cùng kích thước (các kết nối tắt đường liền trong Hình 3). Khi kích thước tăng lên (các kết nối tắt đường chấm trong Hình 3), chúng tôi xem xét hai tùy chọn: (A) Kết nối tắt vẫn thực hiện ánh xạ đồng nhất, với các phần tử không bổ sung được đệm thêm để tăng kích thước. Tùy chọn này không đưa thêm tham số nào; (B) Kết nối tắt phép chiếu trong Eqn.(2) được sử dụng để khớp kích thước (thực hiện bằng các tích chập $1 \times 1$). Với cả hai tùy chọn, khi các kết nối tắt đi qua các bản đồ đặc trưng có hai kích thước, chúng được thực hiện với bước nhảy bằng 2.

### 3.4. Triển khai {#he-2016-resnet-s3-4 .section tag=00FF}

Triển khai của chúng tôi cho ImageNet tuân theo thực hành trong [[krizhevsky-2012-imagenet]], [41]. Ảnh được thay đổi kích thước với cạnh ngắn hơn được lấy mẫu ngẫu nhiên trong $[256, 480]$ để tăng cường theo tỷ lệ [41]. Một vùng cắt $224 \times 224$ được lấy mẫu ngẫu nhiên từ một ảnh hoặc ảnh lật ngang của nó, với giá trị trung bình trên mỗi điểm ảnh được trừ đi [[krizhevsky-2012-imagenet]]. Phép tăng cường màu chuẩn trong [[krizhevsky-2012-imagenet]] được sử dụng. Chúng tôi áp dụng chuẩn hóa theo lô (BN) [16] ngay sau mỗi phép tích chập và trước khi kích hoạt, theo [16]. Chúng tôi khởi tạo các trọng số như trong [13] và huấn luyện tất cả các mạng thường/dư từ đầu. Chúng tôi sử dụng SGD với kích thước lô nhỏ là 256. Tốc độ học bắt đầu từ 0.1 và được chia cho 10 khi lỗi đạt trạng thái bão hòa, và các mô hình được huấn luyện tối đa $60 \times 10^4$ lần lặp. Chúng tôi sử dụng suy giảm trọng số là 0.0001 và động lượng là 0.9. Chúng tôi không sử dụng dropout [14], theo thực hành trong [16].

Trong kiểm thử, để so sánh các nghiên cứu, chúng tôi áp dụng phép kiểm thử cắt 10 vùng tiêu chuẩn [[krizhevsky-2012-imagenet]]. Để đạt kết quả tốt nhất, chúng tôi áp dụng dạng tích chập đầy đủ như trong [41, 13], và lấy trung bình các điểm số ở nhiều tỷ lệ (các ảnh được thay đổi kích thước sao cho cạnh ngắn hơn nằm trong $\{224, 256, 384, 480, 640\}$).
