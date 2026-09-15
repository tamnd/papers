---
paper: nakamoto-2008-bitcoin
title: 'Bitcoin: A Peer-to-Peer Electronic Cash System'
authors:
  - Satoshi Nakamoto
year: 2008
venue: bitcoin.org
field: security
section: "2"
section_title: Giao dịch
tag: "0006"
kind: section
lang: vi
source: https://bitcoin.org/bitcoin.pdf
pdf_sha256: b1674191a88ec5cdd733e4240a81803105dc412d6c6708d53ab94fc248f4f553
pdf_pages: "2"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: d803e9f588797ee0ddb75db2d76df3e56b8629ec48ff595bd2518bd675d3305a
translated_from: content/en/nakamoto-2008-bitcoin/02_transactions.md
source_content_sha256: bc4ecbf3c1d41e101b0518160baaebceda5af8e478ecdc5fc1ceea906094315a
translation_model: gpt-6-astra
translation_run: 20260915T022520Z
glossary_version: 6
glossary_terms_sha256: 363c21723d588ca6b8032fd3e2b0aa8dc6ab225b1f9ca1b6e98d75976e8b0d0a
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Chúng tôi định nghĩa một đồng tiền điện tử là một chuỗi chữ ký số (digital signature). Mỗi chủ sở hữu chuyển đồng tiền cho người tiếp theo bằng cách ký số lên giá trị băm của giao dịch trước đó và khóa công khai (public key) của chủ sở hữu tiếp theo, rồi thêm chúng vào cuối đồng tiền. Người nhận thanh toán có thể xác minh các chữ ký để xác minh chuỗi quyền sở hữu.

Hình.

Vấn đề hiển nhiên là người nhận thanh toán không thể xác minh rằng không có chủ sở hữu nào đã chi tiêu hai lần (double-spending) cùng một đồng tiền. Một giải pháp phổ biến là đưa vào một cơ quan trung ương đáng tin cậy, hay cơ sở phát hành tiền, để kiểm tra mọi giao dịch nhằm phát hiện việc chi tiêu hai lần. Sau mỗi giao dịch, đồng tiền phải được trả lại cho cơ sở phát hành tiền để phát hành một đồng tiền mới, và chỉ những đồng tiền do cơ sở này trực tiếp phát hành mới được tin là chưa bị chi tiêu hai lần. Vấn đề của giải pháp này là số phận của toàn bộ hệ thống tiền tệ phụ thuộc vào công ty vận hành cơ sở phát hành tiền, với mọi giao dịch đều phải thông qua công ty đó, giống như một ngân hàng.

Chúng tôi cần một cách để người nhận thanh toán biết rằng các chủ sở hữu trước đó chưa ký bất kỳ giao dịch nào sớm hơn. Với mục đích của chúng tôi, giao dịch sớm nhất là giao dịch được tính, nên chúng tôi không quan tâm đến những nỗ lực chi tiêu hai lần về sau. Cách duy nhất để xác nhận một giao dịch không tồn tại là biết tất cả các giao dịch. Trong mô hình dựa trên cơ sở phát hành tiền, cơ sở này biết tất cả các giao dịch và quyết định giao dịch nào đến trước. Để thực hiện điều này mà không cần một bên đáng tin cậy, các giao dịch phải được công bố công khai [1], và chúng tôi cần một hệ thống để những người tham gia thống nhất về một lịch sử duy nhất ghi lại thứ tự tiếp nhận các giao dịch. Người nhận thanh toán cần bằng chứng rằng tại thời điểm của mỗi giao dịch, đa số các nút đã đồng ý rằng đó là giao dịch được tiếp nhận đầu tiên.
