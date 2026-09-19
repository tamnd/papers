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
section_title: Introduction
kind: section
lang: en
source: https://doi.org/10.1109/jssc.1974.1050511
pdf_sha256: fe83e914e79d8bf4271ea55de8f78a47a254fd7093a7ab073b80f956089d5690
pdf_pages: "2"
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 4dc02801f19506a27239d52f8bcae4f83cf3af71585048211198c3146c1a76bc
prompt_sha256: c5c47cae65ffa93ca979b448f43adf142f13a9820bcd1d77a3ff1aa1babe667b
---

NEW HIGH resolution lithographic techniques for forming semiconductor integrated circuit patterns offer a decrease in linewidth of five to ten times over the optical contact masking approach which is commonly used in the semiconductor industry today. Of the new techniques, electron beam pattern writing has been widely used for experimental device fabrication [1]–[4] while X-ray lithography [5] and optical projection printing [6] have also exhibited high-resolution capability. Full realization of the benefits of these new high-resolution lithographic techniques requires the development of new device designs, technologies, and structures which can be optimized for very small dimensions.

This paper concerns the design, fabrication, and characterization of very small MOSFET switching devices suitable for digital integrated circuits using dimensions of the order of $1\,\mu$. It is known that reducing the source-to-drain spacing (i.e., the channel length) of an FET leads to undesirable changes in the device characteristics. These changes become significant when the depletion regions surrounding the source and drain extend over a large portion of the region in the silicon substrate under the gate electrode. For switching applications, the most undesirable “short-channel” effect is a reduction in the gate threshold voltage at which the device turns on, which is aggravated by high drain voltages. It has been shown that these short-channel effects can be avoided by scaling down the vertical dimensions (e.g., gate insulator thickness, junction depth, etc.) along with the horizontal dimensions, while also proportionately decreasing the applied voltages and increasing the substrate doping concentration [7], [8]. Applying this scaling approach to a properly designed conventional-size MOSFET shows that a 200-\AA gate insulator is required if the channel length is to be reduced to $1\,\mu$.

A major consideration of this paper is to show how the use of ion implantation leads to an improved design for very small scaled-down MOSFET’s. First, the ability of ion implantation to accurately introduce a low concentration of doping atoms allows the substrate doping profile in the channel region under the gate to be increased in a controlled manner. When combined with a relatively lightly doped starting substrate, this channel implant reduces the sensitivity of the threshold voltage to changes in the source-to-substrate (“backgate”) bias. This reduced “substrate sensitivity” can then be traded off for a thicker gate insulator of 350-\AA thickness which tends to be easier to fabricate reproducibly and reliably. Second, ion implantation allows the formation of very shallow source and drain regions which are more favorable with respect to short-channel effects, while maintaining an acceptable sheet resistance. The combination of these features in an all-implanted design gives a switching device which can be fabricated with a thicker gate insulator if desired, which has well-controlled threshold characteristics, and which has significantly reduced interelectrode capacitances (e.g., drain-to-gate or drain-to-substrate capacitances).

This paper begins by describing the scaling principles which are applied to a conventional MOSFET to obtain a very small device structure capable of improved performance. Experimental verification of the scaling approach is then presented. Next, the fabrication process for an improved scaled-down device structure using ion implantation is described. Design considerations for this all-implanted structure are based on two analytical tools: a simple one-dimensional model that predicts the substrate sensitivity for long channel-length devices, and a two-dimensional current-transport model that predicts the device turn-on characteristics as a function of channel length. The predicted results from both analyses are compared with experimental data. Using the two-dimensional simulation, the sensitivity of the design to various parameters is shown. Then, detailed attention is given to an alternate design, intended for zero substrate bias, which offers some advantages with respect to threshold control. Finally, the paper concludes with a discussion of the performance improvements to be expected from integrated circuits that use these very small FET’s.
