---
paper: gal-2009-tracejit
title: Trace-based Just-in-Time Type Specialization for Dynamic Languages
authors:
  - Andreas Gal
  - Brendan Eich
  - Mike Shaver
  - David Anderson
  - David Mandelin
year: 2009
venue: PLDI
field: languages
section_title: Front Matter
tag: 016A
kind: front
lang: vi
source: https://mozilla.github.io/pdf.js/web/compressed.tracemonkey-pldi-09.pdf
pdf_sha256: 3662ff519e485810520552bf301d8c3b2b917fd2f83303f4965d7abed367e113
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 4af3b35ce6d5238721a02a8efc7fc3306d95581cb5c4a28e857b0cc173a1b2cb
translated_from: content/en/gal-2009-tracejit/00_front.md
source_content_sha256: 727954d26097578ee74ac1da41468db3189f5ec8c8b2ecafb296a433c154fc8b
translation_model: gpt-5
translation_run: 20260914T194201Z
glossary_version: 6
glossary_terms_sha256: e18583cfd8910711c2e3aa00f134fd0de9487b97e78e37da9096be4297760e66
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Chuyên biệt hóa kiểu Just-in-Time dựa trên vết cho các ngôn ngữ động

Andreas Gal*+, Brendan Eich*, Mike Shaver*, David Anderson*, David Mandelin*, Mohammad R. Haghighat\$, Blake Kaplan*, Graydon Hoare*, Boris Zbarsky*, Jason Orendorff*, Jesse Ruderman*, Edwin Smith#, Rick Reitmaier#, Michael Bebenita+, Mason Chang+#, Michael Franz+

Mozilla Corporation*

{gal,brendan,shaver,danderson,dmandelin,mrbkap,graydon,bz,jorendorff,jruderman}@mozilla.com

Adobe Corporation#

{edwsmith,rreitmai}@adobe.com

Intel Corporation\$

{mohammad.r.haghighat}@intel.com

University of California, Irvine+

{mbebenit,changm,franz}@uci.edu

Tóm tắt

Các ngôn ngữ động như JavaScript khó biên dịch hơn các ngôn ngữ có kiểu tĩnh. Vì không có thông tin kiểu cụ thể, các trình biên dịch truyền thống cần phát sinh mã tổng quát có thể xử lý mọi tổ hợp kiểu có thể xảy ra tại thời gian chạy. Chúng tôi trình bày một kỹ thuật biên dịch thay thế cho các ngôn ngữ có kiểu động, kỹ thuật này xác định các vết vòng lặp được thực thi thường xuyên tại thời gian chạy và sau đó phát sinh mã máy ngay lập tức được chuyên biệt hóa cho các kiểu động thực tế xuất hiện trên mỗi đường đi qua vòng lặp. Phương pháp của chúng tôi cung cấp khả năng chuyên biệt hóa kiểu liên thủ tục với chi phí thấp, cùng với một cách thức thanh lịch và hiệu quả để biên dịch gia tăng các đường đi thay thế được phát hiện lười biếng qua các vòng lặp lồng nhau. Chúng tôi đã triển khai một trình biên dịch động cho JavaScript dựa trên kỹ thuật của mình và đã đo được mức tăng tốc 10x trở lên đối với một số chương trình phép đo chuẩn.

Danh mục và mô tả chủ đề D.3.4 [Ngôn ngữ lập trình]: Bộ xử lý — Trình biên dịch gia tăng, phát sinh mã.

Thuật ngữ chung Thiết kế, Thực nghiệm, Đo lường, Hiệu năng.

Từ khóa JavaScript, biên dịch just-in-time, cây vết.

1. Giới thiệu

Các ngôn ngữ động như JavaScript, Python, và Ruby phổ biến vì chúng biểu đạt tốt, dễ tiếp cận đối với những người không chuyên, và giúp việc triển khai trở nên dễ dàng như phân phối một tệp mã nguồn. Chúng được sử dụng cho các script nhỏ cũng như các ứng dụng phức tạp.
