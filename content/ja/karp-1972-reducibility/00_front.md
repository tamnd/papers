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
lang: ja
source: https://doi.org/10.1007/978-1-4684-2001-2_9
pdf_sha256: ae57cf641ae4f1924bdc4d7ef865edb2411c44e3040e8e546d01f1545e288e89
pdf_pages: 1-2
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 63a178f85e8c158968e15202ea61fbc734cd66341eadcca7fa132cf8e6d53692
translated_from: content/en/karp-1972-reducibility/00_front.md
source_content_sha256: c04b8bbc6c2a7aebbe904b3efaa08d0fc2f24fa6d7276ff92ca2ec383b049ad8
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: 662cf3e117a3c08b920782dc2794cfa66d7ab8088f30ff6229b6cca3ba0e4897
prompt_sha256: 28abc9ae7c2a46d63213afc528700760d76ff5866e775238c90c95b3052a886f
---

組合せ問題間の還元可能性

Richard M. Karp

Richard M. Karpによる序論

1960年代を通じて、Paul Rothと論理回路設計を、Mike Heldと組立ラインのバランシングおよび巡回セールスマン問題を含む、組合せ最適化問題に取り組んだ。これらの経験から、一見単純な離散最適化問題が、組合せ爆発の種を内包し得ることを認識した。Dantzig、Fulkerson、Hoffman、Edmonds、Lawlerおよびその他の先駆者たちによるネットワークフロー、マッチング、マトロイドの研究を通じて、ときに可能であった洗練された効率的なアルゴリズムに触れた。Jack Edmondsの論文と彼とのいくつかの重要な議論によって、多項式時間での解決可能性と超多項式時間での解決可能性の間にある決定的な相違に注意を向けるようになった。また、最適解を迅速に検証する手段としてのmin-max定理を重視するJackの姿勢にも影響を受けた。これは、Steve Cookによる計算量クラスNPの定義を予示するものであった。もう一つの影響は、整数計画法が組合せ最適化問題のための普遍的な形式として役立ち得るというGeorge Dantzigの提案であった。

1960年代を通じて、Rabin、Blum、Hartmanis、Stearnsらが先導した計算量理論の発展を追っていた。1960年代後半には、ブルックリン工科大学で再帰関数理論の講義を担当しながら、Hartley Rogersの美しい著書を学んだ。この経験によって、再帰関数理論における還元可能性が果たす中心的な役割を深く認識し、部分再帰的還元可能性が計算量理論においても同様の役割を果たし得るのではないかと考え始めたが、当時はまだその類推を追究していなかった。
