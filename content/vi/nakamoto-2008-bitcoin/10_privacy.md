---
paper: nakamoto-2008-bitcoin
title: 'Bitcoin: A Peer-to-Peer Electronic Cash System'
authors:
  - Satoshi Nakamoto
year: 2008
venue: bitcoin.org
field: security
section: "10"
section_title: Quyền riêng tư
tag: 000E
kind: section
lang: vi
source: https://bitcoin.org/bitcoin.pdf
pdf_sha256: b1674191a88ec5cdd733e4240a81803105dc412d6c6708d53ab94fc248f4f553
pdf_pages: "6"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 6862b465b9ef39d6b691158decb0da207a5e517041d8fac84304ca596efb8852
translated_from: content/en/nakamoto-2008-bitcoin/10_privacy.md
source_content_sha256: fcf18fc95d7b5e8062201f17a8ed3bd05e4ebe8295f9de6367903cf22aef5f6e
translation_model: gpt-6-astra
translation_run: 20260915T022520Z
glossary_version: 6
glossary_terms_sha256: 363c21723d588ca6b8032fd3e2b0aa8dc6ab225b1f9ca1b6e98d75976e8b0d0a
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Mô hình ngân hàng truyền thống đạt được một mức độ riêng tư bằng cách giới hạn quyền truy cập thông tin cho các bên liên quan và bên thứ ba đáng tin cậy (trusted third party). Việc phải công bố công khai tất cả các giao dịch khiến phương pháp này không thể áp dụng, nhưng quyền riêng tư vẫn có thể được duy trì bằng cách ngắt luồng thông tin ở một vị trí khác: giữ cho các khóa công khai (public keys) ẩn danh. Công chúng có thể thấy rằng ai đó đang gửi một khoản tiền cho người khác, nhưng không có thông tin liên kết giao dịch đó với bất kỳ ai. Điều này tương tự như mức độ thông tin được các sở giao dịch chứng khoán công bố, trong đó thời điểm và quy mô của từng giao dịch, tức "băng ghi giao dịch", được công khai, nhưng không cho biết các bên tham gia là ai.

Mô hình quyền riêng tư truyền thống

Danh tính → Giao dịch → Bên thứ ba đáng tin cậy → Đối tác giao dịch → Công chúng

Mô hình quyền riêng tư mới

Danh tính → Giao dịch → Công chúng

Để tạo thêm một lớp tường lửa, nên sử dụng một cặp khóa mới cho mỗi giao dịch nhằm ngăn các giao dịch bị liên kết với cùng một chủ sở hữu. Một số liên kết vẫn không thể tránh khỏi với các giao dịch có nhiều đầu vào, vì các giao dịch này tất yếu tiết lộ rằng các đầu vào của chúng thuộc về cùng một chủ sở hữu. Rủi ro là nếu chủ sở hữu của một khóa bị lộ, việc liên kết có thể làm lộ những giao dịch khác thuộc về cùng chủ sở hữu đó.
