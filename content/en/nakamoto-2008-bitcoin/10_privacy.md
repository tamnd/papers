---
paper: nakamoto-2008-bitcoin
title: 'Bitcoin: A Peer-to-Peer Electronic Cash System'
authors:
  - Satoshi Nakamoto
year: 2008
venue: bitcoin.org
field: security
section: "10"
section_title: Privacy
tag: 000E
kind: section
lang: en
source: https://bitcoin.org/bitcoin.pdf
pdf_sha256: b1674191a88ec5cdd733e4240a81803105dc412d6c6708d53ab94fc248f4f553
pdf_pages: "6"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: fcf18fc95d7b5e8062201f17a8ed3bd05e4ebe8295f9de6367903cf22aef5f6e
prompt_sha256: 329630a0b9175a55e4af1b8e281a3e67eeab250f8d643953b7dcde99743c7628
---

The traditional banking model achieves a level of privacy by limiting access to information to the parties involved and the trusted third party. The necessity to announce all transactions publicly precludes this method, but privacy can still be maintained by breaking the flow of information in another place: by keeping public keys anonymous. The public can see that someone is sending an amount to someone else, but without information linking the transaction to anyone. This is similar to the level of information released by stock exchanges, where the time and size of individual trades, the "tape", is made public, but without telling who the parties were.

Traditional Privacy Model

Identities → Transactions → Trusted Third Party → Counterparty → Public

New Privacy Model

Identities → Transactions → Public

As an additional firewall, a new key pair should be used for each transaction to keep them from being linked to a common owner. Some linking is still unavoidable with multi-input transactions, which necessarily reveal that their inputs were owned by the same owner. The risk is that if the owner of a key is revealed, linking could reveal other transactions that belonged to the same owner.
