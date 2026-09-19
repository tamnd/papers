---
paper: chiu-1989-aimd
title: Analysis of the Increase and Decrease Algorithms for Congestion Avoidance in Computer Networks
authors:
  - Dah-Ming Chiu
  - Raj Jain
year: 1989
venue: Computer Networks and ISDN Systems
field: networks
section: "6"
section_title: Summary of Results
tag: 03D7
kind: section
lang: en
source: https://www.cse.wustl.edu/~jain/papers/cong_av.htm
pdf_sha256: fd0b0386c611744e744969d3c5ec3e236dc6036344128ed16e7f378a9e257be2
pdf_pages: "14"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: bcdb1ef23ce8001e54e63f1e1ff82cc90b4e03fd8992df3d29c3920ea8be360f
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

Congestion avoidance schemes allow a network to operate in the optimal region of low delay and high throughput. This is achieved via the network monitoring its load level and asking the users to increase or decrease the load as appropriate. In this paper, we examined the user increase/decrease policies under the constraints that the feedback from the system is limited to a single bit, which tells whether the current load is above or below the goal.

We formulated a set of conditions that any increase/decrease policy should satisfy to ensure convergence to efficient and fair state in a distributed manner. In particular, we showed that the decrease must be multiplicative to ensure that at every step the fairness either increases or stays the same as that the the current operating point. We derived the sufficient conditions analytically and then explained them using a vector representation.

Optimization considerations require that the change in efficiency and fairness be maximized in every feedback cycle. Using these considerations we showed that additive increase with multiplicative decrease is the optimal policy. This is the policy finally chosen for implementation in the congestion avoidance scheme recommended for Digital Networking Architecture and OSI Transport Class 4 Networks.
