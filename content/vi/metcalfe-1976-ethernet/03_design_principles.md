---
paper: metcalfe-1976-ethernet
title: 'Ethernet: Distributed Packet Switching for Local Computer Networks'
authors:
  - Robert M. Metcalfe
  - David R. Boggs
year: 1976
venue: Communications of the ACM
field: networks
section: "3"
section_title: Nguyên tắc thiết kế
tag: "0299"
kind: section
lang: vi
source: https://www.cl.cam.ac.uk/teaching/0809/DigiCommI/metcalfe1976ethernet.pdf
pdf_sha256: e1e9d67146a1d0955a39b4fbb8e2951d6cefb4f7231a01acb9c78852280da227
pdf_pages: 2-5
extraction: vision
extraction_model: gpt-5
content_sha256: bdd0097353d1320f98a81c851d161e2b439406dec7f31e4b1e543c100edac704
translated_from: content/en/metcalfe-1976-ethernet/03_design_principles.md
source_content_sha256: 5c46f0829ca49c7e51865bacfb02e1365b313f99c5c12f3278cc64d7f41a76ef
translation_model: gpt-5
translation_run: 20260917T145710Z
glossary_version: 6
glossary_terms_sha256: 3a5b9dd3cd6211761c92d70db4c4910c364b1cae9e5e732eea77349f449c860b
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Mục tiêu của chúng tôi là thiết kế một hệ thống truyền thông có thể phát triển một cách trơn tru để đáp ứng một số tòa nhà đầy các máy tính cá nhân và các phương tiện cần thiết cho việc hỗ trợ chúng.

Giống như các trạm tính toán được kết nối, hệ thống truyền thông phải có chi phí thấp. Chúng tôi chọn phân phối quyền điều khiển của phương tiện truyền thông giữa các máy tính đang giao tiếp để loại bỏ các vấn đề về độ tin cậy của bộ điều khiển trung tâm chủ động, tránh tạo ra nút thắt trong một hệ thống giàu tính song song, và giảm các chi phí cố định khiến các hệ thống nhỏ trở nên không kinh tế.

Thiết kế Ethernet bắt đầu với ý tưởng cơ bản về va chạm gói tin và truyền lại được phát triển trong Aloha Network [1]. Chúng tôi dự đoán rằng, giống như Aloha Network, các Ethernet sẽ mang lưu lượng dạng cụm, do đó kỹ thuật ghép kênh phân chia theo thời gian đồng bộ (STDM) thông thường sẽ không hiệu quả [1, 2, 21, 26]. Chúng tôi nhận thấy triển vọng trong cách tiếp cận Aloha đối với việc điều khiển phân tán việc ghép kênh kênh vô tuyến và hy vọng rằng nó có thể được áp dụng hiệu quả với các môi trường phù hợp cho truyền thông máy tính cục bộ. Với một số cải tiến của riêng mình, triển vọng đó đã được hiện thực hóa.

Ethernet được đặt tên theo *luminiferous ether* trong lịch sử, môi trường mà các bức xạ điện từ từng được cho là lan truyền qua đó. Giống như một bộ phát vô tuyến Aloha, một bộ phát Ethernet phát quảng bá các chuỗi bit được đồng bộ với bộ phát và được định địa chỉ hoàn toàn, gọi là các gói tin, lên Ether và hy vọng rằng chúng được các bộ nhận đích nghe thấy. Ether là một môi trường thụ động về mặt logic để lan truyền tín hiệu số và có thể được xây dựng bằng bất kỳ số lượng môi trường nào bao gồm cáp đồng trục, cặp dây xoắn và sợi quang.

Hình 1. Một Ethernet hai phân đoạn. {#metcalfe-1976-ethernet-fig-1 .figure tag=029A}

### 3.1 Tôpô {#metcalfe-1976-ethernet-s3-1 .section tag=029B}

Chúng tôi không thể chi trả cho các kết nối dư thừa và định tuyến động của chuyển mạch gói lưu trữ-và-chuyển tiếp để đảm bảo truyền thông tin cậy, vì vậy chúng tôi chọn đạt được độ tin cậy thông qua sự đơn giản. Chúng tôi chọn làm cho phương tiện truyền thông dùng chung trở nên thụ động để sự cố của một phần tử chủ động chỉ có xu hướng ảnh hưởng đến truyền thông của một trạm duy nhất. Bố trí và các nhu cầu thay đổi của các tòa nhà văn phòng và phòng thí nghiệm dẫn chúng tôi đến việc chọn một tôpô mạng có tiềm năng mở rộng gia tăng và cấu hình lại thuận tiện với sự gián đoạn dịch vụ tối thiểu.

Tôpô của Ethernet là một cây không có gốc. Nó là một *tree* để Ether có thể phân nhánh tại lối vào hành lang của một tòa nhà, đồng thời tránh nhiễu đa đường. Chỉ được phép có một đường đi qua Ether giữa bất kỳ nguồn và đích nào; nếu tồn tại nhiều hơn một đường đi, một *transmission* sẽ gây nhiễu với chính nó, liên tục đến đích dự kiến sau khi đã đi qua các đường có độ dài khác nhau. Ether là *unrooted* vì nó có thể được mở rộng từ bất kỳ điểm nào của nó theo bất kỳ hướng nào. Bất kỳ trạm nào muốn tham gia một Ethernet đều kết nối vào Ether tại điểm thuận tiện gần nhất.

Xem xét mối quan hệ giữa liên kết và điều khiển, chúng tôi thấy rằng Ethernet là đối ngẫu của một mạng hình sao. Thay vì liên kết *distributed* thông qua nhiều liên kết riêng biệt và điều khiển *central* trong một nút chuyển mạch, như trong mạng hình sao, Ethernet có liên kết *central* thông qua Ether và điều khiển *distributed* giữa các trạm của nó.

Khác với Aloha Network, vốn là một mạng hình sao với một kênh quảng bá đi ra và một kênh đa truy nhập đi vào, Ethernet hỗ trợ truyền thông nhiều-đến-nhiều với một kênh đa truy nhập quảng bá duy nhất.

### 3.2 Điều khiển {#metcalfe-1976-ethernet-s3-2 .section tag=029C}

Việc chia sẻ Ether được điều khiển theo cách sao cho không chỉ có khả năng mà còn có xác suất cao rằng hai hoặc nhiều trạm sẽ cố gắng truyền một gói tin vào gần cùng một thời điểm. Các gói tin chồng lấp theo thời gian trên Ether được gọi là *collide*; chúng gây nhiễu đến mức không thể được bộ nhận nhận dạng. Một trạm phục hồi từ va chạm được phát hiện bằng cách từ bỏ lần thử đó và truyền lại gói tin sau một khoảng thời gian ngẫu nhiên được chọn động. Việc phân xử các yêu cầu truyền xung đột vừa được phân tán vừa mang tính thống kê.

Khi Ether phần lớn không được sử dụng, một trạm truyền các gói tin của nó tùy ý, các gói tin được nhận không có lỗi, và mọi thứ đều ổn. Khi nhiều trạm bắt đầu truyền hơn, tốc độ nhiễu gói tin tăng lên. Các bộ điều khiển Ethernet trong mỗi trạm được xây dựng để điều chỉnh khoảng thời gian truyền lại trung bình tỷ lệ với tần suất collisons; việc chia sẻ Ether giữa các truyền trạm-trạm cạnh tranh nhờ đó được giữ gần mức tối ưu [20, 21].

Cần có một mức độ hợp tác nhất định giữa các trạm để chia sẻ Ether một cách công bằng. Trong các ứng dụng yêu cầu cao, một số trạm có thể hữu ích khi giành quyền ưu tiên truyền thông qua một số vi phạm có hệ thống đối với các quy tắc công bằng. Một trạm có thể chiếm dụng Ether bằng cách không điều chỉnh khoảng thời gian truyền lại khi lưu lượng tăng hoặc bằng cách gửi các gói tin rất lớn. Cả hai thực hành này hiện đều bị cấm bởi phần mềm mức thấp trong mỗi trạm.

### 3.3 Định địa chỉ {#metcalfe-1976-ethernet-s3-3 .section tag=029D}

Mỗi gói tin có một nguồn và một đích, cả hai đều được xác định trong phần đầu của gói tin. Một gói tin được đặt lên Ether cuối cùng sẽ lan truyền đến tất cả các trạm. Bất kỳ trạm nào cũng có thể sao chép một gói tin từ Ether vào bộ nhớ cục bộ của nó, nhưng thông thường chỉ một trạm đích chủ động khớp địa chỉ của nó trong phần đầu của gói tin mới thực hiện việc đó khi gói tin đi qua. Theo quy ước, một địa chỉ đích bằng không là một ký tự đại diện và khớp với mọi địa chỉ; một gói tin có đích bằng không được gọi là một *broadcast packet*.

### 3.4 Độ tin cậy {#metcalfe-1976-ethernet-s3-4 .section tag=029E}

Một Ethernet có tính xác suất. Các gói tin có thể bị mất do nhiễu với các gói tin khác, nhiễu xung trên

Communications
of
eth ACM
July 1976
Volume 19

Ether, một bộ thu không hoạt động tại đích đến dự kiến của một gói tin, hoặc sự loại bỏ có chủ đích. Các giao thức được sử dụng để giao tiếp thông qua một Ethernet phải giả định rằng các gói tin sẽ chỉ được nhận đúng tại các đích đến dự kiến *với xác suất cao.*

Một Ethernet thực hiện những nỗ lực tốt nhất để truyền các gói tin thành công, nhưng trách nhiệm của các tiến trình trong các trạm nguồn và trạm đích là thực hiện các biện pháp phòng ngừa cần thiết để bảo đảm giao tiếp tin cậy với chất lượng mà chính chúng mong muốn [18, 21]. Nhận thức được chi phí và nguy cơ của việc hứa hẹn giao tiếp “không có lỗi”, chúng tôi không bảo đảm việc phân phối tin cậy của bất kỳ gói tin đơn lẻ nào để đạt được cả tính kinh tế của truyền tải và độ tin cậy cao được tính trung bình trên nhiều gói tin [21]. Việc loại bỏ trách nhiệm về giao tiếp tin cậy khỏi cơ chế vận chuyển gói tin cho phép chúng tôi điều chỉnh độ tin cậy theo ứng dụng và đặt việc khôi phục lỗi vào nơi nó mang lại hiệu quả cao nhất. Chính sách này trở nên quan trọng hơn khi các Ethernet được kết nối với nhau theo một hệ thống phân cấp các mạng mà qua đó các gói tin phải di chuyển xa hơn và chịu nhiều rủi ro hơn.

### 3.5 Cơ chế {#metcalfe-1976-ethernet-s3-5 .section tag=029F}

Một trạm kết nối với Ether bằng một *tap* và một *transceiver*. Một tap là một thiết bị để kết nối vật lý với Ether trong khi gây nhiễu đến các đặc tính truyền dẫn của nó ít nhất có thể. Thiết kế của transceiver phải là một bài tập về sự cảnh giác cực độ. Phải thực hiện các biện pháp phòng ngừa để các sự cố có khả năng xảy ra trong transceiver hoặc trạm không dẫn đến việc làm ô nhiễm Ether. Cụ thể, việc ngắt nguồn của transceiver phải khiến nó ngắt kết nối khỏi Ether.

Năm cơ chế được cung cấp trong Ethernet thử nghiệm của chúng tôi để giảm xác suất và chi phí mất một gói tin. Các cơ chế này là (1) phát hiện sóng mang, (2) phát hiện nhiễu, (3) phát hiện lỗi gói tin, (4) lọc gói tin bị cắt ngắn, và (5) cưỡng chế đồng thuận va chạm.

### 3.5.1 Phát hiện sóng mang. {#metcalfe-1976-ethernet-s3-5-1 .section tag=02A0}

Khi các bit của một gói tin được một trạm đặt lên Ether, chúng được mã hóa theo pha (giống như các bit trên băng từ), điều này bảo đảm rằng có ít nhất một chuyển tiếp trên Ether trong mỗi thời gian bit. Do đó, việc một gói tin đi qua Ether có thể được phát hiện bằng cách lắng nghe các chuyển tiếp của nó. Sử dụng phép tương tự với radio, chúng tôi nói về sự hiện diện của *carrier* khi một gói tin đi qua một transceiver. Vì một trạm có thể cảm nhận sóng mang của một gói tin đang đi qua, nó có thể trì hoãn việc gửi một gói tin của chính nó cho đến khi gói tin được phát hiện đi qua an toàn. Aloha Network không có phát hiện sóng mang và do đó chịu tỷ lệ va chạm cao hơn đáng kể. Không có phát hiện sóng mang, việc sử dụng Ether hiệu quả sẽ giảm khi độ dài gói tin tăng. Trong Section 6 dưới đây, chúng tôi chỉ ra rằng với phát hiện sóng mang, hiệu quả của Ether tăng khi độ dài gói tin tăng.

Với phát hiện sóng mang, chúng tôi có thể triển khai *deference*: không trạm nào sẽ bắt đầu truyền khi đang nghe thấy sóng mang. Cùng với deference là *acquisition*: một khi việc truyền một gói tin đã diễn ra trong khoảng thời gian lan truyền đầu-cuối của Ether, tất cả các trạm đều đang nghe thấy sóng mang và đang trì hoãn; Ether đã được chiếm quyền và quá trình truyền sẽ hoàn tất mà không có va chạm gây nhiễu.

Với phát hiện sóng mang, các va chạm chỉ nên xảy ra khi hai hoặc nhiều trạm nhận thấy Ether im lặng và bắt đầu truyền đồng thời: trong khoảng thời gian lan truyền đầu-cuối của Ether. Điều này hầu như luôn xảy ra ngay sau một lần truyền gói tin mà trong đó hai hoặc nhiều trạm đã trì hoãn. Vì các trạm hiện không ngẫu nhiên hóa sau khi trì hoãn, khi quá trình truyền kết thúc, các trạm đang chờ cùng dồn lên, va chạm, ngẫu nhiên hóa và truyền lại.

### 3.5.2 Phát hiện nhiễu. {#metcalfe-1976-ethernet-s3-5-2 .section tag=02A1}

Mỗi transceiver có một bộ phát hiện nhiễu. Nhiễu được biểu thị khi transceiver nhận thấy sự khác biệt giữa giá trị của bit mà nó đang nhận từ Ether và giá trị của bit mà nó đang cố truyền.

Phát hiện nhiễu có ba ưu điểm. Thứ nhất, một trạm phát hiện va chạm biết rằng gói tin của nó đã bị hỏng. Gói tin có thể được lập lịch để truyền lại ngay lập tức, tránh thời gian chờ xác nhận dài. Thứ hai, các khoảng thời gian nhiễu trên Ether bị giới hạn tối đa ở một thời gian khứ hồi. Các gói tin va chạm trong Aloha Network chạy đến hoàn tất, nhưng các gói tin bị cắt ngắn do các va chạm Ethernet chỉ lãng phí một phần nhỏ thời gian gói tin trên Ether. Thứ ba, tần suất nhiễu được phát hiện được sử dụng để ước lượng lưu lượng Ether nhằm điều chỉnh các khoảng thời gian truyền lại và tối ưu hóa hiệu quả kênh.

### 3.5.3 Phát hiện lỗi gói tin. {#metcalfe-1976-ethernet-s3-5-3 .section tag=02A2}

Khi một gói tin được đặt lên Ether, một checksum được tính toán và nối thêm. Khi gói tin được đọc từ Ether, checksum được tính toán lại. Các gói tin không mang theo một checksum nhất quán sẽ bị loại bỏ. Theo cách này, các lỗi truyền tải, lỗi do nhiễu xung, và các lỗi do nhiễu không được phát hiện được bắt giữ tại đích đến của một gói tin.

### 3.5.4 Lọc gói tin bị cắt ngắn. {#metcalfe-1976-ethernet-s3-5-4 .section tag=02A3}

Phát hiện nhiễu và deference khiến hầu hết các va chạm dẫn đến các *truncated packets* chỉ có một vài bit; các trạm va chạm phát hiện nhiễu và hủy việc truyền trong thời gian khứ hồi của Ether. Để giảm tải xử lý mà việc từ chối các gói tin bị hỏng rõ ràng như vậy đặt lên phần mềm của các trạm lắng nghe, các gói tin bị cắt ngắn được lọc bằng phần cứng.

### 3.5.5 Thực thi đồng thuận va chạm. {#metcalfe-1976-ethernet-s3-5-5 .section tag=02A4}

Khi một trạm xác định rằng việc truyền của nó đang chịu nhiễu, nó tạm thời gây nhiễu Ether để đảm bảo rằng tất cả các bên tham gia khác trong vụ va chạm sẽ phát hiện nhiễu, và, do sự nhường quyền, sẽ bị buộc phải hủy bỏ. Nếu không có cơ chế *thực thi đồng thuận va chạm* này, có khả năng trạm truyền mà trong trường hợp khác sẽ là trạm cuối cùng phát hiện một vụ va chạm có thể không phát hiện được điều đó khi các quá trình truyền gây nhiễu khác lần lượt hủy bỏ và ngừng gây nhiễu. Mặc dù gói tin có thể trông hợp lệ đối với bộ phát cuối cùng đó, các độ dài đường truyền khác nhau

Communications  
of the ACM

July 1976  
Volume 19 giữa các bộ phát đang va chạm và bộ nhận dự định sẽ khiến gói tin đến nơi bị hỏng.
