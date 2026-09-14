---
paper: barham-2003-xen
title: Xen and the Art of Virtualization
authors:
  - Paul Barham
  - Boris Dragovic
  - Keir Fraser
  - Steven Hand
  - Tim Harris
  - Alex Ho
  - Rolf Neugebauer
  - Ian Pratt
  - Andrew Warfield
year: 2003
venue: SOSP
field: systems
section_title: Front Matter
tag: 016C
kind: front
lang: vi
source: https://doi.org/10.1145/945445.945462
pdf_sha256: 7763a4c6cca63c17c92107b4d296fe2b7600ae8f419eef9ff36ac6c58a7a2a4d
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: e763941c16a6f6b24d7bc1277a276c326ee7f24a87661005a06a72865bf4aefd
translated_from: content/en/barham-2003-xen/00_front.md
source_content_sha256: 28803dac62a9c6ea1c5b590f69b9cce559f5506a0355ca0193c15a9c6e26ff93
translation_model: gpt-5
translation_run: 20260914T155352Z
glossary_version: 6
glossary_terms_sha256: afc6de5d010821f75553a129f8b55d5fbabc0d9d7af198021ca9a5a496de4088
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Xen và Nghệ thuật Ảo hóa

Paul Barham*, Boris Dragovic, Keir Fraser, Steven Hand, Tim Harris,

Alex Ho, Rolf Neugebauer†, Ian Pratt, Andrew Warfield

Phòng thí nghiệm Máy tính Đại học Cambridge

15 JJ Thomson Avenue, Cambridge, UK, CB3 0FD

{firstname.lastname}@cl.cam.ac.uk

TÓM TẮT

Nhiều hệ thống đã được thiết kế sử dụng ảo hóa để phân chia các tài nguyên dồi dào của một máy tính hiện đại. Một số yêu cầu phần cứng chuyên dụng, hoặc không thể hỗ trợ các hệ điều hành phổ biến. Một số hướng tới khả năng tương thích nhị phân 100% với cái giá phải trả là hiệu năng. Những hệ thống khác hy sinh tính bảo mật hoặc chức năng để đổi lấy tốc độ. Rất ít hệ thống cung cấp sự cô lập tài nguyên hoặc các đảm bảo về hiệu năng; phần lớn chỉ cung cấp việc cấp phát theo nỗ lực tốt nhất, dẫn đến nguy cơ từ chối dịch vụ.

Bài báo này trình bày Xen, một bộ giám sát máy ảo x86 cho phép nhiều hệ điều hành phổ biến chia sẻ phần cứng thông thường theo cách an toàn và được quản lý tài nguyên, nhưng không hy sinh cả hiệu năng lẫn chức năng. Điều này đạt được bằng cách cung cấp một sự trừu tượng hóa máy ảo lý tưởng mà các hệ điều hành như Linux, BSD và Windows XP có thể được chuyển sang với nỗ lực tối thiểu.

Thiết kế của chúng tôi hướng tới việc lưu trữ đồng thời tới 100 thể hiện máy ảo trên một server hiện đại. Cách tiếp cận ảo hóa được Xen sử dụng có hiệu quả cực kỳ cao: chúng tôi cho phép các hệ điều hành như Linux và Windows XP được lưu trữ đồng thời với chi phí phụ trội về hiệu năng không đáng kể — nhiều nhất chỉ vài phần trăm so với trường hợp không ảo hóa. Chúng tôi vượt trội đáng kể so với các giải pháp thương mại cạnh tranh và các giải pháp có sẵn miễn phí trong một loạt các phép đo chuẩn vi mô và các kiểm thử trên toàn hệ thống.

Các danh mục và mô tả chủ đề

D.4.1 [Operating Systems]: Quản lý tiến trình; D.4.2 [Operating Systems]: Quản lý lưu trữ; D.4.8 [Operating Systems]: Hiệu năng
