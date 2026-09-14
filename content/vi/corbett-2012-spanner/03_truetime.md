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
section: "3"
section_title: TrueTime
tag: 00A5
kind: section
lang: vi
source: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.258.9924
pdf_sha256: 61875779e75f603d21aefba6d9bd9816d4dd0c18cf41089f43707249e24bbf88
pdf_pages: 5-6
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 6eb6c7646b3494add45f9a844adf5394cdc09edf6b353392711144e59c0ed32f
translated_from: content/en/corbett-2012-spanner/03_truetime.md
source_content_sha256: d2bb5ab6879c6762ffa848154e4205b016ec973179bcf36dd834ca729015c0c5
translation_model: gpt-5
translation_run: 20260914T201546Z
glossary_version: 6
glossary_terms_sha256: a534ae50d60bff0e03804fd3c150e37d1876484531ab87df9c72dc4d0c455eb2
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

| Phương thức | Trả về |
| --- | --- |
| *TT.now()* | *TTinterval:* [earliest, latest] |
| *TT.after(t)* | true nếu $t$ chắc chắn đã trôi qua |
| *TT.before(t)* | true nếu $t$ chắc chắn chưa đến |

Bảng 1: API TrueTime. Đối số $t$ có kiểu $TTstamp$. {#corbett-2012-spanner-tab-1 .table tag=00A6}

Phần này mô tả API TrueTime và phác thảo việc triển khai của nó. Chúng tôi để lại hầu hết các chi tiết cho một bài báo khác: mục tiêu của chúng tôi là minh họa sức mạnh của việc có một API như vậy. Bảng 1 liệt kê các phương thức của API. TrueTime biểu diễn thời gian một cách tường minh dưới dạng $TTinterval$, là một khoảng với độ bất định thời gian bị chặn (khác với các giao diện thời gian tiêu chuẩn không cung cấp cho máy khách khái niệm nào về sự bất định). Các điểm đầu mút của một $TTinterval$ có kiểu $TTstamp$. Phương thức $TT.now()$ trả về một $TTinterval$ được đảm bảo chứa thời gian tuyệt đối trong khoảng thời gian mà $TT.now()$ được gọi. Kỷ nguyên thời gian tương tự như thời gian UNIX với việc làm mờ giây nhuận. Định nghĩa cận lỗi tức thời là $\epsilon$, bằng một nửa độ rộng của khoảng, và cận lỗi trung bình là $\bar{\epsilon}$. Các phương thức $TT.after()$ và $TT.before()$ là các lớp bao tiện ích xung quanh $TT.now()$.

Ký hiệu thời gian tuyệt đối của một sự kiện $e$ bằng hàm $t_{abs}(e)$. Theo cách hình thức hơn, TrueTime đảm bảo rằng với một lần gọi $tt = TT.now(), tt.earliest \leq t_{abs}(e_{now}) \leq tt.latest$, trong đó $e_{now}$ là sự kiện gọi.

Các tham chiếu thời gian nền tảng được TrueTime sử dụng là GPS và đồng hồ nguyên tử. TrueTime sử dụng hai dạng tham chiếu thời gian vì chúng có các chế độ sự cố khác nhau. Các lỗ hổng của nguồn tham chiếu GPS bao gồm sự cố ăng-ten và bộ thu, nhiễu vô tuyến cục bộ, các sự cố tương quan (ví dụ, các lỗi thiết kế như xử lý giây nhuận không đúng và giả mạo), và các sự cố ngừng hoạt động của hệ thống GPS. Đồng hồ nguyên tử có thể gặp sự cố theo các cách không tương quan với GPS và với nhau, và trong các khoảng thời gian dài có thể bị trôi đáng kể do lỗi tần số.

TrueTime được triển khai bởi một tập hợp các máy *time master* trên mỗi trung tâm dữ liệu và một *timeslave daemon* trên mỗi máy. Phần lớn các master có bộ thu GPS với ăng-ten chuyên dụng; các master này được tách biệt về mặt vật lý để giảm ảnh hưởng của sự cố ăng-ten, nhiễu vô tuyến và giả mạo. Các master còn lại (mà chúng tôi gọi là *Armageddon masters*) được trang bị đồng hồ nguyên tử. Một đồng hồ nguyên tử không quá đắt: chi phí của một Armageddon master cùng bậc với chi phí của một GPS master. Các tham chiếu thời gian của tất cả master thường xuyên được so sánh với nhau. Mỗi master cũng kiểm tra chéo tốc độ mà tham chiếu của nó tiến triển thời gian so với đồng hồ cục bộ của chính nó, và tự loại bỏ nếu có sai khác đáng kể. Giữa các lần đồng bộ hóa, các Armageddon master công bố độ bất định thời gian tăng chậm được suy ra từ độ trôi đồng hồ trong trường hợp xấu nhất được áp dụng một cách thận trọng. Các GPS master công bố độ bất định thường gần bằng không.

Mỗi daemon thăm dò nhiều master khác nhau [29] để giảm khả năng bị tổn thương trước lỗi từ bất kỳ master đơn lẻ nào. Một số là các GPS master được chọn từ các trung tâm dữ liệu lân cận; phần còn lại là các GPS master từ các trung tâm dữ liệu xa hơn, cũng như một số Armageddon master. Các daemon áp dụng một biến thể của thuật toán Marzullo [27] để phát hiện và loại bỏ các bên nói dối, đồng thời đồng bộ hóa đồng hồ máy cục bộ với các bên không nói dối. Để bảo vệ trước các đồng hồ cục bộ bị hỏng, các máy thể hiện sai lệch tần số lớn hơn cận trường hợp xấu nhất được suy ra từ đặc tả thành phần và môi trường vận hành sẽ bị loại bỏ.

Giữa các lần đồng bộ hóa, một daemon công bố độ bất định thời gian tăng chậm. $\epsilon$ được suy ra từ độ trôi đồng hồ cục bộ trong trường hợp xấu nhất được áp dụng một cách thận trọng. $\epsilon$ cũng phụ thuộc vào độ bất định của time-master và độ trễ giao tiếp tới các time master. Trong môi trường sản xuất của chúng tôi, $\epsilon$ thường là một hàm răng cưa theo thời gian, thay đổi từ khoảng 1 đến 7 ms trong mỗi khoảng thăm dò. Do đó $\bar{\epsilon}$ là 4 ms trong phần lớn thời gian. Khoảng thăm dò của daemon hiện là 30 giây, và tốc độ trôi được áp dụng hiện tại được đặt ở mức 200 microseconds/second, cùng nhau chiếm

| Thao tác | Thảo luận về dấu thời gian | Điều khiển đồng thời | Bản sao bắt buộc |
| --- | --- | --- | --- |
| Read-Write Transaction | § 4.1.2 | bi quan | leader |
| Read-Only Transaction | § 4.1.4 | không khóa | leader cho dấu thời gian; bất kỳ cho đọc, tuân theo § 4.1.3 |
| Snapshot Read, client-provided timestamp | — | không khóa | bất kỳ, tuân theo § 4.1.3 |
| Snapshot Read, client-provided bound | § 4.1.3 | không khóa | bất kỳ, tuân theo § 4.1.3 |

Bảng 2: Các kiểu đọc và ghi trong Spanner, và cách chúng được so sánh. {#corbett-2012-spanner-tab-2 .table tag=00A7}

cho các cận răng cưa từ 0 đến 6 ms. 1 ms còn lại đến từ độ trễ giao tiếp tới các time master. Các sai lệch khỏi dạng răng cưa này có thể xảy ra khi có sự cố. Ví dụ, tình trạng không khả dụng thỉnh thoảng của time-master có thể gây ra sự gia tăng $\epsilon$ trên toàn trung tâm dữ liệu. Tương tự, các máy và liên kết mạng bị quá tải có thể dẫn đến các đỉnh $\epsilon$ cục bộ xảy ra không thường xuyên.
