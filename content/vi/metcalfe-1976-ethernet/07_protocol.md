---
paper: metcalfe-1976-ethernet
title: 'Ethernet: Distributed Packet Switching for Local Computer Networks'
authors:
  - Robert M. Metcalfe
  - David R. Boggs
year: 1976
venue: Communications of the ACM
field: networks
section: "7"
section_title: Giao thức
tag: 02B4
kind: section
lang: vi
source: https://www.cl.cam.ac.uk/teaching/0809/DigiCommI/metcalfe1976ethernet.pdf
pdf_sha256: e1e9d67146a1d0955a39b4fbb8e2951d6cefb4f7231a01acb9c78852280da227
pdf_pages: 8-9
extraction: vision
extraction_model: gpt-5
content_sha256: 879a67c43ab3275d784e465167274d7d18f5ec5cd597c00f120029c11c093668
translated_from: content/en/metcalfe-1976-ethernet/07_protocol.md
source_content_sha256: e91e91190dc8078b9071e78d4984320c8e5a3414468313325dd4880b00ad81ff
translation_model: gpt-5
translation_run: 20260918T053014Z
glossary_version: 6
glossary_terms_sha256: 3a5b9dd3cd6211761c92d70db4c4910c364b1cae9e5e732eea77349f449c860b
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Việc xây dựng một hệ thống truyền thông gói tin khả dụng không chỉ đơn giản là cung cấp các cơ chế vận chuyển gói tin. Các phương pháp sửa lỗi, điều khiển luồng, đặt tên tiến trình, bảo mật và kế toán cũng phải được cung cấp thông qua các giao thức cấp cao hơn được triển khai trên giao thức điều khiển Ether được mô tả trong các Mục 3 và 4 ở trên. [[cerf-1974-tcpip]], [10], [12], [21], [28], [34]. Điều khiển Ether bao gồm đóng khung gói tin, phát hiện lỗi, định địa chỉ và điều khiển đa truy nhập; giống như các thủ tục điều khiển đường truyền khác, Ethernet được sử dụng để hỗ trợ nhiều kiến trúc mạng và đa bộ xử lý [30, 31].

Sau đây là mô tả ngắn gọn về một giao thức gói tin điều khiển lỗi đơn giản. EFTP (Ethernet File Transfer Protocol) đáng được quan tâm vì nó tương đối dễ hiểu và triển khai đúng, đồng thời nó đã chuyên cần vận chuyển nhiều file có giá trị trong quá trình phát triển các giao thức tổng quát và hiệu quả hơn.

### 7.1. Thuật ngữ chung {#metcalfe-1976-ethernet-s7-1 .section tag=02B5}

Khi thảo luận về các giao thức gói tin, chúng tôi sử dụng các thuật ngữ hữu ích nói chung sau đây. Một gói tin được nói là có một *nguồn* và một *đích*. Một luồng dữ liệu được nói là có một *bên gửi* và một *bên nhận*, với nhận thức rằng để hỗ trợ một luồng dữ liệu, một số gói tin (thường là các gói xác nhận) sẽ có nguồn tại bên nhận và đích đến là bên gửi. Một kết nối được nói là có một *bộ lắng nghe* và một *bộ khởi tạo*, còn một dịch vụ được nói là có một *server* và một *người dùng*. Việc xem chúng như các mô tả trực giao về những bên tham gia giao tiếp là rất hữu ích. Tất nhiên, một server thường là một bộ lắng nghe và nguồn của các gói tin mang dữ liệu thường là bên gửi.

### 7.2 EFTP {#metcalfe-1976-ethernet-s7-2 .section tag=02B6}

16 bit đầu tiên của mọi gói tin Ethernet chứa các địa chỉ trạm đích và nguồn có thể được giao diện diễn giải, mỗi địa chỉ một byte, theo thứ tự đó (xem Hình 2). Theo quy ước phần mềm, 16 bit thứ hai của mọi gói tin Ethernet chứa kiểu gói tin. Các giao thức khác nhau sử dụng các tập kiểu gói tin rời nhau. EFTP sử dụng 5 kiểu gói tin: data, ack, abort, end và endreply. Theo sau từ kiểu 16 bit của một gói tin EFTP là 16 bit số thứ tự, 16 bit độ dài, tùy chọn một số từ dữ liệu 16 bit, và cuối cùng là một từ kiểm tra tổng phần mềm 16 bit (xem Hình 4). Kiểm tra tổng phần cứng của Ethernet chỉ hiện diện trên Ether và không được tính ở mức giao thức này.

Rõ ràng là rất ít sự cẩn trọng đã được dành cho việc ép một số trường nhất định vào đúng số bit thích hợp. Trọng tâm ở đây là tính đơn giản và sự dễ dàng trong lập trình. Mặc dù có lời miễn trừ này, chúng tôi cho rằng nên thiên về các trường rộng rãi; dù cố gắng đến đâu, một trường nào đó cuối cùng cũng sẽ hóa ra quá nhỏ.

Từ kiểm tra tổng phần mềm được sử dụng để giảm xác suất xảy ra lỗi không được phát hiện. Nó không chỉ đóng vai trò dự phòng cho kiểm tra tổng dư thừa tuần hoàn 16 bit phần cứng nối tiếp của Ethernet thử nghiệm (trong Hình 2), mà còn bảo vệ chống lại các sự cố trong các đường dẫn dữ liệu song song bên trong các trạm, vốn không được CRC kiểm tra. Kiểm tra tổng được EFTP sử dụng là phép cộng bù 1 và xoay vòng trên toàn bộ gói tin, bao gồm phần đầu và dữ liệu nội dung. Việc bỏ qua kiểm tra tổng ở bất kỳ đầu nào sẽ khiến người dùng phải chịu rủi ro; bên gửi có thể đặt toàn bộ các bit 1 (một giá trị không thể xảy ra) vào từ kiểm tra tổng để báo cho bên nhận rằng không có kiểm tra tổng nào được tính.

### 7.2.1 Truyền dữ liệu. {#metcalfe-1976-ethernet-s7-2-1 .section tag=02B7}

Các từ 16 bit của một file được truyền từ trạm gửi đến trạm nhận trong các gói dữ liệu được đánh số liên tiếp bắt đầu từ 0. Mỗi gói dữ liệu được bên gửi truyền lại định kỳ cho đến khi một gói ack có số thứ tự tương ứng được bên nhận trả về. Bên nhận bỏ qua mọi gói tin bị hỏng, các gói tin từ một trạm khác với bên gửi, và các gói tin có số thứ tự không khớp với số thứ tự được mong đợi hoặc số đứng ngay trước nó. Khi một gói tin có số thứ tự được mong đợi, gói tin đó được xác nhận, dữ liệu của nó được chấp nhận như một phần của file, và số thứ tự được tăng lên. Khi một gói tin đến với số thứ tự nhỏ hơn số được mong đợi một đơn vị, nó được xác nhận và loại bỏ; giả định là ack của nó đã bị mất và cần được truyền lại [21].

### 7.2.2 Kết thúc. {#metcalfe-1976-ethernet-s7-2-2 .section tag=02B8}

Khi toàn bộ dữ liệu đã được truyền, một gói end được gửi với số thứ tự liên tiếp tiếp theo và sau đó bên gửi chờ một end-reply tương ứng. Sau khi chấp nhận một gói end theo đúng thứ tự, bên nhận dữ liệu trả lời bằng một endreply tương ứng rồi chờ trong một khoảng thời gian tương đối dài (10 giây). Khi nhận được endreply, trạm gửi truyền một endreply lặp lại và được tự do kết thúc với sự bảo đảm rằng file đã được truyền thành công. Bên nhận đang chờ sau đó nhận được end-reply được lặp lại và cũng kết thúc với sự bảo đảm tương tự.

Bảng I. Hiệu suất Ethernet.

| $Q$ | $P = 4096$ | $P = 1024$ | $P = 512$ | $P = 48$ |
|---:|---:|---:|---:|---:|
| 1 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| 2 | 0.9884 | 0.9552 | 0.9143 | 0.5000 |
| 3 | 0.9857 | 0.9447 | 0.8951 | 0.4444 |
| 4 | 0.9842 | 0.9396 | 0.8862 | 0.4219 |
| 5 | 0.9834 | 0.9367 | 0.8810 | 0.4096 |
| 10 | 0.9818 | 0.9310 | 0.8709 | 0.3874 |
| 32 | 0.9807 | 0.9272 | 0.8642 | 0.3737 |
| 64 | 0.9805 | 0.9263 | 0.8627 | 0.3708 |
| 128 | 0.9804 | 0.9259 | 0.8620 | 0.3693 |
| 256 | 0.9803 | 0.9257 | 0.8616 | 0.3686 |

Communications  
of  
the ACM

July 1976  
Volume 19

Hình 4. Bố trí gói tin EFTP. {#metcalfe-1976-ethernet-fig-4 .figure tag=02B9}

Chuỗi end-dally tương đối phức tạp nhằm làm cho bên gửi và bên nhận một file gần như chắc chắn sẽ thống nhất với nhau về việc file đã được truyền đúng hay chưa. Nếu gói tin kết thúc bị mất, bên gửi dữ liệu chỉ cần truyền lại nó như đối với bất kỳ gói tin nào có xác nhận quá hạn. Nếu endreply từ bên nhận dữ liệu bị mất, bên gửi dữ liệu sẽ hết thời gian chờ theo cùng một cách và truyền lại gói tin kết thúc, đến lượt nó sẽ được bên nhận dally xác nhận. Nếu endreply được phản hồi bị mất, bên nhận dally sẽ gặp bất tiện vì phải chờ nó, nhưng khi đã hết thời gian chờ, bên nhận vẫn có thể chắc chắn rằng việc truyền file đã thành công vì gói tin kết thúc đã được nhận.

Vào bất kỳ thời điểm nào trong toàn bộ quá trình này, mỗi bên đều có quyền quyết định rằng việc liên lạc đã thất bại và đơn giản là từ bỏ; việc gửi một gói tin abort để kết thúc liên lạc nhanh chóng được xem là lịch sự trong trường hợp, chẳng hạn, abort do người dùng khởi tạo hoặc lỗi hệ thống file.

### 7.2.3 Những thiếu sót của EFTP. {#metcalfe-1976-ethernet-s7-2-3 .section tag=02BA}

EFTP đã rất hữu ích, nhưng nó có nhiều thiếu sót. Thứ nhất, giao thức chỉ hỗ trợ truyền file từ trạm này sang trạm khác trong một mạng duy nhất và đặc biệt không hỗ trợ truyền từ tiến trình này sang tiến trình khác bên trong các trạm, dù trên cùng mạng hay thông qua một gateway. Thứ hai, rendezvous giữa các tiến trình ở dạng suy biến vì không có cơ chế tìm các tiến trình theo tên hoặc xử lý thuận tiện nhiều người dùng bởi một server duy nhất. Thứ ba, không có kiểm soát luồng thực sự. Nếu dữ liệu đến một bên nhận không thể tiếp nhận dữ liệu vào các bộ đệm của mình, dữ liệu đơn giản có thể bị loại bỏ với sự đảm bảo hoàn toàn rằng cuối cùng nó sẽ được truyền lại. Không có cách nào để bên nhận làm ngừng luồng của những lần truyền lãng phí như vậy hoặc đẩy nhanh việc truyền lại. Thứ tư, dữ liệu được truyền theo số nguyên các từ 16-bit thuộc về những file không có tên và do đó EFTP hoặc là quá hạn chế hoặc đòi hỏi một số định dạng truyền file lồng nhau nằm bên trong các từ dữ liệu của nó. Và thứ năm, tính tổng quát về chức năng bị mất vì bên nhận đồng thời là listener và server.
