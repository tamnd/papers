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
section: "1"
section_title: GIỚI THIỆU
tag: 008D
kind: section
lang: vi
source: arxiv:1312.1719
pdf_sha256: 2bb0ccb7b5410868efdecc9ef5208d235c6f3aa75dee84aa992751aed117a42f
pdf_pages: 1-2
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 651adf8d5a3633f07fb6426600968f2a3fcbfd7e18fc0345a6b004248d717797
translated_from: content/en/bosshart-2014-p4/01_introduction.md
source_content_sha256: ec1c97db9c2528154e7a53184c654844c1afd835061ace9cf6950ef3c8035125
translation_model: gpt-5
translation_run: 20260914T163737Z
glossary_version: 6
glossary_terms_sha256: 3a5b9dd3cd6211761c92d70db4c4910c364b1cae9e5e732eea77349f449c860b
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Mạng được định nghĩa bằng phần mềm (Software-Defined Networking, SDN) cung cấp cho các nhà vận hành khả năng điều khiển mạng của họ bằng chương trình. Trong SDN, mặt phẳng điều khiển được tách biệt về mặt vật lý khỏi mặt phẳng chuyển tiếp, và một mặt phẳng điều khiển điều khiển nhiều thiết bị chuyển tiếp. Mặc dù các thiết bị chuyển tiếp có thể được lập trình theo nhiều cách, việc có một giao diện chung, mở và không phụ thuộc nhà cung cấp (như OpenFlow) cho phép một mặt phẳng điều khiển điều khiển các thiết bị chuyển tiếp từ những nhà cung cấp phần cứng và phần mềm khác nhau.

| Phiên bản | Ngày | Các trường phần đầu |
| --- | --- | --- |
| OF 1.0 | Dec 2009 | 12 trường (Ethernet, TCP/IPv4) |
| OF 1.1 | Feb 2011 | 15 trường (MPLS, metadata liên bảng) |
| OF 1.2 | Dec 2011 | 36 trường (ARP, ICMP, IPv6, v.v.) |
| OF 1.3 | Jun 2012 | 40 trường |
| OF 1.4 | Oct 2013 | 41 trường |

Bảng 1: Các trường được tiêu chuẩn OpenFlow nhận diện {#bosshart-2014-p4-tab-1 .table tag=008E}

Giao diện OpenFlow ban đầu khá đơn giản, với sự trừu tượng hóa của một bảng duy nhất gồm các quy tắc có thể đối sánh các gói tin dựa trên một tá trường phần đầu (ví dụ: địa chỉ MAC, địa chỉ IP, giao thức, số cổng TCP/UDP, v.v.). Trong năm năm qua, đặc tả đã ngày càng trở nên phức tạp hơn (xem Bảng 1), với nhiều trường phần đầu hơn và nhiều giai đoạn bảng quy tắc, nhằm cho phép các chuyển mạch bộc lộ nhiều khả năng hơn của chúng cho bộ điều khiển.

Sự gia tăng các trường phần đầu mới không có dấu hiệu dừng lại. Ví dụ, các nhà vận hành mạng trung tâm dữ liệu ngày càng muốn áp dụng các dạng đóng gói gói tin mới (ví dụ: NVGRE, VXLAN và STT), khiến họ phải triển khai các chuyển mạch phần mềm dễ mở rộng hơn với chức năng mới. Thay vì liên tục mở rộng đặc tả OpenFlow, chúng tôi cho rằng các chuyển mạch trong tương lai nên hỗ trợ các cơ chế linh hoạt để phân tích cú pháp gói tin và đối sánh các trường phần đầu, cho phép các ứng dụng bộ điều khiển khai thác những khả năng này thông qua một giao diện chung, mở (tức là một API “OpenFlow 2.0” mới). Cách tiếp cận tổng quát, có khả năng mở rộng như vậy sẽ đơn giản hơn, thanh nhã hơn và có tính hướng tới tương lai hơn so với tiêu chuẩn OpenFlow 1.x hiện nay.

Hình.

Hình 1: P4 là một ngôn ngữ để cấu hình các chuyển mạch. {#bosshart-2014-p4-fig-1 .figure tag=008F}

Các thiết kế chip gần đây chứng minh rằng tính linh hoạt như vậy có thể đạt được trên các ASIC tùy biến ở tốc độ terabit [1][2][3]. Lập trình thế hệ chip chuyển mạch mới này hoàn toàn không dễ dàng. Mỗi chip có giao diện cấp thấp riêng, tương tự như lập trình microcode. Trong bài báo này, chúng tôi phác thảo thiết kế của một ngôn ngữ cấp cao hơn dành cho các Bộ xử lý Gói tin Độc lập với Giao thức (Programming Protocol-independent Packet Processors, P4). Hình 1 cho thấy mối quan hệ giữa P4—được sử dụng để cấu hình một chuyển mạch, chỉ dẫn cách các gói tin được xử lý—và các API hiện có (chẳng hạn như OpenFlow), vốn được thiết kế để điền các bảng chuyển tiếp trong các chuyển mạch có chức năng cố định. P4 nâng mức độ trừu tượng hóa của việc lập trình mạng, và có thể đóng vai trò là một giao diện tổng quát giữa bộ điều khiển và các chuyển mạch. Nói cách khác, chúng tôi cho rằng các thế hệ OpenFlow trong tương lai nên cho phép bộ điều khiển chỉ dẫn chuyển mạch cách vận hành, thay vì bị ràng buộc bởi một thiết kế chuyển mạch cố định. Thách thức then chốt là tìm ra một “điểm cân bằng” giữa nhu cầu về khả năng biểu đạt và tính dễ triển khai trên một phạm vi rộng các chuyển mạch phần cứng và phần mềm. Khi thiết kế P4, chúng tôi có ba mục tiêu chính:
• Khả năng tái cấu hình. Bộ điều khiển phải có khả năng định nghĩa lại việc phân tích cú pháp và xử lý gói tin ngay tại hiện trường.
• Tính độc lập với giao thức. Chuyển mạch không nên bị ràng buộc với các định dạng gói tin cụ thể. Thay vào đó, bộ điều khiển phải có khả năng đặc tả (i) một bộ phân tích cú pháp gói tin để trích xuất các trường phần đầu với những tên và kiểu cụ thể và (ii) một tập hợp các bảng đối sánh+hành động có kiểu, xử lý các phần đầu này.
• Tính độc lập với đích. Cũng như một lập trình viên C không cần biết các đặc điểm cụ thể của CPU bên dưới, lập trình viên bộ điều khiển không cần biết chi tiết của chuyển mạch bên dưới. Thay vào đó, một trình biên dịch phải tính đến các khả năng của chuyển mạch khi chuyển một mô tả độc lập với đích (được viết bằng P4) thành một chương trình phụ thuộc đích (được sử dụng để cấu hình chuyển mạch).
Bố cục của bài báo như sau. Trước tiên, chúng tôi giới thiệu một mô hình chuyển tiếp chuyển mạch trừu tượng. Tiếp theo, chúng tôi giải thích nhu cầu về một ngôn ngữ mới để mô tả việc xử lý gói tin độc lập với giao thức. Sau đó, chúng tôi trình bày một ví dụ minh họa đơn giản, trong đó một nhà vận hành mạng muốn hỗ trợ một trường phần đầu gói tin mới và xử lý các gói tin qua nhiều giai đoạn. Chúng tôi sử dụng ví dụ này để khảo sát cách chương trình P4 đặc tả các phần đầu, bộ phân tích cú pháp gói tin, nhiều bảng đối sánh+hành động và luồng điều khiển qua các bảng này. Cuối cùng, chúng tôi thảo luận cách một trình biên dịch có thể ánh xạ các chương trình P4 tới các chuyển mạch đích.

Công trình liên quan. Năm 2011, Yadav và cộng sự [4] đề xuất một mô hình chuyển tiếp trừu tượng cho OpenFlow, nhưng ít chú trọng hơn đến trình biên dịch. Kangaroo [1] đưa ra khái niệm phân tích cú pháp có thể lập trình. Gần đây, Song [5] đề xuất cơ chế chuyển tiếp không phụ thuộc giao thức, chia sẻ mục tiêu độc lập với giao thức của chúng tôi, nhưng hướng nhiều hơn tới các bộ xử lý mạng. ONF đưa ra các mẫu định kiểu bảng để biểu đạt các khả năng đối sánh của chuyển mạch [6]. Các công trình gần đây về NOSIX [7] chia sẻ mục tiêu đặc tả linh hoạt các bảng đối sánh+hành động của chúng tôi, nhưng không xem xét tính độc lập với giao thức hoặc đề xuất một ngôn ngữ để đặc tả bộ phân tích cú pháp, các bảng và luồng điều khiển. Các công trình gần đây khác đề xuất một giao diện lập trình cho mặt phẳng dữ liệu nhằm giám sát, điều khiển tắc nghẽn và quản lý hàng đợi [8][9]. Bộ định tuyến mô-đun Click [10] hỗ trợ xử lý gói tin linh hoạt trong phần mềm, nhưng không ánh xạ các chương trình tới nhiều loại chuyển mạch phần cứng đích.
