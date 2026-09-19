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
section_title: Circuit Performance With Scaled-down Devices
kind: section
lang: en
source: https://doi.org/10.1109/jssc.1974.1050511
pdf_sha256: fe83e914e79d8bf4271ea55de8f78a47a254fd7093a7ab073b80f956089d5690
pdf_pages: 9-11
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: f6f4f010a7e52e4ca95d311e60edecda4c3450886aaf1d8041842c4f3a5bf6eb
edited: true
prompt_sha256: c5c47cae65ffa93ca979b448f43adf142f13a9820bcd1d77a3ff1aa1babe667b
---

The performance improvement expected from using very small MOSFET's in integrated circuits of comparably small dimensions is discussed in this section. First, the performance changes due to size reduction alone are obtained from the scaling considerations given earlier. The influence on the circuit performance due to the structural changes of the ion-implanted design is then discussed.

Table I lists the changes in integrated circuit performance which follow from scaling the circuit dimensions, voltages, and substrate doping in the same manner as the device changes described with respect to Fig. 1. These changes are indicated in terms of the dimensionless scaling factor $\kappa$. Justifying these results here in great detail would be tedious, so only a simplified treatment is given. It is argued that all nodal voltages are reduced in the miniaturized circuits in proportion to the reduced supply voltages. This follows because the quiescent voltage levels in digital MOSFET circuits are either the supply levels or some intermediate level given by a voltage divider consisting of two or more devices, and because the resistance $V/I$ of each device is unchanged by scaling. An assumption is made that parasitic resistance elements are either negligible or unchanged by scaling, which will be examined subsequently. The circuits operate properly at lower voltages because the device threshold voltage $V_t$ scales as shown in (2), and furthermore because the tolerance spreads on $V_t$ should be proportionately reduced as well if each parameter in (2) is controlled to the same percentage accuracy. Noise margins are reduced, but at the same time internally generated noise coupling voltages are reduced by the lower signal voltage swings.

Fig. 13. Calculated and experimental subthreshold turn-on characteristics for ion-implanted zero substrate bias design. {#dennard-1974-scaling-fig-13 .figure tag=03A5}

| Device or Circuit Parameter | Scaling Factor |
| --- | --- |
| Device dimension $t_{ox}, L, W$ | $1/\kappa$ |
| Doping concentration $N_a$ | $\kappa$ |
| Voltage $V$ | $1/\kappa$ |
| Current $I$ | $1/\kappa$ |
| Capacitance $\epsilon A/t$ | $1/\kappa$ |
| Delay time/circuit $VC/I$ | $1/\kappa$ |
| Power dissipation/circuit $VI$ | $1/\kappa^2$ |
| Power density $VI/A$ | 1 |

Due to the reduction in dimensions, all circuit elements (i.e., interconnection lines as well as devices) will have their capacitances reduced by a factor of $\kappa$. This occurs because of the reduction by $\kappa^2$ in the area of these components, which is partially cancelled by the decrease in the electrode spacing by $\kappa$ due to thinner insulating films and reduced depletion layer widths. These reduced capacitances are driven by the unchanged device resistances $V/I$ giving decreased transition times with a resultant reduction in the delay time of each circuit by a factor of $\kappa$. The power dissipation of each circuit is reduced by $\kappa^2$ due to the reduced voltage and current levels, so the power-delay product is improved by $\kappa^3$. Since the area of a given device or circuit is also reduced by $\kappa^2$, the power density remains constant. Thus, even if many more circuits are placed on a given integrated circuit chip, the cooling problem is essentially unchanged.

As indicated in Table II, a number of problems arise from the fact that the cross-sectional area of conductors is decreased by $\kappa^2$ while the length is decreased only by $\kappa$. It is assumed here that the thicknesses of the conductors are necessarily reduced along with the widths because of the more stringent resolution requirements (e.g., on etching, etc.). The conductivity is considered to remain constant which is reasonable for metal films down to very small dimensions (until the mean free path becomes comparable to the thickness), and is also reasonable for degenerately doped semiconducting lines where solid solubility and impurity scattering considerations limit any increase in conductivity. Under these assumptions the resistance of a given line increases directly with the scaling factor $\kappa$. The IR drop in such a line is therefore constant (with the decreased current levels), but is $\kappa$ times greater in comparison to the lower operating voltages. The response time of an unterminated transmission line is characteristically limited by its time constant $R_L C$, which is unchanged by scaling; however, this makes it difficult to take advantage of the higher switching speeds inherent in the scaled-down devices when signal propagation over long lines is involved. Also, the current density in a scaled-down conductor is increased by $\kappa$, which causes a reliability concern. In conventional MOSFET circuits, these conductivity problems are relatively minor, but they become significant for line-widths of micron dimensions. The problems may be circumvented in high performance circuits by widening the power buses and by avoiding the use of n+ doped lines for signal propagation.

Use of the ion-implanted devices considered in this paper will give similar performance improvement to that of the scaled-down device with $\kappa = 5$ given in Table I. For the implanted devices with the higher operating voltages (4 V instead of 3 V) and higher threshold voltages (0.9 V instead of 0.4 V), the current level will be reduced

| Parameter | Scaling Factor |
| --- | --- |
| Line resistance, $R_L = \rho L/Wt$ | $\kappa$ |
| Normalized voltage drop $IR_L/V$ | $\kappa$ |
| Line response time $R_L C$ | 1 |
| Line current density $I/A$ | $\kappa$ |

in proportion to $(V_g - V_t)^2 / t_{ox}$ to about 80 percent of the current in the scaled-down device. The power dissipation per circuit is thus about the same in both cases. All device capacitances are about a factor of two less in the implanted devices, and n+ interconnection lines will show the same improvement due to the lighter substrate doping and decreased junction depth. Some capacitance elements such as metal interconnection lines would be essentially unchanged so that the overall capacitance improvement in a typical circuit would be somewhat less than a factor of two. The delay time per circuit which is proportional to $VC/I$ thus appears to be about the same for the implanted and for the directly scaled-down micron devices shown in Fig. 4.
