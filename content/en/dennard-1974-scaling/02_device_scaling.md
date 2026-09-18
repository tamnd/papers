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
section_title: Device Scaling
kind: section
lang: en
source: https://doi.org/10.1109/jssc.1974.1050511
pdf_sha256: fe83e914e79d8bf4271ea55de8f78a47a254fd7093a7ab073b80f956089d5690
pdf_pages: 2-5
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: ad10f05d9bca70a4c01893330a4591af81e5230aad486c2406f57939bbeafde6
prompt_sha256: c5c47cae65ffa93ca979b448f43adf142f13a9820bcd1d77a3ff1aa1babe667b
---

The principles of device scaling [7], [8] show in a concise manner the general design trends to be followed in decreasing the size and increasing the performance of MOSFET switching devices. Fig. 1 compares a state-of-the-art n-channel MOSFET [9] with a scaled-down device designed following the device scaling principles to be described later. The larger structure shown in Fig. 1(a) is reasonably typical of commercially available devices fabricated by using conventional diffusion techniques. It uses a 1000-\AA gate insulator thickness with a substrate doping and substrate bias chosen to give a gate threshold voltage $V_t$ of approximately 2 V relative to the source potential. A substrate doping of $5 \times 10^{15}$ cm$^{-3}$ is low enough to give an acceptable value of substrate sensitivity. The substrate sensitivity is an important criterion in digital switching circuits employing source followers because the design becomes difficult if the threshold voltage increases by more than a factor of two over the full range of variation of the source voltage. For the device illustrated in Fig. 1(a), the design parameters limit the channel length $L$ to about 5 $\mu$. This restriction arises primarily from the penetration of the depletion region surrounding the drain into the area normally controlled by the gate electrode. For a maximum drain voltage of approximately 12–15 V this penetration will modify the surface potential and significantly lower the threshold voltage.

In order to design a new device suitable for smaller values of $L$, the device is scaled by a transformation in three variables: dimension, voltage, and doping. First, all linear dimensions are reduced by a unitless scaling factor $\kappa$, e.g., $t_{ox'} = t_{ox}/\kappa$, where the primed parameters refer to the new scaled-down device. This reduction includes vertical dimensions such as gate insulator thickness, junction depth, etc., as well as the horizontal dimensions of channel length and width. Second, the voltages applied to the device are reduced by the same factor (e.g., $V_{ds'} = V_{ds}/\kappa$). Third, the substrate doping concentration is increased, again using the same scaling factor (i.e., $N_{a'} = \kappa N_a$). The design shown in Fig. 1(b) was obtained using $\kappa = 5$ which corresponds to the desired reduction in channel length to 1 $\mu$.

The scaling relationships were developed by observing that the depletion layer widths in the scaled-down device are reduced in proportion to the device dimensions due to the reduced potentials and the increased doping. For example,

\[
w_s' = \{[2\epsilon_{Si}(\psi_b' + V_{s-sub}/\kappa)]/q\kappa N_a\}^{1/2} \simeq w_s/\kappa.
\] (1)

The threshold voltage at turn-on [9] is also decreased in direct proportion to the reduced device voltages so that the device will function properly in a circuit with reduced voltage levels. This is shown by the threshold voltage equation for the scaled-down device.

\[
V_t' = (t_{ox}/\kappa \epsilon_{ox})\{-Q_{eff} + [2\epsilon_{Si} q\kappa N_a (\psi_s' + V_{s-sub}/\kappa)]^{1/2}\}
+ (\Delta W_f + \psi_s') \simeq V_t/\kappa.
\] (2)

In (2) the reduction in $V_t$ is primarily due to the decreased insulator thickness, $t_{ox}/\kappa$, while the changes in the voltage and doping terms tend to cancel out. In most cases of interest (i.e., polysilicon gates of doping type opposite to that of the substrate or aluminum gates on p-type substrates) the work function difference $\Delta W_f$ is of opposite sign, and approximately cancels out $\psi_s'$. $\psi_s'$ is the band bending in the silicon (i.e., the surface potential) at the onset of strong inversion for zero substrate bias. It would appear that the $\psi'$ terms appearing in (1) and (2) prevent exact scaling since they remain approximately constant, actually increasing slightly due to the increased doping since $\psi_b' \simeq \psi_s' = (2kT/q) \ln (N_{a'}/n_v)$. However, the fixed substrate bias supply normally used with n-channel devices can be adjusted so that $(\psi_s' + V_{sub'}) = (\psi_s + V_{sub})/\kappa$. Thus, by scaling down the applied substrate bias more than the other applied voltages, the potential drop across the source or drain junctions, or across the depletion region under the gate, can be reduced by $\kappa$.

All of the equations that describe the MOSFET device characteristics may be scaled as demonstrated above. For example, the MOSFET current equation [9] given by

\[
I_{d'} = \frac{\mu_{eff} \epsilon_{ox}}{t_{ox}/\kappa} \left( \frac{W/\kappa}{L/\kappa} \right) \left( \frac{V_o - V_t - V_{d}/2}{\kappa} \right) (V_{d}/\kappa) = I_d/\kappa
\] (3) is seen to be reduced by a factor of $\kappa$, for any given set of applied voltages, assuming no change in mobility. Actually, the mobility is reduced slightly due to increased impurity scattering in the heavier doped substrate.

It is possible to generalize the scaling approach to include electric field patterns and current density. The electric field distribution is maintained in the scaled-down device except for a change in scale for the spatial coordinates. Furthermore, the electric field strength at any corresponding point is unchanged because $V/x = V'/x'$. Thus, the carrier velocity at any point is also unchanged due to scaling and, hence, any saturation velocity effects will be similar in both devices, neglecting microscopic differences due to the fixed crystal lattice dimensions. From (3), since the device current is reduced by $\kappa$, the channel current per unit of channel width $W$ is unchanged by scaling. This is consistent with the same sheet density of carriers (i.e., electrons per unit gate area) moving at the same velocity. In the vicinity of the drain, the carriers will move away from the surface to a lesser extent in the new device, due to the shallower diffusions. Thus, the density of mobile carriers per unit volume will be higher in the space-charge region around the drain, complementing the higher density of immobile charge due to the heavier doped substrate. Other scaling relationships for power density, delay time, etc., are given in Table I and will be discussed in a subsequent section on circuit performance.

In order to verify the scaling relationships, two sets of experimental devices were fabricated with gate insulators of 1000 and 200 \AA\ (i.e., $\kappa = 5$). The measured drain voltage characteristics of these devices, normalized to $W/L = 1$, are shown in Fig. 2. The two sets of characteristics are quite similar when plotted with voltage and current scales of the smaller device reduced by a factor of five, which confirms the scaling predictions. In Fig. 2, the exact

Fig. 2. Experimental drain voltage characteristics for (a) conventional, and (b) scaled-down structures shown in Fig. 1 normalized to $W/L = 1$. {#dennard-1974-scaling-fig-2 .figure tag=039F}

Fig. 3. Experimental turn-on characteristics for conventional and scaled-down devices shown in Fig. 1 normalized to $W/L = 1$. {#dennard-1974-scaling-fig-3 .figure tag=03A0}

match on the current scale is thought to be fortuitous since there is some experimental uncertainty in the magnitude of the channel length used to normalize the characteristics (see Appendix). More accurate data from devices with larger width and length dimensions on the same chip shows an approximate reduction of ten percent in mobility for devices with the heavier doped substrate. That the threshold voltage also scales correctly by a factor of five is verified in Fig. 3, which shows the experimental $\sqrt{I_d}$ versus $V_g$ turn-on characteristics for the original and the scaled-down devices. For the cases shown, the drain voltage is large enough to cause pinchoff and the characteristics exhibit the expected linear relationship. When projected to intercept the gate voltage axis this linear relationship defines a threshold voltage useful for most logic circuit design purposes.

One area in which the device characteristics fail to scale is in the subthreshold or weak inversion region of the turn-on characteristic. Below threshold, $I_d$ is exponentially dependent on $V_g$ with an inverse semilogarithmic slope, $\alpha$, [10], [11] which for the scaled-down device is given by

$$
\alpha' \left( \frac{\text{volts}}{\text{decade}} \right) = \frac{d V_g'}{d \log_{10} I_d'}
$$

$$
= (kT/q \log_{10} e) \left( 1 + \frac{\epsilon_{Si} t_{ox}/\kappa}{\epsilon_{ox} w_d/\kappa} \right),
$$

which is the same as for the original larger device. The parameter $\alpha$ is important to dynamic memory circuits because it determines the gate voltage excursion required to go from the low current "off" state to the high current "on" state [11]. In an attempt to also extend the linear scaling relationships to $\alpha$ one could reduce the operating temperature in (4) (i.e., $T' = T/\kappa$), but this would cause a significant increase in the effective surface mobility [12] and thereby invalidate the current scaling relationship of (3). In order to design devices for operation at room temperature and above, one must accept the fact that the subthreshold behavior does not scale as desired. This nonscaling property of the subthreshold characteristic is of particular concern to miniature dynamic memory circuits which require low source-to-drain leakage currents.

Fig. 4. Detailed cross sections for (a) scaled-down device structure, and (b) corresponding ion-implanted device structure. {#dennard-1974-scaling-fig-4 .figure tag=03A1}
