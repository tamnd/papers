---
paper: silver-2016-alphago
title: Mastering the game of Go with deep neural networks and tree search
authors:
  - David Silver
  - Aja Huang
  - Chris J. Maddison
  - Arthur Guez
  - Laurent Sifre
  - George van den Driessche
  - Julian Schrittwieser
  - Ioannis Antonoglou
  - Veda Panneershelvam
  - Marc Lanctot
year: 2016
venue: Nature
field: ai-ml
section_title: Front Matter
tag: 01A4
kind: front
lang: vi
source: https://storage.googleapis.com/deepmind-media/alphago/AlphaGoNaturePaper.pdf
pdf_sha256: 9c9184385a3d37b4f4e9d9715270986c43172747b1d08f29093128c1ef878b60
pdf_pages: 1-3
extraction: vision
extraction_model: gpt-5
content_sha256: ccac69e21bfe6026b4f9a223f1767b703eb6956d1fc399a9fa4edec6f4193816
translated_from: content/en/silver-2016-alphago/00_front.md
source_content_sha256: 52f6dc20585ccc9fea30d7103718d2270d69b381f5d7f965e5a1a62eb0d11372
translation_model: gpt-5
translation_run: 20260915T013833Z
glossary_version: 6
glossary_terms_sha256: 0d0a9334a40352952769479a6ad339487dd551fe3d836bae9914ea196d2f4310
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

doi:10.1038/nature16961

**Trò chơi cờ vây từ lâu đã được xem là trò chơi cổ điển thách thức nhất đối với trí tuệ nhân tạo do không gian tìm kiếm khổng lồ và sự khó khăn trong việc đánh giá các vị trí và nước đi trên bàn cờ. Ở đây chúng tôi giới thiệu một phương pháp mới cho cờ vây trên máy tính sử dụng các ‘mạng giá trị (value networks)’ để đánh giá các vị trí trên bàn cờ và các ‘mạng chính sách (policy networks)’ để lựa chọn nước đi. Các mạng nơ-ron (neural network) sâu này được huấn luyện bằng một sự kết hợp mới giữa học có giám sát từ các ván đấu của chuyên gia con người và học tăng cường từ các ván đấu tự chơi. Không có bất kỳ tìm kiếm nhìn trước nào, các mạng nơ-ron chơi ở mức độ của các chương trình tìm kiếm cây Monte Carlo tiên tiến nhất, vốn mô phỏng hàng nghìn ván đấu ngẫu nhiên của tự chơi. Chúng tôi cũng giới thiệu một thuật toán tìm kiếm mới kết hợp mô phỏng Monte Carlo với các mạng giá trị và mạng chính sách. Sử dụng thuật toán tìm kiếm này, chương trình AlphaGo của chúng tôi đạt tỷ lệ thắng 99.8% trước các chương trình cờ vây khác, và đánh bại nhà vô địch cờ vây châu Âu là con người với tỷ số 5 ván thắng đến 0. Đây là lần đầu tiên một chương trình máy tính đánh bại một kỳ thủ chuyên nghiệp con người trong trò chơi cờ vây kích thước đầy đủ, một thành tựu trước đây được cho là còn cách ít nhất một thập kỷ.**
