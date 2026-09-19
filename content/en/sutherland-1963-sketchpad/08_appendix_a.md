---
paper: sutherland-1963-sketchpad
title: 'Sketchpad: A Man-Machine Graphical Communication System'
authors:
  - Ivan E. Sutherland
year: 1963
venue: MIT PhD thesis / AFIPS Spring Joint Computer Conference
field: graphics
section_title: Appendix A
kind: appendix
lang: en
source: https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-574.pdf
pdf_sha256: e052281b553622badc8dd308003c127617aa5723e4ec3dbfa79b781d8e712742
pdf_pages: 117-118
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: ed33595a85302addd5ada52526c66c35c214771c6cd4c89d800a6d3ed62c4b18
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

CONSTRAINT DESCRIPTIONS code    variable types    description

43      point instance (point)

T       Point bears same relation to instance that (point) bears to its picture.
GENERATED AUTOMATICALLY WITH INSTANCES

33      p thing

L       Three things are collinear. Note: no distinction made about ordering of variables.
GENERATED AUTOMATICALLY WHEN POINTS ARE CREATED ON LINES

22      p thing

C       Distance from first to second is equal to distance from first to third. (First is circle center.)
GENERATED AUTOMATICALLY WHEN POINTS ARE CREATED ON CIRCLES

24      4 thing

E       Thing is erect or on its side.
↑ → ↓ ←

27      p thing

H       First thing is directly above or below, or directly beside second thing. (Horizontal or vertical line.)
GENERATED AUTOMATICALLY FOR ANY LINE BY HORV BUTTON

30      4 thing

I       4 thing is “parallel” to line between p things. Parallel to horizontal line means upright. (To set angle of text.)

| code | variable types | description |
| --- | --- | --- |
| 34 M | p thing p thing p thing p thing | Distance from first thing to second is 1/3, 1/2, 1, 2, 3, times distance from third to fourth. |
| 42 S | 4 thing 4 thing | First thing is 1/3, 1/2, 1, 2, 3 times size of second thing. |
| 23 D | scalar p thing p thing | Value of scalar equals distance between things in inches. |
| 21 B | scalar 4 thing | Value of scalar equals size of thing in inches. |
| 25 F | instance F | Instance is full size, i.e. the same size as its master picture. |
| 47 X | p thing p thing p thing | First thing is at mid point of other two, e.g. dimension in dimension line is at center of line. |
| 06 6 | 4 thing 6 | Thing is 1/32, 1/16, 1/8, 1/4, 1/2 or 1 inch in overall size. |
| 37 P | p thing p thing p thing p thing | Line from first to second would be parallel or perpendicular to line from third to fourth. (Lines need not be there.) |
| 36 O | 4 thing p thing | p thing will be next to 4 thing with enough space for 5 digit number, e.g. to create space in dimension line. |
| 46 W | p thing p thing | Distance between things is maintained what it was last time meta of tog 22 was down. USES META OF TOG 22. e.g. for bridges and linkages. |
| 50 Y | scalar (p thing) (p thing) | Value of scalar is equal to change in distance between p things since meta of tog 22 was down, sign considered. e.g. to display forces in beams. USES META OF TOG 22. |
