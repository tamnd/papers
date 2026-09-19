---
paper: goldwasser-1984-probabilistic
title: Probabilistic Encryption
authors:
  - Shafi Goldwasser
  - Silvio Micali
year: 1984
venue: Journal of Computer and System Sciences
field: security
section: "7"
section_title: FINAL REMARKS
tag: 07F8
kind: section
lang: en
source: https://people.csail.mit.edu/silvio/Selected%20Scientific%20Papers/Encryption/Probabilistic_Encryption.pdf
pdf_sha256: b3d2f75d09da80c0bc3b39e3001ea3dd782b42af46df9c5bde0741f2dab7aa4a
pdf_pages: 28-29
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: aabf6c03a55888b2c3ca4c38d4cf300803ab1cd33a52e80950d819157c28e1f6
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

### 7.1. *Circuits versus Turing Machines* {#goldwasser-1984-probabilistic-s7-1 .section tag=07F9}

Let $A$ be a user in a public key cryptosystem and $k$ the number of bits in the description of the encryption algorithm $E_A$ put by $A$ in the Public File. Assume one (finally) proves that, for all polynomial time Turing machines $M$, there exists a constant $k_M$, such that for all $k > k_M$, inverting $E_A$ on some message space requires $\Omega(2^{\sqrt{k}})$ steps. As a passive eavesdropper is entitled to choose $M$ after $E_A$ has been put in the public file, what $k$ should $A$ choose?

It is to remove this difficulty that we have chosen circuit complexity as a complexity measure. It should be noticed that such choice is not needed for proving our theorems. Intractability with respect to probabilistic polynomial time Turing machines could have been assumed and all the theorems would have been proved in essentially the same way.

### 7.2. Other Types of Adversaries {#goldwasser-1984-probabilistic-s7-2 .section tag=07FA}

In a public key cryptosystem, getting hold of the cyphertext by eavesdropping and trying, by computing, to decrypt it, is the most obvious attack. However it is not the only one! Goldwasser, Micali, and Tong [9], show how in the Diffie and Hellman model of a public key cryptosystem, an adversary can, being a user, break the security of the scheme by communicating. They proposed a modification of the Diffie and Hellman model and show that the new model is secure against line tappers and even against chosen cyphertext attack.

### 7.3. The Relationship between Shannon’s Perfect Secrecy Definition and Semantic Security {#goldwasser-1984-probabilistic-s7-3 .section tag=07FB}

Let us describe Shannon’s definition of “perfect secrecy” in [23]. Consider an adversary with unlimited time and manpower available for analysis of intercepted cryptograms. Let the set of all possible messages be finite. These messages have a priori probabilities and are encoded and sent across the wire. When an adversary intercepts an encoded message, he can calculate the a posteriori probabilities for the various messages. Perfect secrecy is achieved if for all encoded messages the a posteriori probabilities are equal to the a priori probabilities. Thus intercepting the message gives the adversary no information. In this paper, we defined a polynomially bounded version of Shannon’s perfect secrecy, called semantic security. Semantic security means that when the adversary has only polynomially bounded resources available, intercepting the encoded message gives him no new information. Moreover, there exists no function defined on the message set that the adversary can compute after intercepting the encoded message which he could not compute without intercepting the message. For further discussion see [26].
