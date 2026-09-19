---
paper: sutherland-1963-sketchpad
title: 'Sketchpad: A Man-Machine Graphical Communication System'
authors:
  - Ivan E. Sutherland
year: 1963
venue: MIT PhD thesis / AFIPS Spring Joint Computer Conference
field: graphics
section_title: Acknowledgments
kind: section
lang: en
source: https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-574.pdf
pdf_sha256: e052281b553622badc8dd308003c127617aa5723e4ec3dbfa79b781d8e712742
pdf_pages: 11-17
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 048b2063279adafffe840056f842249afc21448f916b782cef1ed1f9b04efd17
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

I am indebted to Professors Claude E. Shannon and Marvin Minsky for their help and advice throughout the course of this research. Their helpful suggestions at several critical times gave Sketchpad much of its present character.

Special thanks are due to Professor Steven A. Coons of the Mechanical Engineering Department and to Douglas T. Ross of the Electronic Systems Laboratory. Even though I was outside their Computer Aided Design group, they provided at least as unstintingly of their time and ideas as if I had been their only concern.

I owe a great debt to the MIT Lincoln Laboratory for the tremendous support it afforded me. I wish to thank Wesley A. Clark and Jack L. Mitchell for making the TX-2 computer available to me and for providing help to make the special equipment I needed. I appreciate the helpful suggestions and interest that they and all the members of Group 51 provided. Special thanks are due Leonard M. Hantman for the additions he made to Sketchpad.

The Research Laboratory of Electronics at MIT provided me with office space and congenial office mates whose discussion and interest I greatly appreciate.

Finally, I wish to thank Lawrence G. Roberts who was a constant source of answers to specific questions I had both about the best ways to program TX-2 and about the mathematics of difference equations and matrix manipulations.

Contents

I    INTRODUCTION                                                                                                    17
II   HISTORY OF SKETCHPAD                                                                                         31
III  RING STRUCTURE                                                                                              37
IV   LIGHT PEN                                                                                                    53
V    DISPLAY GENERATION                                                                                           63
VI   RECURSIVE FUNCTIONS                                                                                          77
VII  BUILDING A DRAWING, THE COPY FUNCTION                                                                       87
VIII CONSTRAINT SATISFACTION                                                                                       93
IX   EXAMPLES AND CONCLUSIONS                                                                                  99
A    CONSTRAINT DESCRIPTIONS                                                                                      117
B    PUSH BUTTON CONTROLS                                                                                         119
C    STRUCTURE OF STORAGE BLOCKS                                                                                 121
D    RING OPERATION MACRO INSTRUCTIONS                                                                           127
E    PROPOSAL FOR AN INCREMENTAL CURVE DRAWING DISPLAY                                                           129
F    MATHEMATICS OF LEAST MEAN SQUARE FIT                                                                         135
G    A BRIEF DESCRIPTION OF TX-2                                                                                 137

CONTENTS

List of Figures

1.1 Hexagonal Pattern .................................................. 19
1.2 TX-2 Operating Area — Sketchpad in Use ......................... 20
1.3 Plotter Used with Sketchpad ..................................... 21
1.4 Line and Circle Drawing .......................................... 22
1.5 Illustrative Example .............................................. 23
1.6 Four Positions of Linkage .......................................... 26
1.7 Hexagon and Semicircle on Same Lattice ......................... 27

3.1 N-Component Elements ............................................ 39
3.2 Basic Ring Structure ............................................. 42
3.3 Line Segment and End Points ..................................... 43
3.4 Zero and One Member Rings ....................................... 43
3.5 Fresh Point Block ................................................ 45
3.6 Compacting the Ring Structure ................................... 46
3.7 Instances Generic Block .......................................... 49
3.8 Generic Structure ................................................ 50

4.1 Light Pen .......................................................... 54
4.2 Construction of Light Pen ......................................... 54
4.3 Predictive Pen Tracking .......................................... 56
4.4 Displays for Pen Tracking ......................................... 57
4.5 Address in Display Register ...................................... 58
4.6 Operation of Pseudo Pen Location ................................. 60

5.1 Twinkled Display .................................................. 65
5.2 Coordinate Systems ................................................ 67
5.3 Display of Constraints ........................................... 74
5.4 Display of Scalar and Digits ..................................... 75

6.1 Applying Two Constraints Indirectly to Two Lines ............... 81

7.1 Definitions to Copy ............................................... 90

9.1 Zig-Zag for Delay Line ........................................... 100
9.2 BCD Encoder for Clock ........................................... 101
9.3 Three Bar Linkage ................................................ 103
9.4 Conic Drawing Linkage ........................................... 103
9.5 Dimension Lines .................................................. 105
9.6 Truss Under Load .................................................. 106

9.7  Cantilever and Arch Bridges ............................................. 108
9.8  Winking Girl and Components ........................................ 109
9.9  Girl Traced from Photograph ......................................... 111
9.10 Girl with Features Changed ........................................... 112
9.11 Circuit Diagrams ....................................................... 113

E.1  DDA for Drawing Lines ............................................... 130
E.2  DDA for Upright Conics .............................................. 132
E.3  DDA for General Conic ................................................ 133

Chapter I
