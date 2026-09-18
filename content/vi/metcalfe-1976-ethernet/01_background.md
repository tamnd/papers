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
content_sha256: 239776b550ba2f4c1920176b4ea43e5806a0b4cba1a63bb03470c4f83e0d42e6
translated_from: content/en/metcalfe-1976-ethernet/01_background.md
source_content_sha256: 964dff0900dd9c2f7a180cb47370587a5f4e274004d4e01bc155170a21a6053a
translation_model: gpt-5
translation_run: 20260917T145710Z
glossary_version: 6
glossary_terms_sha256: 3a5b9dd3cd6211761c92d70db4c4910c364b1cae9e5e732eea77349f449c860b
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Có thể đặc trưng tính toán phân tán (distributed computing) như một phổ các hoạt động khác nhau về mức độ phi tập trung, trong đó một cực là kết nối mạng máy tính từ xa và cực kia là đa xử lý. Kết nối mạng máy tính từ xa là sự liên kết lỏng lẻo giữa các hệ thống tính toán trước đây biệt lập, cách xa nhau và khá lớn. Đa xử lý là việc xây dựng các hệ thống tính toán trước đây nguyên khối và tuần tự từ những thành phần ngày càng nhiều và nhỏ hơn, tính toán song song. Gần giữa phổ này là kết nối mạng cục bộ (local networking), tức liên kết các máy tính nhằm đạt được khả năng chia sẻ tài nguyên của kết nối mạng máy tính và tính song song của đa xử lý.

Khoảng cách giữa các máy tính và tốc độ bit tương ứng của việc truyền thông giữa chúng có thể được dùng để chia phổ tính toán phân tán thành các hoạt động rộng. Tích của khoảng cách và tốc độ bit, hiện khoảng 1 gigabit-meter trên giây (1 Gbmps), là một chỉ dấu về giới hạn của công nghệ truyền thông hiện tại và có thể được kỳ vọng sẽ tăng theo thời gian:

| Hoạt động | Khoảng cách | Tốc độ bit |
|---|---|---|
| Mạng từ xa | > 10 km | < .1 Mbps |
| Mạng cục bộ | 10–.1 km | .1–10 Mbps |
| Bộ đa xử lý | < .1 km | > 10 Mbps |

### 1.1 Kết nối mạng máy tính từ xa {#metcalfe-1976-ethernet-s1-1 .section tag=0295}

Kết nối mạng máy tính phát triển từ truyền thông *terminal-computer* trong viễn thông, trong đó mục tiêu là kết nối các terminal từ xa với một cơ sở tính toán trung tâm. Khi nhu cầu liên kết *computer-computer* tăng lên, chính các máy tính được sử dụng để cung cấp khả năng truyền thông [2, 4, 29]. Truyền thông *using* máy tính làm bộ chuyển mạch gói tin [15-21, 26] và truyền thông *among* các máy tính để chia sẻ tài nguyên [10, 32] đều được thúc đẩy bởi sự phát triển của Arpa Computer Network.

Aloha Network tại University of Hawaii ban đầu được phát triển để áp dụng các kỹ thuật packet radio cho việc truyền thông giữa một máy tính trung tâm và các terminal của nó phân tán trên các đảo Hawaii [1, 2]. Nhiều terminal hiện nay là các minicomputer, giao tiếp với nhau bằng cách sử dụng Menehune của Aloha Network làm bộ chuyển mạch gói tin. Menehune và một Arpanet Imp hiện được kết nối, cung cấp cho các terminal trên Aloha Network quyền truy cập vào các tài nguyên tính toán trên lục địa Hoa Kỳ.

Cũng như các mạng máy tính đã phát triển qua các lục địa và đại dương để liên kết các cơ sở tính toán lớn trên toàn thế giới, hiện nay chúng đang phát triển dọc theo các hành lang và giữa các tòa nhà để liên kết các minicomputer trong văn phòng và phòng thí nghiệm [3, 12, 13, 14, 35].

### 1.2 Đa xử lý {#metcalfe-1976-ethernet-s1-2 .section tag=0296}

Đa xử lý ban đầu có dạng kết nối một bộ điều khiển I/O với một máy tính trung tâm lớn; Asp của IBM là một

Communications of the ACM

July 1976  
Volume 19 ví dụ kinh điển [29]. Tiếp theo, nhiều bộ xử lý trung tâm được kết nối với một bộ nhớ chung để cung cấp năng lực lớn hơn cho các ứng dụng bị giới hạn bởi tính toán [33]. Đối với một số ứng dụng này, các kiến trúc đa bộ xử lý kỳ lạ hơn như Illiac IV đã được đưa vào [5].

Gần đây hơn, các minicomputer được kết nối trong các cấu hình đa bộ xử lý nhằm đạt được tính kinh tế, độ tin cậy và tính mô-đun của hệ thống cao hơn [24, 36]. Xu hướng đã hướng tới phi tập trung hóa để tăng độ tin cậy; các hệ thống đa bộ xử lý ghép nối lỏng phụ thuộc ít hơn vào bộ nhớ trung tâm dùng chung và nhiều hơn vào *thin wires* cho truyền thông giữa các tiến trình, với mức cô lập thành phần cao hơn [18, 26]. Với việc tiếp tục làm mỏng truyền thông giữa các bộ xử lý nhằm tăng độ tin cậy và sự phát triển của các ứng dụng có thể phân tán, đa xử lý đang dần tiến tới một dạng tính toán phân tán cục bộ.

### 1.3 Kết nối mạng máy tính cục bộ {#metcalfe-1976-ethernet-s1-3 .section tag=0297}

Ethernet có nhiều mục tiêu chung với các mạng cục bộ khác như Mitre’s Mitrix, Bell Telephone Laboratory’s Spider và Distributed Computing System (DCS) của U.C. Irvine [12, 13, 14, 35]. Các nguyên mẫu của cả bốn phương thức kết nối mạng cục bộ đều hoạt động ở tốc độ bit từ một đến ba megabit trên giây. Mitrix và Spider có một minicomputer trung tâm để chuyển mạch và phân bổ băng thông, trong khi DCS và Ethernet sử dụng điều khiển phân tán. Spider và DCS sử dụng đường truyền thông hình vòng, Mitrix sử dụng công nghệ CATV có sẵn trên thị trường để triển khai hai bus một chiều, còn Ethernet thử nghiệm của chúng tôi sử dụng một bus thụ động hai chiều phân nhánh. Sự khác biệt giữa các hệ thống này là do sự khác biệt giữa các ứng dụng dự kiến của chúng, sự khác biệt giữa các ràng buộc chi phí theo đó các đánh đổi được thực hiện, và sự khác biệt về quan điểm giữa các nhà nghiên cứu.

Trước khi đi vào mô tả chi tiết về Ethernet, chúng tôi đưa ra tổng quan sau đây (xem Hình 1).
