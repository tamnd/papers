---
paper: nakamoto-2008-bitcoin
title: 'Bitcoin: A Peer-to-Peer Electronic Cash System'
authors:
  - Satoshi Nakamoto
year: 2008
venue: bitcoin.org
field: security
section: "7"
section_title: Thu hồi dung lượng đĩa
tag: 000B
kind: section
lang: vi
source: https://bitcoin.org/bitcoin.pdf
pdf_sha256: b1674191a88ec5cdd733e4240a81803105dc412d6c6708d53ab94fc248f4f553
pdf_pages: "4"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: f4b4d4c5cbafd9709aa2ae33f3bedbb693053463351a8a41c08cce69ac954d97
translated_from: content/en/nakamoto-2008-bitcoin/07_reclaiming_disk_space.md
source_content_sha256: 8150cb6dc79c1e1dae5701749af8c1654684cc9b1fbfd20d88497f3026799bc7
translation_model: gpt-6-astra
translation_run: 20260915T022520Z
glossary_version: 6
glossary_terms_sha256: 363c21723d588ca6b8032fd3e2b0aa8dc6ab225b1f9ca1b6e98d75976e8b0d0a
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Khi giao dịch mới nhất của một đồng tiền đã được chôn dưới đủ số khối, các giao dịch đã chi tiêu trước đó có thể được loại bỏ để tiết kiệm dung lượng đĩa. Để thực hiện việc này mà không làm thay đổi giá trị băm của khối, các giao dịch được băm trong một cây Merkle (Merkle Tree) [7][2][5], trong đó chỉ có gốc cây được đưa vào phép băm của khối. Khi đó, các khối cũ có thể được thu gọn bằng cách cắt bỏ các nhánh của cây. Không cần lưu trữ các giá trị băm bên trong cây.

Các giao dịch được băm trong một cây Merkle

Sau khi cắt tỉa Tx0-2 khỏi khối

Phần đầu của một khối không chứa giao dịch sẽ có kích thước khoảng 80 byte. Nếu giả sử các khối được tạo mỗi 10 phút, thì 80 byte * 6 * 24 * 365 = 4.2MB mỗi năm. Với các hệ thống máy tính thường được bán kèm 2GB RAM vào năm 2008, và định luật Moore dự đoán mức tăng hiện tại là 1.2GB mỗi năm, việc lưu trữ sẽ không phải là vấn đề ngay cả khi các phần đầu khối phải được giữ trong bộ nhớ.
