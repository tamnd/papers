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
content_sha256: 0ab47dc4e9228f3658a989fc3915e69e7142af4d890c42009e9f0925689a6069
translated_from: content/en/boncz-2005-x100/00_front.md
source_content_sha256: e6bada5be532f712f7962f9ac5553fd3773e9bb929695abc3914536d55226ffd
translation_model: gpt-6-astra
translation_run: 20260915T022520Z
glossary_version: 6
glossary_terms_sha256: a534ae50d60bff0e03804fd3c150e37d1876484531ab87df9c72dc4d0c455eb2
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

MonetDB/X100: Thực thi truy vấn bằng siêu đường ống (Hyper-Pipelining)

Peter Boncz, Marcin Zukowski, Niels Nes

CWI  
Kruislaan 413  
Amsterdam, Hà Lan  
{P.Boncz,M.Zukowski,N.Nes}@cwi.nl

Tóm tắt

Các hệ thống cơ sở dữ liệu thường chỉ đạt hiệu suất IPC (số lệnh trên mỗi chu kỳ) thấp trên các CPU hiện đại trong những lĩnh vực ứng dụng đòi hỏi tính toán chuyên sâu như hỗ trợ ra quyết định, OLAP và truy xuất đa phương tiện. Bài báo này bắt đầu bằng việc khảo sát chuyên sâu nguyên nhân của hiện tượng này, tập trung vào phép đo chuẩn TPC-H. Phân tích của chúng tôi về các hệ thống quan hệ khác nhau và MonetDB dẫn đến một tập hợp hướng dẫn mới để thiết kế bộ xử lý truy vấn.

Phần thứ hai của bài báo mô tả kiến trúc của bộ máy truy vấn X100 mới mà chúng tôi xây dựng cho hệ thống MonetDB theo các hướng dẫn này. Nhìn bề ngoài, nó giống một bộ máy kiểu Volcano cổ điển, nhưng điểm khác biệt then chốt là toàn bộ việc thực thi đều dựa trên khái niệm xử lý vectơ (vector processing), giúp nó sử dụng CPU với hiệu suất cao. Chúng tôi đánh giá sức mạnh của MonetDB/X100 trên phiên bản 100GB của TPC-H, cho thấy năng lực thực thi thuần túy của nó cao hơn công nghệ trước đây từ một đến hai bậc độ lớn.
