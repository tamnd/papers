---
paper: lamport-1998-paxos
title: The Part-Time Parliament
authors:
  - Leslie Lamport
year: 1998
venue: ACM TOCS
field: systems
section_title: Front Matter
tag: "0002"
kind: front
lang: vi
source: https://lamport.azurewebsites.net/pubs/lamport-paxos.pdf
pdf_sha256: cd9544e9615bcd417a2c10063671cecca0b28ad4bc5db3f64467a83ecc7028d3
pdf_pages: 1-3
extraction: native
extraction_model: pdftotext version 26.09.0
content_sha256: 408749b01d2ba8218a6df982ef94a8f9936c4e85de5be07fe257b88d066c9338
translated_from: content/en/lamport-1998-paxos/00_front.md
source_content_sha256: 6fac3ffae0952fb7c9d43c72bac006ed766ea295dfe0b80314b76a08bf5a7a76
translation_model: gpt-5
translation_run: 20260914T155352Z
glossary_version: 6
glossary_terms_sha256: afc6de5d010821f75553a129f8b55d5fbabc0d9d7af198021ca9a5a496de4088
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Nghị viện Bán thời gian

Leslie Lamport

Bài báo này xuất hiện trên ACM Transactions on Computer Systems 16, 2 (May 1998), 133-169. Các sửa chữa nhỏ được thực hiện vào ngày 29 tháng 8 năm 2000.

Nghị viện Bán thời gian

LESLIE LAMPORT Digital Equipment Corporation

Những phát hiện khảo cổ học gần đây trên đảo Paxos cho thấy nghị viện vẫn hoạt động bất chấp khuynh hướng nay đây mai đó của các nghị sĩ bán thời gian. Các nghị sĩ duy trì những bản sao nhất quán của hồ sơ nghị viện, bất chấp việc thường xuyên rời khỏi phòng họp và sự đãng trí của những người đưa tin. Giao thức của nghị viện Paxon cung cấp một phương thức mới để triển khai cách tiếp cận máy trạng thái trong thiết kế các hệ thống phân tán. Phân loại và Mô tả Chủ đề: C2.4 [Mạng Máy tính]: Hệ thống phân tán—Hệ điều hành mạng; D4.5 [Hệ điều hành]: Độ tin cậy—Khả năng chịu lỗi; J.1 [Xử lý Dữ liệu Hành chính]: Chính phủ Các thuật ngữ chung: Thiết kế, Độ tin cậy Các từ khóa và cụm từ bổ sung: Máy trạng thái, commit ba pha, biểu quyết

Bản thảo này gần đây được phát hiện phía sau một tủ hồ sơ trong văn phòng biên tập TOCS. Mặc dù đã có tuổi, tổng biên tập cho rằng nó đáng được xuất bản. Vì tác giả hiện đang tiến hành công tác thực địa tại các đảo của Hy Lạp và không thể liên lạc được, tôi được yêu cầu chuẩn bị bản thảo để xuất bản.

Tác giả có vẻ là một nhà khảo cổ học chỉ có mối quan tâm thoáng qua đến khoa học máy tính. Điều này thật đáng tiếc; mặc dù nền văn minh Paxon cổ đại ít được biết đến mà ông mô tả không mấy được hầu hết các nhà khoa học máy tính quan tâm, hệ thống lập pháp của nó là một mô hình tuyệt vời cho cách triển khai một hệ thống máy tính phân tán trong môi trường không đồng bộ.
