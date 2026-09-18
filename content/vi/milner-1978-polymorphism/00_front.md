---
paper: milner-1978-polymorphism
title: A Theory of Type Polymorphism in Programming
authors:
  - Robin Milner
year: 1978
venue: Journal of Computer and System Sciences
field: languages
section_title: Front Matter
tag: "0048"
kind: front
lang: vi
source: https://doi.org/10.1016/0022-0000(78)90014-4
pdf_sha256: a55f1fb81848085165c55a73c33f28b5d25f3b7bdcfa782c462af7997faad6bc
pdf_pages: 1-2
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: de54766b9e1b947a9b97bf4d28bc08f4b2971ca707444f03f3a1d2ec145ad0cf
translated_from: content/en/milner-1978-polymorphism/00_front.md
source_content_sha256: f186118ecc03ae8a65a7764a7180869a64c08786d13302e0e0b992a44a79637c
translation_model: gpt-5
translation_run: 20260918T122832Z
glossary_version: 7
glossary_terms_sha256: 61df191034dbc0d2b4fd3d0e6780a45e637697c607e59ad493d8021ee078cd25
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

A theory of type polymorphism in programming

Trích dẫn cho phiên bản đã xuất bản:

Milner, R 1978, 'A theory of type polymorphism in programming', Journal of Computer and System Sciences, vol. 17, no. 3, pp. 348-375. https://doi.org/10.1016/0022-0000(78)90014-4

Mã định danh đối tượng số (DOI):

10.1016/0022-0000(78)90014-4

Liên kết:

Liên kết tới bản ghi xuất bản trong Edinburgh Research Explorer

Phiên bản tài liệu:

PDF của nhà xuất bản, còn được gọi là phiên bản chính thức

Được xuất bản trong:

Journal of Computer and System Sciences

Quyền chung

Bản quyền đối với các ấn phẩm được cung cấp thông qua Edinburgh Research Explorer thuộc về tác giả và / hoặc các chủ sở hữu bản quyền khác và là điều kiện để người dùng các ấn phẩm này công nhận và tuân thủ các yêu cầu pháp lý liên quan đến các quyền này.

Chính sách gỡ xuống

Đại học Edinburgh đã nỗ lực hợp lý để đảm bảo rằng Edinburgh Research Explorer tuân thủ luật pháp Vương quốc Anh. Nếu bạn tin rằng việc công khai tệp này vi phạm bản quyền, vui lòng liên hệ openaccess@ed.ac.uk và cung cấp chi tiết, chúng tôi sẽ gỡ quyền truy cập và điều tra vấn đề.

ROBIN MILNER

Khoa Khoa học Máy tính, Đại học Edinburgh, Edinburgh, Scotland

Nhận ngày 10 tháng 10 năm 1977; sửa đổi ngày 19 tháng 4 năm 1978

Mục tiêu của công trình này phần lớn mang tính thực tiễn. Một phong cách lập trình được sử dụng rộng rãi, đặc biệt trong các ngôn ngữ xử lý cấu trúc không áp đặt kỷ luật về kiểu, bao hàm việc định nghĩa các thủ tục hoạt động tốt trên các đối tượng thuộc nhiều loại khác nhau. Chúng tôi trình bày một kỷ luật kiểu hình thức cho các thủ tục đa hình như vậy trong ngữ cảnh của một ngôn ngữ lập trình đơn giản, cùng với một thuật toán kiểm tra kiểu tại thời điểm biên dịch $\mathcal{W}$ thực thi kỷ luật này.
