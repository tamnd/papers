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
section: "3"
section_title: Nền tảng CPU, GPU và TPU
tag: "0185"
kind: section
lang: vi
source: arxiv:1704.04760
pdf_sha256: 19793e4ae1486630ac45a12facabc0e80609dd679db8ca7a3a040f8bf0d8e0be
pdf_pages: "5"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: d5730f57f8e52b2fa8125eb7a0825fd2644d925845493d976e6c7c7ef82a3317
translated_from: content/en/jouppi-2017-tpu/03_cpu_gpu_and_tpu_platforms.md
source_content_sha256: 365bb90900e96ac87825735a028e240acc6543e598af4456151dd8dbc669b6cd
translation_model: gpt-5
translation_run: 20260914T201546Z
glossary_version: 6
glossary_terms_sha256: 1f83355a83baacb04f1185b8bd47b133f28d2f764f5d7ae919d5d9d0d7e083ee
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Sáu ứng dụng sản xuất trong Bảng 1 là tải công việc của chúng tôi cho bài báo này. Như đã đề cập ở trên, sáu ứng dụng này đại diện cho 95% việc sử dụng TPU trong các datacenter của chúng tôi. Trớ trêu thay, việc triển khai và đo lường các DNN nhỏ phổ biến như AlexNet hoặc VGG lại khó khăn trên các máy sản xuất. Tuy nhiên, một trong các CNN của chúng tôi bắt nguồn từ Inception V2, vốn được sử dụng rộng rãi.

Các nền tảng benchmark là những máy tính cấp server có sẵn vào năm 2015 khi các TPU được triển khai. Hạn chế này có nghĩa là chúng phải bao gồm ít nhất bảo vệ SECDED của SRAM nội bộ cũng như bộ nhớ DRAM bên ngoài giống như TPU, điều này loại trừ một số lựa chọn như GPU Nvidia Maxwell. Để công ty chúng tôi mua và triển khai chúng, chúng cũng phải là các máy có cấu hình hợp lý, chứ không phải các sản phẩm vụng về được lắp ráp chỉ để giành chiến thắng trong các benchmark.

Bảng 2 liệt kê các lựa chọn của chúng tôi. Server CPU truyền thống được đại diện bởi một bộ xử lý Haswell 18 lõi, hai socket từ Intel. Nền tảng này cũng là server máy chủ cho GPU hoặc TPU. Haswell được chế tạo bằng quy trình Intel 22nm. Cả CPU và GPU đều là các die rất lớn: khoảng 600 mm²!

Tốc độ xung nhịp CPU 2.3 GHz không bao gồm chế độ Turbo vì nó hiếm khi xảy ra trong các datacenter của chúng tôi đối với các ứng dụng NN. Haswell có các tốc độ xung nhịp khác nhau tùy thuộc vào việc các chương trình có sử dụng các lệnh AVX hay không, mà các ứng dụng NN của chúng tôi thường sử dụng. Tốc độ xung nhịp cao hơn của chế độ Turbo (đối với các chương trình tránh AVX) xảy ra khi chúng không sử dụng tất cả các lõi. Do đó, một lý do khác khiến chế độ Turbo hiếm khi xuất hiện trong các datacenter của chúng tôi là các ứng dụng của chúng tôi thường sử dụng tất cả các lõi, ngoài ra chúng có thể chạy các công việc datacenter khác để lấp đầy bất kỳ lõi nào đang rảnh.

Bộ tăng tốc GPU là Nvidia K80. Mỗi card K80 chứa hai die và cung cấp SECDED trên bộ nhớ nội bộ và DRAM. Nvidia tuyên bố rằng “K80 Accelerator dramatically lowers datacenter cost by delivering application performance with fewer, more powerful servers”[Nvi16]. Các nhà nghiên cứu NN thường xuyên sử dụng K80 vào năm 2015, và chúng được chọn cho các sản phẩm GPU dựa trên cloud mới gần đây nhất vào tháng 9 năm 2016 [Bar16].

Có thể cài đặt tối đa tám die K80 trong bốn card trên server này, đây là cấu hình mà chúng tôi benchmark. Nó cung cấp chế độ Boost để tăng tốc độ xung nhịp lên tới 875 MHz. Chế độ Turbo trong Haswell được điều khiển bởi phần cứng và do đó có thể hoạt động trong các đợt ngắn trước khi nhiệt độ chip tăng đáng kể. Tuy nhiên, chế độ Boost nằm dưới sự điều khiển của một driver phần mềm [Nvi15], và do đó kéo dài ít nhất hàng trăm mili giây. Vì vậy, công suất và khả năng làm mát sẽ phải được cung cấp cho K80 như thể nó về cơ bản luôn chạy ở chế độ Boost, nếu không các chip có thể trở nên quá nóng. Đối với nền tảng này, việc bật chế độ Boost sẽ buộc chúng tôi giảm số lượng card K80, điều này sẽ làm tổn hại đến tổng chi phí sở hữu. Vì vậy, chế độ Boost bị vô hiệu hóa. Hạn chế này làm giảm băng thông cực đại và TOPS (xem chú thích Bảng 2); Mục 8 xem xét trường hợp nó được bật.

Do số lượng die trên mỗi server được benchmark thay đổi từ 2 đến 8, chúng tôi thường hiển thị các kết quả dưới đây được chuẩn hóa theo mỗi die (Hình 5-8, Hình 10-11, và Bảng 3, 4, và 6), nhưng đôi khi chúng tôi hiển thị toàn bộ hệ thống (Hình 9). Chúng tôi hy vọng sự phân biệt này là rõ ràng.
