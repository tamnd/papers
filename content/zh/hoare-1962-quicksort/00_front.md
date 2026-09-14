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
lang: zh
source: https://www.cs.ox.ac.uk/files/6226/H2006%20-%20Historic%20Quicksort.pdf
pdf_sha256: 1b54e36fac02a0c19213e2858090fa1dca70688f5f99a2748357fd8329918bab
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: d7d900bd21600d6acb2af3e35107777e79a45f5f756b0a897ef5c9e4df34583e
translated_from: content/en/hoare-1962-quicksort/00_front.md
source_content_sha256: 5a2c556e140ce09b780ceded5b579736cdc08e0ccc54fb57bff8095213749a91
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: efacc7653691a9b863e3c4cb746743abfecf7d31e7791764c13a541e1906db0f
prompt_sha256: da0c2696badfbe5d93fdc534847b1b0ca3b25ec37e0ce29843665f6e701c278e
---

快速排序

每次应用划分过程后，会留下两个待排序的段。如果其中任一段为空或只包含一个项，则可以忽略该段，而只继续处理另一个段。此外，如果一个段包含少于三个或四个项（取决于计算机的特性），则采用专门为排序特定少量项而编写的程序对其进行排序会更有利。最后，如果两个段都相当大，则有必要将其中一个段的处理推迟到另一个段完全排序之后。同时，必须存储被推迟段的第一个和最后一个项的地址。节省段详细信息的存储空间非常重要，因为全部段的数量与待排序项的数量成正比。幸运的是，不必同时存储所有段的详细信息，因为已经完全排序的段的详细信息不再需要。

推荐的存储方法利用一个嵌套区，即与指针关联的一组连续存储位置。该指针始终指向其内容可以被覆盖的块中地址最低的位置。最初，该指针指向该块的第一个位置。
