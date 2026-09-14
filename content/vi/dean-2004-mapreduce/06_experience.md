---
paper: dean-2004-mapreduce
title: 'MapReduce: Simplified Data Processing on Large Clusters'
authors:
  - Jeffrey Dean
  - Sanjay Ghemawat
year: 2004
venue: OSDI
field: systems
section: "6"
section_title: Kinh nghiệm
tag: "0085"
kind: section
lang: vi
source: https://www.usenix.org/legacy/events/osdi04/tech/full_papers/dean/dean.pdf
pdf_sha256: 9cfef3ef1b8fe1a1b66c7221f56c2eeca0b15d6608ea68b0c85a38bfbffd8ce5
pdf_pages: 10-11
extraction: vision
extraction_model: gpt-5
content_sha256: 5f49dce76802abcd689203eb2989d52a05c0e3e563fa972b895154c284305dcc
translated_from: content/en/dean-2004-mapreduce/06_experience.md
source_content_sha256: bcdb99888edac503b375930673b2bb2cf6f4d95a9ed5da9409f472e8dbce720c
translation_model: gpt-5
translation_run: 20260914T163737Z
glossary_version: 6
glossary_terms_sha256: afc6de5d010821f75553a129f8b55d5fbabc0d9d7af198021ca9a5a496de4088
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Chúng tôi viết phiên bản đầu tiên của thư viện MapReduce vào tháng 2 năm 2003, và đã thực hiện những cải tiến đáng kể vào tháng 8 năm 2003, bao gồm tối ưu hóa tính cục bộ, cân bằng tải động cho việc thực thi tác vụ trên các máy worker, v.v. Kể từ đó, chúng tôi đã rất ngạc nhiên một cách thú vị trước phạm vi rộng lớn của các bài toán mà thư viện MapReduce có thể áp dụng. Nó đã được sử dụng trong nhiều lĩnh vực khác nhau tại Google, bao gồm:

- các bài toán học máy quy mô lớn,
- các bài toán phân cụm cho các sản phẩm Google News và Froogle,
- trích xuất dữ liệu được sử dụng để tạo các báo cáo về các truy vấn phổ biến (ví dụ: Google Zeitgeist),
- trích xuất các thuộc tính của các trang web cho các thử nghiệm và sản phẩm mới (ví dụ: trích xuất vị trí địa lý từ một kho ngữ liệu lớn gồm các trang web để phục vụ tìm kiếm theo địa phương), và
- các tính toán đồ thị quy mô lớn.

Hình 4. Các phiên bản MapReduce theo thời gian {#dean-2004-mapreduce-fig-4 .figure tag=0086}

```text
Number of jobs                                      29,423
Average job completion time                         634 secs
Machine used                                       79,186 days
Input data read                                    3,288 TB
Intermediate data produced                           758 TB
Output data written                                  193 TB
Average worker machines per job                       157
Average worker deaths per job                         1.2
Average map tasks per job                           3,351
Average reduce tasks per job                           55
Unique map implementations                            395
Unique reduce implementations                         269
Unique map/reduce combinations                        426
```

Bảng 1: Các công việc MapReduce được thực thi vào tháng 8 năm 2004 {#dean-2004-mapreduce-tab-1 .table tag=0087}

Hình 4 cho thấy sự gia tăng đáng kể theo thời gian về số lượng chương trình MapReduce riêng biệt được đưa vào hệ thống quản lý mã nguồn chính của chúng tôi, từ 0 vào đầu năm 2003 lên gần 900 phiên bản riêng biệt vào cuối tháng 9 năm 2004. MapReduce đã thành công đến vậy vì nó cho phép viết một chương trình đơn giản và thực thi chương trình đó một cách hiệu quả trên một nghìn máy trong vòng nửa giờ, qua đó rút ngắn đáng kể chu kỳ phát triển và tạo mẫu thử. Hơn nữa, nó cho phép các lập trình viên không có kinh nghiệm về hệ thống phân tán và/hoặc hệ thống song song dễ dàng khai thác lượng lớn tài nguyên.

Khi kết thúc mỗi công việc, thư viện MapReduce ghi nhật ký các thống kê về tài nguyên tính toán được công việc sử dụng. Trong Bảng 1, chúng tôi trình bày một số thống kê cho một tập con các công việc MapReduce được thực thi tại Google vào tháng 8 năm 2004.

### 6.1 Lập chỉ mục quy mô lớn {#dean-2004-mapreduce-s6-1 .section tag=0088}

Một trong những ứng dụng quan trọng nhất của MapReduce cho đến nay là viết lại hoàn toàn hệ thống lập chỉ mục trong môi trường sản xuất, hệ thống tạo ra các cấu trúc dữ liệu được sử dụng bởi dịch vụ tìm kiếm web của Google. Hệ thống lập chỉ mục nhận đầu vào là một tập lớn các tài liệu đã được hệ thống crawling của chúng tôi thu thập, được lưu trữ dưới dạng một tập các file GFS. Nội dung thô của các tài liệu này có kích thước hơn 20 terabyte dữ liệu. Quá trình lập chỉ mục chạy dưới dạng một chuỗi gồm năm đến mười thao tác MapReduce. Việc sử dụng MapReduce (thay vì các lượt xử lý phân tán ad-hoc trong phiên bản trước của hệ thống lập chỉ mục) đã mang lại một số lợi ích:

- Mã lập chỉ mục đơn giản hơn, nhỏ hơn và dễ hiểu hơn, vì mã xử lý khả năng chịu lỗi, phân phối và song song hóa được ẩn bên trong thư viện MapReduce. Ví dụ, kích thước của một giai đoạn tính toán đã giảm từ khoảng 3800 dòng mã C++ xuống khoảng 700 dòng khi được biểu diễn bằng MapReduce.
- Hiệu năng của thư viện MapReduce đủ tốt để chúng tôi có thể giữ các tính toán không liên quan về mặt khái niệm tách biệt, thay vì trộn chúng với nhau để tránh các lượt xử lý bổ sung trên dữ liệu. Điều này giúp dễ dàng thay đổi quá trình lập chỉ mục. Ví dụ, một thay đổi trước đây mất vài tháng để thực hiện trong hệ thống lập chỉ mục cũ của chúng tôi thì chỉ mất vài ngày để triển khai trong hệ thống mới.
- Quá trình lập chỉ mục đã trở nên dễ vận hành hơn nhiều, vì hầu hết các vấn đề do sự cố máy, máy chậm và các trục trặc mạng được thư viện MapReduce tự động xử lý mà không cần sự can thiệp của người vận hành. Hơn nữa, có thể dễ dàng cải thiện hiệu năng của quá trình lập chỉ mục bằng cách bổ sung các máy mới vào cụm lập chỉ mục.
