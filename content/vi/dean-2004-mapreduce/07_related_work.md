---
paper: dean-2004-mapreduce
title: 'MapReduce: Simplified Data Processing on Large Clusters'
authors:
  - Jeffrey Dean
  - Sanjay Ghemawat
year: 2004
venue: OSDI
field: systems
section: "7"
section_title: Công trình liên quan
tag: "0089"
kind: section
lang: vi
source: https://www.usenix.org/legacy/events/osdi04/tech/full_papers/dean/dean.pdf
pdf_sha256: 9cfef3ef1b8fe1a1b66c7221f56c2eeca0b15d6608ea68b0c85a38bfbffd8ce5
pdf_pages: 11-12
extraction: vision
extraction_model: gpt-5
content_sha256: 22c725791bdd2027ba492582a9c9a9acbde37866d6d86f914c3e165182c2796e
translated_from: content/en/dean-2004-mapreduce/07_related_work.md
source_content_sha256: 5423801099bdbe679e1be1c7678a9b6690d976650730b4111ae810e69fcc867a
translation_model: gpt-5
translation_run: 20260918T153717Z
glossary_version: 7
glossary_terms_sha256: f834761938c11bca59f7cb79948997ed0706af48cd70392678452699c034a7ad
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Nhiều hệ thống đã cung cấp các mô hình lập trình bị hạn chế và sử dụng các hạn chế này để tự động song song hóa việc tính toán. Ví dụ, một hàm kết hợp có thể được tính trên tất cả các tiền tố của một mảng gồm $N$ phần tử trong thời gian $\log N$ trên $N$ bộ xử lý bằng cách sử dụng các phép tính tiền tố song song [6, 9, 13]. MapReduce có thể được xem là sự đơn giản hóa và chắt lọc của một số mô hình này dựa trên kinh nghiệm của chúng tôi với các phép tính thực tế quy mô lớn. Quan trọng hơn, chúng tôi cung cấp một triển khai chịu lỗi có khả năng mở rộng đến hàng nghìn bộ xử lý. Ngược lại, hầu hết các hệ thống xử lý song song chỉ được triển khai ở quy mô nhỏ hơn và để lại các chi tiết xử lý sự cố máy cho người lập trình.

Bulk Synchronous Programming [17] và một số nguyên thủy MPI [11] cung cấp các trừu tượng hóa cấp cao hơn giúp người lập trình dễ dàng viết các chương trình song song hơn. Một điểm khác biệt quan trọng giữa các hệ thống này và MapReduce là MapReduce khai thác một mô hình lập trình bị hạn chế để tự động song song hóa chương trình của người dùng và cung cấp khả năng chịu lỗi trong suốt.

Tối ưu hóa cục bộ của chúng tôi lấy cảm hứng từ các kỹ thuật như active disks [12, 15], trong đó việc tính toán được đẩy vào các phần tử xử lý gần với các đĩa cục bộ, nhằm giảm lượng dữ liệu được gửi qua các hệ thống con I/O hoặc mạng. Chúng tôi chạy trên các bộ xử lý phổ thông mà một số lượng nhỏ đĩa được kết nối trực tiếp với chúng thay vì chạy trực tiếp trên các bộ xử lý điều khiển đĩa, nhưng cách tiếp cận tổng quát là tương tự.

Cơ chế tác vụ dự phòng của chúng tôi tương tự với cơ chế lập lịch háo hức được sử dụng trong Charlotte System [3]. Một trong những thiếu sót của lập lịch háo hức đơn giản là nếu một tác vụ nhất định gây ra các sự cố lặp lại, toàn bộ tính toán sẽ không hoàn thành. Chúng tôi khắc phục một số trường hợp của vấn đề này bằng cơ chế bỏ qua các bản ghi xấu.

Triển khai MapReduce dựa vào một hệ thống quản lý cụm nội bộ chịu trách nhiệm phân phối và chạy các tác vụ của người dùng trên một tập hợp lớn các máy dùng chung. Mặc dù không phải là trọng tâm của bài báo này, hệ thống quản lý cụm có tinh thần tương tự như các hệ thống khác như Condor [16].

Cơ sở sắp xếp là một phần của thư viện MapReduce có hoạt động tương tự như NOW-Sort [1]. Các máy nguồn (các worker map) phân vùng dữ liệu cần sắp xếp và gửi nó đến một trong $R$ worker reduce. Mỗi worker reduce sắp xếp dữ liệu của mình cục bộ (trong bộ nhớ nếu có thể). Tất nhiên NOW-Sort không có các hàm Map và Reduce do người dùng định nghĩa, những hàm làm cho thư viện của chúng tôi có phạm vi áp dụng rộng rãi.

River [2] cung cấp một mô hình lập trình trong đó các tiến trình giao tiếp với nhau bằng cách gửi dữ liệu qua các hàng đợi phân tán. Giống như MapReduce, hệ thống River cố gắng cung cấp hiệu năng trường hợp trung bình tốt ngay cả khi có các sai khác không đồng nhất do phần cứng không đồng nhất hoặc các nhiễu loạn hệ thống gây ra. River đạt được điều này bằng cách lập lịch cẩn thận các truyền tải đĩa và mạng để đạt được thời gian hoàn thành cân bằng. MapReduce có một cách tiếp cận khác. Bằng cách hạn chế mô hình lập trình, khung MapReduce có thể phân vùng vấn đề thành một số lượng lớn các tác vụ có độ chi tiết nhỏ. Các tác vụ này được lập lịch động trên các worker khả dụng sao cho các worker nhanh hơn xử lý nhiều tác vụ hơn. Mô hình lập trình bị hạn chế cũng cho phép chúng tôi lập lịch các thực thi dư thừa của các tác vụ gần cuối công việc, điều này làm giảm đáng kể thời gian hoàn thành khi có các sai khác không đồng nhất (chẳng hạn như các worker chậm hoặc bị kẹt).

BAD-FS [5] có một mô hình lập trình rất khác so với MapReduce, và không giống MapReduce, được hướng tới việc thực thi các công việc trên một mạng diện rộng. Tuy nhiên, có hai điểm tương đồng cơ bản. (1) Cả hai hệ thống đều sử dụng thực thi dư thừa để khôi phục từ mất dữ liệu do các sự cố gây ra. (2) Cả hai đều sử dụng lập lịch nhận biết tính cục bộ để giảm lượng dữ liệu được gửi qua các liên kết mạng bị tắc nghẽn.

TACC [7] là một hệ thống được thiết kế để đơn giản hóa việc xây dựng các dịch vụ mạng có tính khả dụng cao. Giống như MapReduce, nó dựa vào việc thực thi lại như một cơ chế để triển khai khả năng chịu lỗi.
