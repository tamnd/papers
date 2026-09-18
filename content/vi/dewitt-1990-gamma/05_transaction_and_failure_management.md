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
section: "5"
section_title: Quản lý giao dịch và sự cố
tag: 026E
kind: section
lang: vi
source: http://db.cs.berkeley.edu/cs286/papers/gamma-tkde1990.pdf
pdf_sha256: 420d33f44b8e050f33517cdff1299a58838b4ad826d80a6617200332ea02be5e
pdf_pages: 17-22
extraction: vision
extraction_model: gpt-5
content_sha256: 1746ea0adbaf4a92e2329c13e1a45ad3c516f969365bd25e5e2fd3857295c130
translated_from: content/en/dewitt-1990-gamma/05_transaction_and_failure_management.md
source_content_sha256: 85cd2673868e364d06ad62fcc93e3e1adfb1ee3d1a498e985c7f98b29aeac7d0
translation_model: gpt-5
translation_run: 20260918T053014Z
glossary_version: 6
glossary_terms_sha256: a534ae50d60bff0e03804fd3c150e37d1876484531ab87df9c72dc4d0c455eb2
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Trong phần này chúng tôi mô tả các cơ chế mà Gamma sử dụng cho việc quản lý giao dịch và sự cố. Trong khi các cơ chế khóa đã hoàn toàn hoạt động, hệ thống phục hồi hiện đang được triển khai. Chúng tôi dự kiến bắt đầu triển khai cơ chế quản lý sự cố vào đầu năm 1990.

### 5.1. Kiểm soát đồng thời trong Gamma {#dewitt-1990-gamma-s5-1 .section tag=026F}

Kiểm soát đồng thời trong Gamma dựa trên khóa hai pha [GRAY78]. Hiện tại, hai mức chi tiết của khóa, file và page, cùng năm chế độ khóa, S, X, IS, IX và SIX được cung cấp. Mỗi site trong Gamma có bộ quản lý khóa cục bộ và bộ phát hiện bế tắc riêng. Bộ quản lý khóa duy trì một bảng khóa và một đồ thị chờ-để-giao dịch. Chi phí thiết lập một khóa thay đổi từ khoảng 100 lệnh, nếu không có xung đột, đến 250 lệnh nếu yêu cầu khóa xung đột với nhóm đã được cấp quyền. Trong trường hợp này, đồ thị chờ-để phải được kiểm tra bế tắc và giao dịch yêu cầu khóa phải được tạm dừng thông qua cơ chế semaphore.

Để phát hiện các bế tắc đa site, Gamma sử dụng một thuật toán phát hiện bế tắc tập trung. Định kỳ, bộ phát hiện bế tắc tập trung gửi một thông điệp đến mỗi nút trong cấu hình, yêu cầu đồ thị chờ-để-giao dịch cục bộ của nút đó. Ban đầu, khoảng thời gian chạy bộ phát hiện bế tắc tập trung được đặt là một giây. Mỗi lần bộ phát hiện bế tắc không tìm thấy một bế tắc toàn cục, khoảng thời gian này được nhân đôi và mỗi lần phát hiện thấy một bế tắc thì giá trị hiện tại của khoảng thời gian được chia đôi. Cận trên của khoảng thời gian được giới hạn ở 60 giây và cận dưới là 1 giây. Sau khi thu thập đồ thị chờ-để từ mỗi site, bộ phát hiện bế tắc tập trung tạo ra một đồ thị chờ-để-giao dịch toàn cục. Bất cứ khi nào một chu trình được phát hiện trong đồ thị chờ-để toàn cục, bộ quản lý bế tắc tập trung chọn hủy giao dịch đang giữ số lượng khóa ít nhất.

### 5.2. Kiến trúc phục hồi và Bộ quản lý nhật ký {#dewitt-1990-gamma-s5-2 .section tag=0270}

Các thuật toán hiện đang được triển khai để phối hợp xác nhận, hủy bỏ và quay lui giao dịch hoạt động như sau. Khi một tiến trình toán tử cập nhật một bản ghi, nó cũng tạo ra một bản ghi nhật ký ghi lại sự thay đổi của trạng thái cơ sở dữ liệu. Liên kết với mỗi bản ghi nhật ký là một số thứ tự nhật ký (LSN), được tạo thành từ một số nút và một số thứ tự cục bộ. Số nút được xác định tĩnh tại thời điểm cấu hình hệ thống, trong khi số thứ tự cục bộ, được gọi là **current LSN**, là một giá trị tăng đơn điệu.

Các bản ghi nhật ký được gửi bởi các bộ xử lý truy vấn đến một hoặc nhiều Bộ quản lý nhật ký (mỗi bộ chạy trên một bộ xử lý riêng), các bộ này hợp nhất các bản ghi nhật ký nhận được để tạo thành một luồng nhật ký duy nhất. Nếu M là số lượng bộ xử lý nhật ký đang được sử dụng, bộ xử lý truy vấn i sẽ chuyển các bản ghi nhật ký của nó đến bộ xử lý nhật ký (i mod M) [AGRA85]. Vì thuật toán này chọn bộ xử lý nhật ký một cách tĩnh và một bộ xử lý truy vấn luôn gửi các bản ghi nhật ký của nó đến cùng một bộ xử lý nhật ký, tiến trình phục hồi tại một nút xử lý truy vấn có thể dễ dàng xác định nơi yêu cầu các bản ghi nhật ký để xử lý việc hủy bỏ một giao dịch.

Khi một page của các bản ghi nhật ký đầy, nó được ghi xuống disk. Bộ quản lý nhật ký duy trì một bảng, được gọi là **Flushed Log Table**, chứa, đối với mỗi nút, LSN của bản ghi nhật ký cuối cùng từ nút đó đã được ghi xuống disk. Các giá trị này được trả về các nút theo yêu cầu hoặc khi chúng có thể được ghép kèm trong một thông điệp khác. Các nút xử lý truy vấn lưu thông tin này trong một biến cục bộ, được gọi là **Flushed LSN**.

Các bộ quản lý bộ đệm tại các nút xử lý truy vấn tuân theo giao thức WAL [GRAY78]. Khi một page bẩn cần được ép ghi xuống disk, bộ quản lý bộ đệm trước tiên so sánh LSN của page với giá trị cục bộ của Flushed LSN. Nếu LSN của page của một page nhỏ hơn hoặc bằng Flushed LSN, page đó có thể được ghi an toàn xuống disk. Ngược lại, hoặc một page bẩn khác phải được chọn, hoặc một thông điệp phải được gửi đến Bộ quản lý nhật ký để xóa các bản ghi nhật ký tương ứng của page bẩn. Chỉ sau khi Bộ quản lý nhật ký xác nhận rằng bản ghi nhật ký đã được ghi vào disk nhật ký thì page dữ liệu bẩn mới được ghi trở lại disk. Để giảm thời gian chờ phản hồi từ Bộ quản lý nhật ký, bộ quản lý bộ đệm luôn giữ sẵn T (một ngưỡng được chọn trước) page bộ đệm sạch và không cố định. Khi bộ quản lý bộ đệm nhận thấy số lượng page bộ đệm sạch, không cố định đã giảm xuống dưới T, một tiến trình, được gọi là **local log manager**, được kích hoạt. Tiến trình này gửi một thông điệp đến Bộ quản lý nhật ký để xóa một hoặc nhiều bản ghi nhật ký sao cho số lượng page sạch và không cố định cộng với số lượng page bẩn có thể được ghi an toàn xuống disk lớn hơn T.

Tiến trình bộ lập lịch cho một truy vấn chịu trách nhiệm gửi các bản ghi xác nhận hoặc hủy bỏ đến các Bộ quản lý nhật ký thích hợp. Nếu một giao dịch hoàn thành thành công, một bản ghi xác nhận cho giao dịch đó được tạo bởi bộ lập lịch của nó và được gửi đến mỗi Bộ quản lý nhật ký liên quan, sử dụng một giao thức xác nhận nhóm. Mặt khác, nếu một giao dịch bị hủy bỏ bởi hệ thống hoặc người dùng, bộ lập lịch của nó sẽ gửi một thông điệp hủy bỏ đến tất cả các bộ xử lý truy vấn đã tham gia vào việc thực thi của nó. Tiến trình phục hồi tại mỗi nút tham gia phản hồi bằng cách yêu cầu các bản ghi nhật ký được tạo bởi nút đó từ Bộ quản lý nhật ký của nó (LSN của mỗi bản ghi nhật ký chứa số nút khởi tạo). Khi các bản ghi nhật ký được nhận, tiến trình phục hồi hoàn tác các bản ghi nhật ký theo thứ tự thời gian ngược bằng cách sử dụng thuật toán undo ARIES [MOHA89]. Các thuật toán ARIES cũng được sử dụng làm cơ sở cho việc tạo điểm kiểm tra và phục hồi khởi động lại.

### 5.3. Quản lý sự cố {#dewitt-1990-gamma-s5-3 .section tag=0271}

Để giúp đảm bảo tính sẵn sàng của hệ thống trong trường hợp xảy ra sự cố với bộ xử lý và/hoặc đĩa, Gamma sử dụng một kỹ thuật sẵn sàng mới được gọi là **phân mảnh theo chuỗi** [HSIA90]. Giống như cơ chế đĩa nhân bản của Tandem [BORR81] và cơ chế phân mảnh xen kẽ của Teradata [TERA85, COPE89], phân mảnh theo chuỗi duy trì cả bản sao chính và bản sao dự phòng của mỗi quan hệ. Cả ba hệ thống đều có thể chịu được sự cố của một bộ xử lý hoặc đĩa đơn lẻ mà không chịu bất kỳ sự mất mát nào về tính sẵn sàng của dữ liệu. Trong [HSIA90], chúng tôi chỉ ra rằng phân mảnh theo chuỗi cung cấp mức độ sẵn sàng cao hơn so với phân mảnh xen kẽ và, trong trường hợp xảy ra sự cố với bộ xử lý hoặc đĩa, phân phối tải công việc của nút bị hỏng tốt hơn. Cơ chế đĩa nhân bản, mặc dù cung cấp mức độ sẵn sàng cao nhất, lại phân phối tải của một bộ xử lý bị hỏng rất kém.

### Bố trí dữ liệu với phân mảnh theo chuỗi {#dewitt-1990-gamma-s-data-placement-with-chained-declustering .section tag=0272}

Với phân mảnh theo chuỗi, các nút (một bộ xử lý với một hoặc nhiều đĩa) được chia thành các nhóm rời nhau gọi là các cụm-quan hệ và các bộ của mỗi quan hệ được phân mảnh giữa các ổ đĩa tạo thành một trong các cụm quan hệ. Hai bản sao vật lý của mỗi quan hệ, được gọi là **bản sao chính** và **bản sao dự phòng**, được duy trì. Ví dụ, xét Figure 9 trong đó M, số lượng đĩa trong cụm quan hệ, bằng 8. Các bộ trong bản sao chính của quan hệ R được phân mảnh bằng một trong ba chiến lược phân vùng của Gamma, với các bộ trong mảnh chính thứ i (được ký hiệu là Ri) được lưu trữ trên ổ đĩa thứ {i mod M}. Bản sao dự phòng được phân mảnh bằng cùng một chiến lược phân vùng nhưng mảnh dự phòng thứ i (được ký hiệu là ri) được lưu trữ trên đĩa thứ {(i + 1) mod M}. Chúng tôi gọi phương pháp sao chép dữ liệu này là **phân mảnh theo chuỗi** vì các đĩa được liên kết với nhau bởi các mảnh của một quan hệ, giống như một chuỗi.

Figure 9. Phân mảnh theo chuỗi (Kích thước cụm quan hệ = 8) {#dewitt-1990-gamma-fig-9 .figure tag=0273}

Sự khác biệt giữa cơ chế phân mảnh theo chuỗi và phân mảnh xen kẽ [TERA85, COPE89] được minh họa bởi Figure 10. Trong Figure 10, các mảnh từ bản sao chính của R được phân mảnh trên toàn bộ 8 ổ đĩa bằng cách băm trên một thuộc tính "key". Với cơ chế phân mảnh xen kẽ, tập hợp các đĩa được chia thành các đơn vị có kích thước N gọi là các **cụm**. Như được minh họa trong Figure 10, trong đó N=4, mỗi mảnh dự phòng được chia nhỏ thành N-1 mảnh con và mỗi mảnh con được đặt trên một đĩa khác nhau trong cùng một cụm, khác với đĩa chứa mảnh chính.

Figure 10. Phân mảnh xen kẽ (Kích thước cụm = 4) {#dewitt-1990-gamma-fig-10 .figure tag=0274}

Vì cả phân mảnh xen kẽ và phân mảnh theo chuỗi đều có thể chịu được sự cố của một đĩa hoặc bộ xử lý đơn lẻ, vậy sự khác biệt giữa hai cơ chế này là gì? Trong trường hợp sự cố của một nút đơn lẻ (bộ xử lý hoặc đĩa), cả hai chiến lược phân mảnh theo chuỗi và phân mảnh xen kẽ đều có khả năng phân phối đồng đều tải công việc của cụm giữa các nút hoạt động còn lại. Ví dụ, với kích thước cụm là 8, khi một bộ xử lý hoặc đĩa gặp sự cố, tải trên mỗi nút còn lại sẽ tăng thêm 1/7th. Khi đó có thể kết luận rằng kích thước cụm nên được làm lớn nhất có thể; cho đến khi, tất nhiên, chi phí phụ trội của tính song song bắt đầu lấn át các lợi ích thu được. Mặc dù điều này đúng đối với phân mảnh theo chuỗi, tính sẵn sàng của chiến lược xen kẽ tỷ lệ nghịch với kích thước cụm, vì sự cố của bất kỳ hai bộ xử lý hoặc đĩa nào sẽ làm cho dữ liệu không thể truy cập được. Do đó, việc tăng gấp đôi kích thước cụm để giảm một nửa (xấp xỉ) mức tăng tải trên các nút còn lại khi xảy ra sự cố có tác dụng phụ (rất tiêu cực) là làm tăng gấp đôi xác suất dữ liệu thực sự không sẵn sàng. Vì lý do này, Teradata khuyến nghị kích thước cụm là 4 hoặc 8 bộ xử lý.

Figure 11 minh họa cách tải công việc được cân bằng trong trường hợp xảy ra sự cố nút (nút 1 trong ví dụ này) với cơ chế phân mảnh theo chuỗi. Trong chế độ hoạt động bình thường, các yêu cầu đọc được chuyển đến các mảnh của bản sao chính và các thao tác ghi cập nhật cả hai bản sao. Khi xảy ra sự cố, các phần của cả mảnh chính và mảnh dự phòng được sử dụng cho các thao tác đọc. Ví dụ, với sự cố của nút 1, mảnh chính R1 không còn có thể được truy cập và do đó mảnh dự phòng r1 trên nút 2 phải được sử dụng để xử lý các truy vấn vốn thường được chuyển đến R1. Tuy nhiên, thay vì yêu cầu nút 2 xử lý tất cả các truy cập đến cả R2 và r1, phân mảnh theo chuỗi giảm tải 6/7-ths số truy cập đến R2 bằng cách chuyển hướng chúng đến r2 trên nút 3. Ngược lại, 5/7-ths số truy cập đến R3 trên nút 3 được gửi đến R4 thay thế. Việc gán lại tải công việc động này dẫn đến mức tăng 1/7-th trong tải công việc của mỗi nút còn lại trong cụm. Vì kích thước cụm quan hệ có thể được tăng lên mà không bị phạt, có thể làm cho mức tăng tải này nhỏ đến mức mong muốn.

|  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| **Bản sao chính** | R0 | --- | $\frac{1}{7}$R2 | $\frac{2}{7}$R3 | $\frac{3}{7}$R4 | $\frac{4}{7}$R5 | $\frac{5}{7}$R6 | $\frac{6}{7}$R7 |
| **Bản sao dự phòng** | $\frac{1}{7}$r7 | --- | r1 | $\frac{6}{7}$r2 | $\frac{5}{7}$r3 | $\frac{4}{7}$r4 | $\frac{3}{7}$r5 | $\frac{2}{7}$r6 |

Sử dụng mảnh với phân mảnh theo chuỗi  
Sau sự cố của nút 1 (Kích thước cụm quan hệ = 8)  
Figure 11

Điều làm cho lược đồ này hấp dẫn hơn nữa là việc gán lại các mảnh đang hoạt động không phát sinh I/O đĩa cũng như di chuyển dữ liệu. Chỉ một số giá trị cận và con trỏ/chỉ mục trong một bảng điều khiển nằm trong bộ nhớ cần được thay đổi, và các sửa đổi này có thể được thực hiện rất nhanh chóng và hiệu quả.

Ví dụ được trình bày trong Hình 11 cung cấp một cái nhìn rất đơn giản hóa về cách cơ chế phân cụm phân mảnh theo chuỗi thực sự cân bằng tải công việc trong trường hợp một nút gặp sự cố. Trong thực tế, các truy vấn không thể chỉ đơn giản truy cập một phần tùy ý của một mảnh dữ liệu, đặc biệt khi xét đến sự đa dạng của các cơ chế phân vùng và chỉ mục được cung cấp bởi phần mềm Gamma. Trong [HSIA90], chúng tôi mô tả cách tất cả các tổ hợp của các kiểu truy vấn, phương thức truy cập và phân vùng
