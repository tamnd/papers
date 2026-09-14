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
section_title: Mô hình Lập trình
kind: section
lang: vi
source: https://www.usenix.org/legacy/events/osdi04/tech/full_papers/dean/dean.pdf
pdf_sha256: 9cfef3ef1b8fe1a1b66c7221f56c2eeca0b15d6608ea68b0c85a38bfbffd8ce5
pdf_pages: 2-3
extraction: vision
extraction_model: gpt-5
content_sha256: 79ad3856acbaa33e38741b32fbce24e26a713e3b2e6a6ab1a9d8315dbca58602
translated_from: content/en/dean-2004-mapreduce/02_programming_model.md
source_content_sha256: aaf581737cd4d87ef514b916c1ce15d8ee969caef455403515366f71228c9af2
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: afc6de5d010821f75553a129f8b55d5fbabc0d9d7af198021ca9a5a496de4088
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Tính toán nhận một tập các cặp khóa/giá trị đầu vào, và tạo ra một tập các cặp khóa/giá trị đầu ra. Người dùng của thư viện MapReduce biểu diễn tính toán dưới dạng hai hàm: Map và Reduce.

Map, do người dùng viết, nhận một cặp đầu vào và tạo ra một tập các cặp khóa/giá trị trung gian. Thư viện MapReduce nhóm tất cả các giá trị trung gian được liên kết với cùng một khóa trung gian $I$ lại với nhau và truyền chúng cho hàm Reduce.

Hàm Reduce, cũng do người dùng viết, nhận một khóa trung gian $I$ và một tập các giá trị cho khóa đó. Nó gộp các giá trị này lại với nhau để tạo thành một tập giá trị có thể nhỏ hơn. Thông thường chỉ có không hoặc một giá trị đầu ra được tạo ra cho mỗi lần gọi Reduce. Các giá trị trung gian được cung cấp cho hàm reduce của người dùng thông qua một iterator. Điều này cho phép chúng tôi xử lý các danh sách giá trị quá lớn để vừa trong bộ nhớ.

### 2.1 Ví dụ

Xét bài toán đếm số lần xuất hiện của mỗi từ trong một tập hợp lớn các tài liệu. Người dùng sẽ viết mã tương tự như đoạn mã giả sau:

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

Hàm map xuất ra mỗi từ cùng với một số đếm số lần xuất hiện tương ứng (chỉ là ‘1’ trong ví dụ đơn giản này). Hàm reduce cộng tất cả các số đếm được xuất ra cho một từ cụ thể.

Ngoài ra, người dùng viết mã để điền vào một đối tượng đặc tả mapreduce các tên của các file đầu vào và đầu ra, cùng các tham số tinh chỉnh tùy chọn. Sau đó người dùng gọi hàm MapReduce, truyền cho nó đối tượng đặc tả. Mã của người dùng được liên kết cùng với thư viện MapReduce (được triển khai bằng C++). Phụ lục A chứa toàn bộ văn bản chương trình cho ví dụ này.

### 2.2 Kiểu

Mặc dù mã giả trước đó được viết theo các đầu vào và đầu ra dạng string, về mặt khái niệm các hàm map và reduce do người dùng cung cấp có các kiểu tương ứng:

```text
map     (k1,v1)          → list(k2,v2)
reduce  (k2,list(v2))    → list(v2)
```

Tức là, các khóa và giá trị đầu vào được lấy từ một miền khác với các khóa và giá trị đầu ra. Hơn nữa, các khóa và giá trị trung gian thuộc cùng miền với các khóa và giá trị đầu ra.

Cài đặt C++ của chúng tôi truyền các string đến và đi từ các hàm do người dùng định nghĩa và để mã của người dùng chuyển đổi giữa các string và các kiểu thích hợp.

### 2.3 Các Ví dụ Khác

Dưới đây là một vài ví dụ đơn giản về các chương trình thú vị có thể dễ dàng được biểu diễn dưới dạng các tính toán MapReduce.

Distributed Grep: Hàm map xuất ra một dòng nếu nó khớp với một mẫu được cung cấp. Hàm reduce là một hàm đồng nhất chỉ sao chép dữ liệu trung gian được cung cấp đến đầu ra.

Count of URL Access Frequency: Hàm map xử lý các nhật ký của các yêu cầu trang web và xuất ra $\langle URL,1\rangle$. Hàm reduce cộng tất cả các giá trị cho cùng một URL và xuất ra một cặp $\langle URL,total\ count\rangle$.

Reverse Web-Link Graph: Hàm map xuất ra các cặp $\langle target,source\rangle$ cho mỗi liên kết đến một URL đích được tìm thấy trong một trang có tên source. Hàm reduce nối danh sách tất cả các URL nguồn được liên kết với một URL đích cho trước và xuất ra cặp: $\langle target,list(source)\rangle$

Term-Vector per Host: Một vectơ thuật ngữ tóm tắt các từ quan trọng nhất xuất hiện trong một tài liệu hoặc một tập tài liệu dưới dạng một danh sách các cặp $\langle word,frequency\rangle$. Hàm map xuất ra một cặp $\langle hostname,term\ vector\rangle$ cho mỗi tài liệu đầu vào (trong đó hostname được trích xuất từ URL của tài liệu). Hàm reduce nhận tất cả các vectơ thuật ngữ trên mỗi tài liệu cho một host cụ thể. Nó cộng các vectơ thuật ngữ này lại với nhau, loại bỏ các thuật ngữ không thường xuyên, sau đó xuất ra một cặp $\langle hostname,term\ vector\rangle$ cuối cùng.

Hình 1: Tổng quan về thực thi

Inverted Index: Hàm map phân tích cú pháp từng tài liệu, và xuất ra một chuỗi các cặp $\langle word, document\ ID\rangle$. Hàm reduce nhận tất cả các cặp cho một từ cho trước, sắp xếp các document ID tương ứng và xuất ra một cặp $\langle word, list(document\ ID)\rangle$. Tập hợp tất cả các cặp đầu ra tạo thành một inverted index đơn giản. Dễ dàng mở rộng tính toán này để theo dõi vị trí của các từ.

Distributed Sort: Hàm map trích xuất khóa từ mỗi bản ghi, và xuất ra một cặp $\langle key, record\rangle$. Hàm reduce xuất ra tất cả các cặp không thay đổi. Tính toán này phụ thuộc vào các phương tiện phân vùng được mô tả trong Section 4.1 và các thuộc tính thứ tự được mô tả trong Section 4.2.
