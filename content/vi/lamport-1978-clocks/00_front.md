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
content_sha256: a1aa50790a713ba6c8d2b8b4dd55e9a517bea0ad8bf57434eeca58a7038a95f3
translated_from: content/en/lamport-1978-clocks/00_front.md
source_content_sha256: 4b7ae7f50483519411ec5d2ce1d6efe1cc22702f57cad988b4035630cf300048
translation_model: gpt-5
translation_run: 20260918T122832Z
glossary_version: 7
glossary_terms_sha256: f834761938c11bca59f7cb79948997ed0706af48cd70392678452699c034a7ad
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Thời gian, Đồng hồ, và Thứ tự của các Sự kiện trong một Hệ thống Phân tán

Leslie Lamport  
Massachusetts Computer Associates, Inc.

Khái niệm về việc một sự kiện xảy ra trước một sự kiện khác trong một hệ thống phân tán được xem xét, và được chỉ ra rằng nó xác định một thứ tự từng phần của các sự kiện. Một thuật toán phân tán được đưa ra để đồng bộ hóa một hệ thống các đồng hồ logic, có thể được sử dụng để sắp xếp hoàn toàn các sự kiện. Việc sử dụng thứ tự toàn phần được minh họa bằng một phương pháp giải quyết các vấn đề đồng bộ hóa. Sau đó, thuật toán được chuyên biệt hóa để đồng bộ hóa các đồng hồ vật lý, và một cận được suy ra về mức độ mất đồng bộ mà các đồng hồ có thể đạt tới.

Các từ khóa và cụm từ: hệ thống phân tán, mạng máy tính, đồng bộ hóa đồng hồ, hệ thống đa tiến trình

Các phân loại CR: 4.32, 5.29
