---
paper: dean-2004-mapreduce
title: 'MapReduce: Simplified Data Processing on Large Clusters'
authors:
  - Jeffrey Dean
  - Sanjay Ghemawat
year: 2004
venue: OSDI
field: systems
section: "2"
section_title: Mô hình lập trình
tag: 006C
kind: section
lang: vi
source: https://www.usenix.org/legacy/events/osdi04/tech/full_papers/dean/dean.pdf
pdf_sha256: 9cfef3ef1b8fe1a1b66c7221f56c2eeca0b15d6608ea68b0c85a38bfbffd8ce5
pdf_pages: 2-3
extraction: vision
extraction_model: gpt-5
content_sha256: 02f61812703c9e5ffd34605d6bdca6619e1c39854e1e23e05875992d08be03e4
translated_from: content/en/dean-2004-mapreduce/02_programming_model.md
source_content_sha256: c7e67fc6b1103b4953278edc167bdfc9009815abad8934e8d5cc8c236f7a0d6f
translation_model: gpt-5
translation_run: 20260914T163737Z
glossary_version: 6
glossary_terms_sha256: afc6de5d010821f75553a129f8b55d5fbabc0d9d7af198021ca9a5a496de4088
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Tính toán nhận một tập các cặp khóa/giá trị đầu vào và tạo ra một tập các cặp khóa/giá trị đầu ra. Người dùng của thư viện MapReduce biểu diễn phép tính dưới dạng hai hàm: Map và Reduce.

Map, do người dùng viết, nhận một cặp đầu vào và tạo ra một tập các cặp khóa/giá trị trung gian. Thư viện MapReduce nhóm tất cả các giá trị trung gian gắn với cùng một khóa trung gian $I$ và truyền chúng cho hàm Reduce.

Hàm Reduce, cũng do người dùng viết, nhận một khóa trung gian $I$ và một tập các giá trị của khóa đó. Nó hợp nhất các giá trị này để tạo thành một tập giá trị có thể nhỏ hơn. Thông thường, mỗi lần gọi Reduce chỉ tạo ra không hoặc một giá trị đầu ra. Các giá trị trung gian được cung cấp cho hàm reduce của người dùng thông qua một bộ lặp (iterator). Điều này cho phép chúng tôi xử lý các danh sách giá trị quá lớn để chứa trong bộ nhớ.

### 2.1 Ví dụ {#dean-2004-mapreduce-s2-1 .section tag=006D}

Xét bài toán đếm số lần xuất hiện của mỗi từ trong một tập hợp lớn các tài liệu. Người dùng sẽ viết mã tương tự mã giả sau:

```text
map(String key, String value):
    // key: document name
    // value: document contents
    for each word w in value:
        EmitIntermediate(w, "1");

reduce(String key, Iterator values):
    // key: a word
    // values: a list of counts
    int result = 0;
    for each v in values:
        result += ParseInt(v);
    Emit(AsString(result));
```

Hàm map phát ra mỗi từ cùng với số lần xuất hiện tương ứng (chỉ là ‘1’ trong ví dụ đơn giản này). Hàm reduce cộng tất cả các số đếm được phát ra cho một từ cụ thể.

Ngoài ra, người dùng viết mã để điền vào một đối tượng đặc tả mapreduce tên của các file đầu vào và đầu ra, cùng các tham số tinh chỉnh tùy chọn. Sau đó, người dùng gọi hàm MapReduce, truyền cho nó đối tượng đặc tả. Mã của người dùng được liên kết với thư viện MapReduce (được triển khai bằng C++). Phụ lục A chứa toàn bộ văn bản chương trình cho ví dụ này.

### 2.2 Các kiểu {#dean-2004-mapreduce-s2-2 .section tag=006E}

Mặc dù mã giả trước đó được viết theo các đầu vào và đầu ra kiểu chuỗi, về mặt khái niệm, các hàm map và reduce do người dùng cung cấp có các kiểu tương ứng:

```text
map     (k1,v1)          → list(k2,v2)
reduce  (k2,list(v2))    → list(v2)
```

Tức là, các khóa và giá trị đầu vào được lấy từ một miền khác với miền của các khóa và giá trị đầu ra. Hơn nữa, các khóa và giá trị trung gian thuộc cùng miền với các khóa và giá trị đầu ra.

Cài đặt C++ của chúng tôi truyền các chuỗi đến và đi từ các hàm do người dùng định nghĩa và để mã của người dùng chuyển đổi giữa các chuỗi và các kiểu thích hợp.

### 2.3 Thêm ví dụ {#dean-2004-mapreduce-s2-3 .section tag=006F}

Dưới đây là một vài ví dụ đơn giản về các chương trình thú vị có thể dễ dàng được biểu diễn dưới dạng các phép tính MapReduce.

Grep phân tán: Hàm map phát ra một dòng nếu nó khớp với mẫu được cung cấp. Hàm reduce là một hàm đồng nhất, chỉ sao chép dữ liệu trung gian được cung cấp sang đầu ra.

Đếm tần suất truy cập URL: Hàm map xử lý các nhật ký yêu cầu trang web và xuất $\langle URL,1\rangle$. Hàm reduce cộng tất cả các giá trị của cùng một URL và phát ra một cặp $\langle URL,total\ count\rangle$.

Đồ thị liên kết Web đảo: Hàm map xuất các cặp $\langle target,source\rangle$ cho mỗi liên kết đến một URL đích được tìm thấy trong một trang có tên source. Hàm reduce nối danh sách tất cả các URL nguồn gắn với một URL đích cho trước và phát ra cặp: $\langle target,list(source)\rangle$

Vectơ thuật ngữ theo máy chủ: Một vectơ thuật ngữ tóm tắt các từ quan trọng nhất xuất hiện trong một tài liệu hoặc một tập tài liệu dưới dạng một danh sách các cặp $\langle word,frequency\rangle$. Hàm map phát ra một cặp $\langle hostname,term\ vector\rangle$ cho mỗi tài liệu đầu vào (trong đó hostname được trích xuất từ URL của tài liệu). Hàm reduce nhận tất cả các vectơ thuật ngữ theo từng tài liệu của một máy chủ cho trước. Nó cộng các vectơ thuật ngữ này lại với nhau, loại bỏ các thuật ngữ ít xuất hiện, rồi phát ra một cặp $\langle hostname,term\ vector\rangle$ cuối cùng.

Hình 1: Tổng quan về thực thi {#dean-2004-mapreduce-fig-1 .figure tag=0070}

Chỉ mục đảo: Hàm map phân tích từng tài liệu và phát ra một chuỗi các cặp $\langle word, document\ ID\rangle$. Hàm reduce nhận tất cả các cặp của một từ cho trước, sắp xếp các ID tài liệu tương ứng và phát ra một cặp $\langle word, list(document\ ID)\rangle$. Tập hợp tất cả các cặp đầu ra tạo thành một chỉ mục đảo đơn giản. Có thể dễ dàng mở rộng phép tính này để theo dõi vị trí của các từ.

Sắp xếp phân tán: Hàm map trích xuất khóa từ mỗi bản ghi và phát ra một cặp $\langle key, record\rangle$. Hàm reduce phát ra tất cả các cặp không thay đổi. Phép tính này phụ thuộc vào các cơ chế phân vùng được mô tả trong Mục 4.1 và các thuộc tính thứ tự được mô tả trong Mục 4.2.
