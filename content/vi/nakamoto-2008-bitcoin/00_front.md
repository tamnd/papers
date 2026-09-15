---
paper: nakamoto-2008-bitcoin
title: 'Bitcoin: A Peer-to-Peer Electronic Cash System'
authors:
  - Satoshi Nakamoto
year: 2008
venue: bitcoin.org
field: security
section_title: Front Matter
tag: "0004"
kind: front
lang: vi
source: https://bitcoin.org/bitcoin.pdf
pdf_sha256: b1674191a88ec5cdd733e4240a81803105dc412d6c6708d53ab94fc248f4f553
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: c18cc0e4569b5f7ef3d1b4b636a9d97ed16b7282885d24d058bf6576233e825b
translated_from: content/en/nakamoto-2008-bitcoin/00_front.md
source_content_sha256: bd20f2089af2843bb09bab180463973e8f8401240bbf14dd8e70964810c4899b
translation_model: gpt-6-astra
translation_run: 20260915T022520Z
glossary_version: 6
glossary_terms_sha256: 363c21723d588ca6b8032fd3e2b0aa8dc6ab225b1f9ca1b6e98d75976e8b0d0a
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Bitcoin: Một hệ thống tiền điện tử ngang hàng (peer-to-peer)

Satoshi Nakamoto
satoshin@gmx.com
www.bitcoin.org

Tóm tắt. Một phiên bản tiền điện tử hoàn toàn ngang hàng sẽ cho phép gửi các khoản thanh toán trực tuyến trực tiếp từ bên này sang bên khác mà không cần thông qua một tổ chức tài chính. Chữ ký số cung cấp một phần giải pháp, nhưng những lợi ích chính sẽ mất đi nếu vẫn cần một bên thứ ba đáng tin cậy để ngăn chặn việc chi tiêu hai lần (double-spending). Chúng tôi đề xuất một giải pháp cho vấn đề chi tiêu hai lần bằng cách sử dụng mạng ngang hàng. Mạng gắn dấu thời gian cho các giao dịch bằng cách băm chúng vào một chuỗi bằng chứng công việc (proof-of-work) dựa trên băm liên tục được nối dài, tạo thành một bản ghi không thể thay đổi nếu không thực hiện lại bằng chứng công việc. Chuỗi dài nhất không chỉ là bằng chứng về chuỗi sự kiện đã được chứng kiến, mà còn là bằng chứng cho thấy nó được tạo ra từ nguồn sức mạnh CPU tổng hợp lớn nhất. Miễn là phần lớn sức mạnh CPU do các nút không hợp tác tấn công mạng kiểm soát, các nút này sẽ tạo ra chuỗi dài nhất và vượt lên trước những kẻ tấn công. Bản thân mạng chỉ yêu cầu cấu trúc tối thiểu. Các thông điệp được quảng bá theo nguyên tắc nỗ lực tối đa, và các nút có thể tùy ý rời khỏi rồi tham gia lại mạng, chấp nhận chuỗi bằng chứng công việc dài nhất làm bằng chứng về những gì đã xảy ra trong thời gian chúng vắng mặt.
