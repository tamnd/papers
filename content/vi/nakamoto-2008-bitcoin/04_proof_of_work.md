---
paper: nakamoto-2008-bitcoin
title: 'Bitcoin: A Peer-to-Peer Electronic Cash System'
authors:
  - Satoshi Nakamoto
year: 2008
venue: bitcoin.org
field: security
section: "4"
section_title: Bằng chứng công việc
tag: "0008"
kind: section
lang: vi
source: https://bitcoin.org/bitcoin.pdf
pdf_sha256: b1674191a88ec5cdd733e4240a81803105dc412d6c6708d53ab94fc248f4f553
pdf_pages: "3"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: aeab4c95c4a87a1b5ae1d0ded1ac4a6d03199ea14bc378aa98e7fad948dca7ab
translated_from: content/en/nakamoto-2008-bitcoin/04_proof_of_work.md
source_content_sha256: ad0c83dbc7cfba887e3e637af3734120086b6e5f48eb68340eec3d9329864427
translation_model: gpt-5
translation_run: 20260915T022520Z
glossary_version: 6
glossary_terms_sha256: 363c21723d588ca6b8032fd3e2b0aa8dc6ab225b1f9ca1b6e98d75976e8b0d0a
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Để triển khai một server dấu thời gian phân tán trên cơ sở ngang hàng, chúng tôi sẽ cần sử dụng một hệ thống bằng chứng công việc (proof-of-work) tương tự như Hashcash của Adam Back [6], thay vì các bài đăng trên báo hoặc Usenet. Bằng chứng công việc bao gồm việc tìm kiếm một giá trị mà khi được băm, chẳng hạn như với SHA-256, giá trị băm bắt đầu bằng một số lượng bit 0. Công việc trung bình cần thiết tăng theo hàm mũ với số lượng bit 0 được yêu cầu và có thể được xác minh bằng cách thực thi một lần băm duy nhất.

Đối với mạng dấu thời gian của chúng tôi, chúng tôi triển khai bằng chứng công việc bằng cách tăng dần một nonce trong khối cho đến khi tìm thấy một giá trị khiến giá trị băm của khối có số lượng bit 0 cần thiết. Một khi nỗ lực CPU đã được tiêu tốn để khiến nó thỏa mãn bằng chứng công việc, khối không thể được thay đổi nếu không thực hiện lại công việc. Khi các khối sau được nối chuỗi sau nó, công việc để thay đổi khối sẽ bao gồm việc thực hiện lại tất cả các khối sau nó.

Hình.

Bằng chứng công việc cũng giải quyết vấn đề xác định biểu diễn trong việc ra quyết định theo đa số. Nếu đa số được dựa trên một-IP-address-một-phiếu-bầu, nó có thể bị phá hoại bởi bất kỳ ai có khả năng cấp phát nhiều IP. Bằng chứng công việc về cơ bản là một-CPU-một-phiếu-bầu. Quyết định theo đa số được biểu diễn bởi chuỗi dài nhất, chuỗi có nỗ lực bằng chứng công việc lớn nhất được đầu tư vào đó. Nếu đa số sức mạnh CPU được kiểm soát bởi các nút trung thực, chuỗi trung thực sẽ phát triển nhanh nhất và vượt qua mọi chuỗi cạnh tranh. Để sửa đổi một khối trước đó, kẻ tấn công sẽ phải thực hiện lại bằng chứng công việc của khối đó và tất cả các khối sau nó, sau đó bắt kịp và vượt qua công việc của các nút trung thực. Chúng tôi sẽ chỉ ra sau rằng xác suất một kẻ tấn công chậm hơn bắt kịp giảm theo hàm mũ khi các khối tiếp theo được thêm vào.

Để bù đắp cho tốc độ phần cứng ngày càng tăng và sự quan tâm thay đổi trong việc chạy các nút theo thời gian, độ khó của bằng chứng công việc được xác định bởi một trung bình trượt nhằm đạt được một số lượng khối trung bình mỗi giờ. Nếu chúng được tạo ra quá nhanh, độ khó sẽ tăng lên.
