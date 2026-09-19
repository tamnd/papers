---
paper: chiu-1989-aimd
title: Analysis of the Increase and Decrease Algorithms for Congestion Avoidance in Computer Networks
authors:
  - Dah-Ming Chiu
  - Raj Jain
year: 1989
venue: Computer Networks and ISDN Systems
field: networks
section: "5"
section_title: Practical Considerations
tag: 03D5
kind: section
lang: en
source: https://www.cse.wustl.edu/~jain/papers/cong_av.htm
pdf_sha256: fd0b0386c611744e744969d3c5ec3e236dc6036344128ed16e7f378a9e257be2
pdf_pages: 13-14
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 280988fe133dd98e397123104295376dab0bdb248b228afc0f620dab806c155b
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The problem studied in this report is a generic, but also highly abstracted problem. In order to apply the results to solve the decentralized congestion control problem in real networks, many practical issues must be taken into considerations. We briefly discuss some of them here.

One general principle in choosing an algorithm in a general architecture is to be independent of hardware and software scales or parameters as much as possible. The reason being that in a complex system, scaling parameters are not easily gathered in an automatic fashion and, thus, require human help to configure. Having algorithms depend on system scales would complicate the configuration task and make the algorithm more vulnerable to human error. While in this report we have discussed optimizing the control scheme according to certain criteria, practical consideration may dictate that the control be chosen for the widest range of values of system parameters. As we indicated earlier, the nonlinear controls tend to be more sensitive to the system parameters and, thus, are less likely to be useful in practice.

Another possible constraint is that the resource and thus the allocations must be integral. For example buffers and windows are all measured in integers. Simple rounding off to the nearest integer may cause violation of the various convergence conditions.

Ease of implementation could also affect the choice of the controls. For example, the number of multiplications or exponentiations required to implement a control would impact on the minimal hardware required.

### 5.1. Further Questions {#chiu-1989-aimd-s5-1 .section tag=03D6}

There are many further questions worth exploring in conjunction to this problem. In particular, the following are important:

(1) How does delayed feedback affect the control? In practice there is invariably some delays before the feedback arrives at the controller. As the delay lengthens, the feedback becomes less and less useful, and the performance worsens. It would be valuable to have quantitative assessment of how the performance degrades.

(2) What is the marginal utility of increased bits of feedback? The binary feedback is the simplest. Adding additional feedback signals may help to cut down the oscillations. A formal analysis would allow an assessment of the tradeoff of performance versus complexity.

(3) Is it worthwhile to guess the current number of users n? Users come and go dynamically and the number changes by integral values. A sequence of increase signals may indicate the reduction in the number of users from n to n - 1. If n were known or bounded, sources could predict n - 1 and request that level of resources right away. A wrong guess may make the system less stable. This also deserves further study.

(4) What is the impact of asynchronous operation? The algorithm described in the paper is intrinsically a synchronous algorithm. In other words, it is assumed that all users start from an initial state and follow through common phases of computation and feedback. When the frequency of feedback is different or when the time delay of feedback is drastically different, then the convergence properties cannot be guaranteed. This topic is currently under further study.
