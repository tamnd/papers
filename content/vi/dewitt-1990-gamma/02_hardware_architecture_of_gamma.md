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
section: "2"
section_title: Kiến trúc phần cứng của Gamma
tag: 025C
kind: section
lang: vi
source: http://db.cs.berkeley.edu/cs286/papers/gamma-tkde1990.pdf
pdf_sha256: 420d33f44b8e050f33517cdff1299a58838b4ad826d80a6617200332ea02be5e
pdf_pages: 4-7
extraction: vision
extraction_model: gpt-5
content_sha256: 0fec18c603fe1e80bbac43d8d8975263bbb2a0da165fd880a974ad0a0c65ddee
translated_from: content/en/dewitt-1990-gamma/02_hardware_architecture_of_gamma.md
source_content_sha256: dc353fca75a59e3b1aa60852b79a0b11c6b8807748f7c81f7d98223066b8bf15
translation_model: gpt-5
translation_run: 20260916T132956Z
glossary_version: 6
glossary_terms_sha256: a534ae50d60bff0e03804fd3c150e37d1876484531ab87df9c72dc4d0c455eb2
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

### 2.1. Tổng quan {#dewitt-1990-gamma-s2-1 .section tag=025D}

Gamma dựa trên khái niệm về một kiến trúc không chia sẻ (shared-nothing) [STON86] trong đó các bộ xử lý không chia sẻ các ổ đĩa hoặc bộ nhớ truy cập ngẫu nhiên và chỉ có thể giao tiếp với nhau bằng cách gửi các thông điệp qua một mạng liên kết. Lưu trữ khối lượng lớn trong một kiến trúc như vậy thường được phân tán giữa các bộ xử lý bằng cách kết nối một hoặc nhiều ổ đĩa với mỗi bộ xử lý như được minh họa trong Hình 1. Có một số lý do khiến phương pháp không chia sẻ trở thành kiến trúc được lựa chọn. Thứ nhất, không có gì ngăn cản kiến trúc đạt khả năng mở rộng tới hàng nghìn bộ xử lý, không giống như các máy chia sẻ bộ nhớ mà việc mở rộng vượt quá 30-40 bộ xử lý có thể là không khả thi. Thứ hai, như được chứng minh trong [DEWI88, COPE88, TAND88], bằng cách liên kết một số lượng nhỏ

ổ đĩa Hình 1 với mỗi bộ xử lý và phân phối các bộ của mỗi quan hệ trên các ổ đĩa, có thể đạt được băng thông I/O tổng hợp rất cao mà không sử dụng các bộ điều khiển đĩa tùy chỉnh [KIM86, PATT88]. Hơn nữa, bằng cách sử dụng công nghệ lưu trữ khối lượng lớn có sẵn trên thị trường, người ta có thể sử dụng công nghệ mới nhất trong các ổ đĩa nhỏ 3 1/2" với bộ điều khiển đĩa tích hợp. Một ưu điểm khác của phương pháp không chia sẻ là không còn cần phải tự xây dựng phần cứng. Gần đây, cả Intel và Ncube đã bổ sung lưu trữ khối lượng lớn vào các sản phẩm đa bộ xử lý dựa trên hypercube của họ.

### 2.2. Phiên bản Gamma 1.0 {#dewitt-1990-gamma-s2-2 .section tag=025E}

Phiên bản ban đầu của Gamma bao gồm 17 bộ xử lý VAX 11/750, mỗi bộ có hai megabyte bộ nhớ. Một vòng token 80 megabit/giây [PROT85] được sử dụng để kết nối các bộ xử lý với nhau và với một VAX khác đang chạy Unix. Bộ xử lý này đóng vai trò là máy chủ cho Gamma. Tám trong số các bộ xử lý được gắn các ổ đĩa Fujitsu 333 megabyte được sử dụng để lưu trữ cơ sở dữ liệu. Các bộ xử lý không có đĩa được sử dụng cùng với các bộ xử lý có đĩa để thực thi các toán tử hàm nối và tổng hợp nhằm khảo sát liệu các bộ xử lý không có đĩa có thể được khai thác hiệu quả hay không.

Chúng tôi gặp phải một số vấn đề với nguyên mẫu này. Thứ nhất, vòng token có kích thước gói mạng tối đa là 2K byte. Trong phiên bản đầu tiên của nguyên mẫu, kích thước của một trang đĩa được đặt là 2K byte để có thể truyền một trang đĩa "nguyên vẹn" từ một bộ xử lý sang bộ xử lý khác mà không cần sao chép. Điều này yêu cầu, ví dụ, mỗi trang đĩa cũng phải chứa không gian cho phần đầu giao thức được phần mềm giao tiếp giữa các bộ xử lý sử dụng. Mặc dù ban đầu điều này có vẻ là một ý tưởng tốt, chúng tôi nhanh chóng nhận ra rằng lợi ích của kích thước trang đĩa lớn hơn bù đắp nhiều hơn chi phí phải sao chép các bộ từ một trang đĩa vào một gói mạng.

Vấn đề thứ hai chúng tôi gặp phải là giao diện mạng và Unibus trên 11/750 đều là các nút thắt cổ chai [GERB87, DEWI88]. Mặc dù băng thông của chính vòng token là 80 megabit/giây, Unibus trên 11/750 (nơi giao diện mạng được gắn vào) chỉ có băng thông 4 megabit/giây. Khi thực thi một truy vấn nối mà không có vị từ chọn trên bất kỳ quan hệ đầu vào nào, Unibus trở thành nút thắt cổ chai vì tốc độ truyền các trang từ đĩa cao hơn tốc độ của Unibus [DEWI88]. Giao diện mạng là một nút thắt cổ chai vì nó chỉ có thể đệm hai gói đến tại một thời điểm. Cho đến khi một gói được truyền vào bộ nhớ của VAX, các gói đến khác bị từ chối và phải được giao thức truyền thông truyền lại. Mặc dù cuối cùng chúng tôi đã xây dựng một giao diện tới vòng token được cắm trực tiếp vào bảng nối đa năng của VAX, vào thời điểm bo mạch hoạt động thì các VAX đã lỗi thời và chúng tôi quyết định không chi thêm kinh phí để nâng cấp toàn bộ hệ thống.

Vấn đề nghiêm trọng khác chúng tôi gặp phải với nguyên mẫu này là mỗi bộ xử lý chỉ có 2 megabyte bộ nhớ. Đây đặc biệt là một vấn đề vì hệ điều hành được Gamma sử dụng không cung cấp bộ nhớ ảo. Vấn đề trở nên nghiêm trọng hơn do không gian cho các bảng băm nối, không gian ngăn xếp cho các tiến trình và nhóm bộ đệm được quản lý riêng biệt để tránh xóa các trang nóng khỏi nhóm bộ đệm. Mặc dù việc các không gian này được phần mềm quản lý riêng biệt có những ưu điểm, trong một cấu hình mà bộ nhớ vốn đã hạn chế, việc cân bằng kích thước của ba nhóm bộ nhớ này tỏ ra khó khăn.

### 2.3. Phiên bản Gamma 2.0 {#dewitt-1990-gamma-s2-3 .section tag=025F}

Vào mùa thu năm 1988, chúng tôi thay thế nguyên mẫu dựa trên VAX bằng một hypercube iPSC/2 32 bộ xử lý từ Intel. Mỗi bộ xử lý được cấu hình với một CPU 386, 8 megabyte bộ nhớ và một ổ đĩa MAXTOR 4380 330-megabyte (5 1/4"). Mỗi ổ đĩa có một bộ điều khiển SCSI tích hợp cung cấp một bộ đệm RAM 45 Kbyte đóng vai trò là cache đĩa trong các thao tác đọc.

Các nút trong hypercube được liên kết với nhau để tạo thành một hypercube bằng cách sử dụng các mô-đun định tuyến VLSI tùy chỉnh. Mỗi mô-đun hỗ trợ tám[^1] kênh giao tiếp song công hoàn toàn, nối tiếp, tin cậy hoạt động ở tốc độ 2.8 megabyte/giây. Các thông điệp nhỏ (<= 100 byte) được gửi dưới dạng datagram. Đối với các thông điệp lớn, phần cứng xây dựng một mạch giao tiếp giữa hai nút, qua đó toàn bộ thông điệp được truyền mà không có chi phí phụ trội của phần mềm hoặc sao chép. Sau khi thông điệp được truyền hoàn toàn, mạch được giải phóng. Độ dài của một thông điệp chỉ bị giới hạn bởi kích thước của bộ nhớ vật lý trên mỗi bộ xử lý. Bảng 1 tóm tắt thời gian truyền từ một tiến trình Gamma tới một tiến trình khác (trên hai nút hypercube khác nhau) đối với nhiều kích thước thông điệp.

| Kích thước gói (tính bằng byte) | Thời gian truyền |
|---|---|
| 50 | 0.74 ms. |
| 500 | 1.46 ms. |
| 1000 | 1.57 ms. |
| 4000 | 2.69 ms. |
| 8000 | 4.64 ms. |

Bảng 1

Việc chuyển đổi phần mềm Gamma sang hypercube bắt đầu vào đầu tháng 12 năm 1988. Vì hầu hết người dùng hypercube Intel có xu hướng chạy một tiến trình duy nhất tại một thời điểm trong khi xử lý dữ liệu số, hệ điều hành do Intel cung cấp chỉ hỗ trợ một số lượng hạn chế các tiến trình nặng. Do đó, chúng tôi bắt đầu quá trình chuyển đổi bằng cách chuyển hệ điều hành của Gamma, NOSE (xem Section 3.5). Để đơn giản hóa việc chuyển đổi, chúng tôi quyết định chạy NOSE như một gói luồng bên trong một tiến trình NX/2 duy nhất nhằm tránh phải chuyển NOSE để chạy trực tiếp trên phần cứng thuần.

[^1]: Trên các cấu hình có sự kết hợp giữa các nút tính toán và I/O, một trong 8 kênh được dành riêng cho việc giao tiếp với hệ thống con I/O.

Sau khi NOSE được chạy, chúng tôi bắt đầu chuyển đổi phần mềm Gamma. Quá trình này mất 4-6 tháng-người nhưng kéo dài khoảng 6 tháng vì, trong quá trình chuyển đổi, chúng tôi phát hiện rằng giao diện giữa bộ điều khiển đĩa SCSI và bộ nhớ không thể truyền các khối đĩa lớn hơn 1024 byte (cạm bẫy của việc là một địa điểm thử nghiệm beta). Phần lớn việc chuyển đổi phần mềm Gamma gần như là đơn giản vì, bằng cách chuyển NOSE trước, những khác biệt giữa hai hệ thống trong việc khởi tạo truyền đĩa và thông điệp đã hoàn toàn được ẩn khỏi phần mềm Gamma. Khi chuyển mã sang 386, chúng tôi đã phát hiện một số lỗi ẩn trong phiên bản VAX của mã vì VAX không bắt lỗi khi một con trỏ null bị tham chiếu. Vấn đề lớn nhất mà chúng tôi gặp phải là các nút trên máy tính đa xử lý VAX được đánh số bắt đầu từ 1 trong khi hypercube sử dụng 0 làm địa chỉ logic của nút đầu tiên. Mặc dù chúng tôi nghĩ rằng việc thực hiện các thay đổi cần thiết sẽ tẻ nhạt nhưng đơn giản, chúng tôi đã đi được khoảng một nửa quá trình chuyển đổi trước khi nhận ra rằng chúng tôi phải tìm và thay đổi mọi vòng lặp "for" trong hệ thống mà chỉ số vòng lặp cũng được sử dụng làm địa chỉ của máy mà một thông điệp được gửi tới. Mặc dù điều này nghe có vẻ ngớ ngẩn hiện nay, chúng tôi đã mất vài tuần để tìm tất cả các vị trí cần thay đổi. Nhìn lại, chúng tôi nên để NOSE che giấu những khác biệt giữa hai lược đồ địa chỉ.

Tuy nhiên, từ góc nhìn của hệ thống cơ sở dữ liệu, có một số lĩnh vực mà Intel có thể cải thiện thiết kế của iPSC/2. Trước hết, nên cung cấp một cơ chế tiến trình nhẹ như một phương án thay thế cho NX/2. Mặc dù điều này gần như chắc chắn sẽ làm tăng thời gian cần thiết để thực hiện việc chuyển đổi, về lâu dài chúng tôi có thể tránh được việc duy trì NOSE. Một vấn đề nghiêm trọng hơn nhiều với phiên bản hiện tại của hệ thống là bộ điều khiển đĩa không thực hiện các truyền DMA trực tiếp vào bộ nhớ. Thay vào đó, khi một khối được đọc từ đĩa, bộ điều khiển đĩa thực hiện một truyền DMA vào một FIFO 4K byte. Khi FIFO đầy một nửa, CPU bị ngắt và nội dung của FIFO được sao chép vào vị trí thích hợp trong bộ nhớ.[^1] Mặc dù một lệnh khối được sử dụng cho thao tác sao chép, chúng tôi đã đo được rằng khoảng 10% số chu kỳ CPU khả dụng bị lãng phí để thực hiện thao tác sao chép. Ngoài ra, CPU bị ngắt 13 lần trong quá trình truyền một khối 8 Kbyte, một phần vì sử dụng bộ điều khiển đĩa SCSI và một phần vì FIFO giữa bộ điều khiển đĩa và bộ nhớ.
