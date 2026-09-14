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
section_title: Các nền tảng CPU, GPU và TPU
tag: "0185"
kind: section
lang: vi
source: arxiv:1704.04760
pdf_sha256: 19793e4ae1486630ac45a12facabc0e80609dd679db8ca7a3a040f8bf0d8e0be
pdf_pages: "5"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 0f59f7a4dc305e2ca19aef7331104483235aea6f64f0fcb959cdf35af57220c8
translated_from: content/en/jouppi-2017-tpu/03_cpu_gpu_and_tpu_platforms.md
source_content_sha256: 365bb90900e96ac87825735a028e240acc6543e598af4456151dd8dbc669b6cd
translation_model: gpt-6-astra
translation_run: 20260914T212037Z
glossary_version: 6
glossary_terms_sha256: 1f83355a83baacb04f1185b8bd47b133f28d2f764f5d7ae919d5d9d0d7e083ee
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Sáu ứng dụng đang vận hành thực tế trong Bảng 1 là tải công việc của chúng tôi trong bài báo này. Như đã đề cập ở trên, sáu ứng dụng này đại diện cho 95% mức sử dụng TPU trong các trung tâm dữ liệu của chúng tôi. Trớ trêu thay, việc triển khai và đo lường các mạng nơ-ron sâu (DNN) nhỏ phổ biến như AlexNet hoặc VGG trên các máy đang vận hành thực tế lại khó khăn. Tuy nhiên, một trong các mạng nơ-ron tích chập (CNN) của chúng tôi bắt nguồn từ Inception V2, vốn được sử dụng rộng rãi.

Các nền tảng đo chuẩn là những máy tính cấp server có sẵn vào năm 2015, khi TPU được triển khai. Ràng buộc này có nghĩa là chúng phải có ít nhất cơ chế bảo vệ sửa lỗi một bit và phát hiện lỗi hai bit (SECDED) cho SRAM bên trong cũng như bộ nhớ DRAM bên ngoài giống như TPU, qua đó loại trừ một số lựa chọn như GPU Nvidia Maxwell. Để công ty chúng tôi mua và triển khai, chúng cũng phải là những máy có cấu hình hợp lý, chứ không phải những hệ thống chắp vá được lắp ráp chỉ để thắng các phép đo chuẩn.

Bảng 2 liệt kê các lựa chọn của chúng tôi. Đại diện cho server CPU truyền thống là bộ xử lý Haswell 18 lõi của Intel trong hệ thống hai socket. Nền tảng này cũng là server chủ cho GPU hoặc TPU. Haswell được chế tạo bằng quy trình 22nm của Intel. Cả CPU lẫn GPU đều có đế bán dẫn rất lớn: khoảng 600 mm²!

Tần số xung nhịp CPU 2.3 GHz không bao gồm chế độ Turbo vì chế độ này hiếm khi hoạt động với các ứng dụng mạng nơ-ron trong các trung tâm dữ liệu của chúng tôi. Haswell có các tần số xung nhịp khác nhau tùy thuộc vào việc chương trình có sử dụng các lệnh AVX hay không; các ứng dụng mạng nơ-ron của chúng tôi thường sử dụng những lệnh này. Tần số xung nhịp cao hơn của chế độ Turbo (dành cho các chương trình không dùng AVX) xuất hiện khi chúng không sử dụng hết các lõi. Do đó, một lý do khác khiến chế độ Turbo hiếm khi hoạt động trong các trung tâm dữ liệu của chúng tôi là các ứng dụng thường sử dụng hết các lõi; hơn nữa, các máy có thể chạy những công việc khác của trung tâm dữ liệu để tận dụng mọi lõi đang nhàn rỗi.

Bộ tăng tốc GPU là Nvidia K80. Mỗi card K80 chứa hai đế bán dẫn và cung cấp SECDED cho bộ nhớ bên trong và DRAM. Nvidia tuyên bố rằng “Bộ tăng tốc K80 giảm mạnh chi phí trung tâm dữ liệu bằng cách cung cấp hiệu năng ứng dụng với ít server hơn nhưng mạnh hơn”[Nvi16]. Các nhà nghiên cứu mạng nơ-ron thường xuyên sử dụng K80 vào năm 2015, và đến tận tháng 9 năm 2016, K80 vẫn được chọn cho các dịch vụ GPU mới trên nền tảng đám mây [Bar16].

Có thể lắp tối đa tám đế bán dẫn K80 trên bốn card vào server này, và đây là cấu hình chúng tôi dùng để đo chuẩn. K80 cung cấp chế độ Boost để tăng tần số xung nhịp lên tới 875 MHz. Chế độ Turbo trong Haswell được phần cứng điều khiển nên có thể hoạt động trong những đợt ngắn trước khi nhiệt độ chip tăng đáng kể. Tuy nhiên, chế độ Boost do trình điều khiển phần mềm kiểm soát [Nvi15], nên kéo dài ít nhất hàng trăm mili giây. Vì vậy, hệ thống cấp điện và làm mát phải được trang bị cho K80 như thể nó gần như luôn chạy ở chế độ Boost; nếu không, các chip có thể quá nóng. Với nền tảng này, bật chế độ Boost sẽ buộc chúng tôi phải giảm số lượng card K80, gây bất lợi về tổng chi phí sở hữu. Do đó, chế độ Boost bị tắt. Ràng buộc này làm giảm băng thông đỉnh và TOPS (xem chú thích Bảng 2); Mục 8 xem xét trường hợp chế độ này được bật.

Vì số đế bán dẫn trên mỗi server được đo chuẩn dao động từ 2 đến 8, các kết quả dưới đây thường được chúng tôi chuẩn hóa theo từng đế bán dẫn (các Hình 5-8, các Hình 10-11 và các Bảng 3, 4 và 6), nhưng đôi khi chúng tôi trình bày kết quả cho toàn bộ hệ thống (Hình 9). Chúng tôi hy vọng sự phân biệt này là rõ ràng.
