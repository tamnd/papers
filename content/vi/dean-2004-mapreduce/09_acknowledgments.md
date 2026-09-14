---
paper: dean-2004-mapreduce
title: 'MapReduce: Simplified Data Processing on Large Clusters'
authors:
  - Jeffrey Dean
  - Sanjay Ghemawat
year: 2004
venue: OSDI
field: systems
section_title: Lời cảm ơn
kind: section
lang: vi
source: https://www.usenix.org/legacy/events/osdi04/tech/full_papers/dean/dean.pdf
pdf_sha256: 9cfef3ef1b8fe1a1b66c7221f56c2eeca0b15d6608ea68b0c85a38bfbffd8ce5
pdf_pages: "12"
extraction: vision
extraction_model: gpt-5
content_sha256: 7c4e7ad63e7f89b125008196782464c8ea7cd96172274103e6ddc980159940ef
translated_from: content/en/dean-2004-mapreduce/09_acknowledgments.md
source_content_sha256: a9780cb17081696f83d959340a1569e16f3c536d8508cc5f7edf1e1ee3f518ee
translation_model: gpt-5
translation_run: 20260914T163737Z
glossary_version: 6
glossary_terms_sha256: afc6de5d010821f75553a129f8b55d5fbabc0d9d7af198021ca9a5a496de4088
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Josh Levenberg đã đóng vai trò quan trọng trong việc sửa đổi và mở rộng API MapReduce ở cấp người dùng với một số tính năng mới dựa trên kinh nghiệm của ông trong việc sử dụng MapReduce và các đề xuất cải tiến từ những người khác. MapReduce đọc đầu vào của nó từ và ghi đầu ra của nó vào Google File System [[ghemawat-2003-gfs]]. Chúng tôi xin cảm ơn Mohit Aron, Howard Gobioff, Markus Gutschke, David Kramer, Shun-Tak Leung, và Josh Redstone vì công việc của họ trong việc phát triển GFS. Chúng tôi cũng xin cảm ơn Percy Liang và Olcan Sercinoglu vì công việc của họ trong việc phát triển hệ thống quản lý cụm được MapReduce sử dụng. Mike Burrows, Wilson Hsieh, Josh Levenberg, Sharon Perl, Rob Pike, và Debby Wallach đã đưa ra những nhận xét hữu ích về các bản thảo trước đó của bài báo này. Các phản biện ẩn danh của OSDI, cùng với người hướng dẫn của chúng tôi, Eric Brewer, đã đưa ra nhiều đề xuất hữu ích về các lĩnh vực mà bài báo có thể được cải thiện. Cuối cùng, chúng tôi cảm ơn tất cả người dùng MapReduce trong tổ chức kỹ thuật của Google vì đã cung cấp các phản hồi, đề xuất và báo cáo lỗi hữu ích.
