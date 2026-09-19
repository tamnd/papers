---
paper: cook-1971-np
title: The Complexity of Theorem-Proving Procedures
authors:
  - Stephen A. Cook
year: 1971
venue: STOC
field: theory
section: "3"
section_title: Phép tính vị từ
tag: 034B
kind: section
lang: vi
source: https://www.cs.toronto.edu/~sacook/homepage/1971.pdf
pdf_sha256: aacaca0dd6db8b409317a2de282734539c3186a72cff1cb4dd601c76a4ddfb75
pdf_pages: 5-6
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: dcecb0184d76d99f505678009d5daa2db078bc196169be494baae00923bc4a84
translated_from: content/en/cook-1971-np/04_the_predicate_calculus.md
source_content_sha256: fe5bccbd2bed45cd7cf5b217bb425687084c90b44a55d123fa9611d32f55cf5d
translation_model: gpt-5
translation_run: 20260919T075800Z
glossary_version: 7
glossary_terms_sha256: a53d4b02c913445c3baaef8eee5fd81f1dcadf55e59409c12a52700dc0c85335
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Các công thức trong phép tính vị từ được biểu diễn bằng các chuỗi theo cách tương tự như phép tính mệnh đề. Ngoài các ký hiệu của phép tính mệnh đề, chúng ta cần các ký hiệu lượng từ $\forall$ và $\exists$, cùng các ký hiệu để tạo thành danh sách vô hạn các biến cá thể, và các danh sách vô hạn các ký hiệu hàm và vị từ của mỗi cấp (tất nhiên bảng chữ cái cơ sở $\Sigma$ vẫn là hữu hạn).

Giả sử Q là một thủ tục hoạt động trên các công thức trên và kết thúc trên một công thức đầu vào đã cho A khi và chỉ khi A không thỏa được. Vì không có thủ tục quyết định cho tính thỏa được trong phép tính vị từ, suy ra không có hàm đệ quy T sao cho nếu A không thỏa được, thì Q sẽ kết thúc trong vòng T(n) bước, với n là độ dài của A. Vậy làm thế nào để đánh giá hiệu quả của thủ tục?

Chúng ta sẽ sử dụng cách tiếp cận sau. Hầu hết các bộ chứng minh định lý tự động phụ thuộc vào định lý Herbrand, phát biểu ngắn gọn rằng một công thức A không thỏa được khi và chỉ khi một số phép hội của các thể hiện thay thế của dạng hàm fn(A) của A là không nhất quán theo hàm chân trị. Giả sử chúng ta sắp thứ tự các hạng trong vũ trụ Herbrand của fn(A) theo hạng, rồi sắp xếp theo một cách tự nhiên các thể hiện thay thế của fn(A) từ vũ trụ Herbrand. Thứ tự này nên sao cho nói chung các thể hiện thay thế sử dụng các hạng có hạng lớn hơn sẽ theo sau các thể hiện thay thế sử dụng các hạng nhỏ hơn. Gọi $A_1, A_2, ...$ là các thể hiện thay thế này theo thứ tự.

Định nghĩa: Nếu A không thỏa được, thì $\phi(A)$ là k nhỏ nhất sao cho $A_1 \land A_2 \land ... \land A_k$ là không nhất quán theo hàm chân trị. Nếu A thỏa được, thì $\phi(A)$ không được định nghĩa.

Bây giờ gọi Q là thủ tục, với đầu vào A, tính chuỗi $A_1, A_2, ...$ và với mỗi i, kiểm tra xem $A_1 \land ... \land A_i$ có nhất quán theo hàm chân trị hay không. Nếu câu trả lời là không tại bất kỳ thời điểm nào, thủ tục kết thúc thành công. Khi đó rõ ràng tồn tại một T(k) đệ quy sao cho với mọi k và mọi công thức A, nếu độ dài của $A \leq k$ và $\phi(A) \leq k$, thì Q sẽ kết thúc trong vòng T(k) bước. Chúng tôi đề xuất rằng hàm T(k) là một thước đo hiệu quả của Q.

Để thuận tiện, tất cả các thủ tục trong phần này sẽ được thực hiện trên các máy Turing một băng, mà chúng tôi sẽ gọi đơn giản là máy.

Định nghĩa: Cho một máy $M_Q$ và hàm đệ quy $T_Q(k)$, chúng tôi nói rằng $M_Q$ thuộc kiểu Q và chạy trong thời gian $T_Q(k)$ nếu khi $M_Q$ bắt đầu với một công thức vị từ A được ghi trên băng của nó, thì $M_Q$ dừng khi và chỉ khi A không thỏa được, và với mọi k, nếu $\phi(A) \leq k$ và $|A| \leq \log_2 k$, thì $M_Q$ dừng trong vòng $T_Q(k)$ bước. Trong trường hợp này chúng tôi cũng nói rằng $T_Q(k)$ thuộc kiểu Q. Ở đây $|A|$ là độ dài của A.

Lý do cho điều kiện $|A| \leq \log_2 k$ thay vì $|A| \leq k$, là vì với điều kiện sau, việc tìm một cận dưới cho $T_Q(k)$ sẽ gần tương đương với việc tìm một cận dưới cho bài toán quyết định của phép tính mệnh đề. Đặc biệt, định lý 3A sẽ trở nên hiển nhiên và tầm thường.

Định lý 3: A) Với mọi $T_Q(k)$ thuộc kiểu Q, {#cook-1971-np-thm-3 .statement tag=0412}

$$
\frac{T_Q(k)}{\sqrt{k}/(\log k)^2}
$$

là không bị chặn.

B) Tồn tại một $T_Q(k)$ thuộc kiểu Q sao cho

$$
T_Q(k) \leq k^2 (\log k)^2
$$

Phác thảo chứng minh: A). Với bất kỳ máy M nào, có thể xây dựng một công thức vị từ $A(M)$ thỏa được khi và chỉ khi M không bao giờ dừng khi bắt đầu trên một băng trống. Điều này được thực hiện theo hướng được mô tả trong Wang [7] trong chứng minh giảm bài toán dừng về bài toán quyết định của phép tính vị từ. Hơn nữa, nếu M dừng sau s bước, thì

$$
\phi(A(M)) \leq s^2
$$

Do đó, nếu trái với (2), $T_Q(k) = O(\sqrt{k}/\log^2 k)$, thì một sửa đổi của $M_Q$ có thể xác minh chỉ trong

$$
O(\sqrt{s^2}/\log^2 s^2) = O(s/\log^2 s)
$$

bước rằng M đã dừng sau s bước (với điều kiện $m \leq \log s^2$, trong đó m là độ dài của $A(M)$). Một lập luận đường chéo (xem [8] p. 153) cho thấy điều này nói chung là không thể.

B) Máy $M_Q$ hoạt động trong thời gian $T_Q$ bằng cách tuân theo thủ tục được nêu ở đầu phần này. Lưu ý rằng công thức $A_1 \& A_2 \& \ldots \& A_k$ có độ dài $O(k \log^2 k)$, vì chúng ta có thể giả sử $|A| \leq \log k$.

Định lý 4: Nếu tập S các chuỗi được một máy không tất định chấp nhận trong thời gian $T(n) = 2^n$, và nếu $T_Q(k)$ là một hàm trung thực (nghĩa là đếm được theo thời gian thực) thuộc kiểu Q, thì tồn tại một hằng số K sao cho S có thể được nhận dạng bởi một máy tất định trong thời gian $T_Q(K8^n)$. {#cook-1971-np-thm-4 .statement tag=0413}

Chứng minh: Giả sử $M_1$ là một máy không tất định chấp nhận S trong thời gian $2^n$. Gọi $M_2$ là một máy không tất định mô phỏng $M_1$ đúng $2^n$ bước rồi dừng, trừ khi $M_1$ chấp nhận đầu vào, trong trường hợp đó $M_2$ tính toán mãi mãi. Do đó với mọi chuỗi w, nếu $w \in S$ thì tồn tại một phép tính mà trong đó $M_2$ với đầu vào w không dừng, và nếu $w \notin S$, thì $M_2$ với đầu vào w dừng trong vòng $4^n$ bước đối với mọi phép tính. Bây giờ với w có độ dài n, ta có thể xây dựng một công thức $A(w)$ có độ dài $O(n)$ sao cho $A(w)$ thỏa được khi và chỉ khi $M_1$ chấp nhận w. ($A(w)$ được xây dựng theo cách tương tự như $A(M)$ trong chứng minh của 1A). Hơn nữa, nếu $M_2$ dừng trong vòng $4^n$ bước đối với mọi phép tính có thể có, thì

$$
\phi(A(w)) \leq K(4^n)^2 = K8^n
$$

Do đó, có thể xây dựng một máy tất định M để xác định liệu $w \in S$ hay không bằng cách cung cấp $M_Q$ với đầu vào $A(w)$. Nếu không có kết quả nào xuất hiện trong vòng $T_Q(K8^n)$ bước, thì $w \in S$, và ngược lại $w \notin S$.
