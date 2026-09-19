---
paper: cook-1971-np
title: The Complexity of Theorem-Proving Procedures
authors:
  - Stephen A. Cook
year: 1971
venue: STOC
field: theory
section: "1"
section_title: Các phép đồng nhất và khả quy đa thức
tag: "0346"
kind: section
lang: vi
source: https://www.cs.toronto.edu/~sacook/homepage/1971.pdf
pdf_sha256: aacaca0dd6db8b409317a2de282734539c3186a72cff1cb4dd601c76a4ddfb75
pdf_pages: 1-4
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 30fdb9682f8f74423077dcdecdcdfae601372bc10b0704a3abbc0f669755d19f
translated_from: content/en/cook-1971-np/02_tautologies_and_polynomial_reducibility.md
source_content_sha256: 98c024913226c1199a9236761f09076aa78e25f9618dfdc5d745f5bee5f1ceaf
translation_model: gpt-5
translation_run: 20260919T075800Z
glossary_version: 7
glossary_terms_sha256: a53d4b02c913445c3baaef8eee5fd81f1dcadf55e59409c12a52700dc0c85335
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Ta cố định một hình thức hóa cho phép tính mệnh đề trong đó các công thức được viết dưới dạng các chuỗi trên $\Sigma$. Vì ta sẽ cần vô hạn ký hiệu mệnh đề (nguyên tử), mỗi ký hiệu như vậy sẽ gồm một phần tử của $\Sigma$ theo sau bởi một số ở dạng ký hiệu nhị phân để phân biệt ký hiệu đó. Do đó một công thức có độ dài n chỉ có thể có khoảng $n/\log n$ ký hiệu hàm và vị từ phân biệt. Các liên kết logic là $\&$ (và), $\vee$ (hoặc), và $\neg$ (không).

Tập các phép đồng nhất (được ký hiệu bởi {tautologies}) là một tập đệ quy nào đó của các chuỗi trên bảng chữ cái này, và ta quan tâm đến bài toán tìm một cận dưới tốt cho thời gian nhận dạng có thể có của nó. Ở đây ta không đưa ra cận dưới như vậy, nhưng định lý 1 sẽ cung cấp bằng chứng rằng {tautologies} là một tập khó nhận dạng, vì nhiều bài toán có vẻ khó có thể được rút gọn về việc xác định tính đồng nhất. Khi nói rút gọn, ta có ý gần đúng rằng nếu tính đồng nhất có thể được quyết định tức thời (bởi một "tiên tri") thì các bài toán này có thể được quyết định trong thời gian đa thức. Để làm chính xác khái niệm này, ta đưa vào các máy truy vấn, giống như các máy Turing với tiên tri trong [1].

Một máy truy vấn là một máy Turing nhiều băng với một băng đặc biệt được gọi là băng truy vấn, và ba trạng thái đặc biệt lần lượt được gọi là trạng thái truy vấn, trạng thái yes, và trạng thái no. Nếu M là một máy truy vấn và T là một tập các chuỗi, thì một T-tính toán của M là một tính toán của M trong đó ban đầu M ở trạng thái ban đầu và có một chuỗi đầu vào w trên băng đầu vào, và mỗi lần M đạt đến trạng thái truy vấn thì có một chuỗi u trên băng truy vấn, và trạng thái tiếp theo mà M đạt đến là trạng thái yes nếu $u \in T$ và là trạng thái no nếu $u \notin T$. Ta hình dung một "tiên tri", biết T, đặt M vào trạng thái yes hoặc no.

Định nghĩa

Một tập S các chuỗi là P-khả quy (P là đa thức) về một tập T các chuỗi khi và chỉ khi tồn tại một máy truy vấn M nào đó và một đa thức Q(n) sao cho với mỗi chuỗi đầu vào w, T-tính toán của M với đầu vào w dừng trong vòng $Q(|w|)$ bước ($|w|$ là độ dài của w), và kết thúc ở một trạng thái chấp nhận khi và chỉ khi $w \in S$.

Không khó để thấy rằng P-khả quy là một quan hệ bắc cầu. Vì vậy quan hệ E trên các tập chuỗi, được cho bởi $(S,T)\in E$ khi và chỉ khi mỗi tập $S$ và $T$ đều P-khả quy về tập kia, là một quan hệ tương đương. Lớp tương đương chứa một tập $S$ sẽ được ký hiệu bởi $\deg(S)$ (bậc đa thức về độ khó của $S$).

Định nghĩa: Ta sẽ ký hiệu $\deg(\{0\})$ bởi $\mathcal{L}_*$, trong đó $0$ biểu thị hàm không.

Do đó $\mathcal{L}_*$ là lớp các tập có thể nhận dạng trong thời gian đa thức. $\mathcal{L}_*$ đã được thảo luận trong [2], p. 5, và là dạng tương tự trên chuỗi của lớp $\mathcal{L}$ các hàm của Cabham [3].

Bây giờ ta định nghĩa các tập chuỗi đặc biệt sau đây.

1) Bài toán đồ thị con là bài toán cho hai đồ thị vô hướng hữu hạn, xác định xem đồ thị thứ nhất có đẳng cấu với một đồ thị con của đồ thị thứ hai hay không. Một đồ thị $G$ có thể được biểu diễn bởi một chuỗi $\bar{G}$ trên bảng chữ cái $\{0,1,*\}$ bằng cách liệt kê các hàng liên tiếp của ma trận kề của nó, được phân cách bởi các dấu * . Ta ký hiệu {subgraph pairs} là tập các chuỗi $\bar{G}_1**\bar{G}_2$ sao cho $G_1$ đẳng cấu với một đồ thị con của $G_2$.

2) Bài toán đẳng cấu đồ thị sẽ được biểu diễn bởi tập, được ký hiệu là {isomorphic graphpairs}, gồm tất cả các chuỗi $\bar{G}_1**\bar{G}_2$ sao cho $G_1$ đẳng cấu với $G_2$.

3) Tập {Primes} là tập tất cả các biểu diễn nhị phân của các số nguyên tố.

4) Tập {DNF tautologies} là tập các chuỗi biểu diễn các phép đồng nhất ở dạng chuẩn tách rời.

5) Tập $D_3$ gồm các phép đồng nhất ở dạng chuẩn tách rời trong đó mỗi tuyển thức có nhiều nhất ba hội thức (mỗi hội thức là một nguyên tử hoặc phủ định của một nguyên tử).

Định lý 1: Nếu một tập $S$ các chuỗi được chấp nhận bởi một máy Turing không tất định trong thời gian đa thức, thì $S$ là P-khả quy về {DNF tautologies}. {#cook-1971-np-thm-1 .statement tag=0347}

Hệ quả: Mỗi tập trong các định nghĩa 1)-5) đều là P-khả quy về {DNF tautologies}.

Điều này là vì mỗi tập, hoặc phần bù của nó, được chấp nhận trong thời gian đa thức bởi một máy Turing không tất định nào đó.

Chứng minh định lý: Giả sử một máy Turing không tất định $M$ chấp nhận một tập $S$ các chuỗi trong thời gian $Q(n)$, trong đó $Q(n)$ là một đa thức. Với một đầu vào $w$ cho $M$, ta sẽ xây dựng một công thức mệnh đề $A(w)$ ở dạng chuẩn hội sao cho $A(w)$ thỏa được khi và chỉ khi $M$ chấp nhận $w$. Do đó $\neg\neg A(w)$ dễ dàng được đưa về dạng chuẩn tách rời (sử dụng các luật De Morgan), và $\neg A(w)$ là một phép đồng nhất khi và chỉ khi $w\not\in S$. Vì toàn bộ phép xây dựng có thể được thực hiện trong thời gian bị chặn bởi một đa thức theo $|w|$ (độ dài của $w$), định lý được chứng minh.

Chúng ta có thể giả sử rằng máy Turing $M$ chỉ có một băng, vô hạn về phía bên phải nhưng có một ô ngoài cùng bên trái. Ta đánh số các ô từ trái sang phải $1, 2, \ldots$. Ta cố định một đầu vào $w$ cho $M$ có độ dài $n$, và giả sử $w\in S$. Khi đó có một phép tính của $M$ với đầu vào $w$ kết thúc ở một trạng thái chấp nhận trong vòng $T = Q(n)$ bước. Công thức $A(w)$ sẽ được xây dựng từ nhiều ký hiệu mệnh đề khác nhau, có ý nghĩa dự định, được liệt kê dưới đây, đề cập đến một phép tính như vậy.

Giả sử bảng chữ cái băng của $M$ là $\{\sigma_1, \ldots, \sigma_\ell\}$, và tập các trạng thái là $\{q_1, \ldots, q_s\}$. Lưu ý rằng vì phép tính có nhiều nhất $T = Q(n)$ bước, không có ô băng nào vượt quá số $T$ được quét.

Các ký hiệu mệnh đề:

$$
p_{s,t}^i \quad \text{cho } 1 \leq i \leq \ell, \ 1 \leq s, t \leq T.
$$

$p_{s,t}^i$ đúng khi và chỉ khi ô băng số $s$ tại bước $t$ chứa ký hiệu $\sigma_i$.

$$
Q_t^i \quad \text{cho } 1 \leq i \leq r, \ 1 \leq t \leq T. \quad Q_t^i \text{ đúng khi và chỉ khi tại bước } t \text{ máy ở trạng thái } q_i.
$$

$$
S_{s,t} \quad \text{cho } 1 \leq s, t \leq T \text{ đúng khi và chỉ khi tại thời điểm } t \text{ ô số } s \text{ được đầu đọc băng quét.}
$$

Công thức $A(w)$ là một liên kết hội B\&C\&D\&E\&F\&G\&H\&I được tạo thành như sau. Lưu ý $A(w)$ ở dạng chuẩn hội.

B sẽ khẳng định rằng ở mỗi bước t, một và chỉ một ô được quét. B là một phép hội $B_1 \land B_2 \land \ldots \land B_T$, trong đó $B_t$ khẳng định rằng tại thời điểm t một và chỉ một ô được quét:

$$
B_t = (S_{1,t} \lor S_{2,t} \lor \ldots \lor S_{T,t}) \land 
[\land_{1 \leq i < j \leq T} (\neg S_{i,t} \lor \neg S_{j,t})]
$$

Với $1 \leq s \leq T$ và $1 \leq t \leq T_j$, $C_{s,t}$ khẳng định rằng tại ô s và thời điểm t có một và chỉ một ký hiệu. C là phép hội của tất cả các $C_{s,t}$.

D khẳng định rằng với mỗi t có một và chỉ một trạng thái.

E khẳng định rằng các điều kiện ban đầu được thỏa mãn:

$$
E = Q_1^o \land S_{1,1} \land P_{1,1}^{i_1} \land P_{2,1}^{i_2} \land \ldots \land P_{n,1}^{i_n} \land P_{n+1,1}^1 \land \ldots \land P_{T,1}^1
$$

trong đó $w = \sigma_{i_1} \cdots \sigma_{i_n}$, $q_0$ là trạng thái ban đầu và $\sigma_1$ là ký hiệu trống.

F, G, và H khẳng định rằng với mỗi thời điểm t các giá trị của các P, Q và S được cập nhật đúng. Ví dụ, G là phép hội theo mọi t, i, j của $G_{i,j}^t$, trong đó $G_{i,j}^t$ khẳng định rằng nếu tại thời điểm t máy ở trạng thái $q_i$ đang quét ký hiệu $\sigma_j$, thì tại thời điểm $t + 1$ máy ở trạng thái $q_k$, trong đó $q_k$ là trạng thái được cho bởi hàm chuyển của M.

$$
G_{i,j}^t = \land_{s=1}^T (\neg Q_s^i \lor \neg S_{s,t} \lor \neg P_{s,t}^j \lor Q_{t+1}^k)
$$

Cuối cùng, công thức I khẳng định rằng máy đạt đến trạng thái chấp nhận tại một thời điểm nào đó. Máy M nên được sửa đổi để nó tiếp tục tính toán theo một cách tầm thường sau khi đạt đến trạng thái chấp nhận, sao cho $A(w)$ sẽ được thỏa mãn.

Bây giờ có thể dễ dàng kiểm chứng rằng $A(w)$ có tất cả các tính chất được khẳng định trong đoạn đầu tiên của chứng minh.

Định lý 2: Các tập sau đây P-giảm được lẫn nhau theo từng cặp (và do đó mỗi tập có cùng bậc khó khăn đa thức): {tautologies}, {DNF tautologies}, $D_3$, {subgraph pairs}. {#cook-1971-np-thm-2 .statement tag=0348}

Nhận xét: Chúng tôi chưa thể thêm {primes} hoặc {isomorphic graph pairs} vào danh sách trên. Việc chỉ ra rằng {tautologies} là P-giảm được về {primes} dường như đòi hỏi một số kết quả sâu sắc trong lý thuyết số, trong khi việc chỉ ra rằng {tautologies} là P-giảm được về {isomorphic graph pairs} có lẽ sẽ bác bỏ một phỏng đoán của Corneil [4] mà từ đó ông suy ra rằng bài toán đẳng cấu đồ thị có thể được giải trong thời gian đa thức.

Tình cờ, không khó để thấy từ thủ tục Davis-Putnam [5] rằng tập $D_2$, bao gồm tất cả các hằng đúng DNF với nhiều nhất hai hội tử trong mỗi tuyển tử, nằm trong $\mathcal{L}^*$. Do đó $D_2$ không thể được thêm vào danh sách trong định lý 2 (trừ khi tất cả các tập trong danh sách đều nằm trong $\mathcal{L}^*$).

Chứng minh định lý 2: Theo hệ quả của định lý 1, mỗi tập đều P-giảm được về {DNF tautologies}. Vì hiển nhiên {DNF tautologies} là P-giảm được về {tautologies}, còn lại cần chỉ ra rằng {DNF tautologies} là P-giảm được về $D_3$ và $D_3$ là P-giảm được về {subgraph pairs}.

Để chỉ ra rằng {các hằng đúng DNF} là P-rút gọn được về $D_3$, cho A là một công thức mệnh đề ở dạng chuẩn tuyển. Giả sử $A = B_1 \lor B_2 \lor \ldots \lor B_k$, trong đó $B_1 = R_1 \land \ldots \land R_s$, và mỗi $R_i$ là một nguyên tử hoặc phủ định của một nguyên tử, và $s > 3$. Khi đó A là một hằng đúng khi và chỉ khi $A'$ là một hằng đúng, trong đó

$$
A' = P \land R_3 \land \ldots \land R_s \land \neg P \land R_1 \land R_2 \land \ldots \land R_k,
$$

trong đó P là một nguyên tử mới. Vì chúng ta đã giảm số hạng liên hợp trong $B_1$, quá trình này có thể được lặp lại cho đến khi cuối cùng tìm được một công thức có nhiều nhất ba hạng liên hợp trên mỗi hạng tuyển. Rõ ràng toàn bộ quá trình bị chặn về thời gian bởi một đa thức theo độ dài của A.

Còn lại cần chỉ ra rằng $D_3$ là P-rút gọn được về {các cặp đồ thị con}. Giả sử A là một công thức ở dạng chuẩn tuyển với ba hạng liên hợp trên mỗi hạng tuyển. Do đó $A = C_1 \lor \ldots \lor C_k$, trong đó

C_i = R_{i1} \& R_{i2} \& R_{i3}, và mỗi R_{ij} là một nguyên tử hoặc một phủ định của một nguyên tử. Bây giờ cho G_1 là đồ thị đầy đủ với các đỉnh {v_1, v_2, ..., v_k}, và cho G_2 là đồ thị với các đỉnh {u_{ij}}, 1 \leq i \leq k, 1 \leq j \leq 3, sao cho u_{ij} được nối bằng một cạnh với u_{rs} khi và chỉ khi i \neq r và hai literal (R_{ij}, R_{rs}) không tạo thành một cặp đối nhau (nghĩa là chúng không có dạng (P, \neg P) cũng không có dạng (\neg P, P)). Do đó tồn tại một phép gán chân trị làm sai công thức A khi và chỉ khi tồn tại một đồng cấu đồ thị $\phi : G_1 \to G_2$ sao cho với mỗi i, $\phi(v_i) = u_{ij}$ với một j nào đó. (Đồng cấu cho biết với mỗi i, phần tử nào trong R_{i1}, R_{i2}, R_{i3} cần bị làm sai, và việc thiếu cạnh có chọn lọc trong G_2 đảm bảo rằng phép gán chân trị thu được được xác định nhất quán).

Để đảm bảo rằng một đồng cấu một-một $\phi : G_1 \to G_2$ có tính chất rằng với mỗi i, $\phi(v_i) = u_{ij}$ với một j nào đó, chúng ta sửa đổi G_1 và G_2 như sau. Chúng ta chọn các đồ thị H_1, H_2, ..., H_k đủ khác biệt với nhau sao cho nếu G'_1 được tạo thành từ G_1 bằng cách gắn H_i vào v_i, 1 \leq i \leq k, và G'_2 được tạo thành từ G_2 bằng cách gắn H_i vào mỗi u_{i1} và u_{i2} và u_{i3}, 1 \leq i \leq k, thì mọi đồng cấu một-một $\phi : G'_1 \to G'_2$ đều có tính chất vừa nêu. Không khó để thấy rằng một cấu tạo như vậy có thể được thực hiện trong thời gian đa thức. Khi đó G'_1 có thể được nhúng vào G'_2 khi và chỉ khi A \notin D_3. Điều này hoàn thành chứng minh của định lý 2.
