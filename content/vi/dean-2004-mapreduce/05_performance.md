---
paper: dean-2004-mapreduce
title: 'MapReduce: Simplified Data Processing on Large Clusters'
authors:
  - Jeffrey Dean
  - Sanjay Ghemawat
year: 2004
venue: OSDI
field: systems
section: "5"
section_title: Hiệu năng
tag: 007D
kind: section
lang: vi
source: https://www.usenix.org/legacy/events/osdi04/tech/full_papers/dean/dean.pdf
pdf_sha256: 9cfef3ef1b8fe1a1b66c7221f56c2eeca0b15d6608ea68b0c85a38bfbffd8ce5
pdf_pages: 8-10
extraction: vision
extraction_model: gpt-5
content_sha256: 935ae315ce621215d8a821a9a3a21b2dc56cc7652484ea8749fdb7a2a257fd32
translated_from: content/en/dean-2004-mapreduce/05_performance.md
source_content_sha256: 8cf6aa8c9061baed7ac0fdb241ab6e791739182324ca75e0a972dc12ffa02be8
translation_model: gpt-5
translation_run: 20260914T163737Z
glossary_version: 6
glossary_terms_sha256: afc6de5d010821f75553a129f8b55d5fbabc0d9d7af198021ca9a5a496de4088
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Trong phần này, chúng tôi đo hiệu năng của MapReduce trên hai phép tính chạy trên một cụm lớn gồm nhiều máy. Một phép tính tìm kiếm trong khoảng một terabyte dữ liệu để tìm một mẫu cụ thể. Phép tính còn lại sắp xếp khoảng một terabyte dữ liệu.

Hai chương trình này đại diện cho một tập con lớn các chương trình thực tế do người dùng MapReduce viết – một lớp chương trình xáo trộn dữ liệu từ một biểu diễn này sang một biểu diễn khác, và một lớp khác trích xuất một lượng nhỏ dữ liệu đáng quan tâm từ một tập dữ liệu lớn.

### 5.1 Cấu hình cụm {#dean-2004-mapreduce-s5-1 .section tag=007E}

Tất cả các chương trình được thực thi trên một cụm gồm khoảng 1800 máy. Mỗi máy có hai bộ xử lý Intel Xeon 2GHz với Hyper-Threading được bật, 4GB bộ nhớ, hai ổ đĩa IDE 160GB và một liên kết Ethernet gigabit. Các máy được bố trí trong một mạng chuyển mạch hình cây hai cấp với băng thông tổng hợp khoảng 100-200 Gbps khả dụng tại nút gốc. Tất cả các máy nằm trong cùng một cơ sở lưu trữ và do đó thời gian khứ hồi giữa bất kỳ cặp máy nào đều nhỏ hơn một mili giây.

Hình 2. Tốc độ truyền dữ liệu theo thời gian {#dean-2004-mapreduce-fig-2 .figure tag=007F}

Trong 4GB bộ nhớ, khoảng 1-1.5GB được dành riêng cho các tác vụ khác đang chạy trên cụm. Các chương trình được thực thi vào một buổi chiều cuối tuần, khi CPU, ổ đĩa và mạng phần lớn ở trạng thái nhàn rỗi.

### 5.2 Grep {#dean-2004-mapreduce-s5-2 .section tag=0080}

Chương trình grep quét qua $10^10$ bản ghi 100-byte, tìm kiếm một mẫu ba ký tự tương đối hiếm (mẫu xuất hiện trong 92,337 bản ghi). Đầu vào được chia thành các phần khoảng 64MB ($M = 15000$), và toàn bộ đầu ra được đặt trong một file ($R = 1$).

Hình 2 cho thấy tiến trình của phép tính theo thời gian. Trục Y biểu diễn tốc độ quét dữ liệu đầu vào. Tốc độ tăng dần khi có thêm máy được phân công cho phép tính MapReduce này, và đạt đỉnh trên 30 GB/s khi 1764 worker được phân công. Khi tác vụ map hoàn tất, tốc độ bắt đầu giảm và chạm mức 0 khoảng 80 giây sau khi phép tính bắt đầu. Toàn bộ phép tính mất khoảng 150 giây từ đầu đến cuối. Khoảng một phút trong số đó là chi phí phụ trội khởi động. Chi phí phụ trội này là do việc truyền chương trình đến tất cả các máy worker, cũng như các độ trễ khi tương tác với GFS để mở tập gồm 1000 file đầu vào và lấy thông tin cần thiết cho tối ưu hóa tính cục bộ.

### 5.3 Sort {#dean-2004-mapreduce-s5-3 .section tag=0081}

Chương trình sort sắp xếp $10^10$ bản ghi 100-byte (khoảng một terabyte dữ liệu). Chương trình này được mô hình hóa theo phép đo chuẩn TeraSort [10].

Chương trình sắp xếp gồm chưa đến 50 dòng mã của người dùng. Một hàm Map ba dòng trích xuất một khóa sắp xếp 10-byte từ một dòng văn bản và phát ra khóa cùng

(a) Thực thi bình thường

(b) Không có tác vụ dự phòng

(c) 200 tác vụ bị hủy dòng văn bản gốc dưới dạng cặp khóa/giá trị trung gian. Chúng tôi sử dụng hàm Identity tích hợp sẵn làm toán tử Reduce. Hàm này truyền cặp khóa/giá trị trung gian không thay đổi thành cặp khóa/giá trị đầu ra. Đầu ra đã sắp xếp cuối cùng được ghi vào một tập các file GFS được sao chép 2 chiều (tức là 2 terabyte được ghi làm đầu ra của chương trình).

Hình 3: Tốc độ truyền dữ liệu theo thời gian đối với các lần thực thi khác nhau của chương trình sort {#dean-2004-mapreduce-fig-3 .figure tag=0082}

Như trước đây, dữ liệu đầu vào được chia thành các phần 64MB ($M = 15000$). Chúng tôi phân vùng đầu ra đã sắp xếp thành 4000 file ($R = 4000$). Hàm phân vùng sử dụng các byte đầu tiên của khóa để phân tách nó vào một trong $R$ phần.

Hàm phân vùng của chúng tôi cho phép đo chuẩn này có kiến thức tích hợp về phân phối của các khóa. Trong một chương trình sắp xếp tổng quát, chúng tôi sẽ thêm một phép tính MapReduce tiền xử lý để thu thập một mẫu các khóa và sử dụng phân phối của các khóa được lấy mẫu để tính các điểm phân tách cho lượt sắp xếp cuối cùng.

Hình 3 (a) cho thấy tiến trình của một lần thực thi bình thường của chương trình sort. Đồ thị phía trên bên trái cho thấy tốc độ đọc đầu vào. Tốc độ đạt đỉnh khoảng 13 GB/s và giảm khá nhanh vì tất cả các tác vụ map hoàn tất trước khi 200 giây trôi qua. Lưu ý rằng tốc độ đầu vào thấp hơn so với grep. Điều này là do các tác vụ map của sort dành khoảng một nửa thời gian và băng thông I/O để ghi đầu ra trung gian vào các ổ đĩa cục bộ của chúng. Đầu ra trung gian tương ứng của grep có kích thước không đáng kể.

Đồ thị phía giữa bên trái cho thấy tốc độ dữ liệu được gửi qua mạng từ các tác vụ map đến các tác vụ reduce. Việc xáo trộn này bắt đầu ngay khi tác vụ map đầu tiên hoàn tất. Đỉnh đầu tiên trong đồ thị tương ứng với lô đầu tiên gồm khoảng 1700 tác vụ reduce (toàn bộ MapReduce được phân công cho khoảng 1700 máy, và mỗi máy thực thi nhiều nhất một tác vụ reduce tại một thời điểm). Khoảng 300 giây sau khi phép tính bắt đầu, một số tác vụ reduce thuộc lô đầu tiên này hoàn tất và chúng tôi bắt đầu xáo trộn dữ liệu cho các tác vụ reduce còn lại. Toàn bộ việc xáo trộn hoàn tất khoảng 600 giây sau khi phép tính bắt đầu.

Đồ thị phía dưới bên trái cho thấy tốc độ dữ liệu đã sắp xếp được các tác vụ reduce ghi vào các file đầu ra cuối cùng. Có một độ trễ giữa thời điểm kết thúc giai đoạn xáo trộn đầu tiên và thời điểm bắt đầu giai đoạn ghi vì các máy đang bận sắp xếp dữ liệu trung gian. Việc ghi tiếp tục với tốc độ khoảng 2-4 GB/s trong một thời gian. Toàn bộ việc ghi hoàn tất khoảng 850 giây sau khi phép tính bắt đầu. Bao gồm chi phí phụ trội khởi động, toàn bộ phép tính mất 891 giây. Kết quả này tương tự kết quả tốt nhất hiện được báo cáo là 1057 giây đối với phép đo chuẩn TeraSort [18].

Một vài điều cần lưu ý: tốc độ đầu vào cao hơn tốc độ shuffle và tốc độ đầu ra do tối ưu hóa tính cục bộ của chúng tôi – phần lớn dữ liệu được đọc từ đĩa cục bộ và bỏ qua mạng của chúng tôi vốn bị hạn chế tương đối về băng thông. Tốc độ shuffle cao hơn tốc độ đầu ra vì giai đoạn đầu ra ghi hai bản sao của dữ liệu đã sắp xếp (chúng tôi tạo hai bản sao của đầu ra vì lý do độ tin cậy và tính sẵn sàng). Chúng tôi ghi hai bản sao vì đó là cơ chế đảm bảo độ tin cậy và tính sẵn sàng do hệ thống file nền tảng cung cấp. Yêu cầu về băng thông mạng khi ghi dữ liệu sẽ giảm nếu hệ thống file nền tảng sử dụng mã hóa xóa [14] thay vì sao chép.

### 5.4 Ảnh hưởng của các tác vụ dự phòng {#dean-2004-mapreduce-s5-4 .section tag=0083}

Trong Hình 3 (b), chúng tôi trình bày một lần thực thi chương trình sort khi các tác vụ dự phòng bị vô hiệu hóa. Luồng thực thi tương tự như trong Hình 3 (a), ngoại trừ việc có một phần đuôi rất dài, trong đó hầu như không có hoạt động ghi nào xảy ra. Sau 960 giây, tất cả trừ 5 tác vụ reduce đã hoàn thành. Một vài tác vụ chậm cuối cùng chỉ hoàn thành sau 300 giây nữa. Toàn bộ tính toán mất 1283 giây, tăng 44% về thời gian thực.

### 5.5 Sự cố máy {#dean-2004-mapreduce-s5-5 .section tag=0084}

Trong Hình 3 (c), chúng tôi trình bày một lần thực thi chương trình sort trong đó chúng tôi cố ý kết thúc 200 trong số 1746 tiến trình worker vài phút sau khi bắt đầu tính toán. Bộ lập lịch cụm nền tảng ngay lập tức khởi động lại các tiến trình worker mới trên những máy này (vì chỉ các tiến trình bị kết thúc, các máy vẫn hoạt động bình thường).

Sự cố của các worker xuất hiện dưới dạng tốc độ đầu vào âm vì một phần công việc map đã hoàn thành trước đó biến mất (do các worker map tương ứng bị kết thúc và cần được thực hiện lại). Việc thực thi lại công việc map này diễn ra tương đối nhanh. Toàn bộ tính toán hoàn thành trong 933 giây, bao gồm chi phí phụ trội khởi động (chỉ tăng 5% so với thời gian thực thi bình thường).
