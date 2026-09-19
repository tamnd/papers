---
paper: bayer-1972-btree
title: Organization and Maintenance of Large Ordered Indices
authors:
  - Rudolf Bayer
  - Edward M. McCreight
year: 1972
venue: Acta Informatica
field: databases
section: "10"
section_title: Choice of k
tag: 06FD
kind: section
lang: en
source: https://infolab.usc.edu/csci585/Spring2010/den_ar/indexing.pdf
pdf_sha256: 69826c036d7948fe5b02f7498620c90cc6a8de2504251a57994d13dc7b14e470
pdf_pages: 28-30
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: e92d9ae76d6368a3509c38cfb3cd555ac2e8677c20544c726125586f033c8e29
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The performance of our scheme depends on the parameter k. Thus care should be taken in choosing k to make the performance as good as possible.

To obtain a very rough approximation to the performance of the scheme we make the following assumptions:

i) The time spent for each page which is written or fetched can be expressed in the form:

$$
\alpha + \beta(2k+1) + \gamma \ln(\nu k+1)
$$

$\alpha:$ fixed time spent per page, e.g., average disc seek time plus fixed CPU overhead, etc.

$\beta:$ transfer time per page entry.

$\gamma:$ constant for the logarithmic part of the time, e.g., for a binary search.

$\nu:$ factor for average page occupancy, $1 \leq \nu \leq 2$.

We assume that modifying a page does not require moving keys within a page, but that the necessary channel subcommands are generated to write a page by concatenating several pieces of information in main store. This is the reason for our assumption that fetching and writing a page takes the same time.

i) The average number of pages fetched and written per single transaction in an environment of mixed retrievals, insertions, and deletions is approximately proportional--see Figure 7--to h, say $\delta h$. The total time $T$ spent per transaction can then be approximated by:

$$T \approx \delta h(\alpha+\beta(2k+1)+\gamma \ln(vk+1)).$$

Approximating $h$ itself by:

$$h \approx \log_{vk+1}(I+1)$$

where $I$ is the size of the index, we get:

$$T \approx T_a=\delta\log_{vk+1}(I+1)(\alpha+\beta(2k+1)+\gamma\ln(vk+1))$$

Now one easily obtains the minimum of $T_a$ if $k$ is chosen such that:

$$\frac{\alpha}{\beta}=\frac{2}{v}(vk+1)\ln(vk+1)-(2k+1)=f(k,v)$$

Neglecting CPU time, $k$ is a number which is characteristic for the device used as backup store. To obtain a near optimal page size for our test examples we assumed $\alpha=50$ ms and $\beta=90\ \mu s$. According to the table in Figure 8 an acceptable choice should be $64<k<128$. For reasons of programming convenience we chose $k=60$ resulting in a page size of 120 entries.

Figure 8. The Function $f(k,v)$ for Optimal {#bayer-1972-btree-fig-8 .figure tag=06FE}  
Choice of $k$

The size of the index which can be stored for $k = 60$ in a page tree of a certain height can be seen from Figure 9.

| Height of page tree | Minimum index size | Maximum index size |
| --- | --- | --- |
| 1 | 1 | 120 |
| 2 | 121 | 14640 |
| 3 | 7441 | 1771560 |
| 4 | 453961 | 214358880 |

Figure 9. Height of Page Tree and Index Size {#bayer-1972-btree-fig-9 .figure tag=06FF}
