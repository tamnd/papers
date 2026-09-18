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
section: "3"
section_title: Kiến trúc phần mềm của Gamma
tag: "0260"
kind: section
lang: vi
source: http://db.cs.berkeley.edu/cs286/papers/gamma-tkde1990.pdf
pdf_sha256: 420d33f44b8e050f33517cdff1299a58838b4ad826d80a6617200332ea02be5e
pdf_pages: 7-15
extraction: vision
extraction_model: gpt-5
content_sha256: fb1b2e6f60582c5cd3d3a089574efb15d28c88e03dd686ecc8da43ba0eaa002f
translated_from: content/en/dewitt-1990-gamma/03_software_architecture_of_gamma.md
source_content_sha256: ffdf4e121d3d64f2d9e9fd23b6462d05ef2660640b1aa277758aad8bf8803227
translation_model: gpt-5
translation_run: 20260916T132956Z
glossary_version: 6
glossary_terms_sha256: a534ae50d60bff0e03804fd3c150e37d1876484531ab87df9c72dc4d0c455eb2
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Trong phần này, chúng tôi trình bày tổng quan về kiến trúc phần mềm của Gamma và mô tả các kỹ thuật mà Gamma sử dụng để thực thi các truy vấn theo kiểu luồng dữ liệu. Chúng tôi bắt đầu bằng việc mô tả các cấu trúc lưu trữ thay thế được cung cấp bởi phần mềm Gamma. Tiếp theo, kiến trúc hệ thống tổng thể được mô tả từ trên xuống dưới. Sau khi mô tả cấu trúc tiến trình tổng thể, chúng tôi minh họa hoạt động của hệ thống bằng cách mô tả sự tương tác của

[^1]: Intel buộc phải sử dụng thiết kế như vậy vì hệ thống I/O được thêm vào sau khi hệ thống đã hoàn thành và cách duy nhất để thực hiện I/O là sử dụng một socket trống trên bo mạch không có quyền truy cập DMA vào bộ nhớ.

thuộc tính phân vùng.

Khi một truy vấn đang được tối ưu hóa, thông tin phân vùng cho mỗi quan hệ nguồn trong truy vấn được đưa vào kế hoạch truy vấn do bộ tối ưu hóa truy vấn tạo ra. Trong trường hợp các quan hệ được phân vùng theo băm và theo khoảng, thông tin phân vùng này được bộ lập lịch truy vấn (được thảo luận bên dưới) sử dụng để hạn chế số lượng bộ xử lý tham gia vào việc thực thi các truy vấn chọn trên thuộc tính phân vùng. Ví dụ, nếu quan hệ X được phân vùng theo băm trên thuộc tính y, có thể hướng các thao tác chọn với các vị từ có dạng "X.y = Constant" đến một site duy nhất; tránh sự tham gia của bất kỳ site nào khác trong việc thực thi truy vấn. Trong trường hợp các quan hệ được phân vùng theo khoảng, bộ lập lịch truy vấn có thể hạn chế việc thực thi truy vấn chỉ đến những bộ xử lý có khoảng của chúng chồng lấp với khoảng của vị từ chọn (có thể là vị từ bằng hoặc vị từ khoảng).

Nhìn lại, chúng tôi đã mắc một sai lầm nghiêm trọng khi chọn phân cụm phân tán tất cả các quan hệ trên tất cả các nút có đĩa. Một phương pháp tốt hơn nhiều, như được đề xuất trong [COPE88], là sử dụng "độ nóng" của một quan hệ để xác định mức độ mà quan hệ được phân cụm phân tán. Đáng tiếc, việc bổ sung khả năng như vậy vào phần mềm Gamma tại thời điểm này sẽ đòi hỏi một nỗ lực khá lớn - một nỗ lực mà chúng tôi khó có khả năng thực hiện.

### 3.2. Cấu trúc tiến trình Gamma {#dewitt-1990-gamma-s3-2 .section tag=0261}

Cấu trúc tổng thể của các tiến trình khác nhau tạo thành phần mềm Gamma được thể hiện trong Hình 2. Vai trò của mỗi tiến trình được mô tả ngắn gọn bên dưới. Hoạt động của cơ chế phát hiện và phục hồi bế tắc phân tán được trình bày trong các Mục 5.1 và 5.2. Tại thời điểm khởi tạo hệ thống, một tiến trình daemon UNIX cho Trình quản lý Catalog (CM) được khởi tạo cùng với một tập hợp các Tiến trình Lập lịch, một tập hợp các Tiến trình Toán tử, Tiến trình Phát hiện Bế tắc và Tiến trình Phục hồi.

**Trình quản lý Catalog**

Chức năng của Trình quản lý Catalog là hoạt động như một kho lưu trữ trung tâm cho tất cả thông tin lược đồ khái niệm và nội bộ của mỗi cơ sở dữ liệu. Thông tin lược đồ được tải vào bộ nhớ khi một cơ sở dữ liệu được mở lần đầu. Vì nhiều người dùng có thể mở cùng một cơ sở dữ liệu đồng thời và vì mỗi người dùng có thể cư trú trên một máy khác với máy mà Trình quản lý Catalog đang thực thi, Trình quản lý Catalog chịu trách nhiệm đảm bảo tính nhất quán giữa các bản sao được cache bởi mỗi người dùng.

**Trình quản lý truy vấn**

Một tiến trình trình quản lý truy vấn được liên kết với mỗi người dùng Gamma đang hoạt động. Trình quản lý truy vấn chịu trách nhiệm cache thông tin lược đồ cục bộ, cung cấp giao diện cho các truy vấn đặc biệt sử dụng gdl (biến thể của Quel của chúng tôi [STON76]), phân tích cú pháp truy vấn, tối ưu hóa và biên dịch.

**Các tiến trình lập lịch**

Trong khi thực thi, mỗi truy vấn đa site được điều khiển bởi một tiến trình lập lịch. Tiến trình này chịu trách nhiệm kích hoạt các Tiến trình Toán tử được sử dụng để thực thi các nút của một cây truy vấn đã biên dịch. Các tiến trình lập lịch có thể chạy trên bất kỳ bộ xử lý nào, đảm bảo rằng không có bộ xử lý nào trở thành nút thắt cổ chai. Tuy nhiên, trong thực tế, các tiến trình lập lịch tiêu thụ hầu như không có tài nguyên và có thể chạy một số lượng lớn chúng trên một bộ xử lý duy nhất. Một tiến trình điều phối tập trung được sử dụng để gán các tiến trình lập lịch cho các truy vấn. Những truy vấn mà bộ tối ưu hóa có thể phát hiện là truy vấn một site được gửi trực tiếp đến nút thích hợp để thực thi, bỏ qua tiến trình lập lịch.

Hình 2. Cấu trúc tiến trình Gamma {#dewitt-1990-gamma-fig-2 .figure tag=0262}

**Tiến trình toán tử**

Đối với mỗi toán tử trong một cây truy vấn, ít nhất một Tiến trình Toán tử được sử dụng tại mỗi bộ xử lý tham gia vào việc thực thi toán tử đó. Các toán tử này được chuẩn bị tại thời điểm khởi tạo hệ thống nhằm tránh chi phí phụ trội của việc khởi động các tiến trình tại thời điểm thực thi truy vấn (các tiến trình bổ sung có thể được fork khi cần). Cấu trúc của một tiến trình toán tử và ánh xạ các toán tử quan hệ tới các tiến trình toán tử được thảo luận chi tiết hơn bên dưới. Khi một bộ lập lịch muốn khởi động một toán tử mới trên một nút, nó gửi một yêu cầu đến một cổng truyền thông đặc biệt được gọi là cổng "new task". Khi một yêu cầu được nhận trên cổng này, một tiến trình toán tử nhàn rỗi được gán cho yêu cầu và cổng truyền thông của tiến trình toán tử này được trả về cho tiến trình lập lịch yêu cầu.

### 3.3. Tổng quan về thực thi truy vấn {#dewitt-1990-gamma-s3-3 .section tag=0263}

### Các giao diện truy vấn đặc biệt và truy vấn nhúng {#dewitt-1990-gamma-s-ad-hoc-and-embedded-query-interfaces .section tag=0264}

Hai giao diện cho Gamma có sẵn: một ngôn ngữ truy vấn đặc biệt và một giao diện ngôn ngữ truy vấn nhúng trong đó các truy vấn có thể được nhúng vào một chương trình C. Khi người dùng gọi giao diện truy vấn đặc biệt, một tiến trình Trình quản lý truy vấn (QM) được khởi động và ngay lập tức kết nối với tiến trình CM thông qua cơ chế socket Internet UNIX. Khi giao diện truy vấn đã biên dịch được sử dụng, bộ tiền xử lý dịch mỗi truy vấn nhúng thành một kế hoạch truy vấn đã biên dịch được chương trình gọi tại thời gian chạy. Một cơ chế truyền các tham số từ chương trình C đến các kế hoạch truy vấn đã biên dịch tại thời gian chạy cũng được cung cấp.

### Thực thi truy vấn {#dewitt-1990-gamma-s-query-execution .section tag=0265}

Gamma sử dụng các kỹ thuật quan hệ truyền thống cho việc phân tích cú pháp truy vấn, tối ưu hóa [SELI79, JARK84], và sinh mã. Quá trình tối ưu hóa được đơn giản hóa phần nào vì Gamma chỉ sử dụng các thuật toán dựa trên băm cho các phép nối và các phép toán phức tạp khác. Các truy vấn được biên dịch thành một cây toán tử sâu trái. Tại thời điểm thực thi, mỗi toán tử được thực thi bởi một hoặc nhiều tiến trình toán tử tại mỗi site tham gia.

Khi thiết kế bộ tối ưu hóa cho phiên bản VAX của Gamma, tập các kế hoạch truy vấn khả dĩ được bộ tối ưu hóa xem xét bị giới hạn chỉ còn các cây sâu trái vì chúng tôi cho rằng không có đủ bộ nhớ để hỗ trợ các kế hoạch sâu phải hoặc dạng bụi rậm. Bằng cách sử dụng kết hợp các cây truy vấn sâu trái và các thuật toán nối dựa trên băm, chúng tôi có thể đảm bảo rằng không quá hai phép toán nối từng hoạt động đồng thời và do đó có thể tối đa hóa lượng bộ nhớ vật lý có thể được cấp phát cho mỗi toán tử nối. Vì giới hạn bộ nhớ này thực sự chỉ là một đặc tính của nguyên mẫu VAX, gần đây chúng tôi đã bắt đầu khảo sát các ảnh hưởng về hiệu năng của các kế hoạch truy vấn sâu phải và dạng bụi rậm [SCHN89b].

Như đã thảo luận trong Section 3.1, trong quá trình tối ưu hóa một truy vấn, bộ tối ưu hóa truy vấn nhận biết rằng một số truy vấn nhất định chỉ có thể được hướng tới một tập con các nút trong hệ thống. Trong trường hợp truy vấn một site, truy vấn được QM gửi trực tiếp đến bộ xử lý thích hợp để thực thi. Trong trường hợp truy vấn nhiều site, bộ tối ưu hóa thiết lập một kết nối tới một tiến trình scheduler nhàn rỗi thông qua một tiến trình dispatcher tập trung. Tiến trình dispatcher, bằng cách kiểm soát số lượng scheduler đang hoạt động, triển khai một cơ chế kiểm soát tải đơn giản. Khi đã thiết lập kết nối với một tiến trình scheduler, QM gửi truy vấn đã biên dịch đến tiến trình scheduler và chờ truy vấn hoàn thành thực thi. Tiến trình scheduler, lần lượt, kích hoạt các tiến trình toán tử tại mỗi bộ xử lý truy vấn được chọn để thực thi toán tử. Cuối cùng, QM đọc các kết quả của truy vấn và trả chúng thông qua giao diện truy vấn ad-hoc cho người dùng hoặc thông qua giao diện truy vấn nhúng tới chương trình từ đó truy vấn được khởi tạo.

### 3.4. Cấu trúc Toán tử và Tiến trình {#dewitt-1990-gamma-s3-4 .section tag=0266}

Các thuật toán cho tất cả các toán tử quan hệ được viết như thể chúng sẽ được chạy trên một bộ xử lý duy nhất. Như được trình bày trong Figure 3, đầu vào của một Tiến trình Toán tử là một luồng các tuple và đầu ra là một luồng các tuple được phân kênh thông qua một cấu trúc mà chúng tôi gọi là bảng phân tách. Khi tiến trình bắt đầu thực thi, nó liên tục đọc các tuple từ luồng đầu vào, xử lý từng tuple, và sử dụng một bảng phân tách để định tuyến tuple kết quả tới tiến trình được chỉ ra trong bảng phân tách.[^1] Khi tiến trình phát hiện kết thúc luồng đầu vào, trước tiên nó đóng các luồng đầu ra rồi gửi một thông điệp điều khiển tới tiến trình scheduler của nó cho biết rằng nó đã hoàn thành thực thi. Việc đóng các luồng đầu ra có tác dụng phụ là gửi các thông điệp "end of stream" tới từng tiến trình đích.

Figure 3

Bảng phân tách định nghĩa một ánh xạ các giá trị tới một tập các tiến trình đích. Gamma sử dụng ba kiểu bảng phân tách khác nhau tùy thuộc vào kiểu thao tác đang được thực hiện [DEWI86]. Là một ví dụ về một dạng bảng phân tách, hãy xem xét việc sử dụng bảng phân tách được trình bày trong Figure 4 kết hợp với việc thực thi một phép nối sử dụng 4 bộ xử lý. Mỗi tiến trình tạo ra các tuple cho phép nối sẽ áp dụng một hàm băm cho thuộc tính nối của mỗi tuple đầu ra để tạo ra một giá trị trong khoảng từ 0 đến 3. Giá trị này sau đó được sử dụng làm chỉ mục vào bảng phân tách để lấy địa chỉ của tiến trình đích sẽ nhận tuple.

[^1]: Các tuple thực sự được gửi dưới dạng các lô 8K byte, ngoại trừ lô cuối cùng.

| Giá trị | Tiến trình Đích |
|---|---|
| 0 | (Processor #3, Port #5) |
| 1 | (Processor #2, Port #13) |
| 2 | (Processor #7, Port #6) |
| 3 | (Processor #9, Port #15) |

Một Ví dụ về Bảng Phân Tách  
Figure 4

### Một Ví dụ {#dewitt-1990-gamma-s-an-example .section tag=0267}

Là một ví dụ về cách các truy vấn được thực thi, hãy xem xét truy vấn được trình bày trong Figure 5. Trong Figure 6, các tiến trình được sử dụng để thực thi truy vấn được trình bày cùng với luồng dữ liệu giữa các tiến trình khác nhau cho một cấu hình Gamma bao gồm hai bộ xử lý có đĩa và hai bộ xử lý không có đĩa. Vì hai quan hệ đầu vào A và B được phân vùng trên các đĩa gắn với các bộ xử lý P1 và P2, các toán tử chọn và quét được khởi tạo trên cả hai bộ xử lý P1 và P2. Các bảng phân tách cho cả toán tử chọn và quét đều chứa hai mục nhập vì hai bộ xử lý đang được sử dụng cho thao tác nối. Các bảng phân tách cho mỗi phép chọn và quét là giống hệt nhau - định tuyến các tuple có giá trị thuộc tính nối băm thành 0 (các đường nét đứt) tới P3 và các tuple có giá trị băm thành 1 (các đường liền) tới P4. Toán tử nối thực thi theo hai giai đoạn. Trong giai đoạn đầu tiên, được gọi là giai đoạn *Building*, các tuple từ quan hệ bên trong (A trong ví dụ này) được chèn vào một bảng băm nằm trong bộ nhớ bằng cách băm trên giá trị thuộc tính nối. Sau khi giai đoạn đầu tiên hoàn thành, giai đoạn *probing* của phép nối được khởi tạo, trong đó các tuple từ quan hệ bên ngoài được sử dụng để thăm dò bảng băm nhằm tìm các tuple khớp.[^1] Vì quan hệ kết quả được phân vùng trên hai đĩa, bảng phân tách cho mỗi toán tử nối chứa hai mục nhập và các tuple của C được phân phối theo cách round-robin giữa P1 và P2.

Figure 5

[^1]: Đây thực sự là mô tả của thuật toán nối băm đơn giản. Hoạt động của thuật toán nối băm lai được trình bày trong Section 4.

Figure 6

Một trong những vấn đề chính với nguyên mẫu DIRECT là mỗi trang dữ liệu được xử lý đều yêu cầu ít nhất một thông điệp điều khiển đến một bộ lập lịch tập trung. Trong Gamma, nút thắt này hoàn toàn được tránh. Trên thực tế, số lượng thông điệp điều khiển cần thiết để thực thi một truy vấn xấp xỉ bằng ba lần số lượng toán tử trong truy vấn nhân với số lượng bộ xử lý được sử dụng để thực thi mỗi toán tử. Ví dụ, hãy xem Hình 7, trong đó mô tả luồng điều khiển của các thông điệp điều khiển[^1] từ một tiến trình bộ lập lịch đến các tiến trình trên các bộ xử lý P1 và P3 trong Hình 6 (một tập thông điệp giống hệt sẽ được truyền từ bộ lập lịch đến P2 và P4). Bộ lập lịch bắt đầu bằng cách khởi tạo giai đoạn xây dựng của phép nối và toán tử chọn trên quan hệ A. Khi cả hai toán tử này hoàn thành, bộ lập lịch tiếp theo khởi tạo toán tử lưu trữ, giai đoạn thăm dò của phép nối và việc quét quan hệ B. Khi mỗi toán tử này hoàn thành, một thông điệp kết quả được trả về cho người dùng.

[^1]: Thông điệp "Initiate" được gửi đến một cổng "new operator" trên mỗi bộ xử lý. Một tiến trình điều phối chấp nhận các thông điệp đến trên cổng này và gán toán tử cho một tiến trình. Tiến trình được gán trả lời cho bộ lập lịch bằng một thông điệp "ID" cho biết số cổng riêng của tiến trình toán tử. Các giao tiếp trong tương lai đến toán tử từ bộ lập lịch sử dụng số cổng riêng này.

Hình 7

### 3.5. Hệ điều hành và Hệ thống lưu trữ {#dewitt-1990-gamma-s3-5 .section tag=0268}

Gamma được xây dựng trên một hệ điều hành được thiết kế đặc biệt để hỗ trợ các hệ quản trị cơ sở dữ liệu. NOSE cung cấp nhiều tiến trình nhẹ với bộ nhớ dùng chung. Một chính sách lập lịch không chiếm quyền được sử dụng để giúp ngăn chặn các đoàn xe [BLAS79] xảy ra. NOSE cung cấp giao tiếp giữa các tiến trình NOSE bằng cách sử dụng phần cứng truyền thông điệp đáng tin cậy của siêu khối Intel iPSC/2. Các dịch vụ file trong NOSE dựa trên Wisconsin Storage System (WiSS) [CHOU85]. Các phần tới hạn của WiSS được bảo vệ bằng cơ chế semaphore do NOSE cung cấp.

Các dịch vụ file do WiSS cung cấp bao gồm các file tuần tự có cấu trúc, các file luồng byte như trong UNIX, các chỉ mục B+, các mục dữ liệu dài, một tiện ích sắp xếp và một cơ chế quét. Một file tuần tự là một chuỗi các bản ghi. Các bản ghi có thể thay đổi về độ dài (lên đến một trang), và có thể được chèn và xóa tại các vị trí tùy ý trong một file tuần tự. Tùy chọn, mỗi file có thể có một hoặc nhiều chỉ mục liên kết, ánh xạ các giá trị khóa tới các định danh bản ghi của các bản ghi trong file chứa giá trị khớp. Một thuộc tính được lập chỉ mục có thể được chỉ định làm thuộc tính phân cụm cho file. Cơ chế quét tương tự như cơ chế được System R’s RSS [ASTR76] cung cấp, ngoại trừ việc các vị từ được trình tối ưu hóa truy vấn biên dịch thành ngôn ngữ máy 386 để tối đa hóa hiệu năng.
