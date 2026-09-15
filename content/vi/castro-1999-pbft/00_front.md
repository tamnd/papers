---
paper: castro-1999-pbft
title: Practical Byzantine Fault Tolerance
authors:
  - Miguel Castro
  - Barbara Liskov
year: 1999
venue: OSDI
field: security
section_title: Front Matter
tag: 019D
kind: front
lang: vi
source: https://www.scs.stanford.edu/nyu/03sp/sched/bfs.pdf
pdf_sha256: 9b8d5842c967894eaa2d6aa71d4354d26c4f76880f859a117d96042b4a37efc1
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 32fe80f48b35d53102063ba0159be1a53231c60c9cf693d0a13ef90d8184e512
translated_from: content/en/castro-1999-pbft/00_front.md
source_content_sha256: 555608472de6d22cb9812146bcf369656a4deab92299471d17ba4537082c9bb6
translation_model: gpt-5
translation_run: 20260915T013833Z
glossary_version: 6
glossary_terms_sha256: 363c21723d588ca6b8032fd3e2b0aa8dc6ab225b1f9ca1b6e98d75976e8b0d0a
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Khả năng chịu lỗi Byzantine thực tế

Miguel Castro và Barbara Liskov
Phòng thí nghiệm Khoa học Máy tính,
Viện Công nghệ Massachusetts,
545 Technology Square, Cambridge, MA 02139
{castro,liskov}@lcs.mit.edu

Tóm tắt
Bài báo này mô tả một thuật toán sao chép mới có khả năng chịu được các sự cố Byzantine. Chúng tôi tin rằng các thuật toán chịu sự cố Byzantine sẽ ngày càng trở nên quan trọng trong tương lai vì các cuộc tấn công độc hại và lỗi phần mềm ngày càng phổ biến, đồng thời có thể khiến các nút bị lỗi thể hiện hành vi tùy ý. Trong khi các thuật toán trước đây giả định một hệ thống đồng bộ hoặc quá chậm để được sử dụng trong thực tế, thuật toán được mô tả trong bài báo này mang tính thực tiễn: nó hoạt động trong các môi trường không đồng bộ như Internet và tích hợp một số tối ưu hóa quan trọng giúp cải thiện thời gian đáp ứng của các thuật toán trước đây hơn một bậc độ lớn. Chúng tôi đã triển khai một dịch vụ NFS chịu sự cố Byzantine bằng cách sử dụng thuật toán của mình và đo hiệu năng của nó. Kết quả cho thấy dịch vụ của chúng tôi chỉ chậm hơn 3% so với một NFS chuẩn không sao chép.
