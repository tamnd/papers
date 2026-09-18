---
paper: knuth-1977-kmp
title: Fast Pattern Matching in Strings
authors:
  - Donald E. Knuth
  - James H. Morris Jr.
  - Vaughan R. Pratt
year: 1977
venue: SIAM Journal on Computing
field: algorithms
section_title: Front Matter
tag: "0044"
kind: front
lang: vi
source: https://www.cs.jhu.edu/~misha/ReadingSeminar/Papers/Knuth77.pdf
pdf_sha256: cf3391d85e2456f8242a3dc4a88e7cdead9a419b52890bb4b8a31433e9659dcb
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: e3b6af07a4660a77d1b140816de3838c1efaf7e7787ab061010a80494cd4454d
translated_from: content/en/knuth-1977-kmp/00_front.md
source_content_sha256: 60ce63ba3d84477d570209bf28278eaed833668a8bc0ad505f60de5046d621c3
translation_model: gpt-5
translation_run: 20260918T153717Z
glossary_version: 7
glossary_terms_sha256: d4043ebd5a5c828b0239f76956644bfb5bb815f3188dc3282d75521c97669214
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

SO KHỚP MẪU NHANH TRONG CHUỖI*

DONALD E. KNUTH†, JAMES H. MORRIS, JR.‡ VÀ VAUGHAN R. PRATT¶

Tóm tắt. Một thuật toán được trình bày để tìm tất cả các lần xuất hiện của một chuỗi đã cho bên trong một chuỗi khác, với thời gian chạy tỷ lệ với tổng độ dài của các chuỗi. Hằng số tỷ lệ đủ nhỏ để làm cho thuật toán này có tính ứng dụng thực tế, và thủ tục này cũng có thể được mở rộng để xử lý một số bài toán so khớp mẫu tổng quát hơn. Một ứng dụng lý thuyết của thuật toán cho thấy rằng tập các phép nối của các palindrome chẵn, tức là ngôn ngữ $\{\alpha\alpha^R\}^*$, có thể được nhận biết trong thời gian tuyến tính. Các thuật toán khác có thời gian chạy trung bình còn nhanh hơn cũng được xem xét.

Từ khóa. mẫu, chuỗi, soạn thảo văn bản, so khớp mẫu, bộ nhớ trie, tìm kiếm, chu kỳ của một chuỗi, palindrome, thuật toán tối ưu, chuỗi Fibonacci, biểu thức chính quy

Các chương trình soạn thảo văn bản thường cần tìm kiếm trong một chuỗi ký tự để tìm các thể hiện của một chuỗi “mẫu” đã cho; chúng ta muốn tìm tất cả các vị trí, hoặc có thể chỉ vị trí ngoài cùng bên trái, tại đó mẫu xuất hiện như một chuỗi con liên tục của văn bản. Ví dụ, $c a t e n a r y$ chứa mẫu $t e n$, nhưng chúng ta không xem $c a n a r y$ là một chuỗi con.

Cách hiển nhiên để tìm kiếm một mẫu khớp là thử tìm kiếm tại mọi vị trí bắt đầu của văn bản, từ bỏ việc tìm kiếm ngay khi một ký tự không đúng được tìm thấy.
