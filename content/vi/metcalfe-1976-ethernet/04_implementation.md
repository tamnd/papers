---
paper: metcalfe-1976-ethernet
title: 'Ethernet: Distributed Packet Switching for Local Computer Networks'
authors:
  - Robert M. Metcalfe
  - David R. Boggs
year: 1976
venue: Communications of the ACM
field: networks
section: "4"
section_title: Cài đặt
tag: 02A5
kind: section
lang: vi
source: https://www.cl.cam.ac.uk/teaching/0809/DigiCommI/metcalfe1976ethernet.pdf
pdf_sha256: e1e9d67146a1d0955a39b4fbb8e2951d6cefb4f7231a01acb9c78852280da227
pdf_pages: 5-6
extraction: vision
extraction_model: gpt-5
content_sha256: 4c63f9a0e65afc1189c6112a0c81b083b9cf6b903748963f10e6cc82c6c97315
translated_from: content/en/metcalfe-1976-ethernet/04_implementation.md
source_content_sha256: e9bebae1b9f3b693dc43043d582416e4b95bfe62644931fc35bb3ba64bfdd04a
translation_model: gpt-5
translation_run: 20260917T145710Z
glossary_version: 6
glossary_terms_sha256: 3a5b9dd3cd6211761c92d70db4c4910c364b1cae9e5e732eea77349f449c860b
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Các lựa chọn của chúng tôi về 1 kilometer, 3 megabits per second và 256 trạm cho các tham số của một Ethernet thử nghiệm dựa trên các đặc tính của môi trường truyền thông máy tính phân tán cục bộ và đánh giá của chúng tôi về những gì có thể đạt được ở mức cận biên; chắc chắn chúng không phải là những hạn chế cứng thiết yếu đối với khái niệm Ethernet.

Chúng tôi dự kiến rằng kích thước mạng tối đa hợp lý sẽ vào khoảng 1 kilometer cáp. Chúng tôi sử dụng con số làm việc này để lựa chọn giữa các Ether có mức suy hao tín hiệu khác nhau và thiết kế các bộ thu phát với công suất và độ nhạy thích hợp.

Trạm chủ đạo trên Ethernet thử nghiệm của chúng tôi là một minicomputer mà 3 megabits per second là tốc độ truyền dữ liệu thuận tiện. Bằng cách giữ tốc độ cực đại thấp hơn nhiều so với tốc độ của đường truyền từ máy tính tới bộ nhớ chính, chúng tôi giảm nhu cầu về bộ đệm gói tin chuyên dụng đắt tiền trong các giao diện Ethernet. Bằng cách giữ tốc độ cực đại cao đến mức thuận tiện, chúng tôi hỗ trợ số lượng trạm lớn hơn và các ứng dụng truyền thông đa xử lý tham vọng hơn.

Để đẩy nhanh việc xử lý gói tin ở mức thấp giữa 256 trạm, chúng tôi dành byte 8-bit đầu tiên của gói tin cho trường địa chỉ đích và byte thứ hai cho trường địa chỉ nguồn (xem Hình 2). 256 là một con số đủ nhỏ để cho phép mỗi trạm nhận được phần thích đáng của băng thông khả dụng và tiến gần tới giới hạn mà chúng tôi có thể đạt được với các kỹ thuật hiện tại để đấu nối vào cáp. 256 chỉ là một con số thuận tiện cho mức thấp nhất của giao thức; các mức cao hơn có thể hỗ trợ không gian địa chỉ mở rộng bằng các trường bổ sung bên trong gói tin và phần mềm để diễn giải chúng.

Cài đặt Ethernet thử nghiệm của chúng tôi có bốn phần chính: Ether, các bộ thu phát, các giao diện và các bộ điều khiển (xem Hình 1).

### 4.1 Ether {#metcalfe-1976-ethernet-s4-1 .section tag=02A6}

Chúng tôi chọn triển khai Ether thử nghiệm bằng cáp đồng trục suy hao thấp với các đầu nối và bộ đấu nối CATV bán sẵn. Có thể kết hợp các Ether trên một Ethernet duy nhất; chúng tôi sử dụng cáp đồng trục đường kính nhỏ hơn để kết nối thuận tiện bên trong các cụm trạm và cáp đồng trục đường kính lớn hơn cho các đoạn truyền suy hao thấp giữa các cụm. Chi phí của Ether bằng cáp đồng trục là không đáng kể so với chi phí của các hệ thống tính toán phân tán được Ethernet hỗ trợ.

### 4.2 Bộ thu phát {#metcalfe-1976-ethernet-s4-2 .section tag=02A7}

Các bộ thu phát thử nghiệm của chúng tôi có thể điều khiển một kilometer Ether bằng cáp đồng trục, được 256 trạm đấu nối và truyền ở tốc độ 3 megabits per second. Các bộ thu phát có thể *chịu đựng* (tức là vẫn hoạt động sau khi) bị ngắn mạch trực tiếp kéo dài, Ether được kết cuối không đúng cách và cả 256 trạm đồng thời phát; chúng có thể *chịu được* (tức là vẫn hoạt động trong khi) chênh lệch điện thế đất và nhiễu điện thông thường, từ máy đánh chữ hoặc máy khoan điện, gặp phải khi các trạm cách nhau tới một kilometer.

Một bộ thu phát Ethernet gắn trực tiếp vào Ether chạy qua trên trần hoặc dưới sàn. Nó được cấp nguồn và điều khiển thông qua năm cặp dây xoắn trong một cáp giao diện mang dữ liệu truyền, dữ liệu nhận, tín hiệu phát hiện nhiễu và các điện áp nguồn. Khi không được cấp nguồn, bộ thu phát tự ngắt kết nối điện khỏi Ether. Đây là nơi cuộc chiến của chúng tôi vì độ tin cậy được quyết định; một bộ thu phát bị hỏng có thể, nhưng *không nên*, làm toàn bộ Ethernet ngừng hoạt động. Một mạch bộ định thời giám sát trong mỗi bộ thu phát cố gắng ngăn Ether bị ô nhiễm bằng cách tắt tầng đầu ra nếu nó hoạt động đáng ngờ. Để đơn giản hóa bộ thu phát, chúng tôi sử dụng dải tần cơ sở của Ether, nhưng một Ethernet có thể được xây dựng để sử dụng bất kỳ dải có kích thước thích hợp nào của một Ether ghép kênh phân chia theo tần số.

Mặc dù các bộ thu phát thử nghiệm của chúng tôi rất đơn giản và chỉ có thể chịu được mức suy hao tín hiệu hạn chế, chúng đã chứng tỏ là khá đầy đủ và đáng tin cậy. Một thiết kế bộ thu phát tinh vi hơn có thể cho phép phân nhánh thụ động Ether và khoảng cách giữa các trạm lớn hơn.

### 4.3 Giao diện {#metcalfe-1976-ethernet-s4-3 .section tag=02A8}

Một giao diện Ethernet thực hiện chuyển đổi nối tiếp và giải nối tiếp dữ liệu song song được trạm của nó sử dụng. Có nhiều loại trạm khác nhau trên Ethernet của chúng tôi; phải xây dựng một giao diện cho từng loại.

Mỗi giao diện được trang bị phần cứng cần thiết để tính checksum dư thừa tuần hoàn 16-bit (CRC) trên dữ liệu nối tiếp khi dữ liệu được truyền và nhận. Checksum này chỉ bảo vệ chống lại các lỗi trong Ether và *cụ thể là không* chống lại các lỗi trong các phần song song của phần cứng giao diện hoặc trạm. Các checksum phần mềm ở mức cao hơn được khuyến nghị cho những ứng dụng yêu cầu mức độ tin cậy cao hơn.

Một giao diện truyền sử dụng địa chỉ bộ đệm gói tin và số lượng từ để chuyển đổi nối tiếp và mã hóa pha một số lượng thay đổi các từ 16-bit được lấy từ bộ nhớ của trạm và truyền tới bộ thu phát, đứng trước bởi một bit bắt đầu (được gọi là SYNC trong Hình 2) và theo sau bởi CRC. Một giao diện nhận sử dụng sự xuất hiện của sóng mang để phát hiện bắt đầu của một gói tin và sử dụng bit SYNC để xác định pha bit. Chừng nào sóng mang còn tồn tại, giao diện giải mã và chuyển đổi giải nối tiếp luồng bit đến, đặt các từ 16-bit vào bộ đệm gói tin trong bộ nhớ chính của trạm. Khi sóng mang biến mất, giao diện kiểm tra rằng đã nhận được một số nguyên các từ 16-bit và CRC là đúng. Từ cuối cùng được nhận được giả định là CRC và không được sao chép vào bộ đệm gói tin.

Các giao diện này thường bao gồm phần cứng chỉ chấp nhận những gói tin có địa chỉ thích hợp trong phần đầu của chúng. Bộ lọc địa chỉ bằng phần cứng giúp một trạm tránh việc xử lý gói tin bằng phần mềm nặng nề khi

Communications  
of the ACM  
July 1976  
Volume 19 Ether đang rất bận chuyển lưu lượng dành cho các trạm khác.

Fig. 2. Bố cục gói tin Ethernet. {#metcalfe-1976-ethernet-fig-2 .figure tag=02A9}

### 4.4 Bộ điều khiển {#metcalfe-1976-ethernet-s4-4 .section tag=02AA}

Bộ điều khiển Ethernet là firmware hoặc phần mềm cấp thấp dành riêng cho trạm, dùng để đưa các gói tin vào Ether và lấy chúng ra khỏi Ether. Khi xảy ra va chạm được phát hiện tại nguồn, bộ điều khiển nguồn có trách nhiệm tạo ra một khoảng thời gian truyền lại ngẫu nhiên mới dựa trên số lần va chạm đã được cập nhật. Chúng tôi đã nghiên cứu một số thuật toán để điều khiển tốc độ truyền lại tại các trạm nhằm duy trì hiệu năng của Ether [20, 22]. Các thuật toán thực tế nhất trong số này ước lượng tải lưu lượng bằng cách sử dụng lịch sử va chạm gần đây.

Các khoảng thời gian truyền lại là bội số của một *khe thời gian (slot)*, tức thời gian tối đa giữa lúc bắt đầu truyền và lúc phát hiện va chạm, bằng một độ trễ khứ hồi đầu-cuối. Bộ điều khiển Ethernet bắt đầu truyền mỗi gói tin mới với khoảng thời gian truyền lại trung bình bằng một khe thời gian. Mỗi khi một lần thử truyền kết thúc bằng va chạm, bộ điều khiển trì hoãn trong một khoảng thời gian có độ dài ngẫu nhiên với giá trị trung bình gấp đôi khoảng thời gian trước đó, nhường cho bất kỳ gói tin nào đang đi qua, rồi thử truyền lại. Heuristic này xấp xỉ một thuật toán mà chúng tôi gọi là Binary Exponential Backoff (xem Hình 3) [22].

Khi mạng không tải và các va chạm hiếm xảy ra, giá trị trung bình hiếm khi lệch khỏi một và việc truyền lại diễn ra nhanh chóng. Khi tải lưu lượng tăng, số va chạm xảy ra nhiều hơn, một lượng gói tin tồn đọng hình thành tại các trạm, các khoảng thời gian truyền lại tăng lên, và lưu lượng truyền lại lùi lại để duy trì hiệu năng của kênh.
