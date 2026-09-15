---
paper: bosshart-2014-p4
title: 'P4: Programming Protocol-Independent Packet Processors'
authors:
  - Pat Bosshart
  - Dan Daly
  - Glen Gibb
  - Martin Izzard
  - Nick McKeown
  - Jennifer Rexford
  - Cole Schlesinger
  - Dan Talayco
  - Amin Vahdat
  - George Varghese
  - David Walker
year: 2014
venue: ACM SIGCOMM Computer Communication Review
field: networks
section: "3"
section_title: MỘT NGÔN NGỮ LẬP TRÌNH
tag: "0092"
kind: section
lang: vi
source: arxiv:1312.1719
pdf_sha256: 2bb0ccb7b5410868efdecc9ef5208d235c6f3aa75dee84aa992751aed117a42f
pdf_pages: 3-4
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: b8481a38ead020ea64ecd4e4c93302134de2a5b4927017fe98c1c4792713d10c
translated_from: content/en/bosshart-2014-p4/03_a_programming_language.md
source_content_sha256: 7bf7da21ab26ca0b6c4ef7f306fd670f183052624ab69610e2dbd8cbb5944f5d
translation_model: gpt-5
translation_run: 20260914T163737Z
glossary_version: 6
glossary_terms_sha256: 3a5b9dd3cd6211761c92d70db4c4910c364b1cae9e5e732eea77349f449c860b
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Chúng tôi sử dụng mô hình chuyển tiếp trừu tượng để định nghĩa một ngôn ngữ biểu diễn cách một chuyển mạch được cấu hình và cách các gói tin được xử lý. Mục tiêu chính của bài báo này là đề xuất ngôn ngữ lập trình P4. Tuy nhiên, chúng tôi nhận thấy rằng có thể có nhiều ngôn ngữ, và chúng có khả năng sẽ chia sẻ các đặc điểm chung mà chúng tôi mô tả ở đây. Ví dụ, ngôn ngữ cần có một cách để biểu diễn cách bộ phân tích cú pháp được lập trình để bộ phân tích cú pháp biết những định dạng gói tin nào cần mong đợi; do đó một lập trình viên cần một cách để khai báo những kiểu phần đầu nào có thể tồn tại. Ví dụ, lập trình viên có thể đặc tả định dạng của phần đầu IPv4 và những phần đầu nào có thể theo sau phần đầu IP một cách hợp lệ. Điều này thúc đẩy việc định nghĩa phân tích cú pháp trong P4 bằng cách khai báo các kiểu phần đầu hợp lệ. Tương tự, lập trình viên cần biểu diễn cách các phần đầu gói tin được xử lý. Ví dụ, các trường TTL phải được giảm và kiểm tra, các phần đầu đường hầm mới có thể cần được thêm vào, và các tổng kiểm tra có thể cần được tính toán. Điều này thúc đẩy việc P4 sử dụng một chương trình luồng điều khiển mệnh lệnh để mô tả việc xử lý trường phần đầu bằng cách sử dụng các kiểu phần đầu đã khai báo và một tập hợp nguyên thủy các hành động.

Chúng tôi có thể sử dụng một ngôn ngữ như Click [10], ngôn ngữ xây dựng các chuyển mạch từ các mô-đun được tạo thành từ C++ tùy ý. Click có khả năng biểu diễn cực kỳ cao, và rất phù hợp để biểu diễn cách các gói tin được xử lý trong nhân của một CPU. Nhưng nó bị ràng buộc không đủ chặt chẽ đối với nhu cầu của chúng tôi—chúng tôi cần một ngôn ngữ phản chiếu các đường ống phân tích cú pháp-khớp-hành động trong phần cứng chuyên dụng. Ngoài ra, Click không được thiết kế cho kiến trúc bộ điều khiển-chuyển mạch và do đó không cho phép lập trình viên mô tả các bảng khớp+hành động được điền động bởi các quy tắc có kiểu rõ ràng. Cuối cùng, Click khiến việc suy luận các phụ thuộc ràng buộc thực thi song song trở nên khó khăn—như chúng tôi sẽ thảo luận sau đây.

Một ngôn ngữ xử lý gói tin phải cho phép lập trình viên biểu diễn (ngầm hoặc tường minh) bất kỳ phụ thuộc tuần tự nào giữa các trường phần đầu. Các phụ thuộc xác định những bảng nào có thể được thực thi song song. Ví dụ, thực thi tuần tự là cần thiết đối với một bảng định tuyến IP và một bảng ARP do phụ thuộc dữ liệu giữa chúng. Các phụ thuộc có thể được xác định bằng cách phân tích Đồ thị Phụ thuộc Bảng (TDG); các đồ thị này mô tả các đầu vào trường, hành động và luồng điều khiển giữa các bảng. Hình 3 cho thấy một ví dụ về đồ thị phụ thuộc bảng cho một chuyển mạch L2/L3. Các nút TDG ánh xạ trực tiếp tới các bảng khớp+hành động, và một phân tích phụ thuộc xác định vị trí mà mỗi bảng có thể nằm trong đường ống. Đáng tiếc là TDG không dễ dàng được tiếp cận đối với hầu hết lập trình viên; lập trình viên có xu hướng suy nghĩ về các thuật toán xử lý gói tin bằng cách sử dụng các cấu trúc mệnh lệnh thay vì các đồ thị.

Hình.

Hình 3: Đồ thị phụ thuộc bảng cho một chuyển mạch L2/L3. {#bosshart-2014-p4-fig-3 .figure tag=0093}

Điều này dẫn chúng tôi tới việc đề xuất một quy trình biên dịch hai bước. Ở mức cao nhất, lập trình viên biểu diễn các chương trình xử lý gói tin bằng một ngôn ngữ mệnh lệnh biểu diễn luồng điều khiển (P4); bên dưới mức này, một trình biên dịch dịch biểu diễn P4 thành các TDG để tạo thuận lợi cho phân tích phụ thuộc, sau đó ánh xạ TDG tới một mục tiêu chuyển mạch cụ thể. P4 được thiết kế để giúp việc dịch một chương trình P4 thành một TDG trở nên dễ dàng. Tóm lại, P4 có thể được xem là điểm cân bằng giữa tính tổng quát của Click (khiến việc suy luận phụ thuộc và ánh xạ tới phần cứng trở nên khó khăn) và tính không linh hoạt của OpenFlow 1.0 (khiến không thể cấu hình lại việc xử lý giao thức).
