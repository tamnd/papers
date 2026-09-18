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
section_title: Front Matter
tag: 005A
kind: front
lang: en
source: https://doi.org/10.1109/jssc.1974.1050511
pdf_sha256: fe83e914e79d8bf4271ea55de8f78a47a254fd7093a7ab073b80f956089d5690
pdf_pages: 1-2
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 8c178022392bc73615eb0d41a3ef865551f716b2a300593d828eb1f9b2c22009
prompt_sha256: c5c47cae65ffa93ca979b448f43adf142f13a9820bcd1d77a3ff1aa1babe667b
---

[3] E. J. Boleky, “Subnanosecond switching delays using CMOS/SOS silicon-gate technology,” in 1971 Int. Solid-State Circuit Conf., Dig. Tech. Papers, p. 225.
[4] E. J. Boleky and J. E. Meyer, “High-performance low-power CMOS memories using silicon-on-sapphire technology,” IEEE J. Solid-State Circuits (Special Issue on Micropower Electronics), vol. SC-7, pp. 135–145, Apr. 1972.
[5] R. W. Bower, H. G. Dill, K. G. Aubuchon, and S. A. Thompson, “MOS field effect transistors by gate masked ion implantation,” IEEE Trans. Electron Devices, vol. ED-15, pp. 757–761, Oct. 1968.
[6] J. Tihanyi, “Complementary ESFI MOS devices with gate self adjustment by ion implantation,” in Proc. 5th Int. Conf. Microelectronics in Munich, Nov. 27–29, 1972. München-Wien, Germany: R. Oldenbourg Verlag, pp. 437–447.
[7] E. J. Boleky, “The performance of complementary MOS transistors on insulating substrates,” RCA Rev., vol. 30, pp. 372–395, 1970.
[8] K. Goser, “Channel formation in an insulated gate field effect transistor (IGFET) and its equivalent circuit,” Siemens Forschungs- und Entwicklungsberichte, no. 1, pp. 3–9, 1971.
[9] A. E. Ruehli and P. A. Brennan, “Accurate metallization capacitances for integrated circuits and packages,” IEEE J. Solid-State Circuits (Corresp.), vol. SC-8, pp. 289–290, Aug. 1973.
[10] SINAP (Siemens Netzwerk Analyse Programm Paket), Siemens AG, Munich, Germany.
[11] K. Goser and K. Steinhübl, “Aufteilung der Gate-Kanal-Kapazitat auf Source und Drain im Ersatzschaltbild eines MOS-Transistors,” Siemens Forschungs- und Entwicklungsberichte 1, no. 3, pp. 284–286, 1972.
[12] J. R. Burns, “Switching response of complementary-symmetry MOS transistors logic circuits,” RCA Rev., vol. 25, pp. 627–681, 1964.
[13] R. W. Ahrons and P. D. Gardner, “Introduction of technology and performance in complementary symmetry circuits,” IEEE J. Solid-State Circuits (Special Issue on Technology for Integrated-Circuit Design), vol. SC-5, pp. 24–29, Feb. 1970.
[14] F. F. Fang and H. Rupprecht, “High performance MOS integrated circuits using ion implantation technique,” presented at the 1973 ESSDERC, Munich, Germany.

Michael Pomper, for a photograph and biography, please see p. 238 of this issue.

Jenö Tihanyi, for a photograph and biography, please see p. 238 of this issue.

Design of Ion-Implanted MOSFET’s with Very Small Physical Dimensions

ROBERT H. DENNARD, MEMBER, IEEE, FRITZ H. GAENSSLLEN, HWA-NIEN YU, MEMBER, IEEE, V. LEO RIDEOUT, MEMBER, IEEE, ERNEST BASSOUS, AND ANDRE R. LeBLANC, MEMBER, IEEE

Abstract—This paper considers the design, fabrication, and characterization of very small MOSFET switching devices suitable for digital integrated circuits using dimensions of the order of 1 $\mu$. Scaling relationships are presented which show how a conventional MOSFET can be reduced in size. An improved small device structure is presented that uses ion implantation to provide shallow source and drain regions and a nonuniform substrate doping profile. One-dimensional models are used to predict the substrate doping profile and the corresponding threshold voltage versus source voltage characteristic. A two-dimensional current transport model is used to predict the relative degree of short-channel effects for different device parameter combinations. Polysilicon-gate MOSFET’s with channel lengths as short as 0.5 $\mu$ were fabricated, and the device characteristics measured and compared with predicted values. The performance improvement expected from using these very small devices in highly miniaturized integrated circuits is projected.

Manuscript received May 20, 1974; revised July 3, 1974.
The authors are with the IBM T. J. Watson Research Center, Yorktown Heights, N.Y. 10598.

IEEE JOURNAL OF SOLID-STATE CIRCUITS, VOL. SC-9, NO. 5, OCTOBER 1974

LIST OF SYMBOLS

$\alpha$
Inverse semilogarithmic slope of subthreshold characteristic.

$D$
Width of idealized step function profile for channel implant.

$\Delta W_f$
Work function difference between gate and substrate.

$\epsilon_{Si}, \epsilon_{ox}$
Dielectric constants for silicon and silicon dioxide.

$I_d$
Drain current.

$k$
Boltzmann’s constant.

$\kappa$
Unitless scaling constant.

$L$
MOSFET channel length.

$\mu_{eff}$
Effective surface mobility.

$n_i$
Intrinsic carrier concentration.

$N_a$
Substrate acceptor concentration.

$\Psi_s$
Band bending in silicon at the onset of strong inversion for zero substrate voltage.

DENNARD et al.: ION-IMPLANTED MOSFET'S

$$
\begin{array}{ll}
\Psi_b & \text{Built-in junction potential.} \\
q & \text{Charge on the electron.} \\
Q_{eff} & \text{Effective oxide charge.} \\
t_{ox} & \text{Gate oxide thickness.} \\
T & \text{Absolute temperature.} \\
V_d, V_s, V_g, V_{sub} & \text{Drain, source, gate and substrate voltages.} \\
V_{ds} & \text{Drain voltage relative to source.} \\
V_{s-sub} & \text{Source voltage relative to substrate.} \\
V_t & \text{Gate threshold voltage.} \\
w_s, w_d & \text{Source and drain depletion layer widths.} \\
W & \text{MOSFET channel width.}
\end{array}
$$
