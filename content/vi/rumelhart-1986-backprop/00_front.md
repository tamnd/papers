---
paper: rumelhart-1986-backprop
title: Learning Representations by Back-propagating Errors
authors:
  - David E. Rumelhart
  - Geoffrey E. Hinton
  - Ronald J. Williams
year: 1986
venue: Nature
field: ai-ml
section_title: Front Matter
tag: "0063"
kind: front
lang: vi
source: https://www.iro.umontreal.ca/~vincentp/ift3395/lectures/backprop_old.pdf
pdf_sha256: 2c011a4ffae95e49e1ad0f09a966b386f47db75eab718384bc48c87e90aeffdd
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 951c686c9a59418139383c13558152f39c1e74e0a3dedc522266bd7a327179c4
translated_from: content/en/rumelhart-1986-backprop/00_front.md
source_content_sha256: e4e258b8d5ddd5267175bbf36f016ae2f5273bb9c3f3772bec7ceaac8fd928af
translation_model: gpt-5
translation_run: 20260915T013833Z
glossary_version: 6
glossary_terms_sha256: 0d0a9334a40352952769479a6ad339487dd551fe3d836bae9914ea196d2f4310
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Học các biểu diễn bằng cách lan truyền ngược sai số

David E. Rumelhart*, Geoffrey E. Hinton† & Ronald J. Williams*

* Institute for Cognitive Science, C-015, University of California, San Diego, La Jolla, California 92093, USA

† Department of Computer Science, Carnegie-Mellon University, Pittsburgh, Philadelphia 15213, USA

Chúng tôi mô tả một thủ tục học mới, lan truyền ngược, cho các mạng gồm các đơn vị giống nơ-ron. Thủ tục này liên tục điều chỉnh các trọng số của các kết nối trong mạng nhằm giảm thiểu một phép đo sự khác biệt giữa vectơ đầu ra thực tế của mạng và vectơ đầu ra mong muốn. Do các điều chỉnh trọng số, các đơn vị 'ẩn' bên trong không thuộc về đầu vào hoặc đầu ra dần biểu diễn các đặc trưng quan trọng của miền tác vụ, và các tính quy luật trong tác vụ được nắm bắt bởi sự tương tác của các đơn vị này. Khả năng tạo ra các đặc trưng mới hữu ích phân biệt lan truyền ngược với các phương pháp trước đó, đơn giản hơn như thủ tục hội tụ perceptron¹.

Đã có nhiều nỗ lực nhằm thiết kế các mạng nơ-ron tự tổ chức. Mục tiêu là tìm ra một quy tắc sửa đổi khớp thần kinh mạnh mẽ cho phép một mạng nơ-ron được kết nối tùy ý phát triển một cấu trúc bên trong phù hợp với một miền tác vụ cụ thể. Tác vụ được đặc tả bằng cách cung cấp vectơ trạng thái mong muốn của các đơn vị đầu ra cho mỗi vectơ trạng thái của các đơn vị đầu vào.
