---
paper: goodfellow-2014-gan
title: Generative Adversarial Nets
authors:
  - Ian J. Goodfellow
  - Jean Pouget-Abadie
  - Mehdi Mirza
  - Bing Xu
  - David Warde-Farley
  - Sherjil Ozair
  - Aaron Courville
  - Yoshua Bengio
year: 2014
venue: NIPS
field: ai-ml
section_title: Front Matter
tag: 00C0
kind: front
lang: vi
source: arxiv:1406.2661
pdf_sha256: ff5819e3a7b713c3bd3107b7de3d51fe0a347aa5d8444f0efdcf2345ef0a8b63
pdf_pages: "1"
extraction: vision
extraction_model: gpt-6-astra
content_sha256: e09418c4a6446299c7ab8fee8d5a441de00b6f4d2b708532c84ded29a847e8c8
translated_from: content/en/goodfellow-2014-gan/00_front.md
source_content_sha256: a4e28d68ff58a1ca69f29c4a8a52e6c2dcd135d63d9462b4b91a1eb91d010ffd
translation_model: gpt-5
translation_run: 20260915T022520Z
glossary_version: 6
glossary_terms_sha256: 0d0a9334a40352952769479a6ad339487dd551fe3d836bae9914ea196d2f4310
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Mạng đối kháng sinh (Generative Adversarial Nets)

**Ian J. Goodfellow, Jean Pouget-Abadie[^1], Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair[^2], Aaron Courville, Yoshua Bengio[^3]**

Département d’informatique et de recherche opérationnelle  
Université de Montréal  
Montréal, QC H3C 3J7 arXiv:1406.2661v1 [stat.ML] 10 Jun 2014

Tóm tắt

Chúng tôi đề xuất một khung mới để ước lượng các mô hình sinh thông qua một quá trình đối kháng, trong đó chúng tôi đồng thời huấn luyện hai mô hình: một mô hình sinh $G$ nắm bắt phân phối dữ liệu, và một mô hình phân biệt $D$ ước lượng xác suất rằng một mẫu đến từ dữ liệu huấn luyện thay vì từ $G$. Thủ tục huấn luyện cho $G$ là cực đại hóa xác suất $D$ mắc lỗi. Khung này tương ứng với một trò chơi minimax hai người chơi. Trong không gian của các hàm tùy ý $G$ và $D$, tồn tại một nghiệm duy nhất, với $G$ khôi phục phân phối dữ liệu huấn luyện và $D$ bằng $\frac{1}{2}$ ở mọi nơi. Trong trường hợp $G$ và $D$ được định nghĩa bởi các perceptron đa lớp, toàn bộ hệ thống có thể được huấn luyện bằng lan truyền ngược. Không cần bất kỳ chuỗi Markov nào hoặc các mạng suy luận xấp xỉ được cuộn lại trong quá trình huấn luyện hoặc sinh mẫu. Các thí nghiệm chứng minh tiềm năng của khung này thông qua đánh giá định tính và định lượng các mẫu được sinh ra.
