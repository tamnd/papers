---
paper: sutherland-1963-sketchpad
title: 'Sketchpad: A Man-Machine Graphical Communication System'
authors:
  - Ivan E. Sutherland
year: 1963
venue: MIT PhD thesis / AFIPS Spring Joint Computer Conference
field: graphics
section_title: Discussion
kind: section
lang: en
source: https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-574.pdf
pdf_sha256: e052281b553622badc8dd308003c127617aa5723e4ec3dbfa79b781d8e712742
pdf_pages: 110-116
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: c1321333851483c2f48422fd8a02730d9d83e12e9aae76621a2b14fb6c208598
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

The methods outlined in this report generalize nicely to three dimensional drawing. In fact, work has already been begun to make a complete “Sketchpad Three” which will let the user communicate solid objects to the computer. A

FIGURE 9.9.
GIRL TRACED FROM PHOTOGRAPH

Figure 9.9: (Originally on page 134.) {#sutherland-1963-sketchpad-fig-9-9 .figure tag=0912}

FIGURE 9.10.
GIRL WITH FEATURES CHANGED

Figure 9.10: (Originally on page 135.) {#sutherland-1963-sketchpad-fig-9-10 .figure tag=0913}

FIGURE 9.11.
CIRCUIT DIAGRAMS

Figure 9.11: (Originally on page 137.) {#sutherland-1963-sketchpad-fig-9-11 .figure tag=0914}

forthcoming thesis by Timothy Johnson of the Mechanical Engineering Department will describe this work. When Johnson is finished it should be possible to aim at a particular place in the three dimensional drawing through two dimensional, perspective views presented on the display. Johnson is completely bypassing the problem of converting several two dimensional drawings into a three dimensional shape. Drawing will be directly in three dimensions from the start. No two dimensional representation will ever be stored.

Work is also proceeding on direct conversion of photographs into line drawings. Roberts reports a computer program [8] able to recognize|| simple objects in photographs well enough to produce three dimensional line drawings for them. Roberts is storing his drawings in the ring structure described in Chapter III so that his results will be compatible with the three dimensional version of Sketchpad.

Much room is left in Sketchpad itself for improvements. Some improvements are minor, such as including mirror image subpictures. Some improvements should be made to suit Sketchpad to particular uses that come up. For example, it is so interesting to study the path of particular points on a linkage that Sketchpad should be able to store and later display the path of chosen points.

More major improvements of the same order and power as the existing definition copying capability can be forseen. At present Sketchpad is able to add defined relationships to an existing object drawing. A method should be devised for defining and applying changes which involve removing some parts of the object drawing as well as adding new ones. Such a capability would permit one to define what rounding off a corner means. Then, by pointing at any corner and applying that definition, one could round off any corner. Sketchpad cannot now do this because rounding off a corner involves disconnecting the two lines which form the corner from the corner point and then putting a small circular arc between them.

HARDWARE

Sketchpad has pointed out some weaknesses in present computer hardware. A proposal for a line drawing display which would greatly surpass the capability of the spot display now in use is given in|| Appendix E. Such a display would not only provide flicker free display to the user, but also would relieve the computer of the burden it now carries in computing successive spots in the display.

There are two conflicting demands made by Sketchpad on the light pen. On the one hand, the pen must have a fairly large field of view for ease of tracking. On the other hand, it should have a small field of view for aiming at objects. It should be possible to build a pen with two concentric fields of view which would report to the computer separately.

The arithmetic element of the computer is not used in doing the ring structure processing which forms a large part of Sketchpad. On the other hand, the index registers and their associated arithmetic are extensively used. This suggests that several users could share an arithmetic element if sufficiently powerful index arithmetic were made available to each of them.

EXAMPLES AND CONCLUSIONS
