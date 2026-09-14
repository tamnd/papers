---
paper: graefe-1994-volcano
title: Volcano - An Extensible and Parallel Query Evaluation System
authors:
  - Goetz Graefe
year: 1994
venue: IEEE Transactions on Knowledge and Data Engineering
field: databases
section_title: Front Matter
tag: "0058"
kind: front
lang: vi
source: http://daslab.seas.harvard.edu/reading-group/papers/volcano.pdf
pdf_sha256: 61e9ce81f84d66797c95db711fb593adcf1dbbf95fea53eba44a9b9e2239d6ca
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 9e769a1d5489044643ca4f0b55f540df602c67eea89aa872c57579b6ebb80887
translated_from: content/en/graefe-1994-volcano/00_front.md
source_content_sha256: f3f5216d0b9ee8e1b96dbdbc385a4acb4d80a53b9dc3b71ce8d91c9a06d95e85
translation_model: gpt-5
translation_run: 20260914T163737Z
glossary_version: 6
glossary_terms_sha256: a534ae50d60bff0e03804fd3c150e37d1876484531ab87df9c72dc4d0c455eb2
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Volcano—Một Hệ thống Đánh giá Truy vấn Mở rộng và Song song

Goetz Graefe

Tóm tắt—Để nghiên cứu các tương tác giữa khả năng mở rộng và tính song song trong xử lý truy vấn cơ sở dữ liệu, chúng tôi đã phát triển một hệ thống thực thi truy vấn luồng dữ liệu mới có tên Volcano. Nỗ lực Volcano cung cấp một môi trường phong phú cho nghiên cứu và giáo dục về thiết kế hệ thống cơ sở dữ liệu, các heuristic cho tối ưu hóa truy vấn, thực thi truy vấn song song và phân bổ tài nguyên.

Volcano sử dụng một giao diện tiêu chuẩn giữa các toán tử đại số, cho phép dễ dàng bổ sung các toán tử mới và các cài đặt toán tử. Các phép toán trên từng mục riêng lẻ, ví dụ như các vị từ, được nhập vào các toán tử xử lý truy vấn bằng cách sử dụng các hàm hỗ trợ. Ngữ nghĩa của các hàm hỗ trợ không được quy định trước; bất kỳ kiểu dữ liệu nào bao gồm các đối tượng phức tạp và bất kỳ phép toán nào đều có thể được hiện thực hóa. Do đó, Volcano có khả năng mở rộng với các toán tử, thuật toán, kiểu dữ liệu và phương thức đặc thù cho kiểu mới.

Volcano bao gồm hai toán tử meta mới. Toán tử meta choose-plan hỗ trợ các kế hoạch đánh giá truy vấn động, cho phép trì hoãn các quyết định tối ưu hóa được chọn cho đến thời gian chạy, ví dụ như đối với các truy vấn nhúng có biến tự do. Toán tử meta exchange hỗ trợ tính song song nội toán tử trên các tập dữ liệu được phân vùng và cả tính song song liên toán tử theo chiều dọc và chiều ngang, chuyển đổi giữa luồng dữ liệu hướng theo nhu cầu bên trong các tiến trình và luồng dữ liệu hướng theo dữ liệu giữa các tiến trình.

Tất cả các toán tử, ngoại trừ toán tử exchange, đã được thiết kế và triển khai trong một môi trường đơn tiến trình, và được song song hóa bằng cách sử dụng toán tử exchange. Ngay cả các toán tử chưa được thiết kế cũng có thể được song song hóa bằng cách sử dụng toán tử mới này nếu chúng sử dụng và cung cấp giao diện interator. Do đó, các vấn đề về thao tác dữ liệu và tính song song đã trở nên trực giao, khiến Volcano trở thành bộ máy thực thi truy vấn đầu tiên được triển khai có khả năng kết hợp hiệu quả khả năng mở rộng và tính song song.
