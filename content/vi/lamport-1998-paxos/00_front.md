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
content_sha256: 38d24017e230460c8196de77ecd207851c7284edd54ab9e7c8f64096e48a9cb4
translated_from: content/en/lamport-1998-paxos/00_front.md
source_content_sha256: 6fac3ffae0952fb7c9d43c72bac006ed766ea295dfe0b80314b76a08bf5a7a76
translation_model: gpt-5
translation_run: 20260918T122832Z
glossary_version: 7
glossary_terms_sha256: f834761938c11bca59f7cb79948997ed0706af48cd70392678452699c034a7ad
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Nghị viện Bán thời gian

Leslie Lamport

Bài báo này xuất hiện trong ACM Transactions on Computer Systems 16, 2 (tháng 5 năm 1998), 133-169. Các sửa chữa nhỏ được thực hiện vào ngày 29 tháng 8 năm 2000.

Nghị viện Bán thời gian

LESLIE LAMPORT Digital Equipment Corporation

Những khám phá khảo cổ học gần đây trên đảo Paxos cho thấy nghị viện đã hoạt động bất chấp xu hướng di chuyển liên tục của các nhà lập pháp bán thời gian. Các nhà lập pháp duy trì những bản sao nhất quán của biên bản nghị viện, bất chấp những lần rời khỏi phòng họp thường xuyên của họ và sự đãng trí của các sứ giả. Giao thức của nghị viện Paxon cung cấp một phương pháp mới để triển khai cách tiếp cận máy trạng thái trong việc thiết kế các hệ thống phân tán. Các hạng mục và Bộ mô tả chủ đề: C2.4 [Mạng Truyền thông Máy tính]: Hệ thống phân tán—hệ điều hành mạng; D4.5 [Hệ điều hành]: Độ tin cậy—Khả năng chịu lỗi; J.1 [Xử lý Dữ liệu Hành chính]: Chính phủ Các thuật ngữ chung: Thiết kế, Độ tin cậy Các Từ khóa và Cụm từ bổ sung: Máy trạng thái, cam kết ba pha, bỏ phiếu

Bản gửi này gần đây được phát hiện phía sau một tủ hồ sơ trong văn phòng biên tập TOCS. Mặc dù đã có tuổi đời, tổng biên tập cho rằng nó đáng được xuất bản. Vì tác giả hiện đang tiến hành công việc thực địa tại các đảo Hy Lạp và không thể liên lạc được, tôi được yêu cầu chuẩn bị nó để xuất bản.

Tác giả dường như là một nhà khảo cổ học chỉ có mối quan tâm thoáng qua đến khoa học máy tính. Đây là điều đáng tiếc; mặc dù nền văn minh Paxon cổ đại ít được biết đến mà ông mô tả không mấy được các nhà khoa học máy tính quan tâm, hệ thống lập pháp của nó là một mô hình tuyệt vời cho cách triển khai một hệ thống máy tính phân tán trong một môi trường bất đồng bộ.
