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
content_sha256: 8d31232751c86a1bed609346e3765ba574aa16aa9f0b73160ab68240e40e54aa
translated_from: content/en/tarjan-1972-dfs/00_front.md
source_content_sha256: a6bb930a7d126f94c5bf7a8bffeab75ba66f08f01883677a22d1abde48aab6bd
translation_model: gpt-5
translation_run: 20260918T122832Z
glossary_version: 7
glossary_terms_sha256: d4043ebd5a5c828b0239f76956644bfb5bb815f3188dc3282d75521c97669214
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

TÌM KIẾM THEO CHIỀU SÂU VÀ CÁC THUẬT TOÁN ĐỒ THỊ TUYẾN TÍNH*

Tóm tắt. Giá trị của tìm kiếm theo chiều sâu hoặc “quay lui” như một kỹ thuật để giải quyết các bài toán được minh họa bằng hai ví dụ. Một phiên bản cải tiến của một thuật toán để tìm các thành phần liên thông mạnh của một đồ thị có hướng và một thuật toán để tìm các thành phần liên thông kép của một đồ thị vô hướng được trình bày. Các yêu cầu về không gian và thời gian của cả hai thuật toán bị chặn bởi $k_1 V + k_2 E + k_3$ với một số hằng số $k_1, k_2,$ và $k_3$, trong đó $V$ là số nút và $E$ là số cạnh của đồ thị đang được kiểm tra.
