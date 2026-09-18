---
paper: metcalfe-1976-ethernet
title: 'Ethernet: Distributed Packet Switching for Local Computer Networks'
authors:
  - Robert M. Metcalfe
  - David R. Boggs
year: 1976
venue: Communications of the ACM
field: networks
section: "6"
section_title: Hiệu năng
tag: 02AF
kind: section
lang: vi
source: https://www.cl.cam.ac.uk/teaching/0809/DigiCommI/metcalfe1976ethernet.pdf
pdf_sha256: e1e9d67146a1d0955a39b4fbb8e2951d6cefb4f7231a01acb9c78852280da227
pdf_pages: 6-8
extraction: vision
extraction_model: gpt-5
content_sha256: fd97f19c8537d1027c0453077d6265b43a8018bdfa9265dc74224ef048e6a822
translated_from: content/en/metcalfe-1976-ethernet/06_performance.md
source_content_sha256: 060b2ce77214436db2b11b86e95d8353eacf4900ed56e0054fe464edc977d5e1
translation_model: gpt-5
translation_run: 20260918T053014Z
glossary_version: 6
glossary_terms_sha256: 3a5b9dd3cd6211761c92d70db4c4910c364b1cae9e5e732eea77349f449c860b
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Chúng tôi trình bày ở đây một tập hợp đơn giản các công thức dùng để đặc trưng cho hiệu năng dự kiến của một Ethernet khi chịu tải nặng. Các phân tích phức tạp hơn và một số mô phỏng chi tiết đã được thực hiện, nhưng mô hình đơn giản sau đây đã tỏ ra rất hữu ích trong việc tìm hiểu cơ chế tranh chấp phân tán của Ethernet, ngay cả khi nó chịu tải vượt quá dự kiến [1, 20, 21, 22, 23, 27].

Chúng tôi xây dựng một mô hình đơn giản về hiệu năng của một Ethernet chịu tải bằng cách xem xét các khoảng thời gian Ether xen kẽ nhau. Khoảng thứ nhất, được gọi là một *khoảng truyền*, là khoảng mà Ether đã được giành quyền để truyền thành công một gói tin.

Communications  
of the ACM

July 1976  
Volume 19 trong đó Ether đã được giành quyền để truyền thành công một gói tin. Khoảng thứ hai, được gọi là một *khoảng tranh chấp*, là khoảng được tạo thành từ các khe truyền lại của Section 4.4, trong đó các trạm cố gắng giành quyền điều khiển Ether. Vì các Ethernet trong mô hình chịu tải và vì các trạm trì hoãn khi có gói tin đang truyền đi qua trước khi bắt đầu truyền, các khe được đồng bộ bởi phần cuối của khoảng giành quyền trước đó. Một khe sẽ rỗng khi không có trạm nào chọn thử truyền trong đó và sẽ chứa một va chạm nếu có nhiều hơn một trạm cố gắng truyền. Khi một khe chỉ chứa một lần thử truyền, Ether đã được giành quyền trong khoảng thời gian của một gói tin, khoảng tranh chấp kết thúc và một khoảng truyền bắt đầu.

Cho $P$ là số bit trong một Ethernet *packet*. Cho $C$ là *capacity* cực đại tính bằng bit trên giây, được mang trên Ether. Cho $T$ là *time* tính bằng giây của một khe, tức số giây cần thiết để phát hiện một va chạm sau khi bắt đầu truyền. Giả sử có $Q$ trạm liên tục *queued* để truyền một gói tin; hoặc trạm giành quyền có một gói tin mới ngay sau khi giành quyền thành công, hoặc một trạm khác trở nên sẵn sàng. $Q$ đồng thời cũng cho tổng *offered load* trên mạng, và đối với phân tích này giá trị đó luôn bằng 1 hoặc lớn hơn. Chúng tôi giả sử một trạm đang chờ truyền cố gắng truyền trong khe hiện tại với xác suất $1/Q$, hoặc trì hoãn với xác suất $1-(1/Q)$; điều này được gọi là

Fig. 3. Thuật toán kiểm soát va chạm. {#metcalfe-1976-ethernet-fig-3 .figure tag=02B0}

### 6.1 Xác suất giành quyền {#metcalfe-1976-ethernet-s6-1 .section tag=02B1}

Bây giờ chúng tôi tính $A$, xác suất đúng một trạm cố gắng truyền trong một khe và do đó *giành quyền* trên Ether. $A$ là $Q*(1/Q)*((1-(1/Q))**(Q-1))$; có $Q$ cách để một trạm chọn truyền (với xác suất $(1/Q)$) trong khi $Q-1$ trạm chọn chờ (với xác suất $1-(1/Q)$). Rút gọn,

$$
A=(1-(1/Q))^{(Q-1)}.
$$

### 6.2 Thời gian chờ {#metcalfe-1976-ethernet-s6-2 .section tag=02B2}

Bây giờ chúng tôi tính $W$, số khe *chờ* trung bình trong một khoảng tranh chấp trước khi một trạm truyền và giành quyền thành công trên Ether. Xác suất không phải chờ chút nào chính là $A$, xác suất chỉ có một trạm chọn truyền trong khe đầu tiên sau một lần truyền. Xác suất chờ 1 khe là $A*(1-A)$; xác suất chờ $i$ khe là $A*((1-A)**i)$. Giá trị trung bình của phân phối hình học này là

$$
W=(1-A)/A.
$$

### 6.3 Hiệu suất {#metcalfe-1976-ethernet-s6-3 .section tag=02B3}

Bây giờ chúng tôi tính $E$, phần thời gian mà Ether mang các gói tin hữu ích, tức *efficiency*. Thời gian của Ether được chia thành các khoảng truyền và các khoảng tranh chấp. Một lần truyền gói tin mất $P/C$ giây. Thời gian trung bình để giành quyền là $W*T$. Do đó, theo mô hình đơn giản của chúng tôi,

$$
E=(P/C)/((P/C)+(W*T)).
$$

Table I trình bày các số liệu hiệu năng tiêu biểu (tức $E$) cho Ethernet thực nghiệm của chúng tôi với các kích thước gói tin và số lượng trạm *liên tục chờ truyền* được chỉ ra. Các số liệu hiệu suất được cho không tính đến những suy giảm tất yếu do phần đầu và các gói điều khiển, cũng như những tổn thất do việc kiểm soát không chính xác tham số truyền lại $1/Q$; yếu tố thứ nhất phụ thuộc trực tiếp vào giao thức, còn yếu tố thứ hai đòi hỏi phân tích vượt quá phạm vi của bài báo này. Một lần nữa, chúng tôi cho rằng tất cả các Ethernet trong bảng đều bị quá tải; các Ethernet chịu tải bình thường thường sẽ có $Q$ nhỏ hơn nhiều so với 1 và thể hiện hành vi không được mô hình này đề cập.

Đối với các phép tính của mình, chúng tôi sử dụng $C$ bằng 3 megabit trên giây và $T$ bằng 16 microsecond. Thời lượng khe $T$ phải đủ dài để cho phép phát hiện một va chạm hoặc ít nhất bằng hai lần thời gian khứ hồi của Ether. Chúng tôi giới hạn bằng phần mềm độ dài tối đa của các gói tin ở gần 4000 bit để giảm độ trễ truy cập mạng và cho phép sử dụng hiệu quả bộ nhớ đệm gói tin của trạm.

Đối với các gói tin có kích thước lớn hơn 4000 bit, hiệu suất của Ethernet thực nghiệm của chúng tôi vẫn cao hơn nhiều so với 95

Communications  
of  
the ACM

July 1976  
Volume 19 phần trăm. Đối với các gói tin có kích thước xấp xỉ một khe, hiệu suất Ethernet tiến tới $1/e$, hiệu suất tiệm cận của một mạng Aloha phân khe [27].
