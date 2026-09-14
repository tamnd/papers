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
section: "9"
section_title: Công trình liên quan
tag: "0198"
kind: section
lang: vi
source: arxiv:1704.04760
pdf_sha256: 19793e4ae1486630ac45a12facabc0e80609dd679db8ca7a3a040f8bf0d8e0be
pdf_pages: 13-15
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 3f3943f3ad3624c85775f33bd1326c7100a42d4fc3a857f265021866d0bc4d09
translated_from: content/en/jouppi-2017-tpu/09_related_work.md
source_content_sha256: 37229c17b68d414f9ad7ebf0aae63ae88c41b14fad0644fa60c7e6c610fd73ed
translation_model: gpt-5
translation_run: 20260914T201546Z
glossary_version: 6
glossary_terms_sha256: 1f83355a83baacb04f1185b8bd47b133f28d2f764f5d7ae919d5d9d0d7e083ee
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Hai bài báo khảo sát ghi nhận rằng các ASIC NN tùy chỉnh đã xuất hiện từ ít nhất 25 năm trước [Ien96][Asa02]. Ví dụ, các chip CNAPS chứa một mảng SIMD 64 phần tử gồm các bộ nhân 16-bit với 8-bit, và một số chip CNAPS có thể được kết nối với nhau bằng một bộ tuần tự [Ham90]. Hệ thống Synapse-1 dựa trên một chip nhân-tích lũy dạng tâm thu tùy chỉnh có tên MA-16, thực hiện mười sáu phép nhân 16-bit cùng một lúc [Ram91]. Hệ thống ghép nối nhiều chip MA-16 với nhau và có phần cứng tùy chỉnh để thực hiện các hàm kích hoạt.

Hai mươi lăm máy trạm SPERT-II, được tăng tốc bởi ASIC tùy chỉnh T0, đã được triển khai bắt đầu từ năm 1995 để thực hiện cả huấn luyện NN và suy luận cho nhận dạng tiếng nói [Asa98]. T0 40-Mhz đã bổ sung các lệnh vectơ vào kiến trúc tập lệnh MIPS. Đơn vị vectơ tám làn có thể tạo ra tối đa mười sáu kết quả số học 32-bit mỗi chu kỳ xung nhịp dựa trên các đầu vào 8-bit và 16-bit, khiến nó nhanh hơn 25 lần trong suy luận và nhanh hơn 20 lần trong huấn luyện so với một máy trạm SPARC-20. Họ nhận thấy rằng 16 bit không đủ cho huấn luyện, vì vậy họ sử dụng hai từ 16-bit thay thế, làm tăng gấp đôi thời gian huấn luyện. Để khắc phục nhược điểm đó, họ đưa vào các “bunches” (batches) gồm 32 đến 1000 tập dữ liệu để giảm thời gian dành cho việc cập nhật trọng số, giúp nó nhanh hơn so với huấn luyện bằng một từ nhưng không có batches.

Họ kiến trúc NN DianNao gần đây hơn giảm thiểu các truy cập bộ nhớ cả trên chip và tới DRAM bên ngoài bằng cách có hỗ trợ kiến trúc hiệu quả cho các mẫu truy cập bộ nhớ xuất hiện trong các ứng dụng NN [Keu16]

[Che16a]. Tất cả đều sử dụng các phép toán số nguyên 16-bit và tất cả các thiết kế đều đi sâu đến mức bố trí, nhưng không có chip nào được chế tạo. DianNao ban đầu sử dụng một mảng gồm 64 đơn vị nhân-tích lũy số nguyên 16-bit với 44 KB bộ nhớ trên chip và được ước tính có kích thước 3 mm² (65 nm), chạy ở 1 GHz, và tiêu thụ 0.5W [Che14a]. Phần lớn năng lượng này dành cho các truy cập DRAM tới các trọng số, vì vậy một phiên bản kế nhiệm DaDianNao ("big computer") bao gồm eDRAM để giữ 36 MiB trọng số trên chip [Che14b]. Mục tiêu là có đủ bộ nhớ trong một hệ thống nhiều chip để tránh các truy cập DRAM bên ngoài. PuDianNao kế nhiệm ("general computer") hướng tới các thuật toán học máy truyền thống hơn ngoài DNN, chẳng hạn như máy vectơ hỗ trợ [Liu15]. Một nhánh khác là ShiDianNao ("vision computer") hướng tới CNN, tránh các truy cập DRAM bằng cách kết nối bộ tăng tốc trực tiếp với cảm biến [Du15].

Convolution Engine cũng tập trung vào CNN cho xử lý ảnh [Qad13]. Thiết kế này triển khai 64 đơn vị nhân-tích lũy 10-bit và tùy chỉnh một bộ xử lý Tensilica được ước tính chạy ở 800 MHz trong 45 nm. Nó được dự đoán có hiệu quả năng lượng-diện tích cao hơn từ 8X đến 15X so với một bộ xử lý SIMD, và nằm trong khoảng từ 2X đến 3X so với phần cứng tùy chỉnh chỉ được thiết kế cho một kernel cụ thể.

Bài báo phép đo chuẩn Fathom dường như báo cáo các kết quả trái ngược với chúng tôi, với GPU thực hiện suy luận nhanh hơn nhiều so với CPU [Ado16]. Tuy nhiên, CPU và GPU của họ không thuộc lớp server, CPU chỉ có bốn lõi, các ứng dụng không sử dụng các lệnh AVX của CPU, và không có giới hạn thời gian đáp ứng (xem Table 4) [Bro16].

Catapult là ví dụ được triển khai rộng rãi nhất về việc sử dụng khả năng cấu hình lại để hỗ trợ DNN, điều mà nhiều nghiên cứu đã đề xuất [Far09][Cha10][Far11][Pee13][Cav15][Zha15]. Họ chọn FPGA thay vì GPU để giảm công suất cũng như rủi ro rằng các ứng dụng nhạy cảm với độ trễ sẽ không ánh xạ tốt lên GPU. FPGA cũng có thể được tái sử dụng, chẳng hạn như cho tìm kiếm, nén và các card giao diện mạng [Put15]. Dự án TPU thực sự bắt đầu với FPGA, nhưng chúng tôi đã từ bỏ chúng khi nhận thấy rằng các FPGA thời điểm đó không có hiệu năng cạnh tranh so với GPU thời điểm đó, và TPU có thể có công suất thấp hơn nhiều so với GPU trong khi nhanh tương đương hoặc nhanh hơn, mang lại các lợi ích đáng kể tiềm năng so với cả FPGA và GPU.

Mặc dù được công bố lần đầu vào năm 2014 [Put14], Catapult là một sản phẩm cùng thời với TPU vì nó triển khai FPGA Stratix V 28-nm vào các trung tâm dữ liệu đồng thời với TPU vào năm 2015. Catapult có xung nhịp 200 MHz, 3,926 MAC 18-bit, 5 MiB bộ nhớ trên chip, băng thông bộ nhớ 11 GB/s, và sử dụng 25 Watts. TPU có xung nhịp 700 MHz, 65,536 MAC 8-bit, 28 MiB, 34 GB/s, và thường sử dụng 40 Watts. Một phiên bản sửa đổi của Catapult sử dụng các FPGA mới hơn và được triển khai ở quy mô lớn hơn vào năm 2016 [Cau16].

Catapult V1 chạy CNN, sử dụng một bộ nhân ma trận dạng tâm thu, nhanh gấp 2.3X so với một server 2.1 GHz, 16 lõi, hai socket [Ovt15a]. Sử dụng thế hệ FPGA tiếp theo (14-nm Arria 10) của Catapult V2, hiệu năng có thể tăng lên 7X, và thậm chí có thể đạt 17X với việc floorplanning cẩn thận hơn [Ovt15b]. Mặc dù đây là so sánh giữa táo và cam, một die TPU hiện tại chạy các CNN của nó nhanh hơn từ 40X đến 70X so với một server nhanh hơn đôi chút (Tables 2 và 6). Có lẽ khác biệt lớn nhất là để đạt hiệu năng tốt nhất, người dùng phải viết các chương trình dài bằng ngôn ngữ thiết kế phần cứng cấp thấp Verilog [Met16][Put16] thay vì viết các chương trình ngắn sử dụng khung TensorFlow cấp cao. Nghĩa là, khả năng lập trình lại đến từ phần mềm cho TPU thay vì từ firmware cho FPGA.

Các nghiên cứu gần đây, xuất hiện sau khi TPU được triển khai, tăng tốc DNN bằng cách tối ưu hóa các trường hợp khi trọng số và dữ liệu rất nhỏ hoặc bằng không. Lịch trình chặt chẽ của chúng tôi đã ngăn cản các tối ưu hóa như vậy trong TPU, nhưng chúng tôi nhận thấy cùng cơ hội này trong các nghiên cứu của mình. Efficient Inference Engine dựa trên một bước đầu tiên làm giảm số lượng trọng số khoảng một hệ số 10 [Han15] như một bước riêng biệt bằng cách lọc ra các giá trị rất nhỏ, sau đó sử dụng mã hóa Huffman để thu nhỏ dữ liệu hơn nữa nhằm cải thiện hiệu năng suy luận [Han16]. Cnvlutin [Alb16] tránh các phép nhân khi đầu vào kích hoạt bằng không, điều xảy ra 44% thời gian, có lẽ một phần do hàm phi tuyến ReLU biến đổi các giá trị âm thành không, để cải thiện hiệu năng trung bình 1.4 lần.

Eyeriss là một kiến trúc luồng dữ liệu mới, công suất thấp, tận dụng các giá trị 0 bằng cách mã hóa độ dài chạy dữ liệu để giảm dấu chân bộ nhớ và tiết kiệm năng lượng bằng cách tránh các phép tính khi đầu vào là 0 [Che16a]. Sử dụng thuật ngữ Eyeriss, một lớp tích chập TPU ánh xạ C và M tới các hàng và cột của đơn vị ma trận, mất HWN chu kỳ để thực hiện một lượt quét. Với C/M cao, cần RS lượt quét để xử lý lớp; với C/M thấp, một số kỹ thuật làm giảm số lượt quét và cải thiện mức sử dụng. (Có thể tìm thêm trong các tài liệu tham khảo trực tuyến [Ros15a][Ros15b][Ros15c][Ros15f][Tho15][You15]).

Minerva là một hệ thống đồng thiết kế vượt qua các lĩnh vực thuật toán, kiến trúc và mạch để giảm công suất 8X, một phần bằng cách cắt tỉa dữ liệu kích hoạt với các giá trị nhỏ và một phần bằng cách lượng tử hóa dữ liệu [Rea16]. [Gup15] xem xét phép toán dấu phẩy cố định 16-bit cho huấn luyện thay vì cho suy luận. Các công trình khác tận dụng độ chính xác thấp hơn của các phép tính DNN bằng cách sử dụng các mạch tương tự trong quá trình tính toán để cải thiện năng lượng và hiệu năng [LiK16] [Sha16]. Bằng cách điều chỉnh một tập lệnh cho DNN, Cambricon giảm kích thước mã [Liu16]. Các công trình gần đây xem xét các kiến trúc bộ xử lý trong bộ nhớ cho NN [Chi16][Kim16].

So sánh TPU với một số kiến trúc này:
• [Che14a] DMA dữ liệu từ DRAM tới các bộ đệm đầu vào và trọng số. Chúng được đọc bởi NFU có đường ống 3 giai đoạn, thực hiện các phép nhân, phép cộng và các hàm phi tuyến; các kết quả đi tới bộ đệm đầu ra, sau đó tới DRAM. NFU không có lưu trữ và không phải là systolic.

• [Gup15] dường như truyền luồng cả hai đầu vào ma trận trong khi lưu các tổng từng phần trong mảng systolic; TPU lưu tile ma trận trọng số trong khi truyền luồng đầu vào còn lại và các tổng từng phần trước kích hoạt. TPU không hỗ trợ làm tròn ngẫu nhiên.
• [Zha15] được xây dựng từ các đơn vị tính toán tương đương với phiên bản 4x2 của đơn vị ma trận TPU. Trong một ASIC, chi phí nối dây của các crossbar kết nối bộ đệm đầu vào và đầu ra với các engine tính toán này sẽ rất đáng kể. Chúng tôi ngạc nhiên khi không thấy hỗ trợ kiến trúc cho các phép rút gọn bổ sung để kết hợp các kết quả từ các engine tính toán trong [Zha15].
Cả ba công trình [Gup15][Che14][Zha15] đều lưu các giá trị kích hoạt trong DRAM trong quá trình tính toán; Unified Buffer của TPU có kích thước đủ lớn để không xảy ra việc tràn sang DRAM hoặc nạp lại trong quá trình hoạt động bình thường.
