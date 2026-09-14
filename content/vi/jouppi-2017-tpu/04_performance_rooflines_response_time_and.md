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
section: "4"
section_title: 'Hiệu năng: Roofline, thời gian đáp ứng, và thông lượng'
tag: "0186"
kind: section
lang: vi
source: arxiv:1704.04760
pdf_sha256: 19793e4ae1486630ac45a12facabc0e80609dd679db8ca7a3a040f8bf0d8e0be
pdf_pages: 5-9
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 28aaa2ed48a651f12065d8bb2e9c6aea575b77cd1abd89b78510f4dc664a4074
translated_from: content/en/jouppi-2017-tpu/04_performance_rooflines_response_time_and.md
source_content_sha256: 6b6b8174b2e3962652b182bf128fa08c1c7dc24577908a423596b55f69629b72
translation_model: gpt-5
translation_run: 20260914T201546Z
glossary_version: 6
glossary_terms_sha256: 1f83355a83baacb04f1185b8bd47b133f28d2f764f5d7ae919d5d9d0d7e083ee
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Để minh họa hiệu năng của sáu ứng dụng trên ba bộ xử lý, chúng tôi điều chỉnh mô hình Hiệu năng Roofline từ lĩnh vực tính toán hiệu năng cao (HPC) [Wil09]. Mô hình trực quan đơn giản này không hoàn hảo, tuy nhiên nó cung cấp những hiểu biết về nguyên nhân của các nút thắt hiệu năng. Giả định đằng sau mô hình là các ứng dụng không vừa trong các cache on-chip, vì vậy chúng bị giới hạn bởi tính toán hoặc bị giới hạn bởi băng thông bộ nhớ. Đối với HPC, trục Y là hiệu năng theo số phép toán dấu phẩy động trên giây, do đó tốc độ tính toán cực đại tạo thành phần “phẳng” của đường mái. Trục X là cường độ vận hành, được đo bằng số phép toán dấu phẩy động trên mỗi byte DRAM được truy cập. Băng thông bộ nhớ là số byte trên giây, biến thành phần “xiên” của đường mái vì (FLOPS/sec)/(FLOPS/Byte) = Bytes/sec. Nếu không có đủ cường độ vận hành, một chương trình bị giới hạn bởi băng thông bộ nhớ và nằm dưới phần xiên của đường mái.

Figure 5. Đường mái TPU (die). Điểm đỉnh của nó nằm rất xa về bên phải tại 1350 phép toán trên mỗi byte của bộ nhớ trọng số được nạp. {#jouppi-2017-tpu-fig-5 .figure tag=0187}

Khoảng cách giữa số phép toán thực tế trên giây của một ứng dụng và mức trần ngay phía trên nó cho thấy lợi ích tiềm năng của việc tinh chỉnh hiệu năng thêm trong khi giữ nguyên cường độ vận hành; tất nhiên, các tối ưu hóa làm tăng cường độ vận hành (chẳng hạn như cache blocking) có thể mang lại lợi ích còn lớn hơn.

Để sử dụng mô hình Roofline cho TPU, khi các ứng dụng NN được lượng tử hóa, trước tiên chúng tôi thay thế các phép toán dấu phẩy động bằng các phép toán số nguyên. Vì các trọng số thường không vừa trong bộ nhớ on-chip đối với các ứng dụng NN, thay đổi thứ hai là định nghĩa lại cường độ vận hành thành số phép toán số nguyên trên mỗi byte của *weights* được đọc (xem cột thứ mười của Table 1).

Figure 5 cho thấy mô hình Roofline cho một die TPU đơn lẻ trên các thang đo log-log. TPU có một phần “xiên” dài của đường mái, trong đó cường độ vận hành có nghĩa là hiệu năng bị giới hạn bởi băng thông bộ nhớ thay vì bởi tính toán cực đại. Năm trong sáu ứng dụng đang chạm vào mức trần: các MLP và LSTM bị giới hạn bởi bộ nhớ, còn CNN bị giới hạn bởi tính toán. CNN1, mặc dù có cường độ vận hành rất cao, chỉ chạy ở 14.1 TOPS trong khi CNN0 chạy ở 86 TOPS.

Table 3 giải thích điều gì đã xảy ra với CNN1, dựa trên các bộ đếm hiệu năng cung cấp cho chúng tôi khả năng quan sát một phần hoạt động của TPU. TPU dành ít hơn một nửa số chu kỳ của nó để thực hiện các phép toán ma trận cho CNN1 (cột 7, hàng 1). Trong mỗi chu kỳ hoạt động đó, chỉ khoảng một nửa trong số 65,536 MAC chứa các trọng số hữu ích vì một số lớp trong CNN1 có độ sâu đặc trưng nhỏ. Khoảng 35% số chu kỳ được dành để chờ các trọng số được nạp từ bộ nhớ vào đơn vị ma trận, điều này xảy ra trong 4 lớp kết nối đầy đủ chạy ở cường độ vận hành chỉ 32 (xem Fallacy cuối cùng trong Section 8). Điều này để lại khoảng 19% số chu kỳ chưa được giải thích bởi các bộ đếm liên quan đến ma trận. Do thực thi chồng lấp trên TPU, chúng tôi không có hạch toán chính xác cho các chu kỳ đó, nhưng chúng tôi có thể thấy rằng 23% số chu kỳ có các lần dừng do các phụ thuộc RAW trong đường ống, và 1% được dành để dừng do đầu vào qua bus PCIe.

| Ứng dụng | MLP0 | MLP1 | LSTM0 | LSTM1 | CNN0 | CNN1 | Trung bình | Hàng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Các chu kỳ hoạt động của mảng | 12.7% | 10.6% | 8.2% | 10.5% | 78.2% | 46.2% | 28% | 1 |
| MAC hữu ích trong ma trận 64K (% cực đại) | 12.5% | 9.4% | 8.2% | 6.3% | 78.2% | 22.5% | 23% | 2 |
| MAC không được sử dụng | 0.3% | 1.2% | 0.0% | 4.2% | 0.0% | 23.7% | 5% | 3 |
| Các chu kỳ dừng do trọng số | 53.9% | 44.2% | 58.1% | 62.1% | 0.0% | 28.1% | 43% | 4 |
| Các chu kỳ dịch chuyển trọng số | 15.9% | 13.4% | 15.8% | 17.1% | 0.0% | 7.0% | 12% | 5 |
| Các chu kỳ không thuộc ma trận | 17.5% | 31.9% | 17.9% | 10.3% | 21.8% | 18.7% | 20% | 6 |
| Các lần dừng RAW | 3.3% | 8.4% | 14.6% | 10.6% | 3.5% | 22.8% | 11% | 7 |
| Các lần dừng dữ liệu đầu vào | 6.1% | 8.8% | 5.1% | 2.4% | 3.4% | 0.6% | 4% | 8 |
| TeraOps/sec (92 Peak) | 12.3 | 9.7 | 3.7 | 2.8 | 86.0 | 14.1 | 21.4 | 9 |

Table 3. Các yếu tố giới hạn hiệu năng TPU của tải công việc NN dựa trên các bộ đếm hiệu năng phần cứng. Các hàng 1, 4, 5, và 6 tổng cộng bằng 100% và dựa trên các phép đo hoạt động của đơn vị ma trận. Các hàng 2 và 3 tiếp tục phân rã phần nhỏ của 64K trọng số trong đơn vị ma trận chứa các trọng số hữu ích trong các chu kỳ hoạt động. Các bộ đếm của chúng tôi không thể giải thích chính xác thời gian khi đơn vị ma trận không hoạt động trong hàng 6; các hàng 7 và 8 hiển thị các bộ đếm cho hai nguyên nhân có thể, bao gồm các nguy cơ của đường ống RAW và các lần dừng đầu vào PCIe. Hàng 9 (TOPS) dựa trên các phép đo của mã sản xuất trong khi các hàng khác dựa trên các phép đo bộ đếm hiệu năng, vì vậy chúng không hoàn toàn nhất quán. Chi phí phụ trội của server máy chủ được loại trừ ở đây. Các MLP và LSTM bị giới hạn bởi băng thông bộ nhớ nhưng CNN thì không. Kết quả CNN1 được giải thích trong văn bản. {#jouppi-2017-tpu-tab-3 .table tag=0188}

Figure.

Figure 6. Đường mái CPU Intel Haswell (die) với điểm đỉnh tại 13 phép toán/byte, nằm xa hơn nhiều về bên trái so với trong Figure. 5. LSTM0 và MLP1 nhanh hơn trên Haswell so với K80, nhưng điều ngược lại xảy ra với các DNN khác. {#jouppi-2017-tpu-fig-6 .figure tag=0189}

Figure.

Figure 7. Đường mái GPU NVIDIA K80. Băng thông bộ nhớ cao hơn nhiều di chuyển điểm đỉnh đến 9 phép toán trên mỗi byte trọng số, thậm chí còn xa hơn về bên trái so với Figure 6. Các DNN thấp hơn nhiều so với đường Roofline của chúng do các giới hạn về thời gian đáp ứng (xem Table 4). {#jouppi-2017-tpu-fig-7 .figure tag=018A}

Hình 6 và 7 cho thấy các đường mái (roofline) cho một die Haswell đơn và một die K80 đơn. Sáu ứng dụng NN nhìn chung nằm xa hơn bên dưới các giới hạn của chúng so với TPU trong Hình 5. Thời gian đáp ứng là lý do. Nhiều ứng dụng NN này là các phần của các dịch vụ hướng đến người dùng cuối. Các nhà nghiên cứu đã chứng minh rằng những gia tăng nhỏ trong thời gian đáp ứng khiến khách hàng sử dụng một dịch vụ ít hơn [Sch09]. Vì vậy, trong khi huấn luyện có thể không có các thời hạn cứng về thời gian đáp ứng, suy luận thường có. Nghĩa là, suy luận ưu tiên độ trễ hơn thông lượng [Pat04].

Bảng 4 minh họa tác động của giới hạn thời gian đáp ứng phân vị thứ 99 là 7 ms đối với MLP0 trên Haswell và K80 [Dea13], giới hạn này được yêu cầu bởi nhà phát triển ứng dụng. (Số lần suy luận mỗi giây và độ trễ 7 ms bao gồm thời gian của server host cũng như thời gian của bộ tăng tốc.) Chúng hoạt động lần lượt ở mức 42% và 37% thông lượng cao nhất có thể đạt được cho MLP0 nếu giới hạn thời gian đáp ứng được nới lỏng. Vì vậy, mặc dù CPU và GPU có thông lượng tiềm năng cao hơn nhiều, nó bị lãng phí nếu chúng không đáp ứng giới hạn thời gian đáp ứng. Các cận này cũng ảnh hưởng đến TPU, nhưng ở mức 80% trong Bảng 4, nó đang hoạt động gần hơn nhiều với thông lượng MLP0 cao nhất của mình. So với CPU và GPU, TPU đơn luồng không có bất kỳ tính năng vi kiến trúc phức tạp nào tiêu tốn transistor và năng lượng để cải thiện trường hợp trung bình nhưng không cải thiện trường hợp phân vị thứ 99: không có cache, dự đoán nhánh, thực thi ngoài thứ tự, xử lý đa tiến trình, nạp trước đầu cơ, hợp nhất địa chỉ, đa luồng, chuyển đổi ngữ cảnh, v.v. Chủ nghĩa tối giản là một ưu điểm của các bộ xử lý chuyên biệt theo miền.

Bảng 3 cho thấy hiệu năng TPU, nhưng nó không tính đến thời gian của server host, thời gian này có thể được chia thành việc chạy phần ứng dụng trên host và việc giao tiếp với TPU. Bảng 5 liệt kê phần thứ hai, nhưng phần thứ nhất thì khó. Lý thuyết hàng đợi cho thấy các hàng đợi đầu vào dài làm tăng thông lượng, bằng cách đảm bảo rằng máy tính không bao giờ ở trạng thái nhàn rỗi, nhưng làm kéo dài thời gian đáp ứng. Vì vậy, hầu hết ứng dụng giữ cho các hàng đợi đầu vào của chúng trống. Tuy nhiên, chúng tôi không thể đo được khi nào TPU nhàn rỗi vì nó đang chờ CPU thực hiện phần ứng dụng của nó hoặc vì CPU cũng nhàn rỗi do hàng đợi đầu vào trống.

Bảng 6 đưa ra kết quả cuối cùng của hiệu năng suy luận tương đối trên mỗi die, bao gồm chi phí phụ trội của server host đối với hai bộ tăng tốc so với CPU. Cột áp chót cho thấy trung bình hình học của hiệu năng tương đối đối với sáu ứng dụng NN, cho thấy die K80 nhanh gấp 1.1X so với die Haswell, die TPU nhanh gấp 14.5 lần, và do đó die TPU nhanh gấp 13.2 lần so với die GPU. Hình 8 biểu diễn trực quan tốc độ tương đối của chúng.

Hãy nhớ rằng các kiến trúc sư sử dụng trung bình hình học khi họ không biết tổ hợp chương trình thực tế sẽ được chạy [Hen18]. Tuy nhiên, đối với nghiên cứu này, chúng tôi biết tổ hợp đó (Bảng 1). Trung bình có trọng số trong cột cuối cùng của Bảng 6 sử dụng tổ hợp thực tế làm tăng GPU lên 1.9X và TPU lên 29.2X, vì vậy die TPU hiện nhanh gấp 15.3 lần so với die GPU.

| Kiểu | Lô | Đáp ứng phân vị thứ 99 | Inf/s (IPS) | % Max IPS |
| --- | --- | --- | --- | --- |
| CPU | 16 | 7.2 ms | 5,482 | 42% |
| CPU | 64 | 21.3 ms | 13,194 | 100% |
| GPU | 16 | 6.7 ms | 13,461 | 37% |
| GPU | 64 | 8.3 ms | 36,465 | 100% |
| TPU | 200 | 7.0 ms | 225,000 | 80% |
| TPU | 250 | 10.0 ms | 280,000 | 100% |

Bảng 4. Thời gian đáp ứng phân vị thứ 99 và thông lượng trên mỗi die (IPS) cho MLP0 khi kích thước lô thay đổi đối với MLP0. Độ trễ cho phép dài nhất là 7 ms. Đối với GPU và TPU, thông lượng MLP0 tối đa bị giới hạn bởi chi phí phụ trội của server host. Kích thước lô lớn hơn làm tăng thông lượng, nhưng như văn bản giải thích, thời gian đáp ứng dài hơn của chúng vượt quá giới hạn, vì vậy CPU và GPU phải sử dụng kích thước lô nhỏ hơn, kém hiệu quả hơn (16 so với 200). {#jouppi-2017-tpu-tab-4 .table tag=018B}

| MLP0 | MLP1 | LSTM0 | LSTM1 | CNN0 | CNN1 |
| --- | --- | --- | --- | --- | --- |
| 21% | 76% | 11% | 20% | 51% | 14% |

Bảng 5. Thời gian để CPU host tương tác với TPU được biểu diễn dưới dạng phần trăm thời gian thực thi TPU (từ các bộ đếm hiệu năng TPU). Phần này là thời gian CPU và TPU giao tiếp qua bus PCIe, không bao gồm thời gian CPU thực hiện một phần của ứng dụng nhưng không tương tác với TPU. Như văn bản giải thích, TPU khó đo được liệu CPU đang nhàn rỗi hay đang làm việc trên ứng dụng. {#jouppi-2017-tpu-tab-5 .table tag=018C}

| Kiểu | MLP0 | MLP1 | LSTM0 | LSTM1 | CNN0 | CNN1 | GM | WM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GPU | 2.5 | 0.3 | 0.4 | 1.2 | 1.6 | 2.7 | 1.1 | 1.9 |
| TPU | 41.0 | 18.5 | 3.5 | 1.2 | 40.3 | 71.0 | 14.5 | 29.2 |
| Ratio | 16.7 | 60.0 | 8.0 | 1.0 | 25.4 | 26.3 | 13.2 | 15.3 |

Bảng 6. Hiệu năng die GPU K80 và die TPU tương đối so với CPU đối với tải công việc NN. GM và WM là trung bình hình học và trung bình có trọng số (sử dụng tổ hợp thực tế của sáu ứng dụng trong Bảng 1). Hiệu năng tương đối của GPU và TPU bao gồm chi phí phụ trội của server host. MLP và CNN hoạt động tốt trên TPU. Bảng 4 giải thích rằng TPU có thể có kích thước lô lớn hơn và vẫn đáp ứng các giới hạn thời gian, làm tăng số phép toán trên mỗi byte (Bảng 1) hoặc tương đương, giảm số lần truy cập bộ nhớ trên mỗi phép toán. Ngoài ra, CNN theo bản chất có khả năng tái sử dụng trọng số lớn hơn và do đó có số phép toán trên mỗi byte cao hơn. Vì vậy, băng thông bộ nhớ thấp hơn của TPU không làm giảm đáng kể hiệu năng CNN. {#jouppi-2017-tpu-tab-6 .table tag=018D}

Hình 8. Các Hình 5-7 được kết hợp thành một đồ thị log-log duy nhất. Các ngôi sao là TPU, các tam giác là K80, và các hình tròn là Haswell. Tất cả các ngôi sao TPU đều nằm tại hoặc trên hai đường mái còn lại. {#jouppi-2017-tpu-fig-8 .figure tag=018E}

Hình 9. Hiệu năng tương đối/Watt (TDP) của server GPU (thanh màu xanh lam) và server TPU (thanh màu đỏ) so với server CPU, và server TPU so với server GPU (thanh màu cam). TPU’ là một TPU được cải tiến (Mục 7). Thanh màu xanh lục cho thấy tỷ lệ của nó so với server CPU và thanh màu tím nhạt cho thấy mối quan hệ của nó với server GPU. Tổng bao gồm công suất của server máy chủ, nhưng phần gia tăng thì không. GM và WM là các trung bình hình học và có trọng số. {#jouppi-2017-tpu-fig-9 .figure tag=018F}
