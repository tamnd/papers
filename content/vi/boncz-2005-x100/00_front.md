---
paper: boncz-2005-x100
title: 'MonetDB/X100: Hyper-Pipelining Query Execution'
authors:
  - Peter Boncz
  - Marcin Zukowski
  - Niels Nes
year: 2005
venue: CIDR
field: databases
section_title: Front Matter
tag: "0179"
kind: front
lang: vi
source: https://www.cidrdb.org/cidr2005/papers/P19.pdf
pdf_sha256: c509153c876aee8706e298d43e2fa93ade2696cc3102643b439af0f508bb52fc
pdf_pages: "1"
extraction: vision
extraction_model: gpt-5
content_sha256: 764c29600f1312779e04ca940f8ffe4e5ddaad51650f77aa0bf391afc2e50f85
translated_from: content/en/boncz-2005-x100/00_front.md
source_content_sha256: e6bada5be532f712f7962f9ac5553fd3773e9bb929695abc3914536d55226ffd
translation_model: gpt-5
translation_run: 20260918T153717Z
glossary_version: 7
glossary_terms_sha256: 8d6365491a62bf683f227b4ec25e6ea4a6b206a0b00009512875972be95a0002
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

MonetDB/X100: Thực thi truy vấn theo đường ống siêu tốc

Peter Boncz, Marcin Zukowski, Niels Nes

CWI  
Kruislaan 413  
Amsterdam, The Netherlands  
{P.Boncz,M.Zukowski,N.Nes}@cwi.nl

Tóm tắt

Các hệ thống cơ sở dữ liệu thường chỉ đạt hiệu quả IPC (lệnh trên mỗi chu kỳ) thấp trên các CPU hiện đại trong những lĩnh vực ứng dụng cần nhiều tính toán như hỗ trợ ra quyết định, OLAP và truy xuất đa phương tiện. Bài báo này bắt đầu bằng một nghiên cứu chuyên sâu về nguyên nhân dẫn đến điều này, tập trung vào phép đo chuẩn TPC-H. Phân tích của chúng tôi về nhiều hệ thống quan hệ khác nhau và MonetDB dẫn chúng tôi đến một tập các hướng dẫn mới cho việc thiết kế một bộ xử lý truy vấn.

Phần thứ hai của bài báo mô tả kiến trúc của bộ máy truy vấn X100 mới cho hệ thống MonetDB, tuân theo các hướng dẫn này. Bề ngoài, nó giống một bộ máy kiểu Volcano cổ điển, nhưng sự khác biệt cốt lõi là việc dựa toàn bộ thực thi trên khái niệm xử lý vectơ khiến nó đạt hiệu quả CPU cao. Chúng tôi đánh giá sức mạnh của MonetDB/X100 trên phiên bản 100GB của TPC-H, cho thấy khả năng thực thi thô của nó cao hơn công nghệ trước đây từ một đến hai bậc độ lớn.
