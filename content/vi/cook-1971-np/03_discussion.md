---
paper: cook-1971-np
title: The Complexity of Theorem-Proving Procedures
authors:
  - Stephen A. Cook
year: 1971
venue: STOC
field: theory
section: "2"
section_title: Thảo luận
tag: "0349"
kind: section
lang: vi
source: https://www.cs.toronto.edu/~sacook/homepage/1971.pdf
pdf_sha256: aacaca0dd6db8b409317a2de282734539c3186a72cff1cb4dd601c76a4ddfb75
pdf_pages: 4-5
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: aacb713d10040f894577f3fa61c3e922673ac3d5d9fefc09a990021f858fc650
translated_from: content/en/cook-1971-np/03_discussion.md
source_content_sha256: 7f481a5895fa09c26adac7d195f2f950d7c752b63491b03dc1fd7a32088680d6
translation_model: gpt-5
translation_run: 20260919T075800Z
glossary_version: 7
glossary_terms_sha256: a53d4b02c913445c3baaef8eee5fd81f1dcadf55e59409c12a52700dc0c85335
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Định lý 1 và hệ quả của nó cung cấp bằng chứng mạnh mẽ rằng không dễ xác định liệu một công thức mệnh đề đã cho có phải là một hằng đúng hay không, ngay cả khi công thức đó ở dạng tuyển chuẩn tắc. Định lý 1 và 2 cùng nhau gợi ý rằng việc tìm kiếm một thủ tục quyết định đa thức cho bài toán đồ thị con là vô ích, vì thành công sẽ đưa các thủ tục quyết định đa thức đến nhiều bài toán khác có vẻ không khả thi. Dĩ nhiên nhận xét tương tự áp dụng cho bất kỳ bài toán tổ hợp nào mà {tautologies} là P-reducible. {#cook-1971-np-thm-1-2 .statement tag=034A}

Hơn nữa, các định lý gợi ý rằng {tautologies} là một ứng viên tốt cho một tập thú vị không thuộc $\mathcal{L}^*$, và tôi cảm thấy đáng để dành nỗ lực đáng kể nhằm chứng minh phỏng đoán này. Một chứng minh như vậy sẽ là một đột phá lớn trong lý thuyết độ phức tạp.

Xét đến độ phức tạp rõ ràng của {DNF tautologies}, việc khảo sát thủ tục Davis-Putnam [5] là điều thú vị. Thủ tục này được thiết kế để xác định liệu một công thức đã cho ở dạng hội chuẩn tắc có thỏa được hay không, nhưng dĩ nhiên thủ tục "đối ngẫu" xác định liệu một công thức đã cho ở dạng tuyển chuẩn tắc có phải là một hằng đúng hay không. Cho đến nay tôi vẫn chưa thể tìm được một dãy ví dụ cho thấy thủ tục này (được xử lý một cách thích hợp để tránh một số cạm bẫy nhất định) phải cần nhiều hơn thời gian đa thức. Tôi cũng chưa tìm thấy một cận trên thú vị cho thời gian cần thiết.

Nếu ta cho phép các chuỗi biểu diễn các số tự nhiên, (hoặc các bộ k của các số tự nhiên) sử dụng ký hiệu m-adic hoặc ký hiệu thích hợp khác, thì các khái niệm trong các phần trước có thể được áp dụng cho các tập số (hoặc các quan hệ k-vị trí trên các số). Không khó để thấy rằng tập các quan hệ được chấp nhận trong thời gian đa thức bởi một máy Turing không tất định chính là tập $\mathcal{L}^+$ gồm các quan hệ có dạng

(1) $(\exists y \leq g_k(\bar{x}))\ R(\bar{x},y)$ trong đó $g_k(\bar{x}) = 2^{(\ell(\max \bar{x}))^k}$, $\ell(z)$ là độ dài dyadic của z, và $R(\bar{x}, y)$ là một quan hệ $\mathcal{L}^*$, ($\mathcal{L}^+$ là lớp các quan hệ sơ đẳng dương mở rộng của Bennett [6]). Nếu ta loại bỏ cận trên của lượng từ trong công thức (1), lớp $\mathcal{L}^+$ sẽ trở thành lớp các tập đệ quy đếm được. Vì vậy nếu $\mathcal{L}^+$ là tương tự của lớp các tập r.e., thì việc xác định tautologyhood là tương tự của bài toán dừng; vì, theo định lý 1, {tautologies} có bậc $\mathcal{L}^+$ đầy đủ giống như bài toán dừng có bậc r.e. đầy đủ. Đáng tiếc, lập luận đường chéo cho thấy bài toán dừng không đệ quy dường như không thể được điều chỉnh để chứng minh {tautologies} không thuộc $\mathcal{L}^*$.
