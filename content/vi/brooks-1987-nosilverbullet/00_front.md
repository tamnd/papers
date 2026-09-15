---
paper: brooks-1987-nosilverbullet
title: No Silver Bullet - Essence and Accidents of Software Engineering
authors:
  - Frederick P. Brooks Jr.
year: 1987
venue: IEEE Computer
field: software
section_title: Front Matter
tag: "0069"
kind: front
lang: vi
source: https://www.cs.unc.edu/techreports/86-020.pdf
pdf_sha256: a4a11dcb6ff7dcdfcc680e27760126d86c568cbb99a53a2bf58dc9041fbb190e
pdf_pages: "4"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 6b19475160f148e672e3e81ea8d5e92a7c80edf6fe3f55e0673c3e68cd8635e6
translated_from: content/en/brooks-1987-nosilverbullet/00_front.md
source_content_sha256: b8d52437e312b8895e5ee368ca2be85b3e69bd30441b95294890ef00fbdbc283
translation_model: gpt-5
translation_run: 20260915T033315Z
glossary_version: 6
glossary_terms_sha256: e6d7d95c10a297b8398386447b5f0424f8ccda78f5063d550f1f6b9aef300c33
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

KHÔNG CÓ VIÊN ĐẠN BẠC –

BẢN CHẤT VÀ NHỮNG SỰ CỐ CỦA KỸ THUẬT PHẦN MỀM

Frederick P. Brooks Jr.
Giáo sư Khoa học Máy tính Kenan
University of North Carolina at Chapel Hill
New West Hall 035A
Chapel Hill, North Carolina 27514 USA

Tóm tắt

Mọi hoạt động xây dựng phần mềm đều bao gồm các nhiệm vụ bản chất, là việc tạo dựng các cấu trúc khái niệm phức tạp tạo nên thực thể phần mềm trừu tượng, và các nhiệm vụ ngẫu nhiên, là sự biểu diễn các thực thể trừu tượng này trong các ngôn ngữ lập trình và sự ánh xạ chúng sang các ngôn ngữ máy trong các ràng buộc về không gian và tốc độ. Phần lớn những tiến bộ lớn trong năng suất phần mềm trước đây đến từ việc loại bỏ các rào cản nhân tạo khiến các nhiệm vụ ngẫu nhiên trở nên khó khăn quá mức, chẳng hạn như các hạn chế nghiêm ngặt về phần cứng, các ngôn ngữ lập trình vụng về, thiếu thời gian máy. Bao nhiêu phần trong những gì các kỹ sư phần mềm hiện nay làm vẫn còn dành cho cái ngẫu nhiên, trái ngược với cái bản chất? Trừ khi nó chiếm hơn 9/10 toàn bộ nỗ lực, việc thu nhỏ mọi hoạt động ngẫu nhiên xuống thời gian bằng không sẽ không mang lại sự cải thiện theo cấp độ lớn.

Vì vậy, có vẻ như thời điểm đã đến để giải quyết những phần bản chất của nhiệm vụ phần mềm, những phần liên quan đến việc tạo dựng các cấu trúc khái niệm trừu tượng có độ phức tạp lớn. Tôi đề xuất:

• khai thác thị trường đại chúng để tránh xây dựng những gì có thể mua được.
• sử dụng tạo mẫu nhanh như một phần của một lần lặp có kế hoạch trong việc thiết lập các yêu cầu phần mềm.
• phát triển phần mềm một cách hữu cơ, bổ sung ngày càng nhiều hàm vào các hệ thống khi chúng được chạy, sử dụng và kiểm thử.
• xác định và phát triển những nhà thiết kế khái niệm vĩ đại của thế hệ đang lên.
