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
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 0aed043788f60bba07f77479171b5e609a24906fde98280b3fd3587077adf00b
translated_from: content/en/dewitt-1990-gamma/00_front.md
source_content_sha256: 171b394de555d93b1788732ba2c80f47e859466cdab680118e2684efeb7504f9
translation_model: gpt-5
translation_run: 20260914T163737Z
glossary_version: 6
glossary_terms_sha256: a534ae50d60bff0e03804fd3c150e37d1876484531ab87df9c72dc4d0c455eb2
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Dự án Máy Cơ sở Dữ liệu Gamma

David J. DeWitt

Shahram Ghandeharizadeh

Donovan Schneider

Allan Bricker

Hui-I Hsiao

Rick Rasmussen

Khoa Khoa học Máy tính

Đại học Wisconsin

Nghiên cứu này được hỗ trợ một phần bởi Cơ quan Dự án Nghiên cứu Tiên tiến Quốc phòng theo hợp đồng N00039-86-C-0578, bởi Quỹ Khoa học Quốc gia theo khoản tài trợ DCR-8512862, bởi Học bổng Trợ lý Nghiên cứu Sau đại học trong Xử lý Song song do DARPA/NASA tài trợ, và bởi các khoản tài trợ nghiên cứu từ Intel Scientific Computers, Tandem Computers và Digital Equipment Corporation.

TÓM TẮT

Bài báo này mô tả thiết kế của máy cơ sở dữ liệu Gamma và các kỹ thuật được sử dụng trong quá trình triển khai nó. Gamma là một máy cơ sở dữ liệu quan hệ hiện đang hoạt động trên siêu khối iPSC/2 của Intel với 32 bộ xử lý và 32 ổ đĩa. Gamma sử dụng ba ý tưởng kỹ thuật then chốt cho phép mở rộng kiến trúc đến hàng trăm bộ xử lý. Thứ nhất, tất cả các quan hệ được phân vùng theo chiều ngang trên nhiều ổ đĩa, cho phép quét các quan hệ song song. Thứ hai, các thuật toán song song mới dựa trên băm được sử dụng để triển khai các toán tử quan hệ phức tạp như join và các hàm aggregate. Thứ ba, các kỹ thuật lập lịch luồng dữ liệu được sử dụng để điều phối các truy vấn đa toán tử. Bằng cách sử dụng các kỹ thuật này, có thể kiểm soát việc thực thi các truy vấn rất phức tạp với sự điều phối tối thiểu, một yêu cầu cần thiết đối với các cấu hình liên quan đến một số lượng rất lớn bộ xử lý.

Ngoài việc mô tả thiết kế của phần mềm Gamma, bài báo cũng trình bày một đánh giá hiệu năng toàn diện của phiên bản Gamma chạy trên siêu khối iPSC/2.
