---
paper: tomasulo-1967-algorithm
title: An Efficient Algorithm for Exploiting Multiple Arithmetic Units
authors:
  - R. M. Tomasulo
year: 1967
venue: IBM Journal of Research and Development
field: architecture
section_title: Front Matter
tag: "0059"
kind: front
lang: en
source: https://doi.org/10.1147/rd.111.0025
pdf_sha256: b62a6bc6a0b22d9acf08415f9f95f89d6a0b5c9ce46ee9a42563eb9228695be7
pdf_pages: "1"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: f477a5893c0dba3b63e120acb37e18273f7e2218be9f0270412523d1f0e09987
prompt_sha256: 329630a0b9175a55e4af1b8e281a3e67eeab250f8d643953b7dcde99743c7628
---

An Efficient Algorithm for Exploiting Multiple Arithmetic Units

Abstract: This paper describes the methods employed in the floating-point area of the System/360 Model 91 to exploit the existence of multiple execution units. Basic to these techniques is a simple common data busing and register tagging scheme which permits simultaneous execution of independent instructions while preserving the essential precedences inherent in the instruction stream. The common data bus improves performance by efficiently utilizing the execution units without requiring specially optimized code. Instead, the hardware, by 'looking ahead' about eight instructions, automatically optimizes the program execution on a local basis.

The application of these techniques is not limited to floating-point arithmetic or System/360 architecture. It may be used in almost any computer having multiple execution units and one or more 'accumulators.' Both of the execution units, as well as the associated storage buffers, multiple accumulators and input/output buses, are extensively checked.
