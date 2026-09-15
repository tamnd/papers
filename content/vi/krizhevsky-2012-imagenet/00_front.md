---
paper: krizhevsky-2012-imagenet
title: ImageNet Classification with Deep Convolutional Neural Networks
authors:
  - Alex Krizhevsky
  - Ilya Sutskever
  - Geoffrey E. Hinton
year: 2012
venue: NIPS
field: ai-ml
section_title: Front Matter
tag: 01A0
kind: front
lang: vi
source: https://ci.nii.ac.jp/naid/20001617881
pdf_sha256: 90137160c57217953d5f61857e64ca58e85f06e1b13b4f475c918b1b582b9771
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: efadbcb297c96cbd5a84da7b8026edcd9349c6df2dc1b8fc64778a94bfee38ee
translated_from: content/en/krizhevsky-2012-imagenet/00_front.md
source_content_sha256: 6761a061caa974bed1a941937be4fe121ac8195721788db15baa7a4d506c4884
translation_model: gpt-5
translation_run: 20260915T013833Z
glossary_version: 6
glossary_terms_sha256: 0d0a9334a40352952769479a6ad339487dd551fe3d836bae9914ea196d2f4310
prompt_sha256: f4b6a7380aba378d85a09ee39426d3b7de9063306209b1ce511a657e5551eca8
---

Phân loại ImageNet với Mạng nơ-ron Tích chập Sâu

Alex Krizhevsky
University of Toronto
kriz@cs.utoronto.ca

Ilya Sutskever
University of Toronto
ilya@cs.utoronto.ca

Geoffrey E. Hinton
University of Toronto
hinton@cs.utoronto.ca

Tóm tắt

Chúng tôi đã huấn luyện một mạng nơ-ron tích chập sâu, lớn để phân loại 1.2 triệu ảnh độ phân giải cao trong cuộc thi ImageNet LSVRC-2010 thành 1000 lớp khác nhau. Trên dữ liệu kiểm thử, chúng tôi đạt được tỷ lệ lỗi top-1 và top-5 lần lượt là 37.5% và 17.0%, tốt hơn đáng kể so với trạng thái hiện đại trước đó. Mạng nơ-ron, có 60 triệu tham số và 650,000 nơ-ron, bao gồm năm lớp tích chập, một số lớp trong đó được theo sau bởi các lớp max-pooling, và ba lớp kết nối đầy đủ với softmax 1000 chiều cuối cùng. Để làm cho quá trình huấn luyện nhanh hơn, chúng tôi sử dụng các nơ-ron không bão hòa và một triển khai GPU rất hiệu quả của phép toán tích chập. Để giảm hiện tượng quá khớp trong các lớp kết nối đầy đủ, chúng tôi sử dụng một phương pháp chính quy hóa được phát triển gần đây có tên là “dropout”, phương pháp này đã chứng minh là rất hiệu quả. Chúng tôi cũng đưa một biến thể của mô hình này tham gia cuộc thi ILSVRC-2012 và đạt được tỷ lệ lỗi kiểm thử top-5 chiến thắng là 15.3%, so với 26.2% đạt được bởi bài dự thi đứng thứ hai.
