---
paper: codd-1970-relational
title: A Relational Model of Data for Large Shared Data Banks
authors:
  - E. F. Codd
year: 1970
venue: Communications of the ACM
field: databases
section_title: Front Matter
tag: "0034"
kind: front
lang: vi
source: https://www.seas.upenn.edu/~zives/03f/cis550/codd.pdf
pdf_sha256: fa2579f427a4da68466ef159a3ae0c3c1fe4eafec60f73c9f2f40378a65d8ef9
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 1b564cd9b969d6102ba83a4648195e3aee49024ad68989a17d09b7a06f071d80
translated_from: content/en/codd-1970-relational/00_front.md
source_content_sha256: e23f0c2d9064fac25f81260b415860d52e72ef7f9de29d88b36d839a352006a0
translation_model: gpt-5
translation_run: 20260914T163737Z
glossary_version: 6
glossary_terms_sha256: a534ae50d60bff0e03804fd3c150e37d1876484531ab87df9c72dc4d0c455eb2
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
roundtrip: differs-in-wording
roundtrip_run: 20260914T214350Z
---

Mô hình quan hệ của dữ liệu cho các ngân hàng dữ liệu lớn dùng chung

E. F. Codd
Phòng thí nghiệm Nghiên cứu IBM, San Jose, California

Những người dùng tương lai của các ngân hàng dữ liệu lớn phải được bảo vệ khỏi việc phải biết dữ liệu được tổ chức như thế nào trong máy (biểu diễn nội bộ). Một dịch vụ nhắc nhở cung cấp thông tin như vậy không phải là một giải pháp thỏa đáng. Các hoạt động của người dùng tại các thiết bị đầu cuối và hầu hết các chương trình ứng dụng nên không bị ảnh hưởng khi biểu diễn nội bộ của dữ liệu được thay đổi và ngay cả khi một số khía cạnh của biểu diễn bên ngoài được thay đổi. Những thay đổi trong biểu diễn dữ liệu thường sẽ cần thiết do những thay đổi trong lưu lượng truy vấn, cập nhật và báo cáo, cũng như sự phát triển tự nhiên trong các loại thông tin được lưu trữ.

Các hệ thống dữ liệu có định dạng, không suy luận hiện có cung cấp cho người dùng các file có cấu trúc cây hoặc các mô hình mạng tổng quát hơn một chút của dữ liệu. Trong Mục 1, những điểm không đầy đủ của các mô hình này được thảo luận. Một mô hình dựa trên các quan hệ n-ary, một dạng chuẩn cho các quan hệ cơ sở dữ liệu, và khái niệm về một ngôn ngữ con dữ liệu phổ dụng được giới thiệu. Trong Mục 2, một số phép toán trên các quan hệ (khác với suy luận logic) được thảo luận và áp dụng vào các vấn đề về dư thừa và tính nhất quán trong mô hình của người dùng.

TỪ KHÓA VÀ CỤM TỪ: ngân hàng dữ liệu, cơ sở dữ liệu, cấu trúc dữ liệu, tổ chức dữ liệu, các phân cấp của dữ liệu, các mạng của dữ liệu, các quan hệ, khả năng suy ra, dư thừa, tính nhất quán, phép hợp thành, phép nối, ngôn ngữ truy xuất, phép tính vị từ, bảo mật, tính toàn vẹn dữ liệu
PHÂN LOẠI CR: 3.70, 3.73, 3.75, 4.20, 4.22, 4.29
