---
paper: bosshart-2014-p4
title: 'P4: Programming Protocol-Independent Packet Processors'
authors:
  - Pat Bosshart
  - Dan Daly
  - Glen Gibb
  - Martin Izzard
  - Nick McKeown
  - Jennifer Rexford
  - Cole Schlesinger
  - Dan Talayco
  - Amin Vahdat
  - George Varghese
  - David Walker
year: 2014
venue: ACM SIGCOMM Computer Communication Review
field: networks
section: "5"
section_title: BIÊN DỊCH MỘT CHƯƠNG TRÌNH P4
tag: "0099"
kind: section
lang: vi
source: arxiv:1312.1719
pdf_sha256: 2bb0ccb7b5410868efdecc9ef5208d235c6f3aa75dee84aa992751aed117a42f
pdf_pages: 6-7
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: f16c5c0e153cda3f53949e8c0ff73eb2f5f909a5fe5d22a52384251414734109
translated_from: content/en/bosshart-2014-p4/05_compiled_a_p4_program.md
source_content_sha256: e046a2c6e449cf6ed2859fb8364a2597a86453bb726a088c6be79fd0f8dbbe19
translation_model: gpt-5
translation_run: 20260914T163737Z
glossary_version: 6
glossary_terms_sha256: 3a5b9dd3cd6211761c92d70db4c4910c364b1cae9e5e732eea77349f449c860b
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Để một mạng triển khai chương trình P4 của chúng tôi, cần có một trình biên dịch để ánh xạ mô tả độc lập với mục tiêu lên nền tảng phần cứng hoặc phần mềm cụ thể của chuyển mạch mục tiêu. Việc này bao gồm cấp phát các tài nguyên của mục tiêu và tạo cấu hình thích hợp cho thiết bị.

### 5.1 Biên dịch các bộ phân tích cú pháp gói tin {#bosshart-2014-p4-s5-1 .section tag=009A}

Đối với các thiết bị có bộ phân tích cú pháp có thể lập trình, trình biên dịch dịch mô tả bộ phân tích cú pháp thành một máy trạng thái phân tích cú pháp, trong khi đối với các bộ phân tích cú pháp cố định, trình biên dịch chỉ xác minh rằng mô tả bộ phân tích cú pháp nhất quán với bộ phân tích cú pháp của mục tiêu. Chi tiết về việc tạo máy trạng thái và các mục nhập bảng trạng thái có thể được tìm thấy trong [16].

Table 2 hiển thị các mục nhập bảng trạng thái cho các phần vlan và mTag của bộ phân tích cú pháp (§4.3). Mỗi mục nhập chỉ định trạng thái hiện tại, giá trị trường cần so khớp và trạng thái tiếp theo. Các cột khác được bỏ qua để ngắn gọn.

| Trạng thái hiện tại | Giá trị tra cứu | Trạng thái tiếp theo |
| --- | --- | --- |
| vlan | 0xaaaa | mTag |
| vlan | 0x800 | ipv4 |
| vlan | * | stop |
| mTag | 0x800 | ipv4 |
| mTag | * | stop |

Table 2: Các mục nhập bảng trạng thái của bộ phân tích cú pháp cho ví dụ mTag. {#bosshart-2014-p4-tab-2 .table tag=009B}

### 5.2 Biên dịch các chương trình điều khiển {#bosshart-2014-p4-s5-2 .section tag=009C}

Biểu diễn luồng điều khiển bắt buộc trong §4.6 là một cách thuận tiện để đặc tả hành vi chuyển tiếp logic của một chuyển mạch, nhưng không chỉ rõ các phụ thuộc giữa các bảng hoặc các cơ hội cho tính đồng thời. Do đó, chúng tôi sử dụng một trình biên dịch để phân tích chương trình điều khiển nhằm xác định các phụ thuộc và tìm kiếm các cơ hội xử lý các trường phần đầu song song. Cuối cùng, trình biên dịch tạo cấu hình mục tiêu cho chuyển mạch. Có nhiều mục tiêu tiềm năng: ví dụ, một chuyển mạch phần mềm [17], một chuyển mạch phần mềm đa lõi [18], một NPU [19], một chuyển mạch chức năng cố định [20], hoặc một đường ống bảng so khớp có thể cấu hình lại (RMT) [2].

Như đã thảo luận trong §3, trình biên dịch tuân theo một quy trình biên dịch hai giai đoạn. Đầu tiên, nó chuyển đổi chương trình điều khiển P4 thành một biểu diễn đồ thị phụ thuộc bảng trung gian, sau đó phân tích biểu diễn này để xác định các phụ thuộc giữa các bảng. Một phần cuối dành riêng cho mục tiêu sau đó ánh xạ đồ thị này lên các tài nguyên cụ thể của chuyển mạch.

Chúng tôi xem xét ngắn gọn cách ví dụ mTag sẽ được triển khai trong các loại chuyển mạch khác nhau:

Chuyển mạch phần mềm: Một chuyển mạch phần mềm cung cấp tính linh hoạt hoàn toàn: số lượng bảng, cấu hình bảng và phân tích cú pháp đều nằm dưới sự điều khiển của phần mềm. Trình biên dịch ánh xạ trực tiếp đồ thị bảng mTag tới các bảng chuyển mạch. Trình biên dịch sử dụng thông tin kiểu bảng để giới hạn độ rộng, chiều cao bảng và tiêu chí so khớp (ví dụ: chính xác, tiền tố hoặc ký tự đại diện) của mỗi bảng. Trình biên dịch cũng có thể tối ưu hóa so khớp tam phân hoặc so khớp tiền tố bằng các cấu trúc dữ liệu phần mềm.

Các chuyển mạch phần cứng với RAM và TCAM: Một trình biên dịch có thể cấu hình băm để thực hiện so khớp chính xác hiệu quả bằng RAM cho mTag_table trong các chuyển mạch biên. Ngược lại, bảng chuyển tiếp mTag lõi so khớp trên một tập con các bit thẻ sẽ được ánh xạ tới TCAM.

Các chuyển mạch hỗ trợ các bảng song song: Trình biên dịch có thể phát hiện các phụ thuộc dữ liệu và sắp xếp các bảng song song hoặc nối tiếp. Trong ví dụ mTag, các bảng local_switching và mTag_table có thể thực thi song song cho đến khi thực thi hành động thiết lập một mTag.

Các chuyển mạch áp dụng hành động ở cuối đường ống: Đối với các chuyển mạch chỉ xử lý hành động ở cuối một đường ống, trình biên dịch có thể yêu cầu các giai đoạn trung gian tạo metadata được sử dụng để thực hiện các ghi cuối cùng. Trong ví dụ mTag, việc mTag được thêm vào hay loại bỏ có thể được biểu diễn trong metadata.

Các chuyển mạch có ít bảng: Trình biên dịch có thể ánh xạ một số lượng lớn các bảng P4 tới một số lượng nhỏ hơn các bảng vật lý. Trong ví dụ mTag, chuyển mạch cục bộ có thể được kết hợp với bảng mTag. Khi bộ điều khiển cài đặt các quy tắc mới trong thời gian chạy, bộ dịch quy tắc của trình biên dịch có thể “compose” các quy tắc trong hai bảng P4 để tạo ra các quy tắc cho một bảng vật lý duy nhất.
