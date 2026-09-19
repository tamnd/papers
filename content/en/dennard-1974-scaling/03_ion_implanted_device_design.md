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
section_title: Ion-implanted Device Design
kind: section
lang: en
source: https://doi.org/10.1109/jssc.1974.1050511
pdf_sha256: fe83e914e79d8bf4271ea55de8f78a47a254fd7093a7ab073b80f956089d5690
pdf_pages: "5"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: b4aed156bda3055131d759b154a33e935a799a7ceb410dbcf66ca5eb9c5e2e6c
prompt_sha256: c5c47cae65ffa93ca979b448f43adf142f13a9820bcd1d77a3ff1aa1babe667b
---

The scaling considerations just presented lead to the device structure with a 1-$\mu$ channel length shown in Fig. 4(a). In contrast, the corresponding improved design utilizing the capability afforded by ion implantation is shown in Fig. 4(b). The ion-implanted device uses an initial substrate doping that is lower by about a factor of four, and an implanted boron surface layer having a concentration somewhat greater than the concentration used throughout the unimplanted structure of Fig. 4(a). The concentration and the depth of the implanted surface layer are chosen so that this heavier doped region will be completely within the surface depletion layer when the device is turned on with the source grounded. Thus, when the source is biased above ground potential, the depletion layer will extend deeper into the lighter doped substrate, and the additional exposed "bulk" charge will be reasonably small and will cause only a modest increase in the gate-to-source voltage required to turn on the device. With this improvement in substrate sensitivity the gate insulator thickness can be increased to as much as 350 $\AA$ and still maintain a reasonable gate threshold voltage as will be shown later.

Another aspect of the design philosophy is to use shallow implanted n+ regions of depth comparable to the implanted p-type surface layer. The depletion regions under the gate electrode at the edges of the source and drain are then inhibited by the heavier doped surface layer, roughly pictured in Fig. 4(b), for the case of a turned-off device. The depletion regions under the source and drain extend much further into the lighter doped substrate. With deeper junctions these depletion regions would tend to merge in the lighter doped material which would cause a loss of threshold control or, in the extreme, punchthrough at high drain voltages. However, the shallower junctions give a more favorable electric field pattern which avoids these effects when the substrate doping concentration is properly chosen (i.e., when it is not too light).

The device capacitances are reduced with the ion-implanted structure due to the increased depletion layer width separating the source and drain from the substrate [cf. Figs. 4(a) and 4(b)], and due to the natural self-alignment afforded by the ion implantation process which reduces the overlap of the polysilicon gate over the source and drain regions. The thicker gate insulator also gives reduced gate capacitance, but the performance benefit in this respect is offset by the decreased gate field. To compensate for the thicker gate oxide and the expected threshold increase, a design objective for maximum drain voltage was set at 4 V for the ion-implanted design in Fig. 4(b), compared to 3 V for the scaled-down device of Fig. 4(a).
