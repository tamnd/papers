---
paper: backus-1978-vonneumann
title: Can Programming Be Liberated from the von Neumann Style? A Functional Style and Its Algebra of Programs
authors:
  - John Backus
year: 1978
venue: Communications of the ACM (Turing Award lecture)
field: languages
section_title: Front Matter
tag: "0049"
kind: front
lang: vi
source: https://www.cs.cmu.edu/~crary/819-f09/Backus78.pdf
pdf_sha256: 2e412a7986c7fd1bdd060d90d035faa9ecc8a29675f99206c243da90954ca423
pdf_pages: 1-2
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 32abfed755c348f6012e609daae0652451ec96e6ccd53fa35f8f78f23aa917ec
translated_from: content/en/backus-1978-vonneumann/00_front.md
source_content_sha256: 752feced1622b510f0705492c1cbfb9e3b6bd628b154c0b11f2d80acdd041ccc
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: e18583cfd8910711c2e3aa00f134fd0de9487b97e78e37da9096be4297760e66
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
roundtrip: same
roundtrip_run: 20260914T214350Z
---

Lập trình có thể được giải phóng khỏi phong cách von Neumann? Phong cách hàm và đại số chương trình của nó

John Backus

Phòng thí nghiệm Nghiên cứu IBM, San Jose

Các ngôn ngữ lập trình truyền thống ngày càng trở nên đồ sộ, nhưng không mạnh hơn. Những khiếm khuyết vốn có ở cấp độ cơ bản nhất khiến chúng vừa cồng kềnh vừa yếu kém: phong cách lập trình nguyên thủy, xử lý từng từ một, kế thừa từ tổ tiên chung của chúng — máy tính von Neumann; sự gắn kết chặt chẽ giữa ngữ nghĩa và các chuyển tiếp trạng thái; sự phân chia việc lập trình thành thế giới của các biểu thức và thế giới của các câu lệnh; sự bất lực trong việc sử dụng hiệu quả các dạng kết hợp mạnh mẽ để xây dựng những chương trình mới từ các chương trình hiện có; và sự thiếu vắng các tính chất toán học hữu ích cho việc suy luận về chương trình.

Một phong cách lập trình hàm thay thế được xây dựng dựa trên việc sử dụng các dạng kết hợp để tạo ra chương trình. Các chương trình hàm xử lý dữ liệu có cấu trúc, thường không lặp lại và không đệ quy, được xây dựng theo cấp bậc, không đặt tên cho các đối số, và không đòi hỏi cơ chế phức tạp của các khai báo thủ tục để trở nên có khả năng áp dụng tổng quát. Các dạng kết hợp có thể sử dụng những chương trình cấp cao để xây dựng các chương trình còn cấp cao hơn theo một phong cách không thể thực hiện trong các ngôn ngữ truyền thống.

Gắn liền với phong cách lập trình hàm là một đại số chương trình, trong đó các biến nhận giá trị là các chương trình và các phép toán là những dạng kết hợp. Đại số này có thể được sử dụng để biến đổi chương trình và giải các phương trình mà “ẩn số” là các chương trình, theo cách tương tự như việc biến đổi các phương trình trong đại số trung học.
