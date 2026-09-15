---
paper: patterson-1981-risc
title: 'RISC I: A Reduced Instruction Set VLSI Computer'
authors:
  - David A. Patterson
  - Carlo H. Sequin
year: 1981
venue: ISCA
field: architecture
section_title: Front Matter
tag: 005B
kind: front
lang: vi
source: https://people.eecs.berkeley.edu/~kubitron/courses/cs252-F00/handouts/papers/p216-patterson.pdf
pdf_sha256: d49afdf3db5a8374fbc757059fab0562b9a517b3ff7abec17c2e6b88c48f03e1
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 2410d18d2c30ba2141b18afd2cb8e9f0347ff4aa79d4e1bdf7995ec6d4a6934f
translated_from: content/en/patterson-1981-risc/00_front.md
source_content_sha256: a686fd9175b03d68a4a6bedd90c2299a0601e73a0a0d60e2e5b89ec8a4121cc4
translation_model: gpt-5
translation_run: 20260915T013833Z
glossary_version: 6
glossary_terms_sha256: 1f83355a83baacb04f1185b8bd47b133f28d2f764f5d7ae919d5d9d0d7e083ee
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

RISC I: MÁY TÍNH VLSI VỚI TẬP LỆNH RÚT GỌN

DAVID A. PATTERSON và CARLO H. SEQUIN

Bộ phận Khoa học Máy tính
University of California
Berkeley, California

TÓM TẮT

Dự án Máy tính với Tập lệnh Rút gọn (Reduced Instruction Set Computer, RISC) nghiên cứu một hướng thay thế cho xu hướng chung hướng tới các máy tính có tập lệnh ngày càng phức tạp: Với một tập lệnh thích hợp và thiết kế kiến trúc tương ứng, có thể đạt được một máy có thông lượng hiệu dụng cao. Sự đơn giản của tập lệnh và các chế độ địa chỉ hóa cho phép hầu hết các lệnh thực thi trong một chu kỳ máy, và sự đơn giản của từng lệnh bảo đảm thời gian chu kỳ ngắn. Ngoài ra, một máy như vậy sẽ có thời gian thiết kế ngắn hơn nhiều.

Bài báo này trình bày kiến trúc của RISC I và cơ chế hỗ trợ phần cứng mới cho việc gọi/trả thủ tục. Các tập ngân hàng thanh ghi chồng lấn, có thể truyền trực tiếp các tham số cho các chương trình con, là yếu tố chủ yếu tạo nên hiệu năng xuất sắc của RISC I. Các so sánh tĩnh và động giữa kiến trúc mới này với các máy truyền thống hơn được đưa ra. Mặc dù các lệnh đơn giản hơn, độ dài trung bình của các chương trình được phát hiện là không vượt quá các chương trình cho DEC VAX 11 quá một hệ số 2. Các phép đo chuẩn sơ bộ chứng minh những ưu thế về hiệu năng của RISC. Có vẻ như có thể xây dựng một máy tính đơn chip nhanh hơn VAX 11/780.
