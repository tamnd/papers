---
paper: nakamoto-2008-bitcoin
title: 'Bitcoin: A Peer-to-Peer Electronic Cash System'
authors:
  - Satoshi Nakamoto
year: 2008
venue: bitcoin.org
field: security
section: "6"
section_title: Cơ chế khuyến khích
tag: 000A
kind: section
lang: vi
source: https://bitcoin.org/bitcoin.pdf
pdf_sha256: b1674191a88ec5cdd733e4240a81803105dc412d6c6708d53ab94fc248f4f553
pdf_pages: "4"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 56289c82409c87b2a91b9c1d0e01e371f49d50371385867a21f6f5480085920c
translated_from: content/en/nakamoto-2008-bitcoin/06_incentive.md
source_content_sha256: 01172d2346ed073f420e2442cc427b763d02e88f602c901cf380e00956c9ec95
translation_model: gpt-6-astra
translation_run: 20260915T022520Z
glossary_version: 6
glossary_terms_sha256: 363c21723d588ca6b8032fd3e2b0aa8dc6ab225b1f9ca1b6e98d75976e8b0d0a
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Theo quy ước, giao dịch đầu tiên trong một khối (block) là một giao dịch đặc biệt tạo ra một đồng tiền mới thuộc sở hữu của người tạo khối. Điều này tạo thêm động lực để các nút hỗ trợ mạng, đồng thời cung cấp một cách phân phối tiền ban đầu vào lưu thông, vì không có cơ quan trung ương nào phát hành tiền. Việc đều đặn bổ sung một lượng tiền mới cố định tương tự như việc thợ đào vàng tiêu tốn tài nguyên để đưa thêm vàng vào lưu thông. Trong trường hợp của chúng tôi, những thứ được tiêu tốn là thời gian CPU và điện năng.

Phần thưởng khuyến khích cũng có thể được lấy từ phí giao dịch (transaction fee). Nếu giá trị đầu ra của một giao dịch nhỏ hơn giá trị đầu vào, phần chênh lệch là phí giao dịch được cộng vào giá trị phần thưởng khuyến khích của khối chứa giao dịch đó. Khi một số lượng tiền được định trước đã đi vào lưu thông, phần thưởng khuyến khích có thể chuyển sang hoàn toàn dựa vào phí giao dịch và hoàn toàn không gây lạm phát.

Cơ chế khuyến khích có thể giúp khuyến khích các nút duy trì sự trung thực. Nếu một kẻ tấn công tham lam có thể tập hợp sức mạnh CPU lớn hơn tất cả các nút trung thực, hắn sẽ phải lựa chọn giữa việc dùng sức mạnh đó để lừa đảo bằng cách lấy cắp lại những khoản tiền mình đã thanh toán, hoặc dùng nó để tạo ra tiền mới. Hắn hẳn sẽ thấy việc tuân thủ các quy tắc có lợi hơn, vì các quy tắc đó cho phép hắn nhận được nhiều tiền mới hơn tất cả những người khác cộng lại, so với việc phá hoại hệ thống và tính hợp lệ của chính tài sản của mình.
