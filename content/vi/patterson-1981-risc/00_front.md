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
content_sha256: 2d6994bbfe416d232eaa7cb8c52ff3da8480e149d0a15f2409caddcea1e0d1cd
translated_from: content/en/patterson-1981-risc/00_front.md
source_content_sha256: a686fd9175b03d68a4a6bedd90c2299a0601e73a0a0d60e2e5b89ec8a4121cc4
translation_model: gpt-5
translation_run: 20260918T153717Z
glossary_version: 7
glossary_terms_sha256: cb514473400f65abfd1e5d09e5f82163f246175d67293cbba8eac7dbb7d7b890
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

RISC I: MÁY TÍNH VLSI VỚI TẬP LỆNH RÚT GỌN

DAVID A. PATTERSON và CARLO H. SEQUIN

Bộ phận Khoa học Máy tính
Đại học California
Berkeley, California

TÓM TẮT

Dự án Máy tính với Tập Lệnh Rút Gọn (RISC) nghiên cứu một phương án thay thế cho xu hướng chung hướng tới các máy tính có tập lệnh ngày càng phức tạp: Với một tập hợp lệnh thích hợp và một thiết kế kiến trúc tương ứng, có thể đạt được một máy có thông lượng hiệu dụng cao. Sự đơn giản của tập lệnh và các chế độ định địa chỉ cho phép hầu hết các lệnh thực thi trong một chu kỳ máy, và sự đơn giản của từng lệnh bảo đảm thời gian chu kỳ ngắn. Ngoài ra, một máy như vậy sẽ có thời gian thiết kế ngắn hơn nhiều.

Bài báo này trình bày kiến trúc của RISC I và sơ đồ hỗ trợ phần cứng mới của nó cho lời gọi/trả về thủ tục. Các tập ngân hàng thanh ghi chồng lấp có thể truyền các tham số trực tiếp tới các chương trình con là nguyên nhân chủ yếu tạo nên hiệu năng xuất sắc của RISC I. Các so sánh tĩnh và động giữa kiến trúc mới này với các máy truyền thống hơn được đưa ra. Mặc dù các lệnh đơn giản hơn, độ dài trung bình của các chương trình được phát hiện là không vượt quá các chương trình cho DEC VAX 11 quá một hệ số 2. Các phép đo chuẩn sơ bộ chứng minh các ưu điểm về hiệu năng của RISC. Có vẻ có khả năng xây dựng một máy tính một chip nhanh hơn VAX 11/780.
