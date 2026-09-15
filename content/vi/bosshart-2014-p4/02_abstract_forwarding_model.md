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
section: "2"
section_title: MÔ HÌNH CHUYỂN TIẾP TRỪU TƯỢNG
tag: "0090"
kind: section
lang: vi
source: arxiv:1312.1719
pdf_sha256: 2bb0ccb7b5410868efdecc9ef5208d235c6f3aa75dee84aa992751aed117a42f
pdf_pages: 2-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 9905e2cb16b4bd30b2f28c22d67c3a0bf4d24baf1087c5e7412b21452dcf13cc
translated_from: content/en/bosshart-2014-p4/02_abstract_forwarding_model.md
source_content_sha256: 05698be2c0f93db00cd6cf1e551213006816fd5c3e699517631731cd535d3ccc
translation_model: gpt-5
translation_run: 20260914T163737Z
glossary_version: 6
glossary_terms_sha256: 3a5b9dd3cd6211761c92d70db4c4910c364b1cae9e5e732eea77349f449c860b
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Trong mô hình trừu tượng của chúng tôi (Fig. 2), các chuyển mạch chuyển tiếp các gói tin thông qua một bộ phân tích cú pháp có thể lập trình, tiếp theo là nhiều giai đoạn match+action, được sắp xếp theo chuỗi, song song, hoặc kết hợp cả hai. Được suy ra từ OpenFlow, mô hình của chúng tôi đưa ra ba khái quát hóa. Thứ nhất, OpenFlow giả định một bộ phân tích cú pháp cố định, trong khi mô hình của chúng tôi hỗ trợ một bộ phân tích cú pháp có thể lập trình để cho phép định nghĩa các phần đầu mới. Thứ hai, OpenFlow giả định các giai đoạn match+action nằm theo chuỗi, trong khi trong mô hình của chúng tôi chúng có thể nằm song song hoặc theo chuỗi. Thứ ba, mô hình của chúng tôi giả định rằng các hành động được tạo thành từ các nguyên thủy không phụ thuộc giao thức được chuyển mạch hỗ trợ.

Mô hình trừu tượng của chúng tôi khái quát hóa cách các gói tin được xử lý trong các thiết bị chuyển tiếp khác nhau (ví dụ, các chuyển mạch Ethernet, các bộ định tuyến, các bộ cân bằng tải) và bởi các công nghệ khác nhau (ví dụ, các ASIC chuyển mạch chức năng cố định, các NPU, các chuyển mạch có thể cấu hình lại, các chuyển mạch phần mềm, các FPGA). Điều này cho phép chúng tôi xây dựng một ngôn ngữ chung (P4) để biểu diễn cách các gói tin được xử lý theo mô hình trừu tượng chung của chúng tôi. Do đó, các lập trình viên có thể tạo ra các chương trình không phụ thuộc mục tiêu mà một trình biên dịch có thể ánh xạ tới nhiều thiết bị chuyển tiếp khác nhau, từ các chuyển mạch phần mềm tương đối chậm đến các chuyển mạch dựa trên ASIC nhanh nhất.

Hình.

Figure 2: Mô hình chuyển tiếp trừu tượng. {#bosshart-2014-p4-fig-2 .figure tag=0091}

Mô hình chuyển tiếp được điều khiển bởi hai loại thao tác: Configure và Populate. Các thao tác Configure lập trình bộ phân tích cú pháp, thiết lập thứ tự của các giai đoạn match+action, và đặc tả các trường phần đầu được xử lý bởi mỗi giai đoạn. Cấu hình xác định các giao thức nào được hỗ trợ và cách chuyển mạch có thể xử lý các gói tin. Các thao tác Populate thêm (và loại bỏ) các mục nhập vào các bảng match+action đã được đặc tả trong quá trình cấu hình. Population xác định chính sách được áp dụng cho các gói tin tại bất kỳ thời điểm nào.

Với mục đích của bài báo này, chúng tôi giả định rằng cấu hình và population là hai pha riêng biệt. Cụ thể, chuyển mạch không cần xử lý các gói tin trong quá trình cấu hình. Tuy nhiên, chúng tôi kỳ vọng các triển khai sẽ cho phép xử lý gói tin trong quá trình tái cấu hình một phần hoặc toàn bộ, cho phép nâng cấp mà không có thời gian ngừng hoạt động. Mô hình của chúng tôi chủ ý cho phép và khuyến khích việc tái cấu hình không làm gián đoạn chuyển tiếp.

Rõ ràng, pha cấu hình có ít ý nghĩa trong các chuyển mạch ASIC chức năng cố định; đối với loại chuyển mạch này, công việc của trình biên dịch chỉ đơn giản là kiểm tra xem chip có thể hỗ trợ chương trình P4 hay không. Thay vào đó, mục tiêu của chúng tôi là nắm bắt xu hướng chung hướng tới các đường ống xử lý gói tin có thể cấu hình lại nhanh, như được mô tả trong [2][3].

Các gói tin đến trước tiên được xử lý bởi bộ phân tích cú pháp. Phần thân gói tin được giả định là được đệm riêng và không khả dụng cho việc so khớp. Bộ phân tích cú pháp nhận dạng và trích xuất các trường từ phần đầu, do đó xác định các giao thức được chuyển mạch hỗ trợ. Mô hình không đưa ra giả định nào về ý nghĩa của các phần đầu giao thức, chỉ rằng biểu diễn đã được phân tích cú pháp định nghĩa một tập hợp các trường mà trên đó việc so khớp và các hành động hoạt động.

Các trường phần đầu được trích xuất sau đó được chuyển tới các bảng match+action. Các bảng match+action được chia giữa ingress và egress. Trong khi cả hai có thể sửa đổi phần đầu gói tin, ingress match+action xác định (các) cổng egress và xác định hàng đợi mà gói tin được đặt vào. Dựa trên xử lý ingress, gói tin có thể được chuyển tiếp, sao chép (cho multicast, span, hoặc tới mặt phẳng điều khiển), loại bỏ, hoặc kích hoạt điều khiển luồng. Egress match+action thực hiện các sửa đổi theo từng thực thể đối với phần đầu gói tin – ví dụ, đối với các bản sao multicast. Các bảng hành động (counters, policers, v.v.) có thể được liên kết với một luồng để theo dõi trạng thái từ frame này tới frame khác.

Các gói tin có thể mang thêm thông tin giữa các giai đoạn, được gọi là metadata, được xử lý giống hệt như các trường phần đầu gói tin. Một số ví dụ về metadata bao gồm cổng ingress, đích truyền và hàng đợi, một dấu thời gian có thể được sử dụng cho việc lập lịch gói tin, và dữ liệu được truyền từ bảng này sang bảng khác không liên quan đến việc thay đổi biểu diễn đã được phân tích cú pháp của gói tin như một định danh mạng ảo.

Các cơ chế xếp hàng được xử lý theo cùng cách như OpenFlow hiện tại: một hành động ánh xạ một gói tin tới một hàng đợi, được cấu hình để nhận một cơ chế dịch vụ cụ thể. Cơ chế dịch vụ (ví dụ, minimum rate, DRR) được chọn như một phần của cấu hình chuyển mạch.

Mặc dù nằm ngoài phạm vi của bài báo này, các nguyên thủy hành động có thể được thêm vào để cho phép lập trình viên triển khai các giao thức điều khiển tắc nghẽn mới hoặc hiện có. Ví dụ, chuyển mạch có thể được lập trình để thiết lập bit ECN dựa trên các điều kiện mới, hoặc nó có thể triển khai một cơ chế điều khiển tắc nghẽn độc quyền sử dụng các bảng match+action.
