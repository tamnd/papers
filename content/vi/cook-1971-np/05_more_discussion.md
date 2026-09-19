---
paper: cook-1971-np
title: The Complexity of Theorem-Proving Procedures
authors:
  - Stephen A. Cook
year: 1971
venue: STOC
field: theory
section: "4"
section_title: 'Thảo luận thêm:'
tag: "0414"
kind: section
lang: vi
source: https://www.cs.toronto.edu/~sacook/homepage/1971.pdf
pdf_sha256: aacaca0dd6db8b409317a2de282734539c3186a72cff1cb4dd601c76a4ddfb75
pdf_pages: 6-7
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: c1988b9c802e1482b9dea5318f055cee5087d18238dbce21b132e6dd481f7d31
translated_from: content/en/cook-1971-np/05_more_discussion.md
source_content_sha256: 5c67e4468d8cfa9c468ec70d6fd9b85d49cc08aadf42d1f321866bad437c2be1
translation_model: gpt-5
translation_run: 20260919T075800Z
glossary_version: 7
glossary_terms_sha256: a53d4b02c913445c3baaef8eee5fd81f1dcadf55e59409c12a52700dc0c85335
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Có một khoảng cách lớn giữa cận dưới $\sqrt{k}/(\log k)^2$ đối với các hàm thời gian $T_Q(k)$ được đưa ra trong định lý 3A và một

$$
T_Q(k) = k^2 k^{(\log k)^2}
$$

có thể có được trong 3B. Tuy nhiên, có những lý do cho khoảng cách này. Chẳng hạn, nếu chúng ta có thể cải thiện kết quả trong 3B và tìm được một $T_Q(k)$ bị chặn bởi một đa thức theo k, thì theo định lý 4 chúng ta có thể mô phỏng một máy bị chặn thời gian $2^n$ không tất định một cách tất định trong thời gian $p(2^n)$ với một đa thức p nào đó. Điều này trái với kinh nghiệm cho thấy mô phỏng tất định một máy bị chặn thời gian $T(n)$ không tất định nói chung đòi hỏi thời gian $k^{T(n)}$.

Mặt khác, nếu chúng ta có thể nâng cận dưới được đưa ra trong định lý 3A và chứng minh rằng

$$
\frac{T_Q(k)}{2^k}
$$

là không bị chặn, thì chúng ta có thể kết luận {Tautologies} $\notin \mathcal{L}^*$, vì nếu không thì thủ tục chứng minh Herbrand tổng quát sẽ cung cấp một $T_Q(k)$ nhỏ hơn $2^k$. Do đó, một cải thiện như vậy trong 3A sẽ đòi hỏi một bước đột phá lớn trong lý thuyết độ phức tạp.

Lĩnh vực chứng minh định lý cơ học rất cần một cơ sở để so sánh và đánh giá hàng chục thủ tục xuất hiện trong tài liệu. Hiệu năng của một thủ tục trên các ví dụ bằng máy tính là một tiêu chí tốt, nhưng không đủ (trừ khi thủ tục chứng minh được tính hữu dụng theo một cách thực tiễn nào đó). Cần có một tiêu chí độ phức tạp lý thuyết để làm nổi bật các giới hạn cơ bản và đề xuất những mục tiêu mới cần theo đuổi.

Tiêu chí được đề xuất ở đây (hàm $T_Q(k)$) có lẽ là quá thô. Chẳng hạn, có thể tốt hơn nếu biến $T_Q(k)$ thành một hàm của nhiều biến, trong đó một biến là $\phi(A)$, và một biến khác có thể là số tối thiểu các thể hiện phép thế của $fn(A)$ cần thiết để tạo thành một mâu thuẫn (lưu ý rằng nói chung không phải tất cả các $A_1, A_2, \ldots, A_{\phi(A)}$ đều cần thiết.)

$T_Q(k)$ có thể là một phép đo thô, nhưng nó cung cấp một cơ sở cho thảo luận, và tôi hy vọng sẽ kích thích tiến bộ hướng tới việc tìm ra các phép đo độ phức tạp tốt hơn cho các hệ chứng minh định lý.
