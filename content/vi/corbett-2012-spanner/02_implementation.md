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
content_sha256: 202b634609649c292270bdc297788af6ed09208458f935109e35f2d9cfda7317
translated_from: content/en/corbett-2012-spanner/02_implementation.md
source_content_sha256: 824c517dc3bb6707da0f5607a35f6b2c4f083b94bb3a19d05ac9be99a7032886
translation_model: gpt-6-astra
translation_run: 20260914T212527Z
glossary_version: 6
glossary_terms_sha256: a534ae50d60bff0e03804fd3c150e37d1876484531ab87df9c72dc4d0c455eb2
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Phần này mô tả cấu trúc và cơ sở lý giải cho cách triển khai Spanner. Tiếp đó, phần này mô tả trừu tượng hóa thư mục (directory), được dùng để quản lý sao chép và tính cục bộ của dữ liệu, đồng thời là đơn vị di chuyển dữ liệu. Cuối cùng, phần này mô tả mô hình dữ liệu của chúng tôi, lý do Spanner có dạng một cơ sở dữ liệu quan hệ thay vì một kho khóa-giá trị, và cách các ứng dụng có thể kiểm soát tính cục bộ của dữ liệu.

Một bản triển khai Spanner được gọi là một vũ trụ (universe). Do Spanner quản lý dữ liệu trên toàn cầu, sẽ chỉ có một số ít vũ trụ đang hoạt động. Hiện chúng tôi vận hành một vũ trụ dành cho kiểm thử/thử nghiệm, một vũ trụ dành cho phát triển/vận hành thực tế, và một vũ trụ chỉ dành cho vận hành thực tế.

Spanner được tổ chức thành một tập hợp các vùng, trong đó mỗi vùng gần tương đương với một bản triển khai các server Bigtable [9]. Vùng là đơn vị triển khai về mặt quản trị. Tập hợp các vùng cũng là tập hợp các vị trí mà dữ liệu có thể được sao chép giữa chúng. Có thể thêm vùng vào hoặc loại bỏ vùng khỏi một hệ thống đang hoạt động khi các trung tâm dữ liệu mới được đưa vào sử dụng hoặc các trung tâm dữ liệu cũ ngừng hoạt động. Vùng cũng là đơn vị cách ly vật lý: một trung tâm dữ liệu có thể có một hoặc nhiều vùng, chẳng hạn khi dữ liệu của các ứng dụng khác nhau phải được phân vùng trên các tập hợp server khác nhau trong cùng trung tâm dữ liệu.

Hình 1 minh họa các server trong một vũ trụ Spanner. Một vùng có một zonemaster và từ một trăm đến vài nghìn spanserver. Zonemaster phân công dữ liệu cho các spanserver; các spanserver phục vụ dữ liệu cho máy khách. Máy khách sử dụng các proxy định vị của từng vùng để tìm các spanserver được phân công phục vụ dữ liệu của mình. Hiện tại, bộ chủ quản vũ trụ và bộ điều khiển bố trí đều chỉ có một thực thể duy nhất. Bộ chủ quản vũ trụ chủ yếu là một bảng điều khiển hiển thị thông tin trạng thái về tất cả các vùng để gỡ lỗi tương tác. Bộ điều khiển bố trí xử lý việc tự động di chuyển dữ liệu giữa các vùng trên thang thời gian tính bằng phút. Bộ điều khiển bố trí định kỳ trao đổi với các spanserver để tìm dữ liệu cần di chuyển, nhằm đáp ứng các ràng buộc sao chép đã cập nhật hoặc để cân bằng tải. Do giới hạn dung lượng bài viết, chúng tôi chỉ mô tả chi tiết spanserver.

Hình.

Hình 1: Tổ chức server của Spanner. {#corbett-2012-spanner-fig-1 .figure tag=00A2}

### 2.1 Ngăn xếp phần mềm Spanserver {#corbett-2012-spanner-s2-1 .section tag=00A3}

Phần này tập trung vào cách triển khai spanserver để minh họa cách sao chép và giao dịch phân tán được xây dựng thành các lớp trên bản triển khai dựa trên Bigtable của chúng tôi. Ngăn xếp phần mềm được trình bày trong Hình 2. Ở lớp dưới cùng, mỗi spanserver chịu trách nhiệm quản lý từ 100 đến 1000 thực thể của một cấu trúc dữ liệu gọi là tablet. Tablet tương tự trừu tượng hóa tablet của Bigtable ở chỗ nó triển khai một đa tập các ánh xạ sau:

```text
(key:string, timestamp:int64) → string
```

Khác với Bigtable, Spanner gán dấu thời gian cho dữ liệu; đây là một điểm quan trọng khiến Spanner giống cơ sở dữ liệu đa phiên bản hơn là kho khóa-giá trị. Trạng thái của một tablet được lưu trong một tập hợp các file có dạng cây B và một nhật ký ghi trước (write-ahead log), tất cả đều nằm trên một hệ thống file phân tán có tên Colossus (hệ thống kế nhiệm Google File System [[ghemawat-2003-gfs]]).

Để hỗ trợ sao chép, mỗi spanserver triển khai một máy trạng thái Paxos duy nhất trên mỗi tablet. (Một phiên bản ban đầu của Spanner hỗ trợ nhiều máy trạng thái Paxos trên mỗi tablet, cho phép các cấu hình sao chép linh hoạt hơn. Độ phức tạp của thiết kế đó khiến chúng tôi từ bỏ nó.) Mỗi máy trạng thái lưu siêu dữ liệu và nhật ký trong tablet tương ứng. Bản triển khai Paxos của chúng tôi hỗ trợ các nút lãnh đạo tồn tại lâu dài với quyền lãnh đạo có thời hạn dựa trên thời gian, mặc định là 10 giây. Bản triển khai Spanner hiện tại ghi nhật ký mỗi thao tác ghi Paxos hai lần: một lần trong nhật ký của tablet và một lần trong nhật ký Paxos. Lựa chọn này nhằm thuận tiện cho việc triển khai, và nhiều khả năng chúng tôi sẽ khắc phục điều này về sau. Bản triển khai Paxos của chúng tôi sử dụng đường ống để cải thiện thông lượng của Spanner khi có độ trễ WAN; tuy nhiên, Paxos áp dụng các thao tác ghi theo thứ tự (một đặc điểm mà chúng tôi sẽ dựa vào trong Phần 4).

Các máy trạng thái Paxos được dùng để triển khai một đa tập các ánh xạ được sao chép với tính nhất quán. Trạng thái ánh xạ khóa-giá trị của mỗi bản sao được lưu trong tablet tương ứng. Các thao tác ghi phải khởi tạo giao thức Paxos tại nút lãnh đạo; các thao tác đọc truy cập trạng thái trực tiếp từ tablet bên dưới tại bất kỳ bản sao nào đã được cập nhật đủ mới. Tập hợp các bản sao được gọi chung là một *nhóm Paxos*.

Tại mỗi bản sao đóng vai trò lãnh đạo, mỗi spanserver triển khai một *bảng khóa* để thực hiện điều khiển đồng thời. Bảng khóa chứa trạng thái phục vụ khóa hai pha: nó ánh xạ các khoảng khóa tới các trạng thái khóa. (Lưu ý rằng việc có một nút lãnh đạo Paxos tồn tại lâu dài là thiết yếu để quản lý bảng khóa hiệu quả.) Trong cả Bigtable lẫn Spanner, chúng tôi thiết kế để hỗ trợ các giao dịch kéo dài (ví dụ, để tạo báo cáo, có thể mất khoảng vài phút), vốn có hiệu năng kém khi sử dụng điều khiển đồng thời lạc quan trong trường hợp có xung đột. Các thao tác cần đồng bộ hóa, chẳng hạn như đọc trong giao dịch, lấy khóa trong bảng khóa; các thao tác khác bỏ qua bảng khóa.

Tại mỗi bản sao đóng vai trò lãnh đạo, mỗi spanserver còn triển khai một *bộ quản lý giao dịch* để hỗ trợ giao dịch phân tán. Bộ quản lý giao dịch được dùng để triển khai một *nút lãnh đạo tham gia*; các bản sao khác trong nhóm sẽ được gọi là *các nút phụ tham gia*. Nếu một giao dịch chỉ liên quan đến một nhóm Paxos (như trường hợp của phần lớn giao dịch), nó có thể bỏ qua bộ quản lý giao dịch, vì bảng khóa kết hợp với Paxos cung cấp các tính chất giao dịch. Nếu một giao dịch liên quan đến nhiều nhóm Paxos, các nút lãnh đạo của những nhóm đó phối hợp để thực hiện xác nhận hai pha. Một trong các nhóm tham gia được chọn làm bộ điều phối: nút lãnh đạo tham gia của nhóm đó sẽ được gọi là *nút lãnh đạo điều phối*, và các nút phụ của nhóm đó là *các nút phụ điều phối*. Trạng thái của mỗi bộ quản lý giao dịch được lưu trong nhóm Paxos bên dưới (và do đó được sao chép).

### 2.2 Thư mục và bố trí {#corbett-2012-spanner-s2-2 .section tag=0125}

Trên tập hợp các ánh xạ khóa-giá trị, bản triển khai Spanner hỗ trợ một trừu tượng hóa gom nhóm gọi là *thư mục* (directory), tức một tập hợp các khóa liên tiếp có chung tiền tố. (Việc chọn thuật ngữ *thư mục* là một sự tình cờ trong lịch sử; thuật ngữ phù hợp hơn có thể là *nhóm.*) Chúng tôi sẽ giải thích nguồn gốc của tiền tố đó trong Mục 2.3. Việc hỗ trợ thư mục cho phép các ứng dụng kiểm soát tính cục bộ của dữ liệu bằng cách lựa chọn khóa cẩn thận.

Thư mục là đơn vị bố trí dữ liệu. Toàn bộ dữ liệu trong một thư mục có cùng cấu hình sao chép. Khi dữ liệu được di chuyển giữa các nhóm Paxos, dữ liệu được di chuyển theo từng thư mục, như minh họa trong Hình 3. Spanner có thể di chuyển một thư mục để giảm tải cho một nhóm Paxos; để đặt các thư mục thường được truy cập cùng nhau vào cùng một nhóm; hoặc để chuyển một thư mục vào nhóm gần các bên truy cập thư mục đó hơn. Các thư mục có thể được di chuyển trong khi các thao tác của máy khách vẫn đang diễn ra. Có thể kỳ vọng rằng một thư mục 50MB được di chuyển trong vài giây.

Việc một nhóm Paxos có thể chứa nhiều thư mục có nghĩa là tablet của Spanner khác với tablet của Bigtable: tablet của Spanner không nhất thiết là một phân vùng liên tiếp duy nhất theo thứ tự từ điển của không gian hàng. Thay vào đó, tablet của Spanner là một vùng chứa có thể bao gồm nhiều phân vùng của không gian hàng. Chúng tôi đưa ra quyết định này để có thể đặt nhiều thư mục thường được truy cập cùng nhau tại cùng một nơi.

Movedir là tác vụ nền được dùng để di chuyển các thư mục giữa các nhóm Paxos [14]. Movedir cũng được dùng để thêm bản sao vào hoặc loại bỏ bản sao khỏi các nhóm Paxos [25], vì Spanner chưa hỗ trợ thay đổi cấu hình ngay trong Paxos. Movedir không được triển khai dưới dạng một giao dịch duy nhất, nhằm tránh chặn các thao tác đọc và ghi đang diễn ra khi di chuyển một lượng lớn dữ liệu. Thay vào đó, movedir ghi nhận việc bắt đầu di chuyển dữ liệu và di chuyển dữ liệu trong nền. Khi đã di chuyển gần hết dữ liệu, chỉ còn lại một lượng nhỏ, nó sử dụng một giao dịch để di chuyển lượng nhỏ đó và cập nhật siêu dữ liệu cho hai nhóm Paxos một cách nguyên tử.

Thư mục cũng là đơn vị nhỏ nhất mà ứng dụng có thể đặc tả các thuộc tính sao chép theo địa lý (hay gọi ngắn gọn là bố trí). Thiết kế ngôn ngữ đặc tả bố trí của chúng tôi phân tách các trách nhiệm quản lý cấu hình sao chép. Quản trị viên kiểm soát hai chiều: số lượng và kiểu bản sao, cùng với vị trí địa lý của các bản sao đó. Họ tạo một danh mục các tùy chọn có tên theo hai chiều này (ví dụ: Bắc Mỹ, sao chép thành 5 bản với 1 bản sao làm chứng). Ứng dụng kiểm soát cách sao chép dữ liệu bằng cách gắn thẻ cho từng cơ sở dữ liệu và/hoặc từng thư mục bằng một tổ hợp các tùy chọn đó. Ví dụ, một ứng dụng có thể lưu dữ liệu của mỗi người dùng cuối trong một thư mục riêng, nhờ đó dữ liệu của người dùng $A$ có thể có ba bản sao ở châu Âu, còn dữ liệu của người dùng $B$ có thể có năm bản sao ở Bắc Mỹ.

Để trình bày rõ ràng, chúng tôi đã đơn giản hóa quá mức. Trên thực tế, Spanner sẽ phân mảnh một thư mục thành nhiều mảnh nếu thư mục đó trở nên quá lớn. Các mảnh có thể được phục vụ từ những nhóm Paxos khác nhau (và do đó từ những server khác nhau). Movedir thực ra di chuyển các mảnh giữa các nhóm, chứ không phải toàn bộ thư mục.

### 2.3 Mô hình dữ liệu {#corbett-2012-spanner-s2-3 .section tag=010D}

Spanner cung cấp cho các ứng dụng tập hợp tính năng dữ liệu sau: một mô hình dữ liệu dựa trên các bảng bán quan hệ có lược đồ, một ngôn ngữ truy vấn và các giao dịch đa dụng. Việc chuyển sang hỗ trợ các tính năng này được thúc đẩy bởi nhiều yếu tố. Sự phổ biến của Megastore [5] cho thấy nhu cầu hỗ trợ các bảng bán quan hệ có lược đồ và sao chép đồng bộ. Ít nhất 300 ứng dụng trong Google sử dụng Megastore (mặc dù hiệu năng của nó tương đối thấp) vì mô hình dữ liệu của nó dễ quản lý hơn mô hình của Bigtable, và vì nó hỗ trợ sao chép đồng bộ giữa các trung tâm dữ liệu. (Bigtable chỉ hỗ trợ sao chép với tính nhất quán cuối cùng giữa các trung tâm dữ liệu.) Các ứng dụng nổi tiếng của Google sử dụng Megastore bao gồm Gmail, Picasa, Calendar, Android Market và AppEngine. Nhu cầu hỗ trợ một ngôn ngữ truy vấn tương tự SQL trong Spanner cũng rất rõ ràng, xét đến sự phổ biến của Dremel [28] với vai trò công cụ phân tích dữ liệu tương tác. Cuối cùng, việc thiếu các giao dịch xuyên hàng trong Bigtable dẫn đến những phàn nàn thường xuyên; Percolator [32] được xây dựng một phần để khắc phục thiếu sót này. Một số tác giả cho rằng chi phí hỗ trợ xác nhận hai pha (two-phase commit) trong trường hợp tổng quát là quá cao, do những vấn đề về hiệu năng hoặc tính sẵn sàng mà nó gây ra [9, 10, 19]. Chúng tôi cho rằng tốt hơn là để các lập trình viên ứng dụng xử lý những vấn đề hiệu năng do lạm dụng giao dịch khi các nút thắt xuất hiện, thay vì luôn phải viết mã để khắc phục việc thiếu giao dịch. Thực thi xác nhận hai pha trên Paxos làm giảm các vấn đề về tính sẵn sàng.

Mô hình dữ liệu ứng dụng được xây dựng thành một lớp bên trên các ánh xạ khóa-giá trị được gom nhóm theo thư mục mà bản triển khai hỗ trợ. Một ứng dụng tạo một hoặc nhiều cơ sở dữ liệu trong một vũ trụ. Mỗi cơ sở dữ liệu có thể chứa số lượng không giới hạn các bảng có lược đồ. Các bảng trông giống bảng trong cơ sở dữ liệu quan hệ, với các hàng, cột và giá trị có phiên bản. Chúng tôi sẽ không đi sâu vào ngôn ngữ truy vấn của Spanner. Nó giống SQL với một số phần mở rộng để hỗ trợ các trường có giá trị kiểu protocol buffer.

Mô hình dữ liệu của Spanner không thuần quan hệ, ở chỗ các hàng phải có tên. Chính xác hơn, mỗi bảng bắt buộc phải có một tập hợp có thứ tự gồm một hoặc nhiều cột khóa chính. Yêu cầu này là điểm mà Spanner vẫn giống một kho khóa-giá trị: các khóa chính tạo thành tên của một hàng, và mỗi bảng định nghĩa một ánh xạ từ các cột khóa chính sang các cột không thuộc khóa chính. Một hàng chỉ tồn tại nếu có một giá trị nào đó (kể cả NULL) được định nghĩa cho các khóa của hàng đó. Việc áp đặt cấu trúc này là hữu ích vì nó cho phép các ứng dụng kiểm soát tính cục bộ của dữ liệu thông qua việc lựa chọn khóa.

Hình 4 trình bày một ví dụ về lược đồ Spanner để lưu trữ siêu dữ liệu ảnh theo từng người dùng, từng album. Ngôn ngữ lược đồ tương tự ngôn ngữ của Megastore, với yêu cầu bổ sung rằng mỗi cơ sở dữ liệu Spanner phải được các máy khách phân vùng thành một hoặc nhiều hệ phân cấp bảng. Các ứng dụng máy khách khai báo các hệ phân cấp trong lược đồ cơ sở dữ liệu thông qua các khai báo INTERLEAVE IN. Bảng ở đỉnh của một hệ phân cấp là bảng thư mục (directory table). Mỗi hàng trong một bảng thư mục có khóa $K$, cùng với tất cả các hàng trong các bảng hậu duệ bắt đầu bằng $K$ theo thứ tự từ điển, tạo thành một thư mục. ON DELETE CASCADE quy định rằng việc xóa một hàng trong bảng thư mục sẽ xóa mọi hàng con liên quan. Hình này cũng minh họa cách bố trí xen kẽ (interleaving) cho cơ sở dữ liệu ví dụ: chẳng

```text
CREATE TABLE Users {
    uid INT64 NOT NULL, email STRING
} PRIMARY KEY (uid), DIRECTORY;

CREATE TABLE Albums {
    uid INT64 NOT NULL, aid INT64 NOT NULL,
    name STRING
} PRIMARY KEY (uid, aid),
INTERLEAVE IN PARENT Users ON DELETE CASCADE;
```

| Users(1) | Albums(1,1) | Albums(1,2) | Users(2) | Albums(2,1) | Albums(2,2) | Albums(2,3) |
| --- | --- | --- | --- | --- | --- | --- |

Thư mục 3665

Thư mục 453 hạn, Albums $(2,1)$ biểu diễn hàng trong bảng Albums ứng với user_id 2, album_id 1. Việc xen kẽ các bảng để tạo thành các thư mục có ý nghĩa quan trọng vì nó cho phép các máy khách mô tả các mối quan hệ về tính cục bộ (locality) tồn tại giữa nhiều bảng, điều cần thiết để đạt hiệu năng tốt trong một cơ sở dữ liệu phân tán có phân mảnh. Nếu không có cách bố trí này, Spanner sẽ không biết được các mối quan hệ quan trọng nhất về tính cục bộ.

Hình 4: Ví dụ về lược đồ Spanner cho siêu dữ liệu ảnh và cách xen kẽ được xác định bởi INTERLEAVE IN. {#corbett-2012-spanner-fig-4 .figure tag=00A4}
