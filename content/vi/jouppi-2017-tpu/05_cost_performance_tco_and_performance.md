---
paper: jouppi-2017-tpu
title: In-Datacenter Performance Analysis of a Tensor Processing Unit
authors:
  - Norman P. Jouppi
  - Cliff Young
  - Nishant Patil
  - David Patterson
  - Gaurav Agrawal
  - Raminder Bajwa
  - Sarah Bates
  - Suresh Bhatia
  - Nan Boden
  - Al Borchers
year: 2017
venue: ISCA
field: architecture
section: "5"
section_title: Chi phí-Hiệu năng, TCO, và Hiệu năng/Watt
tag: "0190"
kind: section
lang: vi
source: arxiv:1704.04760
pdf_sha256: 19793e4ae1486630ac45a12facabc0e80609dd679db8ca7a3a040f8bf0d8e0be
pdf_pages: "10"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 93e9e491568ee6222a92ae278dd020ee033ab223054990f8c4b80032bfd4fecc
translated_from: content/en/jouppi-2017-tpu/05_cost_performance_tco_and_performance.md
source_content_sha256: 483e14ed4b9e74bdce60f3c235ba492aed4b4b67c4b4e9ad846af3c16b121053
translation_model: gpt-5
translation_run: 20260914T201546Z
glossary_version: 6
glossary_terms_sha256: 1f83355a83baacb04f1185b8bd47b133f28d2f764f5d7ae919d5d9d0d7e083ee
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Khi mua máy tính với số lượng hàng nghìn, chi phí-hiệu năng vượt trội hơn hiệu năng. Chỉ số chi phí tốt nhất trong một datacenter là tổng chi phí sở hữu (TCO). Giá thực tế mà chúng tôi trả cho hàng nghìn chip phụ thuộc vào các cuộc đàm phán giữa các công ty liên quan. Vì lý do kinh doanh, chúng tôi không thể công bố thông tin giá như vậy hoặc dữ liệu có thể cho phép suy ra chúng. Tuy nhiên, công suất có tương quan với TCO, và chúng tôi có thể công bố Watts trên mỗi server, vì vậy trong bài báo này chúng tôi sử dụng hiệu năng/Watt làm đại diện cho hiệu năng/TCO. Trong phần này, chúng tôi so sánh toàn bộ server thay vì các die đơn lẻ, như được liệt kê trong các cột “Benchmarked Server” của Table 2.

Figure 9 trình bày trung bình hình học và trung bình có trọng số của hiệu năng/Watt đối với GPU K80 và TPU so với CPU Haswell. Chúng tôi trình bày hai cách tính khác nhau của hiệu năng/Watt. Cách thứ nhất (“total”) bao gồm công suất được tiêu thụ bởi server CPU máy chủ khi tính hiệu năng/Watt cho GPU và TPU. Cách thứ hai (“incremental”) trừ công suất của server CPU máy chủ khỏi GPU và TPU trước đó.

Đối với total-performance/Watt, server K80 đạt 1.2 - 2.1X Haswell. Đối với incremental-performance/Watt, khi bỏ qua công suất của server Haswell, server K80 đạt 1.7- 2.9X.

Server TPU có total-performance/Watt tốt hơn Haswell từ 17 đến 34 lần, điều này khiến server TPU đạt hiệu năng/Watt bằng 14 đến 16 lần server K80. incremental-performance/Watt tương đối — là lý do biện minh của công ty chúng tôi cho một ASIC tùy chỉnh — là 41 đến 83 đối với TPU, giúp TPU đạt hiệu năng/Watt bằng 25 đến 29 lần GPU.
