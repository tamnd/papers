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
section_title: Triển khai
tag: 02A5
kind: section
lang: vi
source: https://www.cl.cam.ac.uk/teaching/0809/DigiCommI/metcalfe1976ethernet.pdf
pdf_sha256: e1e9d67146a1d0955a39b4fbb8e2951d6cefb4f7231a01acb9c78852280da227
pdf_pages: 5-6
extraction: vision
extraction_model: gpt-5
content_sha256: 2be090df534a5adfa4a69bd857ddfb0af828d466714ca643da4da568a74b877b
translated_from: content/en/metcalfe-1976-ethernet/04_implementation.md
source_content_sha256: e9bebae1b9f3b693dc43043d582416e4b95bfe62644931fc35bb3ba64bfdd04a
translation_model: gpt-5
translation_run: 20260918T110147Z
glossary_version: 7
glossary_terms_sha256: 5bfb74d0e4b3e9a8237f78ceae59e221549684c174791655271c5455f7fd5e4e
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Các lựa chọn của chúng tôi về 1 kilometer, 3 megabits per second và 256 trạm cho các tham số của một Ethernet thử nghiệm dựa trên các đặc điểm của môi trường truyền thông máy tính phân tán cục bộ và đánh giá của chúng tôi về những gì có thể đạt được ở mức biên; chắc chắn chúng không phải là những hạn chế cứng thiết yếu đối với khái niệm Ethernet.

Chúng tôi kỳ vọng rằng kích thước tối đa hợp lý của mạng sẽ vào khoảng 1 kilometer cáp. Chúng tôi sử dụng con số làm việc này để lựa chọn giữa các Ether có mức suy hao tín hiệu khác nhau và để thiết kế các bộ thu phát với công suất và độ nhạy thích hợp.

Trạm chiếm ưu thế trên Ethernet thử nghiệm của chúng tôi là một minicomputer, trong đó 3 megabits per second là tốc độ truyền dữ liệu thuận tiện. Bằng cách giữ tốc độ cực đại thấp hơn nhiều so với tốc độ của đường truyền của máy tính tới bộ nhớ chính, chúng tôi giảm nhu cầu về bộ đệm gói tin chuyên dụng đắt tiền trong các giao diện Ethernet của mình. Bằng cách giữ tốc độ cực đại cao nhất trong mức thuận tiện, chúng tôi cung cấp khả năng hỗ trợ số lượng trạm lớn hơn và các ứng dụng truyền thông đa xử lý tham vọng hơn.

Để đẩy nhanh việc xử lý gói tin mức thấp giữa 256 trạm, chúng tôi phân bổ byte 8-bit đầu tiên của gói tin cho trường địa chỉ đích và byte thứ hai cho trường địa chỉ nguồn (xem Hình 2). 256 là một con số đủ nhỏ để cho phép mỗi trạm nhận được phần băng thông khả dụng thích hợp và tiến gần tới giới hạn mà chúng tôi có thể đạt được với các kỹ thuật hiện tại để đấu nối vào cáp. 256 chỉ là một con số thuận tiện cho mức thấp nhất của giao thức; các mức cao hơn có thể hỗ trợ không gian địa chỉ mở rộng với các trường bổ sung bên trong gói tin và phần mềm để diễn giải chúng.

Triển khai Ethernet thử nghiệm của chúng tôi có bốn phần chính: Ether, các bộ thu phát, các giao diện và các bộ điều khiển (xem Hình 1).

### 4.1 Ether {#metcalfe-1976-ethernet-s4-1 .section tag=02A6}

Chúng tôi chọn triển khai Ether thử nghiệm bằng cách sử dụng cáp đồng trục suy hao thấp với các đầu nối và điểm đấu nối CATV có sẵn trên thị trường. Có thể trộn các Ether trên một Ethernet duy nhất; chúng tôi sử dụng cáp đồng trục đường kính nhỏ hơn để kết nối thuận tiện trong các cụm trạm và cáp đồng trục đường kính lớn hơn cho các đoạn chạy suy hao thấp giữa các cụm. Chi phí của Ether cáp đồng trục là không đáng kể so với chi phí của các hệ thống tính toán phân tán được Ethernet hỗ trợ.

### 4.2 Bộ thu phát {#metcalfe-1976-ethernet-s4-2 .section tag=02A7}

Các bộ thu phát thử nghiệm của chúng tôi có thể điều khiển một kilometer Ether cáp đồng trục được đấu nối bởi 256 trạm truyền ở tốc độ 3 megabits per second. Các bộ thu phát có thể *chịu được* (tức là hoạt động sau khi) việc nối tắt trực tiếp kéo dài, kết cuối Ether không đúng và việc điều khiển đồng thời bởi tất cả 256 trạm; chúng có thể *chịu đựng* (tức là hoạt động trong khi) các sai biệt điện thế đất và nhiễu điện hằng ngày, từ máy đánh chữ hoặc máy khoan điện, gặp phải khi các trạm cách nhau tới một kilometer.

Một bộ thu phát Ethernet gắn trực tiếp vào Ether chạy qua trên trần hoặc dưới sàn. Nó được cấp nguồn và điều khiển thông qua năm cặp dây xoắn trong một cáp giao diện mang dữ liệu truyền, dữ liệu nhận, phát hiện nhiễu và điện áp nguồn. Khi không được cấp nguồn, bộ thu phát tự ngắt kết nối điện khỏi Ether. Đây là nơi cuộc đấu tranh của chúng tôi vì độ tin cậy được quyết định thắng hay thua; một bộ thu phát hỏng có thể, nhưng *không nên*, làm sập toàn bộ Ethernet. Một mạch bộ định thời watchdog trong mỗi bộ thu phát cố gắng ngăn ngừa việc làm ô nhiễm Ether bằng cách tắt tầng đầu ra nếu nó hoạt động đáng ngờ. Để đơn giản hóa bộ thu phát, chúng tôi sử dụng dải tần cơ sở của Ether, nhưng một Ethernet có thể được xây dựng để sử dụng bất kỳ dải tần có kích thước phù hợp nào của một Ether ghép kênh phân chia theo tần số.

Mặc dù các bộ thu phát thử nghiệm của chúng tôi rất đơn giản và chỉ có thể chịu được suy hao tín hiệu giới hạn, chúng đã chứng tỏ là hoàn toàn đủ và đáng tin cậy. Một thiết kế bộ thu phát tinh vi hơn có thể cho phép phân nhánh thụ động của Ether và khoảng cách giữa các trạm rộng hơn.

### 4.3 Giao diện {#metcalfe-1976-ethernet-s4-3 .section tag=02A8}

Một giao diện Ethernet tuần tự hóa và giải tuần tự hóa dữ liệu song song được sử dụng bởi trạm của nó. Có một số loại trạm khác nhau trên Ethernet của chúng tôi; một giao diện phải được xây dựng cho từng loại.

Mỗi giao diện được trang bị phần cứng cần thiết để tính toán một tổng kiểm tra dư vòng 16-bit (CRC) trên dữ liệu nối tiếp khi nó được truyền và nhận. Tổng kiểm tra này chỉ bảo vệ chống lại các lỗi trong Ether và *cụ thể không phải* chống lại các lỗi trong các phần song song của phần cứng giao diện hoặc trạm. Các tổng kiểm tra bằng phần mềm mức cao hơn được khuyến nghị cho các ứng dụng yêu cầu mức độ tin cậy cao hơn.

Một giao diện truyền sử dụng địa chỉ bộ đệm gói tin và số lượng từ để tuần tự hóa và mã hóa pha một số lượng thay đổi các từ 16-bit được lấy từ bộ nhớ của trạm và truyền tới bộ thu phát, với một bit bắt đầu (gọi là SYNC trong Hình 2) đứng trước và CRC đứng sau. Một giao diện nhận sử dụng sự xuất hiện của sóng mang để phát hiện sự bắt đầu của gói tin và sử dụng bit SYNC để thu nhận pha bit. Khi sóng mang còn bật, giao diện giải mã và giải tuần tự hóa luồng bit đến, đặt các từ 16-bit vào một bộ đệm gói tin trong bộ nhớ chính của trạm. Khi sóng mang biến mất, giao diện kiểm tra rằng một số nguyên các từ 16-bit đã được nhận và CRC là đúng. Từ cuối cùng được nhận được giả định là CRC và không được sao chép vào bộ đệm gói tin.

Các giao diện này thông thường bao gồm phần cứng chỉ chấp nhận những gói tin có địa chỉ thích hợp trong phần đầu của chúng. Bộ lọc địa chỉ bằng phần cứng giúp một trạm tránh việc xử lý gói tin bằng phần mềm nặng nề khi

Communications  
of the ACM  
July 1976  
Volume 19 Ether rất bận rộn với việc mang lưu lượng dành cho các trạm khác.

Fig. 2. Bố cục gói tin Ethernet. {#metcalfe-1976-ethernet-fig-2 .figure tag=02A9}

### 4.4 Bộ điều khiển {#metcalfe-1976-ethernet-s4-4 .section tag=02AA}

Bộ điều khiển Ethernet là phần sụn hoặc phần mềm mức thấp dành riêng cho trạm để đưa các gói tin vào và ra khỏi Ether. Khi xảy ra va chạm được phát hiện tại nguồn, trách nhiệm của bộ điều khiển nguồn là tạo ra một khoảng thời gian truyền lại ngẫu nhiên mới dựa trên số lần va chạm đã được cập nhật. Chúng tôi đã nghiên cứu một số thuật toán để điều khiển tốc độ truyền lại trong các trạm nhằm duy trì hiệu suất Ether [20, 22]. Các thuật toán thực tế nhất trong số này ước lượng tải lưu lượng bằng cách sử dụng lịch sử va chạm gần đây.

Các khoảng thời gian truyền lại là bội số của một *slot*, thời gian tối đa giữa lúc bắt đầu một lần truyền và lúc phát hiện một va chạm, tức một độ trễ khứ hồi đầu cuối đến đầu cuối. Một bộ điều khiển Ethernet bắt đầu truyền mỗi gói tin mới với khoảng thời gian truyền lại trung bình bằng một slot. Mỗi lần một nỗ lực truyền kết thúc bằng va chạm, bộ điều khiển trì hoãn trong một khoảng thời gian có độ dài ngẫu nhiên với giá trị trung bình gấp đôi khoảng thời gian trước đó, nhường cho bất kỳ gói tin nào đang đi qua, rồi thử truyền lại. Heuristic này xấp xỉ một thuật toán mà chúng tôi gọi là Binary Exponential Backoff (xem Hình 3) [22].

Khi mạng không có tải và các va chạm hiếm khi xảy ra, giá trị trung bình hiếm khi rời khỏi một và việc truyền lại diễn ra nhanh chóng. Khi tải lưu lượng tăng lên, nhiều va chạm hơn xảy ra, một lượng lớn gói tin chờ tích tụ tại các trạm, các khoảng thời gian truyền lại tăng lên, và lưu lượng truyền lại giảm tốc để duy trì hiệu suất kênh.
