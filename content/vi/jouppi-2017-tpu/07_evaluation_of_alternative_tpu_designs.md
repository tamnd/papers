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
section: "7"
section_title: Đánh giá các thiết kế TPU thay thế
tag: "0192"
kind: section
lang: vi
source: arxiv:1704.04760
pdf_sha256: 19793e4ae1486630ac45a12facabc0e80609dd679db8ca7a3a040f8bf0d8e0be
pdf_pages: 10-12
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 1c71ad0cf312badc862e368cf74efaf7eeba0c44ea9784b63f91c0abbbbab1db
translated_from: content/en/jouppi-2017-tpu/07_evaluation_of_alternative_tpu_designs.md
source_content_sha256: cbc44598e387dbade95f3923e473f77cbb158031fcce3e02d4bb7591cec14fad
translation_model: gpt-5
translation_run: 20260914T201546Z
glossary_version: 6
glossary_terms_sha256: 1f83355a83baacb04f1185b8bd47b133f28d2f764f5d7ae919d5d9d0d7e083ee
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Giống như một FPU, bộ đồng xử lý TPU có kiến trúc vi mô (microarchitecture) tương đối dễ đánh giá, vì vậy chúng tôi đã tạo một mô hình hiệu năng (performance model) cho sáu ứng dụng của mình. Bảng 7 cho thấy sự khác biệt giữa các kết quả của mô hình và các bộ đếm hiệu năng phần cứng, với giá trị trung bình dưới 10%. Sau đó chúng tôi mô hình hóa hiệu năng khi thay đổi băng thông bộ nhớ, tần số xung nhịp và số lượng bộ tích lũy, cùng với kích thước của đơn vị nhân ma trận.

Hình 11 cho thấy độ nhạy hiệu năng trung bình của khuôn TPU khi chúng tôi mở rộng các tham số này trong phạm vi từ 0.25x đến 4x. Hình này biểu diễn các giá trị trung bình có trọng số, nhưng các giá trị trung bình hình học trông tương tự. Ngoài việc đánh giá tác động của chỉ tăng tần số xung nhịp (clock trong Hình 11), chúng tôi cũng biểu diễn một thiết kế (clock+) trong đó tần số xung nhịp được tăng lên và số lượng bộ tích lũy được mở rộng tương ứng để trình biên dịch có thể giữ nhiều tham chiếu bộ nhớ hơn đang được xử lý. Tương tự, chúng tôi biểu diễn việc mở rộng đơn vị ma trận nếu tăng số lượng bộ tích lũy theo bình phương của mức tăng ở một chiều (matrix+), vì số lượng bộ nhân trong ma trận tăng theo cả hai chiều, cũng như chỉ tăng riêng đơn vị ma trận (matrix).

| MLP0 | MLP1 | LSTM0 | LSTM1 | CNN0 | CNN1 |
| --- | --- | --- | --- | --- | --- |
| 6.8% | 10.9% | 7.7% | 5.4% | 8.2% | 11.2% |

Bảng 7. Sự khác biệt về số chu kỳ xung nhịp giữa các bộ đếm hiệu năng phần cứng TPU và mô hình hiệu năng TPU. Giá trị trung bình là 8%. {#jouppi-2017-tpu-tab-7 .table tag=0193}

Hình 10. Watts/khuôn cho CNN0 khi mức sử dụng nền tảng mục tiêu thay đổi từ 0% đến 100%. Công suất GPU và TPU Tổng cộng là các đường màu đỏ và cam, còn công suất Tăng thêm của chúng là các đường màu xanh lá và tím. (Đường màu xanh dương là công suất của CPU Haswell, theo định nghĩa là công suất Tổng cộng.) Một server có 2 CPU và 8 GPU hoặc 4 TPU, vì vậy chúng tôi chuẩn hóa công suất bằng cách chia lần lượt cho 2, 8 và 4. {#jouppi-2017-tpu-fig-10 .figure tag=0194}

Hình 11. Hiệu năng TPU trung bình có trọng số khi các chỉ số thay đổi từ 0.25x đến 4x: băng thông bộ nhớ, tần số xung nhịp + bộ tích lũy, tần số xung nhịp, kích thước đơn vị ma trận + bộ tích lũy, và kích thước đơn vị ma trận. Giá trị trung bình có trọng số khiến việc nhận biết đóng góp của từng DNN trở nên khó khăn, nhưng MLP và LSTM cải thiện 3X với băng thông bộ nhớ 4X, nhưng không nhận được gì từ xung nhịp cao hơn. Đối với CNN thì ngược lại; 2X với xung nhịp 4X, nhưng nhận được ít lợi ích từ bộ nhớ nhanh hơn. Một đơn vị nhân ma trận lớn hơn không giúp ích cho bất kỳ DNN nào. {#jouppi-2017-tpu-fig-11 .figure tag=0195}

Thứ nhất, việc tăng băng thông bộ nhớ (memory) có tác động lớn nhất: hiệu năng cải thiện trung bình 3X khi bộ nhớ tăng 4X. Thứ hai, tần số xung nhịp có ít lợi ích trung bình dù có hay không có thêm bộ tích lũy. Lý do là MLP và LSTM bị giới hạn bởi bộ nhớ nhưng chỉ CNN bị giới hạn bởi tính toán. Mặc dù khó thấy trong Hình 11, vì hình này chỉ hiển thị giá trị trung bình có trọng số của cả sáu DNN, việc tăng tần số xung nhịp lên 4X hầu như không có tác động đến MLP và LSTM nhưng cải thiện hiệu năng của CNN khoảng 2X. Thứ ba, hiệu năng trung bình trong Hình 11 hơi *giảm* khi đơn vị ma trận mở rộng từ 256x256 lên 512x512 cho tất cả ứng dụng, bất kể chúng có nhận thêm bộ tích lũy hay không. Vấn đề này tương tự như phân mảnh nội bộ của các trang lớn, chỉ tệ hơn vì nó xảy ra trong hai chiều. Xét ma trận 600x600 được sử dụng trong LSTM1. Với một đơn vị ma trận 256x256, cần 9 bước để lát ma trận 600x600, tổng cộng mất 18 us thời gian. Đơn vị 512x512 lớn hơn chỉ cần bốn bước, nhưng mỗi bước mất thời gian dài gấp bốn lần, tổng cộng 32 us. Các lệnh CISC của chúng tôi dài, vì vậy giải mã không đáng kể và không che giấu được chi phí phụ trội của việc tải từ DRAM.

Bảng 8 cho thấy mức sử dụng của Unified Buffer 24 MiB, ban đầu được định kích thước để cho phép MLP chạy với kích thước lô lên đến 2048. Gần đây chúng tôi đã cải thiện bộ cấp phát lưu trữ cho Unified Buffer, giúp giảm bộ nhớ cần thiết cho ứng dụng lớn nhất trong sáu ứng dụng xuống còn 14 MiB. Trong 18 tháng đầu tiên triển khai, TPU sử dụng toàn bộ dung lượng của nó trong khi bộ cấp phát mới được phát triển. Hiện nay dung lượng bổ sung tạo ra khoảng dự phòng cho việc áp dụng các mô hình lớn hơn.

Tiếp theo chúng tôi sử dụng mô hình hiệu năng để đánh giá một khuôn TPU giả định (*TPU'*) có thể đã được thiết kế trong cùng công nghệ quy trình nếu chúng tôi có hơn 15 tháng. Việc tổng hợp logic và thiết kế khối tích cực hơn có thể đã tăng tần số xung nhịp lên 50%. Thiết kế một mạch giao diện cho bộ nhớ GDDR5, như trong K80, sẽ cải thiện băng thông Weight Memory hơn *năm* lần, dịch chuyển điểm gờ roofline của nó từ 1350 xuống 250. Như Hình 11 cho thấy, tăng tần số xung nhịp lên 1050 MHz nhưng không hỗ trợ bộ nhớ hầu như không tạo ra thay đổi. Nếu chúng tôi giữ xung nhịp ở 700 MHz nhưng sử dụng GDDR5 cho Weight Memory, mức tăng trung bình hình học tăng lên 2.6 đầy ấn tượng và trung bình có trọng số tăng lên 3.9. Thực hiện cả hai việc làm tăng trung bình hình học (2.9) nhưng không tăng trung bình có trọng số, vì vậy TPU’ chỉ có bộ nhớ nhanh hơn.

Hình 11 *không* bao gồm thời gian của server máy chủ. Chúng tôi sử dụng Bảng 5 để tính toán thời gian cho chi phí phụ trội tương tác với server máy chủ của TPU. Việc thêm cùng khoảng thời gian bổ sung đó làm giảm các giá trị trung bình của TPU’ từ 2.6 xuống 1.9 và từ 3.9 xuống 3.2. Thay đổi này vừa lạc quan, vì nó không bao gồm thời gian CPU để chạy phần ứng dụng của nó, vừa bi quan, vì chúng tôi có khả năng sẽ tinh chỉnh mạnh mã máy chủ khi có một TPU’ nhanh hơn 3X.

Thay thế chỉ Weight Memory DDR3 bằng bộ nhớ GDDR5 tương đương yêu cầu tăng gấp đôi số kênh bộ nhớ lên bốn. Cải tiến này sẽ mở rộng kích thước khuôn khoảng 10%. Tuy nhiên, băng thông bộ nhớ cao hơn làm giảm áp lực lên Unified Buffer, vì vậy việc giảm Unified Buffer xuống 14 MiB có thể lấy lại 10% diện tích. GDDR5 cũng sẽ tăng ngân sách công suất hệ thống TPU từ 861 Watts lên khoảng 900 Watts, vì có 4 TPU trên mỗi server.

Hình 9 ở trên cho thấy hiệu năng tổng thể/Watt/khuôn tương đối của TPU’ tăng vọt lên 31X - 86X so với Haswell và 25X - 41X so với K80. Chỉ số gia tăng tăng vọt lên mức đáng kinh ngạc 69X - 196X so với Haswell và 42X - 68X so với K80.

| MLP0 | MLP1 | LSTM0 | LSTM1 | CNN0 | CNN1 |
| --- | --- | --- | --- | --- | --- |
| 11.0 | 2.3 | 4.8 | 4.5 | 1.5 | 13.9 |

Bảng 8. MiB tối đa của Unified Buffer 24 MiB được sử dụng cho mỗi ứng dụng NN. Một Unified Buffer 14 MiB là đủ cho các ứng dụng này. {#jouppi-2017-tpu-tab-8 .table tag=0196}
