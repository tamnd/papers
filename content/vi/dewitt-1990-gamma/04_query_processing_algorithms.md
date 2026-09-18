---
paper: dewitt-1990-gamma
title: The Gamma Database Machine Project
authors:
  - David J. DeWitt
  - Shahram Ghandeharizadeh
  - Donovan A. Schneider
  - Allan Bricker
  - Hui-I Hsiao
  - Rick Rasmussen
year: 1990
venue: IEEE Transactions on Knowledge and Data Engineering
field: databases
section: "4"
section_title: Các thuật toán xử lý truy vấn
tag: "0269"
kind: section
lang: vi
source: http://db.cs.berkeley.edu/cs286/papers/gamma-tkde1990.pdf
pdf_sha256: 420d33f44b8e050f33517cdff1299a58838b4ad826d80a6617200332ea02be5e
pdf_pages: 16-17
extraction: vision
extraction_model: gpt-5
content_sha256: 14deb036bcac108b2b4d1784a158e57b39caca99ec40691c816f223a7cfce60d
translated_from: content/en/dewitt-1990-gamma/04_query_processing_algorithms.md
source_content_sha256: d22e48238c755bbcc929c10e234ae51aec60286784490475c9054648fe7655c5
translation_model: gpt-5
translation_run: 20260916T132956Z
glossary_version: 6
glossary_terms_sha256: a534ae50d60bff0e03804fd3c150e37d1876484531ab87df9c72dc4d0c455eb2
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

### 4.1. Toán tử Selection {#dewitt-1990-gamma-s4-1 .section tag=026A}

Vì tất cả các quan hệ đều được giải cụm trên nhiều ổ đĩa, việc song song hóa thao tác selection chỉ đơn giản là khởi tạo một toán tử selection trên tập các nút liên quan có đĩa. Khi vị từ trong mệnh đề selection nằm trên thuộc tính phân vùng của quan hệ và quan hệ được phân vùng bằng hash hoặc theo khoảng, bộ lập lịch có thể điều hướng toán tử selection đến một tập con các nút. Nếu quan hệ được phân vùng round-robin hoặc vị từ selection không nằm trên thuộc tính phân vùng, một toán tử selection phải được khởi tạo trên tất cả các nút mà quan hệ được giải cụm. Để cải thiện hiệu năng, Gamma sử dụng một cơ chế đọc trước một trang khi quét các trang của một file theo tuần tự hoặc thông qua một chỉ mục phân cụm. Cơ chế này cho phép việc xử lý một trang được chồng lấp với thao tác I/O của trang tiếp theo.

### 4.2. Toán tử Join {#dewitt-1990-gamma-s4-2 .section tag=026B}

Các thuật toán join đa bộ xử lý do Gamma cung cấp dựa trên khái niệm phân vùng hai quan hệ cần được join thành các tập con rời nhau gọi là **buckets** [GOOD81, KITS83, BRAT84]. bằng cách áp dụng một hàm hash lên thuộc tính join của mỗi bộ. Các bucket đã được phân vùng biểu diễn các tập con rời nhau của các quan hệ ban đầu và có đặc tính quan trọng là tất cả các bộ có cùng giá trị thuộc tính join đều nằm trong cùng một bucket. Chúng tôi đã triển khai các phiên bản song song của bốn thuật toán join trên nguyên mẫu Gamma: sort-merge, Grace [KITS83], Simple [DEWI84], và Hybrid [DEWI84]. Mặc dù cả bốn thuật toán đều sử dụng khái niệm phân vùng dựa trên hash này, phép tính join thực tế phụ thuộc vào thuật toán. Thuật toán join hybrid song song được mô tả trong phần tiếp theo. Thông tin bổ sung về cả bốn thuật toán song song và hiệu năng tương đối của chúng có thể được tìm thấy trong [SCHN89a]. Vì nghiên cứu này cho thấy Hybrid hash join gần như luôn cung cấp hiệu năng tốt nhất, nó hiện là thuật toán mặc định trong Gamma và được mô tả chi tiết hơn trong phần tiếp theo. Vì các thuật toán join dựa trên hash này không thể được sử dụng để thực thi các thao tác non-equijoin, các thao tác như vậy hiện chưa được hỗ trợ. Để khắc phục tình trạng này, chúng tôi đang trong quá trình thiết kế một thuật toán non-equijoin song song cho Gamma.

**Hybrid Hash-Join**

Một thuật toán Hybrid hash-join **tập trung** [DEWI84] hoạt động trong ba giai đoạn. Trong giai đoạn đầu tiên, thuật toán sử dụng một hàm hash để phân vùng quan hệ bên trong (nhỏ hơn), R, thành N bucket. Các bộ của bucket đầu tiên được sử dụng để xây dựng một bảng hash trong bộ nhớ trong khi N-1 bucket còn lại được lưu trong các file tạm thời. Một hàm hash tốt tạo ra vừa đủ số lượng bucket để đảm bảo rằng mỗi bucket các bộ sẽ đủ nhỏ để hoàn toàn vừa với bộ nhớ chính. Trong giai đoạn thứ hai, quan hệ S được phân vùng bằng cách sử dụng hàm hash từ bước 1. Một lần nữa, N-1 bucket cuối cùng được lưu trong các file tạm thời trong khi các bộ trong bucket đầu tiên được sử dụng để ngay lập tức dò tìm bảng hash trong bộ nhớ được xây dựng trong giai đoạn đầu tiên. Trong giai đoạn thứ ba, thuật toán join các bucket $N-1$ còn lại từ quan hệ $R$ với các bucket tương ứng của chúng từ quan hệ $S$. Do đó, phép join được chia thành một chuỗi các phép join nhỏ hơn; mỗi phép trong số đó hy vọng có thể được tính toán mà không gặp phải tràn join. Kích thước của quan hệ nhỏ hơn xác định số lượng bucket; phép tính này độc lập với kích thước của quan hệ lớn hơn.

Phiên bản song song của thuật toán Hybrid hash join của chúng tôi tương tự như thuật toán tập trung được mô tả ở trên. Một **bảng tách phân vùng** trước tiên tách các quan hệ join thành $N$ bucket logic. Số lượng bucket được chọn sao cho các bộ tương ứng với mỗi bucket logic sẽ vừa trong **bộ nhớ tổng hợp** của các bộ xử lý join. Các bucket $N-1$ được dành cho việc lưu trữ tạm thời trên đĩa đều được phân vùng trên tất cả các vị trí đĩa khả dụng. Tương tự, một **bảng tách join** sẽ được sử dụng để định tuyến các bộ đến bộ xử lý join tương ứng của chúng (các bộ xử lý này không nhất thiết có đĩa gắn kèm), do đó song song hóa giai đoạn join. Hơn nữa, việc phân vùng quan hệ bên trong, $R$, thành các bucket được chồng lấp với việc chèn các bộ từ bucket đầu tiên của $R$ vào các bảng hash cư trú trong bộ nhớ tại mỗi nút join. Ngoài ra, việc phân vùng quan hệ bên ngoài, $S$, thành các bucket được chồng lấp với việc join bucket đầu tiên của $S$ với bucket đầu tiên của $R$. Điều này yêu cầu bảng tách phân vùng cho $R$ và $S$ được tăng cường bằng bảng tách join vì các bộ trong bucket đầu tiên phải được gửi đến những bộ xử lý được sử dụng để thực hiện phép join. Tất nhiên, khi các bucket $N-1$ còn lại được join, chỉ cần bảng tách join. Figure 8 mô tả quan hệ $R$ được phân vùng thành $N$ bucket trên $k$ vị trí đĩa trong đó bucket đầu tiên được join trên $m$ bộ xử lý ($m$ có thể nhỏ hơn, bằng, hoặc lớn hơn $k$).

### 4.3. Các thao tác Aggregate {#dewitt-1990-gamma-s4-3 .section tag=026C}

Gamma triển khai các aggregate vô hướng bằng cách cho mỗi bộ xử lý tính toán phần kết quả của nó song song. Các kết quả từng phần sau đó được gửi đến một process duy nhất, process này kết hợp các kết quả từng phần này thành đáp án cuối cùng. Các hàm aggregate được tính toán theo hai bước. Đầu tiên, mỗi bộ xử lý tính toán một phần của kết quả bằng cách tính một giá trị cho từng phân vùng. Tiếp theo, các bộ xử lý phân phối lại các kết quả từng phần bằng cách băm trên thuộc tính "group by". Kết quả của bước này là thu thập các kết quả từng phần cho mỗi phân vùng tại một vị trí duy nhất để có thể tính toán kết quả cuối cùng cho mỗi phân vùng.

### 4.4. Các toán tử cập nhật {#dewitt-1990-gamma-s4-4 .section tag=026D}

Phần lớn, các toán tử cập nhật (thay thế, xóa và thêm vào) được triển khai bằng cách sử dụng các kỹ thuật chuẩn. Ngoại lệ duy nhất xảy ra khi một toán tử thay thế sửa đổi thuộc tính phân vùng của một bộ. Trong trường hợp này, thay vì ghi bộ đã sửa đổi trở lại vào phân mảnh cục bộ của quan hệ, bộ đã sửa đổi được truyền qua một bảng phân tách để xác định site nào nên chứa bộ đó.
