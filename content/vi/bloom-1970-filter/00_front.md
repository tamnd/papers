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
content_sha256: 8412132bfb17f462c7d188d9cdc86dd631110d3e62d2a7241990941e813df0c3
translated_from: content/en/bloom-1970-filter/00_front.md
source_content_sha256: 6e3e5001e35618a95d7390add14305bc048634f4195f7b3026a34d8a0cf633d5
translation_model: gpt-5
translation_run: 20260918T122832Z
glossary_version: 7
glossary_terms_sha256: d4043ebd5a5c828b0239f76956644bfb5bb815f3188dc3282d75521c97669214
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Đánh đổi Không gian/Thời gian trong Mã hóa Băm với Các Lỗi Cho phép

BURTON H. BLOOM

Computer Usage Company, Newton Upper Falls, Mass.

Trong bài báo này, các sự đánh đổi giữa một số yếu tố tính toán nhất định trong mã hóa băm được phân tích. Bài toán mô hình được xem xét là kiểm tra một chuỗi thông điệp lần lượt từng thông điệp một để xác định việc thuộc về một tập thông điệp đã cho. Hai phương pháp mã hóa băm mới được khảo sát và so sánh với một phương pháp mã hóa băm quy ước cụ thể. Các yếu tố tính toán được xem xét là kích thước của vùng băm (không gian), thời gian cần thiết để xác định một thông điệp là không phải thành viên của tập đã cho (thời gian loại bỏ), và một tần suất lỗi cho phép.

Các phương pháp mới nhằm giảm lượng không gian cần thiết để chứa thông tin được mã hóa băm so với lượng không gian tương ứng với các phương pháp quy ước. Việc giảm không gian đạt được bằng cách khai thác khả năng rằng một phần nhỏ các lỗi do chấp nhận nhầm có thể được chấp nhận trong một số ứng dụng, đặc biệt là các ứng dụng trong đó một lượng lớn dữ liệu có liên quan và do đó một vùng băm thường trú trong bộ nhớ lõi là không khả thi khi sử dụng các phương pháp quy ước.

Trong các ứng dụng như vậy, người ta dự kiến rằng hiệu năng tổng thể có thể được cải thiện bằng cách sử dụng một vùng băm thường trú trong bộ nhớ lõi nhỏ hơn kết hợp với các phương pháp mới và, khi cần thiết, bằng cách sử dụng một số phép kiểm tra phụ có thể tốn thời gian để "bắt" phần nhỏ các lỗi liên quan đến các phương pháp mới. Một ví dụ được thảo luận nhằm minh họa các lĩnh vực ứng dụng khả dĩ của các phương pháp mới.
