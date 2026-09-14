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
content_sha256: cb81e349ffbeb8edc693ab4a5168ab040c1fc4b7bc5c4354642d98af34fccdfe
translated_from: content/en/dijkstra-1959-shortestpath/00_front.md
source_content_sha256: 584ada85ee4b242ab88f6aec897b92de14d45b2b822306bde835bf4e815a61ca
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: 51f62d367854beec600f51894702ad34dfcde96c993d5c00a2f7a9873047d13f
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
roundtrip: same
roundtrip_run: 20260914T214350Z
---

Một ghi chú về hai bài toán liên quan đến đồ thị

Bởi

E. W. DIJKSTRA

Xét $n$ điểm (nút), một số hoặc tất cả các cặp điểm được nối với nhau bởi một nhánh; độ dài của mỗi nhánh được cho trước. Chúng ta giới hạn xét trường hợp tồn tại ít nhất một đường đi giữa bất kỳ hai nút nào. Bây giờ chúng ta xét hai bài toán.

Bài toán 1. Xây dựng cây có tổng độ dài nhỏ nhất giữa $n$ nút. (Cây là một đồ thị có đúng một đường đi giữa mọi cặp nút.)

Trong quá trình xây dựng mà chúng tôi trình bày ở đây, các nhánh được chia thành ba tập:

I. các nhánh chắc chắn được đưa vào cây đang xây dựng (chúng sẽ tạo thành một cây con);

II. các nhánh mà từ đó nhánh tiếp theo được thêm vào tập I sẽ được chọn;

III. các nhánh còn lại (bị loại bỏ hoặc chưa được xét).

Các nút được chia thành hai tập:

A. các nút được nối bởi các nhánh của tập I,

B. các nút còn lại (mỗi nút trong số này sẽ có đúng một nhánh của tập II dẫn tới).

Chúng ta bắt đầu xây dựng bằng cách chọn một nút tùy ý làm phần tử duy nhất của tập A, và đưa tất cả các nhánh kết thúc tại nút này vào tập II. Ban đầu, tập I là rỗng. Từ đó trở đi, chúng ta lặp đi lặp lại hai bước sau.

Bước 1. Nhánh ngắn nhất của tập II được loại khỏi tập này và thêm vào tập I.
