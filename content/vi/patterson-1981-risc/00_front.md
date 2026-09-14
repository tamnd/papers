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
content_sha256: 9eb01c9d6b7def75f15a7863963d1f70ab5057b7bea4bdbc52e70c19459d0157
translated_from: content/en/patterson-1981-risc/00_front.md
source_content_sha256: a686fd9175b03d68a4a6bedd90c2299a0601e73a0a0d60e2e5b89ec8a4121cc4
translation_model: gpt-5
translation_run: 20260914T201546Z
glossary_version: 6
glossary_terms_sha256: 1f83355a83baacb04f1185b8bd47b133f28d2f764f5d7ae919d5d9d0d7e083ee
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
roundtrip: differs-materially
roundtrip_run: 20260914T214350Z
---

RISC I: MÁY TÍNH VLSI VỚI TẬP LỆNH RÚT GỌN

DAVID A. PATTERSON và CARLO H. SEQUIN

Bộ phận Khoa học Máy tính
Đại học California
Berkeley, California

TÓM TẮT

Dự án Máy tính với Tập Lệnh Rút Gọn (RISC) nghiên cứu một phương án thay thế cho xu hướng chung hướng tới các máy tính có tập lệnh ngày càng phức tạp: Với một tập lệnh thích hợp và một thiết kế kiến trúc tương ứng, có thể đạt được một máy có thông lượng hiệu dụng cao. Tính đơn giản của tập lệnh và các chế độ định địa chỉ cho phép hầu hết các lệnh thực thi trong một chu kỳ máy duy nhất, và tính đơn giản của mỗi lệnh đảm bảo thời gian chu kỳ ngắn. Ngoài ra, một máy như vậy sẽ có thời gian thiết kế ngắn hơn nhiều.

Bài báo này trình bày kiến trúc của RISC I và sơ đồ hỗ trợ phần cứng mới cho việc gọi/trả về thủ tục. Các tập ngân hàng thanh ghi chồng lấp có thể truyền trực tiếp các tham số tới các chương trình con là yếu tố chủ yếu tạo nên hiệu năng xuất sắc của RISC I. Các so sánh tĩnh và động giữa kiến trúc mới này với các máy truyền thống hơn được đưa ra. Mặc dù các lệnh đơn giản hơn, độ dài trung bình của các chương trình được phát hiện là không vượt quá các chương trình cho DEC VAX 11 quá một hệ số 2. Các phép đo chuẩn sơ bộ chứng minh các ưu điểm về hiệu năng của RISC. Có vẻ khả thi để xây dựng một máy tính một chip nhanh hơn VAX 11/780.
