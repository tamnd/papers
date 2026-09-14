---
paper: hamming-1950-codes
title: Error Detecting and Error Correcting Codes
authors:
  - Richard W. Hamming
year: 1950
venue: Bell System Technical Journal
field: theory
section_title: Front Matter
tag: "0036"
kind: front
lang: zh
source: https://archive.org/download/bstj29-2-147/bstj29-2-147.pdf
pdf_sha256: 32f13768d0e37bcc482517d3e1f50f9309d6db65e145edc476622c435829bdad
pdf_pages: 1-3
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 6dc8d4f77055c262dba66e91c28fba4f1b5fac868184a03adc30f8ffeae54939
translated_from: content/en/hamming-1950-codes/00_front.md
source_content_sha256: 971d65afaa79d5bb3cdb5a51fe6f8e1e8c181d48d9030e299fd3fe9b93bfa1a9
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: fdb843fdc63f5c3983beed236d73d0b32777dbad1ce40750adddaf64213e5d33
prompt_sha256: da0c2696badfbe5d93fdc534847b1b0ca3b25ec37e0ce29843665f6e701c278e
---

错误检测与纠错码

R. W. HAMMING 著

1. 引言

本文的研究源于对大规模计算机的思考。在这类计算机中，必须执行大量操作，而最终结果不能出现任何错误。这种大规模“把事情做对”的问题并非全新问题。例如，在电话交换局中，虽然导致号码错误的故障尚未完全消除，但大量操作得以执行，且这类故障得到了很好的控制。这部分得益于自检电路的使用。偶尔逃过常规检查的故障仍会被用户发现；如果故障持续存在，就会引起用户投诉，而如果故障是暂时性的，则只会偶尔产生错误号码。与此同时，交换局的其他功能仍能正常运行。另一方面，在数字计算机中，单个故障通常意味着整个系统的失效。也就是说，如果故障被检测出来，在定位并纠正故障之前，计算机将无法继续进行计算；而如果故障未被检测出来，那么它就会使计算机随后执行的所有操作失效。
