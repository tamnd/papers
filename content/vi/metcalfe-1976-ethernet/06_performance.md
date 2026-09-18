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
content_sha256: a98745492be83d00a5f53b4c1849b1db878d66c0c6cf3240b8ff7a20f172c2b6
translated_from: content/en/metcalfe-1976-ethernet/06_performance.md
source_content_sha256: 060b2ce77214436db2b11b86e95d8353eacf4900ed56e0054fe464edc977d5e1
translation_model: gpt-5
translation_run: 20260918T110147Z
glossary_version: 7
glossary_terms_sha256: 5bfb74d0e4b3e9a8237f78ceae59e221549684c174791655271c5455f7fd5e4e
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Chúng tôi trình bày ở đây một tập hợp công thức đơn giản để đặc trưng cho hiệu năng được mong đợi của một Ethernet khi chịu tải lớn. Các phân tích phức tạp hơn và một số mô phỏng chi tiết đã được thực hiện, nhưng mô hình đơn giản sau đây đã chứng tỏ rất hữu ích trong việc tìm hiểu sơ đồ tranh chấp phân tán của Ethernet, ngay cả khi nó được tải vượt quá mức dự kiến [1, 20, 21, 22, 23, 27].

Chúng tôi xây dựng một mô hình đơn giản về hiệu năng của một Ethernet đang chịu tải bằng cách xem xét các khoảng thời gian Ether xen kẽ. Khoảng đầu tiên, được gọi là một *khoảng truyền*, là khoảng

Truyền thông  
của ACM

Tháng 7 năm 1976  
Tập 19 trong đó Ether đã được chiếm dụng để truyền thành công một gói tin. Khoảng thứ hai, được gọi là một *khoảng tranh chấp*, là khoảng được tạo thành từ các khe truyền lại của Section 4.4, trong đó các trạm cố gắng giành quyền điều khiển Ether. Vì các Ethernet trong mô hình chịu tải và vì các trạm trì hoãn trước các gói tin đang đi qua trước khi bắt đầu truyền, các khe được đồng bộ hóa bởi phần cuối của khoảng giành quyền trước đó. Một khe sẽ trống khi không có trạm nào chọn thử truyền trong đó và nó sẽ chứa một va chạm nếu có nhiều hơn một trạm cố gắng truyền. Khi một khe chỉ chứa một lần thử truyền duy nhất, Ether đã được chiếm dụng trong thời gian của một gói tin, khoảng tranh chấp kết thúc và một khoảng truyền bắt đầu.

Gọi $P$ là số bit trong một *gói tin* Ethernet. Gọi $C$ là *dung lượng* cực đại tính bằng bit trên giây, được mang trên Ether. Gọi $T$ là *thời gian* tính bằng giây của một khe, là số giây cần thiết để phát hiện một va chạm sau khi bắt đầu một lần truyền. Giả sử rằng có $Q$ trạm liên tục *xếp hàng* để truyền một gói tin; hoặc trạm giành quyền có một gói tin mới ngay sau khi giành quyền thành công hoặc một trạm khác trở nên sẵn sàng. Lưu ý rằng $Q$ cũng đồng thời cho tải được cung cấp tổng cộng trên mạng, trong phân tích này luôn là 1 hoặc lớn hơn. Chúng tôi giả sử rằng một trạm đang xếp hàng thử truyền trong khe hiện tại với xác suất $1/Q$, hoặc trì hoãn với xác suất $1-(1/Q)$; điều này được biết đến

Hình 3. Thuật toán điều khiển va chạm. {#metcalfe-1976-ethernet-fig-3 .figure tag=02B0}

### 6.1 Xác suất giành quyền {#metcalfe-1976-ethernet-s6-1 .section tag=02B1}

Bây giờ chúng tôi tính $A$, xác suất chính xác một trạm thử truyền trong một khe và do đó *giành quyền* trên Ether. $A$ là $Q*(1/Q)*((1-(1/Q))**(Q-1))$; có $Q$ cách để một trạm chọn truyền (với xác suất $(1/Q)$) trong khi $Q-1$ trạm chọn chờ (với xác suất $1-(1/Q)$). Rút gọn,

$$
A=(1-(1/Q))^{(Q-1)}.
$$

### 6.2 Thời gian chờ {#metcalfe-1976-ethernet-s6-2 .section tag=02B2}

Bây giờ chúng tôi tính $W$, số khe *chờ* trung bình trong một khoảng tranh chấp trước khi một lần truyền của một trạm giành quyền trên Ether thành công. Xác suất không chờ chút thời gian nào chính là $A$, xác suất một và chỉ một trạm chọn truyền trong khe đầu tiên sau một lần truyền. Xác suất chờ 1 khe là $A*(1-A)$; xác suất chờ $i$ khe là $A*((1-A)**i)$. Giá trị trung bình của phân phối hình học này là

$$
W=(1-A)/A.
$$

### 6.3 Hiệu suất {#metcalfe-1976-ethernet-s6-3 .section tag=02B3}

Bây giờ chúng tôi tính $E$, phần thời gian mà Ether đang mang các gói tin hữu ích, tức *hiệu suất*. Thời gian của Ether được chia giữa các khoảng truyền và các khoảng tranh chấp. Một lần truyền gói tin mất $P/C$ giây. Thời gian trung bình để giành quyền là $W*T$. Do đó, theo mô hình đơn giản của chúng tôi,

$$
E=(P/C)/((P/C)+(W*T)).
$$

Bảng I trình bày các số liệu hiệu năng tiêu biểu (tức là $E$) cho Ethernet thử nghiệm của chúng tôi với các kích thước gói tin và số lượng trạm *xếp hàng liên tục* được chỉ ra. Các số liệu hiệu suất được đưa ra không tính đến các suy giảm không thể tránh khỏi do các phần đầu và các gói điều khiển cũng như các mất mát do việc điều khiển không chính xác tham số truyền lại $1/Q$; phần trước phụ thuộc trực tiếp vào giao thức và phần sau cần phân tích vượt quá phạm vi của bài báo này. Một lần nữa, chúng tôi cho rằng tất cả các Ethernet trong bảng đều bị quá tải; các Ethernet chịu tải bình thường thường sẽ có $Q$ nhỏ hơn nhiều so với 1 và thể hiện hành vi không được mô hình này bao quát.

Trong các phép tính của chúng tôi, chúng tôi sử dụng $C$ bằng 3 megabit trên giây và $T$ bằng 16 microgiây. Thời lượng khe $T$ phải đủ dài để cho phép phát hiện một va chạm hoặc ít nhất bằng hai lần thời gian khứ hồi của Ether. Chúng tôi giới hạn bằng phần mềm độ dài tối đa của các gói tin của mình gần 4000 bit để giữ độ trễ của truy cập mạng thấp và cho phép sử dụng hiệu quả bộ lưu trữ bộ đệm gói tin của trạm.

Đối với các gói tin có kích thước lớn hơn 4000 bit, hiệu suất của Ethernet thử nghiệm của chúng tôi vẫn cao hơn nhiều so với 95

Truyền thông  
của  
ACM

Tháng 7 năm 1976  
Tập 19 phần trăm. Đối với các gói tin có kích thước xấp xỉ kích thước của một khe, hiệu suất Ethernet tiến gần đến $1/e$, hiệu suất tiệm cận của một mạng Aloha phân khe [27].
