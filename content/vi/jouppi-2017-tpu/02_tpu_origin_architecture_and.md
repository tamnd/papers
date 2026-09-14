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
section: "2"
section_title: Nguồn gốc, Kiến trúc và Triển khai TPU
tag: 017F
kind: section
lang: vi
source: arxiv:1704.04760
pdf_sha256: 19793e4ae1486630ac45a12facabc0e80609dd679db8ca7a3a040f8bf0d8e0be
pdf_pages: 2-5
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: e07f56c2e962e05100b1a0aca7565faa6a34aab2da1210c60193a90eb8f738b3
translated_from: content/en/jouppi-2017-tpu/02_tpu_origin_architecture_and.md
source_content_sha256: e90e3c6bc650eebea899710b61417f657b7a011da0bef3301e59df3cfaea90e4
translation_model: gpt-5
translation_run: 20260914T201546Z
glossary_version: 6
glossary_terms_sha256: 1f83355a83baacb04f1185b8bd47b133f28d2f764f5d7ae919d5d9d0d7e083ee
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Bắt đầu từ năm 2006, chúng tôi đã thảo luận về việc triển khai GPU, FPGA hoặc ASIC tùy biến trong các datacenter của mình. Chúng tôi kết luận rằng một số ít ứng dụng có thể chạy trên phần cứng chuyên dụng có thể được thực hiện gần như miễn phí bằng công suất dư thừa của các datacenter lớn, và rất khó cải thiện một thứ miễn phí. Cuộc thảo luận thay đổi vào năm 2013 khi một dự báo cho rằng nếu mọi người sử dụng tìm kiếm bằng giọng nói 3 phút mỗi ngày với các DNN nhận dạng tiếng nói, chúng tôi sẽ phải tăng gấp đôi số datacenter để đáp ứng nhu cầu tính toán, điều này sẽ rất tốn kém nếu đáp ứng bằng các CPU thông thường. Do đó, chúng tôi bắt đầu một dự án ưu tiên cao nhằm nhanh chóng sản xuất một ASIC tùy biến cho suy luận (và mua GPU có sẵn trên thị trường cho huấn luyện). Mục tiêu là cải thiện hiệu năng-chi phí lên 10X so với GPU. Theo yêu cầu này, TPU được thiết kế, kiểm chứng [Ste15], chế tạo và triển khai trong các datacenter chỉ trong 15 tháng. (Giới hạn về dung lượng khiến lượng thông tin và mức độ chi tiết về TPU trong bài báo này bị hạn chế; xem [Ros15a], [Ros15b], [Ros15c], [Ros15d], [Tho15] và [You15] để biết thêm.)

Thay vì tích hợp chặt chẽ với CPU, nhằm giảm khả năng làm chậm quá trình triển khai, TPU được thiết kế như một bộ đồng xử lý trên bus I/O PCIe, cho phép cắm nó vào các server hiện có giống như GPU. Ngoài ra, để đơn giản hóa thiết kế phần cứng và gỡ lỗi, server máy chủ gửi các lệnh TPU để TPU thực thi thay vì tự lấy chúng.

Do đó, về bản chất, TPU gần với một bộ đồng xử lý FPU (floating-point unit) hơn là GPU.

Hình.

Hình 1. Sơ đồ khối TPU. Bộ phận tính toán chính là đơn vị Matrix Multiply màu vàng ở góc trên bên phải. Đầu vào của nó là Weight FIFO màu xanh và Unified Buffer (UB) màu xanh, còn đầu ra là các Accumulators (Acc) màu xanh. Activation Unit màu vàng thực hiện các hàm phi tuyến trên Acc, sau đó các kết quả này được đưa vào UB. {#jouppi-2017-tpu-fig-1 .figure tag=0180}

Hình.

Hình 2. Sơ đồ bố trí khuôn TPU. Phần tô bóng tuân theo Hình 1. Các bộ đệm dữ liệu màu nhạt (xanh) chiếm 37% khuôn, phần tính toán màu nhạt (vàng) chiếm 30%, I/O màu trung bình (xanh lục) chiếm 10%, và phần điều khiển màu đậm (đỏ) chỉ chiếm 2%. Phần điều khiển lớn hơn nhiều (và khó thiết kế hơn nhiều) trong CPU hoặc GPU {#jouppi-2017-tpu-fig-2 .figure tag=0181}

Mục tiêu là chạy toàn bộ các mô hình suy luận trên TPU để giảm tương tác với CPU máy chủ và đủ linh hoạt để đáp ứng nhu cầu NN của năm 2015 và những năm sau đó, thay vì chỉ đáp ứng những gì cần thiết cho các NN năm 2013. Hình 1 cho thấy sơ đồ khối của TPU.

Các lệnh TPU được gửi từ máy chủ qua bus PCIe Gen3 x16 vào một bộ đệm lệnh. Các khối bên trong thường được kết nối với nhau bằng các đường truyền rộng 256 byte. Bắt đầu từ góc trên bên phải, Matrix Multiply Unit là trung tâm của TPU. Nó chứa 256x256 MAC có thể thực hiện phép nhân-cộng 8-bit trên các số nguyên có dấu hoặc không dấu. Các tích 16-bit được tập hợp trong 4 MiB Accumulators 32-bit bên dưới đơn vị ma trận. 4MiB biểu diễn 4096 accumulator 32-bit, mỗi accumulator gồm 256 phần tử. Đơn vị ma trận tạo ra một tổng từng phần gồm 256 phần tử trong mỗi chu kỳ xung nhịp. Chúng tôi chọn 4096 bằng cách trước hết nhận thấy rằng số phép toán trên mỗi byte cần thiết để đạt hiệu năng cực đại (điểm gối roofline trong Section 4) là ~1350, nên chúng tôi làm tròn lên 2048 rồi nhân đôi nó để trình biên dịch có thể sử dụng double buffering khi chạy ở hiệu năng cực đại.

Khi sử dụng kết hợp các trọng số 8-bit và các activation 16-bit (hoặc ngược lại), Matrix Unit tính toán ở tốc độ bằng một nửa, và tính toán ở tốc độ bằng một phần tư khi cả hai đều là 16 bit. Nó đọc và ghi 256 giá trị trong mỗi chu kỳ xung nhịp và có thể thực hiện phép nhân ma trận hoặc tích chập. Đơn vị ma trận chứa một tile trọng số 64 KiB cộng thêm một tile để double-buffering (để che giấu 256 chu kỳ cần thiết để dịch một tile vào). Đơn vị này được thiết kế cho các ma trận dày. Hỗ trợ kiến trúc thưa bị loại bỏ vì lý do thời gian triển khai. Tính thưa sẽ được ưu tiên cao trong các thiết kế tương lai.

Các trọng số cho đơn vị ma trận được đưa qua một Weight FIFO on-chip, đọc từ một DRAM 8 GiB off-chip gọi là Weight Memory (đối với suy luận, các trọng số chỉ được đọc; 8 GiB hỗ trợ nhiều mô hình đang hoạt động đồng thời). Weight FIFO có độ sâu bốn tile. Các kết quả trung gian được lưu trong Unified Buffer on-chip 24 MiB, có thể cung cấp đầu vào cho Matrix Unit. Một bộ điều khiển DMA có thể lập trình truyền dữ liệu đến hoặc từ bộ nhớ Host CPU và Unified Buffer.

Hình 2 cho thấy sơ đồ bố trí khuôn của TPU. Unified Buffer 24 MiB chiếm gần một phần ba khuôn và Matrix Multiply Unit chiếm một phần tư, do đó datapath chiếm gần hai phần ba khuôn. Kích thước 24 MiB được chọn một phần để phù hợp với pitch của Matrix Unit trên khuôn và, do lịch trình phát triển ngắn, một phần để đơn giản hóa trình biên dịch (xem Section 7). Phần điều khiển chỉ chiếm 2%. Hình 3 cho thấy TPU trên card mạch in của nó, được cắm vào các server hiện có giống như một đĩa SATA.

Vì các lệnh được gửi qua bus PCIe tương đối chậm, các lệnh TPU tuân theo truyền thống CISC, bao gồm một trường lặp. Số chu kỳ xung nhịp trung bình trên mỗi lệnh (CPI) của các lệnh CISC này thường là 10 đến 20. Tổng cộng nó có khoảng một tá lệnh, nhưng năm lệnh sau đây là những lệnh then chốt:

1. Read_Host_Memory đọc dữ liệu từ bộ nhớ máy chủ CPU vào Unified Buffer (UB).
2. Read_Weights đọc các trọng số từ Weight Memory vào Weight FIFO làm đầu vào cho Matrix Unit.
3. MatrixMultiply/Convolve khiến Matrix Unit thực hiện phép nhân ma trận hoặc tích chập từ Unified Buffer vào các Accumulators. Một phép toán ma trận nhận đầu vào B*256 có kích thước biến thiên, nhân nó với đầu vào trọng số hằng 256x256, và tạo ra đầu ra B*256, cần B chu kỳ được đường ống hóa để hoàn thành.

4. Activate thực hiện hàm phi tuyến của nơ-ron nhân tạo, với các tùy chọn cho ReLU, Sigmoid, v.v. Các đầu vào của nó là các Accumulator, và đầu ra của nó là Unified Buffer. Nó cũng có thể thực hiện các phép pooling cần thiết cho các phép tích chập bằng cách sử dụng phần cứng chuyên dụng trên die, vì nó được kết nối với logic hàm phi tuyến.

5. Write_Host_Memory ghi dữ liệu từ Unified Buffer vào bộ nhớ host của CPU.

Các lệnh khác là đọc/ghi bộ nhớ host thay thế, thiết lập cấu hình, hai phiên bản đồng bộ hóa, ngắt host, debug-tag, nop, và halt. Lệnh CISC MatrixMultiply có 12 byte, trong đó 3 byte là địa chỉ Unified Buffer; 2 byte là địa chỉ accumulator; 4 byte là độ dài (đôi khi là 2 chiều đối với các phép tích chập); phần còn lại là opcode và cờ.

Triết lý của vi kiến trúc TPU là giữ cho đơn vị ma trận luôn bận. Nó sử dụng pipeline 4 giai đoạn cho các lệnh CISC này, trong đó mỗi lệnh thực thi trong một giai đoạn riêng biệt. Kế hoạch là che giấu việc thực thi các lệnh khác bằng cách chồng lấp việc thực thi của chúng với lệnh MatrixMultiply. Nhằm đạt được mục đích đó, lệnh Read_Weights tuân theo triết lý decoupled-access/execute [Smi82], theo đó nó có thể hoàn thành sau khi gửi địa chỉ của nó nhưng trước khi trọng số được lấy từ Weight Memory. Đơn vị ma trận sẽ bị stall nếu activation đầu vào hoặc dữ liệu trọng số chưa sẵn sàng.

Chúng tôi không có các sơ đồ chồng lấp pipeline rõ ràng, vì các lệnh CISC của chúng tôi có thể chiếm giữ một station trong hàng nghìn chu kỳ clock, không giống pipeline RISC truyền thống với một chu kỳ clock cho mỗi giai đoạn. Các trường hợp thú vị xảy ra khi các activation cho một lớp mạng phải hoàn thành trước khi các phép nhân ma trận của lớp tiếp theo có thể bắt đầu; chúng tôi thấy một “delay slot,” trong đó đơn vị ma trận chờ đồng bộ hóa tường minh trước khi đọc an toàn từ Unified Buffer.

Vì việc đọc một SRAM lớn sử dụng nhiều năng lượng hơn nhiều so với phép toán số học, đơn vị ma trận sử dụng thực thi systolic để tiết kiệm năng lượng bằng cách giảm số lần đọc và ghi của Unified Buffer [Kun80][Ram91][Ovt15b]. Nó dựa vào dữ liệu từ các hướng khác nhau đến các ô trong một mảng tại các khoảng thời gian đều đặn, nơi chúng được kết hợp. Figure 4 cho thấy dữ liệu chảy vào từ bên trái, và các trọng số được nạp từ phía trên. Một phép nhân-tích lũy 256 phần tử nhất định di chuyển qua ma trận như một mặt sóng chéo. Các trọng số được nạp trước, và có hiệu lực cùng với mặt sóng đang tiến lên song song với dữ liệu đầu tiên của một block mới. Điều khiển và dữ liệu được pipeline để tạo ra ảo giác rằng 256 đầu vào được đọc cùng lúc, và rằng chúng cập nhật tức thời một vị trí của mỗi trong 256 accumulator. Xét về tính đúng đắn, phần mềm không nhận biết bản chất systolic của đơn vị ma trận, nhưng về hiệu năng, nó quan tâm đến độ trễ của đơn vị.

Ngăn xếp phần mềm TPU phải tương thích với các ngăn xếp được phát triển cho CPU và GPU để các ứng dụng có thể được chuyển nhanh sang TPU. Phần của ứng dụng chạy trên TPU thường được viết bằng TensorFlow và được biên dịch thành một API có thể chạy trên GPU hoặc TPU [Lar16]. Giống như GPU, ngăn xếp TPU được chia thành User Space Driver và Kernel Driver. Kernel Driver nhẹ và chỉ xử lý quản lý bộ nhớ và các ngắt. Nó được thiết kế để ổn định trong dài hạn. User Space driver thay đổi thường xuyên. Nó thiết lập và điều khiển thực thi TPU, định dạng lại dữ liệu theo thứ tự TPU, dịch các lời gọi API thành các lệnh TPU, và biến chúng thành một binary ứng dụng. User Space driver biên dịch một mô hình lần đầu tiên nó được đánh giá, lưu cache ảnh chương trình và ghi ảnh trọng số vào bộ nhớ trọng số của TPU; lần đánh giá thứ hai và các lần tiếp theo chạy ở tốc độ tối đa. TPU chạy hầu hết các mô hình hoàn toàn từ đầu vào đến đầu ra, tối đa hóa tỷ lệ giữa thời gian tính toán TPU và thời gian I/O. Tính toán thường được thực hiện từng lớp một, với thực thi chồng lấp cho phép đơn vị nhân ma trận che giấu hầu hết các thao tác không nằm trên đường quan trọng.

Figure 3. Bảng mạch in TPU. Nó có thể được cắm vào khe dành cho một đĩa SATA trong một server, nhưng card này sử dụng PCIe Gen3 x16. {#jouppi-2017-tpu-fig-3 .figure tag=0182}

Figure 4. Luồng dữ liệu systolic của Đơn vị Nhân Ma trận. Phần mềm có ảo giác rằng mỗi đầu vào 256B được đọc cùng lúc, và chúng ngay lập tức cập nhật một vị trí của mỗi trong 256 RAM accumulator. {#jouppi-2017-tpu-fig-4 .figure tag=0183}

```text
Model  Die  Benchmarked Servers  Measured
mm^2  nm  MHz  TDP  Measured  TOPS/s  GB/s  On-Chip Memory  Dies  DRAM Size  TDP  Idle  Busy
Haswell E5-2699 v3  662  22  2300  145W  41W  145W  2.6  1.3  51  51 MiB  2  256 GiB  504W  159W  455W
NVIDIA K80 (2 dies/card)  561  28  560  150W  25W  98W  --  2.8  160  8 MiB  8  256 GiB (host) + 12 GiB x 8  1838W  357W  991W
TPU  NA*  28  700  75W  28W  40W  92  --  34  28 MiB  4  256 GiB (host) + 8 GiB x 4  861W  290W  384W
```

Table 2. Các server được đo chuẩn sử dụng CPU Haswell, GPU K80, và TPU. Haswell có 18 lõi, và K80 có 13 bộ xử lý SMX. Figure 10 có công suất đã đo. TPU công suất thấp cho phép mật độ cấp rack tốt hơn so với GPU công suất cao. 8 GiB DRAM trên mỗi TPU là Weight Memory. Chế độ GPU Boost không được sử dụng (Sec. 8). SECDEC và không sử dụng chế độ Boost làm giảm băng thông K80 từ 240 xuống 160. Không sử dụng chế độ Boost và hiệu năng của single die so với dual die làm giảm TOPS cực đại của K80 từ 8.7 xuống 2.8. (*Die TPU có kích thước ≤ một nửa kích thước die Haswell.) {#jouppi-2017-tpu-tab-2 .table tag=0184}
