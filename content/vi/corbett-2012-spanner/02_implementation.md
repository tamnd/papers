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
section: "2"
section_title: Triển khai
tag: 00A1
kind: section
lang: vi
source: http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.258.9924
pdf_sha256: 61875779e75f603d21aefba6d9bd9816d4dd0c18cf41089f43707249e24bbf88
pdf_pages: 2-5
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 2ad5d3e93bd08d6d49e6aacd79fc4efcf0542aa24a49dd3c428e3578d46064b2
translated_from: content/en/corbett-2012-spanner/02_implementation.md
source_content_sha256: 9de2aa4ca1dc68c609189a4ceded7e2873f5d4b89501935db21227ab19d4c300
translation_model: gpt-5
translation_run: 20260914T201546Z
glossary_version: 6
glossary_terms_sha256: a534ae50d60bff0e03804fd3c150e37d1876484531ab87df9c72dc4d0c455eb2
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Phần này mô tả cấu trúc và lý do nền tảng của việc triển khai Spanner. Sau đó, phần này mô tả trừu tượng hóa thư mục, được dùng để quản lý sao chép và vị trí cục bộ, và là đơn vị của việc di chuyển dữ liệu. Cuối cùng, phần này mô tả mô hình dữ liệu của chúng tôi, lý do Spanner có vẻ giống một cơ sở dữ liệu quan hệ thay vì một kho khóa-giá trị, và cách các ứng dụng có thể kiểm soát vị trí cục bộ của dữ liệu.

Một triển khai Spanner được gọi là một universe. Vì Spanner quản lý dữ liệu trên toàn cầu, sẽ chỉ có một số ít universe đang chạy. Hiện tại chúng tôi chạy một universe thử nghiệm/sân chơi, một universe phát triển/sản xuất, và một universe chỉ dành cho sản xuất.

Spanner được tổ chức thành một tập hợp các zone, trong đó mỗi zone là phép tương tự gần đúng của một triển khai các server Bigtable [9]. Các zone là đơn vị triển khai quản trị. Tập hợp các zone cũng là tập hợp các vị trí mà dữ liệu có thể được sao chép qua đó. Các zone có thể được thêm vào hoặc loại bỏ khỏi một hệ thống đang chạy khi các datacenter mới được đưa vào phục vụ và các datacenter cũ được tắt đi tương ứng. Các zone cũng là đơn vị cô lập vật lý: có thể có một hoặc nhiều zone trong một datacenter, chẳng hạn, nếu dữ liệu của các ứng dụng khác nhau phải được phân vùng trên các tập hợp server khác nhau trong cùng một datacenter.

Figure 1 minh họa các server trong một universe Spanner. Một zone có một zonemaster và từ một trăm đến vài nghìn spanserver. Thành phần đầu tiên gán dữ liệu cho các spanserver; thành phần thứ hai phục vụ dữ liệu cho các máy khách. Các proxy vị trí theo từng zone được các máy khách sử dụng để xác định vị trí của các spanserver được gán để phục vụ dữ liệu của chúng. Universe master và placement driver hiện là các singleton. Universe master chủ yếu là một console hiển thị thông tin trạng thái về tất cả các zone để gỡ lỗi tương tác. Placement driver xử lý việc di chuyển dữ liệu tự động giữa các zone trên thang thời gian tính bằng phút. Placement driver định kỳ giao tiếp với các spanserver để tìm dữ liệu cần được di chuyển, nhằm đáp ứng các ràng buộc sao chép được cập nhật hoặc để cân bằng tải. Vì lý do không gian, chúng tôi sẽ chỉ mô tả spanserver ở mức chi tiết.

Figure.

Figure 1: Tổ chức server Spanner. {#corbett-2012-spanner-fig-1 .figure tag=00A2}

### 2.1 Ngăn xếp phần mềm Spanserver {#corbett-2012-spanner-s2-1 .section tag=00A3}

Phần này tập trung vào việc triển khai spanserver để minh họa cách sao chép và các giao dịch phân tán được xếp lớp trên triển khai dựa trên Bigtable của chúng tôi. Ngăn xếp phần mềm được trình bày trong Figure 2. Ở tầng dưới cùng, mỗi spanserver chịu trách nhiệm cho từ 100 đến 1000 thể hiện của một cấu trúc dữ liệu được gọi là tablet. Một tablet tương tự như trừu tượng hóa tablet của Bigtable, ở chỗ nó triển khai một tập hợp các ánh xạ sau:

(key:string, timestamp:int64) → string

Không giống Bigtable, Spanner gán dấu thời gian cho dữ liệu, đây là một cách quan trọng khiến Spanner giống cơ sở dữ liệu đa phiên bản hơn là một kho khóa-giá trị. Trạng thái của một tablet được lưu trữ trong tập hợp các file dạng B-tree và một nhật ký ghi trước, tất cả trên một hệ thống file phân tán có tên Colossus (kế nhiệm của Google File System [[ghemawat-2003-gfs]]).

Để hỗ trợ sao chép, mỗi spanserver triển khai một máy trạng thái Paxos duy nhất trên mỗi tablet. (Một phiên bản Spanner ban đầu hỗ trợ nhiều máy trạng thái Paxos trên mỗi tablet, cho phép các cấu hình sao chép linh hoạt hơn. Độ phức tạp của thiết kế đó khiến chúng tôi từ bỏ nó.) Mỗi máy trạng thái lưu trữ siêu dữ liệu và nhật ký của nó trong tablet tương ứng. Triển khai Paxos của chúng tôi hỗ trợ các leader tồn tại lâu dài với các hợp đồng thuê leader dựa trên thời gian, có độ dài mặc định là 10 giây. Triển khai Spanner hiện tại ghi nhật ký mỗi lần ghi Paxos hai lần: một lần trong nhật ký của tablet, và một lần trong nhật ký Paxos. Lựa chọn này được thực hiện vì sự thuận tiện, và chúng tôi có khả năng sẽ khắc phục điều này trong tương lai. Triển khai Paxos của chúng tôi sử dụng đường ống, nhằm cải thiện thông lượng của Spanner khi có độ trễ WAN; nhưng các lần ghi được Paxos áp dụng theo thứ tự (một thực tế mà chúng tôi sẽ dựa vào trong Section 4).

Các máy trạng thái Paxos được sử dụng để triển khai một tập hợp các ánh xạ được sao chép nhất quán. Trạng thái ánh xạ khóa-giá trị của mỗi bản sao được lưu trữ trong tablet tương ứng của nó. Các lần ghi phải khởi tạo giao thức Paxos tại leader; các lần đọc truy cập trực tiếp trạng thái từ tablet bên dưới tại bất kỳ bản sao nào đủ được cập nhật. Tập hợp các bản sao được gọi chung là một *nhóm Paxos*.

Tại mọi bản sao là leader, mỗi spanserver triển khai một *bảng khóa* để triển khai điều khiển đồng thời. Bảng khóa chứa trạng thái cho khóa hai pha: nó ánh xạ các phạm vi khóa thành các trạng thái khóa. (Lưu ý rằng việc có một leader Paxos tồn tại lâu dài là quan trọng để quản lý hiệu quả bảng khóa.) Trong cả Bigtable và Spanner, chúng tôi thiết kế cho các giao dịch tồn tại lâu dài (ví dụ, để tạo báo cáo, có thể mất khoảng vài phút), vốn hoạt động kém dưới điều khiển đồng thời lạc quan khi có xung đột. Các thao tác yêu cầu đồng bộ hóa, chẳng hạn như các lần đọc giao dịch, thu nhận khóa trong bảng khóa; các thao tác khác bỏ qua bảng khóa.

Tại mọi bản sao là leader, mỗi spanserver cũng triển khai một *bộ quản lý giao dịch* để hỗ trợ các giao dịch phân tán. Bộ quản lý giao dịch được dùng để triển khai một *leader tham gia*; các bản sao khác trong nhóm sẽ được gọi là *slave tham gia*. Nếu một giao dịch chỉ liên quan đến một nhóm Paxos (như trường hợp của hầu hết các giao dịch), nó có thể bỏ qua bộ quản lý giao dịch, vì bảng khóa và Paxos cùng nhau cung cấp tính giao dịch. Nếu một giao dịch liên quan đến nhiều hơn một nhóm Paxos, các leader của những nhóm đó phối hợp để thực hiện xác nhận hai pha. Một trong các nhóm tham gia được chọn làm điều phối viên: leader tham gia của nhóm đó sẽ được gọi là *leader điều phối*, và các slave của nhóm đó là *slave điều phối*. Trạng thái của mỗi bộ quản lý giao dịch được lưu trữ trong nhóm Paxos bên dưới (và do đó được sao chép).

### 2.2 Thư mục và Đặt vị trí {#corbett-2012-spanner-s2-2 .section tag=0125}

Bên trên tập các ánh xạ khóa-giá trị, triển khai Spanner hỗ trợ một trừu tượng hóa phân nhóm được gọi là một *directory*, là một tập hợp các khóa liên tiếp chia sẻ cùng một tiền tố. (Việc lựa chọn thuật ngữ *directory* là một tai nạn lịch sử; một thuật ngữ tốt hơn có thể là *bucket.*) Chúng tôi sẽ giải thích nguồn gốc của tiền tố đó trong Section 2.3. Việc hỗ trợ các directory cho phép các ứng dụng kiểm soát tính cục bộ của dữ liệu bằng cách lựa chọn các khóa một cách cẩn thận.

Một directory là đơn vị đặt dữ liệu. Tất cả dữ liệu trong một directory có cùng cấu hình sao chép. Khi dữ liệu được di chuyển giữa các nhóm Paxos, nó được di chuyển directory theo directory, như được minh họa trong Figure 3. Spanner có thể di chuyển một directory để giảm tải từ một nhóm Paxos; để đặt các directory thường xuyên được truy cập cùng nhau vào cùng một nhóm; hoặc để di chuyển một directory vào một nhóm gần hơn với các máy truy cập của nó. Các directory có thể được di chuyển trong khi các thao tác của máy khách đang diễn ra. Có thể kỳ vọng rằng một directory 50MB có thể được di chuyển trong vài giây.

Việc một nhóm Paxos có thể chứa nhiều directory ngụ ý rằng một tablet Spanner khác với một tablet Bigtable: cái trước không nhất thiết là một phân vùng liên tiếp theo thứ tự từ điển duy nhất của không gian hàng. Thay vào đó, một tablet Spanner là một bộ chứa có thể bao bọc nhiều phân vùng của không gian hàng. Chúng tôi đưa ra quyết định này để có thể đặt cùng vị trí nhiều directory thường xuyên được truy cập cùng nhau.

Movedir là tác vụ nền được sử dụng để di chuyển các directory giữa các nhóm Paxos [14]. Movedir cũng được sử dụng để thêm hoặc loại bỏ các bản sao vào các nhóm Paxos [25], bởi vì Spanner chưa hỗ trợ các thay đổi cấu hình trong Paxos. Movedir không được triển khai như một giao dịch đơn lẻ, nhằm tránh chặn các thao tác đọc và ghi đang diễn ra trong quá trình di chuyển dữ liệu lớn. Thay vào đó, movedir đăng ký sự kiện rằng nó bắt đầu di chuyển dữ liệu và di chuyển dữ liệu trong nền. Khi nó đã di chuyển tất cả dữ liệu ngoại trừ một lượng danh nghĩa, nó sử dụng một giao dịch để di chuyển nguyên tử lượng danh nghĩa đó và cập nhật metadata cho hai nhóm Paxos.

Một directory cũng là đơn vị nhỏ nhất mà các thuộc tính sao chép theo địa lý (hay đặt vị trí, gọi tắt) có thể được một ứng dụng đặc tả. Thiết kế của ngôn ngữ đặc tả đặt vị trí của chúng tôi phân tách trách nhiệm quản lý các cấu hình sao chép. Các quản trị viên kiểm soát hai chiều: số lượng và kiểu của các bản sao, và vị trí địa lý của các bản sao đó. Họ tạo một danh sách các tùy chọn có tên trong hai chiều này (ví dụ, North America, được sao chép 5 cách với 1 witness). Một ứng dụng kiểm soát cách dữ liệu được sao chép, bằng cách gắn thẻ mỗi cơ sở dữ liệu và/hoặc các directory riêng lẻ với một tổ hợp các tùy chọn đó. Ví dụ, một ứng dụng có thể lưu trữ dữ liệu của mỗi người dùng cuối trong directory riêng của nó, điều này cho phép dữ liệu của người dùng $A$ có ba bản sao ở Europe, và dữ liệu của người dùng $B$ có năm bản sao ở North America.

Để làm rõ phần trình bày, chúng tôi đã đơn giản hóa quá mức. Trên thực tế, Spanner sẽ phân mảnh một directory thành nhiều mảnh nếu nó phát triển quá lớn. Các mảnh có thể được phục vụ từ các nhóm Paxos khác nhau (và do đó từ các server khác nhau). Movedir thực sự di chuyển các mảnh, chứ không phải toàn bộ directory, giữa các nhóm.

### 2.3 Mô hình dữ liệu {#corbett-2012-spanner-s2-3 .section tag=010D}

Spanner cung cấp cho các ứng dụng tập hợp các tính năng dữ liệu sau: một mô hình dữ liệu dựa trên các bảng bán-quan hệ có lược đồ, một ngôn ngữ truy vấn, và các giao dịch mục đích chung. Sự chuyển hướng tới việc hỗ trợ các tính năng này được thúc đẩy bởi nhiều yếu tố. Nhu cầu hỗ trợ các bảng bán-quan hệ có lược đồ và sao chép đồng bộ được củng cố bởi sự phổ biến của Megastore [5]. Ít nhất 300 ứng dụng trong Google sử dụng Megastore (mặc dù hiệu năng tương đối thấp của nó) bởi vì mô hình dữ liệu của nó đơn giản hơn để quản lý so với Bigtable’s, và bởi vì nó hỗ trợ sao chép đồng bộ giữa các trung tâm dữ liệu. (Bigtable chỉ hỗ trợ sao chép nhất quán cuối cùng giữa các trung tâm dữ liệu.) Các ví dụ về những ứng dụng Google nổi tiếng sử dụng Megastore là Gmail, Picasa, Calendar, Android Market, và AppEngine. Nhu cầu hỗ trợ một ngôn ngữ truy vấn giống SQL trong Spanner cũng rõ ràng, xét đến sự phổ biến của Dremel [28] như một công cụ phân tích dữ liệu tương tác. Cuối cùng, sự thiếu vắng các giao dịch xuyên hàng trong Bigtable đã dẫn đến những phàn nàn thường xuyên; Percolator [32] được xây dựng một phần để giải quyết thiếu sót này. Một số tác giả đã cho rằng commit hai pha tổng quát là quá đắt để hỗ trợ, do các vấn đề về hiệu năng hoặc tính khả dụng mà nó gây ra [9, 10, 19]. Chúng tôi tin rằng tốt hơn là để các lập trình viên ứng dụng xử lý các vấn đề hiệu năng do việc sử dụng quá mức các giao dịch khi các nút thắt xuất hiện, thay vì luôn viết mã để né tránh sự thiếu vắng các giao dịch. Việc chạy commit hai pha trên Paxos giảm nhẹ các vấn đề về tính khả dụng.

Mô hình dữ liệu ứng dụng được xếp lớp bên trên các ánh xạ khóa-giá trị được phân nhóm theo directory được triển khai hỗ trợ. Một ứng dụng tạo một hoặc nhiều cơ sở dữ liệu trong một universe. Mỗi cơ sở dữ liệu có thể chứa số lượng bảng có lược đồ không giới hạn. Các bảng trông giống như các bảng cơ sở dữ liệu quan hệ, với các hàng, cột và các giá trị có phiên bản. Chúng tôi sẽ không đi vào chi tiết về ngôn ngữ truy vấn cho Spanner. Nó giống SQL với một số mở rộng để hỗ trợ các trường có giá trị protocol-buffer.

Mô hình dữ liệu của Spanner không hoàn toàn quan hệ, vì các hàng phải có tên. Chính xác hơn, mọi bảng được yêu cầu có một tập hợp có thứ tự gồm một hoặc nhiều cột khóa chính. Yêu cầu này là nơi Spanner vẫn giống một kho khóa-giá trị: các khóa chính tạo thành tên cho một hàng, và mỗi bảng định nghĩa một ánh xạ từ các cột khóa chính tới các cột không phải khóa chính. Một hàng chỉ tồn tại nếu một số giá trị (ngay cả khi là NULL) được định nghĩa cho các khóa của hàng đó. Việc áp đặt cấu trúc này hữu ích vì nó cho phép các ứng dụng kiểm soát tính cục bộ của dữ liệu thông qua lựa chọn các khóa của chúng.

Hình 4 chứa một lược đồ Spanner ví dụ để lưu trữ siêu dữ liệu ảnh trên cơ sở mỗi người dùng, mỗi album. Ngôn ngữ lược đồ tương tự như của Megastore, với yêu cầu bổ sung rằng mọi cơ sở dữ liệu Spanner phải được các máy khách phân vùng thành một hoặc nhiều hệ phân cấp của các bảng. Các ứng dụng máy khách khai báo các hệ phân cấp trong các lược đồ cơ sở dữ liệu thông qua các khai báo INTERLEAVE IN. Bảng ở đầu một hệ phân cấp là một bảng thư mục. Mỗi hàng trong một bảng thư mục với khóa $K$, cùng với tất cả các hàng trong các bảng hậu duệ bắt đầu bằng $K$ theo thứ tự từ điển, tạo thành một thư mục. ON DELETE CASCADE chỉ ra rằng việc xóa một hàng trong bảng thư mục sẽ xóa mọi hàng con liên quan. Hình này cũng minh họa bố cục đan xen cho cơ sở dữ liệu ví dụ: với

CREATE TABLE Users {
    uid INT64 NOT NULL, email STRING
} PRIMARY KEY (uid), DIRECTORY;

CREATE TABLE Albums {
    uid INT64 NOT NULL, aid INT64 NOT NULL,
    name STRING
} PRIMARY KEY (uid, aid),
INTERLEAVE IN PARENT Users ON DELETE CASCADE;

| Users(1) | Albums(1,1) | Albums(1,2) | Users(2) | Albums(2,1) | Albums(2,2) | Albums(2,3) |
| --- | --- | --- | --- | --- | --- | --- |

Thư mục 3665

Ví dụ Thư mục 453, Albums $(2,1)$ biểu diễn hàng từ bảng Albums cho user_id 2, album_id 1. Việc đan xen các bảng này để tạo thành các thư mục có ý nghĩa quan trọng vì nó cho phép các máy khách mô tả các mối quan hệ cục bộ tồn tại giữa nhiều bảng, điều cần thiết để có hiệu năng tốt trong một cơ sở dữ liệu phân mảnh, phân tán. Nếu không có nó, Spanner sẽ không biết các mối quan hệ cục bộ quan trọng nhất.

Hình 4: Lược đồ Spanner ví dụ cho siêu dữ liệu ảnh và sự đan xen được ngụ ý bởi INTERLEAVE IN. {#corbett-2012-spanner-fig-4 .figure tag=00A4}
