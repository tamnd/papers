---
paper: hoare-1962-quicksort
title: Quicksort
authors:
  - C. A. R. Hoare
year: 1962
venue: The Computer Journal
field: algorithms
section_title: Front Matter
tag: 003E
kind: front
lang: vi
source: https://www.cs.ox.ac.uk/files/6226/H2006%20-%20Historic%20Quicksort.pdf
pdf_sha256: 1b54e36fac02a0c19213e2858090fa1dca70688f5f99a2748357fd8329918bab
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 1ac889930340e36c2762df830e74038bf50f02830ef5ad616f6af9a55090150e
translated_from: content/en/hoare-1962-quicksort/00_front.md
source_content_sha256: 5a2c556e140ce09b780ceded5b579736cdc08e0ccc54fb57bff8095213749a91
translation_model: gpt-5
translation_run: 20260918T122832Z
glossary_version: 7
glossary_terms_sha256: d4043ebd5a5c828b0239f76956644bfb5bb815f3188dc3282d75521c97669214
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Sắp xếp nhanh

Sau mỗi lần áp dụng quá trình phân hoạch, còn lại hai đoạn cần được sắp xếp. Nếu một trong hai đoạn này rỗng hoặc chỉ gồm một phần tử, thì có thể bỏ qua nó, và quá trình sẽ chỉ được tiếp tục trên đoạn còn lại. Hơn nữa, nếu một đoạn gồm ít hơn ba hoặc bốn phần tử (tùy thuộc vào các đặc tính của máy tính), thì sẽ có lợi khi sắp xếp nó bằng cách sử dụng một chương trình được viết riêng để sắp xếp một số lượng nhỏ phần tử cụ thể. Cuối cùng, nếu cả hai đoạn đều khá lớn, cần phải trì hoãn việc xử lý một trong chúng cho đến khi đoạn kia được sắp xếp hoàn toàn. Trong khi đó, địa chỉ của phần tử đầu tiên và cuối cùng của đoạn bị trì hoãn phải được lưu trữ. Việc tiết kiệm bộ nhớ để lưu trữ các chi tiết của đoạn là rất quan trọng, vì tổng số đoạn tỷ lệ với số lượng phần tử đang được sắp xếp. May mắn thay, không cần thiết phải lưu trữ chi tiết của tất cả các đoạn đồng thời, vì chi tiết của những đoạn đã được sắp xếp hoàn toàn không còn cần thiết nữa.

Phương pháp lưu trữ được khuyến nghị sử dụng một ngăn xếp, tức là một khối các vị trí liên tiếp được liên kết với một con trỏ. Con trỏ này luôn tham chiếu đến vị trí có địa chỉ thấp nhất của khối mà nội dung của nó có thể bị ghi đè. Ban đầu con trỏ tham chiếu đến vị trí đầu tiên của khối.
