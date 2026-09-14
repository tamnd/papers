---
paper: cooley-1965-fft
title: An Algorithm for the Machine Calculation of Complex Fourier Series
authors:
  - James W. Cooley
  - John W. Tukey
year: 1965
venue: Mathematics of Computation
field: algorithms
section_title: Front Matter
tag: "0040"
kind: front
lang: vi
source: https://doi.org/10.1090/s0025-5718-1965-0178586-1
pdf_sha256: b4fa04410bcbf324eca035ab9d94818f075cee2f2ae38e99ebb0e2348e64654a
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: a9a44bef70221f10e26ad660757f58c344fe559cd0c6d7be2c6db1f12957dbdf
translated_from: content/en/cooley-1965-fft/00_front.md
source_content_sha256: 75f827c0ac01a12a53f6f7d8ac49df10329caa98952de96c18f1d44bf14b5a54
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: 51f62d367854beec600f51894702ad34dfcde96c993d5c00a2f7a9873047d13f
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
roundtrip: same
roundtrip_run: 20260914T214350Z
---

Một Thuật toán cho Việc Tính toán bằng Máy của Chuỗi Fourier Phức

Bởi James W. Cooley và John W. Tukey

Một phương pháp hiệu quả để tính toán các tương tác của một thí nghiệm giai thừa $2^m$ đã được Yates đưa ra và được biết rộng rãi theo tên của ông. Sự tổng quát hóa cho $3^m$ được Box và cộng sự đưa ra [1]. Good [2] đã tổng quát hóa các phương pháp này và đưa ra các thuật toán thanh lịch, trong đó một lớp ứng dụng là việc tính toán các chuỗi Fourier. Ở dạng tổng quát đầy đủ, các phương pháp của Good có thể áp dụng cho một số bài toán trong đó cần nhân một vectơ $N$ với một ma trận $N \times N$ có thể được phân tích thành $m$ ma trận thưa, trong đó $m$ tỷ lệ với $\log N$. Điều này dẫn đến một thủ tục yêu cầu số lượng phép toán tỷ lệ với $N \log N$ thay vì $N^2$. Các phương pháp này được áp dụng ở đây để tính toán các chuỗi Fourier phức. Chúng hữu ích trong các tình huống mà số lượng điểm dữ liệu là, hoặc có thể được chọn là, một số có tính hợp thành cao. Thuật toán được suy ra và trình bày ở đây dưới một dạng khá khác biệt. Sự chú ý được dành cho việc lựa chọn $N$. Cũng chỉ ra rằng có thể thu được lợi thế đặc biệt khi sử dụng một máy tính nhị phân với $N = 2^m$ và toàn bộ phép tính có thể được thực hiện bên trong mảng gồm $N$ vị trí lưu trữ dữ liệu được sử dụng cho các hệ số Fourier đã cho.

Xét bài toán tính toán chuỗi Fourier phức
