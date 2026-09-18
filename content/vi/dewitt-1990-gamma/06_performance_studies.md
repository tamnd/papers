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
section: "6"
section_title: Các nghiên cứu về hiệu năng
tag: "0275"
kind: section
lang: vi
source: http://db.cs.berkeley.edu/cs286/papers/gamma-tkde1990.pdf
pdf_sha256: 420d33f44b8e050f33517cdff1299a58838b4ad826d80a6617200332ea02be5e
pdf_pages: 23-34
extraction: vision
extraction_model: gpt-5
content_sha256: c077ad6eec4e4cd2d42ad67b3b0088e83bae520b05e30f3f53916bf5bb0136d6
translated_from: content/en/dewitt-1990-gamma/06_performance_studies.md
source_content_sha256: 44b46d758a0a7f9e6df90fa280db25c00920503a6bf1ab01e6a9a5887e6100e3
translation_model: gpt-5
translation_run: 20260916T132956Z
glossary_version: 6
glossary_terms_sha256: a534ae50d60bff0e03804fd3c150e37d1876484531ab87df9c72dc4d0c455eb2
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

### 6.1. Giới thiệu và Tổng quan về Thí nghiệm {#dewitt-1990-gamma-s6-1 .section tag=0276}

Để đánh giá hiệu năng của phiên bản siêu khối của Gamma, ba độ đo khác nhau đã được sử dụng. Trước tiên, tập các truy vấn phép đo chuẩn Wisconsin [BITT83] được chạy trên một cấu hình gồm 30 bộ xử lý với ba kích thước khác nhau của các quan hệ: 100,000, 1 triệu, và 10 triệu bộ. Trong khi hiệu năng tuyệt đối là một độ đo của một hệ thống cơ sở dữ liệu, tăng tốc và mở rộng quy mô cũng là các độ đo hữu ích cho các máy cơ sở dữ liệu đa bộ xử lý [ENGL89]. Tăng tốc là một độ đo thú vị vì nó chỉ ra liệu các bộ xử lý và ổ đĩa bổ sung có dẫn đến sự giảm tương ứng trong thời gian đáp ứng của một truy vấn hay không. Đối với một tập con các truy vấn phép đo chuẩn Wisconsin, chúng tôi đã tiến hành các thí nghiệm tăng tốc bằng cách thay đổi số lượng bộ xử lý từ 1 đến 30 trong khi kích thước của các quan hệ kiểm tra được cố định ở 1 triệu bộ. Với cùng tập truy vấn đó, chúng tôi cũng tiến hành các thí nghiệm mở rộng quy mô bằng cách thay đổi số lượng bộ xử lý từ 5 đến 30 trong khi kích thước của các quan hệ kiểm tra lần lượt được tăng từ 1 đến 6 triệu bộ. Mở rộng quy mô là một độ đo có giá trị vì nó chỉ ra liệu một thời gian đáp ứng không đổi có thể được duy trì khi tải công việc được tăng lên bằng cách thêm một số lượng bộ xử lý và ổ đĩa tỷ lệ thuận hay không. [ENGL89] mô tả một tập kiểm tra tương tự trên Release 2 của hệ thống NonStop SQL của Tandem.

Các quan hệ phép đo chuẩn được sử dụng cho các thí nghiệm dựa trên các quan hệ phép đo chuẩn Wisconsin tiêu chuẩn [BITT83]. Mỗi quan hệ bao gồm các bộ có độ rộng 208 byte. Chúng tôi đã xây dựng các phiên bản 100,000, 1 triệu, và 10 triệu bộ của các quan hệ phép đo chuẩn. Hai bản sao của mỗi quan hệ được tạo và nạp. Ngoại trừ trường hợp được ghi chú khác, các bộ được phân tán bằng cách phân vùng băm trên thuộc tính Unique1. Trong mọi trường hợp, các kết quả được trình bày biểu diễn thời gian đáp ứng trung bình của một số truy vấn tương đương. Gamma được cấu hình để sử dụng kích thước trang đĩa 8K byte và một nhóm bộ đệm 2 megabyte.

Kết quả của tất cả các truy vấn được lưu trữ trong cơ sở dữ liệu. Chúng tôi tránh trả dữ liệu về máy chủ để tránh việc tốc độ của liên kết truyền thông giữa máy chủ và máy cơ sở dữ liệu hoặc chính bộ xử lý máy chủ ảnh hưởng đến kết quả. Bằng cách lưu trữ các quan hệ kết quả trong cơ sở dữ liệu, tác động của các yếu tố này được giảm thiểu - với chi phí phải chịu thêm chi phí phân tán và lưu trữ các quan hệ kết quả.

### 6.2. Các truy vấn lựa chọn {#dewitt-1990-gamma-s6-2 .section tag=0277}

### Hiệu năng tương đối so với kích thước quan hệ {#dewitt-1990-gamma-s-performance-relative-to-relation-size .section tag=0278}

Tập kiểm tra lựa chọn đầu tiên được thiết kế để xác định cách Gamma phản hồi khi kích thước của các quan hệ nguồn được tăng lên trong khi cấu hình máy được giữ ở mức 30 bộ xử lý với các ổ đĩa. Lý tưởng nhất, thời gian đáp ứng của một truy vấn nên tăng theo một hàm tuyến tính của kích thước các quan hệ đầu vào và kết quả. Đối với các kiểm tra này, sáu truy vấn lựa chọn khác nhau được chạy trên ba tập quan hệ chứa lần lượt 100,000, 1 triệu, và 10 triệu bộ. Hai truy vấn đầu tiên có hệ số chọn lọc là 1% và 10% và không sử dụng bất kỳ chỉ mục nào. Truy vấn thứ ba và thứ tư có cùng các hệ số chọn lọc nhưng sử dụng một chỉ mục phân cụm để định vị các bộ thỏa mãn. Truy vấn thứ năm có hệ số chọn lọc 1% và sử dụng một chỉ mục không phân cụm để định vị các bộ mong muốn. Không có truy vấn lựa chọn 10% thông qua chỉ mục không phân cụm vì bộ tối ưu hóa truy vấn của Gamma chọn sử dụng quét tuần tự cho truy vấn này. Truy vấn cuối cùng sử dụng một chỉ mục phân cụm để lấy một bộ duy nhất. Ngoại trừ truy vấn cuối cùng, vị từ của mỗi truy vấn chỉ định một miền giá trị và do đó, vì các quan hệ đầu vào được phân tán bằng băm, truy vấn phải được gửi đến tất cả các nút.

Các kết quả từ các kiểm tra này được lập bảng trong Bảng 3. Phần lớn, thời gian thực thi của mỗi truy vấn mở rộng theo một hàm khá tuyến tính của kích thước các quan hệ đầu vào và đầu ra. Tuy nhiên, có một số trường hợp việc mở rộng không hoàn toàn tuyến tính. Trước tiên hãy xét phép lựa chọn 1% không có chỉ mục. Trong khi sự tăng thời gian đáp ứng khi kích thước quan hệ đầu vào được tăng từ 1 đến 10 triệu bộ gần như hoàn toàn tuyến tính (8.16 secs. đến 81.15 secs.), sự tăng từ 100,000 bộ đến 1 triệu bộ (0.45 sec. đến 8.16 sec) thực sự là dưới tuyến tính. Phép lựa chọn 10% sử dụng chỉ mục phân cụm là một ví dụ khác trong đó việc tăng kích thước quan hệ đầu vào lên một hệ số mười dẫn đến mức tăng lớn hơn mười lần trong thời gian đáp ứng của truy vấn. Truy vấn này mất 5.02 giây trên quan hệ 1 triệu bộ và 61.86 giây trên quan hệ 10 triệu bộ. Để hiểu tại sao điều này xảy ra, cần xem xét tác động của thời gian tìm kiếm lên thời gian thực thi của truy vấn. Vì hai bản sao của mỗi quan hệ đã được nạp, khi hai quan hệ một triệu bộ được phân tán trên 30 ổ đĩa, các mảnh chiếm xấp xỉ 53 cylinder (trong số 1224) trên mỗi ổ đĩa. Hai quan hệ mười triệu bộ lấp đầy khoảng 530 cylinder trên mỗi ổ đĩa. Khi mỗi trang của quan hệ kết quả được ghi vào đĩa, các đầu đọc đĩa phải được di chuyển từ vị trí hiện tại của chúng trên quan hệ đầu vào đến một khối trống trên đĩa. Vì vậy, với quan hệ 10 triệu bộ, chi phí ghi mỗi trang đầu ra cao hơn nhiều.

Như mong đợi, việc sử dụng chỉ mục B-tree phân cụm luôn cung cấp sự cải thiện đáng kể về hiệu năng. Một nhận xét rút ra từ Bảng 3 là tính nhất quán tương đối của thời gian thực thi của các truy vấn lựa chọn thông qua chỉ mục phân cụm. Lưu ý rằng thời gian thực thi của một phép lựa chọn 10% trên quan hệ 1 triệu bộ gần như giống hệt thời gian thực thi của phép lựa chọn 1% trên quan hệ 10 triệu bộ. Trong cả hai trường hợp, 100,000 bộ được lấy và lưu trữ, dẫn đến chi phí I/O và CPU giống hệt nhau.

Hàng cuối cùng của Bảng 3 trình bày thời gian cần thiết để chọn một bộ từ đơn bằng cách sử dụng chỉ mục phân cụm và trả nó về máy chủ. Vì vị từ chọn nằm trên thuộc tính phân vùng, truy vấn được hướng đến một nút duy nhất, tránh chi phí phụ trội của việc khởi động truy vấn trên tất cả 30 bộ xử lý. Thời gian đáp ứng cho truy vấn này tăng đáng kể khi kích thước

**Bảng 3 - Các truy vấn chọn**  
**30 Bộ xử lý với các đĩa**  
(Tất cả thời gian thực thi tính bằng giây)

```text
                                                     Number of Tuples in Source Relation
Query Description                                    100,000          1,000,000          10,000,000

1% nonindexed selection                              0.45             8.16               81.15
10% nonindexed selection                             0.82             10.82              135.61
1% selection using clustered index                   0.35             0.82               5.12
10% selection using clustered index                  0.77             5.02               61.86
1% selection using non-clustered index               0.60             8.77               113.37
single tuple select using clustered index            0.08             0.08               0.14
```

của quan hệ được tăng từ 1 triệu lên 10 triệu bộ từ vì chiều cao của B-tree tăng từ hai lên ba mức.

### Các thí nghiệm tăng tốc {#dewitt-1990-gamma-s-speedup-experiments .section tag=0279}

Trong phần này, chúng tôi xem xét cách thời gian đáp ứng của cả các truy vấn chọn không có chỉ mục và có chỉ mục trên quan hệ 1 triệu bộ từ[^1] bị ảnh hưởng bởi số lượng bộ xử lý được sử dụng để thực thi truy vấn. Lý tưởng nhất là có thể thấy sự cải thiện tuyến tính về hiệu năng khi số lượng bộ xử lý được tăng từ 1 lên 30. Việc tăng số lượng bộ xử lý làm tăng cả công suất CPU tổng hợp và băng thông I/O khả dụng, đồng thời giảm số lượng bộ từ phải được xử lý bởi mỗi bộ xử lý.

Trong Hình 12, thời gian đáp ứng trung bình cho các truy vấn chọn không có chỉ mục 1% và 10% trên quan hệ một triệu bộ từ được trình bày. Như mong đợi, thời gian đáp ứng của mỗi truy vấn giảm khi số lượng nút được tăng lên. Thời gian đáp ứng cao hơn đối với phép chọn 10% do chi phí của việc phân cụm lại và lưu trữ quan hệ kết quả. Mặc dù luôn có thể lưu trữ các bộ từ kết quả cục bộ, bằng cách phân vùng tất cả các quan hệ kết quả theo cách round-robin (hoặc băm), có thể đảm bảo rằng các mảnh của mỗi quan hệ kết quả chứa xấp xỉ cùng một số lượng bộ từ. Các đường cong tăng tốc tương ứng với Hình 12 được trình bày trong Hình 13. Trong Hình 14, thời gian đáp ứng trung bình được trình bày như một hàm của số lượng bộ xử lý cho ba truy vấn sau: một phép chọn 1% thông qua chỉ mục phân cụm, một phép chọn 10% thông qua chỉ mục phân cụm, và một phép chọn 1% thông qua chỉ mục không phân cụm,

[^1]: Quan hệ 1 triệu bộ từ được sử dụng cho các thí nghiệm này vì quan hệ 10 triệu bộ từ sẽ không vừa trên 1 ổ đĩa.

Hình 12

Hình 13 chỉ mục phân cụm, tất cả đều truy cập quan hệ 1 triệu bộ từ. Các đường cong tăng tốc tương ứng được trình bày trong Hình 15.

Trong số các đường cong tăng tốc được trình bày trong Hình 13 và 14, ba truy vấn là siêu tuyến tính, một truy vấn hơi dưới tuyến tính, và một truy vấn dưới tuyến tính đáng kể. Trước tiên, hãy xem xét phép chọn 10% thông qua quét quan hệ, phép chọn 1% thông qua chỉ mục không phân cụm, và phép chọn 10% thông qua chỉ mục phân cụm. Như đã thảo luận ở trên, nguồn gốc của các mức tăng tốc siêu tuyến tính thể hiện bởi các truy vấn này là do sự khác biệt đáng kể về thời gian mà các cấu hình khác nhau dành cho việc tìm kiếm. Với một bộ xử lý, quan hệ 1 triệu bộ từ chiếm xấp xỉ 66% đĩa. Khi cùng quan hệ đó được phân cụm lại trên 30 ổ đĩa, nó chiếm khoảng 2% của mỗi đĩa. Trong trường hợp chọn chỉ mục không phân cụm 1%, mỗi bộ từ được chọn yêu cầu một lần tìm kiếm ngẫu nhiên. Với một bộ xử lý, phạm vi của mỗi lần tìm kiếm ngẫu nhiên xấp xỉ 800 cylinder, trong khi với 30 bộ xử lý, phạm vi của lần tìm kiếm bị giới hạn khoảng 27 cylinder. Vì thời gian tìm kiếm tỷ lệ với căn bậc hai của khoảng cách mà đầu đĩa di chuyển [GRAY88], việc giảm kích thước của mảnh quan hệ trên mỗi đĩa làm giảm đáng kể lượng thời gian mà truy vấn dành cho việc tìm kiếm.

Một hiệu ứng tương tự cũng xảy ra với phép chọn chỉ mục phân cụm 10%. Trong trường hợp này, một khi chỉ mục đã được sử dụng để định vị các bộ từ thỏa mãn truy vấn, mỗi trang đầu vào sẽ tạo ra một trang đầu ra và tại một thời điểm nào đó vùng bộ đệm sẽ được lấp đầy bằng các trang đầu ra bẩn. Để ghi một trang đầu ra, đầu đĩa phải được di chuyển

Hình 14

Hình 15 từ vị trí của nó trên quan hệ đầu vào đến vị trí trên đĩa nơi các trang đầu ra được đặt. Chi phí tương đối của lần tìm kiếm này giảm tỷ lệ thuận khi số lượng bộ xử lý tăng lên, dẫn đến mức tăng tốc siêu tuyến tính cho truy vấn. Phép chọn không có chỉ mục 10% được thể hiện trong Hình 13 cũng siêu tuyến tính vì các lý do tương tự. Lý do truy vấn này không bị ảnh hưởng ở cùng mức độ là vì, không có chỉ mục, thời gian tìm kiếm chiếm một phần nhỏ hơn trong tổng thời gian thực thi của truy vấn.

Phép chọn 1% thông qua chỉ mục phân cụm thể hiện các mức tăng tốc dưới tuyến tính vì chi phí khởi tạo toán tử chọn và lưu trữ trên mỗi bộ xử lý (tổng cộng 0.24 giây cho 30 bộ xử lý) trở thành một phần đáng kể của tổng quá trình thực thi khi số lượng bộ xử lý được tăng lên.

**Các thí nghiệm mở rộng quy mô**

Trong tập cuối cùng của các thí nghiệm selection, số lượng bộ xử lý được thay đổi từ 5 đến 30 trong khi kích thước của các quan hệ đầu vào được tăng tương ứng từ 1 triệu đến 6 triệu bộ. Như được thể hiện trong Figure 16, thời gian phản hồi cho mỗi trong năm truy vấn selection vẫn gần như không đổi. Sự gia tăng nhỏ trong thời gian phản hồi là do chi phí phụ trội của việc khởi tạo toán tử selection và store tại mỗi site. Vì một process đơn được sử dụng để khởi tạo việc thực thi của một truy vấn, khi số lượng bộ xử lý được sử dụng tăng lên, tải trên process này cũng tăng theo tỷ lệ. Chuyển sang sơ đồ khởi tạo truy vấn dựa trên cây [GERB87] sẽ phân phối chi phí phụ trội này giữa tất cả các bộ xử lý.

Figure 16

### 6.3. Các truy vấn Join {#dewitt-1990-gamma-s6-3 .section tag=027A}

Giống như các truy vấn selection trong phần trước, chúng tôi đã tiến hành ba tập thí nghiệm join. Trước tiên, đối với hai truy vấn join khác nhau, chúng tôi thay đổi kích thước của các quan hệ đầu vào trong khi cấu hình của các bộ xử lý được giữ không đổi. Tiếp theo, đối với một truy vấn join, một loạt các thí nghiệm speedup và scaleup đã được tiến hành. Với mỗi phép kiểm tra này, hai cách phân vùng khác nhau của các quan hệ đầu vào đã được sử dụng. Trong trường hợp thứ nhất, các quan hệ đầu vào được decluster bằng cách băm trên thuộc tính join. Trong trường hợp thứ hai, các quan hệ đầu vào được decluster bằng cách sử dụng một thuộc tính khác. Thuật toán join lai được sử dụng cho tất cả các truy vấn.

### Hiệu năng tương đối so với kích thước quan hệ {#dewitt-1990-gamma-s-performance-relative-to-relation-size-2 .section tag=027B}

Truy vấn join đầu tiên [BITT83], joinABprime, là một phép join đơn giản của hai quan hệ: A và Bprime. Quan hệ A chứa lần lượt 100,000, 1 triệu, hoặc 10 triệu bộ. Quan hệ Bprime chứa tương ứng 10,000, 100,000, hoặc 1 triệu bộ. Quan hệ kết quả có cùng số lượng bộ như quan hệ Bprime.[^1] Truy vấn thứ hai, joinAselB, bao gồm một phép join và một phép selection. A và B có cùng số lượng bộ và phép

[^1]: Với mỗi phép toán join, quan hệ kết quả chứa tất cả các trường của cả hai quan hệ đầu vào và do đó các bộ kết quả có độ rộng 416 byte.

selection trên B làm giảm kích thước của B xuống kích thước của quan hệ Bprime trong truy vấn joinABprime tương ứng. Quan hệ kết quả của truy vấn này có cùng số lượng bộ như trong truy vấn joinABprime tương ứng. Ví dụ, nếu A có 10 triệu bộ, thì joinABprime thực hiện join A với một quan hệ Bprime chứa 1 triệu bộ, trong khi trong joinAselB phép selection trên B giới hạn B từ 10 triệu bộ xuống 1 triệu bộ và sau đó thực hiện join kết quả với A.

Biến thể đầu tiên của các truy vấn join được kiểm tra không sử dụng chỉ mục và sử dụng một thuộc tính không phân vùng cho cả thuộc tính join và thuộc tính selection. Do đó, trước khi phép join có thể được thực hiện, hai quan hệ đầu vào phải được phân phối lại bằng cách băm trên giá trị thuộc tính join của mỗi bộ. Kết quả từ các phép kiểm tra này được trình bày trong 2 hàng đầu tiên của Table 4. Biến thể thứ hai của các truy vấn join cũng không sử dụng bất kỳ chỉ mục nào nhưng trong trường hợp này, các quan hệ được phân vùng băm trên thuộc tính join; cho phép bỏ qua giai đoạn phân phối lại của phép join. Kết quả cho các phép kiểm tra này được trình bày trong 2 hàng cuối của Table 4.

Các kết quả trong Table 4 chỉ ra rằng thời gian thực thi của mỗi truy vấn join tăng theo cách gần tuyến tính khi kích thước của các quan hệ đầu vào tăng lên. Gamma không thể hiện tính tuyến tính đối với các truy vấn 10 triệu bộ vì kích thước của quan hệ bên trong (208 megabyte) lớn gấp hai lần không gian khả dụng tổng cộng cho các bảng băm. Vì vậy, thuật toán join Hybrid cần hai bucket để xử lý các truy vấn này. Trong khi các bộ trong bucket đầu tiên có thể được đặt trực tiếp vào các bảng băm cư trú trong bộ nhớ, bucket thứ hai phải được ghi ra disk (xem Section 4.2).

Như dự kiến, phiên bản của mỗi truy vấn trong đó thuộc tính phân vùng được sử dụng làm thuộc tính join chạy nhanh hơn. Từ các kết quả này, có thể ước lượng một cận dưới về tốc độ tổng hợp mà dữ liệu có thể được phân phối lại bởi hypercube Intel iPSC/2. Xét phiên bản của truy vấn joinABprime trong đó một quan hệ một triệu bộ được

Table 4 - Các truy vấn Join  
30 Bộ xử lý với Disk  
(Tất cả thời gian thực thi tính bằng giây)

| Mô tả truy vấn | 100,000 | 1,000,000 | 10,000,000 |
| --- | --- | --- | --- |
| JoinABprime với các thuộc tính không phân vùng của A và B được sử dụng làm thuộc tính join | 3.52 | 28.69 | 438.90 |
| JoinAselB với các thuộc tính không phân vùng của A và B được sử dụng làm thuộc tính join | 2.69 | 25.13 | 373.98 |
| JoinABprime với các thuộc tính phân vùng của A và B được sử dụng làm thuộc tính join | 3.34 | 25.95 | 426.25 |
| JoinAselB với các thuộc tính phân vùng của A và B được sử dụng làm thuộc tính join | 2.74 | 23.77 | 362.89 |

join với một quan hệ 100,000 bộ. Truy vấn này cần 28.69 giây khi phép join không được thực hiện trên thuộc tính phân vùng. Trong quá trình thực thi truy vấn này, 1.1 triệu bộ 208 byte phải được phân phối lại bằng cách băm trên thuộc tính join, tạo ra tốc độ truyền tổng hợp là 7.9 megabyte/giây trong quá trình xử lý truy vấn này. Tuy nhiên, điều này không nên được xem là một ước lượng chính xác về băng thông truyền thông giữa các bộ xử lý tối đa có thể đạt được vì các CPU có thể là yếu tố giới hạn (các disk khó có khả năng là yếu tố giới hạn vì từ Table 3 có thể ước lượng rằng băng thông tổng hợp của 30 disk là khoảng 25 megabyte/giây).

### Các thí nghiệm Speedup {#dewitt-1990-gamma-s-speedup-experiments-2 .section tag=027C}

Đối với các thí nghiệm speedup của join, chúng tôi sử dụng truy vấn joinABprime với một quan hệ A có 1 triệu bộ và một quan hệ Bprime có 100,000 bộ. Số lượng bộ xử lý được thay đổi từ năm đến ba mươi. Vì với ít hơn năm bộ xử lý cần hai hoặc nhiều bucket, việc bao gồm thời gian thực thi cho một bộ xử lý (cần 5 bucket) sẽ khiến thời gian phản hồi cho năm hoặc nhiều bộ xử lý xuất hiện nhanh một cách giả tạo; dẫn đến các đường cong speedup siêu tuyến tính.

Thời gian đáp ứng thu được được biểu diễn trong Hình 17 và các đường cong tăng tốc tương ứng được trình bày trong Hình 18. Từ hình dạng của các đồ thị này, rõ ràng rằng thời gian thực thi của truy vấn được giảm đáng kể khi sử dụng thêm các bộ xử lý. Một số yếu tố ngăn hệ thống đạt được mức tăng tốc tuyến tính hoàn hảo.

Hình 17

Hình 18

Thứ nhất, chi phí khởi động bốn tác vụ toán tử (hai phép quét, một phép nối, và một phép lưu trữ) trên mỗi bộ xử lý tăng theo số lượng bộ xử lý được sử dụng. Thứ hai, ảnh hưởng của việc bỏ qua các thông điệp cục bộ giảm khi số lượng bộ xử lý tăng lên. Ví dụ, xét một cấu hình năm bộ xử lý và phiên bản thuộc tính không phân vùng của truy vấn JoinABprime. Khi mỗi bộ xử lý phân vùng lại các bộ bằng cách băm trên thuộc tính nối, 1/5 số bộ đầu vào mà nó xử lý được dành cho chính nó và sẽ được phần mềm truyền thông bỏ qua. Ngoài ra, khi truy vấn tạo ra các bộ của quan hệ kết quả (được phân vùng theo cách vòng tròn), chúng cũng sẽ được bỏ qua. Khi số lượng bộ xử lý tăng lên, số lượng gói tin được bỏ qua giảm đến mức với 30 bộ xử lý, chỉ 1/30 số gói tin được bỏ qua. Vì các gói tin nội nút này ít tốn kém hơn so với các gói tin liên nút tương ứng, các cấu hình nhỏ hơn sẽ hưởng lợi nhiều hơn từ việc bỏ qua. Trong trường hợp các phép nối theo thuộc tính phân vùng, tất cả các bộ đầu vào sẽ bỏ qua mạng cùng với một phần các bộ đầu ra.

### Các thí nghiệm mở rộng quy mô {#dewitt-1990-gamma-s-scaleup-experiments .section tag=027D}

Truy vấn JoinABprime cũng được sử dụng cho các thí nghiệm mở rộng quy mô của phép nối. Đối với các phép thử này, số lượng bộ xử lý được thay đổi từ 5 đến 30 trong khi kích thước của quan hệ A được thay đổi từ 1 triệu đến 6 triệu bộ theo các bước tăng 1 triệu bộ và kích thước của quan hệ Bprime được thay đổi từ 100,000 đến 600,000 bộ theo các bước tăng 100,000. Với mỗi cấu hình, chỉ cần một bucket nối. Kết quả của các phép thử này được trình bày trong Hình 19. Ba yếu tố góp phần làm tăng nhẹ thời gian đáp ứng. Thứ nhất, tác vụ khởi tạo 4 tiến trình tại mỗi site được thực hiện bởi một bộ xử lý duy nhất. Thứ hai, khi số lượng bộ xử lý tăng lên, ảnh hưởng của việc bỏ qua thông điệp trong quá trình thực thi các truy vấn này giảm đi - đặc biệt trong trường hợp thuộc tính nối không phải là thuộc tính phân vùng. Cuối cùng, thời gian đáp ứng có thể bị giới hạn bởi tốc độ của mạng truyền thông.

Hình 19

### 6.4. Các truy vấn tổng hợp {#dewitt-1990-gamma-s6-4 .section tag=027E}

Các phép thử tổng hợp của chúng tôi bao gồm sự kết hợp giữa các truy vấn tổng hợp vô hướng và các truy vấn hàm tổng hợp chạy trên cấu hình 30 bộ xử lý. Truy vấn đầu tiên tính giá trị nhỏ nhất của một thuộc tính không có chỉ mục. Hai truy vấn tiếp theo lần lượt tính tổng và giá trị nhỏ nhất của một thuộc tính sau khi phân vùng quan hệ thành 20 tập con. Ba kích thước của quan hệ đầu vào được sử dụng: 100,000, 1 triệu, và 10 triệu bộ. Kết quả từ các phép thử này được chứa trong Bảng 5. Vì các toán tử tổng hợp vô hướng và toán tử hàm tổng hợp được thực thi bằng các thuật toán tương tự như các thuật toán được sử dụng bởi các toán tử chọn và nối, tương ứng, nên không tiến hành các thí nghiệm tăng tốc hoặc mở rộng quy mô.

**Bảng 5 - Các truy vấn tổng hợp**  
**30 Bộ xử lý với Đĩa**  
*(Tất cả thời gian thực thi tính bằng giây)*

| Mô tả truy vấn | Số lượng bộ trong quan hệ nguồn |  |  |
| --- | --- | --- | --- |
|  | 100,000 | 1,000,000 | 10,000,000 |
| Tổng hợp vô hướng | 1.10 | 10.36 | 106.42 |
| Hàm tổng hợp Min (20 Phân vùng) | 2.03 | 12.48 | 120.03 |
| Hàm tổng hợp Sum (20 Phân vùng) | 2.03 | 12.39 | 120.22 |

### 6.5. Các truy vấn cập nhật {#dewitt-1990-gamma-s6-5 .section tag=027F}

Tập các phép thử tiếp theo bao gồm sự kết hợp giữa các truy vấn thêm, xóa và sửa đổi trên ba kích thước quan hệ khác nhau: 100,000, 1 triệu, và 10 triệu bộ. Kết quả của các phép thử này được trình bày trong Bảng 6. Vì cơ chế phục hồi của Gamma vẫn chưa hoạt động, các kết quả này cần được xem xét tương ứng.

Truy vấn đầu tiên thêm một bộ đơn vào một quan hệ không tồn tại chỉ mục nào. Truy vấn thứ hai thêm một bộ vào một quan hệ có một chỉ mục tồn tại. Truy vấn thứ ba xóa một bộ đơn khỏi một quan hệ, sử dụng chỉ mục B-tree phân cụm để định vị bộ cần xóa. Trong truy vấn đầu tiên không có chỉ mục nào tồn tại và do đó không cần cập nhật chỉ mục nào, trong khi ở truy vấn thứ hai và thứ ba, một chỉ mục cần được cập nhật.

Các truy vấn thứ tư đến thứ sáu kiểm tra chi phí sửa đổi một bộ theo ba cách khác nhau. Trong cả ba phép thử, một chỉ mục không phân cụm tồn tại trên thuộc tính unique2, và ngoài ra, một chỉ mục phân cụm tồn tại trên thuộc tính Unique1. Trong trường hợp đầu tiên, thuộc tính được sửa đổi là thuộc tính phân vùng, do đó yêu cầu bộ được sửa đổi phải được định vị lại. Hơn nữa, vì bộ được định vị lại, chỉ mục thứ cấp cũng phải được cập nhật. Truy vấn sửa đổi thứ hai sửa đổi một thuộc tính không phân vùng, không có chỉ mục. Truy vấn sửa đổi thứ ba sửa đổi một thuộc tính trên đó một chỉ mục không phân cụm đã được xây dựng, sử dụng chỉ mục để định vị bộ cần sửa đổi.

Bảng 6 - Các truy vấn cập nhật  
30 Bộ xử lý Với Đĩa  
(Tất cả thời gian thực thi tính bằng giây)

|  | Số lượng bộ trong quan hệ nguồn |  |  |
| --- | --- | --- | --- |
|  | 100,000 | 1,000,000 | 10,000,000 |
| Thêm 1 bộ (Không tồn tại chỉ mục) | 0.07 | 0.08 | 0.10 |
| Thêm 1 bộ (Một chỉ mục tồn tại) | 0.18 | 0.21 | 0.22 |
| Xóa 1 bộ | 0.34 | 0.28 | 0.49 |
| Sửa đổi 1 bộ (#1) | 0.72 | 0.73 | 0.93 |
| Sửa đổi 1 bộ (#2) | 0.18 | 0.20 | 0.24 |
| Sửa đổi 1 bộ (#3) | 0.33 | 0.38 | 0.52 |
