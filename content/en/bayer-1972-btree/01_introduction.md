---
paper: bayer-1972-btree
title: Organization and Maintenance of Large Ordered Indices
authors:
  - Rudolf Bayer
  - Edward M. McCreight
year: 1972
venue: Acta Informatica
field: databases
section: "1"
section_title: Introduction
tag: 06EC
kind: section
lang: en
source: https://infolab.usc.edu/csci585/Spring2010/den_ar/indexing.pdf
pdf_sha256: 69826c036d7948fe5b02f7498620c90cc6a8de2504251a57994d13dc7b14e470
pdf_pages: 3-5
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: d6f7dcfebf61f0ab7aa758aab34f9bd1fec51d1146468b23e071339adb46313c
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

In this paper we consider the problem of organizing and maintaining an index for a dynamically changing random access file. By an index we mean a collection of index elements which are pairs $(x, \alpha)$ of fixed size physically adjacent data items, namely a key $x$ and some associated information $\alpha$. The key $x$ identifies a unique element in the index, the associated information is typically a pointer to a record or a collection of records in a random access file. For this paper the associated information is of no further interest.

We assume that the index itself is so voluminous that only rather small parts of it can be kept in main store at one time. Thus the bulk of the index must be kept on some backup store. The class of backup stores considered are pseudo random access devices which have a rather long access or wait time—as opposed to a true random access device like core store—and a rather high data rate once the transmission of physically sequential data has been initiated. Typical pseudo random access devices are: fixed and moving head discs, drums, and data cells.

Since the data file itself changes, it must be possible not only to search the index and to retrieve elements, but also to delete and to insert keys—more accurately index elements—economically. The index organization described in this paper always allows retrieval, insertion, and deletion of keys in time proportional to $\log_k I$ or better, where $I$ is the size of the index, and $k$ is a device dependent natural number which describes the page size such that the performance of the maintenance and retrieval scheme becomes near optimal.

In more illustrative terms theoretical analysis and actual experiments show that it is possible to maintain an index of size 15000 with an average of 9 retrievals, insertions, and deletions per second in real time on an IBM 360/44 with a 2311 disc as backup store. According to our theoretical analysis, it should be possible to maintain an index of size 1500000 with at least two transactions per second on such a configuration in real time.

The index is organized in pages of fixed size capable of holding up to 2k keys, but pages need only be partially filled. Pages are the blocks of information transferred between main store and backup store.

The pages themselves are the nodes of a rather specialized tree, a so-called B-tree, described in the next section. In this paper these trees grow and contract in only one way, namely nodes split off a brother, or two brothers are merged or "catenated" into a single node. The splitting and catenation processes are initiated at the leaves only and propagate toward the root. If the root node splits, a new root must be introduced, and this is the only way in which the height of the tree can increase. The opposite process occurs if the tree contracts.

There are, of course, many competitive schemes, e.g., hash-coding, for organizing an index. For a large class of applications the scheme presented in this paper offers significant advantages over others:

i) Storage utilization is at least 50% at any time and should be considerably better in the average.

ii) Storage is requested and released as the file grows and contracts. There is no congestion problem or degradation of performance if the storage occupancy is very high.

iii) The natural order of the keys is maintained and allows processing based on that order like: find predecessors and successors; search the file sequentially to answer queries; skip, delete, retrieve a number of records starting from a given key.

iv) If retrievals, insertions, and deletions come in batches, very efficient essentially sequential processing of the index is possible by presorting the transactions on their keys and by using a simple prepaging algorithm.
