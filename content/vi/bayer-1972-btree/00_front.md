---
paper: bayer-1972-btree
title: Organization and Maintenance of Large Ordered Indices
authors:
  - Rudolf Bayer
  - Edward M. McCreight
year: 1972
venue: Acta Informatica
field: databases
section_title: Front Matter
tag: "0055"
kind: front
lang: vi
source: https://infolab.usc.edu/csci585/Spring2010/den_ar/indexing.pdf
pdf_sha256: 69826c036d7948fe5b02f7498620c90cc6a8de2504251a57994d13dc7b14e470
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 10ab3ada2d7ed6959a624ad367b4c301cef37c01ea277cc302961c045c5948c8
translated_from: content/en/bayer-1972-btree/00_front.md
source_content_sha256: 7c93793b3f151d03a0aa9a66f01c36b220f01eb08bb461b0fa0bcdf149fd0a81
translation_model: gpt-5
translation_run: 20260914T163737Z
glossary_version: 6
glossary_terms_sha256: a534ae50d60bff0e03804fd3c150e37d1876484531ab87df9c72dc4d0c455eb2
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
roundtrip: same
roundtrip_run: 20260914T214350Z
---

TỔ CHỨC VÀ BẢO TRÌ CÁC CHỈ MỤC LỚN CÓ THỨ TỰ bởi

R. Bayer và

E. McCreight

Báo cáo Toán học và Khoa học Thông tin Số 20

Phòng thí nghiệm Toán học và Khoa học Thông tin

CÁC PHÒNG THÍ NGHIỆM NGHIÊN CỨU KHOA HỌC BOEING

Tháng 7 năm 1970

TÓM TẮT

Việc tổ chức và bảo trì một chỉ mục cho một file truy cập ngẫu nhiên động được xem xét. Giả sử rằng chỉ mục phải được lưu giữ trên một bộ lưu trữ dự phòng truy cập ngẫu nhiên giả như đĩa hoặc trống. Tổ chức chỉ mục được mô tả cho phép truy xuất, chèn và xóa các khóa trong thời gian tỷ lệ với $\log_k I$ trong đó $I$ là kích thước của chỉ mục và $k$ là một số tự nhiên phụ thuộc vào thiết bị sao cho hiệu năng của lược đồ trở nên gần tối ưu. Việc sử dụng bộ nhớ lưu trữ ít nhất là 50% nhưng nhìn chung cao hơn nhiều. Các trang của chỉ mục được tổ chức trong một cấu trúc dữ liệu đặc biệt, được gọi là cây B. Lược đồ được phân tích, các cận hiệu năng được thu nhận, và một $k$ gần tối ưu được tính toán. Các thí nghiệm đã được thực hiện với các chỉ mục có tới 100,000 khóa. Một chỉ mục có kích thước 15,000 (100,000) có thể được duy trì với trung bình 9 (ít nhất 4) giao dịch mỗi giây trên một IBM 360/44 với một đĩa 2311.

Từ khóa và Cụm từ: Cấu trúc dữ liệu, file truy cập ngẫu nhiên, bảo trì chỉ mục động, chèn khóa, xóa khóa, truy xuất khóa, phân trang, truy xuất thông tin.

Phân loại CR: 3.70, 3.73, 3.74.

1. Giới thiệu

Trong bài báo này, chúng tôi xem xét vấn đề tổ chức và bảo trì một chỉ mục cho một file truy cập ngẫu nhiên thay đổi động.
