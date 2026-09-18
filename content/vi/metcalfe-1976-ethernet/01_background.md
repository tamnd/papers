---
paper: metcalfe-1976-ethernet
title: 'Ethernet: Distributed Packet Switching for Local Computer Networks'
authors:
  - Robert M. Metcalfe
  - David R. Boggs
year: 1976
venue: Communications of the ACM
field: networks
section: "1"
section_title: Bối cảnh
tag: "0294"
kind: section
lang: vi
source: https://www.cl.cam.ac.uk/teaching/0809/DigiCommI/metcalfe1976ethernet.pdf
pdf_sha256: e1e9d67146a1d0955a39b4fbb8e2951d6cefb4f7231a01acb9c78852280da227
pdf_pages: 1-2
extraction: vision
extraction_model: gpt-5
content_sha256: 5db8d3d2fd208eb216ed2e72e496e6a63f3beb23e4df0c8ae534984126a43ec1
translated_from: content/en/metcalfe-1976-ethernet/01_background.md
source_content_sha256: 964dff0900dd9c2f7a180cb47370587a5f4e274004d4e01bc155170a21a6053a
translation_model: gpt-5
translation_run: 20260918T110147Z
glossary_version: 7
glossary_terms_sha256: 5bfb74d0e4b3e9a8237f78ceae59e221549684c174791655271c5455f7fd5e4e
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Có thể đặc trưng hóa tính toán phân tán như một phổ các hoạt động thay đổi theo mức độ phi tập trung của chúng, với một cực là mạng máy tính từ xa và cực kia là xử lý đa nhiệm. Mạng máy tính từ xa là sự kết nối lỏng lẻo của các hệ thống tính toán trước đây bị cô lập, cách xa nhau và tương đối lớn. Xử lý đa nhiệm là việc xây dựng các hệ thống tính toán trước đây nguyên khối và tuần tự từ những phần ngày càng nhiều và nhỏ hơn, thực hiện tính toán song song. Gần giữa phổ này là mạng cục bộ, sự kết nối các máy tính để đạt được khả năng chia sẻ tài nguyên của mạng máy tính và tính song song của xử lý đa nhiệm.

Khoảng cách giữa các máy tính và tốc độ bit liên quan trong việc truyền thông của chúng có thể được dùng để chia phổ tính toán phân tán thành các hoạt động rộng. Tích của khoảng cách và tốc độ bit, hiện khoảng 1 gigabit-meter mỗi giây (1 Gbmps), là một chỉ dấu về giới hạn của công nghệ truyền thông hiện tại và có thể được kỳ vọng sẽ tăng theo thời gian:

| Hoạt động | Khoảng cách | Tốc độ bit |
|---|---|---|
| Mạng từ xa | > 10 km | < .1 Mbps |
| Mạng cục bộ | 10–.1 km | .1–10 Mbps |
| Bộ xử lý đa nhiệm | < .1 km | > 10 Mbps |

### 1.1 Mạng máy tính từ xa {#metcalfe-1976-ethernet-s1-1 .section tag=0295}

Mạng máy tính phát triển từ truyền thông *terminal-computer* trong viễn thông, trong đó mục tiêu là kết nối các terminal từ xa với một cơ sở tính toán trung tâm. Khi nhu cầu kết nối *computer-computer* tăng lên, chính các máy tính được sử dụng để cung cấp truyền thông [2, 4, 29]. Truyền thông *using* máy tính làm các bộ chuyển mạch gói tin [15-21, 26] và truyền thông *among* các máy tính để chia sẻ tài nguyên [10, 32] đều được thúc đẩy bởi sự phát triển của Arpa Computer Network.

Aloha Network tại University of Hawaii ban đầu được phát triển để áp dụng các kỹ thuật radio gói tin cho truyền thông giữa một máy tính trung tâm và các terminal của nó phân tán trên các quần đảo Hawaii [1, 2]. Nhiều terminal hiện nay là các minicomputer truyền thông với nhau bằng cách sử dụng Menehune của Aloha Network như một bộ chuyển mạch gói tin. Menehune và một Arpanet Imp hiện đã được kết nối, cung cấp cho các terminal trên Aloha Network quyền truy cập vào các tài nguyên tính toán trên đất liền Hoa Kỳ.

Cũng như các mạng máy tính đã phát triển xuyên qua các lục địa và đại dương để kết nối các cơ sở tính toán lớn trên toàn thế giới, chúng hiện đang phát triển dọc theo các hành lang và giữa các tòa nhà để kết nối các minicomputer trong văn phòng và phòng thí nghiệm [3, 12, 13, 14, 35].

### 1.2 Xử lý đa nhiệm {#metcalfe-1976-ethernet-s1-2 .section tag=0296}

Xử lý đa nhiệm ban đầu có dạng kết nối một bộ điều khiển I/O với một máy tính trung tâm lớn; Asp của IBM là một

Communications of the ACM

Tháng 7 1976  
Tập 19 ví dụ kinh điển [29]. Tiếp theo, nhiều bộ xử lý trung tâm được kết nối với một bộ nhớ chung để cung cấp nhiều năng lực hơn cho các ứng dụng bị giới hạn bởi tính toán [33]. Đối với một số ứng dụng này, các kiến trúc bộ xử lý đa nhiệm phức tạp hơn như Illiac IV đã được đưa vào [5].

Gần đây hơn, các minicomputer đã được kết nối trong các cấu hình bộ xử lý đa nhiệm vì tính kinh tế, độ tin cậy và tính mô-đun hệ thống tăng lên [24, 36]. Xu hướng đã hướng tới sự phi tập trung để tăng độ tin cậy; các hệ thống bộ xử lý đa nhiệm ghép lỏng phụ thuộc ít hơn vào bộ nhớ trung tâm dùng chung và nhiều hơn vào *thin wires* cho truyền thông giữa các tiến trình với sự cô lập thành phần tăng lên [18, 26]. Với việc tiếp tục làm mỏng truyền thông giữa các bộ xử lý vì độ tin cậy và sự phát triển của các ứng dụng có thể phân phối, xử lý đa nhiệm đang dần tiến gần tới một dạng cục bộ của tính toán phân tán.

### 1.3 Mạng máy tính cục bộ {#metcalfe-1976-ethernet-s1-3 .section tag=0297}

Ethernet chia sẻ nhiều mục tiêu với các mạng cục bộ khác như Mitre’s Mitrix, Bell Telephone Laboratory’s Spider và U.C. Irvine’s Distributed Computing System (DCS) [12, 13, 14, 35]. Các nguyên mẫu của cả bốn sơ đồ mạng cục bộ này hoạt động ở tốc độ bit từ một đến ba megabit mỗi giây. Mitrix và Spider có một minicomputer trung tâm để chuyển mạch và phân bổ băng thông, trong khi DCS và Ethernet sử dụng điều khiển phân tán. Spider và DCS sử dụng đường truyền thông hình vòng, Mitrix sử dụng công nghệ CATV có sẵn để triển khai hai bus một chiều, và Ethernet thử nghiệm của chúng tôi sử dụng một bus thụ động hai chiều phân nhánh. Sự khác biệt giữa các hệ thống này là do sự khác biệt giữa các ứng dụng dự kiến của chúng, sự khác biệt giữa các ràng buộc chi phí mà trong đó các đánh đổi được thực hiện, và sự khác biệt về quan điểm giữa các nhà nghiên cứu.

Trước khi đi vào mô tả chi tiết về Ethernet, chúng tôi đưa ra tổng quan sau đây (xem Hình 1).
