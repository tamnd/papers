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
content_sha256: 85557c40bdd6b7d025ea0f5b07630d3bbb0c191f9ade55bc832d0e400da86d87
translated_from: content/en/ongaro-2014-raft/00_front.md
source_content_sha256: 863da2a3022c8b1cf2e1bb0245003b3366efc9652169fd6e5fc09623d13e8435
translation_model: gpt-5
translation_run: 20260918T122832Z
glossary_version: 7
glossary_terms_sha256: f834761938c11bca59f7cb79948997ed0706af48cd70392678452699c034a7ad
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Tìm kiếm một Thuật toán Đồng thuận Dễ Hiểu (Phiên bản Mở rộng)

Diego Ongaro và John Ousterhout
Stanford University

Tóm tắt
Raft là một thuật toán đồng thuận để quản lý một nhật ký được sao chép. Nó tạo ra một kết quả tương đương với (multi-)Paxos, và nó có hiệu năng tương đương với Paxos, nhưng cấu trúc của nó khác với Paxos; điều này làm cho Raft dễ hiểu hơn Paxos và cũng cung cấp một nền tảng tốt hơn để xây dựng các hệ thống thực tế. Để nâng cao khả năng dễ hiểu, Raft tách các thành phần chính của đồng thuận, chẳng hạn như bầu chọn leader, sao chép nhật ký và an toàn, đồng thời nó áp dụng một mức độ nhất quán mạnh hơn để giảm số lượng trạng thái cần được xem xét. Kết quả từ một nghiên cứu người dùng cho thấy Raft dễ học hơn Paxos đối với sinh viên. Raft cũng bao gồm một cơ chế mới để thay đổi thành viên cụm, sử dụng các đa số chồng lấn để đảm bảo an toàn.
