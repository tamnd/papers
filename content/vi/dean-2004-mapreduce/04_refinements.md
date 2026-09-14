---
paper: dean-2004-mapreduce
title: 'MapReduce: Simplified Data Processing on Large Clusters'
authors:
  - Jeffrey Dean
  - Sanjay Ghemawat
year: 2004
venue: OSDI
field: systems
section: "4"
section_title: Các tinh chỉnh
tag: "0073"
kind: section
lang: vi
source: https://www.usenix.org/legacy/events/osdi04/tech/full_papers/dean/dean.pdf
pdf_sha256: 9cfef3ef1b8fe1a1b66c7221f56c2eeca0b15d6608ea68b0c85a38bfbffd8ce5
pdf_pages: 6-8
extraction: vision
extraction_model: gpt-5
content_sha256: e335ac42b558d148ce83d7e47da132eb94e28fd9e58d9fd0f9db3ee570e2b195
translated_from: content/en/dean-2004-mapreduce/04_refinements.md
source_content_sha256: cb5353b749d5b916e20595caf53cb7bfaa43a9e257e2b649bad9930652735060
translation_model: gpt-5
translation_run: 20260914T163737Z
glossary_version: 6
glossary_terms_sha256: afc6de5d010821f75553a129f8b55d5fbabc0d9d7af198021ca9a5a496de4088
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Mặc dù chức năng cơ bản được cung cấp chỉ bằng cách viết các hàm Map và Reduce là đủ cho hầu hết nhu cầu, chúng tôi đã nhận thấy một vài phần mở rộng hữu ích. Các phần mở rộng này được mô tả trong phần này.

### 4.1 Hàm phân vùng {#dean-2004-mapreduce-s4-1 .section tag=0074}

Người dùng MapReduce chỉ định số lượng tác vụ reduce/tệp đầu ra mà họ mong muốn ($R$). Dữ liệu được phân vùng trên các tác vụ này bằng cách sử dụng một hàm phân vùng trên khóa trung gian. Một hàm phân vùng mặc định được cung cấp, sử dụng phép băm (ví dụ: “hash(key) mod $R$”). Điều này thường tạo ra các phân vùng được cân bằng khá tốt. Tuy nhiên, trong một số trường hợp, việc phân vùng dữ liệu bằng một hàm khác của khóa là hữu ích. Ví dụ, đôi khi các khóa đầu ra là các URL, và chúng tôi muốn tất cả các mục nhập cho một host duy nhất kết thúc trong cùng một tệp đầu ra. Để hỗ trợ các tình huống như vậy, người dùng của thư viện MapReduce có thể cung cấp một hàm phân vùng đặc biệt. Ví dụ, sử dụng “hash(Hostname(urlkey)) mod $R$” làm hàm phân vùng khiến tất cả URL từ cùng một host kết thúc trong cùng một tệp đầu ra.

### 4.2 Các đảm bảo về thứ tự {#dean-2004-mapreduce-s4-2 .section tag=0075}

Chúng tôi đảm bảo rằng trong một phân vùng nhất định, các cặp khóa/giá trị trung gian được xử lý theo thứ tự khóa tăng dần. Đảm bảo về thứ tự này giúp dễ dàng tạo ra một tệp đầu ra đã sắp xếp cho mỗi phân vùng, điều này hữu ích khi định dạng tệp đầu ra cần hỗ trợ các thao tác tra cứu truy cập ngẫu nhiên hiệu quả theo khóa, hoặc người dùng của đầu ra thấy thuận tiện khi dữ liệu được sắp xếp.

### 4.3 Hàm Combiner {#dean-2004-mapreduce-s4-3 .section tag=0076}

Trong một số trường hợp, có sự lặp lại đáng kể trong các khóa trung gian được tạo ra bởi mỗi tác vụ map, và hàm Reduce do người dùng chỉ định có tính giao hoán và kết hợp. Một ví dụ điển hình là ví dụ đếm từ trong Section 2.1. Vì tần suất từ có xu hướng tuân theo phân phối Zipf, mỗi tác vụ map sẽ tạo ra hàng trăm hoặc hàng nghìn bản ghi có dạng . Tất cả các số đếm này sẽ được gửi qua mạng đến một tác vụ reduce duy nhất và sau đó được cộng lại bởi hàm Reduce để tạo ra một số. Chúng tôi cho phép người dùng chỉ định một hàm Combiner tùy chọn thực hiện việc gộp một phần dữ liệu này trước khi nó được gửi qua mạng.

Hàm Combiner được thực thi trên mỗi máy thực hiện một tác vụ map. Thông thường cùng một mã được sử dụng để triển khai cả hàm combiner và hàm reduce. Khác biệt duy nhất giữa một hàm reduce và một hàm combiner là cách thư viện MapReduce xử lý đầu ra của hàm. Đầu ra của một hàm reduce được ghi vào tệp đầu ra cuối cùng. Đầu ra của một hàm combiner được ghi vào một tệp trung gian sẽ được gửi đến một tác vụ reduce.

Việc kết hợp một phần giúp tăng tốc đáng kể một số lớp thao tác MapReduce. Appendix A chứa một ví dụ sử dụng một combiner.

### 4.4 Các kiểu đầu vào và đầu ra {#dean-2004-mapreduce-s4-4 .section tag=0077}

Thư viện MapReduce cung cấp hỗ trợ đọc dữ liệu đầu vào ở nhiều định dạng khác nhau. Ví dụ, đầu vào ở chế độ “text” xem mỗi dòng là một cặp khóa/giá trị: khóa là vị trí lệch trong tệp và giá trị là nội dung của dòng. Một định dạng được hỗ trợ phổ biến khác lưu trữ một chuỗi các cặp khóa/giá trị được sắp xếp theo khóa. Mỗi triển khai kiểu đầu vào biết cách chia chính nó thành các phạm vi có ý nghĩa để xử lý như các tác vụ map riêng biệt (ví dụ: việc chia phạm vi của chế độ text đảm bảo rằng các điểm chia phạm vi chỉ xảy ra tại ranh giới dòng). Người dùng có thể thêm hỗ trợ cho một kiểu đầu vào mới bằng cách cung cấp một triển khai của giao diện reader đơn giản, mặc dù hầu hết người dùng chỉ sử dụng một trong một số ít kiểu đầu vào được định nghĩa trước.

Một reader không nhất thiết cần cung cấp dữ liệu được đọc từ một tệp. Ví dụ, dễ dàng định nghĩa một reader đọc các bản ghi từ một cơ sở dữ liệu, hoặc từ các cấu trúc dữ liệu được ánh xạ trong bộ nhớ.

Theo cách tương tự, chúng tôi hỗ trợ một tập hợp các kiểu đầu ra để tạo dữ liệu ở các định dạng khác nhau và mã người dùng dễ dàng thêm hỗ trợ cho các kiểu đầu ra mới.

### 4.5  Side-effects {#dean-2004-mapreduce-s4-5 .section tag=0078}

Trong một số trường hợp, người dùng MapReduce nhận thấy thuận tiện khi tạo các tệp phụ như các đầu ra bổ sung từ các toán tử map và/hoặc reduce của họ. Chúng tôi dựa vào người viết ứng dụng để làm cho các side-effect như vậy có tính nguyên tử và idempotent. Thông thường ứng dụng ghi vào một tệp tạm thời và đổi tên nguyên tử tệp này sau khi nó đã được tạo hoàn chỉnh.

Chúng tôi không cung cấp hỗ trợ cho các commit hai pha nguyên tử của nhiều tệp đầu ra được tạo bởi một tác vụ duy nhất. Vì vậy, các tác vụ tạo ra nhiều tệp đầu ra với các yêu cầu về tính nhất quán giữa các tệp nên có tính xác định. Hạn chế này chưa từng là một vấn đề trong thực tế.

### 4.6 Bỏ qua các bản ghi lỗi {#dean-2004-mapreduce-s4-6 .section tag=0079}

Đôi khi có các lỗi trong mã người dùng khiến các hàm Map hoặc Reduce bị crash một cách xác định trên một số bản ghi nhất định. Các lỗi như vậy ngăn một thao tác MapReduce hoàn thành. Cách xử lý thông thường là sửa lỗi, nhưng đôi khi điều này không khả thi; có thể lỗi nằm trong một thư viện bên thứ ba mà mã nguồn không có sẵn. Ngoài ra, đôi khi việc bỏ qua một vài bản ghi là chấp nhận được, ví dụ khi thực hiện phân tích thống kê trên một tập dữ liệu lớn. Chúng tôi cung cấp một chế độ thực thi tùy chọn trong đó thư viện MapReduce phát hiện các bản ghi gây ra crash xác định và bỏ qua các bản ghi này để tiếp tục tiến trình.

Mỗi tiến trình worker cài đặt một bộ xử lý tín hiệu bắt các lỗi vi phạm phân đoạn và lỗi bus. Trước khi gọi một thao tác Map hoặc Reduce của người dùng, thư viện MapReduce lưu số thứ tự của đối số vào một biến toàn cục. Nếu mã nguồn của người dùng tạo ra một tín hiệu, bộ xử lý tín hiệu gửi một gói UDP “last gasp” chứa số thứ tự tới master MapReduce. Khi master đã thấy nhiều hơn một sự cố trên một bản ghi cụ thể, nó chỉ ra rằng bản ghi đó nên được bỏ qua khi nó phát hành lần thực thi lại tiếp theo của tác vụ Map hoặc Reduce tương ứng.

### 4.7  Thực thi cục bộ {#dean-2004-mapreduce-s4-7 .section tag=007A}

Việc gỡ lỗi các vấn đề trong các hàm Map hoặc Reduce có thể phức tạp, vì tính toán thực tế diễn ra trong một hệ thống phân tán, thường trên vài nghìn máy, với các quyết định gán công việc được master đưa ra một cách động. Để hỗ trợ việc gỡ lỗi, lập hồ sơ và kiểm thử quy mô nhỏ, chúng tôi đã phát triển một triển khai thay thế của thư viện MapReduce, thực thi tuần tự toàn bộ công việc của một thao tác MapReduce trên máy cục bộ. Các điều khiển được cung cấp cho người dùng để tính toán có thể được giới hạn ở các tác vụ map cụ thể. Người dùng gọi chương trình của họ với một cờ đặc biệt và sau đó có thể dễ dàng sử dụng bất kỳ công cụ gỡ lỗi hoặc kiểm thử nào mà họ thấy hữu ích (ví dụ: gdb).

### 4.8  Thông tin trạng thái {#dean-2004-mapreduce-s4-8 .section tag=007B}

Master chạy một server HTTP nội bộ và xuất ra một tập hợp các trang trạng thái để con người sử dụng. Các trang trạng thái hiển thị tiến trình của tính toán, chẳng hạn như có bao nhiêu tác vụ đã hoàn thành, bao nhiêu tác vụ đang được thực hiện, byte của đầu vào, byte của dữ liệu trung gian, byte của đầu ra, tốc độ xử lý, v.v. Các trang này cũng chứa các liên kết tới các file lỗi tiêu chuẩn và đầu ra tiêu chuẩn được tạo bởi mỗi tác vụ. Người dùng có thể sử dụng dữ liệu này để dự đoán tính toán sẽ mất bao lâu và liệu có nên thêm nhiều tài nguyên hơn vào tính toán hay không. Các trang này cũng có thể được sử dụng để xác định khi nào tính toán chậm hơn nhiều so với dự kiến.

Ngoài ra, trang trạng thái cấp cao nhất hiển thị những worker nào đã gặp sự cố, và những tác vụ map và reduce nào chúng đang xử lý khi gặp sự cố. Thông tin này hữu ích khi cố gắng chẩn đoán lỗi trong mã nguồn của người dùng.

### 4.9  Bộ đếm {#dean-2004-mapreduce-s4-9 .section tag=007C}

Thư viện MapReduce cung cấp một tiện ích bộ đếm để đếm sự xuất hiện của các sự kiện khác nhau. Ví dụ, mã nguồn của người dùng có thể muốn đếm tổng số từ đã được xử lý hoặc số tài liệu tiếng Đức đã được lập chỉ mục, v.v.

Để sử dụng tiện ích này, mã nguồn của người dùng tạo một đối tượng bộ đếm có tên và sau đó tăng bộ đếm một cách thích hợp trong hàm Map và/hoặc Reduce. Ví dụ:

```text
Counter* uppercase;
uppercase = GetCounter("uppercase");

map(String name, String contents):
  for each word w in contents:
    if (IsCapitalized(w)):
      uppercase->Increment();
    EmitIntermediate(w, "1");
```

Các giá trị bộ đếm từ từng máy worker được truyền định kỳ tới master (được gắn kèm trong phản hồi ping). Master tổng hợp các giá trị bộ đếm từ các tác vụ map và reduce thành công và trả chúng về mã nguồn của người dùng khi thao tác MapReduce hoàn tất. Các giá trị bộ đếm hiện tại cũng được hiển thị trên trang trạng thái của master để con người có thể theo dõi tiến trình của tính toán đang chạy. Khi tổng hợp các giá trị bộ đếm, master loại bỏ ảnh hưởng của các lần thực thi trùng lặp của cùng một tác vụ map hoặc reduce để tránh đếm kép. (Các lần thực thi trùng lặp có thể phát sinh từ việc chúng tôi sử dụng các tác vụ sao lưu và từ việc thực thi lại các tác vụ do sự cố.)

Một số giá trị bộ đếm được thư viện MapReduce tự động duy trì, chẳng hạn như số cặp khóa/giá trị đầu vào đã được xử lý và số cặp khóa/giá trị đầu ra đã được tạo ra.

Người dùng nhận thấy tiện ích bộ đếm hữu ích để kiểm tra tính hợp lý của hành vi các thao tác MapReduce. Ví dụ, trong một số thao tác MapReduce, mã nguồn của người dùng có thể muốn đảm bảo rằng số cặp đầu ra được tạo ra chính xác bằng số cặp đầu vào đã được xử lý, hoặc rằng tỷ lệ tài liệu tiếng Đức được xử lý nằm trong một tỷ lệ chấp nhận được nào đó của tổng số tài liệu đã được xử lý.
