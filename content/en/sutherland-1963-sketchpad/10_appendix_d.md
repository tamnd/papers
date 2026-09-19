---
paper: sutherland-1963-sketchpad
title: 'Sketchpad: A Man-Machine Graphical Communication System'
authors:
  - Ivan E. Sutherland
year: 1963
venue: MIT PhD thesis / AFIPS Spring Joint Computer Conference
field: graphics
section_title: Appendix D
kind: appendix
lang: en
source: https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-574.pdf
pdf_sha256: e052281b553622badc8dd308003c127617aa5723e4ec3dbfa79b781d8e712742
pdf_pages: 127-128
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 748bab2e47f3bd86f5107aa543c5131eb13def4befe6ec5380f7032506648872
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

RING OPERATION MACRO INSTRUCTIONS

The macro instructions listed in this appendix are used to implement the basic ring operations listed in Chapter III. Only the format is given here since to list the machine instructions generated would be of value only to persons familiar with the TX-2 instruction code. In each case the macro name is followed by dummy variables separated by non-alphabetic symbols. The dummy variables XR and XR2 refer to index registers which contain the address of the block which contains the ring element being worked on. The terms N of XR or N × XR mean the Nth element of the block pointed to by index register XR, for example, the LSP (line start point) register of the line block pointed to by index register $\alpha$.

LTAKE $\equiv$ N × XR

Take N of XR out of whatever ring it is in. The ring is reclosed. If N of XR is not in a ring, LTAKE does nothing. N of XR must not be a hen with chickens.

PUTL $\equiv$ N × XR → M × XR2
PUTR $\equiv$ N × XR → M × XR2

Put N of XR into the ring of which M of XR2 is a member. N of XR is placed to the left (PUTL) or right (PUTR) of M of XR2. M of XR2 may be either a hen or a chicken. N of XR must not already belong to a ring.

MOVEL $\equiv$ N × XR → M × XR2
MOVER $\equiv$ N × XR → M × XR2

Combination of LTAKE and PUTL (PUTR). Assumes that both N of XR and M of XR2 are in the same ring. Intended for reordering a ring.

CHGRL $\equiv$ N × XR → M × XR2
CHGRR $\equiv$ N × XR → M × XR2

Combination of LTAKE and PUTL (PUTR). N of XR and M of XR2 may be in different rings.

LGORR $\equiv$ N × XR → M × XR2 → SUBR → LEXIT
LGORL $\equiv$ N × XR → M × XR2 → SUBR → LEXIT

Go around the ring of which N of XR is the hen. Exit to subroutine SUBR once for each ring member. The address of the top of the block to which each ring member belongs is put in XR before starting the subroutine. XR2 is used as a working index register. The subroutine may destroy the contents of both XR and XR2. The subroutine may delete individual members of the ring provided recursive deletion does not delete additional ring members. The subroutine must not generate new ring members. Jump to LEXIT when finished with the ring. Go around the ring to the right (LGORRR) or left (LGORRL).

$$
\begin{align*}
\text{LGORRI} & \equiv \text{N} \times \text{XR} \rightarrow \text{M} \times \text{XR2} \rightarrow \text{SUBR} \rightarrow \text{LEXIT} \\
\text{LGORLI} & \equiv \text{N} \times \text{XR} \rightarrow \text{M} \times \text{XR2} \rightarrow \text{SUBR} \rightarrow \text{LEXIT}
\end{align*}
$$

Same as LGORRR except that the subroutine may generate new members in the ring. The subroutine must not delete the current member of the ring. New members will be visited if they are put in the ring later in sequence.

$$
\begin{align*}
\text{COMBHR} & \equiv \text{N} \times \text{XR} \rightarrow \text{M} \times \text{XR2} \\
\text{COMBHL} & \equiv \text{N} \times \text{XR} \rightarrow \text{M} \times \text{XR2}
\end{align*}
$$

The members of the ring whose hen is at N of XR are placed in the ring of which M of XR2 is a member. N of XR must not be empty. The new members are placed to the right (COMBHR) or left (COMBHL) of M of XR2. M of XR2 may be either a hen or a chicken. N of XR is left empty.
