---
paper: bosshart-2014-p4
title: 'P4: Programming Protocol-Independent Packet Processors'
authors:
  - Pat Bosshart
  - Dan Daly
  - Glen Gibb
  - Martin Izzard
  - Nick McKeown
  - Jennifer Rexford
  - Cole Schlesinger
  - Dan Talayco
  - Amin Vahdat
  - George Varghese
  - David Walker
year: 2014
venue: ACM SIGCOMM Computer Communication Review
field: networks
section_title: Front Matter
tag: 008C
kind: front
lang: vi
source: arxiv:1312.1719
pdf_sha256: 2bb0ccb7b5410868efdecc9ef5208d235c6f3aa75dee84aa992751aed117a42f
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 6e3d0d46fa707b9637c73fe078d05eabe958adf1faf335f1fbf524263c72f537
translated_from: content/en/bosshart-2014-p4/00_front.md
source_content_sha256: c0a1e839a70b2bd83c38d085a9b7f7fe6a96ddff19b02b73cd77c3d0bf047c27
translation_model: gpt-5
translation_run: 20260914T163737Z
glossary_version: 6
glossary_terms_sha256: 3a5b9dd3cd6211761c92d70db4c4910c364b1cae9e5e732eea77349f449c860b
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

P4: Lập trình các bộ xử lý gói tin độc lập với giao thức

Pat Bosshart†, Dan Daly*, Glen Gibb†, Martin Izzard†, Nick McKeown‡, Jennifer Rexford**, Cole Schlesinger**, Dan Talayco†, Amin Vahdat†, George Varghese§, David Walker**
†Barefoot Networks   *Intel   ‡Stanford University   **Princeton University   †Google   §Microsoft Research

TÓM TẮT
P4 là một ngôn ngữ lập trình cấp cao để lập trình các bộ xử lý gói tin độc lập với giao thức. P4 hoạt động kết hợp với các giao thức điều khiển SDN như OpenFlow. Ở dạng hiện tại, OpenFlow đặc tả rõ ràng các phần đầu giao thức mà nó vận hành trên đó. Tập hợp này đã tăng từ 12 lên 41 trường trong vài năm, làm tăng độ phức tạp của đặc tả trong khi vẫn không cung cấp tính linh hoạt để thêm các phần đầu mới. Trong bài báo này, chúng tôi đề xuất P4 như một đề xuất sơ bộ cho cách OpenFlow nên phát triển trong tương lai. Chúng tôi có ba mục tiêu: (1) Khả năng cấu hình lại trong thực địa: Các lập trình viên có thể thay đổi cách các chuyển mạch xử lý các gói tin sau khi chúng được triển khai. (2) Tính độc lập với giao thức: Các chuyển mạch không nên bị ràng buộc với bất kỳ giao thức mạng cụ thể nào. (3) Tính độc lập với mục tiêu: Các lập trình viên có thể mô tả chức năng xử lý gói tin một cách độc lập với các chi tiết của phần cứng bên dưới. Ví dụ, chúng tôi mô tả cách sử dụng P4 để cấu hình một chuyển mạch nhằm thêm một nhãn phân cấp mới.
