---
paper: bloom-1970-filter
title: Space/Time Trade-offs in Hash Coding with Allowable Errors
authors:
  - Burton H. Bloom
year: 1970
venue: Communications of the ACM
field: algorithms
section_title: Front Matter
tag: "0041"
kind: front
lang: vi
source: http://crystal.uta.edu/~mcguigan/cse6350/papers/Bloom.pdf
pdf_sha256: def80c7d042c39d5aab15e6ae1c2b55262ee1123ffcdf53143895089ab5c1728
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 2e4852aa647384f6836a96baf59e32cc51325c78749c3a1583263c63c3b15075
translated_from: content/en/bloom-1970-filter/00_front.md
source_content_sha256: 6e3e5001e35618a95d7390add14305bc048634f4195f7b3026a34d8a0cf633d5
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: 51f62d367854beec600f51894702ad34dfcde96c993d5c00a2f7a9873047d13f
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
roundtrip: same
roundtrip_run: 20260914T214350Z
---

Đánh đổi Không gian/Thời gian trong Mã hóa Băm với Sai số Cho phép

BURTON H. BLOOM

Computer Usage Company, Newton Upper Falls, Mass.

Trong bài báo này, các đánh đổi giữa một số yếu tố tính toán trong mã hóa băm được phân tích. Bài toán điển hình được xét là kiểm tra lần lượt từng thông điệp trong một chuỗi để xác định liệu chúng có thuộc một tập thông điệp cho trước hay không. Hai phương pháp mã hóa băm mới được khảo sát và so sánh với một phương pháp mã hóa băm thông thường cụ thể. Các yếu tố tính toán được xem xét là kích thước của vùng băm (không gian), thời gian cần thiết để xác định một thông điệp không phải là thành viên của tập cho trước (thời gian từ chối), và tần suất sai số cho phép.

Các phương pháp mới nhằm giảm lượng không gian cần thiết để chứa thông tin đã được mã hóa băm so với lượng không gian gắn với các phương pháp thông thường. Việc giảm không gian đạt được bằng cách khai thác khả năng rằng một tỷ lệ nhỏ các sai số dương giả có thể chấp nhận được trong một số ứng dụng, đặc biệt là các ứng dụng liên quan đến một lượng dữ liệu lớn, khiến một vùng băm thường trú trong bộ nhớ chính trở nên không khả thi khi sử dụng các phương pháp thông thường.

Trong những ứng dụng như vậy, người ta dự kiến rằng hiệu năng tổng thể có thể được cải thiện bằng cách sử dụng một vùng băm thường trú trong bộ nhớ chính nhỏ hơn kết hợp với các phương pháp mới và, khi cần thiết, sử dụng một phép kiểm tra phụ, có thể tốn thời gian, để "bắt" tỷ lệ nhỏ các sai số gắn với các phương pháp mới. Một ví dụ được thảo luận nhằm minh họa các lĩnh vực ứng dụng khả dĩ của các phương pháp mới.
