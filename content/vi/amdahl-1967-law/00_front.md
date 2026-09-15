---
paper: amdahl-1967-law
title: Validity of the Single Processor Approach to Achieving Large Scale Computing Capabilities
authors:
  - Gene M. Amdahl
year: 1967
venue: AFIPS Spring Joint Computer Conference
field: architecture
section_title: Front Matter
tag: "0003"
kind: front
lang: vi
source: https://www3.cs.stonybrook.edu/~rezaul/Spring-2012/CSE613/reading/Amdahl-1967.pdf
pdf_sha256: 81a363deb884ca23e495280eb9229df1064b4b3f79d662f270be35b50bea5318
pdf_pages: "1"
extraction: native
extraction_model: pdftotext version 24.02.0
content_sha256: 4872d88e30a0138e9167c774737ab1959805ba9e5c2f73e426dff9882de6aefb
translated_from: content/en/amdahl-1967-law/00_front.md
source_content_sha256: 080d937afdb838b5b3ba5e349fdd9401e761ffa730c10c526cde8d0f7b2dfa9f
translation_model: gpt-5
translation_run: 20260915T090439Z
glossary_version: 6
glossary_terms_sha256: 1f83355a83baacb04f1185b8bd47b133f28d2f764f5d7ae919d5d9d0d7e083ee
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

TÀI LIỆU KỸ THUẬT

Tính hợp lệ của phương pháp bộ xử lý đơn trong việc

Đạt được các khả năng tính toán quy mô lớn

In lại từ AFIPS Conference Proceedings, Vol. 30 (Atlantic City, N.J., Apr. 18–20), AFIPS Press, Reston, Va., 1967, pp. 483–485, khi Dr. Amdahl đang làm việc tại International

Business Machines Corporation, Sunnyvale, California

Dr. Gene M. Amdahl

Bài báo này là công bố đầu tiên của Gene Amdahl về điều sau này được biết đến là Định luật Amdahl. Điều thú vị là bài báo không có phương trình nào và chỉ có một hình duy nhất. Trong số báo này của SSCS News, Dr. Amdahl đã đồng ý vẽ lại hình đó. Trong bản sao cứng hiện có, hình này không thể đọc được. Chúng tôi in lại bài báo lịch sử này để cho phép các thành viên đọc nguồn gốc ban đầu từ khoảng 40 năm trước.

Các biên tập viên

Trong hơn một thập kỷ, các nhà tiên tri đã nêu lên quan điểm rằng tổ chức của một máy tính đơn đã đạt đến giới hạn của nó và những tiến bộ thực sự đáng kể chỉ có thể đạt được bằng cách kết nối nhiều máy tính theo một phương thức cho phép giải quyết hợp tác. Theo nhiều cách khác nhau, hướng đi đúng đã được chỉ ra là các máy tính mục đích chung với sự kết nối tổng quát của các bộ nhớ, hoặc các máy tính chuyên dụng với các kết nối bộ nhớ có quan hệ hình học và được điều khiển bởi một hoặc nhiều luồng lệnh.

Việc chứng minh được đưa ra về tính hợp lệ tiếp tục của phương pháp bộ xử lý đơn và những điểm yếu của phương pháp đa bộ xử lý xét theo việc áp dụng vào các vấn đề thực tế cùng những tính bất thường đi kèm.

Các lập luận được trình bày dựa trên các đặc tính thống kê của tính toán trên máy tính trong thập kỷ vừa qua và dựa trên các yêu cầu vận hành bên trong những vấn đề có ý nghĩa vật lý. Một tài liệu tham khảo bổ sung sẽ là một trong những phân tích toàn diện nhất hiện được công bố về các khả năng tương đối của máy tính - "Changes in Computer Performance," Datamation, September 1966, Professor Kenneth E. Knight, Stanford School of Business Administration.

Mùa hè 2007

Đặc tính đầu tiên được quan tâm là phần tỷ lệ của tải tính toán liên quan đến các công việc quản lý dữ liệu. Phần này gần như không đổi trong khoảng mười năm, và chiếm 40% số lệnh đã thực thi trong các lần chạy sản xuất. Trong một môi trường chuyên dụng hoàn toàn, điều này có thể được giảm đi một hệ số hai, nhưng rất khó có khả năng giảm đi một hệ số ba. Bản chất của chi phí phụ trội này có vẻ là tuần tự, do đó khó có khả năng phù hợp với các kỹ thuật xử lý song song. Chỉ riêng chi phí phụ trội sẽ đặt một giới hạn trên cho thông lượng ở mức gấp năm đến bảy lần tốc độ xử lý tuần tự, ngay cả khi các công việc quản lý được thực hiện trong một bộ xử lý riêng biệt. Phần không phải công việc quản lý của vấn đề nhiều nhất chỉ có thể khai thác một bộ xử lý có hiệu năng gấp ba đến bốn lần hiệu năng của bộ xử lý quản lý. Một kết luận khá rõ ràng có thể rút ra tại thời điểm này là nỗ lực dành cho việc đạt được tốc độ xử lý song song cao sẽ bị lãng phí trừ khi đi kèm với những thành tựu về tốc độ xử lý tuần tự gần như cùng mức độ.

Công việc quản lý dữ liệu không phải là vấn đề duy nhất gây khó khăn cho các phương pháp đơn giản hóa quá mức đối với tính toán tốc độ cao. Các vấn đề vật lý có ý nghĩa thực tiễn thường có những phức tạp khá đáng kể. Ví dụ về các phức tạp này như sau: Các biên có khả năng không đều; các vùng bên trong có khả năng không đồng nhất; các phép tính cần thiết có thể phụ thuộc vào các trạng thái của các biến tại mỗi điểm; tốc độ lan truyền của các hiệu ứng vật lý khác nhau có thể rất khác nhau; tốc độ hội tụ, hoặc việc có hội tụ hay không, có thể

phụ thuộc mạnh vào việc quét qua mảng dọc theo các trục khác nhau trong các lượt tiếp theo, v.v. Ảnh hưởng của mỗi phức tạp này là rất nghiêm trọng đối với bất kỳ tổ chức máy tính nào dựa trên các bộ xử lý có quan hệ hình học trong một hệ thống xử lý song song. Ngay cả sự tồn tại của các biên hình chữ nhật đều cũng có tính chất thú vị rằng với chiều không gian là N thì có 3N hình học điểm khác nhau cần được xử lý trong một phép tính với láng giềng gần nhất. Nếu láng giềng gần thứ hai cũng được đưa vào, sẽ có 5N hình học điểm khác nhau cần xem xét. Một biên không đều làm phức tạp thêm vấn đề này, cũng như một vùng bên trong không đồng nhất. Các phép tính phụ thuộc vào trạng thái của các biến sẽ yêu cầu việc xử lý tại mỗi điểm tiêu tốn xấp xỉ cùng thời gian tính toán như tổng của các phép tính của tất cả các hiệu ứng vật lý trong một vùng lớn. Những khác biệt hoặc thay đổi trong tốc độ lan truyền có thể ảnh hưởng đến các quan hệ điểm lưới.

Lý tưởng nhất, việc tính toán tác động của các điểm lân cận lên điểm đang được xem xét liên quan đến các giá trị của chúng tại một thời điểm trước đó tỷ lệ thuận với khoảng cách lưới và tỷ lệ nghịch với tốc độ lan truyền. Vì bước thời gian thường được giữ không đổi, tốc độ lan truyền nhanh hơn đối với một số hiệu ứng sẽ hàm ý các tương tác với những điểm ở xa hơn. Cuối cùng, thực hành khá phổ biến là quét qua lưới dọc theo các trục khác nhau trong các lượt tiếp theo đặt ra các vấn đề về quản lý dữ liệu ảnh hưởng đến tất cả các bộ xử lý; tuy nhiên, nó ảnh hưởng nghiêm trọng hơn đến các bộ xử lý có quan hệ hình học bằng cách yêu cầu chuyển vị tất cả các điểm trong bộ nhớ lưu trữ ngoài việc lập lịch đầu vào-đầu ra đã được sửa đổi. Một đánh giá thực tế về

IEEE SSCS NEWS 19
