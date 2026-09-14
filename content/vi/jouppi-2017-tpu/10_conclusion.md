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
section: "10"
section_title: Kết luận
tag: "0199"
kind: section
lang: vi
source: arxiv:1704.04760
pdf_sha256: 19793e4ae1486630ac45a12facabc0e80609dd679db8ca7a3a040f8bf0d8e0be
pdf_pages: "15"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 8500120e4809dfb289e2fea99e0abaa6dad1d3d17ce06c5a0dea6df282a421e6
translated_from: content/en/jouppi-2017-tpu/10_conclusion.md
source_content_sha256: ebf239fda26a84d818a849046c51ff1aab8d067276b19e93d22b51e2a5e2934a
translation_model: gpt-5
translation_run: 20260914T201546Z
glossary_version: 6
glossary_terms_sha256: 1f83355a83baacb04f1185b8bd47b133f28d2f764f5d7ae919d5d9d0d7e083ee
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Mặc dù sống trên một bus I/O và có băng thông bộ nhớ tương đối nhỏ làm hạn chế việc sử dụng TPU—bốn trong sáu ứng dụng NN bị giới hạn bởi bộ nhớ—một phần nhỏ của một con số lớn vẫn có thể tương đối lớn, như mô hình hiệu năng Roofline chứng minh. Kết quả này gợi ý một “Hệ quả Cornucopia” đối với Định luật Amdahl: *mức sử dụng thấp của một tài nguyên khổng lồ, giá rẻ vẫn có thể mang lại hiệu năng cao, hiệu quả về chi phí.*

TPU tận dụng sự giảm bậc độ lớn về năng lượng và diện tích của các bộ nhân ma trận dạng tâm thu số nguyên 8-bit so với các đường dẫn dữ liệu dấu phẩy động 32-bit của GPU K80 để tích hợp số lượng MAC gấp 25 lần (65,536 8-bit so với 2,496 32-bit) và bộ nhớ trên chip lớn gấp 3.5 lần (28 MiB so với 8 MiB) trong khi sử dụng ít hơn một nửa công suất của K80 trong một die tương đối nhỏ. Bộ nhớ lớn hơn này giúp tăng cường độ hoạt động của các ứng dụng để cho phép chúng tận dụng các MAC dồi dào một cách đầy đủ hơn nữa.

Chúng tôi nhận thấy rằng mặc dù gần đây cộng đồng kiến trúc nhấn mạnh vào CNN, chúng chỉ chiếm khoảng 5% tải công việc NN đại diện cho các datacenter của chúng tôi, điều này cho thấy cần chú ý nhiều hơn đến MLP và LSTM. Lặp lại lịch sử, điều này tương tự như khi nhiều kiến trúc sư tập trung vào hiệu năng dấu phẩy động trong khi phần lớn tải công việc chính thống hóa ra lại bị chi phối bởi các phép toán số nguyên.

Chúng tôi quan sát thấy rằng số lượng suy luận mỗi giây (IPS) phụ thuộc nhiều hơn vào NN chứ không phải phần cứng bên dưới, và do đó IPS là một chỉ số hiệu năng đơn lẻ còn tệ hơn đối với các bộ xử lý NN so với MIPS và MFLOPS đối với CPU và GPU.

Chúng tôi cũng nhận thấy rằng các ứng dụng suy luận có các cận thời gian đáp ứng nghiêm ngặt vì chúng thường là một phần của các ứng dụng hướng tới người dùng, do đó kiến trúc NN cần hoạt động tốt khi xử lý các thời hạn độ trễ ở phân vị thứ 99. Mặc dù K80 có thể vượt trội trong huấn luyện, trung bình nó chỉ nhanh hơn Haswell một chút trong suy luận đối với tải công việc của chúng tôi, có lẽ vì nó nhấn mạnh vào thông lượng thay vì độ trễ; điều đó xung đột với các thời hạn đáp ứng nghiêm ngặt của các ứng dụng suy luận của chúng tôi.

Die TPU tận dụng lợi thế về MAC và bộ nhớ trên chip để chạy các chương trình ngắn được viết bằng khung TensorFlow chuyên biệt theo miền nhanh gấp 15 lần die GPU K80, dẫn đến lợi thế hiệu năng/Watt là 29 lần, tương quan với hiệu năng/tổng chi phí sở hữu. So với die CPU Haswell, các tỷ lệ tương ứng là 29 và 83. Mặc dù các CPU và GPU tương lai chắc chắn sẽ chạy suy luận nhanh hơn, một TPU được thiết kế lại sử dụng bộ nhớ GPU vào khoảng năm 2015 sẽ nhanh hơn từ hai đến ba lần và nâng lợi thế hiệu năng/Watt lên gần 70 lần so với K80 và 200 lần so với Haswell.

Tóm lại, TPU thành công nhờ đơn vị nhân ma trận lớn—nhưng không quá lớn; bộ nhớ trên chip đáng kể được điều khiển bằng phần mềm; khả năng chạy toàn bộ mô hình suy luận để giảm sự phụ thuộc vào CPU máy chủ; mô hình thực thi đơn luồng, xác định đã chứng minh là phù hợp với các giới hạn thời gian đáp ứng ở phân vị thứ 99; đủ tính linh hoạt để phù hợp với các NN của năm 2017 cũng như năm 2013; việc loại bỏ các tính năng đa dụng giúp tạo ra một die nhỏ và công suất thấp mặc dù có đường dẫn dữ liệu và bộ nhớ lớn hơn; việc sử dụng số nguyên 8-bit bởi các ứng dụng lượng tử hóa; và việc các ứng dụng được viết bằng TensorFlow, giúp dễ dàng chuyển chúng sang TPU với hiệu năng cao thay vì phải viết lại để chạy tốt trên phần cứng TPU rất khác biệt.

Sự khác biệt bậc độ lớn giữa các sản phẩm thương mại là hiếm trong kiến trúc máy tính, điều này có thể khiến TPU trở thành một nguyên mẫu cho các kiến trúc chuyên biệt theo miền. Chúng tôi kỳ vọng rằng nhiều người sẽ xây dựng các thế hệ kế nhiệm, nâng cao tiêu chuẩn hơn nữa.
