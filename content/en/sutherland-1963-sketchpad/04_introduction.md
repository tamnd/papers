---
paper: sutherland-1963-sketchpad
title: 'Sketchpad: A Man-Machine Graphical Communication System'
authors:
  - Ivan E. Sutherland
year: 1963
venue: MIT PhD thesis / AFIPS Spring Joint Computer Conference
field: graphics
section_title: Introduction
kind: section
lang: en
source: https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-574.pdf
pdf_sha256: e052281b553622badc8dd308003c127617aa5723e4ec3dbfa79b781d8e712742
pdf_pages: 17-29
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: 6fb401a32a024794ea9f74f3010d375c215f4e93571b6e1a4ac7ac18646a92e8
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

|| The Sketchpad system makes it possible for a man and a computer to converse rapidly through the medium of line drawings. Heretofore, most interaction between men and computers has been slowed down by the need to reduce all communication to written statements that can be typed; in the past, we have been writing letters to rather than conferring with our computers. For many types of communication, such as describing the shape of a mechanical part or the connections of an electrical circuit, typed statements can prove cumbersome. The Sketchpad system, by eliminating typed statements (except for legends) in favor of line drawings, opens up a new area of man-machine communication.

The decision actually to implement a drawing system reflected our feeling that knowledge of the facilities which would prove useful could only be obtained by actually trying them. The decision actually to implement a drawing system did not mean, however, that brute force techniques were to be used to computerize ordinary drafting tools; it was implicit in the research nature of the work that simple new facilities should be discovered which, when implemented, should be useful in a wide range of applications, preferably including some unforeseen ones. It has turned out that the properties of a computer drawing are entirely different from a paper drawing not only because of the accuracy, ease of drawing, and speed of erasing provided by the computer, but also primarily because of the ability to move drawing parts around on a computer drawing without the need to erase them. Had a working system not been developed, our thinking would have been too strongly influenced by a lifetime of drawing on paper to discover many of the useful services|| that the computer can provide.

As the work has progressed, several simple and very widely applicable facilities have been discovered and implemented. They provide a subpicture capability for including arbitrary symbols on a drawing, a constraint capability for relating the parts of a drawing in any computable way, and a definition copying capability for building complex relationships from combinations of simple atomic constraints.* When combined with the ability to point at picture parts given by the demonstrative light pen language, the subpicture, constraint, and

*Terms with specialized meanings are listed in the glossary at the very end of this thesis.

definition copying capabilities produce a system of extraordinary power. As was hoped at the outset, the system is useful in a wide range of applications, and unforeseen uses are turning up.

AN INTRODUCTORY EXAMPLE

To understand what is possible with the system at present let us consider using it to draw the hexagonal pattern of Figure 1.1. We will issue specific commands with a set of push buttons, turn functions on and off with switches, indicate position information and point to existing drawing parts with the light pen, rotate and magnify picture parts by turning knobs, and observe the drawing on the display system. This equipment as provided at Lincoln Laboratory’s TX-2 computer [1] is shown in Figure 1.2. When our drawing is complete it may be inked on paper, as were all the drawings in the thesis, by the plotter [12] shown in|| Figure 1.3. It is our intent with this example to show what the computer can do to help us draw while leaving the details of how it performs its functions for the chapters which follow.

If we point the light pen at the display system and press a button called “draw”, the computer will construct a straight line segment* which stretches like a rubber band from the initial to the present location of the pen as shown in Figure 1.4. Additional presses of the button will produce additional lines until we have made six, enough for a single hexagon. To close the figure we return the light pen to near the end of the first line drawn where it will “lock on” to the end exactly. A sudden flick of the pen terminates drawing, leaving the closed irregular hexagon shown in Figure 1.5A.

To make the hexagon regular, we can inscribe it in a circle. To draw the circle we place the light pen where the center is to be and press the button “circle center”, leaving behind a center point. Now, choosing a point on the circle (which fixes the radius,) we press the button “draw” again, this time getting a circle arc* whose length only is controlled by light pen position as shown in Figure 1.4.

Next we move the hexagon into the circle by pointing to a corner of the hexagon and pressing the button “move” so that the corner follows|| the light pen, stretching two rubber band line segments behind it. By pointing to the circle and giving the termination flick we indicate that the corner is to lie on the circle. Each corner is in this way moved onto the circle at roughly equal spacing around it as shown in Figure 1.5D.

We have indicated that the vertices of the hexagon are to lie on the circle, and they will remain on the circle throughout our further manipulations. If we also insist that the sides of the hexagon be of equal length, a regular hexagon will be constructed. This we can do by pointing to one side and pressing the “copy” button, and then to another side and giving the termination flick. The button in this case copies a definition of equal length lines and applies it to the

*The terms “circle” and “line” may be used in place of “circle arc” and “line segment” respectively since a full circle in Sketchpad is a circle arc of 360 or more degrees and no infinite line can be drawn.

FIGURE 1.1. HEXAGONAL PATTERN

Figure 1.1: (Originally on page 10.) {#sutherland-1963-sketchpad-fig-1-1 .figure tag=08F3}

Figure 1.2: TX-2 OPERATING AREA — SKETCHPAD IN USE. On the display can be seen part of a bridge similar to that of Figure 9.6. The Author is holding the Light pen. The push buttons used to control specific drawing functions are on the box in front of the Author. Part of the bank of toggle switches can be seen behind the Author. The size and position of the part of the total picture seen on the display is obtained through the four black knobs just above the table. (Originally on page 11.) {#sutherland-1963-sketchpad-fig-1-2 .figure tag=08F4}

Figure 1.3: PLOTTER USED WITH SKETCHPAD. A digital and analog control system makes the plotter draw straight lines and circles either under direct control of the TX-2 or off-line from punched paper tape. (Originally on page 12.) {#sutherland-1963-sketchpad-fig-1-3 .figure tag=08F5}

FIGURE 1.4.
LINE AND CIRCLE DRAWING

Figure 1.4: (Originally on page 14.) {#sutherland-1963-sketchpad-fig-1-4 .figure tag=08F6}

AN INTRODUCTORY EXAMPLE

A. SIX SIDED FIGURE    B. TO BE INSCRIBED IN CIRCLE

C. BY MOVING EACH CORNER    D. ON TO CIRCLE

E. MAKE SIDES EQUAL    F. ERASE CIRCLE

G. CALL 7 HEXAGONS    H. JOIN CORNERS

FIGURE 1.5. ILLUSTRATIVE EXAMPLE

Figure 1.5: (Originally on page 15.) {#sutherland-1963-sketchpad-fig-1-5 .figure tag=08F7}

lines indicated. We have said, in effect, make *this* line equal in length to *that* line. We indicate that all six lines are equal in length by five such statements. The computer satisfies all existing conditions (if it is possible) whenever we turn on a toggle switch. This done, we have a complete regular hexagon inscribed in a circle. We can erase the entire circle by pointing to any part of it and pressing the “delete” button. The completed hexagon is shown in Figure 1.5F.

To make the hexagonal pattern of Figure 1.1 we wish to attach a large number of hexagons together by their corners, and so we designate the six corners of our hexagon as attachment points by pointing to each and pressing a button. We now file away the basic hexagon and begin work on a fresh “sheet of paper” by changing a switch setting. On the new sheet we assemble, by pressing a button to create each hexagon as a subpicture, six hexagons around a central seventh in approximate position as shown in Figure 1.5G. Subpictures may be positioned, each in its entirety, with the light pen, rotated or scaled with the knobs|| and fixed in position by the pen flick termination signal; but their internal shape is fixed. By pointing to the corner of one hexagon, pressing a button, and then pointing to the corner of another hexagon we can fasten those corners together, because these corners have been designated as attachment points. If we attach two corners of each outer hexagon to the appropriate corners of the inner hexagon, the seven are uniquely related, and the computer will reposition them as shown in Figure 1.5H. An entire group of hexagons, once assembled, can be treated as a symbol. The entire group can be called up on another “sheet of paper” as a subpicture and assembled with other groups or with single hexagons to make a very large pattern. Using Figure 1.5H seven times we get the pattern of Figure 1.1. Constructing the pattern of Figure 1.1 takes less than five minutes with the Sketchpad system.

INTERPRETATION OF INTRODUCTORY EXAMPLE

In the introductory example above we have seen how to draw lines and circles and how to move existing parts of the drawing around. We used the light pen both to position parts of the drawing and to point to existing parts. For example, we pointed to the circle to erase it, and while drawing the sixth line, we pointed to the end of the first line drawn to close the hexagon. We also saw in action the very general *subpicture*, *constraint*, and *definition copying* capabilities of the system.

Subpicture: The original hexagon might just as well have been anything else: a picture of a transistor, a roller bearing, an airplane wing, a letter, or an entire figure for this report. Any number of different symbols may be drawn, in terms of other simpler symbols if desired, and any symbol may be used as often as desired.||

Constraint: When we asked that the vertices of the hexagon lie on the circle we were making use of a basic relationship between picture parts that is built into the system. Basic relationships (atomic constraints) to make lines vertical, horizontal, parallel, or perpendicular; to make points lie on lines or circles; to make symbols appear upright, vertically above one another or be of equal size; and to relate symbols to other drawing parts such as points and lines have been included in the system. It is so easy to program new constraint types that the set of atomic constraints was expanded from five to the seventeen listed in Appendix A in a period of about two days; specialized constraint types may be added as needed.

Definition Copying: In the introductory example above we asked that the sides of the hexagon be equal in length by pressing a button while pointing to the side in question. Here we were using the definition copying capability of the system. Had we defined a composite operation such as to make two lines both parallel and equal in length, we could have applied it just as easily. The number of operations which can be defined from the basic constraints applied to various picture parts is almost unlimited. Useful new definitions are drawn regularly; they are as simple as horizontal lines and as complicated as dimension lines complete with arrowheads and a number which indicates the length of the line correctly. The definition copying capability makes using the constraint capability easy.

IMPLICATIONS OF INTRODUCTORY EXAMPLE

As we have seen in the introductory example, drawing with the Sketchpad system is different from drawing with an ordinary pencil and paper. Most important of all, the Sketchpad drawing itself is entirely different from the trail of carbon left on a piece of paper. Information about how the drawing is tied together is stored in the computer as well as the information which gives the drawing its particular appearance. Since the drawing is tied together, it will keep a useful appearance even when parts of it are moved. For example, when we moved the corners of the hexagon onto the circle, the lines next to each corner|| were automatically moved so that the closed topology of the hexagon was preserved. Again, since we indicated that the corners of the hexagon were to lie on the circle they remained on the circle throughout our further manipulations.

It is this ability to store information relating the parts of a drawing to each other that makes Sketchpad most useful. For example, the linkage shown in Figure 1.6 was drawn with Sketchpad in just a few minutes. Constraints were applied to the linkage to keep the length of its various members constant. Rotation of the short central link is supposed to move the left end of the dotted line vertically. Since exact information about the properties of the linkage has been stored in Sketchpad, it is possible to observe the motion of the entire linkage when the short central link is rotated. The value of the number in Figure 1.6 was constrained to indicate the length of the dotted line, comparing the actual motion with the vertical line at the right of the linkage. One can observe that for all positions of the linkage the length of the dotted line is constant,

FIGURE 1.6.
FOUR POSITIONS OF LINKAGE
NUMBER SHOWS LENGTH OF DOTTED LINE

Figure 1.6: (Originally on page 20.) {#sutherland-1963-sketchpad-fig-1-6 .figure tag=08F8}

FIGURE 1.7.

AND ON SAME LATTICE demonstrating that this is indeed a straight line linkage. Other examples of moving drawings made with Sketchpad may be found in the final chapter.

Figure 1.7: (Originally on page 20.) {#sutherland-1963-sketchpad-fig-1-7 .figure tag=08F9}

As well as storing how the various parts of the drawing are related, Sketchpad stores the structure of the subpicture used. For example, the storage for the hexagonal pattern of Figure 1.1 indicates that this pattern is made of smaller patterns which are in turn made of smaller patterns which are composed of single hexagons. If the master hexagon is changed, the entire appearance of the hexagonal pattern will be changed. The structure of the pattern will, of course, be the same. For example, if we change the basic hexagon into a semicircle, the fish scale pattern shown in Figure 1.7 instantly results.

|| Since Sketchpad stores the structure of a drawing, a Sketchpad drawing explicitly indicates similarity of symbols. In an electrical drawing, for example, all transistor symbols are created from a single master transistor drawing. If some change to the basic transistor symbol is made, this change appears at once in all transistor symbols without further effort. Most important of all, the computer “knows” that a “transistor” is intended at that place in the circuit. It has no need to interpret the collection of lines which we would easily recognize as a transistor symbol. Since Sketchpad stores the topology of the drawing as we saw in closing the hexagon, one indicates both what a circuit looks like and its electrical connections when one draws it with Sketchpad. One can see that the circuit connections are stored because moving a component automatically moves any wiring on that component to maintain the correct connections. Sketchpad circuit drawings will soon be used as inputs for a circuit simulator. Having drawn a circuit one will find out its electrical properties.

SKETCHPAD AND THE DESIGN PROCESS

Construction of a drawing with Sketchpad is *itself* a model of the design process. The locations of the points and lines of the drawing model the variables of a design, and the geometric constraints applied to the points and lines of the drawing model the design constraints which limit the values of design variables. The ability of Sketchpad to satisfy the geometric constraints applied to the parts of a drawing models the ability of a good designer to satisfy all the design conditions imposed by the limitations of his materials, cost, etc. In fact, since designers in many fields produce nothing themselves but a drawing of a part, design conditions may well be thought of as applying to the drawing of a part rather than to the part itself. If such design conditions were added to Sketchpad’s vocabulary of constraints the computer could assist a user not only in arriving at a nice looking drawing, but also in arriving at a sound design.

PRESENT USEFULNESS

At the outset of the research no one had ever drawn engineering drawings directly on a computer display with nearly the facility now possible, and consequently no one knew what it would be like. We have now accumulated about a hundred hours of experience actually making drawings with a working system. As is shown in the final chapter, application of computer drawing techniques to a variety of problems has been made. As more and more applications have been made it has become clear that the properties of Sketchpad drawings make them most useful in four broad areas:

For Making Small Changes to Existing Drawings:

Each time a drawing is made, a description of that drawing is stored in the computer in a form that is readily transferred to magnetic tape. Thus, as time passes, a library of drawings will develop, parts of which may be used in other drawings at only a fraction of the investment of time that was put into the original drawing. Since a drawing stored in the computer may contain explicit representation of design conditions in its constraints, manual change of a critical part will automatically result in appropriate changes to related parts.

For Gaining Scientific or Engineering Understanding of Operations That Can Be Described Graphically:

The description of a drawing stored in the Sketchpad system is more than a collection of static drawing parts, lines and curves, etc. A drawing in the Sketchpad system may contain explicit statements about the relations between its parts so that as one part is changed the implications of this change become evident throughout the drawing. It is possible, as we saw in Figure 1.6, to give the property of fixed length to lines so as to study mechanical linkages, observing the path of some parts when others are moved.

As we saw in Figure 1.7 any change made in the definition of a subpicture is at once reflected in the appearance of that subpicture wherever it may occur. By making such changes, understanding of the relationships of complex sets of subpictures can be gained. For example, one can study how a change in the basic element of a crystal structure is reflected throughout the crystal.

As a Topological Input Device for Circuit Simulators, etc.:

Since the ring structure storage of Sketchpad reflects the topology of any circuit or diagram, it can serve as an input for many network or circuit simulating programs. The additional effort required to draw a circuit completely from scratch with the Sketchpad system may well be recompensed if the properties of the circuit are obtainable through simulation of the circuit drawn.

For Highly Repetitive Drawings:

The ability of the computer to reproduce any drawn symbol anywhere at the press of a button, and to recursively include subpictures within subpictures makes it easy to produce drawings which are composed of huge numbers of parts all similar in shape. Great interest in doing this comes from people in such fields as memory development and micro logic where vast numbers of elements are to be generated at once through photographic processes. Master drawings of the repetitive patterns necessary can be easily drawn. Here again, the ability to change the individual element of the repetitive structure and have the change at once brought into all sub-elements makes it possible to change the elements of an array without redrawing the entire array.

Those readers who are primarily interested in the application of Sketchpad are invited to turn next to Chapter IX, page 120 for aditional examples and conclusions.
