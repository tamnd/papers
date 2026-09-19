---
paper: bayer-1972-btree
title: Organization and Maintenance of Large Ordered Indices
authors:
  - Rudolf Bayer
  - Edward M. McCreight
year: 1972
venue: Acta Informatica
field: databases
section: "5"
section_title: Cost of Retrievals and Insertions
tag: 06F6
kind: section
lang: en
source: https://infolab.usc.edu/csci585/Spring2010/den_ar/indexing.pdf
pdf_sha256: 69826c036d7948fe5b02f7498620c90cc6a8de2504251a57994d13dc7b14e470
pdf_pages: 15-16
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: a3bec35046ad4998b17f7a24d05a0eb63acd939a720bc38a208cdcf0fbf53639
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

To analyze the cost of maintaining an index and retrieving keys we need to know how many pages must be fetched from the backup store into main store and how many pages must be written onto the backup store. For our analysis we make the following assumption: Any page, whose content is examined or modified during a single retrieval, insertion, or deletion of a key, is fetched or paged out respectively exactly once. It will become clear during the course of this paper that a paging area to hold h + 1 pages in main store is sufficient to do this.

Any more powerful paging scheme, like, e.g., keeping the root page permanently locked in main store, will, of course, decrease the number of pages which must be fetched or paged out. We will not, however, analyze such schemes, although we have used them in our experiments.

Denote by $f_{\min}$ ($f_{\max}$) the minimal (maximal) number of pages fetched, and by $w_{\min}$ ($w_{\max}$) the minimal (maximal) number of pages written.

Cost of Retrieval: From the retrieval algorithm it is clear that for retrieving a single key we get

$$
f_{\min} = 1; \quad f_{\max} = h; \quad w_{\min} = w_{\max} = 0;
$$

Cost of Insertion: For inserting a single key the least work is required if no page splitting occurs, then

$$
f_{\min} = h; \quad w_{\min} = 1;
$$

Most work is required if all pages in the retrieval path including the root page split into two. Since the retrieval path contains h pages and we have to write a new root page, we get:

$$
f_{\max} = h; \quad w_{\max} = 2h + 1
$$

Note that h always denotes the height of the old tree. Although this worst bound is sharp, it is not a good measure for the amount of work which must generally be done for inserting one key.

If we consider an index in which keys are only retrieved or inserted, but no keys are deleted, then we can derive a bound for the average amount of work to be done for building an index of I keys as follows:

Each page split causes one (or two if the root page splits) new pages to be created. Thus the number of page splits occurring in building an index of I items is bounded by n(I) - 1, where n(I) is the number of pages in the tree. Since each page has at least k keys, except the root page which may have only 1, we get: $n(I) \leq \frac{I - 1}{k} + 1$. Each single page split causes at most 2 additional pages to be written. Thus the average number of pages written per single key insertion due to page splitting is bounded by

$$
(n(I) - 1) \cdot \frac{2}{I} < \frac{2}{k}
$$

A page split does not require any additional page retrievals. Thus in the average for an index without deletions we get for a single insertion:

$$
f_a = h; \quad w_a < 1 + \frac{2}{k}
$$
