---
paper: karp-1972-reducibility
title: Reducibility Among Combinatorial Problems
authors:
  - Richard M. Karp
year: 1972
venue: Complexity of Computer Computations
field: theory
section_title: Front Matter
tag: 003A
kind: front
lang: zh
source: https://doi.org/10.1007/978-1-4684-2001-2_9
pdf_sha256: ae57cf641ae4f1924bdc4d7ef865edb2411c44e3040e8e546d01f1545e288e89
pdf_pages: 1-2
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 3c6a737c488e1d097734e0375fad9ccd6f5af2b893a57b8024709aa7df2f51df
translated_from: content/en/karp-1972-reducibility/00_front.md
source_content_sha256: c04b8bbc6c2a7aebbe904b3efaa08d0fc2f24fa6d7276ff92ca2ec383b049ad8
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: fdb843fdc63f5c3983beed236d73d0b32777dbad1ce40750adddaf64213e5d33
prompt_sha256: da0c2696badfbe5d93fdc534847b1b0ca3b25ec37e0ce29843665f6e701c278e
---

组合问题之间的可归约性

Richard M. Karp

Richard M. Karp 的引言

整个20世纪60年代，我一直研究组合优化问题，包括与 Paul Roth 合作的逻辑电路设计、与 Mike Held 合作的装配线平衡问题和旅行商问题。这些经历使我意识到，看似简单的离散优化问题可能蕴含着组合爆炸的根源。Dantzig、Fulkerson、Hoffman、Edmonds、Lawler 以及其他先驱者在网络流、匹配和拟阵方面的工作，使我了解了有时可能实现的优雅而高效的算法。Jack Edmonds 的论文以及与他的几次关键讨论，使我注意到多项式时间可解性和超多项式时间可解性之间的关键区别。我还受到 Jack 对极小极大定理的强调所影响，他将其作为快速验证最优解的工具，而这一思想预示了 Steve Cook 对复杂度类 NP 的定义。另一个影响因素是 George Dantzig 提出的建议，即整数规划可以作为组合优化问题的通用形式。

整个60年代，我关注由 Rabin、Blum、Hartmanis、Stearns 以及其他人开创的计算复杂度理论的发展。在60年代末，我在布鲁克林理工学院教授一门关于该主题的课程时，研读了 Hartley Rogers 关于递归函数理论的精彩著作。这段经历使我深刻认识到可归约性在递归函数理论中的关键作用，并开始思考子递归可归约性是否能够在复杂度理论中发挥类似作用，但我当时还没有进一步研究这一类比。
