---
paper: hamming-1950-codes
title: Error Detecting and Error Correcting Codes
authors:
  - Richard W. Hamming
year: 1950
venue: Bell System Technical Journal
field: theory
section_title: Front Matter
tag: "0036"
kind: front
lang: vi
source: https://archive.org/download/bstj29-2-147/bstj29-2-147.pdf
pdf_sha256: 32f13768d0e37bcc482517d3e1f50f9309d6db65e145edc476622c435829bdad
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 659ab362cc4122c4c65f69df49c3a567257a703a4a5034efe42345c6b9fb6b6a
translated_from: content/en/hamming-1950-codes/00_front.md
source_content_sha256: 971d65afaa79d5bb3cdb5a51fe6f8e1e8c181d48d9030e299fd3fe9b93bfa1a9
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: 6d9e5417e9b1c2ea0332cc910589a2f1f7989033c37ee6d1610f4912cdc9e218
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Mã phát hiện lỗi và mã sửa lỗi

Bởi R. W. HAMMING

1. Giới thiệu

Tác giả được dẫn dắt đến nghiên cứu được trình bày trong bài báo này từ việc xem xét các máy tính quy mô lớn, trong đó một số lượng lớn phép toán phải được thực hiện mà không có một lỗi nào trong kết quả cuối cùng. Vấn đề "thực hiện đúng mọi việc" ở quy mô lớn này về cơ bản không phải là mới; chẳng hạn, trong một tổng đài điện thoại, một số lượng rất lớn phép toán được thực hiện trong khi các lỗi dẫn đến các số sai được kiểm soát rất chặt chẽ, mặc dù chúng chưa được loại bỏ hoàn toàn. Điều này đã đạt được một phần thông qua việc sử dụng các mạch tự kiểm tra. Sự cố không thường xuyên thoát khỏi việc kiểm tra định kỳ vẫn được khách hàng phát hiện và sẽ, nếu kéo dài, dẫn đến khiếu nại của khách hàng, trong khi nếu nó là tạm thời thì nó chỉ tạo ra các số sai không thường xuyên. Đồng thời, các chức năng còn lại của tổng đài vẫn hoạt động thỏa đáng. Mặt khác, trong một máy tính số, một sự cố đơn lẻ thường có nghĩa là sự hỏng hóc hoàn toàn, theo nghĩa rằng nếu nó được phát hiện thì không thể thực hiện thêm tính toán nào cho đến khi sự cố được xác định và sửa chữa, còn nếu nó thoát khỏi việc phát hiện thì nó làm vô hiệu hóa tất cả các phép toán tiếp theo của máy.
