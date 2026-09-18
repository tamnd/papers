---
paper: dewitt-1990-gamma
title: The Gamma Database Machine Project
authors:
  - David J. DeWitt
  - Shahram Ghandeharizadeh
  - Donovan A. Schneider
  - Allan Bricker
  - Hui-I Hsiao
  - Rick Rasmussen
year: 1990
venue: IEEE Transactions on Knowledge and Data Engineering
field: databases
section: "7"
section_title: Các kết luận và hướng nghiên cứu trong tương lai
tag: "0280"
kind: section
lang: vi
source: http://db.cs.berkeley.edu/cs286/papers/gamma-tkde1990.pdf
pdf_sha256: 420d33f44b8e050f33517cdff1299a58838b4ad826d80a6617200332ea02be5e
pdf_pages: 34-35
extraction: vision
extraction_model: gpt-5
content_sha256: 5e71836b255c7a51982cdb01fafcdfef99fdd6cbd5a81dc83b4f74dd5a492234
translated_from: content/en/dewitt-1990-gamma/07_conclusions_and_future_research.md
source_content_sha256: 327952d20ec4acb6459cb5b0d99b07f5c608a519ef47d4c2dbd015b706808381
translation_model: gpt-5
translation_run: 20260916T132956Z
glossary_version: 6
glossary_terms_sha256: a534ae50d60bff0e03804fd3c150e37d1876484531ab87df9c72dc4d0c455eb2
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Trong bài báo này, chúng tôi đã mô tả thiết kế và triển khai của máy cơ sở dữ liệu Gamma. Gamma sử dụng kiến trúc không chia sẻ (shared-nothing) trong đó mỗi bộ xử lý có một hoặc nhiều đĩa và các bộ xử lý chỉ có thể giao tiếp với nhau bằng cách gửi thông điệp thông qua một mạng liên kết. Trong khi phiên bản trước của phần mềm Gamma chạy trên một tập hợp các VAX 11/750 được liên kết với nhau thông qua một vòng token 80 mbit/giây, hiện tại hệ thống chạy trên một siêu khối iPSC/2 của Intel với 32 bộ xử lý và 32 ổ đĩa.

Gamma sử dụng ba ý tưởng then chốt cho phép kiến trúc được mở rộng tới hàng trăm bộ xử lý. Thứ nhất, tất cả các quan hệ được phân vùng ngang trên nhiều ổ đĩa được gắn với các bộ xử lý riêng biệt; cho phép các quan hệ được quét song song mà không cần bất kỳ phần cứng chuyên dụng nào. Ngoài ra, để cho phép thiết kế cơ sở dữ liệu được điều chỉnh theo nhu cầu của ứng dụng, ba chiến lược phân vùng thay thế được cung cấp. Đóng góp lớn thứ hai của phần mềm Gamma là việc sử dụng rộng rãi các thuật toán song song dựa trên băm để xử lý các toán tử quan hệ phức tạp như các phép nối và các hàm tổng hợp. Cuối cùng, hệ thống sử dụng các kỹ thuật lập lịch luồng dữ liệu độc đáo để phối hợp việc thực thi các truy vấn đa toán tử. Các kỹ thuật này giúp có thể kiểm soát việc thực thi các truy vấn rất phức tạp với sự phối hợp tối thiểu - một yêu cầu cần thiết đối với các cấu hình liên quan đến số lượng lớn bộ xử lý

Ngoài việc mô tả thiết kế của phần mềm Gamma, chúng tôi cũng đã trình bày một đánh giá hiệu năng toàn diện của phiên bản Gamma trên siêu khối iPSC/2. Ba nhóm thí nghiệm đã được thực hiện. Thứ nhất, với một cấu hình máy cố định gồm 30 bộ xử lý, thời gian đáp ứng cho tập truy vấn chuẩn của phép đo chuẩn Wisconsin được đo với 3 kích thước khác nhau của các quan hệ. Đối với một tập con các truy vấn này, chúng tôi cũng đo hiệu năng của hệ thống tương ứng với số lượng bộ xử lý được sử dụng khi kích thước của các quan hệ đầu vào được giữ cố định (tăng tốc) và khi kích thước của các quan hệ đầu vào được tăng tỷ lệ thuận với số lượng bộ xử lý (mở rộng quy mô). Các kết quả tăng tốc thu được cho cả truy vấn chọn và truy vấn nối gần như tuyến tính hoàn hảo; do đó tăng gấp đôi số lượng bộ xử lý sẽ giảm một nửa thời gian đáp ứng cho một truy vấn. Các kết quả mở rộng quy mô thu được cũng rất đáng khích lệ. Chúng cho thấy thời gian đáp ứng không đổi có thể được duy trì cho cả các truy vấn chọn và truy vấn nối khi tải công việc được tăng lên bằng cách thêm số lượng bộ xử lý và đĩa tỷ lệ thuận.

Hiện tại chúng tôi đang tiến hành một số dự án mới. Thứ nhất, chúng tôi dự định triển khai cơ chế phân cụm liên kết và đánh giá tính hiệu quả của nó. Liên quan đến việc xử lý truy vấn, chúng tôi đã thiết kế [SCHN89b] và hiện đang đánh giá các chiến lược thay thế để xử lý các truy vấn liên quan đến nhiều phép nối. Ví dụ, xét một truy vấn liên quan đến 10 phép nối trên một máy có 100 bộ xử lý. Liệu tốt hơn là sử dụng tất cả 100 bộ xử lý cho mỗi phép nối (phân bổ 1/10 bộ nhớ trên mỗi bộ xử lý cho mỗi phép nối), hay sử dụng 10 bộ xử lý cho mỗi phép nối (trong trường hợp này mỗi toán tử nối sẽ được sử dụng toàn bộ bộ nhớ tại mỗi bộ xử lý)? Cuối cùng, chúng tôi đang nghiên cứu một số cơ chế phân vùng mới kết hợp các đặc điểm tốt nhất của các chiến lược phân vùng băm và phân vùng theo khoảng.
