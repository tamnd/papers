---
paper: nakamoto-2008-bitcoin
title: 'Bitcoin: A Peer-to-Peer Electronic Cash System'
authors:
  - Satoshi Nakamoto
year: 2008
venue: bitcoin.org
field: security
section: "9"
section_title: Kết hợp và Tách giá trị
tag: 000D
kind: section
lang: vi
source: https://bitcoin.org/bitcoin.pdf
pdf_sha256: b1674191a88ec5cdd733e4240a81803105dc412d6c6708d53ab94fc248f4f553
pdf_pages: "5"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 0538dd2e163eb0bc2485012705a2fbe74256836472f42f67865b95d35a799d6f
translated_from: content/en/nakamoto-2008-bitcoin/09_combining_and_splitting_value.md
source_content_sha256: 6599d72a213eb5e43934457dc617a1419e2acfc68b49e22b783de6765968079e
translation_model: gpt-5
translation_run: 20260915T023027Z
glossary_version: 6
glossary_terms_sha256: 363c21723d588ca6b8032fd3e2b0aa8dc6ab225b1f9ca1b6e98d75976e8b0d0a
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Mặc dù có thể xử lý từng đồng tiền riêng lẻ, việc tạo một giao dịch riêng cho mỗi cent trong một lần chuyển tiền sẽ rất bất tiện. Để cho phép giá trị được tách và kết hợp, các giao dịch chứa nhiều đầu vào và đầu ra. Thông thường sẽ có hoặc là một đầu vào duy nhất từ một giao dịch trước đó có giá trị lớn hơn, hoặc nhiều đầu vào kết hợp các khoản nhỏ hơn, và tối đa hai đầu ra: một cho khoản thanh toán, và một trả lại phần tiền thừa, nếu có, về cho người gửi.

Hình.

Cần lưu ý rằng fan-out, trong đó một giao dịch phụ thuộc vào nhiều giao dịch, và các giao dịch đó lại phụ thuộc vào nhiều giao dịch hơn nữa, không phải là vấn đề ở đây. Không bao giờ cần phải trích xuất một bản sao độc lập hoàn chỉnh của lịch sử giao dịch.
