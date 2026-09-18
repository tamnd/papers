---
paper: stonebraker-2005-cstore
title: 'C-Store: A Column-oriented DBMS'
authors:
  - Mike Stonebraker
  - Daniel J. Abadi
  - Adam Batkin
  - Xuedong Chen
  - Mitch Cherniack
  - Miguel Ferreira
  - Edmond Lau
  - Amerson Lin
  - Sam Madden
  - Elizabeth O'Neil
  - Pat O'Neil
  - Alex Rasin
  - Nga Tran
  - Stan Zdonik
year: 2005
venue: VLDB
field: databases
section_title: Front Matter
tag: "0178"
kind: front
lang: vi
source: https://www.vldb.org/archives/website/2005/program/paper/thu/p553-stonebraker.pdf
pdf_sha256: c619eacc696c847e0d7697edb9193a2c35f242b12ac2835f486970a07129eecb
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 6b1869efea289235f6c877957c5596cc7cce80e8865b62f9194a2c085784b47b
translated_from: content/en/stonebraker-2005-cstore/00_front.md
source_content_sha256: 3e84e8845775995bd8fe3061ad4e85bc329049437d8776d660a6008298badc4c
translation_model: gpt-5
translation_run: 20260918T153717Z
glossary_version: 7
glossary_terms_sha256: 8d6365491a62bf683f227b4ec25e6ea4a6b206a0b00009512875972be95a0002
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

C-Store: Một DBMS dạng cột

Mike Stonebraker*, Daniel J. Abadi*, Adam Batkin†, Xuedong Chen†, Mitch Cherniack†,  
Miguel Ferreira*, Edmond Lau*, Amerson Lin*, Sam Madden*, Elizabeth O’Neil†,  
Pat O’Neil†, Alex Rasin‡, Nga Tran†, Stan Zdonik‡

*MIT CSAIL  
Cambridge, MA

†Brandeis University  
Waltham, MA

†UMass Boston  
Boston, MA

‡Brown University  
Providence, RI

Tóm tắt

Bài báo này trình bày thiết kế của một DBMS quan hệ được tối ưu hóa cho đọc, tương phản rõ rệt với hầu hết các hệ thống hiện tại, vốn được tối ưu hóa cho ghi. Trong số nhiều điểm khác biệt trong thiết kế của nó có: lưu trữ dữ liệu theo cột thay vì theo hàng, mã hóa và đóng gói cẩn thận các đối tượng vào bộ nhớ lưu trữ bao gồm bộ nhớ chính trong quá trình xử lý truy vấn, lưu trữ một tập hợp chồng lấp các phép chiếu hướng cột, thay vì cách thức hiện tại với các bảng và chỉ mục, một cách triển khai giao dịch không truyền thống bao gồm tính sẵn sàng cao và cô lập snapshot cho các giao dịch chỉ đọc, và việc sử dụng rộng rãi các chỉ mục bitmap để bổ sung cho các cấu trúc B-tree.

Chúng tôi trình bày dữ liệu hiệu năng sơ bộ trên một tập con của TPC-H và chỉ ra rằng hệ thống mà chúng tôi đang xây dựng, C-Store, nhanh hơn đáng kể so với các sản phẩm thương mại phổ biến. Do đó, kiến trúc này có triển vọng rất đáng khích lệ.
