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
section: "1"
section_title: Giới thiệu
tag: 025B
kind: section
lang: vi
source: http://db.cs.berkeley.edu/cs286/papers/gamma-tkde1990.pdf
pdf_sha256: 420d33f44b8e050f33517cdff1299a58838b4ad826d80a6617200332ea02be5e
pdf_pages: 3-4
extraction: vision
extraction_model: gpt-5
content_sha256: 82b4d561bccc22bcaa4562035907c534f0131043569ffbc4dcdc4e38ff3b249c
translated_from: content/en/dewitt-1990-gamma/01_introduction.md
source_content_sha256: 0acd26d44d8ea65b1bb23bce00e963e70a3dd66529d773890726c715981e9d68
translation_model: gpt-5
translation_run: 20260916T132956Z
glossary_version: 6
glossary_terms_sha256: a534ae50d60bff0e03804fd3c150e37d1876484531ab87df9c72dc4d0c455eb2
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Trong 5 năm qua, dự án máy cơ sở dữ liệu Gamma đã tập trung vào các vấn đề liên quan đến thiết kế và triển khai các máy cơ sở dữ liệu song song cao. Theo nhiều cách, thiết kế của Gamma dựa trên những điều chúng tôi đã học được từ máy cơ sở dữ liệu trước đây của mình, DIRECT [DEWI79]. Mặc dù DIRECT đã chứng minh rằng tính song song có thể được áp dụng thành công vào việc xử lý các thao tác cơ sở dữ liệu, nó có một số thiếu sót nghiêm trọng trong thiết kế khiến việc mở rộng kiến trúc lên hàng trăm bộ xử lý là không thể; chủ yếu là do việc sử dụng bộ nhớ chia sẻ và điều khiển tập trung cho việc thực thi các thuật toán song song của nó [BITT83].

Như một giải pháp cho các vấn đề gặp phải với DIRECT, Gamma sử dụng những giải pháp ngày nay có vẻ tương đối đơn giản. Về mặt kiến trúc, Gamma dựa trên kiến trúc không chia sẻ (shared-nothing) [STON86] bao gồm một số bộ xử lý được kết nối với nhau bởi một mạng truyền thông như hypercube hoặc vòng, với các đĩa được kết nối trực tiếp tới từng bộ xử lý riêng lẻ. Người ta nhìn chung chấp nhận rằng các kiến trúc như vậy có thể được mở rộng để tích hợp hàng nghìn bộ xử lý. Trên thực tế, các máy cơ sở dữ liệu Teradata [TERA85] sử dụng kiến trúc không chia sẻ với hơn 200 bộ xử lý đã được đưa vào sử dụng. Ý tưởng then chốt thứ hai được Gamma sử dụng là việc dùng các thuật toán song song dựa trên băm. Không giống như các thuật toán được sử dụng bởi DIRECT, các thuật toán này không yêu cầu điều khiển tập trung và do đó, giống như kiến trúc phần cứng, có thể được mở rộng gần như vô hạn. Cuối cùng, để tận dụng tốt nhất băng thông I/O hạn chế do thế hệ ổ đĩa hiện tại cung cấp, Gamma sử dụng khái niệm **phân vùng ngang** [RIES78] (còn được gọi là **phân cụm lại** [LIVN87]) để phân phối các bộ của một quan hệ giữa nhiều ổ đĩa. Thiết kế này cho phép các quan hệ lớn được xử lý bởi nhiều bộ xử lý đồng thời mà không phát sinh bất kỳ chi phí phụ trội truyền thông nào.

Sau khi thiết kế phần mềm Gamma được hoàn thành vào mùa thu năm 1984, công việc bắt đầu trên nguyên mẫu đầu tiên, nguyên mẫu này đã hoạt động vào mùa thu năm 1985. Phiên bản Gamma này được triển khai trên nền một hệ thống đa máy tính hiện có bao gồm 20 bộ xử lý VAX 11/750 [DEWI84b]. Trong giai đoạn 1986-1988, nguyên mẫu được cải tiến thông qua việc bổ sung một số toán tử mới (ví dụ: các toán tử tổng hợp và cập nhật), các phương pháp kết nối song song mới (Hybrid, Grace, và Sort-Merge [SCHN89a]), cùng một cơ chế điều khiển đồng thời hoàn chỉnh. Ngoài ra, chúng tôi cũng tiến hành một số nghiên cứu về hiệu năng của hệ thống trong giai đoạn này [DEWI86, DEWI88, GHAN89, GHAN90]. Vào mùa xuân năm 1989, Gamma được chuyển sang một hypercube Intel iPSC/2 gồm 32 bộ xử lý và nguyên mẫu dựa trên VAX được loại bỏ.

Gamma tương tự với một số nỗ lực tích cực khác về máy cơ sở dữ liệu song song. Ngoài Teradata [TERA85], Bubba [COPE88] và Tandem [TAND88] cũng sử dụng kiến trúc không chia sẻ và áp dụng khái niệm phân vùng ngang. Trong khi Teradata và Tandem cũng dựa vào băm để phi tập trung hóa việc thực thi các thuật toán song song của chúng, cả hai hệ thống có xu hướng dựa vào các thuật toán kết nối tương đối truyền thống như sort-merge để xử lý các mảnh của quan hệ tại mỗi vị trí. Gamma, XPRS [STON88], và Volcano [GRAE89] đều sử dụng các phiên bản song song của thuật toán kết nối Hybrid [DEWI84a].

Phần còn lại của bài báo này được tổ chức như sau. Trong Section 2, chúng tôi mô tả phần cứng được sử dụng bởi mỗi nguyên mẫu Gamma và kinh nghiệm của chúng tôi với từng nguyên mẫu. Section 3 thảo luận về tổ chức của phần mềm Gamma và mô tả cách các truy vấn nhiều toán tử được điều khiển. Các thuật toán song song được Gamma sử dụng được mô tả trong Section 4 và các kỹ thuật chúng tôi sử dụng cho quản lý giao dịch và sự cố được trình bày trong Section 5. Section 6 trình bày một nghiên cứu về hiệu năng của nguyên mẫu hypercube Intel gồm 32 bộ xử lý. Các kết luận và hướng nghiên cứu tương lai của chúng tôi được mô tả trong Section 7.
