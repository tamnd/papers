---
paper: amdahl-1967-law
title: Validity of the Single Processor Approach to Achieving Large Scale Computing Capabilities
authors:
  - Gene M. Amdahl
year: 1967
venue: AFIPS Spring Joint Computer Conference
field: architecture
section_title: Front Matter
tag: "0003"
kind: front
lang: zh
source: https://www3.cs.stonybrook.edu/~rezaul/Spring-2012/CSE613/reading/Amdahl-1967.pdf
pdf_sha256: 81a363deb884ca23e495280eb9229df1064b4b3f79d662f270be35b50bea5318
pdf_pages: "1"
extraction: native
extraction_model: pdftotext version 26.09.0
content_sha256: a5d3eb78fdaa584a8a1f0093a94b459d03dfe3997f32e362a3f49a221198ddf3
translated_from: content/en/amdahl-1967-law/00_front.md
source_content_sha256: 171773ab6985277014edc3cd9c8194b6f319c68c97b5f19c7035fd7df73aebc8
translation_model: gpt-5
translation_run: 20260915T020405Z
glossary_version: 6
glossary_terms_sha256: f2cc5b0eefe7b06d94615a8f7e8f16341f179359e9a5d34f12553ab545a2c59c
prompt_sha256: da0c2696badfbe5d93fdc534847b1b0ca3b25ec37e0ce29843665f6e701c278e
---

单处理器方法在实现大规模计算能力方面的有效性

实现大规模计算能力

转载自《AFIPS Conference Proceedings》，第30卷（Atlantic City, N.J., Apr. 18–20），AFIPS Press，Reston, Va., 1967年，第483–485页，当时Amdahl博士任职于International

Business Machines Corporation，Sunnyvale, California

Gene M. Amdahl博士

本文是Gene Amdahl首次发表关于后来被称为阿姆达尔定律的研究成果。有趣的是，本文没有任何方程，只有一幅图。对于本期《SSCS News》，Amdahl博士同意重新绘制该图。在现有的纸质版本中，该图无法辨认。我们刊印这篇历史性论文，使会员能够阅读约40年前的原始文献。

编者

十多年来，一些预言家一直认为，单台计算机的组织形式已经达到极限，真正重大的进步只能通过将多台计算机互连起来，以实现协同求解。人们提出的适当方向各不相同：一种是具有通用化内存互连的通用计算机，另一种是具有几何相关内存互连、并由一个或多个指令流控制的专用计算机。

本文论证了单处理器方法持续存在的有效性，以及多处理器方法在应用于实际问题及其伴随的不规则性时所存在的弱点。
