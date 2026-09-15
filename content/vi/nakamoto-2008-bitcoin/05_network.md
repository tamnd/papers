---
paper: nakamoto-2008-bitcoin
title: 'Bitcoin: A Peer-to-Peer Electronic Cash System'
authors:
  - Satoshi Nakamoto
year: 2008
venue: bitcoin.org
field: security
section: "5"
section_title: Mạng
tag: "0009"
kind: section
lang: vi
source: https://bitcoin.org/bitcoin.pdf
pdf_sha256: b1674191a88ec5cdd733e4240a81803105dc412d6c6708d53ab94fc248f4f553
pdf_pages: 3-4
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 0d2670e3f1355a79dfef4bc63a98324f62fba29fe2e0e73f8c65f16856181955
translated_from: content/en/nakamoto-2008-bitcoin/05_network.md
source_content_sha256: 424f914a0d030f1dd7ebc43d1a9984d71525b1f4eafc2cb68bb1ed523c26c2d8
translation_model: gpt-6-astra
translation_run: 20260915T022520Z
glossary_version: 6
glossary_terms_sha256: 363c21723d588ca6b8032fd3e2b0aa8dc6ab225b1f9ca1b6e98d75976e8b0d0a
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Các bước vận hành mạng như sau:

1) Các giao dịch mới được quảng bá đến tất cả các nút.
2) Mỗi nút tập hợp các giao dịch mới vào một khối.
3) Mỗi nút tìm một bằng chứng công việc (proof-of-work) có độ khó cao cho khối của mình.
4) Khi một nút tìm được bằng chứng công việc, nó quảng bá khối đó đến tất cả các nút.
5) Các nút chỉ chấp nhận khối nếu tất cả các giao dịch trong khối đều hợp lệ và chưa được chi tiêu trước đó.
6) Các nút thể hiện việc chấp nhận khối bằng cách tạo khối tiếp theo trong chuỗi, sử dụng giá trị băm của khối đã được chấp nhận làm giá trị băm trước đó.

Các nút luôn coi chuỗi dài nhất là chuỗi đúng và sẽ tiếp tục mở rộng chuỗi đó. Nếu hai nút đồng thời quảng bá các phiên bản khác nhau của khối tiếp theo, một số nút có thể nhận được phiên bản này hoặc phiên bản kia trước. Trong trường hợp đó, chúng tiếp tục làm việc trên phiên bản nhận được đầu tiên, nhưng lưu lại nhánh còn lại phòng khi nhánh đó trở nên dài hơn. Thế cân bằng sẽ bị phá vỡ khi bằng chứng công việc tiếp theo được tìm thấy và một nhánh trở nên dài hơn; các nút đang làm việc trên nhánh còn lại khi đó sẽ chuyển sang nhánh dài hơn.

Thông điệp quảng bá giao dịch mới không nhất thiết phải đến được tất cả các nút. Miễn là chúng đến được nhiều nút, các giao dịch đó sẽ sớm được đưa vào một khối. Việc quảng bá khối cũng có khả năng chịu được tình trạng mất thông điệp. Nếu một nút không nhận được một khối, nó sẽ yêu cầu khối đó khi nhận được khối tiếp theo và nhận ra rằng mình đã bỏ lỡ một khối.
