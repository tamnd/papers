---
paper: stoica-2001-chord
title: 'Chord: A Scalable Peer-to-peer Lookup Service for Internet Applications'
authors:
  - Ion Stoica
  - Robert Morris
  - David Karger
  - M. Frans Kaashoek
  - Hari Balakrishnan
year: 2001
venue: SIGCOMM
field: networks
section_title: Front Matter
tag: "0174"
kind: front
lang: vi
source: https://pdos.csail.mit.edu/papers/chord:sigcomm01/chord_sigcomm.pdf
pdf_sha256: cca4ae7873ac128b7b9034b2c3fbf32f7d84541a88b5e70d0c7c1ce1d6381fe8
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 9ecbaac421c5b407435fbc9e84a115bbde9f1a24e50d6365f7c6ff354eb9f7c6
translated_from: content/en/stoica-2001-chord/00_front.md
source_content_sha256: 86165771a8378397bd37b4dea450176c7f140f2d894c5eb147012a6356016637
translation_model: gpt-5
translation_run: 20260918T122832Z
glossary_version: 7
glossary_terms_sha256: 5bfb74d0e4b3e9a8237f78ceae59e221549684c174791655271c5455f7fd5e4e
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Chord: Một Dịch vụ Tra cứu Peer-to-peer Có khả năng Mở rộng cho các Ứng dụng Internet

Ion Stoica\*, Robert Morris, David Karger, M. Frans Kaashoek, Hari Balakrishnan†
MIT Laboratory for Computer Science
chord@lcs.mit.edu
http://pdos.lcs.mit.edu/chord/

Tóm tắt
Một vấn đề cơ bản mà các ứng dụng peer-to-peer phải đối mặt là định vị hiệu quả nút lưu trữ một mục dữ liệu cụ thể. Bài báo này trình bày Chord, một giao thức tra cứu phân tán giải quyết vấn đề này. Chord chỉ hỗ trợ một thao tác duy nhất: với một khóa cho trước, nó ánh xạ khóa đó tới một nút. Việc định vị dữ liệu có thể dễ dàng được triển khai trên Chord bằng cách liên kết một khóa với mỗi mục dữ liệu và lưu cặp khóa/mục dữ liệu tại nút mà khóa ánh xạ tới. Chord thích nghi hiệu quả khi các nút tham gia và rời khỏi hệ thống, đồng thời có thể trả lời các truy vấn ngay cả khi hệ thống liên tục thay đổi. Các kết quả từ phân tích lý thuyết, mô phỏng và thử nghiệm cho thấy Chord có khả năng mở rộng, với chi phí truyền thông và trạng thái được duy trì bởi mỗi nút tăng theo cấp số logarit với số lượng nút Chord.
