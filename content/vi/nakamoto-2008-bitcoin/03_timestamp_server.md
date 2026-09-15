---
paper: nakamoto-2008-bitcoin
title: 'Bitcoin: A Peer-to-Peer Electronic Cash System'
authors:
  - Satoshi Nakamoto
year: 2008
venue: bitcoin.org
field: security
section: "3"
section_title: Server dấu thời gian
tag: "0007"
kind: section
lang: vi
source: https://bitcoin.org/bitcoin.pdf
pdf_sha256: b1674191a88ec5cdd733e4240a81803105dc412d6c6708d53ab94fc248f4f553
pdf_pages: "2"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 48c169681e9f0f204240be2db9d472a63ab27b9245a999cc99baea50a992e90e
translated_from: content/en/nakamoto-2008-bitcoin/03_timestamp_server.md
source_content_sha256: 62e208cc5f8c7a08c9798a3fce707fd5de5f73898f4f8afd9b3d50681205da5b
translation_model: gpt-6-astra
translation_run: 20260915T022520Z
glossary_version: 6
glossary_terms_sha256: 363c21723d588ca6b8032fd3e2b0aa8dc6ab225b1f9ca1b6e98d75976e8b0d0a
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Giải pháp chúng tôi đề xuất bắt đầu bằng một server dấu thời gian (timestamp server). Server dấu thời gian hoạt động bằng cách tính giá trị băm (hash) của một khối các mục cần được gắn dấu thời gian và công bố rộng rãi giá trị băm đó, chẳng hạn trên một tờ báo hoặc trong một bài đăng trên Usenet [2-5]. Dấu thời gian chứng minh rằng dữ liệu phải đã tồn tại vào thời điểm đó, vì hiển nhiên dữ liệu phải tồn tại thì mới có thể được đưa vào phép băm. Mỗi dấu thời gian bao gồm dấu thời gian trước đó trong giá trị băm của nó, tạo thành một chuỗi, trong đó mỗi dấu thời gian được thêm vào củng cố các dấu thời gian đứng trước nó.

Hình.
