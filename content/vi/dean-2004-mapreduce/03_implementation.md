---
paper: dean-2004-mapreduce
title: 'MapReduce: Simplified Data Processing on Large Clusters'
authors:
  - Jeffrey Dean
  - Sanjay Ghemawat
year: 2004
venue: OSDI
field: systems
section: "3"
section_title: Cài đặt
tag: "0071"
kind: section
lang: vi
source: https://www.usenix.org/legacy/events/osdi04/tech/full_papers/dean/dean.pdf
pdf_sha256: 9cfef3ef1b8fe1a1b66c7221f56c2eeca0b15d6608ea68b0c85a38bfbffd8ce5
pdf_pages: 3-6
extraction: vision
extraction_model: gpt-5
content_sha256: 17c3efdd3592c716f2d5b076adbd800d4e3ab9e473896a47e99d3bc53ce3ff2c
translated_from: content/en/dean-2004-mapreduce/03_implementation.md
source_content_sha256: 0d48c976d3c509f3fc40cd3481146b310c03c626b926b01101dda70eedbdc44a
translation_model: gpt-5
translation_run: 20260914T163737Z
glossary_version: 6
glossary_terms_sha256: afc6de5d010821f75553a129f8b55d5fbabc0d9d7af198021ca9a5a496de4088
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Có thể có nhiều cách cài đặt khác nhau cho giao diện MapReduce. Lựa chọn phù hợp phụ thuộc vào môi trường. Ví dụ, một cài đặt có thể phù hợp với một máy nhỏ có bộ nhớ chia sẻ, một cài đặt khác cho một máy đa bộ xử lý NUMA lớn, và một cài đặt khác nữa cho một tập hợp các máy được kết nối mạng thậm chí còn lớn hơn.

Phần này mô tả một cài đặt hướng tới môi trường tính toán được sử dụng rộng rãi tại Google: các cụm lớn gồm các PC phổ thông được kết nối với nhau bằng Ethernet chuyển mạch [4]. Trong môi trường của chúng tôi:

(1) Các máy thường là các bộ xử lý x86 hai bộ xử lý chạy Linux, với 2-4 GB bộ nhớ trên mỗi máy.

(2) Phần cứng mạng phổ thông được sử dụng – thường là 100 megabits/second hoặc 1 gigabit/second ở mức máy, nhưng trung bình thấp hơn đáng kể xét về băng thông chia đôi tổng thể.

(3) Một cluster bao gồm hàng trăm hoặc hàng nghìn máy, và do đó sự cố máy xảy ra thường xuyên.

(4) Lưu trữ được cung cấp bởi các ổ đĩa IDE giá rẻ được gắn trực tiếp vào từng máy riêng lẻ. Một hệ thống file phân tán [[ghemawat-2003-gfs]] được phát triển nội bộ được sử dụng để quản lý dữ liệu được lưu trữ trên các ổ đĩa này. Hệ thống file sử dụng sao chép để cung cấp tính sẵn sàng và độ tin cậy trên phần cứng không đáng tin cậy.

(5) Người dùng gửi các job đến một hệ thống lập lịch. Mỗi job bao gồm một tập hợp các tác vụ, và được bộ lập lịch ánh xạ tới một tập hợp các máy khả dụng trong một cluster.

### 3.1 Tổng quan về thực thi {#dean-2004-mapreduce-s3-1 .section tag=0072}

Các lời gọi Map được phân tán trên nhiều máy bằng cách tự động phân vùng dữ liệu đầu vào thành một tập hợp gồm $M$ phần chia. Các phần chia đầu vào có thể được xử lý song song bởi các máy khác nhau. Các lời gọi Reduce được phân tán bằng cách phân vùng không gian khóa trung gian thành $R$ phần bằng cách sử dụng một hàm phân vùng (ví dụ, hash(key) mod $R$). Số lượng phân vùng ($R$) và hàm phân vùng được người dùng chỉ định.

Figure 1 cho thấy luồng tổng thể của một thao tác MapReduce trong cài đặt của chúng tôi. Khi chương trình người dùng gọi hàm MapReduce, chuỗi hành động sau đây xảy ra (các nhãn được đánh số trong Figure 1 tương ứng với các số trong danh sách dưới đây):

1. Thư viện MapReduce trong chương trình người dùng trước tiên chia các file đầu vào thành $M$ phần, thường có kích thước từ 16 megabytes đến 64 megabytes (MB) cho mỗi phần (có thể được người dùng điều khiển thông qua một tham số tùy chọn). Sau đó nó khởi động nhiều bản sao của chương trình trên một cluster các máy.

1. Một trong các bản sao của chương trình là đặc biệt – master. Các bản sao còn lại là các worker được master gán công việc. Có $M$ tác vụ map và $R$ tác vụ reduce cần được gán. Master chọn các worker đang rảnh và gán cho mỗi worker một tác vụ map hoặc một tác vụ reduce.

1. Một worker được gán một tác vụ map đọc nội dung của phần chia đầu vào tương ứng. Nó phân tích cú pháp các cặp khóa/giá trị từ dữ liệu đầu vào và truyền từng cặp cho hàm Map do người dùng định nghĩa. Các cặp khóa/giá trị trung gian được tạo bởi hàm Map được lưu trong bộ đệm trong bộ nhớ.

1. Định kỳ, các cặp được lưu trong bộ đệm được ghi vào đĩa cục bộ, được phân vùng thành $R$ vùng bởi hàm phân vùng. Vị trí của các cặp được lưu trong bộ đệm này trên đĩa cục bộ được truyền trở lại master, bộ phận chịu trách nhiệm chuyển tiếp các vị trí này tới các worker reduce.

1. Khi một worker reduce được master thông báo về các vị trí này, nó sử dụng các lời gọi thủ tục từ xa để đọc dữ liệu được lưu trong bộ đệm từ các đĩa cục bộ của các worker map. Khi một worker reduce đã đọc toàn bộ dữ liệu trung gian, nó sắp xếp dữ liệu theo các khóa trung gian sao cho mọi lần xuất hiện của cùng một khóa được nhóm lại với nhau. Việc sắp xếp là cần thiết vì thông thường nhiều khóa khác nhau được ánh xạ tới cùng một tác vụ reduce. Nếu lượng dữ liệu trung gian quá lớn để vừa trong bộ nhớ, một phép sắp xếp ngoài được sử dụng.

1. Worker reduce duyệt qua dữ liệu trung gian đã sắp xếp và với mỗi khóa trung gian duy nhất gặp được, nó truyền khóa đó cùng với tập các giá trị trung gian tương ứng tới hàm Reduce của người dùng. Đầu ra của hàm Reduce được nối thêm vào một file đầu ra cuối cùng cho phân vùng reduce này.

1. Khi tất cả các tác vụ map và tác vụ reduce đã hoàn thành, master đánh thức chương trình người dùng. Tại thời điểm này, lời gọi MapReduce trong chương trình người dùng trả quyền điều khiển trở lại mã của người dùng.

Sau khi hoàn thành thành công, đầu ra của thực thi mapreduce có sẵn trong các file đầu ra $R$ (mỗi file cho một tác vụ reduce, với tên file do người dùng chỉ định). Thông thường, người dùng không cần kết hợp các file đầu ra $R$ này thành một file – họ thường truyền các file này làm đầu vào cho một lời gọi MapReduce khác, hoặc sử dụng chúng từ một ứng dụng phân tán khác có khả năng xử lý đầu vào được phân vùng thành nhiều file.

### 3.2 Cấu trúc dữ liệu của Master {#dean-2004-mapreduce-s3-2 .section tag=0121}

Master duy trì một số cấu trúc dữ liệu. Đối với mỗi tác vụ map và tác vụ reduce, nó lưu trữ trạng thái (idle, in-progress, hoặc completed), và định danh của máy worker (đối với các tác vụ không ở trạng thái idle).

Master là kênh thông qua đó vị trí của các vùng file trung gian được truyền từ các tác vụ map tới các tác vụ reduce. Vì vậy, đối với mỗi tác vụ map đã hoàn thành, master lưu trữ vị trí và kích thước của $R$ vùng file trung gian được tạo ra bởi tác vụ map đó. Các cập nhật về thông tin vị trí và kích thước này được nhận khi các tác vụ map hoàn thành. Thông tin được đẩy tăng dần tới các worker đang có các tác vụ reduce đang tiến hành.

### 3.3 Khả năng chịu lỗi {#dean-2004-mapreduce-s3-3 .section tag=0122}

Vì thư viện MapReduce được thiết kế để giúp xử lý lượng dữ liệu rất lớn bằng cách sử dụng hàng trăm hoặc hàng nghìn máy, thư viện phải có khả năng chịu các sự cố máy một cách linh hoạt.

Lỗi của Worker

Bộ master ping tới mọi worker theo định kỳ. Nếu không nhận được phản hồi từ một worker trong một khoảng thời gian nhất định, master đánh dấu worker đó là đã gặp sự cố. Bất kỳ tác vụ map nào được worker hoàn thành đều được đặt lại về trạng thái nhàn rỗi ban đầu, và do đó trở nên đủ điều kiện để được lập lịch trên các worker khác. Tương tự, bất kỳ tác vụ map hoặc reduce nào đang thực thi trên một worker đã gặp sự cố cũng được đặt lại về trạng thái nhàn rỗi và trở nên đủ điều kiện để được lập lịch lại.

Các tác vụ map đã hoàn thành được thực thi lại khi xảy ra sự cố vì đầu ra của chúng được lưu trên các đĩa cục bộ của máy đã gặp sự cố và do đó không thể truy cập được. Các tác vụ reduce đã hoàn thành không cần được thực thi lại vì đầu ra của chúng được lưu trong một hệ thống file toàn cục.

Khi một tác vụ map được thực thi lần đầu bởi worker $A$ và sau đó được thực thi lại bởi worker $B$ (vì $A$ đã gặp sự cố), tất cả worker đang thực thi các tác vụ reduce được thông báo về việc thực thi lại. Bất kỳ tác vụ reduce nào chưa đọc dữ liệu từ worker A sẽ đọc dữ liệu từ worker B.

MapReduce có khả năng chống chịu với các sự cố worker ở quy mô lớn. Ví dụ, trong một phép tính MapReduce, việc bảo trì mạng trên một cluster đang chạy đã khiến các nhóm gồm 80 máy mỗi lần không thể truy cập được trong vài phút. Master MapReduce chỉ đơn giản thực thi lại công việc do các máy worker không thể truy cập thực hiện, và tiếp tục tiến triển, cuối cùng hoàn thành phép tính MapReduce.

Sự cố master

Dễ dàng khiến master ghi các điểm kiểm tra định kỳ của các cấu trúc dữ liệu master được mô tả ở trên. Nếu tác vụ master bị dừng, một bản sao mới có thể được khởi động từ trạng thái được lưu tại điểm kiểm tra gần nhất. Tuy nhiên, do chỉ có một master duy nhất, khả năng xảy ra sự cố của nó là thấp; vì vậy triển khai hiện tại của chúng tôi hủy bỏ phép tính MapReduce nếu master gặp sự cố. Các máy khách có thể kiểm tra điều kiện này và thử lại phép tính MapReduce nếu muốn.

Ngữ nghĩa khi có sự cố

Khi các toán tử map và reduce do người dùng cung cấp là các hàm tất định của các giá trị đầu vào, triển khai phân tán của chúng tôi tạo ra cùng một đầu ra như đầu ra được tạo ra bởi một thực thi tuần tự không có lỗi của toàn bộ chương trình.

Chúng tôi dựa vào các lần commit nguyên tử của đầu ra của các tác vụ map và reduce để đạt được tính chất này. Mỗi tác vụ đang thực thi ghi đầu ra của nó vào các file tạm riêng tư. Một tác vụ reduce tạo ra một file như vậy, còn một tác vụ map tạo ra $R$ file như vậy (mỗi file tương ứng với một tác vụ reduce). Khi một tác vụ map hoàn thành, worker gửi một thông báo tới master và bao gồm tên của $R$ file tạm trong thông báo. Nếu master nhận được thông báo hoàn thành cho một tác vụ map đã hoàn thành trước đó, nó bỏ qua thông báo này. Ngược lại, nó ghi lại tên của $R$ file trong một cấu trúc dữ liệu master.

Khi một tác vụ reduce hoàn thành, worker reduce đổi tên nguyên tử file đầu ra tạm thời của nó thành file đầu ra cuối cùng. Nếu cùng một tác vụ reduce được thực thi trên nhiều máy, nhiều lời gọi đổi tên sẽ được thực hiện cho cùng một file đầu ra cuối cùng. Chúng tôi dựa vào thao tác đổi tên nguyên tử do hệ thống file bên dưới cung cấp để đảm bảo rằng trạng thái hệ thống file cuối cùng chỉ chứa dữ liệu được tạo ra bởi một lần thực thi của tác vụ reduce.

Phần lớn các toán tử map và reduce của chúng tôi là tất định, và việc ngữ nghĩa của chúng tôi tương đương với một thực thi tuần tự trong trường hợp này khiến các lập trình viên rất dễ suy luận về hành vi của chương trình của họ. Khi các toán tử map và/hoặc reduce là không tất định, chúng tôi cung cấp ngữ nghĩa yếu hơn nhưng vẫn hợp lý. Với các toán tử không tất định, đầu ra của một tác vụ reduce cụ thể $R_1$ tương đương với đầu ra cho $R_1$ được tạo ra bởi một thực thi tuần tự của chương trình không tất định. Tuy nhiên, đầu ra của một tác vụ reduce khác $R_2$ có thể tương ứng với đầu ra cho $R_2$ được tạo ra bởi một thực thi tuần tự khác của chương trình không tất định.

Xét tác vụ map $M$ và các tác vụ reduce $R_1$ và $R_2$. Gọi $e(R_i)$ là thực thi của $R_i$ đã được commit (có đúng một thực thi như vậy). Ngữ nghĩa yếu hơn xuất hiện vì $e(R_1)$ có thể đã đọc đầu ra được tạo bởi một lần thực thi của $M$ và $e(R_2)$ có thể đã đọc đầu ra được tạo bởi một lần thực thi khác của $M$.

### 3.4 Tính cục bộ {#dean-2004-mapreduce-s3-4 .section tag=0109}

Băng thông mạng là một tài nguyên tương đối khan hiếm trong môi trường tính toán của chúng tôi. Chúng tôi tiết kiệm băng thông mạng bằng cách tận dụng thực tế rằng dữ liệu đầu vào (được quản lý bởi GFS [[ghemawat-2003-gfs]]) được lưu trên các đĩa cục bộ của các máy tạo nên cluster của chúng tôi. GFS chia mỗi file thành các khối 64 MB, và lưu nhiều bản sao của mỗi khối (thông thường 3 bản sao) trên các máy khác nhau. Master MapReduce xem xét thông tin vị trí của các file đầu vào và cố gắng lập lịch một tác vụ map trên một máy chứa bản sao của dữ liệu đầu vào tương ứng. Nếu không thành công, nó cố gắng lập lịch một tác vụ map gần một bản sao của dữ liệu đầu vào của tác vụ đó (ví dụ, trên một máy worker nằm trên cùng bộ chuyển mạch mạng với máy chứa dữ liệu). Khi chạy các phép toán MapReduce lớn trên một phần đáng kể các worker trong một cluster, phần lớn dữ liệu đầu vào được đọc cục bộ và không tiêu tốn băng thông mạng.

### 3.5 Độ hạt của tác vụ {#dean-2004-mapreduce-s3-5 .section tag=010A}

Chúng tôi chia nhỏ giai đoạn map thành $M$ phần và giai đoạn reduce thành $R$ phần, như đã mô tả ở trên. Lý tưởng nhất, $M$ và $R$ nên lớn hơn nhiều so với số lượng máy worker. Việc để mỗi worker thực hiện nhiều tác vụ khác nhau cải thiện cân bằng tải động, đồng thời cũng tăng tốc quá trình khôi phục khi một worker gặp sự cố: nhiều tác vụ map mà nó đã hoàn thành có thể được phân tán trên tất cả các máy worker khác.

Có các cận thực tế về độ lớn của $M$ và $R$ trong triển khai của chúng tôi, vì master phải đưa ra $O(M + R)$ quyết định lập lịch và duy trì $O(M * R)$ trạng thái trong bộ nhớ như đã mô tả ở trên. (Tuy nhiên, các hệ số hằng của việc sử dụng bộ nhớ là nhỏ: phần $O(M * R)$ của trạng thái bao gồm xấp xỉ một byte dữ liệu cho mỗi cặp tác vụ map/tác vụ reduce.)

Hơn nữa, $R$ thường bị người dùng giới hạn vì đầu ra của mỗi tác vụ reduce cuối cùng được ghi vào một file đầu ra riêng biệt. Trong thực tế, chúng tôi có xu hướng chọn $M$ sao cho mỗi tác vụ riêng lẻ có khoảng 16 MB đến 64 MB dữ liệu đầu vào (để tối ưu hóa locality được mô tả ở trên đạt hiệu quả cao nhất), và chúng tôi đặt $R$ là một bội số nhỏ của số máy worker mà chúng tôi dự kiến sử dụng. Chúng tôi thường thực hiện các tính toán MapReduce với $M = 200,000$ và $R = 5,000$, sử dụng 2,000 máy worker.

### 3.6 Các tác vụ dự phòng {#dean-2004-mapreduce-s3-6 .section tag=010B}

Một trong những nguyên nhân phổ biến làm kéo dài tổng thời gian thực hiện một thao tác MapReduce là một “straggler”: một máy mất thời gian dài bất thường để hoàn thành một trong vài tác vụ map hoặc reduce cuối cùng trong phép tính. Straggler có thể phát sinh do rất nhiều nguyên nhân. Ví dụ, một máy có ổ đĩa bị lỗi có thể gặp các lỗi có thể sửa chữa thường xuyên làm giảm hiệu năng đọc của nó từ 30 MB/s xuống 1 MB/s. Hệ thống lập lịch cụm có thể đã lập lịch các tác vụ khác trên máy đó, khiến nó thực thi mã MapReduce chậm hơn do cạnh tranh về CPU, bộ nhớ, ổ đĩa cục bộ hoặc băng thông mạng. Một vấn đề gần đây mà chúng tôi gặp phải là một lỗi trong mã khởi tạo máy khiến các cache của bộ xử lý bị vô hiệu hóa: các phép tính trên những máy bị ảnh hưởng chậm hơn hơn một trăm lần.

Chúng tôi có một cơ chế tổng quát để giảm nhẹ vấn đề của các straggler. Khi một thao tác MapReduce gần hoàn thành, master lập lịch các thực thi dự phòng của các tác vụ còn đang tiến hành. Tác vụ được đánh dấu là đã hoàn thành bất cứ khi nào thực thi chính hoặc thực thi dự phòng hoàn thành. Chúng tôi đã tinh chỉnh cơ chế này để nó thường làm tăng các tài nguyên tính toán được sử dụng bởi thao tác không quá vài phần trăm. Chúng tôi nhận thấy rằng cơ chế này làm giảm đáng kể thời gian hoàn thành các thao tác MapReduce lớn. Ví dụ, chương trình sort được mô tả trong Section 5.3 mất nhiều hơn 44% thời gian để hoàn thành khi cơ chế tác vụ dự phòng bị vô hiệu hóa.
