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
section_title: Appendix
kind: appendix
lang: en
source: https://doi.org/10.1109/jssc.1974.1050511
pdf_sha256: fe83e914e79d8bf4271ea55de8f78a47a254fd7093a7ab073b80f956089d5690
pdf_pages: 11-12
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: a369c207f7d5f40702cd07ab6106a216670f8ef63e30783e13f419ad069cf825
prompt_sha256: c5c47cae65ffa93ca979b448f43adf142f13a9820bcd1d77a3ff1aa1babe667b
---

EXPERIMENTAL DETERMINATION OF CHANNEL LENGTH

A technique for determining the effective electrical channel length $L$ for very small MOSFET's from experimental data is described here. The technique is based

Figure.

on the observation that

$$
WR_{chan} = L \rho_{chan}
$$

where $R_{chan}$ is the channel resistance, and $\rho_{chan}$ the sheet resistance of the channel. For a fixed value of $V_g - V_t > 0$, and with the device turned on in the below-pinchoff region, the channel sheet resistance is relatively independent of $L$. Then, a plot of $WR_{chan}$ versus $L_{mask}$ will intercept the $L_{mask}$ axis at $\Delta L$ because $\Delta L = L_{mask} - L$, where $\Delta L$ is the processing reduction in the mask dimension due to exposure and etching. An example of this technique is illustrated in Fig. 14.

The experimental values of $W$ and $R_{chan}$ used in Fig. 14 were obtained as follows. First, the sheet resistance of the ion-implanted n+ region was determined using a relatively large four-point probe structure. Knowing the n+ sheet resistance allows us to compute the source and drain resistance $R_s$ and $R_d$, and to deduce $W$ from the resistance of a long, slender, n+ line. The channel resistance can be calculated from

$$
R_{chan} = V_{chan}/I_d = (V_d - I_d(R_s + R_d + 2R_c + R_{load}))/I_d,
$$

where $R_c$ is the contact resistance of the source or drain, and $R_{load}$ is the load resistance of the measurement circuit. $I_d$ was determined at $V_g = V_t + 0.5$ V with a small applied drain voltage of 50 or 100 mV. The procedure is more simple and accurate if one uses a set of MOSFET's having different values of $L_{mask}$ but all with the same value of $W_{mask}$. Then one needs only to plot $R_{chan}$ versus $L_{mask}$ in order to determine $\Delta L$.

DENNARD et al.: ION-IMPLANTED MOSFET'S
