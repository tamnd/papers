---
paper: lamport-1978-clocks
title: Time, Clocks, and the Ordering of Events in a Distributed System
authors:
  - Leslie Lamport
year: 1978
venue: Communications of the ACM
field: systems
section_title: Front Matter
tag: 004F
kind: front
lang: vi
source: https://lamport.azurewebsites.net/pubs/time-clocks.pdf
pdf_sha256: c55e7cab4230aa3d7126748a149b2db6f0d7a67296d5eccfdd50a210299a96b2
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: f1dc3712c12d402cd8e147f01749fb7fb93a9bc200614924af367ade8b168d4e
translated_from: content/en/lamport-1978-clocks/00_front.md
source_content_sha256: 4b7ae7f50483519411ec5d2ce1d6efe1cc22702f57cad988b4035630cf300048
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: afc6de5d010821f75553a129f8b55d5fbabc0d9d7af198021ca9a5a496de4088
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
roundtrip: same
roundtrip_run: 20260914T214350Z
---

Thời gian, Đồng hồ, và Thứ tự của các Sự kiện trong một Hệ thống Phân tán

Leslie Lamport
Massachusetts Computer Associates, Inc.

Khái niệm một sự kiện xảy ra trước một sự kiện khác trong một hệ thống phân tán được xem xét, và được chỉ ra rằng nó xác định một thứ tự từng phần của các sự kiện. Một thuật toán phân tán được đưa ra để đồng bộ hóa một hệ thống các đồng hồ logic có thể được sử dụng để sắp xếp toàn phần các sự kiện. Việc sử dụng thứ tự toàn phần được minh họa bằng một phương pháp giải quyết các bài toán đồng bộ hóa. Sau đó, thuật toán được chuyên biệt hóa để đồng bộ hóa các đồng hồ vật lý, và một cận được suy ra về mức độ không đồng bộ tối đa mà các đồng hồ có thể đạt tới.

Từ khóa và Cụm từ: hệ thống phân tán, mạng máy tính, đồng bộ hóa đồng hồ, hệ thống đa tiến trình

CR Categories: 4.32, 5.29
