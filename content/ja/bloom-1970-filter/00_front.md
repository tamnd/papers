---
paper: bloom-1970-filter
title: Space/Time Trade-offs in Hash Coding with Allowable Errors
authors:
  - Burton H. Bloom
year: 1970
venue: Communications of the ACM
field: algorithms
section_title: Front Matter
tag: "0041"
kind: front
lang: ja
source: http://crystal.uta.edu/~mcguigan/cse6350/papers/Bloom.pdf
pdf_sha256: def80c7d042c39d5aab15e6ae1c2b55262ee1123ffcdf53143895089ab5c1728
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 5bf0bd31797cae01a2749b3c6d609286a652c516ccecea88a5d1d47f2a2e9e1a
translated_from: content/en/bloom-1970-filter/00_front.md
source_content_sha256: 6e3e5001e35618a95d7390add14305bc048634f4195f7b3026a34d8a0cf633d5
translation_model: gpt-5
translation_run: 20260914T102340Z
glossary_version: 6
glossary_terms_sha256: 81be60ea3284bdc3129ecda2524a99e799d0b3ec06fd0a74a1fb3922eda78382
prompt_sha256: 28abc9ae7c2a46d63213afc528700760d76ff5866e775238c90c95b3052a886f
---

許容誤りを伴うハッシュ符号化における空間／時間のトレードオフ

BURTON H. BLOOM

Computer Usage Company, Newton Upper Falls, Mass.

本論文では、ハッシュ符号化におけるいくつかの計算上の要因間のトレードオフを分析する。検討する典型的な問題は、メッセージの所与の集合への所属を、一連のメッセージについて一つずつ検査することである。2つの新しいハッシュ符号化法を検討し、特定の従来型ハッシュ符号化法と比較する。考慮する計算上の要因は、ハッシュ領域の大きさ（空間）、メッセージが所与の集合の非所属要素であることを識別するために必要な時間（拒否時間）、および許容可能な誤り頻度である。

新しい方法は、従来の方法に伴うものよりも、ハッシュ符号化された情報を格納するために必要な空間量を削減することを目的としている。空間の削減は、いくつかの応用では、誤って所属と判定する誤りのごく一部が許容され得る可能性を利用することによって達成される。特に、大量のデータを扱い、そのため従来の方法ではコア常駐のハッシュ領域が現実的でない応用が対象となる。

このような応用では、新しい方法と併用してより小さいコア常駐のハッシュ領域を使用し、必要に応じて、時間を要する可能性のある何らかの二次的な検査を行って、新しい方法に伴う誤りのごく一部を「捕捉」することにより、全体的な性能を向上できると考えられる。新しい方法の応用可能な領域を示す例についても論じる。
