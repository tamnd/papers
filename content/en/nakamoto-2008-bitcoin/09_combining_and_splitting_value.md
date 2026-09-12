---
paper: nakamoto-2008-bitcoin
title: 'Bitcoin: A Peer-to-Peer Electronic Cash System'
authors:
  - Satoshi Nakamoto
year: 2008
venue: bitcoin.org
field: security
section: "9"
section_title: Combining and Splitting Value
tag: 000D
kind: section
lang: en
source: https://bitcoin.org/bitcoin.pdf
pdf_sha256: b1674191a88ec5cdd733e4240a81803105dc412d6c6708d53ab94fc248f4f553
pdf_pages: "5"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 24dc8e9b7608c4b08b846cf5af6c29faf8471c7a216244f62258919819872b63
edited: true
prompt_sha256: 329630a0b9175a55e4af1b8e281a3e67eeab250f8d643953b7dcde99743c7628
---

Although it would be possible to handle coins individually, it would be unwieldy to make a separate transaction for every cent in a transfer. To allow value to be split and combined, transactions contain multiple inputs and outputs. Normally there will be either a single input from a larger previous transaction or multiple inputs combining smaller amounts, and at most two outputs: one for the payment, and one returning the change, if any, back to the sender.

Figure.
