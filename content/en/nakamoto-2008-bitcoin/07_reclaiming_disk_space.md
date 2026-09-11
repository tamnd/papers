---
paper: nakamoto-2008-bitcoin
title: 'Bitcoin: A Peer-to-Peer Electronic Cash System'
authors:
  - Satoshi Nakamoto
year: 2008
venue: bitcoin.org
field: security
section: "7"
section_title: Reclaiming Disk Space
kind: section
lang: en
source: https://bitcoin.org/bitcoin.pdf
pdf_sha256: b1674191a88ec5cdd733e4240a81803105dc412d6c6708d53ab94fc248f4f553
pdf_pages: "4"
extraction: native
content_sha256: ed9204e29200507f1b4024d352c1a755139ccbc3ca67bf65afdcbe7317f36bfa
---

Once the latest transaction in a coin is buried under enough blocks, the spent transactions before it can be discarded to save disk space. To facilitate this without breaking the block's hash, transactions are hashed in a Merkle Tree [7][2][5], with only the root included in the block's hash. Old blocks can then be compacted by stubbing off branches of the tree. The interior hashes do not need to be stored.

Block Block

Block Header (Block Hash) Block Header (Block Hash)

Prev Hash Nonce Prev Hash Nonce

Root Hash Root Hash

Hash01 Hash23 Hash01 Hash23

Hash0 Hash1 Hash2 Hash3 Hash2 Hash3

Tx0 Tx1 Tx2 Tx3 Tx3

Transactions Hashed in a Merkle Tree After Pruning Tx0-2 from the Block

A block header with no transactions would be about 80 bytes. If we suppose blocks are generated every 10 minutes, 80 bytes * 6 * 24 * 365 = 4.2MB per year. With computer systems typically selling with 2GB of RAM as of 2008, and Moore's Law predicting current growth of 1.2GB per year, storage should not be a problem even if the block headers must be kept in memory.
