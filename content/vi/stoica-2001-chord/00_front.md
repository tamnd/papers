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
content_sha256: 45750085e87b74081ee1eac0cc229e1e58b29d2a80cbd21bbe7b6e971e968fae
translated_from: content/en/stoica-2001-chord/00_front.md
source_content_sha256: 86165771a8378397bd37b4dea450176c7f140f2d894c5eb147012a6356016637
translation_model: gpt-5
translation_run: 20260914T163737Z
glossary_version: 6
glossary_terms_sha256: 3a5b9dd3cd6211761c92d70db4c4910c364b1cae9e5e732eea77349f449c860b
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
roundtrip: same
roundtrip_run: 20260914T214350Z
---

Chord: Dịch vụ tra cứu ngang hàng (Peer-to-peer) có khả năng mở rộng cho các ứng dụng Internet

Ion Stoica\*, Robert Morris, David Karger, M. Frans Kaashoek, Hari Balakrishnan†
MIT Laboratory for Computer Science
chord\@lcs.mit.edu
http://pdos.lcs.mit.edu/chord/

Tóm tắt
Một vấn đề cơ bản mà các ứng dụng ngang hàng (peer-to-peer) phải đối mặt là xác định hiệu quả nút lưu trữ một mục dữ liệu cụ thể. Bài báo này trình bày Chord, một giao thức tra cứu phân tán giải quyết vấn đề này. Chord chỉ hỗ trợ một thao tác: với một khóa cho trước, nó ánh xạ khóa đó tới một nút. Việc định vị dữ liệu có thể dễ dàng được triển khai trên Chord bằng cách gắn một khóa với mỗi mục dữ liệu và lưu cặp khóa/mục dữ liệu tại nút mà khóa ánh xạ tới. Chord thích ứng hiệu quả khi các nút tham gia và rời khỏi hệ thống, đồng thời có thể trả lời các truy vấn ngay cả khi hệ thống liên tục thay đổi. Kết quả từ phân tích lý thuyết, mô phỏng và thực nghiệm cho thấy Chord có khả năng mở rộng, với chi phí truyền thông và trạng thái được duy trì bởi mỗi nút tăng theo hàm logarithm của số lượng nút Chord.
