---
paper: corbett-2012-spanner
title: 'Spanner: Google''s Globally-Distributed Database'
authors:
  - James C. Corbett
  - Jeffrey Dean
  - Michael Epstein
  - Andrew Fikes
  - Christopher Frost
  - J. J. Furman
  - Sanjay Ghemawat
  - Andrey Gubarev
  - Christopher Heiser
  - Peter Hochschild
year: 2012
venue: OSDI
field: databases
section: "5"
section_title: Đánh giá
tag: 00B4
kind: section
lang: vi
source: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.258.9924
pdf_sha256: 61875779e75f603d21aefba6d9bd9816d4dd0c18cf41089f43707249e24bbf88
pdf_pages: 9-12
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: e449fad13cf1ca66eab6163f6a57ff5a1be08b443d5d463dd0027e041df29d78
translated_from: content/en/corbett-2012-spanner/05_evaluation.md
source_content_sha256: c9c10f1c76c4c385602bfd1a438bf03cb71243d3ac151292d10068ebd24133fa
translation_model: gpt-6-astra
translation_run: 20260914T205336Z
glossary_version: 6
glossary_terms_sha256: a534ae50d60bff0e03804fd3c150e37d1876484531ab87df9c72dc4d0c455eb2
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Trước tiên, chúng tôi đo hiệu năng của Spanner về sao chép, giao dịch và tính sẵn sàng. Sau đó, chúng tôi cung cấp một số dữ liệu về hành vi của TrueTime và một nghiên cứu trường hợp về máy khách đầu tiên của chúng tôi, F1.

### 5.1 Các phép đo chuẩn vi mô {#corbett-2012-spanner-s5-1 .section tag=00B5}

Bảng 3 trình bày một số phép đo chuẩn vi mô cho Spanner. Các phép đo này được thực hiện trên các máy chia sẻ thời gian: mỗi spanserver chạy trên các đơn vị lập lịch có 4GB RAM và 4 lõi (AMD Barcelona 2200MHz). Các máy khách chạy trên những máy riêng biệt. Mỗi vùng chứa một spanserver. Các máy khách và các vùng được đặt trong một tập hợp các trung tâm dữ liệu có khoảng cách mạng dưới 1ms. (Cách bố trí như vậy có lẽ sẽ phổ biến: hầu hết các ứng dụng không cần phân tán toàn bộ dữ liệu của mình trên toàn thế giới.) Cơ sở dữ liệu thử nghiệm được tạo với 50 nhóm Paxos và 2500 thư mục. Các thao tác là những lần đọc và ghi độc lập có kích thước 4KB. Tất cả các lần đọc đều được phục vụ từ bộ nhớ sau một lần nén gộp, vì vậy chúng tôi chỉ đo chi phí phụ trội của ngăn xếp lời gọi của Spanner. Ngoài ra, một lượt đọc không được đo đã được thực hiện trước để làm nóng các cache vị trí.

Trong các thí nghiệm về độ trễ, máy khách phát ra đủ ít thao tác để tránh việc xếp hàng đợi tại các server. Từ các thí nghiệm với 1 bản sao, thời gian chờ xác nhận (commit wait) là khoảng 5ms và độ trễ Paxos là khoảng 9ms. Khi số lượng bản sao tăng, độ trễ gần như không đổi với độ lệch chuẩn nhỏ hơn vì Paxos thực thi song song tại các bản sao của một nhóm. Khi số lượng bản sao tăng, độ trễ để đạt đủ số đại biểu (quorum) trở nên ít nhạy hơn với tình trạng chậm tại một bản sao phụ.

Trong các thí nghiệm về thông lượng, máy khách phát ra đủ nhiều thao tác để làm bão hòa các

| bên tham gia | độ trễ (ms) |  |
| --- | --- | --- |
|  | trung bình | phân vị thứ 99 |
| 1 | 17.0 ±1.4 | 75.0 ±34.9 |
| 2 | 24.5 ±2.5 | 87.6 ±35.9 |
| 5 | 31.5 ±6.2 | 104.5 ±52.2 |
| 10 | 30.0 ±3.7 | 95.6 ±25.4 |
| 25 | 35.5 ±5.6 | 100.4 ±42.7 |
| 50 | 42.7 ±4.1 | 93.7 ±22.9 |
| 100 | 71.4 ±7.6 | 131.2 ±17.6 |
| 200 | 150.5 ±11.0 | 320.3 ±35.1 |

Bảng 4: Khả năng mở rộng của xác nhận hai pha. Giá trị trung bình và độ lệch chuẩn qua 10 lần chạy. {#corbett-2012-spanner-tab-4 .table tag=00B6}

CPU của các server. Các lần đọc ảnh chụp có thể thực thi tại bất kỳ bản sao nào đã được cập nhật, vì vậy thông lượng của chúng tăng gần như tuyến tính theo số lượng bản sao. Các giao dịch chỉ đọc gồm một lần đọc chỉ thực thi tại các nút lãnh đạo vì việc gán dấu thời gian phải diễn ra tại các nút lãnh đạo. Thông lượng của giao dịch chỉ đọc tăng theo số lượng bản sao vì số spanserver hoạt động hữu hiệu tăng: trong thiết lập thí nghiệm, số spanserver bằng số bản sao và các nút lãnh đạo được phân bố ngẫu nhiên giữa các vùng. Thông lượng ghi cũng được hưởng lợi từ chính đặc điểm này của thiết lập thí nghiệm (điều này giải thích mức tăng thông lượng khi tăng từ 3 lên 5 bản sao), nhưng lợi ích đó không bù được mức tăng tuyến tính của lượng công việc thực hiện cho mỗi lần ghi khi số lượng bản sao tăng.

Bảng 4 cho thấy xác nhận hai pha có thể mở rộng đến một số lượng bên tham gia hợp lý: bảng tóm tắt một tập hợp thí nghiệm được chạy trên 3 vùng, mỗi vùng có 25 spanserver. Việc mở rộng lên 50 bên tham gia vẫn đạt mức hợp lý ở cả giá trị trung bình và phân vị thứ 99, và độ trễ bắt đầu tăng rõ rệt ở mức 100 bên tham gia.

Hình 5 minh họa các lợi ích về tính sẵn sàng khi chạy Spanner trong nhiều trung tâm dữ liệu. Hình này cho thấy kết quả của ba thí nghiệm về thông lượng khi có sự cố trung tâm dữ liệu, tất cả được vẽ chồng lên cùng một thang thời gian. Toàn hệ thống thử nghiệm gồm 5 vùng $Z_i$, mỗi vùng có 25 spanserver. Cơ sở dữ liệu thử nghiệm được phân mảnh thành 1250 nhóm Paxos và 100 máy khách thử nghiệm liên tục phát ra các lần đọc không dùng ảnh chụp với tổng tốc độ 50K lần đọc/giây. Tất cả các nút lãnh đạo đều được chủ động đặt tại $Z_1$. Sau năm giây kể từ khi bắt đầu mỗi lần thử nghiệm, tất cả các server trong một vùng bị buộc dừng: *không có nút lãnh đạo* buộc dừng $Z_2$; *dừng cứng nút lãnh đạo* buộc dừng $Z_1$; *dừng mềm nút lãnh đạo* buộc dừng $Z_1$, nhưng thông báo cho tất cả các server rằng chúng cần bàn giao vai trò lãnh đạo trước.

Việc buộc dừng $Z_2$ không ảnh hưởng đến thông lượng đọc. Việc buộc dừng $Z_1$ trong khi cho các nút lãnh đạo thời gian để bàn giao vai trò lãnh đạo sang một vùng khác chỉ gây ảnh hưởng nhỏ: mức giảm thông lượng không thể hiện rõ trên đồ thị, nhưng vào khoảng 3-4%. Mặt khác, việc buộc dừng $Z_1$ mà không báo trước gây ảnh hưởng nghiêm trọng: tốc độ hoàn tất giảm xuống gần 0. Tuy nhiên, khi các nút lãnh đạo được bầu lại, thông lượng của hệ thống tăng lên khoảng 100K lần đọc/giây do hai đặc điểm của thí nghiệm: hệ thống có năng lực xử lý dư thừa và các thao tác được xếp vào hàng đợi trong thời gian nút lãnh đạo không sẵn sàng. Do đó, thông lượng của hệ thống tăng lên trước khi ổn định trở lại ở tốc độ trong trạng thái ổn định.

Chúng tôi cũng có thể thấy ảnh hưởng của việc thời hạn thuê vai trò lãnh đạo Paxos (leader lease) được đặt là 10 giây. Khi chúng tôi buộc dừng vùng, thời điểm hết hạn thuê vai trò lãnh đạo của các nhóm sẽ phân bố đều trong 10 giây tiếp theo. Ngay sau khi mỗi quyền thuê của một nút lãnh đạo đã dừng hết hạn, một nút lãnh đạo mới được bầu. Khoảng 10 giây sau thời điểm buộc dừng, tất cả các nhóm đều có nút lãnh đạo và thông lượng đã phục hồi. Thời hạn thuê ngắn hơn sẽ giảm ảnh hưởng của việc server dừng hoạt động lên tính sẵn sàng, nhưng sẽ đòi hỏi lưu lượng mạng lớn hơn để gia hạn thuê. Chúng tôi đang thiết kế và triển khai một cơ chế khiến các bản sao phụ giải phóng quyền thuê vai trò lãnh đạo Paxos khi nút lãnh đạo gặp sự cố.

### 5.2 Tính sẵn sàng {#corbett-2012-spanner-s5-2 .section tag=00B7}

### 5.3 TrueTime {#corbett-2012-spanner-s5-3 .section tag=00B8}

Cần trả lời hai câu hỏi về TrueTime: $\epsilon$ có thực sự là cận của độ bất định đồng hồ (clock uncertainty) không, và $\epsilon$ có thể lớn đến mức nào? Với câu hỏi thứ nhất, vấn đề nghiêm trọng nhất sẽ xảy ra nếu độ trôi của đồng hồ cục bộ lớn hơn 200us/sec: điều đó sẽ phá vỡ các giả định của TrueTime. Số liệu thống kê về máy của chúng tôi cho thấy khả năng CPU bị lỗi cao gấp 6 lần khả năng đồng hồ bị lỗi. Nghĩa là các vấn đề về đồng hồ cực kỳ hiếm gặp so với những vấn đề phần cứng nghiêm trọng hơn nhiều. Do đó, chúng tôi tin rằng bản triển khai TrueTime cũng đáng tin cậy như bất kỳ phần mềm nào khác mà Spanner phụ thuộc vào.

Hình 6 trình bày dữ liệu TrueTime được thu thập trên vài nghìn máy spanserver tại các trung tâm dữ liệu cách nhau tới 2200 km. Hình biểu diễn các phân vị thứ 90, 99 và 99.9 của $\epsilon$, được lấy mẫu tại các tiến trình nền timeslave ngay sau khi thăm dò các máy chủ thời gian. Cách lấy mẫu này loại bỏ dạng răng cưa của $\epsilon$ do độ bất định của đồng hồ cục bộ, và do đó đo độ bất định của máy chủ thời gian (thường bằng 0) cộng với độ trễ truyền thông tới các máy chủ thời gian.

Hình 6: Phân bố các giá trị $\epsilon$ của TrueTime, được lấy mẫu ngay sau khi tiến trình nền timeslave thăm dò các máy chủ thời gian. Các phân vị thứ 90, 99 và 99.9 được biểu diễn trên đồ thị. {#corbett-2012-spanner-fig-6 .figure tag=00B9}

Dữ liệu cho thấy hai yếu tố quyết định giá trị cơ sở của $\epsilon$ này nhìn chung không gây vấn đề. Tuy nhiên, có thể xuất hiện các vấn đề đáng kể về độ trễ đuôi (tail latency), khiến $\epsilon$ có giá trị cao hơn. Độ trễ đuôi giảm từ ngày 30 tháng 3 nhờ những cải tiến về mạng giúp giảm tắc nghẽn tạm thời trên các liên kết mạng. Sự gia tăng của $\epsilon$ vào ngày 13 tháng 4, kéo dài khoảng một giờ, là do 2 máy chủ thời gian tại một trung tâm dữ liệu bị tắt để bảo trì định kỳ. Chúng tôi tiếp tục tìm hiểu và loại bỏ các nguyên nhân gây ra những đợt tăng đột biến của TrueTime.

### 5.4 F1 {#corbett-2012-spanner-s5-4 .section tag=00BA}

Spanner bắt đầu được đánh giá thử nghiệm với tải công việc thực tế vào đầu năm 2011, trong khuôn khổ việc viết lại hệ thống backend quảng cáo của Google có tên F1 [35]. Backend này ban đầu dựa trên một cơ sở dữ liệu MySQL được phân mảnh (sharding) thủ công theo nhiều cách. Tập dữ liệu chưa nén có dung lượng hàng chục terabyte, nhỏ so với nhiều hệ thống NoSQL, nhưng đủ lớn để gây khó khăn cho MySQL phân mảnh. Phương án phân mảnh MySQL gán mỗi khách hàng và toàn bộ dữ liệu liên quan vào một mảnh cố định. Cách bố trí này cho phép sử dụng chỉ mục và xử lý truy vấn phức tạp theo từng khách hàng, nhưng đòi hỏi logic nghiệp vụ của ứng dụng phải có một số hiểu biết về cách phân mảnh. Việc phân mảnh lại cơ sở dữ liệu có vai trò thiết yếu đối với doanh thu này khi số lượng khách hàng và dữ liệu của họ tăng lên là cực kỳ tốn kém. Lần phân mảnh lại gần nhất đòi hỏi hơn hai năm nỗ lực tập trung, cùng sự phối hợp và kiểm thử giữa hàng chục nhóm để giảm thiểu rủi ro. Thao tác này quá phức tạp để thực hiện thường xuyên: do đó, nhóm phải hạn chế sự tăng trưởng của cơ sở dữ liệu MySQL bằng cách lưu một phần dữ liệu trong các Bigtable bên ngoài, làm ảnh hưởng đến hành vi giao dịch và khả năng truy vấn trên toàn bộ dữ liệu.

Nhóm F1 chọn sử dụng Spanner vì một số lý do. Thứ nhất, Spanner loại bỏ nhu cầu phân mảnh lại thủ công. Thứ hai, Spanner cung cấp sao chép đồng bộ và chuyển đổi dự phòng (failover) tự động. Với sao chép chủ-tớ của MySQL, chuyển đổi dự phòng rất khó khăn và có nguy cơ gây mất dữ liệu cũng như gián đoạn dịch vụ. Thứ ba, F1 đòi hỏi ngữ nghĩa giao dịch mạnh, khiến việc sử dụng các hệ thống NoSQL khác không khả thi. Ngữ nghĩa ứng dụng đòi hỏi các giao dịch trên dữ liệu tùy ý và các phép đọc nhất quán. Nhóm F1 cũng cần các chỉ mục thứ cấp trên dữ liệu của mình (vì Spanner chưa cung cấp hỗ trợ tự động cho chỉ mục thứ cấp), và đã có thể tự triển khai các chỉ mục toàn cục nhất quán bằng giao dịch Spanner.

Hiện nay, mọi thao tác ghi của ứng dụng mặc định đều được gửi qua F1 tới Spanner, thay cho ngăn xếp ứng dụng dựa trên MySQL. F1 có 2 bản sao ở bờ Tây Hoa Kỳ và 3 bản sao ở bờ Đông. Các địa điểm đặt bản sao này được chọn để ứng phó với tình trạng ngừng hoạt động do các thảm họa thiên nhiên lớn có thể xảy ra, đồng thời phù hợp với các địa điểm đặt frontend của họ. Theo trải nghiệm được chia sẻ, việc chuyển đổi dự phòng tự động của Spanner gần như không thể nhận thấy đối với họ. Mặc dù đã có các sự cố cụm ngoài kế hoạch trong vài tháng qua, điều nhiều nhất mà nhóm F1 phải làm là cập nhật lược đồ cơ sở dữ liệu để cho Spanner biết nơi ưu tiên đặt các nút lãnh đạo Paxos, nhằm giữ chúng gần nơi các frontend đã chuyển tới.

Ngữ nghĩa dấu thời gian của Spanner giúp F1 duy trì hiệu quả các cấu trúc dữ liệu trong bộ nhớ được tính toán từ trạng thái cơ sở dữ liệu. F1 duy trì một nhật ký lịch sử logic ghi lại mọi thay đổi, được ghi vào chính Spanner như một phần của mỗi giao dịch. F1 lấy các ảnh chụp đầy đủ của dữ liệu tại một dấu thời gian để khởi tạo các cấu trúc dữ liệu, rồi đọc các thay đổi gia tăng để cập nhật chúng.

Bảng 5 minh họa phân bố số lượng mảnh trên mỗi thư mục trong F1. Mỗi thư mục thường tương ứng với một khách hàng trong ngăn xếp ứng dụng phía trên F1. Phần lớn các thư mục (và do đó là khách hàng) chỉ gồm 1 mảnh, nghĩa là các thao tác đọc và ghi dữ liệu của những khách hàng đó được bảo đảm chỉ diễn ra trên một server duy nhất. Các thư mục có hơn 100 mảnh đều là những bảng chứa chỉ mục thứ cấp của F1: các thao tác ghi vào nhiều hơn một vài mảnh

| thao tác | độ trễ (ms) |  | số lượng |
| --- | --- | --- | --- |
|  | trung bình | độ lệch chuẩn |  |
| tất cả các phép đọc | 8.7 | 376.4 | 21.5B |
| xác nhận tại một địa điểm | 72.3 | 112.8 | 31.2M |
| xác nhận tại nhiều địa điểm | 103.0 | 52.2 | 32.1M |

Bảng 6: Độ trễ thao tác theo quan sát của F1, được đo trong khoảng thời gian 24 giờ. {#corbett-2012-spanner-tab-6 .table tag=00BB}

của những bảng như vậy là cực kỳ hiếm. Nhóm F1 chỉ thấy hành vi này khi thực hiện các đợt nạp dữ liệu hàng loạt chưa được tinh chỉnh dưới dạng giao dịch.

Bảng 6 trình bày độ trễ của các thao tác Spanner được đo từ các server F1. Các bản sao trong những trung tâm dữ liệu ở bờ đông được ưu tiên cao hơn khi chọn nút lãnh đạo Paxos (Paxos leader). Dữ liệu trong bảng được đo từ các server F1 tại những trung tâm dữ liệu đó. Độ lệch chuẩn lớn của độ trễ ghi bắt nguồn từ phần đuôi khá dày của phân phối do xung đột khóa. Độ lệch chuẩn của độ trễ đọc còn lớn hơn, một phần là do các nút lãnh đạo Paxos được phân bố trên hai trung tâm dữ liệu, trong đó chỉ một trung tâm có các máy được trang bị SSD. Ngoài ra, phép đo bao gồm mọi thao tác đọc trong hệ thống từ hai trung tâm dữ liệu: giá trị trung bình và độ lệch chuẩn của số byte được đọc lần lượt xấp xỉ 1.6KB và 119KB.
