---
paper: tarjan-1972-dfs
title: Depth-First Search and Linear Graph Algorithms
authors:
  - Robert Tarjan
year: 1972
venue: SIAM Journal on Computing
field: algorithms
section_title: Front Matter
tag: "0042"
kind: front
lang: vi
source: https://sites.cs.ucsb.edu/~gilbert/cs240a/old/cs240aSpr2011/slides/TarjanDFS.pdf
pdf_sha256: d0ee53bb4bf82602cb5dd7bd08f39927f6d0253cb30c79aaa84378ac6b94f064
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: ea16d6760ef8896a5fc1ed181ba7b3e075906fae7e18b6db82a1361535cd62c4
translated_from: content/en/tarjan-1972-dfs/00_front.md
source_content_sha256: a6bb930a7d126f94c5bf7a8bffeab75ba66f08f01883677a22d1abde48aab6bd
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: 51f62d367854beec600f51894702ad34dfcde96c993d5c00a2f7a9873047d13f
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
roundtrip: same
roundtrip_run: 20260914T214350Z
---

TÌM KIẾM THEO CHIỀU SÂU VÀ CÁC THUẬT TOÁN ĐỒ THỊ TUYẾN TÍNH*

Tóm tắt. Giá trị của tìm kiếm theo chiều sâu (depth-first search) hay “quay lui” (backtracking) như một kỹ thuật giải quyết bài toán được minh họa qua hai ví dụ. Một phiên bản cải tiến của thuật toán tìm các thành phần liên thông mạnh của đồ thị có hướng và một thuật toán tìm các thành phần song liên thông của đồ thị vô hướng được trình bày. Yêu cầu về không gian và thời gian của cả hai thuật toán đều bị chặn bởi $k_1 V + k_2 E + k_3$ với một số hằng số $k_1, k_2,$ và $k_3$, trong đó $V$ là số đỉnh và $E$ là số cạnh của đồ thị đang được xét.
