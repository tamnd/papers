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
content_sha256: d8433b0933683b9bd728afe9ef8f4c756e258191106eb2abb0adb5b39212c6df
translated_from: content/en/dijkstra-1959-shortestpath/00_front.md
source_content_sha256: 584ada85ee4b242ab88f6aec897b92de14d45b2b822306bde835bf4e815a61ca
translation_model: gpt-5
translation_run: 20260918T122832Z
glossary_version: 7
glossary_terms_sha256: d4043ebd5a5c828b0239f76956644bfb5bb815f3188dc3282d75521c97669214
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Một ghi chú về hai bài toán liên quan đến đồ thị

Bởi

E. W. DIJKSTRA

Xét $n$ điểm (nút), một số hoặc tất cả các cặp trong số chúng được nối với nhau bởi một nhánh; độ dài của mỗi nhánh được cho trước. Chúng ta chỉ xét trường hợp trong đó tồn tại ít nhất một đường đi giữa bất kỳ hai nút nào. Bây giờ chúng ta xét hai bài toán.

Bài toán 1. Xây dựng cây có tổng độ dài nhỏ nhất giữa $n$ nút. (Một cây là một đồ thị có một và chỉ một đường đi giữa mỗi hai nút.)

Trong quá trình xây dựng mà chúng ta trình bày ở đây, các nhánh được chia thành ba tập:

I. các nhánh chắc chắn được gán cho cây đang được xây dựng (chúng sẽ tạo thành một cây con);

II. các nhánh mà từ đó nhánh tiếp theo được thêm vào tập I sẽ được chọn;

III. các nhánh còn lại (bị loại bỏ hoặc chưa được xét đến).

Các nút được chia thành hai tập:

A. các nút được nối bởi các nhánh của tập I,

B. các nút còn lại (một và chỉ một nhánh của tập II sẽ dẫn đến mỗi nút này).

Chúng ta bắt đầu việc xây dựng bằng cách chọn một nút tùy ý làm thành viên duy nhất của tập A, và đặt tất cả các nhánh kết thúc tại nút này vào tập II. Ban đầu, tập I là rỗng. Từ đó trở đi, chúng ta lặp lại hai bước sau.

Bước 1. Nhánh ngắn nhất của tập II được lấy ra khỏi tập này và thêm vào tập I.
