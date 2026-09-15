---
paper: nakamoto-2008-bitcoin
title: 'Bitcoin: A Peer-to-Peer Electronic Cash System'
authors:
  - Satoshi Nakamoto
year: 2008
venue: bitcoin.org
field: security
section: "8"
section_title: Xác minh thanh toán đơn giản hóa
tag: 000C
kind: section
lang: vi
source: https://bitcoin.org/bitcoin.pdf
pdf_sha256: b1674191a88ec5cdd733e4240a81803105dc412d6c6708d53ab94fc248f4f553
pdf_pages: "5"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 21744672146a43029775a651c8b8b2ed349b0a5b5543f4562208e5d078a4b2fc
translated_from: content/en/nakamoto-2008-bitcoin/08_simplified_payment_verification.md
source_content_sha256: 0bd61c38957b1b1273053a9aacdfbd6024186ba1071037fd839127be351a38e0
translation_model: gpt-6-astra
translation_run: 20260915T022520Z
glossary_version: 6
glossary_terms_sha256: 363c21723d588ca6b8032fd3e2b0aa8dc6ab225b1f9ca1b6e98d75976e8b0d0a
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Có thể xác minh các khoản thanh toán mà không cần vận hành một nút mạng đầy đủ. Người dùng chỉ cần giữ một bản sao các phần đầu khối của chuỗi bằng chứng công việc (proof-of-work) dài nhất, có thể lấy được bằng cách truy vấn các nút mạng cho đến khi tin chắc rằng mình có chuỗi dài nhất, và lấy nhánh Merkle (Merkle branch) liên kết giao dịch với khối chứa dấu thời gian của giao dịch đó. Người dùng không thể tự kiểm tra giao dịch, nhưng bằng cách liên kết giao dịch với một vị trí trong chuỗi, họ có thể thấy rằng một nút mạng đã chấp nhận giao dịch đó, và các khối được thêm vào sau đó tiếp tục xác nhận rằng mạng đã chấp nhận giao dịch.

Hình.

Do đó, việc xác minh là đáng tin cậy chừng nào các nút trung thực còn kiểm soát mạng, nhưng dễ bị tấn công hơn nếu kẻ tấn công chiếm ưu thế áp đảo trên mạng. Trong khi các nút mạng có thể tự xác minh giao dịch, phương pháp đơn giản hóa có thể bị đánh lừa bởi các giao dịch giả mạo của kẻ tấn công chừng nào kẻ tấn công còn có thể duy trì ưu thế áp đảo trên mạng. Một chiến lược để phòng chống điều này là tiếp nhận cảnh báo từ các nút mạng khi chúng phát hiện một khối không hợp lệ, qua đó kích hoạt phần mềm của người dùng tải xuống toàn bộ khối và các giao dịch bị cảnh báo để xác nhận sự thiếu nhất quán. Các doanh nghiệp thường xuyên nhận thanh toán có lẽ vẫn muốn vận hành các nút riêng để bảo đảm an toàn một cách độc lập hơn và xác minh nhanh hơn.
