---
paper: wegman-1991-sccp
title: Constant Propagation with Conditional Branches
authors:
  - Mark N. Wegman
  - F. Kenneth Zadeck
year: 1991
venue: ACM TOPLAS
field: languages
section_title: Front Matter
tag: 004C
kind: front
lang: vi
source: https://www.cs.utexas.edu/users/lin/cs380c/wegman.pdf
pdf_sha256: 40929436cdf1c477f2318221df5d0aa71488db4a01cc448b184e0aba8bf95ddb
pdf_pages: "2"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 7ad63681a39ebb422aa91debce676b19918a81e5b7a9a46e82b5206ca8e2390a
translated_from: content/en/wegman-1991-sccp/00_front.md
source_content_sha256: 94ce5b5dba477ad2c0e4754f4c994d52f8979f20334977030a8748c85db9197d
translation_model: gpt-5
translation_run: 20260914T160437Z
glossary_version: 6
glossary_terms_sha256: e18583cfd8910711c2e3aa00f134fd0de9487b97e78e37da9096be4297760e66
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Mặc dù bài toán lan truyền hằng số dễ dàng được chứng minh là không quyết định được nói chung (xem Kam và Ullman [25], chẳng hạn), có nhiều trường hợp hợp lý của bài toán này là quyết định được và tồn tại các thuật toán có hiệu quả tính toán. Trong bài báo này, chúng tôi trình bày bốn thuật toán như vậy. Mỗi thuật toán được trình bày ở đây mang tính bảo thủ theo nghĩa có thể không tìm được tất cả các hằng số, nhưng mỗi hằng số được tìm thấy đều là hằng số trong mọi thực thi có thể của chương trình.

Sau một số kiến thức sơ bộ, các thuật toán được trình bày trong Section 3 theo thứ tự tăng dần về sức mạnh; mỗi thuật toán tiếp theo tìm được ít nhất các hằng số mà thuật toán trước đó tìm được. Ba thuật toán đầu tiên là những cách xây dựng lại từ công trình của các tác giả khác; thuật toán thứ tư là mới và chứa những đặc điểm tốt nhất của từng thuật toán trong ba thuật toán trước. Các thuật toán này thuộc số những thuật toán lan truyền hằng số toàn cục đơn giản nhất, nhanh nhất và mạnh nhất đã biết. Trong Section 4, thuật toán của chúng tôi được chứng minh là đúng và ít nhất mạnh bằng các thuật toán tốt nhất trước đây với các cận thời gian đa thức. Trong Section 5, một số vấn đề triển khai thường gặp được thảo luận.

Trong Section 6, một số kỹ thuật được khảo sát để thực hiện lan truyền hằng số trên một phạm vi lớn hơn các thủ tục đơn lẻ. Trong Section 6.2, mối quan hệ giữa lan truyền hằng số và tích hợp thủ tục được thảo luận. Section 6.3 trình bày một thuật toán mới thực hiện một dạng phân tích luồng dữ liệu liên thủ tục, trong đó thông tin bí danh được thu thập kết hợp với lan truyền hằng số.

Section 7 phác thảo một số vấn đề còn bỏ ngỏ và Section 8 kết luận bài báo.

### 1. {#wegman-1991-sccp-s-1 .section tag=012F}
