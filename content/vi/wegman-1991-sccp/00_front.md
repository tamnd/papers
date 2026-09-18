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
content_sha256: af6d08dddeafb353e7d8e2925f937df01401e9b9b6d373507ae18f93b9ed999d
translated_from: content/en/wegman-1991-sccp/00_front.md
source_content_sha256: 94ce5b5dba477ad2c0e4754f4c994d52f8979f20334977030a8748c85db9197d
translation_model: gpt-5
translation_run: 20260918T122832Z
glossary_version: 7
glossary_terms_sha256: 61df191034dbc0d2b4fd3d0e6780a45e637697c607e59ad493d8021ee078cd25
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Mặc dù bài toán lan truyền hằng có thể dễ dàng được chứng minh là không quyết định được nói chung (xem Kam và Ullman [25], chẳng hạn), có nhiều trường hợp hợp lý của bài toán này là quyết định được và có các thuật toán hiệu quả về mặt tính toán tồn tại. Chúng tôi trình bày bốn thuật toán như vậy trong bài báo này. Mỗi thuật toán được trình bày ở đây có tính bảo thủ theo nghĩa là có thể không tìm được tất cả các hằng số, nhưng mỗi hằng số được tìm thấy là hằng số trong mọi thực thi có thể có của chương trình.

Sau một số kiến thức sơ bộ, các thuật toán được trình bày trong Mục 3 theo thứ tự tăng dần về sức mạnh; mỗi thuật toán kế tiếp tìm được ít nhất các hằng số mà thuật toán trước đó tìm được. Ba thuật toán đầu tiên là các cách xây dựng lại từ công trình của những người khác; thuật toán thứ tư là mới và chứa các đặc điểm tốt nhất của mỗi thuật toán trong ba thuật toán trước. Các thuật toán này nằm trong số những thuật toán lan truyền hằng toàn cục đơn giản nhất, nhanh nhất và mạnh nhất đã biết. Trong Mục 4, thuật toán của chúng tôi được chứng minh là đúng và mạnh ít nhất bằng các thuật toán trước tốt nhất với các cận thời gian đa thức. Trong Mục 5, một số vấn đề triển khai phổ biến được thảo luận.

Trong Mục 6, một số kỹ thuật được khảo sát để thực hiện lan truyền hằng trên một vùng lớn hơn các thủ tục đơn lẻ. Trong Mục 6.2, mối quan hệ giữa lan truyền hằng và tích hợp thủ tục được thảo luận. Mục 6.3 đưa ra một thuật toán mới thực hiện một dạng phân tích luồng dữ liệu liên thủ tục trong đó thông tin bí danh được thu thập kết hợp với lan truyền hằng.

Mục 7 phác thảo một số vấn đề mở và Mục 8 kết luận bài báo.

### 1. {#wegman-1991-sccp-s-1 .section tag=012F}
