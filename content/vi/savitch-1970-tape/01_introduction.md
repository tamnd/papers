---
paper: savitch-1970-tape
title: Relationships Between Nondeterministic and Deterministic Tape Complexities
authors:
  - Walter J. Savitch
year: 1970
venue: Journal of Computer and System Sciences
field: theory
section_title: Giới thiệu
kind: section
lang: vi
source: https://web.archive.org/web/20240712003717id_/https://core.ac.uk/download/pdf/82306488.pdf
pdf_sha256: 18c874bdb0c9b7908ab97bdeea66e0d5397ed5b715eb43402020454179f281d1
pdf_pages: 1-16
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 78fd181d7a3ba0905a72498537ebd84a759e568cc68345865545e9176a5a7ef5
translated_from: content/en/savitch-1970-tape/01_introduction.md
source_content_sha256: e3060aa8278afd55b5dc5b6c356e6b8ea89a6409a0fcee89a673407f9f06b533
translation_model: gpt-5
translation_run: 20260919T075800Z
glossary_version: 7
glossary_terms_sha256: a53d4b02c913445c3baaef8eee5fd81f1dcadf55e59409c12a52700dc0c85335
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Một bài toán mở nổi tiếng trong lý thuyết ngôn ngữ hình thức và độ phức tạp tính toán là quyết định liệu có tồn tại hay không một ngôn ngữ phi ngữ cảnh nhạy cảm không tất định, tức là quyết định liệu có hay không một tập được chấp nhận bởi một ôtômát bị giới hạn tuyến tính không tất định, nhưng không được chấp nhận bởi bất kỳ máy tất định tương tự nào. Trong bài báo này, chúng tôi đưa ra một số câu trả lời từng phần cho một khái quát hóa tự nhiên của bài toán này. Chúng tôi cố gắng trả lời câu hỏi sau: "Cho một máy Turing bị giới hạn băng không tất định chấp nhận một tập $A$, một máy Turing tất định cần bao nhiêu bộ nhớ bổ sung để nhận biết $A$?"

Cụ thể hơn, chúng tôi chỉ ra rằng bất kỳ máy Turing bị giới hạn băng $L(n)$ không tất định nào cũng có thể được mô phỏng bởi một máy Turing bị giới hạn băng $[L(n)]^2$ tất định, với điều kiện $L(n) \geq \log_2 n$. Do đó, đặc biệt, mọi ngôn ngữ nhạy cảm ngữ cảnh đều có thể được nhận biết trong bộ nhớ tất định $n^2$, trong đó $n$ là độ dài của đầu vào. Như một hệ quả của chứng minh định lý này, chúng tôi thu được rằng nếu một ngôn ngữ nhạy cảm ngữ cảnh được

* Công trình này dựa trên một phần luận án tiến sĩ của tác giả tại Khoa Toán học của University of California, Berkeley. Phần lớn các kết quả đã được công bố trong [9]. Một phần của nghiên cứu này được thực hiện khi tác giả là National Science Foundation Graduate Fellow.

chấp nhận bởi một ôtômát bị giới hạn tuyến tính không tất định trong thời gian đa thức, thì ngôn ngữ đó được chấp nhận bởi một máy Turing tất định trong bộ nhớ $n \log_2 n$. Cũng chỉ ra rằng nếu các lớp độ phức tạp băng không tất định và tất định bằng nhau đối với các hàm "nhỏ", thì chúng cũng bằng nhau đối với các hàm "lớn".

Khái niệm mê cung được hình thức hóa và các tính toán của các máy không tất định được liên hệ với các cách đi xuyên qua của một số mê cung nhất định. Mối liên hệ này được sử dụng để thu được một tập cụ thể, cụ thể là tập các mã hóa của các mê cung có thể đi xuyên qua, sao cho, nếu có bất kỳ tập nào phân biệt các lớp độ phức tạp băng không tất định với các lớp độ phức tạp băng tất định, thì đây là một tập như vậy. Nghĩa là, có một máy Turing không tất định chấp nhận các mã hóa của các mê cung có thể đi xuyên qua trong bộ nhớ $\log_2 n$. Ngoài ra, nếu có một máy Turing tất định chấp nhận chúng trong cùng bộ nhớ, $\log_2 n$, thì với mọi hàm bộ nhớ $L(n) \geq \log_2 n$, bất kỳ máy Turing bị giới hạn băng $L(n)$ không tất định nào cũng có thể được kích thích bởi một máy Turing bị giới hạn băng $L(n)$ tất định.

Mô hình máy

Thiết bị được nghiên cứu trong bài báo này là Máy Turing nhiều băng. Theo thuật ngữ của [3], đây là một máy Turing với hữu hạn băng lưu trữ vô hạn hai chiều và một băng đầu vào chỉ đọc được cung cấp các dấu kết thúc. Chúng tôi chỉ đưa ra một định nghĩa không chính thức về thiết bị này. Một *máy Turing nhiều băng* (sau đây gọi đơn giản là *máy Turing*) là một bộ điều khiển trạng thái hữu hạn được gắn với một băng đầu vào chỉ đọc và hữu hạn các băng lưu trữ đọc/ghi. Các băng được chia thành các ô. Mỗi ô của một băng lưu trữ có khả năng chứa một ký hiệu từ bảng chữ cái băng lưu trữ hữu hạn $\Gamma$. Băng đầu vào sẽ luôn chứa một chuỗi hữu hạn $w$ gồm các ký hiệu từ bảng chữ cái đầu vào hữu hạn $\Sigma$. Chuỗi $w$ được phân cách bởi hai ký hiệu không thuộc $\Sigma$ được gọi là *dấu kết thúc bên trái* và *dấu kết thúc bên phải*. Mỗi băng có một đầu đọc giao tiếp với bộ điều khiển hữu hạn.

Tại bất kỳ thời điểm nào, mỗi đầu đọc sẽ quét một ô trên băng của nó và bộ điều khiển sẽ ở một trạng thái. Phụ thuộc vào trạng thái này và các ký hiệu được các đầu đọc quét, máy sẽ, trong một bước, chuyển sang một trạng thái khác, ghi đè một ký hiệu trên ô đang được quét của mỗi băng lưu trữ của nó, rồi dịch chuyển một số đầu đọc của nó (có thể bao gồm cả đầu đọc đầu vào) sang trái hoặc phải một ô. Bộ điều khiển hữu hạn được thiết kế sao cho đầu đọc đầu vào sẽ không bao giờ rời khỏi đoạn băng chứa $w$ và các dấu kết thúc. Máy được gọi là *tất định* nếu chỉ có một hành động khả dĩ tại mỗi bước. Máy được gọi là *không tất định* nếu có hữu hạn hành động khả dĩ tại mỗi bước.

Một số trạng thái được phân biệt và gọi là *các trạng thái chấp nhận* và một trạng thái được phân biệt và gọi là *trạng thái ban đầu*. Chúng tôi nói máy tất định $Z$ *chấp nhận* chuỗi đầu vào $w$ trên $\Sigma$ nếu $Z$ đi vào một trạng thái chấp nhận sau hữu hạn bước, khi bắt đầu ở trạng thái ban đầu, với tất cả các băng lưu trữ trống, $w$ trên băng đầu vào và đầu đọc đầu vào đang quét dấu kết thúc bên trái. Định nghĩa này cũng giống trong trường hợp $Z$ là không tất định ngoại trừ việc chúng ta chỉ yêu cầu rằng có một chuỗi hữu hạn các bước khả dĩ dẫn đến một trạng thái chấp nhận, bắt đầu từ cấu hình ban đầu được mô tả ở trên.

Định nghĩa. Giả sử $L(n)$ là một hàm trên các số tự nhiên, $Z$ là một máy Turing (tất định hoặc không tất định), và $A$ là một tập các chuỗi trên bảng chữ cái đầu vào của $Z$. $Z$ được nói là chấp nhận tập $A$ trong bộ nhớ $L(n)$ nếu

(i) với mỗi chuỗi $w$ trong $A$, có ít nhất một tính toán khả dĩ của $Z$ chấp nhận $w$ và trong đó mỗi đầu đọc băng lưu trữ quét nhiều nhất $L(|w|)$ ô, và

(ii) $Z$ không chấp nhận chuỗi nào không thuộc $A$. $|w|$ là độ dài của chuỗi, $w$.

Trong bài báo này chúng tôi chỉ xem xét tốc độ tăng trưởng của các hàm bộ nhớ. Nghĩa là, đối với mục đích của chúng tôi, các hàm bộ nhớ $L(n)$ và $\epsilon L(n)$ là giống nhau, với mọi hằng số $\epsilon > 0$. Sự đồng nhất này của các hàm xuất phát từ thực tế rằng các máy Turing của chúng tôi được phép có các bảng chữ cái băng lưu trữ hữu hạn tùy ý. Vì vậy, bất kỳ máy Turing nào hoạt động với bộ nhớ $L(n)$ đều có thể được sửa đổi để hoạt động với bộ nhớ $\epsilon L(n)$ và vẫn chấp nhận cùng một tập băng. (Xem, ví dụ, [3].) Chúng tôi giả sử người đọc quen thuộc với các kỹ thuật giảm băng như vậy.

Trong phần tiếp theo, đôi khi sẽ thuận tiện khi giả sử rằng các hàm lưu trữ là "tốt". Điều kiện về tính tốt mà chúng ta muốn là các hàm phải đo được [4].

Định nghĩa. Một hàm $L(n)$ được gọi là *đo được* nếu tồn tại một máy Turing chỉ với một băng lưu trữ sao cho, với bất kỳ đầu vào nào có độ dài $n$, máy sẽ dừng sau một quá trình tính toán trong đó đầu đọc của băng lưu trữ quét chính xác $L(n)$ ô.

Có vẻ như tất cả các hàm lưu trữ thông dụng $L(n) \geq \log_2 n$ đều đo được. Cụ thể, mọi đa thức theo $n$ và $\log_2 n$ đều đo được.

Mô phỏng xác định của các máy Turing không xác định

Định lý 1. Nếu một tập, $A$, được chấp nhận bởi một máy Turing không xác định, $Z_N$, trong phạm vi lưu trữ $L(n) \geq \log_2 n$, thì $A$ được chấp nhận bởi một máy Turing xác định nào đó, $Z_D$, trong phạm vi lưu trữ $[L(n)]^2$. {#savitch-1970-tape-thm-1 .statement tag=0400}

Chứng minh. Định lý được chứng minh bằng cách đưa ra một thuật toán theo đó $Z_D$ có thể mô phỏng các phép tính của $Z_N$. Thuật toán này tương tự như thuật toán được Lewis, Stearns, và Hartmanis [7] sử dụng để chỉ ra rằng mọi ngôn ngữ phi ngữ cảnh đều được chấp nhận bởi một máy Turing xác định trong phạm vi lưu trữ $(\log_2 n)^2$.

Giả sử máy Turing $Z_N$ có $k$ băng lưu trữ, bảng chữ cái của băng lưu trữ $\Gamma$, và tập trạng thái bên trong $Q$. Gọi $\Delta = Q \cup \Gamma \cup \{1, 2, *, \downarrow\}$, trong đó $\downarrow$ và $*$ là hai ký hiệu mới. Một *mô tả tức thời* (ID) của $Z_N$ là một chuỗi trên $\Delta$ có dạng pq * u₁ ↓ v₁ * u₂ ↓ v₂ * ... * uₖ ↓ vₖ, trong đó p là một số ở dạng ký hiệu dyadic¹ chỉ vị trí của đầu đọc đầu vào của $Z_N$, q là một phần tử của Q chỉ ra rằng bộ điều khiển hữu hạn của $Z_N$ đang ở trạng thái q, và $u_i, v_i$ là các phần tử của $\Gamma^*$, $i = 1, 2, ..., k$. $u_i ↓ v_i$ được hiểu là $u_i v_i$ là nội dung của băng lưu trữ thứ i của $Z_N$ và đầu đọc trên băng này đang quét ký hiệu đầu tiên của chuỗi $v_i$. Vì vậy, ngoại trừ nội dung của băng đầu vào, một ID của $Z_N$ là một mô tả hoàn chỉnh về một cấu hình của $Z_N$.

Vì $Z_N$ chấp nhận tập $A$ trong phạm vi lưu trữ $L(n) \geq \log_2 n$, nên suy ra rằng với mỗi chuỗi w có độ dài n được $Z_N$ chấp nhận, tồn tại một phép tính của $Z_N$ chấp nhận w trong đó mỗi ID có độ dài không vượt quá $cL(n)$. Hơn nữa, vì mỗi ID có độ dài nhiều nhất là $cL(n)$, phép tính cần không quá $2^{c'L(n)}$ bước. c và $c'$ là các hằng số chỉ phụ thuộc vào $Z_N$ chứ không phụ thuộc vào đầu vào w.

Trước hết chúng ta đưa ra thuật toán cho trường hợp: $L(n)$ là đo được.

Với một đầu vào có độ dài n, $Z_D$ khởi tạo phép tính của nó bằng cách chia một trong các băng lưu trữ của nó thành $[c'L(n)] + 1$ khối (được gọi là các thanh ghi), mỗi khối có độ dài $[cL(n)]$, tiếp theo là $[c'L(n)] + 1$ khối (được gọi là các thẻ), mỗi khối có khả năng lưu trữ hoặc 0 hoặc 1. Nó có thể dễ dàng thực hiện việc này nếu $L(n)$ là đo được. [y] là số nguyên lớn nhất không vượt quá y. Lưu ý rằng mỗi thanh ghi có khả năng chứa bất kỳ ID nào của $Z_N$ trong đó phần không trắng của mỗi băng lưu trữ nhiều nhất là $L(n)$. $Z_D$ có một băng lưu trữ thứ hai cho công việc tạm thời.

Ý tưởng của thuật toán như sau. $Z_D$ có chuỗi w làm đầu vào. Trong quá trình của thuật toán, $Z_D$ sẽ xem xét hai ID I, $I''$ được lưu trong các thanh ghi cụ thể. Với một m được chọn trước, nó sẽ cần kiểm tra xem, với đầu vào w, $Z_N$ có thể trong $2^m$ bước thay đổi cấu hình của nó từ I sang $I''$ hay không. Hơn nữa, $Z_D$ sẽ phải thực hiện nhiệm vụ này chỉ sử dụng m thanh ghi. $Z_D$ tiến hành như sau. Nó duyệt qua (theo một cách có hệ thống) tất cả các ID $I'$ của $Z_N$ và với mỗi $I'$, kiểm tra xem có một tính toán gồm không quá $2^{m-1}$ bước từ I đến $I'$, và một tính toán gồm không quá $2^{m-1}$ bước từ $I'$ đến $I''$ hay không. $Z_D$ cần một thanh ghi để theo dõi $I'$, khiến nó còn lại $m - 1$ thanh ghi. Vì vậy $Z_D$ đã giảm nhiệm vụ mô phỏng $2^m$ chuyển động của $Z_N$ sử dụng m thanh ghi thành mô phỏng $2^{m-1}$ chuyển động của $Z_N$ sử dụng $m - 1$ thanh ghi. Sau đó $Z_D$ giảm mỗi tính toán gồm $2^{m-1}$ bước thành hai tính toán gồm $2^{m-2}$ bước. $Z_D$ tiếp tục giảm độ dài của các tính toán mà nó cần kiểm tra cho đến khi nó chỉ cần kiểm tra, với các ID thích hợp $I_1$ và $I_2$, liệu với đầu vào w, $Z_N$ có thể trong một bước đi từ $I_1$ đến $I_2$ hay không. Điều này nó có thể dễ dàng thực hiện bằng cách sử dụng không gian lưu trữ bằng không. Bây giờ nếu có bất kỳ tính toán chấp nhận nào của $Z_N$, thì có một tính toán chấp nhận trong $2^{c'L(n)}$ bước. Vì vậy $Z_D$ có thể mô phỏng tính toán này bằng cách sử dụng $c'L(n)$ thanh ghi hoặc khoảng $[L(n)]^2$ ô của băng lưu trữ.

Bây giờ chúng ta định nghĩa một số ký hiệu cho phát biểu hình thức của thuật toán. Vì các ID là các chuỗi trên một bảng chữ cái hữu hạn, $\Delta$, chúng có thể được xem như các số nguyên trong ký hiệu m-adic, trong đó m là số ký hiệu trong $\Delta$. Cụ thể hơn, nếu $\Delta = \{a_1, a_2, ..., a_m\}$ thì chuỗi $a_{i_k} a_{i_{k-1}} \cdots a_{i_0}$ sẽ biểu diễn số $\sum_{j=0}^k i_j m^j$. Chúng ta sẽ không phân biệt giữa một chuỗi và số mà nó biểu diễn.

¹ Chuỗi $d_l d_{l-1} \cdots d_0$ trên bảng chữ cái {1, 2} là biểu diễn dyadic của số $\sum_{i=0}^l d_i 2^i$.

ĐỊNH NGHĨA. Nếu $I$ và $I'$ là các ID của $Z_N$ và nếu $Z_N$ có thể trong một bước, với đầu vào $w$, chuyển từ cấu hình $I$ sang cấu hình $I'$, hoặc nếu $I = I'$, thì ta sẽ viết $I \xrightarrow{w} I'$. Trong thuật toán, ta sẽ kiểm tra xem $I \xrightarrow{w} I'$ có đúng với các chuỗi tùy ý $I, I'$ trên $\Delta$ hay không. Nếu $I$ hoặc $I'$ không phải là một ID của $Z_N$, thì phép kiểm tra thất bại.

Trong thuật toán sau, $x_i$ biểu thị nội dung của thanh ghi thứ $i$ và $T_i$ biểu thị nội dung của thẻ thứ $i$ $[1 \leq i \leq c'L(n) + 1]$. $Z_D$ có một chuỗi $w$ làm đầu vào và mọi tham chiếu đến các tính toán của $Z_N$ đều có nghĩa là các tính toán của $Z_N$ dưới đầu vào $w$ và trong đó phần không trắng của mỗi băng công việc luôn dài không quá $L(|w|)$ ô. Tại bất kỳ thời điểm nào trong tính toán của $Z_D$, nếu $T_i = 1$, thì tồn tại một tính toán của $Z_N$ từ ID bắt đầu đến $x_i$.

THUẬT TOÁN CHO MÁY $Z_D$

Tóm tắt ký hiệu

$w$ là chuỗi đầu vào.
$n$ là độ dài của $w$.
$r$ là số nguyên nhỏ nhất sao cho $r \geq c'L(n)$.
$c'$ là số sao cho, với $w$ làm đầu vào, nếu $Z_N$ chấp nhận $w$ tại bất kỳ thời điểm nào, thì $Z_N$ chấp nhận $w$ trong $2^{c'L(n)}$ bước.
$I_0$ là ID ban đầu của $Z_N$.
$N$ là số nguyên lớn nhất có biểu diễn $m$-adic có thể được lưu trong một thanh ghi.
$x_i$ là nội dung của thanh ghi thứ $i$.
$T_i$ là nội dung của thẻ thứ $i$.

D0 (Khởi tạo). Tính $r$ và thiết lập $r + 1$ thanh ghi và thẻ. Với $i = 1, 2, ..., r$, đặt $x_i \leftarrow 1$ và $T_i \leftarrow 0$. Đặt $x_{r+1} \leftarrow I_0$ (ID ban đầu) và $T_{r+1} \leftarrow 1$.

D1 (Kiểm tra). Nếu mỗi $T_i = 1$, chuyển đến D3. Ngược lại, đặt $j$ là chỉ số nhỏ nhất sao cho $T_j = 0$. Kiểm tra: Với một chỉ số $h$ nào đó, $T_h = 1$ và $x_h \xrightarrow{w} x_j$.
Có: Chuyển đến D2.
Không: Chuyển đến D3.

D2 (Xóa bộ nhớ) ($j$ như trong D1). Nếu $x_j$ là một ID chấp nhận, ACCEPT. Ngược lại, đặt $T_j \leftarrow 1$ và với $i = 1, 2, ..., j - 1$ đặt $x_i \leftarrow 1$ và $T_i \leftarrow 0$. Chuyển đến D1.

D3 (Quay lui). Nếu $x_i = N$ với mỗi $i \leq r$, REJECT. Ngược lại, đặt $k$ là chỉ số nhỏ nhất sao cho $x_k \neq N$. Đặt $x_k \leftarrow x_k + 1$, $T_k \leftarrow 0$, và với $i = 1, 2, ..., k - 1$ đặt $x_i \leftarrow 1$, $T_i \leftarrow 0$. Chuyển đến D1.

Rõ ràng thuật toán hoạt động với bộ nhớ $c''[L(n)]^2$, trong đó $c''$ là một hằng số chỉ phụ thuộc vào $Z_N$. Bằng các kỹ thuật chuẩn [3], hằng số này có thể được giảm xuống còn một. Một phép quy nạp đơn giản theo số bước đã hoàn thành cho thấy rằng nếu $Z_D$ chấp nhận một đầu vào $w$, thì máy không tất định $Z_N$ cũng chấp nhận. Vì vậy, chỉ cần chỉ ra rằng $Z_D$ chấp nhận mọi chuỗi mà $Z_N$ chấp nhận. Để chỉ ra điều này, chúng ta cần một số bổ đề sơ bộ. Các bổ đề dễ phát biểu hơn trong trường hợp máy không dừng khi nó chấp nhận. Vì vậy, giả sử D2 (Xóa bộ nhớ) đã được sửa đổi để bỏ dòng đầu tiên ("If $x_j$ is an accepting ID, ACCEPT"). Ta sẽ nói rằng $Z_D$ đang ở *cấu hình*

$$
\langle x_1, x_2, ..., x_{r+1} \rangle,\quad \langle T_1, T_2, ..., T_{r+1} \rangle
$$

nếu nó sắp thực thi D1, và nội dung của các thanh ghi và các thẻ lần lượt là $x_1, x_2, ..., x_{r+1}$ và $T_1, T_2, ..., T_{r+1}$.

**Bổ đề 1.** (Đối với D2 đã sửa đổi). Với mỗi chỉ số $i (i = 1, 2, ..., r)$ và mỗi số nguyên $x$ ($x = 1, 2, ..., N$), nếu tại một thời điểm nào đó trong một phép tính của $Z_D$ cấu hình của $Z_D$ là {#savitch-1970-tape-lem-1 .statement tag=0401}

$$
\langle \underbrace{1, 1, ..., 1}_{i}, x_{i+1}, x_{i+2}, ..., x_r, I_0 \rangle,\quad \langle \underbrace{0, 0, ..., 0}_{i}, T_{i+1}, T_{i+2}, ..., T_r, 1 \rangle \tag{1}
$$
{#savitch-1970-tape-eq-1 .equation tag=0402}

với một số $x_{i+1}, x_{i+2}, ..., x_r$ và một số $T_{i+1}, T_{i+2}, ..., T_r$, thì tại một thời điểm sau đó cấu hình sẽ là

$$
\langle \underbrace{1, 1, ..., 1}_{i-1}, x, x_{i+1}, x_{i+2}, ..., x_r, I_0 \rangle,\quad \langle \underbrace{0, 0, ..., 0}_{i}, T_{i+1}, T_{i+2}, ..., T_r, 1 \rangle \tag{2}
$$
{#savitch-1970-tape-eq-2 .equation tag=0403}

hoặc

$$
\langle \underbrace{1, 1, ..., 1}_{j-1}, x_j, x_{j+1}, ..., x_r, I_0 \rangle,\quad \langle \underbrace{0, 0, ..., 0}_{j-1}, 1, T_{j+1}, ..., T_r, 1 \rangle, \tag{3}
$$
{#savitch-1970-tape-eq-3 .equation tag=0404}

trong đó $j$ là chỉ số nhỏ nhất trong (1) sao cho $j > i$ và $T_j = 0$. (Nếu không tồn tại $j$ như vậy, thì (2) xảy ra.)

Thuật toán đang cố gắng thiết lập rằng tồn tại một phép tính của $Z_N$ từ ID ban đầu đến $x_j$. Nó cố gắng thực hiện điều này bằng cách chỉ sử dụng các thanh ghi ở bên trái của $x_j$. Vì vậy, bổ đề nói rằng $Z_D$ có thể đưa bất kỳ ID nào vào bất kỳ thanh ghi nào, nếu cần.

*Chứng minh.* Một chứng minh hình thức sẽ sử dụng quy nạp trên $i$ và $x$. Chúng tôi liệt kê một số cấu hình tiêu biểu trong một tính toán. Điều này sẽ làm rõ bổ đề. Lưu ý rằng vì $N$ là một chuỗi mà tất cả các chữ số của nó đều giống nhau, $N$ không phải là một ID và do đó, $x \uparrow_w N$ không đúng với bất kỳ số nguyên $x$ nào. Giả sử $Z_D$ được khởi động trong cấu hình (1) và tại không thời điểm nào sau đó $Z_D$ nhận các cấu hình (3). Khi đó $Z_D$ sẽ nhận các cấu hình sau:

$$
\langle 1, 1, ..., 1, x - 1; x_{i+1}, x_{i+2}, ..., x_r, I_0 \rangle,
$$

$$
\langle 0, 0, ..., 0, T_{i+1}, T_{i+2}, ..., T_r, 1 \rangle
$$

$$
\langle 1, 1, ..., 1, N, x - 1, x_{i+1}, x_{i+2}, ..., x_r, I_0 \rangle,
$$

$$
\langle 0, 0, ..., 0, T_i, T_{i+1}, T_{i+2}, ..., T_r, 1 \rangle
$$

trong đó $T_i = 0$ hoặc 1.

$$
\langle N, N, ..., N, x - 1, x_{i+1}, x_{i+2}, ..., x_r, I_0 \rangle,
$$

$$
\langle 0, 0, ..., 0, T_i, T_{i+1}, T_{i+2}, ..., T_r, 1 \rangle
$$

Cuối cùng, thông qua D3, $Z_D$ nhận (2) như mong muốn.

Bổ đề 2. (Đối với D2 đã sửa đổi). Giả sử tại một thời điểm nào đó trong một tính toán, cấu hình của $Z_D$ là {#savitch-1970-tape-lem-2 .statement tag=0405}

$$
\langle 1, 1, ..., 1, x, x_{j+1}, x_{j+2}, ..., x_r, I_0 \rangle,
$$

$$
\langle 0, 0, ..., 0, T_j, T_{j+1}, T_{j+2}, ..., T_r, 1 \rangle \tag{4}
$$
{#savitch-1970-tape-eq-4 .equation tag=0406}

với $T_j = 0$ và các giá trị bất kỳ cho các $x$ và các $T$ còn lại. Nếu với một chỉ số nào đó $q, T_q = 1$ và có một tính toán của $Z_N$ gồm không quá $2^j$ bước từ $x_q$ đến $x$, thì tại một thời điểm sau đó cấu hình của $Z_D$ sẽ là (4) với $T_j = 1$.

Bổ đề phát biểu rằng $j$ thanh ghi là đủ để $Z_D$ kiểm tra một tính toán gồm $2^j$ bước của $Z_N$.

Bổ đề 3. (Đối với D2 đã sửa đổi). Giả sử tại một thời điểm nào đó trong một tính toán, cấu hình của $Z_D$ là {#savitch-1970-tape-lem-3 .statement tag=0407}

$$
\langle 1, 1, ..., 1, x_j, x_{j+1}, ..., x_{j+p}, x, x_{j+p+2}, ..., x_r, I_0 \rangle,
$$

$$
\langle 0, 0, ..., 0, 1, 1, ..., 1, 0, T_{j+p+2}, T_{j+p+3}, ..., T_r, 1 \rangle \tag{5}
$$
{#savitch-1970-tape-eq-5 .equation tag=0408}

với các giá trị bất kỳ của các $x$ và $T$. Nếu với một chỉ số nào đó $q, T_q = 1$ và có một tính toán của $Z_N$ gồm không quá $2^j$ bước từ $x_q$ đến $x$, thì tại một thời điểm sau đó cấu hình của $Z_D$ sẽ là

$$
\langle 1, 1, ..., 1, x, x_{j+p+2}, x_{j+p+3}, ..., x_r, I_0 \rangle,
$$

$$
\langle 0, 0, ..., 0, 1, T_{j+p+2}, T_{j+p+3}, ..., T_r, 1 \rangle. \tag{6}
$$
{#savitch-1970-tape-eq-6 .equation tag=0409}

Chứng minh của Cả Hai Bổ đề. Bổ đề 2 và 3 về cơ bản là một bổ đề duy nhất và được chứng minh đồng thời bằng quy nạp trên $j$. Trường hợp cơ sở, $j = 1$, là rõ ràng. Giả sử cả hai bổ đề đúng khi $j$ được thay bằng $j - 1$. Chúng tôi sẽ chứng minh rằng Bổ đề 2 đúng với $j$.

Giả sử $Z_D$ đang ở cấu hình (4) với $T_j = 0$ và với một chỉ số nào đó, $q$, có một tính toán của $Z_N$ từ $x_q$ đến $x$ gồm nhiều nhất $2^j$ bước. Phân rã tính toán này từ $x_q$ đến $x$, ta thu được rằng tồn tại một $y$ sao cho có các tính toán gồm nhiều nhất $2^{j-1}$ bước từ $x_q$ đến $y$ và từ $y$ đến $x$. Theo Bổ đề 1, suy ra rằng, tại một thời điểm sau đó, hoặc cấu hình của $Z_D$ là

$$
\langle 1, 1, ..., 1, y, x, x_{j+1}, x_{j+2}, ..., x_r, I_0 \rangle,
$$

$$
\langle 0, 0, ..., 0, T_{j-1}, 0, T_{j+1}, T_{j+2}, ..., T_r, 1 \rangle
$$

với $T_{j-1} = 0$ hoặc cấu hình là (4) với $T_j = 1$. Cấu hình (4) với $T_j = 1$ là kết quả mong muốn. Vì vậy, giả sử $Z_D$ đã nhận cấu hình (7) với $T_{j-1} = 0$. Theo giả thiết quy nạp trên Bổ đề 2, suy ra rằng tại một thời điểm vẫn sau đó nữa, cấu hình của $Z_D$ sẽ là (7) với $T_{j-1} = 1$. Nếu sau đó áp dụng giả thiết quy nạp trên Bổ đề 3, ta thu được rằng tại một thời điểm sau đó nữa, cấu hình của $Z_D$ sẽ là (4) với $T_j = 1$. Vì vậy Bổ đề 2 đúng với $j$. Bổ đề 3 với $j$ được thiết lập theo cách tương tự. Do đó, giả thiết quy nạp được thiết lập và chứng minh của cả hai bổ đề được hoàn thành.

Sử dụng các Bổ đề 1 và 2, ta dễ dàng hoàn thành chứng minh của định lý. Giả sử máy không tất định $Z_N$ chấp nhận $w$. Ta phải chỉ ra rằng $Z_D$ chấp nhận $w$. Vì $Z_N$ chấp nhận $w$, tồn tại một ID chấp nhận, $x$, của $Z_N$ sao cho có một tính toán, với $w$ là đầu vào, gồm nhiều nhất $2^r$ bước từ $I_0$ (ID ban đầu của $Z_N$) đến $x$. Theo Bổ đề 1, suy ra rằng $Z_D$ cuối cùng sẽ nhận cấu hình

$$
\langle 1, 1, ..., 1, x, I_0 \rangle, \quad \langle 0, 0, ..., 0, T_r, 1 \rangle
$$

với $T_r = 0$. Theo Bổ đề 2, suy ra rằng tại một thời điểm sau đó $Z_D$ sẽ nhận cấu hình (8) với $T_r = 1$. Tất cả điều này là đối với D2 đã sửa đổi. D2 chưa sửa đổi sẽ chấp nhận $w$ thay vì đặt $T_r \leftarrow 1$. Điều này hoàn thành chứng minh Định lý 1 trong trường hợp: $L(n)$ đo được.

Nếu $L(n)$ không đo được, thì thuật toán trên phải được thay đổi, vì $Z_D$ không nhất thiết có thể đánh dấu các khối có độ dài $cL(n)$ trong phạm vi bộ nhớ tỷ lệ với $[L(n)]^2$. Tuy nhiên, nếu bằng cách nào đó $Z_D$ được cung cấp giá trị của $L(n)$, thì theo thủ tục trên, $Z_D$ có thể xác định liệu $Z_N$ có chấp nhận đầu vào $w$ trong phạm vi bộ nhớ $L(n)$ hay không. Vì vậy $Z_D$ hoạt động như sau. Đầu tiên $Z_D$ giả sử $L(n) = 1$. Nếu $Z_N$ chấp nhận trong phạm vi bộ nhớ $L(n) = 1$, thì $Z_D$ sẽ chấp nhận. Nếu $Z_N$ không chấp nhận trong phạm vi bộ nhớ 1, thì tiếp theo $Z_D$ giả sử $L(n) = 2$. Nếu $Z_N$ chấp nhận trong phạm vi bộ nhớ 2, thì $Z_D$ chấp nhận. Nếu không, thì tiếp theo $Z_D$ giả sử $L(n) = 3$. $Z_D$ tiếp tục theo cách này bằng cách thử các giá trị ngày càng lớn hơn của $L(n)$. Nếu $Z_N$ chấp nhận đầu vào $w$, thì cuối cùng $Z_D$ sẽ tìm được giá trị đúng của $L(n)$ và chấp nhận $w$ trong phạm vi bộ nhớ tỷ lệ với $[L(n)]^2$. Nếu $Z_N$ không chấp nhận $w$, thì $Z_D$ tính toán vô hạn trên đầu vào $w$. Điều này hoàn thành chứng minh của Định lý 1.

Các ngôn ngữ phụ thuộc ngữ cảnh chính xác là những tập được chấp nhận bởi các máy Turing không tất định trong phạm vi bộ nhớ $L(n) = n$ (xem, ví dụ, [3]). Vì vậy, đặt $L(n) = n$ trong Định lý 1, ta thu được,

Hệ quả 1. Mọi ngôn ngữ phụ thuộc ngữ cảnh đều được chấp nhận bởi một máy Turing tất định nào đó trong phạm vi bộ nhớ $n^2$. {#savitch-1970-tape-cor-1 .statement tag=040A}

Định lý 1 có thể được tổng quát hóa như sau. {#savitch-1970-tape-thm-1-2 .statement tag=040B}

Định lý 2. Nếu một tập, $A$, được chấp nhận bởi một máy Turing không tất định trong phạm vi bộ nhớ $L(n)$ và thời gian $T(n)$, thì $A$ được chấp nhận bởi một máy Turing tất định nào đó trong phạm vi bộ nhớ $L(n) \log_2 T(n)$. {#savitch-1970-tape-thm-2 .statement tag=040C}

Định nghĩa. Một máy Turing, $Z$, được nói là chấp nhận một tập, $A$, trong phạm vi bộ nhớ $L(n)$ và thời gian $T(n)$ với điều kiện rằng

(i) với mỗi $w$ trong $A$, có ít nhất một phép tính của $Z$ chấp nhận $w$, thực hiện không quá $T(n)$ bước, và trong đó mỗi đầu băng làm việc quét không quá $L(n)$ ô, trong đó $n$ là độ dài của $w$, và với điều kiện rằng

(ii) $Z$ chấp nhận không có chuỗi nào không thuộc $A$.

Chứng minh Định lý 2. Phân tích chứng minh của Định lý 1 cho thấy rằng thuật toán sử dụng một cận về bộ nhớ của máy không xác định để thu được một cận, cụ thể là hàm mũ theo bộ nhớ, về thời gian của máy không xác định. Sau đó nó đánh dấu $[\log_2 T(n)]$ khối bộ nhớ, trong đó $T(n)$ là một cận về thời gian. Rõ ràng, nếu cận thời gian dễ tính toán, thuật toán có thể được sửa đổi để sử dụng nó làm cận về thời gian. Khi đó ta sẽ thu được Định lý 2. Nếu hàm thời gian không dễ tính toán, thì ta sử dụng cùng một loại thủ thuật như thủ thuật được dùng cho các hàm không đo được trong chứng minh của Định lý 1.

Hệ quả 2. Nếu một ngôn ngữ phụ thuộc ngữ cảnh được chấp nhận bởi một máy Turing không xác định trong phạm vi bộ nhớ tuyến tính và thời gian đa thức, thì nó được chấp nhận bởi một máy Turing xác định nào đó trong phạm vi bộ nhớ $n \log_2 n$. {#savitch-1970-tape-cor-2 .statement tag=040D}

Định lý sau đây nói rằng đối với mọi hàm bộ nhớ "có tính chất tốt" $L(n)$, nếu mọi máy Turing bị giới hạn băng $L(n)$ không xác định có thể được mô phỏng bởi một máy Turing bị giới hạn băng $L(n)$ xác định, thì đối với mọi hàm bộ nhớ lớn hơn, độ phức tạp băng không xác định và xác định là như nhau.

ĐỊNH LÝ 3. Giả sử rằng $L(n)$ và $H(n)$ là đo được, rằng $L(n)$ là đơn điệu tăng và không bị chặn, và rằng $\log_2 n \leq L(n) \leq H(n)$, với mọi $n$. Gọi hàm $k(n)$ được định nghĩa như sau. Với mỗi số tự nhiên $n$, $k(n)$ là số tự nhiên nhỏ nhất sao cho $H(n) \leq L[k(n)]$.

Giả sử thêm rằng đối với bất kỳ tập hợp nào, $A$, nếu $A$ được chấp nhận bởi một máy Turing không xác định trong phạm vi bộ nhớ $L(n)$, thì $A$ được chấp nhận bởi một máy Turing xác định trong phạm vi bộ nhớ $L(n)$. Khi đó suy ra rằng đối với bất kỳ tập hợp nào, $B$, nếu $B$ được chấp nhận bởi một máy Turing không xác định trong phạm vi bộ nhớ $H(n)$, thì $B$ được chấp nhận bởi một máy Turing xác định trong phạm vi bộ nhớ $L[k(n)]$.

Định lý này mạnh hơn một chút so với vẻ ngoài của nó. Đối với hầu hết các hàm bộ nhớ thông dụng, $L$, tồn tại một hằng số $c$ sao cho $cL[k(n)] \leq H(n) \leq L[k(n)]$, với mọi $H$ và $n$. Vì vậy, trong các trường hợp này, kết luận có thể được củng cố để nói rằng bất kỳ tập hợp nào được chấp nhận trong phạm vi bộ nhớ không xác định $H(n)$ có thể được chấp nhận trong phạm vi bộ nhớ xác định $H(n)$. Cụ thể,

HỆ QUẢ 3. Giả sử $L(n)$ là một đa thức theo $\log_2 n, n$ và $c^n$, với một hằng số $c$ nào đó. Giả sử thêm rằng đối với bất kỳ tập hợp nào, $A$, nếu $A$ được chấp nhận bởi một máy Turing không xác định trong phạm vi bộ nhớ $L(n)$, thì $A$ được chấp nhận bởi một máy Turing xác định nào đó trong phạm vi bộ nhớ $L(n)$.

Khi đó suy ra rằng đối với bất kỳ hàm đo được nào $H(n) \geq L(n)$ và bất kỳ tập hợp nào, $B$, nếu $B$ được chấp nhận bởi một máy Turing không xác định trong phạm vi bộ nhớ $H(n)$, thì $B$ được chấp nhận bởi một máy Turing xác định nào đó trong phạm vi bộ nhớ $H(n)$.

Trong số các điều khác, hệ quả nói rằng nếu mọi ngôn ngữ phụ thuộc ngữ cảnh đều được chấp nhận bởi một ôtômát giới hạn tuyến tính xác định (tức là máy Turing xác định với cận bộ nhớ $n$), thì độ phức tạp băng không xác định và xác định là như nhau đối với mọi cận băng đo được $H(n) \geq n$.

Chứng minh Hệ quả 3. Có thể dễ dàng kiểm tra rằng với mọi đa thức $L(n)$ như vậy, tồn tại một hằng số $c$ sao cho $L(n)/L(n+1) \geq c$ với mọi $n$. Do đó $cL[k(n)] \leq L[k(n)-1]$. $k(n)$ là hàm được định nghĩa trong phát biểu của định lý. Theo định nghĩa của $k(n)$, $L[k(n)-1] \leq H(n)$. Do đó $cL[k(n)] \leq H(n)$.

Giả sử giả thuyết của hệ quả đúng và giả sử $B$ được chấp nhận bởi một máy Turing không tất định trong phạm vi bộ nhớ $H(n)$. Theo Định lý 3, $B$ được chấp nhận bởi một máy Turing tất định trong phạm vi bộ nhớ $L[k(n)]$. Vì vậy, bằng các kỹ thuật rút gọn băng tiêu chuẩn [3], suy ra rằng $B$ được chấp nhận bởi một máy Turing tất định trong phạm vi bộ nhớ $cL[k(n)]$. Cuối cùng, vì $cL[k(n)] \leq H(n)$, điều này có nghĩa là $B$ được chấp nhận bởi một máy Turing tất định trong phạm vi bộ nhớ $H(n)$.

Chứng minh Định lý 3. Giả sử giả thuyết của Định lý 3 đúng và giả sử $B$ là một tập được chấp nhận bởi một máy Turing không tất định, $Z_N^H$, trong phạm vi bộ nhớ $H(n)$.

Chúng tôi sẽ xây dựng một máy tất định, $Z_D^H$, chấp nhận $B$ trong phạm vi bộ nhớ $L[k(n)]$.

Cho $\beta$ là một ký hiệu mới. Cho $A = \{ w\beta^h \mid w \text{ trong } B \text{ và } |w| + h \geq k(|w|) \}$. Một máy Turing không tất định, $Z_N^L$, chấp nhận $A$ trong phạm vi bộ nhớ $L(n)$ có thể được xây dựng như sau. Với đầu vào $w\beta^h$, $Z_N^L$ trước hết đánh dấu $L(n)$ ô của bộ nhớ, trong đó $n = |w\beta^h|$. Sau đó nó kiểm tra xem $L(n) \geq H(|w|)$ hay không. Nếu điều này không đúng, thì $n = |w| + h < k(|w|)$ và tính toán dừng lại. Nếu $L(n) \geq H(|w|)$, thì $Z_N^L$ mô phỏng $Z_N^H$ để xem $w$ có thuộc $B$ hay không. Nếu $Z_N^H$ chấp nhận, thì nó cũng chấp nhận. Vì $L(n) \geq H(|w|)$, máy này sẽ chấp nhận $A$ trong phạm vi bộ nhớ $L(n)$. Vì vậy, theo giả thuyết, tồn tại một máy tất định, $Z_D^L$, chấp nhận $A$ trong phạm vi bộ nhớ $L(n)$. Hơn nữa, vì $L$ là đo được, chúng ta có thể giả sử rằng với mọi đầu vào có độ dài $n$, $Z_D^L$ dừng sau một tính toán trong đó nhiều nhất $L(n)$ ô của băng bộ nhớ được quét. (Các định nghĩa của chúng tôi chỉ yêu cầu điều này khi máy chấp nhận đầu vào.)

Máy tất định, $Z_D^H$, chấp nhận $B$ trong phạm vi bộ nhớ $L[k(n)]$ hoạt động như sau. Với một đầu vào $w$, $Z_D^H$ mô phỏng $Z_D^L$ hoạt động trên $w\beta^h$ với các giá trị khác nhau của $h$. Trước tiên nó thử $h = 0$. Nếu $Z_D^L$ chấp nhận $w$, thì $Z_D^H$ cũng chấp nhận. Nếu không, nó thử $h = 1$. Nếu $Z_D^L$ chấp nhận $w\beta$, thì $Z_D^H$ cũng chấp nhận. Nếu không, nó thử $h = 2$. Nếu $Z_D^L$ chấp nhận $w\beta^2$, thì $Z_D^H$ cũng chấp nhận. Nếu không, nó thử $h = 3$, và cứ tiếp tục như vậy. Nếu $w$ thuộc $B$, thì cuối cùng $Z_D^H$ sẽ tìm thấy giá trị $h$ nhỏ nhất sao cho $|w| + h \geq k(|w|)$ và sẽ chấp nhận $w$ trong phạm vi bộ nhớ $L(|w\beta^h|) = L[k(|w|)]$. Điều này hoàn thành chứng minh của Định lý 3.

Một cách tự nhiên, người ta đặt câu hỏi liệu có hàm bộ nhớ nào mà các lớp độ phức tạp tất định và không tất định của nó bằng nhau hay không. Câu trả lời được đưa ra bởi Manuel Blum và là "có". Blum đã chỉ ra rằng có các hàm bộ nhớ $L(n)$ lớn tùy ý sao cho một tập hợp được chấp nhận trong bộ nhớ tất định $L(n)$ khi và chỉ khi nó được chấp nhận trong bộ nhớ không tất định $L(n)$. Tuy nhiên, các hàm $L(n)$ này không "có tính chất tốt" và Định lý 3 không áp dụng cho chúng. Chúng không đo được. Một phác thảo của chứng minh cho kết quả của Blum xuất hiện trong [8].

Người ta cũng có thể hỏi liệu có một hàm bộ nhớ (đủ lớn để có ý nghĩa) mà các lớp độ phức tạp tất định và không tất định của nó khác nhau hay không. Phần tiếp theo dành cho câu hỏi này. Tuy nhiên, chỉ có một câu trả lời chưa hoàn chỉnh được đưa ra, và câu hỏi vẫn còn bỏ ngỏ.

Mê cung và Máy Turing

Một cách không chính thức, một mê cung là một tập hợp các phòng được nối với nhau bởi các hành lang một chiều. Một số phòng được chỉ định là phòng đích và một phòng được chỉ định là phòng bắt đầu. Do đó, một mê cung là một đồ thị có hướng với một số nút hoặc phòng được phân biệt. Mê cung có thể luồn qua được nếu có một đường đi từ phòng bắt đầu đến một phòng đích nào đó.

Một máy Turing không tất định, với đầu vào $w$, tạo ra một mê cung theo một cách tự nhiên. Các phòng của mê cung là các mô tả tức thời của máy và các hành lang được cho bởi hàm chuyển của máy. Nghĩa là có một hành lang từ phòng $I_1$ đến phòng $I_2$ nếu, với đầu vào $w$, máy có thể trong một bước thay đổi cấu hình của nó từ $I_1$ sang $I_2$. Mô tả tức thời ban đầu của máy được chỉ định là phòng bắt đầu. Những mô tả tức thời bao gồm một trạng thái chấp nhận được chỉ định là các phòng đích. Máy sẽ chấp nhận đầu vào $w$ khi và chỉ khi mê cung tương ứng có thể luồn qua được.

Thuật toán mô phỏng một máy Turing không tất định, được đưa ra trong phần trước, thực sự là một phương pháp hiệu quả để xác định liệu mê cung tương ứng có thể luồn qua được hay không. Trong phần này, chúng tôi chỉ ra rằng nếu có thể tìm được một phương pháp đủ hiệu quả để "luồn qua" các mê cung, thì các máy tất định có thể mô phỏng các máy không tất định với cùng một bộ nhớ. Chính xác hơn, tập hợp các mê cung có thể luồn qua được, được mã hóa thích hợp, có thể được nhận biết bởi một máy Turing không tất định trong phạm vi bộ nhớ $\log_2 n$. Tập hợp này có thể được nhận biết bởi một máy Turing tất định nào đó trong phạm vi bộ nhớ $\log_2 n$ khi và chỉ khi các máy Turing bị chặn bởi băng $L(n)$ tất định có thể mô phỏng các máy Turing bị chặn bởi băng $L(n)$ không tất định, với mọi $L(n) \geq \log_2 n$.

Định nghĩa. Một mê cung trên $\Sigma$ (một bảng chữ cái hữu hạn) là một bộ bốn, $\mathcal{M} = (X, R, s, G)$, trong đó $X$ là một tập hữu hạn các chuỗi trên $\Sigma$ ($X$ là tập các phòng), $R$ là một quan hệ nhị phân trên $X$ (cho các hành lang), $s$ là một phần tử của $X$ ($s$ là phòng bắt đầu), và $G$ là một tập con của $X$ ($G$ là tập các phòng đích).

Định nghĩa. Mê cung $\mathcal{M} = (X, R, s, G)$ là có thể luồn được nếu có một chuỗi $r_1, r_2, ..., r_e$ các phòng sao cho $r_1 = s$ (phòng bắt đầu), $r_e$ là một phần tử của $G$ (các phòng đích), và $R(r_i, r_{i+1})$ đúng với $i = 1, 2, ..., e - 1$.

Định nghĩa. Gọi ], [,* là ba ký hiệu mới. Một mã hóa của mê cung $\mathcal{M} = (X, R, s, G)$ là một chuỗi có dạng

$$
s[x_1 * y_1^1 * y_2^1 * \cdots y_{n(1)}^1][x_2 * y_1^2 * y_2^2 * \cdots * y_{n(2)}^2]
$$

$$
\cdots [x_l * y_1^l * \cdots y_{n(l)}^l] u_1 * u_2 * \cdots u_g
$$

trong đó $s$ là phòng bắt đầu của $\mathcal{M}$; $x_1, x_2, ..., x_l$ là một phép liệt kê không lặp lại các phòng trong $X$; với $1 \leq i \leq l$, $y_1^i, y_2^i, ..., y_{n(i)}^i$ là một phép liệt kê không lặp lại của tất cả các $y$ trong $X$ sao cho $R(x_i, y)$ đúng; và $u_1, u_2, ..., u_g$ là một phép liệt kê không lặp lại các phòng trong $G$.

Ký hiệu. $M_\Sigma$ biểu diễn tập hợp tất cả các mã hóa của các mê cung có thể luồn được trên $\Sigma$.

Định lý 4. Với mọi bảng chữ cái hữu hạn $\Sigma$, tồn tại một máy Turing không tất định chấp nhận $M_\Sigma$ trong giới hạn bộ nhớ $\log_2 n$. {#savitch-1970-tape-thm-4 .statement tag=040E}

Chứng minh. Nếu mê cung có độ dài $n$, thì nó có nhiều nhất $n$ phòng. Vì vậy mỗi phòng có thể được mã hóa bởi một số có thể được lưu trữ trong $\log_2 n$ ô băng. Cụ thể hơn, nếu mê cung được cho bởi (1), thì phòng $x_i$ được mã hóa bởi số $i$ trong ký pháp nhị phân. Thuật toán rất đơn giản. Máy ghi số mã của phòng ban đầu lên băng làm việc, tìm các phòng kế tiếp có thể có, đoán một trong số chúng, xóa băng làm việc, và ghi một mã hóa của phỏng đoán của nó. Sau đó nó tìm các phòng kế tiếp có thể có, đoán một trong số chúng, và cứ tiếp tục như vậy. Sau mỗi lần đoán nó kiểm tra xem đã đến một phòng đích hay chưa. Nếu đã đến, nó chấp nhận. Rõ ràng băng làm việc sẽ bị giới hạn bởi $c \log_2 n$, với một hằng số $c$ nào đó.

Một lập luận dãy giao cắt trực tiếp, giống như lập luận của Cobham [2], cho thấy rằng cận $\log_2 n$ trong Định lý 4 là tốt nhất có thể, sai khác không quá một hệ số hằng số.

Áp dụng các Định lý 1 và 4 cho $M_\Sigma$ thu được

Hệ quả 4. Với mọi bảng chữ cái hữu hạn $\Sigma$, tồn tại một máy Turing tất định chấp nhận $M_\Sigma$ trong giới hạn bộ nhớ $(\log_2 n)^2$. {#savitch-1970-tape-cor-4 .statement tag=040F}

Bổ đề 4. Với mọi bảng chữ cái hữu hạn $\Sigma$ và $\Delta$ có ít nhất hai phần tử, $M_\Sigma$ được chấp nhận bởi một máy Turing tất định nào đó trong giới hạn bộ nhớ $\log_2 n$ khi và chỉ khi $M_\Delta$ được như vậy. {#savitch-1970-tape-lem-4 .statement tag=0410}

Chứng minh. Với mọi mã hóa, $w$, của một mê cung trên $\Sigma$, tồn tại một mã hóa, $\delta(w)$, của một mê cung trên $\Delta$ đẳng cấu với $w$. Vì vậy $w$ thuộc $M_\Sigma$ khi và chỉ khi $\delta(w)$ thuộc $M_\Delta$. Cụ thể hơn, nếu $w$ là

$$
s[x_1 * y_1^1 * y_2^1 * \cdots y_{n(1)}^1][x_2 * y_1^2 * y_2^2 * \cdots * y_{n(2)}^2]
$$

$$
\cdots [x_l * y_1^l * \cdots y_{n(l)}^l] u_1 * u_2 * \cdots u_g
$$

thì $\delta(w)$ có thể được lấy là

$$
\delta(s)[\delta(x_1) * \delta(y_1^1) * \delta(y_2^1) * \cdots \delta(y_{n(1)}^1)][\delta(x_2) * \delta(y_1^2) * \delta(y_2^2) * \cdots * \delta(y_{n(2)}^2)]
$$

$$
\cdots [\delta(x_l) * \delta(y_1^l) * \cdots \delta(y_{n(l)}^l)] \delta(u_1) * \delta(u_2) * \cdots \delta(u_g)
$$

trong đó nếu $k$ là số ký hiệu trong $\Delta$, thì $\delta(x_i)$ là biểu diễn $k$-phân của số $i$ và do đó là một phần tử của $\Delta^*$. Vì các $u$ và $y$ và $s$ đều bằng một số $x_i$ nào đó, điều này cũng xác định $\delta$ trên chúng.

Cho một máy tất định, $Z_\Delta$, chấp nhận $M_\Delta$ trong phạm vi bộ nhớ $\log_2 n$, ta xây dựng một máy tất định, $Z_\Sigma$, chấp nhận $M_\Sigma$ trong phạm vi bộ nhớ $\log_2 n$, như sau. Với một đầu vào $w$, $Z_\Sigma$ hoạt động bằng cách mô phỏng $Z_\Delta$ hoạt động trên $\delta(w)$. Cụ thể hơn, giả sử $Z_\Sigma$ có đầu vào $w$ như trong (1). Khi $Z_\Sigma$ đang mô phỏng $Z_\Delta$ với đầu đọc đầu vào của $Z_\Delta$ đang ở một vị trí nào đó trong $\delta(z)$, trong đó $z$ là một trong $s, x, y,$ hoặc $u$ nào đó trong (1), thì $Z_\Sigma$ sẽ có đầu đọc đầu vào của nó đọc ký hiệu đầu tiên của $z$ và sẽ có $\delta(z)$ được ghi trên một băng lưu trữ phụ. $Z_{\Sigma}$ sử dụng băng lưu trữ phụ này chứa $\delta(z)$ để mô phỏng băng đầu vào của $Z_{\Delta}$. Khi, trong quá trình mô phỏng, đầu đọc đầu vào của $Z_{\Delta}$ sẽ rời khỏi đầu bên trái (tương ứng, bên phải) của $\delta(z)$, thì $Z_{\Sigma}$ di chuyển đầu đọc đầu vào của nó tới $s, x, y,$ hoặc $u$ ở bên trái (tương ứng, bên phải) của $z$, tính $\delta$ của $s, x, y,$ hoặc $u$ này và thay thế $\delta(z)$ bằng $\delta$ của $s, x, y,$ hoặc $u$ này. $\delta$ của $s, x, y,$ hoặc $u$ này trở thành $\delta(z)$ mới và quá trình mô phỏng tiếp tục. Để tính $\delta(z)$ mới, $Z_{\Sigma}$ chỉ cần so sánh $z$ mới với từng $x_i$ cho đến khi tìm thấy $x_i$ bằng với $z$. Nó có thể thực hiện điều này từng ký hiệu một và do đó giữ lượng băng lưu trữ được sử dụng nhỏ hơn $c \log_2 n$, với một hằng số $c$ nào đó.

Vì $\Sigma$ và $\Delta$ là đối xứng trong phát biểu của bổ đề, điều này đủ để chứng minh bổ đề.

Định lý 5. Với mọi bảng chữ cái hữu hạn, $\Sigma$, có ít nhất hai phần tử, các phát biểu sau là tương đương: {#savitch-1970-tape-thm-5 .statement tag=0411}

(1) $M_{\Sigma}$ được chấp nhận bởi một máy Turing tất định nào đó trong phạm vi bộ nhớ $\log_2 n$.

(2) Với mọi bảng chữ cái hữu hạn $\Gamma$, mọi tập, $A$, các chuỗi trên $\Gamma$ và mọi hàm $L(n) \geq \log_2 n$, nếu $A$ được chấp nhận bởi một máy Turing không tất định trong bộ nhớ $L(n)$, thì $A$ được chấp nhận bởi một máy Turing tất định nào đó trong bộ nhớ $L(n)$.

Chứng minh. Phát biểu (1) suy ra từ phát biểu (2) theo Định lý 4.

Giả sử (1) đúng và $A$ là một tập được chấp nhận bởi một máy Turing không tất định nào đó, $Z_N$, trong bộ nhớ $L(n) \geq \log_2 n$. Chúng tôi sẽ xây dựng một máy tất định, $Z_D$, chấp nhận $A$ với cùng cận bộ nhớ $L(n)$. Giả sử $L(n)$ đo được. Sau này chúng tôi sẽ chỉ ra cách loại bỏ hạn chế này. Với mỗi chuỗi $w$ trên bảng chữ cái đầu vào của $Z_N$, gắn với mê cung $\mathcal{M}(w) = (X, R, s, G)$, trong đó $X$ là tập tất cả các ID's của $Z_N$ mà phần không trắng của mỗi băng công tác có độ dài nhiều nhất là $L(|w|)$, $s$ là ID khởi đầu của $Z_N$, $G$ là tập các ID's trong $X$ có chứa một trạng thái chấp nhận, và $R$ được định nghĩa bởi: $R(x, y)$ đúng khi và chỉ khi $x \xrightarrow{w} y$. Rõ ràng, $Z_N$ chấp nhận $w$ khi và chỉ khi $\mathcal{M}(w)$ có thể xâu luồn. Gọi $m(w)$ là một mã hóa của mê cung $\mathcal{M}(w)$. Máy tất định $Z_D$ chấp nhận $A$ hoạt động như sau. Với một đầu vào $w$, $Z_D$ xây dựng $m(w)$ trên một trong các băng lưu trữ của nó, rồi mô phỏng máy trong phát biểu (1) để xác định liệu $m(w)$ có thuộc $M_{\Sigma}$ hay không. Nếu có, thì $Z_D$ chấp nhận $w$. Theo Bổ đề 4, ta có thể giả sử $\Sigma$ đủ lớn để tất cả ID's của $Z_N$ đều là các chuỗi trên $\Sigma$. Vì vậy $m(w)$ thuộc $M_{\Sigma}$ khi và chỉ khi $Z_N$ chấp nhận $w$. Do đó, $Z_D$ chấp nhận chính xác tập $A$. $m(w)$ có độ dài nhiều nhất là $h^{L(n)}$, trong đó $n = |w|$ và $h$ là một hằng số chỉ phụ thuộc vào $Z_N$. Ngoại trừ băng được dùng để lưu trữ $m(w)$, $Z_D$ hoạt động với bộ nhớ $\log_2 h^{L(n)}$ tỉ lệ với $L(n)$.

Máy $Z_D$ không thể viết ra toàn bộ chuỗi, $m(w)$, cùng một lúc mà vẫn hoạt động trong phạm vi bộ nhớ được cấp phát. Tuy nhiên, tất cả những gì cần thiết để mô phỏng máy trong phát biểu (1) là $Z_D$ có thể tính toán từng ký hiệu một của chuỗi $m(w)$ và theo dõi vị trí của các ký hiệu trong $m(w)$. Nó có thể làm được điều này nếu, trong phạm vi bộ nhớ $L(n)$, nó có thể sinh ra $m(w)$, từ phải sang trái, từng ký hiệu một.

Các nhận xét của chúng tôi cho đến nay áp dụng cho bất kỳ mã hóa $m(w)$ nào của mê cung $\mathcal{M}(w)$. Bây giờ chúng tôi cố định $m(w)$ là mã hóa sau đây của mê cung $\mathcal{M}(w)$

$$
s[x_1 * y_1^1 * y_2^1 * \cdots y_{n(1)}^1][x_2 * y_1^2 * y_2^2 * \cdots * y_{n(2)}^2]
$$

$$
\cdots [x_l * y_1^l * \cdots y_{n(l)}^l] u_1 * u_2 * \cdots u_g
$$

trong đó $x_1 < x_2 < x_3 < \cdots < x_l$ với mỗi $i = 1, 2, \ldots, l$, $y_1^i < y_2^i < y_3^i < \cdots < y_{n(i)}^i$ và $u_1 < u_2 < \cdots < u_g . <$ là thứ tự "nhỏ hơn" thông thường trên các số tự nhiên. Các $x$'s, $y$'s, và $u$'s là các chuỗi trên một bảng chữ cái hữu hạn và do đó có thể được xem như các số trong ký hiệu $k$-adic, với một $k$ nào đó. Theo định nghĩa của $\mathcal{M}(w)$, các $x$'s, $y$'s, $u$'s, và $s$ là các ID của $Z_N$ có độ dài nhỏ hơn $cL(n)$, trong đó $c$ là một hằng số chỉ phụ thuộc vào $Z_N$. $Z_D$ có thể tạo ra $m(w)$ ký hiệu từng ký hiệu một, trong bộ nhớ được cấp phát, như sau. $Z_D$ có thể dễ dàng tính $s$, ID ban đầu của $Z_N$. Sau khi tạo ra $s$, $Z_D$ tiếp theo duyệt theo thứ tự số tất cả các chuỗi có độ dài nhỏ hơn $cL(n)$ cho đến khi tìm thấy một chuỗi là một ID của $Z_N$. Đây sẽ là $x_1$. Như vậy $Z_D$ đã tạo ra $x_1$. Tiếp theo nó tạo ra tất cả các $y$ sao cho $x_1 \xrightarrow{w} y$. Theo cách này, nó tạo ra các $y_j^1$. Tiếp theo nó duyệt theo thứ tự số tất cả các chuỗi có độ dài nhỏ hơn $cL(n)$ cho đến khi tìm thấy chuỗi đầu tiên như vậy là một ID của $Z_N$ và lớn hơn $x_1$. Đây là $x_2$. Bây giờ nó có thể xóa $x_1$. Điều duy nhất nó cần giữ trong bộ nhớ tại thời điểm này là $x_2$. $Z_D$ sau đó tiếp tục tạo ra các $y_j^2$. Nó tạo ra $x_3$ từ $x_2$ theo cùng cách mà nó đã tính $x_2$ từ $x_1$. Nó tiếp tục theo cách này cho đến khi tìm thấy $x_i$ lớn nhất. Sau khi đã tạo ra $x_i$ lớn nhất và các $y$ tương ứng của nó, nó tiếp tục tạo ra các $u_i$ như sau. Nó duyệt qua tất cả các chuỗi có độ dài nhiều nhất là $cL(n)$ và kiểm tra xem những chuỗi nào là các ID có chứa một trạng thái chấp nhận. Những chuỗi đó là các $u_i$. Điều này hoàn tất quá trình tạo và chứng minh cho trường hợp: $L(n)$ là đo được.

Nếu $L(n)$ không đo được, thì $Z_D$ không nhất thiết có thể sinh chính xác các chuỗi có độ dài nhỏ hơn $cL(n)$ trong phạm vi bộ nhớ tỷ lệ với $L(n)$ và do đó thủ tục trên sẽ không hoạt động. Tuy nhiên, nếu bằng cách nào đó $Z_D$ được cung cấp giá trị của $L(n)$, thì theo thủ tục trên nó có thể xác định liệu $w$ có được $Z_N$ chấp nhận hay không trong phạm vi bộ nhớ $L(n)$. $Z_D$ sử dụng cùng loại thủ thuật đã được sử dụng cho các hàm không đo được trong chứng minh của Định lý 1. Nghĩa là, trước tiên nó giả sử $L(n) = 1$. Nếu $Z_N$ chấp nhận đầu vào $w$ trong phạm vi bộ nhớ $L(n) = 1$, thì $Z_D$ chấp nhận $w$. Nếu không, $Z_D$ tiếp theo thử $L(n) = 2$. Nếu $Z_N$ chấp nhận trong phạm vi bộ nhớ $L(n) = 2$, thì $Z_D$ cũng làm như vậy. Nếu không, $Z_D$ tiếp theo thử $L(n) = 3$, và cứ tiếp tục như vậy. Nếu $Z_N$ chấp nhận đầu vào $w$, thì cuối cùng $Z_D$ sẽ tìm được giá trị đúng của $L(n)$ và chấp nhận $w$ trong phạm vi bộ nhớ tỷ lệ với $L(n)$.

Một vấn đề chưa được giải quyết trong lý thuyết độ phức tạp băng là liệu có tồn tại một tập $A$ gồm các chuỗi và một hàm $L(n) \geq \log_2 n$ nào đó sao cho $A$ được một máy Turing không tất định chấp nhận trong phạm vi bộ nhớ $L(n)$ nhưng không được bất kỳ máy Turing tất định nào chấp nhận trong phạm vi bộ nhớ $L(n)$ hay không. Định lý 5 chỉ ra rằng nếu tồn tại bất kỳ $A$ và $L(n)$ như vậy, thì $A = M_\Sigma$ và $L(n) = \log_2 n$ sẽ thỏa mãn.

SAVITCH
