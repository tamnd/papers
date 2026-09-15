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
content_sha256: e4dd3ed8c12113a300f7c4afa3dd1cfe6dbba9d970bd0304998877f051bb4ff9
translated_from: content/en/milner-1978-polymorphism/00_front.md
source_content_sha256: f186118ecc03ae8a65a7764a7180869a64c08786d13302e0e0b992a44a79637c
translation_model: gpt-5
translation_run: 20260915T062339Z
glossary_version: 6
glossary_terms_sha256: e18583cfd8910711c2e3aa00f134fd0de9487b97e78e37da9096be4297760e66
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Một lý thuyết về đa hình kiểu trong lập trình

Trích dẫn cho phiên bản đã xuất bản:

Milner, R 1978, 'A theory of type polymorphism in programming', Journal of Computer and System Sciences, vol. 17, no. 3, pp. 348-375. https://doi.org/10.1016/0022-0000(78)90014-4

Mã định danh đối tượng số (DOI):

10.1016/0022-0000(78)90014-4

Liên kết:

Liên kết đến bản ghi xuất bản trong Edinburgh Research Explorer

Phiên bản tài liệu:

PDF của nhà xuất bản, còn được gọi là Phiên bản ghi nhận

Được xuất bản trong:

Journal of Computer and System Sciences

Quyền chung

Bản quyền đối với các ấn phẩm được cung cấp thông qua Edinburgh Research Explorer thuộc về (các) tác giả và / hoặc (các) chủ sở hữu bản quyền khác và người dùng có trách nhiệm nhận biết và tuân thủ các yêu cầu pháp lý liên quan đến các quyền này.

Chính sách gỡ bỏ

The University of Edinburgh đã thực hiện mọi nỗ lực hợp lý để đảm bảo rằng Edinburgh Research Explorer tuân thủ luật pháp Vương quốc Anh. Nếu bạn tin rằng việc công khai tệp này vi phạm bản quyền, vui lòng liên hệ openaccess@ed.ac.uk cung cấp thông tin chi tiết, và chúng tôi sẽ gỡ quyền truy cập công khai đối với tác phẩm ngay lập tức và điều tra khiếu nại của bạn.

ROBIN MILNER

Khoa Khoa học Máy tính, University of Edinburgh, Edinburgh, Scotland

Nhận ngày 10 tháng 10 năm 1977; sửa đổi ngày 19 tháng 4 năm 1978

Mục tiêu của công trình này phần lớn mang tính thực tiễn. Một phong cách lập trình được sử dụng rộng rãi, đặc biệt trong các ngôn ngữ xử lý cấu trúc không áp đặt kỷ luật về kiểu, bao gồm việc định nghĩa các thủ tục hoạt động tốt trên các đối tượng thuộc nhiều loại khác nhau. Chúng tôi trình bày một kỷ luật kiểu hình thức cho các thủ tục đa hình như vậy trong ngữ cảnh của một ngôn ngữ lập trình đơn giản, và một thuật toán kiểm tra kiểu tại thời điểm biên dịch $\mathcal{W}$ thực thi kỷ luật này.
