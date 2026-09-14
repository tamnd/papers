---
paper: ongaro-2014-raft
title: In Search of an Understandable Consensus Algorithm
authors:
  - Diego Ongaro
  - John Ousterhout
year: 2014
venue: USENIX ATC
field: systems
section_title: Front Matter
tag: "0170"
kind: front
lang: vi
source: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.998.3935
pdf_sha256: 5a5c679b6a7c88007faeff8c3eef19a77e9e5caa8bd7390922584fe8ecf0ce1f
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: ae8c4d09163c001faac74f82b2700123eedada78963fdad0c6ea8286d35475f0
translated_from: content/en/ongaro-2014-raft/00_front.md
source_content_sha256: 863da2a3022c8b1cf2e1bb0245003b3366efc9652169fd6e5fc09623d13e8435
translation_model: gpt-5
translation_run: 20260914T201546Z
glossary_version: 6
glossary_terms_sha256: afc6de5d010821f75553a129f8b55d5fbabc0d9d7af198021ca9a5a496de4088
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Tìm kiếm một thuật toán đồng thuận dễ hiểu (Phiên bản mở rộng)

Diego Ongaro and John Ousterhout
Stanford University

Tóm tắt
Raft là một thuật toán đồng thuận để quản lý một nhật ký được sao chép. Nó tạo ra một kết quả tương đương với (multi-)Paxos, và nó có hiệu quả tương đương Paxos, nhưng cấu trúc của nó khác với Paxos; điều này làm cho Raft dễ hiểu hơn Paxos và cũng cung cấp một nền tảng tốt hơn để xây dựng các hệ thống thực tế. Để tăng khả năng dễ hiểu, Raft tách các thành phần chính của đồng thuận, chẳng hạn như bầu chọn leader, sao chép nhật ký và tính an toàn, đồng thời nó áp dụng mức độ nhất quán cao hơn để giảm số lượng trạng thái cần được xem xét. Kết quả từ một nghiên cứu người dùng cho thấy Raft dễ học hơn Paxos đối với sinh viên. Raft cũng bao gồm một cơ chế mới để thay đổi thành viên của cụm, cơ chế này sử dụng các đa số chồng lấn để đảm bảo tính an toàn.
