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
content_sha256: df1b1e8b7c6cb18bde2008add0d0e5b64967209a6a2e3c5281ed9cf7f69377d3
translated_from: content/en/corbett-2012-spanner/05_evaluation.md
source_content_sha256: c9c10f1c76c4c385602bfd1a438bf03cb71243d3ac151292d10068ebd24133fa
translation_model: gpt-5
translation_run: 20260918T153717Z
glossary_version: 7
glossary_terms_sha256: 8d6365491a62bf683f227b4ec25e6ea4a6b206a0b00009512875972be95a0002
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Trước tiên, chúng tôi đo hiệu năng của Spanner đối với sao chép, giao dịch và tính sẵn sàng. Sau đó, chúng tôi cung cấp một số dữ liệu về hành vi của TrueTime và một nghiên cứu tình huống về máy khách đầu tiên của chúng tôi, F1.

### 5.1 Các phép đo chuẩn vi mô {#corbett-2012-spanner-s5-1 .section tag=00B5}

Bảng 3 trình bày một số phép đo chuẩn vi mô cho Spanner. Các phép đo này được thực hiện trên các máy chia sẻ thời gian: mỗi spanserver chạy trên các đơn vị lập lịch gồm 4GB RAM và 4 lõi (AMD Barcelona 2200MHz). Các máy khách được chạy trên các máy riêng biệt. Mỗi zone chứa một spanserver. Các máy khách và zone được đặt trong một tập hợp các trung tâm dữ liệu có khoảng cách mạng nhỏ hơn 1ms. (Một bố cục như vậy nên là phổ biến: hầu hết ứng dụng không cần phân phối toàn bộ dữ liệu của chúng trên toàn thế giới.) Cơ sở dữ liệu kiểm thử được tạo với 50 nhóm Paxos cùng với 2500 thư mục. Các thao tác là các lần đọc và ghi độc lập với kích thước 4KB. Tất cả các lần đọc được phục vụ từ bộ nhớ sau một lần compaction, do đó chúng tôi chỉ đo chi phí phụ trội của call stack của Spanner. Ngoài ra, một vòng đọc không được đo lường được thực hiện trước tiên để làm nóng mọi cache vị trí.

Đối với các thí nghiệm về độ trễ, các máy khách phát hành đủ ít thao tác để tránh xếp hàng tại các server. Từ các thí nghiệm 1-replica, thời gian chờ xác nhận là khoảng 5ms, và độ trễ Paxos là khoảng 9ms. Khi số lượng replica tăng lên, độ trễ giữ gần như không đổi với độ lệch chuẩn nhỏ hơn vì Paxos thực thi song song tại các replica của một nhóm. Khi số lượng replica tăng lên, độ trễ để đạt được quorum trở nên ít nhạy cảm hơn với sự chậm chạp tại một replica slave.

Đối với các thí nghiệm về thông lượng, các máy khách phát hành đủ nhiều thao tác để bão hòa các CPU của server.

| participants | latency (ms) |  |
| --- | --- | --- |
|  | mean | 99th percentile |
| 1 | 17.0 ±1.4 | 75.0 ±34.9 |
| 2 | 24.5 ±2.5 | 87.6 ±35.9 |
| 5 | 31.5 ±6.2 | 104.5 ±52.2 |
| 10 | 30.0 ±3.7 | 95.6 ±25.4 |
| 25 | 35.5 ±5.6 | 100.4 ±42.7 |
| 50 | 42.7 ±4.1 | 93.7 ±22.9 |
| 100 | 71.4 ±7.6 | 131.2 ±17.6 |
| 200 | 150.5 ±11.0 | 320.3 ±35.1 |

Bảng 4: Khả năng mở rộng của xác nhận hai pha. Trung bình và độ lệch chuẩn trên 10 lần chạy. {#corbett-2012-spanner-tab-4 .table tag=00B6}

Các lần đọc snapshot có thể thực thi tại bất kỳ replica nào được cập nhật mới nhất, vì vậy thông lượng của chúng tăng gần tuyến tính với số lượng replica. Các giao dịch chỉ đọc một lần đọc chỉ thực thi tại các leader vì việc gán dấu thời gian phải xảy ra tại các leader. Thông lượng của giao dịch chỉ đọc tăng theo số lượng replica vì số lượng spanserver hiệu dụng tăng lên: trong thiết lập thí nghiệm, số lượng spanserver bằng số lượng replica, và các leader được phân phối ngẫu nhiên giữa các zone. Thông lượng ghi được hưởng lợi từ cùng một hiện tượng thực nghiệm (điều này giải thích sự tăng thông lượng từ 3 đến 5 replica), nhưng lợi ích đó bị lấn át bởi sự gia tăng tuyến tính về lượng công việc được thực hiện cho mỗi lần ghi khi số lượng replica tăng lên.

Bảng 4 cho thấy xác nhận hai pha có thể mở rộng đến một số lượng participant hợp lý: nó tóm tắt một tập hợp thí nghiệm được thực hiện trên 3 zone, mỗi zone có 25 spanserver. Việc mở rộng lên đến 50 participant là hợp lý cả về giá trị trung bình và phân vị 99, và độ trễ bắt đầu tăng đáng kể tại 100 participant.

Hình 5 minh họa các lợi ích về tính sẵn sàng của việc chạy Spanner trong nhiều trung tâm dữ liệu. Hình này cho thấy kết quả của ba thí nghiệm về thông lượng khi có sự cố trung tâm dữ liệu, tất cả được chồng lên cùng một thang thời gian. Không gian kiểm thử bao gồm 5 zone $Z_i$, mỗi zone có 25 spanserver. Cơ sở dữ liệu kiểm thử được phân mảnh thành 1250 nhóm Paxos, và 100 máy khách kiểm thử liên tục phát hành các lần đọc không snapshot với tốc độ tổng hợp 50K reads/second. Tất cả leader được đặt rõ ràng trong $Z_1$. Năm giây sau khi bắt đầu mỗi kiểm thử, tất cả server trong một zone bị tắt: *non-leader* tắt $Z_2$; *leader-hard* tắt $Z_1$; *leader-soft* tắt $Z_1$, nhưng nó gửi thông báo đến tất cả server rằng chúng nên chuyển giao quyền lãnh đạo trước tiên.

Việc tắt $Z_2$ không có ảnh hưởng đến thông lượng đọc. Việc tắt $Z_1$ trong khi cho các leader thời gian để chuyển giao quyền lãnh đạo sang một zone khác có ảnh hưởng nhỏ: sự sụt giảm thông lượng không nhìn thấy trong đồ thị, nhưng vào khoảng 3-4%. Mặt khác, việc tắt $Z_1$ mà không có cảnh báo gây ảnh hưởng nghiêm trọng: tốc độ hoàn thành giảm gần về 0. Tuy nhiên, khi các leader được bầu lại, thông lượng của hệ thống tăng lên xấp xỉ 100K reads/second do hai hiện tượng thực nghiệm: hệ thống có thêm công suất và các thao tác được xếp hàng trong khi leader không khả dụng. Do đó, thông lượng của hệ thống tăng lên trước khi lại ổn định ở tốc độ ổn định của nó.

Chúng tôi cũng có thể thấy ảnh hưởng của thực tế rằng các lease leader Paxos được đặt thành 10 giây. Khi chúng tôi tắt zone, thời điểm hết hạn lease leader cho các nhóm phải được phân phối đều trong 10 giây tiếp theo. Ngay sau khi mỗi lease từ một leader đã chết hết hạn, một leader mới được bầu. Khoảng 10 giây sau thời điểm tắt, tất cả các nhóm đều có leader và thông lượng đã được khôi phục. Thời gian lease ngắn hơn sẽ làm giảm ảnh hưởng của việc server chết đối với tính sẵn sàng, nhưng sẽ yêu cầu lượng lưu lượng mạng gia hạn lease lớn hơn. Chúng tôi đang trong quá trình thiết kế và triển khai một cơ chế sẽ khiến các slave giải phóng lease leader Paxos khi leader gặp sự cố.

### 5.2 Tính khả dụng {#corbett-2012-spanner-s5-2 .section tag=00B7}

### 5.3 TrueTime {#corbett-2012-spanner-s5-3 .section tag=00B8}

Có hai câu hỏi cần được trả lời liên quan đến TrueTime: liệu $\epsilon$ có thực sự là một cận của độ bất định đồng hồ hay không, và $\epsilon$ có thể trở nên tệ đến mức nào? Đối với câu hỏi đầu tiên, vấn đề nghiêm trọng nhất sẽ xảy ra nếu độ trôi của đồng hồ cục bộ lớn hơn 200us/sec: điều đó sẽ phá vỡ các giả định mà TrueTime đưa ra. Thống kê máy của chúng tôi cho thấy các CPU lỗi có khả năng xảy ra cao hơn 6 lần so với các đồng hồ lỗi. Nghĩa là, các vấn đề về đồng hồ cực kỳ hiếm gặp so với những vấn đề phần cứng nghiêm trọng hơn nhiều. Do đó, chúng tôi tin rằng triển khai của TrueTime đáng tin cậy như bất kỳ phần mềm nào khác mà Spanner phụ thuộc vào.

Hình 6 trình bày dữ liệu TrueTime được lấy từ vài nghìn máy spanserver trên các datacenter cách nhau tới 2200 km. Hình này biểu diễn các phân vị thứ 90, 99 và 99.9 của $\epsilon$, được lấy mẫu tại các timeslave daemon ngay sau khi thăm dò các time master. Việc lấy mẫu này loại bỏ dạng răng cưa trong $\epsilon$ do độ bất định của đồng hồ cục bộ, và vì vậy đo độ bất định của time-master (thường là 0) cộng với độ trễ truyền thông tới các time master.

Hình 6: Phân phối các giá trị $\epsilon$ của TrueTime, được lấy mẫu ngay sau khi timeslave daemon thăm dò các time master. Các phân vị thứ 90, 99 và 99.9 được biểu diễn trên đồ thị. {#corbett-2012-spanner-fig-6 .figure tag=00B9}

Dữ liệu cho thấy hai yếu tố này trong việc xác định giá trị cơ sở của $\epsilon$ nhìn chung không phải là vấn đề. Tuy nhiên, có thể có các vấn đề độ trễ đuôi đáng kể gây ra các giá trị $\epsilon$ cao hơn. Việc giảm độ trễ đuôi bắt đầu từ ngày 30 tháng 3 là do các cải tiến về mạng làm giảm tắc nghẽn tạm thời trên liên kết mạng. Sự gia tăng $\epsilon$ vào ngày 13 tháng 4, kéo dài khoảng một giờ, là do việc tắt 2 time master tại một datacenter để bảo trì định kỳ. Chúng tôi tiếp tục điều tra và loại bỏ các nguyên nhân gây ra các đột biến của TrueTime.

### 5.4 F1 {#corbett-2012-spanner-s5-4 .section tag=00BA}

Spanner bắt đầu được đánh giá thử nghiệm dưới các tải công việc sản xuất vào đầu năm 2011, như một phần của việc viết lại backend quảng cáo của Google có tên F1 [35]. Backend này ban đầu dựa trên một cơ sở dữ liệu MySQL được phân mảnh thủ công theo nhiều cách. Tập dữ liệu chưa nén có kích thước hàng chục terabyte, nhỏ so với nhiều phiên bản NoSQL, nhưng đủ lớn để gây khó khăn với MySQL đã phân mảnh. Cơ chế sharding của MySQL gán mỗi khách hàng và toàn bộ dữ liệu liên quan vào một shard cố định. Bố cục này cho phép sử dụng các chỉ mục và xử lý truy vấn phức tạp theo từng khách hàng, nhưng yêu cầu một số kiến thức về sharding trong logic nghiệp vụ của ứng dụng. Việc phân mảnh lại cơ sở dữ liệu quan trọng về doanh thu này khi số lượng khách hàng và dữ liệu của họ tăng lên có chi phí cực kỳ lớn. Lần phân mảnh lại cuối cùng mất hơn hai năm nỗ lực cao độ, và liên quan đến việc phối hợp và kiểm thử giữa hàng chục nhóm để giảm thiểu rủi ro. Thao tác này quá phức tạp để thực hiện thường xuyên: do đó, nhóm phải hạn chế sự tăng trưởng trên cơ sở dữ liệu MySQL bằng cách lưu trữ một số dữ liệu trong các Bigtables bên ngoài, điều này làm ảnh hưởng đến hành vi giao dịch và khả năng truy vấn trên toàn bộ dữ liệu.

Nhóm F1 chọn sử dụng Spanner vì một số lý do. Thứ nhất, Spanner loại bỏ nhu cầu phân mảnh lại thủ công. Thứ hai, Spanner cung cấp sao chép đồng bộ và chuyển đổi dự phòng tự động. Với sao chép master-slave của MySQL, chuyển đổi dự phòng rất khó khăn và có nguy cơ mất dữ liệu cũng như thời gian ngừng hoạt động. Thứ ba, F1 yêu cầu ngữ nghĩa giao dịch mạnh, khiến việc sử dụng các hệ thống NoSQL khác trở nên không thực tế. Ngữ nghĩa ứng dụng yêu cầu các giao dịch trên dữ liệu tùy ý và các lần đọc nhất quán. Nhóm F1 cũng cần các chỉ mục thứ cấp trên dữ liệu của họ (vì Spanner chưa cung cấp hỗ trợ tự động cho các chỉ mục thứ cấp), và có thể tự triển khai các chỉ mục toàn cục nhất quán bằng cách sử dụng các giao dịch Spanner.

Tất cả các ghi ứng dụng hiện được mặc định gửi qua F1 tới Spanner, thay vì ngăn xếp ứng dụng dựa trên MySQL. F1 có 2 bản sao ở bờ tây của Mỹ, và 3 bản sao ở bờ đông. Lựa chọn các site bản sao này được thực hiện để đối phó với các sự cố ngừng hoạt động do các thảm họa tự nhiên lớn có thể xảy ra, đồng thời cũng dựa trên lựa chọn các site frontend của họ. Theo quan sát không chính thức, chuyển đổi dự phòng tự động của Spanner gần như không thể nhận thấy đối với họ. Mặc dù đã có các sự cố cụm không được lên kế hoạch trong vài tháng gần đây, điều duy nhất mà nhóm F1 phải làm nhiều nhất là cập nhật lược đồ cơ sở dữ liệu của họ để cho Spanner biết nơi ưu tiên đặt các leader Paxos, nhằm giữ chúng gần nơi các frontend của họ đã di chuyển đến.

Ngữ nghĩa dấu thời gian của Spanner giúp F1 duy trì hiệu quả các cấu trúc dữ liệu trong bộ nhớ được tính toán từ trạng thái cơ sở dữ liệu. F1 duy trì một nhật ký lịch sử logic của tất cả thay đổi, được ghi vào chính Spanner như một phần của mỗi giao dịch. F1 lấy các snapshot đầy đủ của dữ liệu tại một dấu thời gian để khởi tạo các cấu trúc dữ liệu của mình, sau đó đọc các thay đổi gia tăng để cập nhật chúng.

Bảng 5 minh họa phân phối số lượng mảnh trên mỗi thư mục trong F1. Mỗi thư mục thường tương ứng với một khách hàng trong ngăn xếp ứng dụng phía trên F1. Phần lớn áp đảo các thư mục (và do đó là khách hàng) chỉ bao gồm 1 mảnh, điều này có nghĩa là các lần đọc và ghi dữ liệu của những khách hàng đó được đảm bảo chỉ xảy ra trên một server duy nhất. Các thư mục có hơn 100 mảnh đều là các bảng chứa các chỉ mục thứ cấp của F1: các lần ghi tới nhiều hơn một vài mảnh

| operation | latency (ms) |  | count |
| --- | --- | --- | --- |
|  | mean | std dev |  |
| all reads | 8.7 | 376.4 | 21.5B |
| single-site commit | 72.3 | 112.8 | 31.2M |
| multi-site commit | 103.0 | 52.2 | 32.1M |

Bảng 6: Độ trễ thao tác được F1 cảm nhận được đo trong khoảng thời gian 24 giờ. {#corbett-2012-spanner-tab-6 .table tag=00BB}

của các bảng như vậy cực kỳ hiếm gặp. Nhóm F1 chỉ quan sát thấy hành vi như vậy khi họ thực hiện các lần nạp dữ liệu hàng loạt chưa được tinh chỉnh dưới dạng các giao dịch.

Bảng 6 trình bày độ trễ của các thao tác Spanner được đo từ các server F1. Các bản sao trong các trung tâm dữ liệu ở bờ đông được ưu tiên cao hơn trong việc chọn các leader Paxos. Dữ liệu trong bảng được đo từ các server F1 trong các trung tâm dữ liệu đó. Độ lệch chuẩn lớn của độ trễ ghi là do phần đuôi khá lớn gây ra bởi các xung đột khóa. Độ lệch chuẩn thậm chí còn lớn hơn của độ trễ đọc một phần là do thực tế rằng các leader Paxos được phân bố trên hai trung tâm dữ liệu, chỉ một trong số đó có các máy với SSD. Ngoài ra, phép đo bao gồm mọi lần đọc trong hệ thống từ hai trung tâm dữ liệu: giá trị trung bình và độ lệch chuẩn của số byte được đọc lần lượt xấp xỉ là 1.6KB và 119KB.
