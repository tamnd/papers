---
paper: dennard-1974-scaling
title: Design of Ion-Implanted MOSFET's with Very Small Physical Dimensions
authors:
  - Robert H. Dennard
  - Fritz H. Gaensslen
  - Hwa-Nien Yu
  - V. Leo Rideout
  - Ernest Bassous
  - Andre R. LeBlanc
year: 1974
venue: IEEE Journal of Solid-State Circuits
field: architecture
section_title: Characteristics of the Zero Substrate Bias Design
kind: section
lang: en
source: https://doi.org/10.1109/jssc.1974.1050511
pdf_sha256: fe83e914e79d8bf4271ea55de8f78a47a254fd7093a7ab073b80f956089d5690
pdf_pages: "9"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 1fb76be228957b23774188af0436b12ab3b9b3fbde277b6adc3373b45abdb551
prompt_sha256: c5c47cae65ffa93ca979b448f43adf142f13a9820bcd1d77a3ff1aa1babe667b
---

Since the last design shown in Fig. 10(e) appears to be better behaved in terms of short-channel effects, it is worthwhile to review its properties more fully. Experimental devices corresponding to this design were built and tested with various channel lengths. In this case a 20 keV, $6.0 \times 10^{11}$ atoms/cm$^2$ B$^{11}$ implant was used to obtain a shallower implanted layer of approximately 1000-$\AA$ depth [11]. Data on threshold voltage for these devices with 4 V applied to the drain is presented in Fig. 11 and corresponds very well to the calculated values. Data for a small drain voltage is also given in this figure, showing much less variation of threshold with channel length, as expected. The dependence of threshold voltage on source-to-substrate bias is shown in Fig. 12 for different values of $L$. The drain-to-source voltage was held at a constant low value for this measurement. The results show that the substrate sensitivity is indeed about the same for this design with zero substrate bias as for the original design with $V_{sub} = -1$ V. Note that the smaller devices show a somewhat flatter substrate sensitivity characteristic with relatively lower thresholds at high values of source (and drain) voltage.

The turn-on characteristics for the zero substrate bias design, both experimental and calculated, are shown in Fig. 13 for different values of $L$. The relatively small shift in threshold for the short-channel devices is evident; however, the turn-on rate is considerably slower for this case than for the $V_{sub} = -1$ V case shown in Fig. 7. This is due to the fact that the depletion region in the silicon under the gate is very shallow for this zero substrate bias case so that a large portion of a given gate voltage change is dropped across the gate insulator capacitance rather than across the silicon depletion layer capacitance. This is discussed in some detail for these devices in another paper [11]. The consequence for dynamic memory applications is that, even though the zero substrate bias design offers improved threshold control for strong inversion, this advantage is offset by the flatter subthreshold turn-on characteristic. For such applications the noise margin with the turn-on characteristic of Fig. 13 is barely suitable if the device is turned off by bringing its gate to ground. Furthermore, elevated temperature aggravates the situation [18]. Thus, for dynamic memory, the basic design with $V_{sub} = -1$ V presented earlier is preferred.
