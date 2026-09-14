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
section: "4"
section_title: Kiểm soát đồng thời
tag: 00A8
kind: section
lang: vi
source: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.258.9924
pdf_sha256: 61875779e75f603d21aefba6d9bd9816d4dd0c18cf41089f43707249e24bbf88
pdf_pages: 6-9
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 0cb03073b68a3c5f86666b8c03f8c8d3438a2f36d046613cb6eaa0e6b0ed566b
translated_from: content/en/corbett-2012-spanner/04_concurrency_control.md
source_content_sha256: e78c17f9e4181cb30ec241ea6d2c3a69b4586af420515ec57048d4a5c983f0c9
translation_model: gpt-5
translation_run: 20260914T201546Z
glossary_version: 6
glossary_terms_sha256: a534ae50d60bff0e03804fd3c150e37d1876484531ab87df9c72dc4d0c455eb2
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Phần này mô tả cách TrueTime được sử dụng để đảm bảo các thuộc tính đúng đắn xung quanh kiểm soát đồng thời, và cách các thuộc tính đó được sử dụng để triển khai các tính năng như giao dịch nhất quán bên ngoài, giao dịch chỉ đọc không khóa, và đọc không chặn trong quá khứ. Các tính năng này cho phép, ví dụ, đảm bảo rằng một thao tác đọc kiểm tra toàn bộ cơ sở dữ liệu tại dấu thời gian $t$ sẽ thấy chính xác ảnh hưởng của mọi giao dịch đã xác nhận tính đến $t$.

Trong phần tiếp theo, sẽ rất quan trọng khi phân biệt các ghi nhận được Paxos quan sát (mà chúng tôi sẽ gọi là *các ghi Paxos* trừ khi ngữ cảnh đã rõ) với các ghi của máy khách Spanner. Ví dụ, xác nhận hai pha tạo ra một ghi Paxos cho giai đoạn chuẩn bị mà không có ghi máy khách Spanner tương ứng.

### 4.1 Quản lý dấu thời gian {#corbett-2012-spanner-s4-1 .section tag=00A9}

Bảng 2 liệt kê các kiểu thao tác mà Spanner hỗ trợ. Cài đặt Spanner hỗ trợ *giao dịch đọc-ghi*, *giao dịch chỉ đọc* (các giao dịch cô lập ảnh chụp được khai báo trước), và *đọc ảnh chụp*. Các ghi độc lập được triển khai dưới dạng giao dịch đọc-ghi; các đọc độc lập không phải ảnh chụp được triển khai dưới dạng giao dịch chỉ đọc. Cả hai đều được thử lại nội bộ (máy khách không cần tự viết các vòng lặp thử lại).

Một giao dịch chỉ đọc là một kiểu giao dịch có các lợi ích về hiệu năng của cô lập ảnh chụp [6]. Một giao dịch chỉ đọc phải được khai báo trước là không có bất kỳ ghi nào; nó không đơn giản chỉ là một giao dịch đọc-ghi không có ghi nào. Các đọc trong một giao dịch chỉ đọc được thực thi tại một dấu thời gian do hệ thống chọn mà không khóa, để các ghi đến không bị chặn. Việc thực thi các đọc trong một giao dịch chỉ đọc có thể tiến hành trên bất kỳ bản sao nào đủ cập nhật (Mục 4.1.3).

Một đọc ảnh chụp là một đọc trong quá khứ được thực thi mà không khóa. Một máy khách có thể chỉ định một dấu thời gian cho một đọc ảnh chụp, hoặc cung cấp một cận trên về độ cũ mong muốn của dấu thời gian và để Spanner chọn một dấu thời gian. Trong cả hai trường hợp, việc thực thi một đọc ảnh chụp tiến hành trên bất kỳ bản sao nào đủ cập nhật.

Đối với cả giao dịch chỉ đọc và đọc ảnh chụp, xác nhận là tất yếu một khi một dấu thời gian đã được chọn, trừ khi dữ liệu tại dấu thời gian đó đã được thu gom rác. Kết quả là, máy khách có thể tránh đệm các kết quả bên trong một vòng lặp thử lại. Khi một server gặp sự cố, máy khách có thể tiếp tục truy vấn nội bộ trên một server khác bằng cách lặp lại dấu thời gian và vị trí đọc hiện tại.

### 4.1.1 Các hợp đồng thuê lãnh đạo Paxos {#corbett-2012-spanner-s4-1-1 .section tag=00AA}

Cài đặt Paxos của Spanner sử dụng các hợp đồng thuê có định thời để làm cho vai trò lãnh đạo tồn tại lâu dài (mặc định 10 giây). Một lãnh đạo tiềm năng gửi các yêu cầu cho các *phiếu thuê* có định thời; khi nhận được một số đại diện phiếu thuê, lãnh đạo biết rằng nó có một hợp đồng thuê. Một bản sao mở rộng phiếu thuê của nó một cách ngầm định khi có một ghi thành công, và lãnh đạo yêu cầu các mở rộng phiếu thuê nếu chúng gần hết hạn. Định nghĩa *khoảng thuê* của một lãnh đạo là bắt đầu khi nó phát hiện có một số đại diện phiếu thuê, và kết thúc khi nó không còn có một số đại diện phiếu thuê (vì một số đã hết hạn). Spanner phụ thuộc vào bất biến rời rạc sau: đối với mỗi nhóm Paxos, khoảng thuê của mỗi lãnh đạo Paxos là rời rạc với mọi khoảng thuê của các lãnh đạo khác. Phụ lục A mô tả cách bất biến này được đảm bảo.

Cài đặt Spanner cho phép một lãnh đạo Paxos thoái vị bằng cách giải phóng các bản sao phụ của nó khỏi các phiếu thuê. Để duy trì bất biến rời rạc, Spanner giới hạn thời điểm việc thoái vị được phép. Định nghĩa $s_{max}$ là dấu thời gian lớn nhất được sử dụng bởi một lãnh đạo. Các phần tiếp theo sẽ mô tả khi nào $s_{max}$ được tăng lên. Trước khi thoái vị, một lãnh đạo phải đợi cho đến khi *TT.after($s_{max}$) is true*.

### 4.1.2 Gán dấu thời gian cho các giao dịch RW {#corbett-2012-spanner-s4-1-2 .section tag=00AB}

Các đọc và ghi giao dịch sử dụng khóa hai pha. Do đó, chúng có thể được gán dấu thời gian tại bất kỳ thời điểm nào khi tất cả các khóa đã được thu nhận, nhưng trước khi bất kỳ khóa nào được giải phóng. Với một giao dịch cụ thể, Spanner gán cho nó dấu thời gian mà Paxos gán cho ghi Paxos biểu diễn việc xác nhận giao dịch.

Spanner phụ thuộc vào bất biến đơn điệu sau: trong mỗi nhóm Paxos, Spanner gán dấu thời gian cho các ghi Paxos theo thứ tự tăng đơn điệu, ngay cả giữa các lãnh đạo. Một bản sao lãnh đạo đơn lẻ có thể dễ dàng gán dấu thời gian theo thứ tự tăng đơn điệu. Bất biến này được đảm bảo giữa các lãnh đạo bằng cách sử dụng bất biến rời rạc: một lãnh đạo chỉ được gán dấu thời gian trong khoảng của hợp đồng thuê lãnh đạo của nó. Lưu ý rằng bất cứ khi nào một dấu thời gian $s$ được gán, $s_{max}$ được tăng lên thành $s$ để duy trì tính rời rạc.

Spanner cũng thực thi bất biến nhất quán bên ngoài sau: nếu thời điểm bắt đầu của một giao dịch $T_2$ xảy ra sau thời điểm xác nhận của một giao dịch $T_1$, thì dấu thời gian xác nhận của $T_2$ phải lớn hơn dấu thời gian xác nhận của $T_1$. Định nghĩa các sự kiện bắt đầu và xác nhận cho một giao dịch $T_i$ lần lượt bởi $e_i^{start}$ và $e_i^{commit}$; và dấu thời gian xác nhận của một giao dịch $T_i$ bởi $s_i$. Bất biến trở thành $t_{abs}(e_1^{commit}) < t_{abs}(e_2^{start}) \Rightarrow s_1 < s_2$.
Giao thức để thực thi các giao dịch và gán dấu thời gian tuân theo hai quy tắc, cùng nhau đảm bảo bất biến này, như được trình bày bên dưới. Định nghĩa sự kiện đến của yêu cầu xác nhận tại lãnh đạo điều phối cho một ghi $T_i$ là $e_i^{server}$.

Bắt đầu Lãnh đạo điều phối cho một ghi $T_i$ gán một dấu thời gian xác nhận $s_i$ không nhỏ hơn giá trị của $TT.now().latest$, được tính sau $e_i^{server}$. Lưu ý rằng các lãnh đạo tham gia không quan trọng ở đây; Mục 4.2.1 mô tả cách chúng tham gia vào việc triển khai quy tắc tiếp theo.

Chờ xác nhận Điều phối viên leader đảm bảo rằng các máy khách không thể thấy bất kỳ dữ liệu nào được xác nhận bởi $T_i$ cho đến khi $TT.after(s_i)$ là đúng. Chờ xác nhận đảm bảo rằng $s_i$ nhỏ hơn thời điểm xác nhận tuyệt đối của $T_i$, hoặc $s_i < t_{abs}(e_i^{commit})$. Việc triển khai chờ xác nhận được mô tả trong Section 4.2.1. Chứng minh:

$$
\begin{align*}
s_1 &< t_{abs}(e_1^{commit}) & \text{(chờ xác nhận)} \\
t_{abs}(e_1^{commit}) &< t_{abs}(e_2^{start}) & \text{(giả định)} \\
t_{abs}(e_2^{start}) &\leq t_{abs}(e_2^{server}) & \text{(nhân quả)} \\
t_{abs}(e_2^{server}) &\leq s_2 & \text{(bắt đầu)} \\
s_1 &< s_2 & \text{(tính bắc cầu)}
\end{align*}
$$

### 4.1.3 Phục vụ các lần đọc tại một dấu thời gian {#corbett-2012-spanner-s4-1-3 .section tag=00AC}

Bất biến đơn điệu được mô tả trong Section 4.1.2 cho phép Spanner xác định chính xác liệu trạng thái của một bản sao có đủ được cập nhật để đáp ứng một lần đọc hay không. Mỗi bản sao theo dõi một giá trị được gọi là *safe time* $t_{safe}$, là dấu thời gian lớn nhất tại đó một bản sao được cập nhật đầy đủ. Một bản sao có thể đáp ứng một lần đọc tại dấu thời gian $t$ nếu $t <= t_{safe}$.

Định nghĩa $t_{safe} = min(t_{safe}^{Paxos}, t_{safe}^{TM})$, trong đó mỗi máy trạng thái Paxos có một thời gian an toàn $t_{safe}^{Paxos}$ và mỗi trình quản lý giao dịch có một thời gian an toàn $t_{safe}^{TM}$. $t_{safe}^{Paxos}$ đơn giản hơn: nó là dấu thời gian của lần ghi Paxos được áp dụng cao nhất. Vì các dấu thời gian tăng đơn điệu và các lần ghi được áp dụng theo thứ tự, các lần ghi sẽ không còn xảy ra tại hoặc thấp hơn $t_{safe}^{Paxos}$ theo Paxos.

$t_{safe}^{TM}$ là $\infty$ tại một bản sao nếu có không có giao dịch nào đã chuẩn bị (nhưng chưa được xác nhận), tức là các giao dịch nằm giữa hai pha của xác nhận hai pha. (Đối với một slave tham gia, $t_{safe}^{TM}$ thực sự đề cập đến trình quản lý giao dịch của leader của bản sao, mà trạng thái của slave có thể suy ra thông qua metadata được truyền trong các lần ghi Paxos.) Nếu có bất kỳ giao dịch nào như vậy, thì trạng thái bị ảnh hưởng bởi các giao dịch đó là không xác định: một bản sao tham gia chưa biết liệu các giao dịch như vậy có được xác nhận hay không. Như chúng tôi thảo luận trong Section 4.2.1, giao thức xác nhận đảm bảo rằng mọi bên tham gia biết một cận dưới về dấu thời gian của một giao dịch đã chuẩn bị. Mọi leader tham gia (đối với một nhóm $g$) cho một giao dịch $T_i$ gán một dấu thời gian chuẩn bị $s_{i,g}^{prepare}$ cho bản ghi chuẩn bị của nó. Leader điều phối đảm bảo rằng dấu thời gian xác nhận của giao dịch $s_i >= s_{i,g}^{prepare}$ trên tất cả các nhóm tham gia $g$. Do đó, đối với mọi bản sao trong một nhóm $g$, trên tất cả các giao dịch $T_i$ được chuẩn bị tại $g$, $t_{safe}^{TM} = min_i(s_{i,g}^{prepare}) - 1$ trên tất cả các giao dịch được chuẩn bị tại $g$.

### 4.1.4 Gán dấu thời gian cho các giao dịch RO {#corbett-2012-spanner-s4-1-4 .section tag=00AD}

Một giao dịch chỉ đọc thực thi trong hai pha: gán một dấu thời gian $s_{read}$ [8], rồi thực thi các lần đọc của giao dịch dưới dạng các lần đọc snapshot tại $s_{read}$. Các lần đọc snapshot có thể thực thi tại bất kỳ bản sao nào được cập nhật đầy đủ.

Việc gán đơn giản $s_{read} = TT.now().latest$, tại bất kỳ thời điểm nào sau khi một giao dịch bắt đầu, duy trì tính nhất quán bên ngoài bằng một lập luận tương tự như lập luận được trình bày cho các lần ghi trong Section 4.1.2. Tuy nhiên, một dấu thời gian như vậy có thể yêu cầu việc thực thi các lần đọc dữ liệu tại $s_{read}$ phải chặn nếu $t_{safe}$ chưa tiến triển đủ. (Ngoài ra, lưu ý rằng việc chọn một giá trị của $s_{read}$ cũng có thể làm tăng $s_{max}$ để duy trì tính rời rạc.) Để giảm khả năng bị chặn, Spanner nên gán dấu thời gian cũ nhất vẫn duy trì tính nhất quán bên ngoài. Section 4.2.2 giải thích cách có thể chọn một dấu thời gian như vậy.

### 4.2 Chi tiết {#corbett-2012-spanner-s4-2 .section tag=00AE}

Phần này giải thích một số chi tiết thực tế của các giao dịch đọc-ghi và các giao dịch chỉ đọc đã được lược bỏ trước đó, cũng như việc triển khai một kiểu giao dịch đặc biệt được sử dụng để thực hiện các thay đổi lược đồ nguyên tử.

Sau đó mô tả một số tinh chỉnh của các lược đồ cơ bản như đã trình bày.

### 4.2.1 Các giao dịch đọc-ghi {#corbett-2012-spanner-s4-2-1 .section tag=00AF}

Giống như Bigtable, các lần ghi xảy ra trong một giao dịch được lưu vào bộ đệm tại máy khách cho đến khi xác nhận. Do đó, các lần đọc trong một giao dịch không thấy tác động của các lần ghi của giao dịch. Thiết kế này hoạt động tốt trong Spanner vì một lần đọc trả về các dấu thời gian của mọi dữ liệu được đọc, và các lần ghi chưa được xác nhận vẫn chưa được gán dấu thời gian.

Các lần đọc trong các giao dịch đọc-ghi sử dụng wound-wait [33] để tránh bế tắc. Máy khách gửi các lần đọc đến bản sao leader của nhóm thích hợp, bản sao này thu nhận các khóa đọc rồi đọc dữ liệu mới nhất. Trong khi một giao dịch của máy khách vẫn mở, nó gửi các thông điệp keepalive để ngăn các leader tham gia hết thời gian chờ giao dịch của nó. Khi một máy khách đã hoàn thành tất cả các lần đọc và lưu vào bộ đệm tất cả các lần ghi, nó bắt đầu xác nhận hai pha. Máy khách chọn một nhóm điều phối và gửi một thông điệp xác nhận đến leader của mỗi bên tham gia cùng với danh tính của điều phối viên và mọi lần ghi đã được lưu vào bộ đệm. Việc để máy khách điều khiển xác nhận hai pha tránh gửi dữ liệu hai lần qua các liên kết diện rộng.

Một leader không phải điều phối viên-tham gia trước tiên thu nhận các khóa ghi. Sau đó nó chọn một dấu thời gian chuẩn bị phải lớn hơn mọi dấu thời gian mà nó đã gán cho các giao dịch trước đó (để duy trì tính đơn điệu), và ghi một bản ghi chuẩn bị thông qua Paxos. Mỗi bên tham gia sau đó thông báo cho điều phối viên về dấu thời gian chuẩn bị của nó.

Trưởng nhóm điều phối cũng trước tiên thu được các khóa ghi, nhưng bỏ qua pha chuẩn bị. Nó chọn một dấu thời gian cho toàn bộ giao dịch sau khi nhận thông tin từ tất cả các trưởng nhóm tham gia khác. Dấu thời gian xác nhận s phải lớn hơn hoặc bằng tất cả các dấu thời gian chuẩn bị (để thỏa mãn các ràng buộc được thảo luận trong Section 4.1.3), lớn hơn TT.now().latest tại thời điểm trưởng nhóm điều phối nhận được thông điệp xác nhận của nó, và lớn hơn bất kỳ dấu thời gian nào mà trưởng nhóm đã gán cho các giao dịch trước đó (một lần nữa, để duy trì tính đơn điệu). Sau đó trưởng nhóm điều phối ghi một bản ghi xác nhận thông qua Paxos (hoặc hủy bỏ nếu nó hết thời gian chờ trong khi đợi các bên tham gia khác).

Trước khi cho phép bất kỳ bản sao điều phối nào áp dụng bản ghi xác nhận, trưởng nhóm điều phối đợi cho đến TT.after(s), để tuân theo quy tắc chờ xác nhận được mô tả trong Section 4.1.2. Vì trưởng nhóm điều phối đã chọn s dựa trên TT.now().latest, và bây giờ đợi cho đến khi dấu thời gian đó được đảm bảo đã nằm trong quá khứ, thời gian chờ kỳ vọng ít nhất là $2 * \overline{\epsilon}$. Thời gian chờ này thường được chồng lấp với việc giao tiếp Paxos. Sau thời gian chờ xác nhận, trưởng nhóm điều phối gửi dấu thời gian xác nhận đến máy khách và tất cả các trưởng nhóm tham gia khác. Mỗi trưởng nhóm tham gia ghi kết quả của giao dịch thông qua Paxos. Tất cả các bên tham gia áp dụng cùng một dấu thời gian và sau đó giải phóng các khóa.

### 4.2.2 Giao dịch chỉ đọc {#corbett-2012-spanner-s4-2-2 .section tag=00B0}

Việc gán một dấu thời gian yêu cầu một pha thương lượng giữa tất cả các nhóm Paxos có liên quan đến các thao tác đọc. Do đó, Spanner yêu cầu một biểu thức phạm vi cho mọi giao dịch chỉ đọc, là một biểu thức tóm tắt các khóa sẽ được đọc bởi toàn bộ giao dịch. Spanner tự động suy ra phạm vi cho các truy vấn độc lập.

Nếu các giá trị của phạm vi được phục vụ bởi một nhóm Paxos duy nhất, thì máy khách gửi giao dịch chỉ đọc đến trưởng nhóm của nhóm đó. (Triển khai Spanner hiện tại chỉ chọn một dấu thời gian cho giao dịch chỉ đọc tại một trưởng nhóm Paxos.) Trưởng nhóm đó gán $s_{read}$ và thực thi thao tác đọc. Đối với một thao tác đọc tại một site duy nhất, Spanner nhìn chung hoạt động tốt hơn TT.now().latest. Định nghĩa LastTS() là dấu thời gian của lần ghi đã xác nhận cuối cùng tại một nhóm Paxos. Nếu không có các giao dịch đã chuẩn bị, phép gán $s_{read} = LastTS()$ hiển nhiên thỏa mãn tính nhất quán bên ngoài: giao dịch sẽ thấy kết quả của lần ghi cuối cùng, và do đó được sắp xếp sau nó.

Nếu các giá trị của phạm vi được phục vụ bởi nhiều nhóm Paxos, có một số lựa chọn. Lựa chọn phức tạp nhất là thực hiện một vòng giao tiếp với tất cả các trưởng nhóm của các nhóm đó để thương lượng $s_{read}$ dựa trên LastTS(). Spanner hiện thực hiện một lựa chọn đơn giản hơn. Máy khách tránh một vòng thương lượng, và chỉ cho các thao tác đọc của nó thực thi tại $s_{read} = TT.now().latest$ (điều này có thể phải chờ thời gian an toàn tiến triển). Tất cả các thao tác đọc trong giao dịch có thể được gửi đến các bản sao đủ cập nhật.

### 4.2.3 Giao dịch thay đổi lược đồ {#corbett-2012-spanner-s4-2-3 .section tag=00B1}

TrueTime cho phép Spanner hỗ trợ các thay đổi lược đồ nguyên tử. Việc sử dụng một giao dịch tiêu chuẩn sẽ không khả thi, bởi vì số lượng bên tham gia (số lượng nhóm trong một cơ sở dữ liệu) có thể lên đến hàng triệu. Bigtable hỗ trợ các thay đổi lược đồ nguyên tử trong một datacenter, nhưng các thay đổi lược đồ của nó chặn mọi thao tác.

Một giao dịch thay đổi lược đồ của Spanner là một biến thể nhìn chung không chặn của một giao dịch tiêu chuẩn. Thứ nhất, nó được gán rõ ràng một dấu thời gian trong tương lai, dấu này được đăng ký trong pha chuẩn bị. Do đó, các thay đổi lược đồ trên hàng nghìn server có thể hoàn tất với sự gián đoạn tối thiểu đối với các hoạt động đồng thời khác. Thứ hai, các thao tác đọc và ghi, vốn phụ thuộc ngầm vào lược đồ, đồng bộ với bất kỳ dấu thời gian thay đổi lược đồ nào đã đăng ký tại thời điểm t: chúng có thể tiếp tục nếu các dấu thời gian của chúng đứng trước t, nhưng chúng phải chặn phía sau giao dịch thay đổi lược đồ nếu các dấu thời gian của chúng đứng sau t. Nếu không có TrueTime, việc định nghĩa thay đổi lược đồ xảy ra tại t sẽ không có ý nghĩa.

| bản sao | độ trễ (ms) |  |  | thông lượng (Kops/sec) |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | ghi | giao dịch chỉ đọc | đọc snapshot | ghi | giao dịch chỉ đọc | đọc snapshot |
| 1D | 9.4±.6 | — | — | 4.0±.3 | — | — |
| 1 | 14.4±1.0 | 1.4±.1 | 1.3±.1 | 4.1±.05 | 10.9±.4 | 13.5±.1 |
| 3 | 13.9±.6 | 1.3±.1 | 1.2±.1 | 2.2±.5 | 13.8±3.2 | 38.5±.3 |
| 5 | 14.4±.4 | 1.4±.05 | 1.3±.04 | 2.8±.3 | 25.3±5.2 | 50.0±1.1 |

Bảng 3: Các phép đo chuẩn vi mô cho thao tác. Trung bình và độ lệch chuẩn trên 10 lần chạy. 1D nghĩa là một bản sao với thời gian chờ xác nhận bị vô hiệu hóa. {#corbett-2012-spanner-tab-3 .table tag=00B2}

### 4.2.4 Tinh chỉnh {#corbett-2012-spanner-s4-2-4 .section tag=00B3}

$t_{safe}^{TM}$ như được định nghĩa ở trên có một điểm yếu, đó là một giao dịch đã chuẩn bị duy nhất ngăn $t_{safe}$ tiến triển. Do đó, không có thao tác đọc nào có thể xảy ra tại các dấu thời gian muộn hơn, ngay cả khi các thao tác đọc không xung đột với giao dịch. Các xung đột giả như vậy có thể được loại bỏ bằng cách bổ sung cho $t_{safe}^{TM}$ một ánh xạ chi tiết từ các phạm vi khóa đến các dấu thời gian của giao dịch đã chuẩn bị. Thông tin này có thể được lưu trữ trong bảng khóa, vốn đã ánh xạ các phạm vi khóa tới siêu dữ liệu khóa. Khi một thao tác đọc đến, nó chỉ cần được kiểm tra với thời gian an toàn chi tiết cho các phạm vi khóa mà thao tác đọc đó xung đột.

$LastTS()$ như được định nghĩa ở trên có một điểm yếu tương tự: nếu một giao dịch vừa được commit, một giao dịch chỉ đọc không xung đột vẫn phải được gán $s_{read}$ để theo sau giao dịch đó. Do đó, việc thực thi của lần đọc có thể bị trì hoãn. Điểm yếu này có thể được khắc phục tương tự bằng cách bổ sung cho $LastTS()$ một ánh xạ chi tiết từ các khoảng khóa đến các dấu thời gian commit trong bảng khóa. (Chúng tôi vẫn chưa triển khai tối ưu hóa này.) Khi một giao dịch chỉ đọc đến, dấu thời gian của nó có thể được gán bằng cách lấy giá trị lớn nhất của $LastTS()$ đối với các khoảng khóa mà giao dịch xung đột, trừ khi có một giao dịch đã chuẩn bị xung đột (có thể được xác định từ thời gian an toàn chi tiết).

$t_{safe}^{Paxos}$ như được định nghĩa ở trên có một điểm yếu là nó không thể tiến triển khi không có các lần ghi Paxos. Nghĩa là, một lần đọc snapshot tại $t$ không thể thực thi ở các nhóm Paxos mà lần ghi cuối cùng xảy ra trước $t$. Spanner giải quyết vấn đề này bằng cách tận dụng tính rời nhau của các khoảng thời gian thuê của leader. Mỗi leader Paxos tiến triển $t_{safe}^{Paxos}$ bằng cách duy trì một ngưỡng mà phía trên đó các dấu thời gian của các lần ghi trong tương lai sẽ xuất hiện: nó duy trì một ánh xạ $MinNextTS(n)$ từ số thứ tự Paxos $n$ đến dấu thời gian tối thiểu có thể được gán cho số thứ tự Paxos $n + 1$. Một replica có thể tiến triển $t_{safe}^{Paxos}$ đến $MinNextTS(n) - 1$ khi nó đã áp dụng qua $n$.

Một leader duy nhất có thể dễ dàng thực thi các cam kết $MinNextTS()$ của nó. Vì các dấu thời gian được $MinNextTS()$ cam kết nằm trong thời gian thuê của một leader, bất biến về tính rời nhau thực thi các cam kết $MinNextTS()$ giữa các leader. Nếu một leader muốn tiến triển $MinNextTS()$ vượt quá thời điểm kết thúc thời gian thuê của nó, trước tiên nó phải gia hạn thời gian thuê. Lưu ý rằng $s_{max}$ luôn được tiến triển đến giá trị cao nhất trong $MinNextTS()$ để duy trì tính rời nhau.

Một leader mặc định tiến triển các giá trị $MinNextTS()$ mỗi 8 giây. Do đó, khi không có các giao dịch đã chuẩn bị, các slave khỏe mạnh trong một nhóm Paxos không hoạt động có thể phục vụ các lần đọc tại các dấu thời gian cũ hơn 8 giây trong trường hợp xấu nhất. Một leader cũng có thể tiến triển các giá trị $MinNextTS()$ theo yêu cầu từ các slave.
