---
paper: corbett-2012-spanner
title: 'Spanner: Google''s Globally-Distributed Database'
authors:
  - James C. Corbett
  - Jeffrey Dean
  - Michael Epstein
  - Andrew Fikes
  - Christopher Frost
  - J. J. Furman
  - Sanjay Ghemawat
  - Andrey Gubarev
  - Christopher Heiser
  - Peter Hochschild
year: 2012
venue: OSDI
field: databases
section: "6"
section_title: Công trình liên quan
tag: 00BC
kind: section
lang: vi
source: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.258.9924
pdf_sha256: 61875779e75f603d21aefba6d9bd9816d4dd0c18cf41089f43707249e24bbf88
pdf_pages: "12"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: c6140db28528707912971f9673c8eae23e4b4816906b1e61ea4cea7a2f6626e5
translated_from: content/en/corbett-2012-spanner/06_related_work.md
source_content_sha256: 0de7ed181baa027b2254013706a6200e830b014018961af7c141bd37e54b5460
translation_model: gpt-5
translation_run: 20260914T201546Z
glossary_version: 6
glossary_terms_sha256: a534ae50d60bff0e03804fd3c150e37d1876484531ab87df9c72dc4d0c455eb2
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Sao chép nhất quán trên các datacenter như một dịch vụ lưu trữ đã được cung cấp bởi Megastore [5] và DynamoDB [3]. DynamoDB cung cấp một giao diện khóa-giá trị, và chỉ sao chép trong phạm vi một vùng. Spanner tiếp nối Megastore trong việc cung cấp một mô hình dữ liệu bán quan hệ, và thậm chí cả một ngôn ngữ lược đồ tương tự. Megastore không đạt được hiệu năng cao. Nó được xây dựng trên Bigtable, vốn áp đặt chi phí giao tiếp cao. Nó cũng không hỗ trợ các leader tồn tại lâu dài: nhiều bản sao có thể khởi tạo việc ghi. Tất cả các thao tác ghi từ các bản sao khác nhau tất yếu xung đột trong giao thức Paxos, ngay cả khi chúng không xung đột về mặt logic: thông lượng sụp đổ trên một nhóm Paxos ở mức vài thao tác ghi mỗi giây. Spanner cung cấp hiệu năng cao hơn, các giao dịch đa dụng, và tính nhất quán bên ngoài.

Pavlo et al. [31] đã so sánh hiệu năng của các cơ sở dữ liệu và MapReduce [12]. Họ chỉ ra một số nỗ lực khác đã được thực hiện để khám phá chức năng cơ sở dữ liệu được xây dựng trên các kho khóa-giá trị phân tán [1, 4, 7, 41] như bằng chứng rằng hai thế giới đang hội tụ. Chúng tôi đồng ý với kết luận này, nhưng chứng minh rằng việc tích hợp nhiều tầng có những ưu điểm: ví dụ, tích hợp kiểm soát đồng thời với sao chép làm giảm chi phí chờ xác nhận trong Spanner.

Khái niệm xây dựng các giao dịch trên một kho được sao chép có lịch sử ít nhất từ luận án của Gifford [16]. Scatter [17] là một kho khóa-giá trị dựa trên DHT gần đây, xây dựng các giao dịch trên lớp sao chép nhất quán. Spanner tập trung vào việc cung cấp một giao diện cấp cao hơn so với Scatter. Gray và Lamport [18] mô tả một giao thức xác nhận không chặn dựa trên Paxos. Giao thức của họ phát sinh nhiều chi phí thông điệp hơn so với xác nhận hai pha, điều này sẽ làm trầm trọng thêm chi phí xác nhận trên các nhóm được phân tán rộng rãi. Walter [36] cung cấp một biến thể của cô lập ảnh chụp nhanh hoạt động trong phạm vi một datacenter, nhưng không hoạt động xuyên qua các datacenter. Ngược lại, các giao dịch chỉ đọc của chúng tôi cung cấp một ngữ nghĩa tự nhiên hơn, bởi vì chúng tôi hỗ trợ tính nhất quán bên ngoài trên tất cả các thao tác.

Đã có một loạt công trình gần đây về việc giảm hoặc loại bỏ chi phí phụ trội của khóa. Calvin [40] loại bỏ kiểm soát đồng thời: nó gán trước các dấu thời gian và sau đó thực thi các giao dịch theo thứ tự dấu thời gian. H-Store [39] và Granola [11] mỗi hệ thống đều hỗ trợ cách phân loại riêng của chúng về các kiểu giao dịch, một số trong đó có thể tránh khóa. Không hệ thống nào trong số này cung cấp tính nhất quán bên ngoài. Spanner giải quyết vấn đề tranh chấp bằng cách cung cấp hỗ trợ cho cô lập ảnh chụp nhanh.

VoltDB [42] là một cơ sở dữ liệu trong bộ nhớ được phân mảnh hỗ trợ sao chép chủ-tớ trên diện rộng để khôi phục sau thảm họa, nhưng không hỗ trợ các cấu hình sao chép tổng quát hơn. Nó là một ví dụ về thứ được gọi là NewSQL, vốn là một sự thúc đẩy của thị trường nhằm hỗ trợ SQL có khả năng mở rộng [38]. Một số cơ sở dữ liệu thương mại triển khai việc đọc trong quá khứ, chẳng hạn như MarkLogic [26] và Oracle’s Total Recall [30]. Lomet và Li [24] mô tả một chiến lược triển khai cho một cơ sở dữ liệu thời gian như vậy.

Farsite suy ra các cận về độ không chắc chắn của đồng hồ (lớn hơn nhiều so với của TrueTime) so với một tham chiếu đồng hồ đáng tin cậy [13]: các hợp đồng thuê server trong Farsite được duy trì theo cùng cách mà Spanner duy trì các hợp đồng thuê Paxos. Các đồng hồ được đồng bộ lỏng đã được sử dụng cho các mục đích kiểm soát đồng thời trong các công trình trước đây [2, 23]. Chúng tôi đã chỉ ra rằng TrueTime cho phép suy luận về thời gian toàn cục trên các tập hợp máy trạng thái Paxos.
