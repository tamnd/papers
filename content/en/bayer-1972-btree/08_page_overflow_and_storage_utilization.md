---
paper: bayer-1972-btree
title: Organization and Maintenance of Large Ordered Indices
authors:
  - Rudolf Bayer
  - Edward M. McCreight
year: 1972
venue: Acta Informatica
field: databases
section: "8"
section_title: Page Overflow and Storage Utilization
tag: 06FA
kind: section
lang: en
source: https://infolab.usc.edu/csci585/Spring2010/den_ar/indexing.pdf
pdf_sha256: 69826c036d7948fe5b02f7498620c90cc6a8de2504251a57994d13dc7b14e470
pdf_pages: 22-23
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 1da85218964aab6bf3cc6b66f97f8b50e17dbc0ca828fd5676af7cc8e281247e
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In the scheme described so far utilization of back-up store may be as low as 50% in extreme cases--disregarding the root page--if all pages contain only k keys. This could be improved by avoiding certain page splits.

An overflow between two adjacent brother pages P and P' can be performed as follows: Assume that a key must be inserted in P and P is already full, but P' is not full. Then the key is inserted into the key-sequence in P' and an underflow as described in Section 6 between the resulting sequence and P' is performed. This avoids the need to split P into two pages. Thus a page will be split only if both adjacent brothers are full, otherwise an overflow occurs.

In an index without deletions overflows will increase the storage utilization in the worst cases to about 66%. If both insertions and deletions occur, then the storage utilization may of course again be as low as 50%. For most practical applications, however, storage utilization should be improved appreciably with overflows.

One could, of course, consider a larger neighborhood of pages than just the adjacent brothers as candidates for overflows, underflows, and catenations and increase the minimal storage occupancy accordingly.

Bounds for the cost of insertions for a scheme with overflows are easily derived as:

$$
f_{\min} = h; \quad w_{\min} = 1;
$$

$$
f_{\max} = 3h - 2; \quad w_{\max} = 2h + 1
$$

For a pure insertion process one obtains as bounds for the average cost:

$$
f_a < h + 2 + \frac{2}{k}; \quad w_a < 3 + \frac{2}{k}.
$$

It is easy to construct examples in which each insertion causes an overflow, thus these bounds cannot be improved very much without special assumptions about the insertion process.
