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
content_sha256: 797c9c38501ff5ccc347c202b4fb5a2108ea5b29e2f0e3ab0d10b86cfe143921
translated_from: content/en/dean-2004-mapreduce/06_experience.md
source_content_sha256: bcdb99888edac503b375930673b2bb2cf6f4d95a9ed5da9409f472e8dbce720c
translation_model: gpt-5
translation_run: 20260918T153717Z
glossary_version: 7
glossary_terms_sha256: f834761938c11bca59f7cb79948997ed0706af48cd70392678452699c034a7ad
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Chúng tôi đã viết phiên bản đầu tiên của thư viện MapReduce vào tháng 2 năm 2003, và thực hiện những cải tiến đáng kể đối với nó vào tháng 8 năm 2003, bao gồm tối ưu hóa tính cục bộ, cân bằng tải động của việc thực thi tác vụ trên các máy worker, v.v. Kể từ thời điểm đó, chúng tôi đã rất ngạc nhiên một cách tích cực về mức độ áp dụng rộng rãi của thư viện MapReduce đối với các loại bài toán mà chúng tôi xử lý. Nó đã được sử dụng trong nhiều lĩnh vực khác nhau bên trong Google, bao gồm:

- các bài toán học máy quy mô lớn,
- các bài toán phân cụm cho các sản phẩm Google News và Froogle,
- trích xuất dữ liệu được sử dụng để tạo báo cáo về các truy vấn phổ biến (ví dụ: Google Zeitgeist),
- trích xuất các thuộc tính của các trang web cho các thử nghiệm và sản phẩm mới (ví dụ: trích xuất vị trí địa lý từ một tập dữ liệu lớn các trang web cho tìm kiếm cục bộ), và
- các phép tính trên đồ thị quy mô lớn.

Hình 4. Các thể hiện MapReduce theo thời gian {#dean-2004-mapreduce-fig-4 .figure tag=0086}

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

Bảng 1: Các công việc MapReduce được chạy vào tháng 8 năm 2004 {#dean-2004-mapreduce-tab-1 .table tag=0087}

Hình 4 cho thấy sự tăng trưởng đáng kể về số lượng các chương trình MapReduce riêng biệt được đưa vào hệ thống quản lý mã nguồn chính của chúng tôi theo thời gian, từ 0 vào đầu năm 2003 đến gần 900 thể hiện riêng biệt vào cuối tháng 9 năm 2004. MapReduce đã thành công đến vậy vì nó cho phép viết một chương trình đơn giản và chạy nó một cách hiệu quả trên một nghìn máy trong khoảng thời gian nửa giờ, giúp tăng tốc đáng kể chu kỳ phát triển và tạo mẫu. Hơn nữa, nó cho phép các lập trình viên không có kinh nghiệm với các hệ thống phân tán và/hoặc song song dễ dàng khai thác lượng lớn tài nguyên.

Vào cuối mỗi công việc, thư viện MapReduce ghi nhật ký các thống kê về các tài nguyên tính toán được công việc sử dụng. Trong Bảng 1, chúng tôi trình bày một số thống kê cho một tập con các công việc MapReduce được chạy tại Google vào tháng 8 năm 2004.

### 6.1 Lập chỉ mục quy mô lớn {#dean-2004-mapreduce-s6-1 .section tag=0088}

Một trong những cách sử dụng MapReduce quan trọng nhất của chúng tôi cho đến nay là viết lại hoàn toàn hệ thống lập chỉ mục sản xuất tạo ra các cấu trúc dữ liệu được sử dụng cho dịch vụ tìm kiếm web của Google. Hệ thống lập chỉ mục nhận đầu vào là một tập lớn các tài liệu đã được hệ thống thu thập dữ liệu của chúng tôi lấy về, được lưu trữ dưới dạng một tập các file GFS. Nội dung thô của các tài liệu này có kích thước hơn 20 terabyte dữ liệu. Quá trình lập chỉ mục chạy dưới dạng một chuỗi từ năm đến mười phép toán MapReduce. Việc sử dụng MapReduce (thay vì các lượt truyền phân tán đặc biệt trong phiên bản trước của hệ thống lập chỉ mục) đã mang lại một số lợi ích:

- Mã lập chỉ mục đơn giản hơn, nhỏ hơn và dễ hiểu hơn, bởi vì mã xử lý khả năng chịu lỗi, phân phối và song song hóa được ẩn bên trong thư viện MapReduce. Ví dụ, kích thước của một giai đoạn của phép tính đã giảm từ khoảng 3800 dòng mã C++ xuống còn khoảng 700 dòng khi được biểu diễn bằng MapReduce.
- Hiệu năng của thư viện MapReduce đủ tốt để chúng tôi có thể giữ các phép tính không liên quan về mặt khái niệm tách biệt, thay vì trộn chúng với nhau để tránh các lượt truyền bổ sung qua dữ liệu. Điều này giúp dễ dàng thay đổi quá trình lập chỉ mục. Ví dụ, một thay đổi mất vài tháng để thực hiện trong hệ thống lập chỉ mục cũ của chúng tôi chỉ mất vài ngày để triển khai trong hệ thống mới.
- Quá trình lập chỉ mục trở nên dễ vận hành hơn nhiều, bởi vì phần lớn các vấn đề do sự cố máy, máy chậm và các trục trặc mạng gây ra được thư viện MapReduce tự động xử lý mà không cần sự can thiệp của toán tử. Hơn nữa, có thể dễ dàng cải thiện hiệu năng của quá trình lập chỉ mục bằng cách thêm các máy mới vào cụm lập chỉ mục.
