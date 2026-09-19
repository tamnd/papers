---
paper: ford-1956-maxflow
title: Maximal Flow Through a Network
authors:
  - L. R. Ford Jr.
  - D. R. Fulkerson
year: 1956
venue: Canadian Journal of Mathematics
field: algorithms
section_title: L. R. Ford, Jr. và D. R. Fulkerson
kind: section
lang: vi
source: https://www.cs.yale.edu/homes/lans/readings/routing/ford-max_flow-1956.pdf
pdf_sha256: ad378e3c07842a685e94f4cd4c2a18ae2fabe4d39a65338afd896fb069b394a1
pdf_pages: 1-6
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 7bd6275a68436d463ad6dc4149a97eaa5e7bbfcba57d581f296223b46537f4db
translated_from: content/en/ford-1956-maxflow/01_l_r_ford_jr_and_d_r_fulkerson.md
source_content_sha256: 909c66bc21c54753dc872fe95adfefffbd41c172d18fc67ffbcf23fa8eb10b4f
translation_model: gpt-5
translation_run: 20260919T113512Z
glossary_version: 7
glossary_terms_sha256: d4043ebd5a5c828b0239f76956644bfb5bb815f3188dc3282d75521c97669214
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Nhập đề. Bài toán được thảo luận trong bài báo này được T. Harris xây dựng như sau:
"Hãy xét một mạng đường sắt nối hai thành phố thông qua một số thành phố trung gian, trong đó mỗi liên kết của mạng có một số được gán cho nó biểu diễn khả năng của nó. Giả sử điều kiện trạng thái ổn định, hãy tìm một luồng cực đại từ một thành phố đã cho đến thành phố kia."
Mặc dù bài toán này có thể được thiết lập như một bài toán quy hoạch tuyến tính với số phương trình bằng số thành phố trong mạng, và do đó có thể được giải bằng phương pháp simplex (1), nhưng hóa ra trong các trường hợp có ý nghĩa thực tiễn nhất, khi mạng là phẳng theo một nghĩa hạn chế nhất định, có thể mô tả một thủ tục tính toán bằng tay đơn giản hơn nhiều và hiệu quả hơn.
Trong §1 chúng tôi chứng minh định lý lát cắt tối thiểu, thiết lập rằng một cận trên hiển nhiên đối với các luồng trên một mạng tùy ý luôn có thể đạt được. Chứng minh là không kiến tạo. Tuy nhiên, bằng cách chuyên biệt hóa mạng (§2), chúng tôi thu được như một hệ quả của định lý lát cắt tối thiểu một lược đồ tính toán hiệu quả. Cuối cùng, trong §3 chúng tôi quan sát tính đối ngẫu giữa bài toán khả năng và bài toán tìm đường đi ngắn nhất, thông qua một mạng, giữa hai điểm đã cho.

1. Định lý lát cắt tối thiểu. Một đồ thị G là một phức hữu hạn, 1 chiều, được tạo thành từ các đỉnh $a, b, c, \ldots, e$, và các cung $\alpha(ab), \beta(ac), \ldots, \delta(ce)$. Một cung $\alpha(ab)$ nối các đỉnh đầu mút của nó $a, b$; nó đi qua không có đỉnh nào khác của $G$ và giao với các cung khác chỉ tại các đỉnh. Một chuỗi là một tập hợp các cung khác nhau của $G$ có thể được sắp xếp thành $\alpha(ab), \beta(bc), \gamma(cd), \ldots, \delta(gh)$, trong đó các đỉnh $a, b, c, \ldots, h$ là khác nhau, tức là, một chuỗi không tự giao nhau; một chuỗi nối các đỉnh đầu mút $a$ và $h$ của nó.
Chúng tôi phân biệt hai đỉnh của $G$: $a$, nguồn, và $b$, đích.$^1$ Một luồng chuỗi từ $a$ đến $b$ là một cặp $(C; k)$ bao gồm một chuỗi $C$ nối $a$ và $b$, và một số không âm $k$ biểu diễn luồng dọc theo $C$ từ nguồn đến đích.
Mỗi cung trong $G$ được gắn với một số dương được gọi là khả năng của nó. Chúng tôi gọi đồ thị $G$, cùng với các khả năng của từng cung riêng lẻ, là một mạng. Một luồng trong một mạng là một tập hợp các luồng chuỗi có tính chất rằng tổng các số của tất cả các luồng chuỗi chứa bất kỳ cung nào không lớn hơn khả năng của cung đó. Nếu đẳng thức xảy ra, chúng tôi nói cung đó được bão hòa bởi luồng. Một chuỗi được bão hòa đối với một luồng nếu nó chứa

Nhận ngày 20 tháng 9, 1955.

$^1$Trường hợp có nhiều nguồn và đích với việc vận chuyển được cho phép từ bất kỳ nguồn nào đến bất kỳ đích nào rõ ràng có thể quy về trường hợp này.

một cung được bão hòa. Giá trị của một luồng là tổng các số của tất cả các luồng chuỗi tạo thành nó.

Rõ ràng rằng định nghĩa luồng ở trên không đủ rộng để bao gồm mọi thứ mà trực giác người ta muốn xem là một luồng, ví dụ, gửi các đoàn tàu ra một ngõ cụt rồi quay lại hoặc chạy quanh một mạch, nhưng xét về vận tải hiệu quả thì định nghĩa được đưa ra là đủ.

Một tập hợp ngắt kết nối là một tập hợp các cung có tính chất rằng mọi chuỗi nối $a$ và $b$ đều gặp tập hợp đó. Một tập hợp ngắt kết nối mà không có tập con thực sự nào của nó là ngắt kết nối được gọi là một lát cắt. Giá trị của một tập hợp ngắt kết nối $D$ (được viết là $v(D)$) là tổng các khả năng của các phần tử riêng lẻ của nó. Do đó một tập hợp ngắt kết nối có giá trị tối thiểu tự động là một lát cắt.

Định lý 1. (Định lý lát cắt tối thiểu). *Giá trị luồng cực đại có thể thu được trong một mạng $N$ là giá trị nhỏ nhất của $v(D)$ lấy trên tất cả các tập hợp ngắt kết nối $D$.* {#ford-1956-maxflow-thm-1 .statement tag=031D}

*Chứng minh.* Chỉ có hữu hạn chuỗi nối $a$ và $b$, giả sử có $n$ chuỗi. Nếu chúng ta liên kết với mỗi chuỗi một tọa độ trong không gian $n$ chiều, thì một luồng có thể được biểu diễn bởi một điểm mà tọa độ thứ $j$ của nó là số gắn với luồng chuỗi dọc theo chuỗi thứ $j$. Với biểu diễn này, lớp tất cả các luồng là một đa diện lồi đóng trong không gian $n$ chiều, và giá trị của một luồng là một phiếm hàm tuyến tính trên đa diện này. Vì vậy, tồn tại một luồng cực đại, và tập hợp tất cả các luồng cực đại là lồi.

Bây giờ gọi $S$ là lớp tất cả các cung được bão hòa trong mọi luồng cực đại.

Bổ đề 1. *$S$ là một tập hợp ngắt kết nối.* {#ford-1956-maxflow-lem-1 .statement tag=031E}

Giả sử không phải vậy. Khi đó tồn tại một chuỗi $\alpha_1, \alpha_2, \ldots, \alpha_m$ nối $a$ và $b$ với $\alpha_i \notin S$ đối với mỗi $i$. Do đó, tương ứng với mỗi $\alpha_i$, tồn tại một luồng cực đại $f_i$ trong đó $\alpha_i$ không được bão hòa. Nhưng trung bình của các luồng này,

$$
f = \frac{1}{m} \sum f_i,
$$

là cực đại và $\alpha_i$ không được bão hòa bởi $f$ đối với mỗi $i$. Vì vậy giá trị của $f$ có thể được tăng lên bằng cách áp đặt một luồng chuỗi lớn hơn trên $\alpha_1, \alpha_2, \ldots, \alpha_m$, mâu thuẫn với tính cực đại.

Lưu ý rằng hướng được gán cho một cung của $S$ bởi một luồng chuỗi dương của một luồng cực đại là giống nhau đối với tất cả các luồng chuỗi như vậy. Thật vậy, trước hết giả sử rằng $(C_1, k_1), (C_2, k_2)$ là hai luồng chuỗi xuất hiện trong một luồng cực đại $f, k_1 \geq k_2 > 0$, trong đó

$$
C_1 = \alpha_1(a a_1), \alpha_2(a_1 a_2), \ldots, \alpha_j(a_{j-1}, a_j), \ldots, \alpha_r(a_{r-1}, b)
$$

$$
C_2 = \beta_1(a b_1), \beta_2(b_1 b_2), \ldots, \beta_k(b_{k-1}, b_k), \ldots, \beta_s(b_{s-1}, b),
$$

và $\alpha_j(a_{j-1}, a_j) = \beta_k(b_{k-1}, b_k) \in S, a_{j-1} = b_k, a_j = b_{k-1}$. Khi đó

$$
C'_1 = \alpha_1, \alpha_2, \ldots, \alpha_{j-1}, \beta_{k+1}, \ldots, \beta_s
$$

$$
C'_2 = \beta_1, \beta_2, \ldots, \beta_{k-1}, \alpha_{j+1}, \ldots, \alpha_r
$$

chứa các chuỗi $C_1''$, $C_2''$ nối $a$ và $b$, và một luồng cực đại khác có thể thu được từ $f$ như sau. Giảm các thành phần $C_1$ và $C_2$ của $f$ mỗi thành phần một lượng $k_2$, và tăng mỗi thành phần $C_1''$ và $C_2''$ một lượng $k_2$. Điều này làm mất bão hòa cung $\alpha_j$, mâu thuẫn với định nghĩa của nó như một phần tử của $S$. Mặt khác, nếu $(C_1, k_1), (C_2, k_2)$ là các thành viên của các luồng cực đại khác nhau $f_1, f_2$, việc xét $f = \frac{1}{2}(f_1 + f_2)$ đưa chúng ta trở lại trường hợp trước. Do đó, các cung của $S$ có một hướng xác định được gán cho chúng bởi các luồng cực đại. Chúng tôi gọi đỉnh của một cung $\alpha \in S$ xuất hiện đầu tiên trong một luồng chuỗi dương của một luồng cực đại là đỉnh trái của $\alpha$.

Bây giờ định nghĩa một cung trái của $S$ như sau: một cung $\alpha$ của $S$ là một cung trái khi và chỉ khi tồn tại một luồng cực đại $f$ và một chuỗi $\alpha_1, \alpha_2, \ldots, \alpha_k$ (có thể rỗng) nối $a$ và đỉnh trái của $\alpha$ mà không có $\alpha_i$ nào bị bão hòa bởi $f$. Gọi $L$ là tập các cung trái của $S$.

Bổ đề 2. $L$ là một tập phân tách. {#ford-1956-maxflow-lem-2 .statement tag=031F}

Cho một chuỗi bất kỳ $\alpha_1(a\ a_1), \alpha_2(a_1a_2), \ldots, \alpha_m(a_{m-1}\ b)$ nối $a$ và $b$, nó phải giao với $S$ theo Bổ đề 1. Gọi $\alpha_t(a_{t-1}, a_t)$ là $\alpha_i \in S$ đầu tiên. Khi đó với mỗi $\alpha_i, i < t$, tồn tại một luồng cực đại $f_i$ trong đó $\alpha_i$ không bị bão hòa. Trung bình của các luồng này cung cấp một luồng cực đại $f$ trong đó $\alpha_1, \alpha_2, \ldots, \alpha_{t-1}$ không bị bão hòa. Còn lại cần chứng minh rằng chuỗi này nối $a$ với đỉnh trái của $\alpha_t$, tức là $a_{t-1}$ là đỉnh trái của $\alpha_t$. Giả sử không đúng. Khi đó luồng cực đại $f$ chứa một luồng chuỗi

$$
[\beta_1(ab_1), \beta_2(b_1, b_2), \ldots, \beta_r(b_{r-1}, b); k],\ k > 0,\ \beta_s = \alpha_t,\ b_{s-1} = a_t,\ b_s = a_{t-1}.
$$

Lượng không bão hòa trong $f$ của $\alpha_i \ (i = 1, \ldots, t - 1)$ là $k_i > 0$. Bây giờ thay đổi $f$ như sau: giảm luồng dọc theo chuỗi $\beta_1, \beta_2, \ldots, \beta_r$ đi $\min[k, k_i] > 0$ và tăng luồng dọc theo chuỗi chứa trong

$$
\alpha_1, \alpha_2, \ldots, \alpha_{t-1}, \beta_{s+1}, \ldots, \beta_r
$$

một lượng như vậy. Kết quả là một luồng cực đại trong đó $\alpha_t$ không bão hòa, một mâu thuẫn. Do đó $\alpha_t \in L$.

Bổ đề 3. Không có luồng chuỗi dương nào của một luồng cực đại có thể chứa nhiều hơn một cung của $L$. {#ford-1956-maxflow-lem-3 .statement tag=0320}

Giả sử điều ngược lại, tức là tồn tại một luồng cực đại $f_1$ chứa một luồng chuỗi

$$
[\beta_1(ab_1), \beta_2(b_1b_2), \ldots, \beta_r(b_{r-1}, b); k],\ k > 0,
$$

với các cung $\beta_i, \beta_j \in L, \beta_i$ xuất hiện trước $\beta_j$, chẳng hạn, trong chuỗi. Gọi $f_2$ là luồng cực đại sao cho có một chuỗi không bão hòa

$$
\alpha_1(aa_1),\ \alpha_2(a_1, a_2), \ldots, \alpha_s(a_{s-1}, b_{j-1})
$$

từ $a$ đến nút bên trái của $\beta_j$. Xét $f = \frac{1}{2}(f_1 + f_2)$. Luồng cực đại này chứa luồng chuỗi $[\beta_1, \beta_2, \ldots, \beta_r; k']$ với $k' \geq \frac{1}{2}k$, và mỗi $\alpha_i (i = 1, \ldots, s)$ không bão hòa một lượng $k_i > 0$ trong $f$. Một lần nữa thay đổi $f$: giảm luồng dọc theo

$\beta_1, \beta_2, \ldots, \beta_r$ đi min $[k', k_i] > 0$ và tăng luồng dọc theo chuỗi chứa trong $\alpha_1, \alpha_2, \ldots, \alpha_s, \beta_j, \ldots, \beta_r$ cùng một lượng, thu được một luồng cực đại trong đó $\beta_i$ không bão hòa, một mâu thuẫn.

Bây giờ để chứng minh định lý, chỉ cần nhận xét rằng giá trị của mọi luồng không lớn hơn $v(D)$ trong đó $D$ là bất kỳ tập phân tách nào; và mặt khác từ Bổ đề 3 và định nghĩa của $S$ ta thấy rằng khi cộng các khả năng của các cung của $L$, ta đã tính mỗi luồng chuỗi của một luồng cực đại đúng một lần. Vì theo Bổ đề 2 $L$ là một tập phân tách, ta có bất đẳng thức ngược lại. Do đó $L$ là một lát cắt tối thiểu và giá trị của một luồng cực đại là $v(L)$.

Chúng tôi sẽ gọi giá trị của một luồng cực đại qua một mạng $N$ là khả năng của $N$ ($\operatorname{cap}(N)$). Khi đó chú ý đến hệ quả sau của định lý lát cắt tối thiểu.

Hệ quả. *Cho $A$ là một tập hợp các cung của một mạng $N$ sao cho nó gặp mỗi lát cắt của $N$ chỉ tại một cung. Nếu $N'$ là một mạng thu được từ $N$ bằng cách thêm $k$ vào khả năng của mỗi cung của $A$, thì $\operatorname{cap}(N') = \operatorname{cap}(N) + k$.*

Cần chỉ ra rằng định lý lát cắt tối thiểu không đúng đối với các mạng có nhiều nguồn và các đích tương ứng, trong đó việc vận chuyển bị giới hạn từ một nguồn đến đích của nó. Chẳng hạn, trong mạng (Hình 1) với việc vận chuyển từ $a_i$ đến $b_i$ và các khả năng như được chỉ ra, giá trị của một tập phân tách tối thiểu (tức là một tập các cung gặp tất cả các chuỗi nối các nguồn và các đích tương ứng) là 4, nhưng giá trị của một luồng cực đại là 3.

Hình.

Hình 1

2. **Một thủ tục tính toán cho các mạng phẳng nguồn-đích.** Chúng tôi nói rằng một mạng $N$ là *phẳng* đối với nguồn và đích của nó, hay ngắn gọn, $N$ là *phẳng-$ab$*, nếu đồ thị $G$ của $N$, cùng với cung $ab$, là một

2Người ta đã phỏng đoán bởi G. Dantzig, trước khi có được chứng minh của định lý lát cắt tối thiểu, rằng thủ tục tính toán được mô tả trong phần này sẽ dẫn đến một luồng cực đại cho các mạng phẳng.

đồ thị phẳng $(2; 3)$. (Để thuận tiện, chúng tôi giả sử không có cung nào trong $G$ nối $a$ và $b$.) Tầm quan trọng của các mạng phẳng-$ab$ nằm trong định lý sau.

**Định lý 2.** *Nếu $N$ là ab-planar, tồn tại một chuỗi nối $a$ và $b$ mà gặp mỗi lát cắt của $N$ đúng một lần.* {#ford-1956-maxflow-thm-2 .statement tag=0321}

*Chứng minh.* Không mất tính tổng quát, ta có thể giả sử rằng cung $ab$ là một phần của biên của vùng ngoài, và rằng $G$ nằm trong một dải thẳng đứng với $a$ nằm trên đường biên bên trái của dải, $b$ nằm trên đường biên bên phải. Gọi $T$ là chuỗi nối $a$ và $b$ nằm cao nhất trong $N$. $T$ có tính chất mong muốn, như ta sẽ chỉ ra sau đây. Giả sử ngược lại. Khi đó tồn tại một lát cắt $D$, trong đó có ít nhất hai cung thuộc $T$. Gọi các cung này là $\alpha_1$ và $\alpha_2$, với $\alpha_1$ xuất hiện trước $\alpha_2$ khi đi theo $T$ từ $a$ đến $b$. Vì $D$ là một lát cắt, tồn tại một chuỗi $C_1$ nối $a$ và $b$ chỉ gặp $D$ tại $\alpha_1$. Tương tự, tồn tại một chuỗi $C_2$ chỉ gặp $D$ tại $\alpha_2$. Gọi $C_2'$ là phần của $C_2$ nối $a$ với một đầu mút của $\alpha_2$. Theo định nghĩa của $T$, $C_1$ và $C_2'$ phải giao nhau. Nhưng bây giờ, bắt đầu từ $a$, đi theo $C_2'$ đến giao điểm cuối cùng của nó với $C_1$, sau đó đi theo $C_1$ đến $b$. Do đó ta có một chuỗi từ $a$ đến $b$ không gặp $D$, mâu thuẫn với sự kiện rằng $D$ là một lát cắt.

Tương tự, dĩ nhiên, chuỗi thấp nhất của $N$ cũng có cùng tính chất.

Chú ý rằng định lý này không đúng đối với các mạng không phải là $ab$-planar. Một ví dụ đơn giản minh họa điều này được cung cấp bởi đồ thị "gas, water, electricity" (Hình 2), trong đó mọi chuỗi nối $a$ và $b$ đều gặp một lát cắt nào đó tại ba cung.

Hình.

Hình 2

Định lý 2 và hệ quả của Định lý 1 cung cấp một thủ tục tính toán đơn giản để xác định một luồng cực đại trong một mạng thuộc loại đang xét. Chỉ cần xác định một chuỗi có tính chất của Định lý 2; điều này có thể thực hiện ngay bằng cách tìm hai vùng được ngăn cách bởi cung $ab$, và lấy phần còn lại của biên của một trong hai vùng (loại bỏ các phần của biên nơi nó đã quay ngược lại và giao với chính nó, để thu được một chuỗi). Áp đặt một luồng chuỗi $(T; k)$ lớn nhất có thể lên chuỗi này, qua đó bão hòa một hoặc nhiều cung của nó. Theo hệ quả, việc trừ $k$ khỏi mỗi khả năng trong $T$ làm giảm khả năng của $N$ đi $k$. Xóa các cung đã bão hòa, và tiếp tục như trước. Cuối cùng, đồ thị bị tách rời, và một luồng cực đại đã được xây dựng. {#ford-1956-maxflow-thm-2-2 .statement tag=0322}

3. Một bài toán đường đi tối thiểu. Đối với các mạng phẳng nguồn-đích, tồn tại một tính đối ngẫu thú vị giữa bài toán tìm một chuỗi có tổng dung lượng tối thiểu nối nguồn và đích với bài toán dung lượng mạng, điều này nằm ở chỗ các chuỗi của $N$ nối nguồn và đích tương ứng với các lát cắt (tương ứng với hai đỉnh cụ thể) của đối ngẫu$^3$ của $N$ và ngược lại. Cụ thể hơn, giả sử có một mạng $N$, phẳng tương ứng với hai đỉnh $a$ và $b$, và muốn tìm một chuỗi nối $a$ và $b$ sao cho tổng các số được gán cho các cung của chuỗi là nhỏ nhất. Một cách dễ dàng để giải bài toán này như sau. Thêm cung $ab$, và xây dựng đối ngẫu của đồ thị thu được $G$. Gọi $a'$ và $b'$ là các đỉnh của đối ngẫu nằm trong các miền của $G$ bị phân tách bởi $ab$. Gán mỗi số của mạng ban đầu cho cung tương ứng trong đối ngẫu. Sau đó giải bài toán dung lượng tương ứng với $a'$ và $b'$ cho mạng đối ngẫu bằng thủ tục của §2. Một lát cắt tối thiểu được xây dựng như vậy tương ứng với một chuỗi tối thiểu trong mạng ban đầu.

$^3$Đối ngẫu của một đồ thị phẳng $G$ được tạo thành bằng cách lấy một đỉnh bên trong mỗi miền của $G$ và nối các đỉnh nằm trong các miền kề nhau bằng các cung. Xem (2; 3).
