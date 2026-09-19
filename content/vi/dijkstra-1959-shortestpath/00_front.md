---
paper: dijkstra-1959-shortestpath
title: A Note on Two Problems in Connexion with Graphs
authors:
  - Edsger W. Dijkstra
year: 1959
venue: Numerische Mathematik
field: algorithms
section_title: Front Matter
tag: 003D
kind: front
lang: vi
source: https://ir.cwi.nl/pub/9256/9256D.pdf
pdf_sha256: ee0938a64a327cf6d60c25115ae98990417224408d9c062f09907a044e045ac0
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 561b62d63f3edab97be879e614d8ae9e373ed42b253b4bd43573ca1f010d8359
translated_from: content/en/dijkstra-1959-shortestpath/00_front.md
source_content_sha256: a31154142bc70b6cc2902b02475a56116828fb179aef58c75e01773274da4b43
translation_model: gpt-5
translation_run: 20260919T113512Z
glossary_version: 7
glossary_terms_sha256: d4043ebd5a5c828b0239f76956644bfb5bb815f3188dc3282d75521c97669214
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Một ghi chú về hai bài toán liên quan đến đồ thị

Bởi
E. W. DIJKSTRA

Xét $n$ điểm (nút), một số hoặc tất cả các cặp điểm trong đó được nối với nhau bởi một nhánh; độ dài của mỗi nhánh được cho trước. Chúng tôi giới hạn xét trường hợp mà giữa hai nút bất kỳ luôn tồn tại ít nhất một đường đi. Bây giờ chúng tôi xét hai bài toán.

Bài toán 1. Xây dựng cây có tổng độ dài nhỏ nhất giữa $n$ nút. (Một cây là một đồ thị có đúng một và chỉ một đường đi giữa mỗi hai nút.)

Trong quá trình xây dựng được trình bày ở đây, các nhánh được chia thành ba tập:
I. các nhánh chắc chắn được gán vào cây đang xây dựng (chúng sẽ tạo thành một cây con);
II. các nhánh mà từ đó nhánh tiếp theo được thêm vào tập I sẽ được chọn;
III. các nhánh còn lại (bị loại bỏ hoặc chưa được xét đến).

Các nút được chia thành hai tập:
A. các nút được nối bởi các nhánh của tập I,
B. các nút còn lại (một và chỉ một nhánh của tập II sẽ dẫn đến mỗi nút này).

Chúng tôi bắt đầu quá trình xây dựng bằng cách chọn một nút tùy ý làm thành viên duy nhất của tập A, và đặt tất cả các nhánh kết thúc tại nút này vào tập II. Ban đầu, tập I rỗng. Từ đó trở đi chúng tôi lặp lại hai bước sau.

Bước 1. Nhánh ngắn nhất của tập II được loại bỏ khỏi tập này và được thêm vào tập I. Kết quả là một nút được chuyển từ tập $B$ sang tập $A$.

Bước 2. Xét các nhánh dẫn từ nút vừa được chuyển sang tập A đến các nút vẫn còn thuộc tập B. Nếu nhánh đang xét dài hơn nhánh tương ứng trong tập II, nó bị loại bỏ; nếu ngắn hơn, nó thay thế nhánh tương ứng trong tập II, và nhánh sau bị loại bỏ.

Sau đó chúng tôi quay lại bước 1 và lặp lại quá trình cho đến khi các tập II và B đều rỗng. Các nhánh trong tập I tạo thành cây cần tìm.

Lời giải được đưa ra ở đây được ưu tiên hơn lời giải do J. B. KRUSKAL [1] đưa ra và những lời giải do H. LOBERMAN và A. WEINBERGER [2] đưa ra. Trong các lời giải của họ, tất cả các nhánh — có thể là $\frac{1}{2} n(n-1)$ — trước hết được sắp xếp theo độ dài. Ngay cả khi độ dài của các nhánh là một hàm có thể tính được của tọa độ các nút, các phương pháp của họ yêu cầu dữ liệu của tất cả các nhánh được lưu trữ đồng thời. Phương pháp của chúng tôi chỉ yêu cầu lưu trữ đồng thời dữ liệu của nhiều nhất $n$ nhánh, cụ thể là các nhánh trong các tập I và II cùng với nhánh đang được xét trong bước 2.

Bài toán 2. Tìm đường đi có tổng độ dài nhỏ nhất giữa hai nút đã cho $P$ và $Q$.

Chúng tôi sử dụng sự kiện rằng, nếu $R$ là một nút trên đường đi tối thiểu từ $P$ đến $Q$, thì việc biết đường đi sau này suy ra việc biết đường đi tối thiểu từ $P$ đến $R$. Trong lời giải được trình bày, các đường đi tối thiểu từ $P$ đến các nút khác được xây dựng theo thứ tự độ dài tăng dần cho đến khi đạt tới $Q$.

Trong quá trình giải, các nút được chia thành ba tập:
A. các nút mà đường đi có độ dài nhỏ nhất từ $P$ đã được biết; các nút sẽ được thêm vào tập này theo thứ tự độ dài đường đi nhỏ nhất tăng dần từ nút $P$;
B. các nút mà từ đó nút tiếp theo được thêm vào tập A sẽ được chọn; tập này bao gồm tất cả các nút được nối với ít nhất một nút của tập A nhưng bản thân chưa thuộc A;
C. các nút còn lại.

Các nhánh cũng được chia thành ba tập:
I. các nhánh xuất hiện trong các đường đi tối thiểu từ nút $P$ đến các nút trong tập A;
II. các nhánh mà từ đó nhánh tiếp theo được đặt vào tập I sẽ được chọn; một và chỉ một nhánh của tập này sẽ dẫn đến mỗi nút trong tập B;
III. các nhánh còn lại (bị loại bỏ hoặc chưa được xét đến).

Ban đầu, tất cả các nút đều thuộc tập C và tất cả các nhánh đều thuộc tập III. Bây giờ chúng tôi chuyển nút $P$ sang tập A và từ đó trở đi lặp lại các bước sau.

Bước 1. Xét tất cả các nhánh $r$ nối nút vừa được chuyển sang tập A với các nút $R$ trong các tập B hoặc C. Nếu nút $R$ thuộc tập B, chúng tôi khảo sát liệu việc sử dụng nhánh $r$ có tạo ra đường đi ngắn hơn từ $P$ đến $R$ so với đường đi đã biết sử dụng nhánh tương ứng trong tập II hay không. Nếu không, nhánh $r$ bị loại bỏ; nếu ngược lại, việc sử dụng nhánh $r$ tạo ra một kết nối ngắn hơn giữa $P$ và $R$ so với kết quả thu được trước đó, nó thay thế nhánh tương ứng trong tập II và nhánh sau bị loại bỏ. Nếu nút $R$ thuộc tập C, nó được thêm vào tập B và nhánh $r$ được thêm vào tập II.

Bước 2. Mỗi nút trong tập B chỉ có thể được nối với nút $P$ theo một cách nếu chúng ta chỉ xét các nhánh từ tập I và một nhánh từ tập II. Theo nghĩa này, mỗi nút trong tập B có một khoảng cách tới nút $P$: nút có khoảng cách nhỏ nhất tới $P$ được chuyển từ tập B sang tập A, và nhánh tương ứng được chuyển từ tập II sang tập I. Sau đó chúng tôi quay lại bước 1 và lặp lại quá trình cho đến khi nút $Q$ được chuyển sang tập A. Khi đó lời giải đã được tìm thấy.

Nhận xét 1. Quá trình trên cũng có thể được áp dụng trong trường hợp độ dài của một nhánh phụ thuộc vào hướng mà nó được duyệt. {#dijkstra-1959-shortestpath-rem-1 .statement tag=0418}

Nhận xét 2. Đối với mỗi nhánh trong các tập I và II, nên ghi lại hai nút của nó (theo thứ tự khoảng cách tăng dần từ $P$), và khoảng cách giữa $P$ và nút của nhánh đó xa $P$ nhất. Đối với các nhánh của tập I, đây là khoảng cách nhỏ nhất thực tế, còn đối với các nhánh của tập II, đây chỉ là khoảng cách nhỏ nhất thu được cho đến thời điểm hiện tại. {#dijkstra-1959-shortestpath-rem-2 .statement tag=0419}

Lời giải được đưa ra ở trên được ưu tiên hơn lời giải của L. R. Ford [3] như được C. Berge [4] mô tả, vì, không phụ thuộc vào số lượng nhánh, chúng ta không cần lưu trữ đồng thời dữ liệu của tất cả các nhánh mà chỉ cần dữ liệu của các nhánh trong các tập I và II, và số lượng này luôn nhỏ hơn $n$. Hơn nữa, lượng công việc cần thực hiện dường như ít hơn đáng kể.
