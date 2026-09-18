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
section_title: Front Matter
tag: "0177"
kind: front
lang: vi
source: http://db.cs.berkeley.edu/cs286/papers/gamma-tkde1990.pdf
pdf_sha256: 420d33f44b8e050f33517cdff1299a58838b4ad826d80a6617200332ea02be5e
pdf_pages: 1-2
extraction: vision
extraction_model: gpt-5
content_sha256: ab1d9b0c3b958514e08b104503afe9851be253c3a947105cd99c50d92be8a9ca
translated_from: content/en/dewitt-1990-gamma/00_front.md
source_content_sha256: 64bdcf07b7a3c62861e451e668dcf626b539ea8cca55a9db6022c680103aa88b
translation_model: gpt-5
translation_run: 20260916T132956Z
glossary_version: 6
glossary_terms_sha256: a534ae50d60bff0e03804fd3c150e37d1876484531ab87df9c72dc4d0c455eb2
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Dự án Máy Cơ sở dữ liệu Gamma

David J. DeWitt  
Shahram Ghandeharizadeh  
Donovan Schneider  
Allan Bricker  
Hui-I Hsiao  
Rick Rasmussen

Khoa Khoa học Máy tính  
Đại học Wisconsin

Nghiên cứu này được hỗ trợ một phần bởi Cơ quan Dự án Nghiên cứu Tiên tiến Quốc phòng theo hợp đồng N00039-86-C-0578, bởi Quỹ Khoa học Quốc gia theo tài trợ DCR-8512862, bởi một chương trình Trợ lý Nghiên cứu Sau đại học do DARPA/NASA tài trợ trong lĩnh vực Xử lý Song song, và bởi các khoản tài trợ nghiên cứu từ Intel Scientific Computers, Tandem Computers, và Digital Equipment Corporation.

TÓM TẮT

Bài báo này mô tả thiết kế của máy cơ sở dữ liệu Gamma và các kỹ thuật được sử dụng trong quá trình triển khai nó. Gamma là một máy cơ sở dữ liệu quan hệ hiện đang hoạt động trên một siêu khối Intel iPSC/2 với 32 bộ xử lý và 32 ổ đĩa. Gamma sử dụng ba ý tưởng kỹ thuật then chốt cho phép kiến trúc có thể mở rộng đến hàng trăm bộ xử lý. Thứ nhất, tất cả các quan hệ được phân vùng theo chiều ngang trên nhiều ổ đĩa, cho phép quét các quan hệ song song. Thứ hai, các thuật toán song song mới dựa trên băm được sử dụng để triển khai các toán tử quan hệ phức tạp như phép nối và các hàm tổng hợp. Thứ ba, các kỹ thuật lập lịch luồng dữ liệu được sử dụng để phối hợp các truy vấn đa toán tử. Bằng cách sử dụng các kỹ thuật này, có thể kiểm soát việc thực thi các truy vấn rất phức tạp với sự phối hợp tối thiểu - một yêu cầu cần thiết đối với các cấu hình liên quan đến một số lượng rất lớn bộ xử lý.

Ngoài việc mô tả thiết kế của phần mềm Gamma, bài báo cũng trình bày một đánh giá hiệu năng toàn diện của phiên bản Gamma trên siêu khối iPSC/2. Ngoài việc đo lường ảnh hưởng của kích thước quan hệ và các chỉ mục đến thời gian đáp ứng đối với các truy vấn chọn lọc, nối, tổng hợp và cập nhật, chúng tôi cũng phân tích hiệu năng của Gamma so với số lượng bộ xử lý được sử dụng khi kích thước của các quan hệ đầu vào được giữ không đổi (tăng tốc) và khi kích thước của các quan hệ đầu vào được tăng tỷ lệ thuận với số lượng bộ xử lý (mở rộng quy mô). Các kết quả tăng tốc thu được cho cả truy vấn chọn lọc và truy vấn nối là tuyến tính; do đó, việc tăng gấp đôi số lượng bộ xử lý sẽ giảm một nửa thời gian đáp ứng cho một truy vấn. Các kết quả mở rộng quy mô thu được cũng rất đáng khích lệ. Chúng cho thấy rằng có thể duy trì thời gian đáp ứng gần như không đổi đối với cả truy vấn chọn lọc và truy vấn nối khi tải công việc được tăng lên bằng cách bổ sung một số lượng bộ xử lý và đĩa tỷ lệ thuận.
