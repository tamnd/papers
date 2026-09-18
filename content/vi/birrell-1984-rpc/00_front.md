---
paper: birrell-1984-rpc
title: Implementing Remote Procedure Calls
authors:
  - Andrew D. Birrell
  - Bruce Jay Nelson
year: 1984
venue: ACM TOCS
field: systems
section_title: Front Matter
tag: "0051"
kind: front
lang: vi
source: https://www.cs.cmu.edu/~dga/15-712/F07/papers/birrell842.pdf
pdf_sha256: 0c5058383786e2b3e8fa9894872358e362a6f6ffc58c06f29dc08b836318f432
pdf_pages: 2-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: faa44c159d78c5a48cf13f3469494eddcb94b1b1ab662655d83958ff3fe65b10
translated_from: content/en/birrell-1984-rpc/00_front.md
source_content_sha256: 443c55fbdd07742a112658c60d65e70a2b25966b03a3fec4d237d8c751d86d25
translation_model: gpt-5
translation_run: 20260918T122832Z
glossary_version: 7
glossary_terms_sha256: f834761938c11bca59f7cb79948997ed0706af48cd70392678452699c034a7ad
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

vẫn tiếp tục thực thi (phụ thuộc vào các chi tiết về tính đồng thời của môi trường đó và việc triển khai RPC).

Có nhiều khía cạnh hấp dẫn của ý tưởng này. Một khía cạnh là ngữ nghĩa sạch và đơn giản: chúng sẽ giúp việc xây dựng các tính toán phân tán trở nên dễ dàng hơn, và giúp thực hiện chúng đúng đắn. Một khía cạnh khác là hiệu quả: các lời gọi thủ tục có vẻ đủ đơn giản để việc giao tiếp có thể diễn ra rất nhanh. Khía cạnh thứ ba là tính tổng quát: trong các tính toán trên một máy đơn, các thủ tục thường là cơ chế quan trọng nhất để giao tiếp giữa các phần của thuật toán.

Ý tưởng về RPC đã tồn tại trong nhiều năm. Nó đã được thảo luận trong các tài liệu công khai nhiều lần kể từ ít nhất là năm 1976 [15]. Luận án tiến sĩ của Nelson [13] là một khảo sát sâu rộng về các khả năng thiết kế cho một hệ thống RPC và có các tài liệu tham khảo đến nhiều công trình trước đó về RPC. Tuy nhiên, các triển khai RPC quy mô đầy đủ hiếm hơn các thiết kế trên giấy. Những nỗ lực đáng chú ý gần đây bao gồm Courier trong họ các giao thức Xerox NS [4], và công việc hiện tại tại MIT [10].

Bài báo này là kết quả từ việc xây dựng một cơ sở RPC cho dự án Cedar. Chúng tôi cho rằng, dựa trên các công trình trước đó (đặc biệt là luận án của Nelson và các thử nghiệm liên quan), chúng tôi đã hiểu được những lựa chọn mà người thiết kế một cơ sở RPC phải đưa ra. Nhiệm vụ của chúng tôi là đưa ra các lựa chọn dựa trên những mục tiêu và môi trường cụ thể của mình. Trong thực tế, chúng tôi nhận thấy rằng một số lĩnh vực chưa được hiểu đầy đủ, và chúng tôi đã tạo ra một hệ thống có thiết kế chứa một số khía cạnh mới lạ.
