---
paper: corbett-2012-spanner
title: 'Spanner: Google''s Globally-Distributed Database'
authors:
  - James C. Corbett
  - Jeffrey Dean
  - Michael Epstein
  - Andrew Fikes
  - Christopher Frost
  - J. J. Furman
  - Sanjay Ghemawat
  - Andrey Gubarev
  - Christopher Heiser
  - Peter Hochschild
year: 2012
venue: OSDI
field: databases
section: "8"
section_title: Kết luận
tag: 00BE
kind: section
lang: vi
source: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.258.9924
pdf_sha256: 61875779e75f603d21aefba6d9bd9816d4dd0c18cf41089f43707249e24bbf88
pdf_pages: "13"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 3a91e093bbf23de60e738a7396d1647168e4f83e81165e458aac71f3de6c929e
translated_from: content/en/corbett-2012-spanner/08_conclusions.md
source_content_sha256: 44717e60e4a9c495930df6af27525e0fcdc2a6fbf4628297eeb39405e234a039
translation_model: gpt-5
translation_run: 20260914T201546Z
glossary_version: 6
glossary_terms_sha256: a534ae50d60bff0e03804fd3c150e37d1876484531ab87df9c72dc4d0c455eb2
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Tóm lại, Spanner kết hợp và mở rộng các ý tưởng từ hai cộng đồng nghiên cứu: từ cộng đồng cơ sở dữ liệu, một giao diện bán quan hệ quen thuộc, dễ sử dụng, các giao dịch, và một ngôn ngữ truy vấn dựa trên SQL; từ cộng đồng hệ thống, khả năng mở rộng, phân mảnh tự động, khả năng chịu lỗi, sao chép nhất quán, tính nhất quán bên ngoài, và phân phối diện rộng. Kể từ khi Spanner ra đời, chúng tôi đã mất hơn 5 năm để lặp lại qua các phiên bản nhằm đạt đến thiết kế và triển khai hiện tại. Một phần của giai đoạn lặp lại dài này là do việc nhận ra chậm rằng Spanner nên làm nhiều hơn việc giải quyết vấn đề về một không gian tên được sao chép toàn cầu, và cũng nên tập trung vào các tính năng cơ sở dữ liệu mà Bigtable còn thiếu.

Một khía cạnh trong thiết kế của chúng tôi nổi bật: yếu tố then chốt trong tập tính năng của Spanner là TrueTime. Chúng tôi đã chỉ ra rằng việc hiện thực hóa sự không chắc chắn của đồng hồ trong API thời gian giúp có thể xây dựng các hệ thống phân tán với ngữ nghĩa thời gian mạnh hơn nhiều. Ngoài ra, khi hệ thống nền tảng áp đặt các cận chặt chẽ hơn về sự không chắc chắn của đồng hồ, chi phí phụ trội của ngữ nghĩa mạnh hơn sẽ giảm xuống. Là một cộng đồng, chúng ta không nên còn phụ thuộc vào các đồng hồ được đồng bộ lỏng lẻo và các API thời gian yếu trong việc thiết kế các thuật toán phân tán.
