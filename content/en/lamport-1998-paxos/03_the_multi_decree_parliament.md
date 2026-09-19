---
paper: lamport-1998-paxos
title: The Part-Time Parliament
authors:
  - Leslie Lamport
year: 1998
venue: ACM TOCS
field: systems
section: "3"
section_title: The Multi-Decree Parliament
tag: "0241"
kind: section
lang: en
source: https://lamport.azurewebsites.net/pubs/lamport-paxos.pdf
pdf_sha256: cd9544e9615bcd417a2c10063671cecca0b28ad4bc5db3f64467a83ecc7028d3
pdf_pages: 16-23
extraction: vision
extraction_model: olmOCR-2-7B-1025-FP8
content_sha256: f291587d63893e87413ca95aa344e1f1c31ac119f3cc1fda59f07198bbfec014
prompt_sha256: 3224ee77210123d34b3df794cfa1ada9ce71ba395aadd9fddc54c0ae5b2cd36c
---

When Parliament was established, a protocol to satisfy its consistency and progress requirements was derived from the Synod protocol. The derivation and properties of the original parliamentary protocol are described in Sections 3.1 and 3.2. Section 3.3 discusses the further evolution of the protocol.

### 3.1 The Protocol {#lamport-1998-paxos-s3-1 .section tag=0246}

Instead of passing just one decree, the Paxon Parliament had to pass a series of numbered decrees. As in the Synod protocol, a president was elected. Anyone who wanted a decree passed would inform the president, who would assign a number to the decree and attempt to pass it. Logically, the parliamentary protocol used a separate instance of the complete Synod protocol for each decree number. However, a single president was selected for all these instances, and he performed the first two steps of the protocol just once.

The key to deriving the parliamentary protocol is the observation that, in the Synod protocol, the president does not choose the decree or the quorum until step 3. A newly elected president p can send to some set of legislators a single message that serves as the NextBallot (b) message for all instances of the Synod protocol. (There are an infinite number of instances—one for each decree number.) A legislator q can reply with a single message that serves as the LastVote messages for step 2 of all instances of the Synod protocol. This message contains only a finite amount of information, since q can have voted in only a finite number of instances.

When the new president has received a reply from every member of a majority set, he is ready to perform step 3 for every instance of the Synod protocol. For some finite number of instances (decree numbers), the choice of decree in step 3 will be determined by B3. The president immediately performs step 3 for each of those instances to try passing these decrees. Then, whenever he receives a request to pass a decree, he chooses the lowest-numbered decree that he is still free to choose, and he performs step 3 for that decree number (instance of the Synod protocol) to try to pass the decree.

The following modifications to this simple protocol lead to the actual Paxon Parliament’s protocol.

—There is no reason to go through the Synod protocol for a decree number whose outcome is already known. Therefore, if a newly elected president p has all decrees with numbers less than or equal to n written in his ledger, then he sends a NextBallot (b, n) message that serves as a NextBallot (b) message in all instances of the Synod protocol for decree numbers larger than n. In his response to this message, legislator q informs p of all decrees numbered greater than n that already appear in q’s ledger (in addition to sending the usual LastVote information for decrees not in his ledger), and he asks p to send him any decrees numbered n or less that are not in his ledger. —Suppose decrees 125 and 126 are introduced late Friday afternoon, decree 126 is passed and is written in one or two ledgers, but before anything else happens, the legislators all go home for the weekend. Suppose also that the following Monday,

∆φωρκ is elected the new president and learns about decree 126, but she has no knowledge of decree 125 because the previous president and all legislators who had voted for it are still out of the Chamber. She will hold a ballot that passes decree 126, which leaves a gap in the ledgers. Assigning number 125 to a new decree would cause it to appear earlier in the ledger than decree 126, which had been passed the previous week. Passing decrees out of order in this way might cause confusion—for example, if the citizen who proposed the new decree did so because he knew decree 126 had already passed. Instead, ∆φωρκ would attempt to pass

125: The ides of February is national olive day a traditional decree that made absolutely no difference to anyone in Paxos. In general, a new president would fill any gaps in his ledger by passing the “oliveday” decree.

The consistency and progress properties of the parliamentary protocol follow immediately from the corresponding properties of the Synod protocol from which it was derived. To our knowledge, the Paxons never bothered writing a precise description of the parliamentary protocol because it was so easily derived from the Synod protocol.

### 3.2 Properties of the Protocol {#lamport-1998-paxos-s3-2 .section tag=0247}

3.2.1 The Ordering of Decrees Balloting could take place concurrently for many different decree numbers, with ballots initiated by different legislators—each thinking he was president when he initiated the ballot. We cannot say precisely in what order decrees would be passed, especially without knowing how a president was selected. However, there is one important property about the ordering of decrees that can be deduced.

A decree was said to to be proposed when it was chosen by the president in step 3 of the corresponding instance of the Synod protocol. The decree was said to be passed when it was written for the first time in a ledger. Before a president could propose any new decrees, he had to learn from all the members of a majority set what decrees they had voted for. Any decree that had already been passed must have been voted for by at least one legislator in the majority set. Therefore, the president must have learned about all previously passed decrees before initiating any new decree. The president would not fill a gap in the ledgers with an important decree—that is, with any decree other than the “olive-day” decree. He would also not propose decrees out of order. Therefore, the protocol satisfied the following decree-ordering property.

If decrees A and B are important and decree A was passed before decree B was proposed, then A has a lower decree number than B. 3.2.2 Behind Closed Doors Although we don’t know the details involved in choosing a new president, we do know exactly how Parliament functioned when the president had been chosen and no one was entering or leaving the Chamber. Upon receiving a request to pass a decree—either directly from a citizen or relayed from another legislator—the president assigned the decree a number and passed it with the following exchange of messages. (The numbers refer to the corresponding steps in the Synod protocol.)

(3) The president sent a BeginBallot message to each legislator in a quorum. (4) Each legislator in the quorum sent a Voted message to the president. (5) The president sent a Success message to every legislator.

This is a total of three message delays and about 3N messages, assuming a parliament of N legislators and a quorum of about N/2. Moreover, if Parliament was busy, the president would combine the BeginBallot message for one decree with the Success message for a previous one, for a total of only 2N messages per decree.

### 3.3 Further Developments {#lamport-1998-paxos-s3-3 .section tag=0248}

Governing the island turned out to be a more complex task than the Paxons realized. A number of problems arose whose solutions required changes to the protocol. The most important of these changes are described below.

3.3.1 Picking a President The president of parliament was originally chosen by the method that had been used in the Synod, which was based purely on the alphabetical ordering of names. Thus, when legislator Ωκι returned from a sixmonth vacation, he was immediately made president—even though he had no idea what had happened in his absence. Parliamentary activity came to a halt while Ωκι, who was a slow writer, laboriously copied six months worth of decrees to bring his ledger up to date.

This incident led to a debate about the best way to choose a president. Some Paxons urged that once a legislator became president, he should remain president until he left the Chamber. An influential group of citizens wanted the richest legislator in the Chamber to be president, since he could afford to hire more scribes and other servants to help him with the presidential duties. They argued that once a rich legislator had brought his ledger up to date, there was no reason for him not to assume the presidency. Others, however, argued that the most upstanding citizen should be made president, regardless of wealth. Upstanding probably meant less likely to be dishonest, although no Paxon would publicly admit the possibility of official malfeasance. Unfortunately, the outcome of this debate is not known; no record exists of the presidential selection protocol that was ultimately used.

3.3.2 Long Ledgers As the years progressed and Parliament passed more and more decrees, Paxons had to pore over an ever longer list of decrees to find the current olive tax or what color goat could be sold. A legislator who returned to the Chamber after an extended voyage had to do quite a bit of copying to bring his ledger up to date. Eventually, the legislators were forced to convert their ledgers from lists of decrees into law books that contained only the current state of the law and the number of the last decree whose passage was reflected in that state.

To learn the current olive tax, one looked in the law book under “taxes”; to learn what color goat could be sold, one looked under “mercantile law”. If a legislator’s ledger contained the law through decree 1298 and he learned that decree 1299 set the olive tax to 6 drachmas per ton, he just changed the entry for the olive-tax law and noted that his ledger was complete through decree 1299. If he then learned about decree 1302, he would write it down in the back of the ledger and wait until he learned about decrees 1300 and 1301 before incorporating decree 1302 into the law book.

To enable a legislator who had been gone for a short time to catch up without copying the entire law book, legislators kept a list of the past week’s decrees in the back of the book. They could have kept this list on a slip of paper, but it was convenient for a legislator to enter decrees in the back of the ledger as they were passed and update the law book only two or three times a week.

3.3.3 Bureaucrats As Paxos prospered, legislators became very busy. Parliament could no longer handle all details of government, so a bureaucracy was established. Instead of passing a decree to declare whether each lot of cheese was fit for sale, Parliament passed a decree appointing a cheese inspector to make those decisions.

It soon became evident that selecting bureaucrats was not as simple as it first seemed. Parliament passed a decree making ∆ῐκστρα the first cheese inspector. After some months, merchants complained that ∆ῐκστρα was too strict and was rejecting perfectly good cheese. Parliament then replaced him by passing the decree

1375: Γωυδα is the new cheese inspector

But ∆ῐκστρα did not pay close attention to what Parliament did, so he did not learn of this decree right away. There was a period of confusion in the cheese market when both ∆ῐκστρα and Γωυδα were inspecting cheese and making conflicting decisions.

To prevent such confusion, the Paxons had to guarantee that a position could be held by at most one bureaucrat at any time. To do this, a president included as part of each decree the time and date when it was proposed. A decree making ∆ῐκστρα the cheese inspector might read

2716: 8:30 15 Jan 72—∆ῐκστρα is cheese inspector for 3 months

This declares his term to begin either at 8:30 on 15 January or when the previous inspector’s term ended—whichever was later. His term would end at 8:30 on 15 March, unless he explicitly resigned by asking the president to pass a decree like

2834: 9:15 3 Mar 72—∆ῐκστρα resigns as cheese inspector

A bureaucrat was appointed for a short term, so he could be replaced quickly— for example, if he left the island. Parliament would pass a decree to extend the bureaucrat’s term if he was doing a satisfactory job.

A bureaucrat needed to tell time to determine if he currently held a post. Mechanical clocks were unknown on Paxos, but Paxons could tell time accurately to within 15 minutes by the position of the sun or the stars. 13 If ∆ῐκστρα’s term began at 8:30, he would not start inspecting cheese until his celestial observations indicated that it was 8:45.

It is easy to make this method of appointing bureaucrats work if higher-numbered decrees always have later proposal times. But what if Parliament passed the decrees

2854: 9:45 9 Apr 78—Φρανσζ is wine taster for 2 months 2855: 9:20 9 Apr 78—Πνυλῐ is wine taster for 1 month

13 Cloudy days are rare in Paxos’s balmy climate.

that were proposed between 9:30 and 9:35 by different legislators who both thought they were president? Such out-of-order proposal times are easily prevented because the parliamentary protocol satisfies the following property.

If two decrees are passed by different presidents, then one of the presidents proposed his decree after learning that the other decree had been proposed.

To see that this property is satisfied, suppose that ballot number $b$ was successful for decree $D$, ballot number $b'$ was successful for decree $D'$, and $b < b'$. Let $q$ be a legislator who voted in both ballots. The balloting for $D'$ began with a $NextBallot(b', n)$ message. If the sender of that message did not already know about $D$, then $n$ is less than the decree number of $D$, and $q$'s reply to the $NextBallot$ message must state that he voted for $D$.

3.3.4 Learning the Law In addition to requesting the passage of decrees, ordinary citizens needed to inquire about the current law of the land. The Paxons at first thought that a citizen could simply examine the ledger of any legislator, but the following incident demonstrated that a more sophisticated approach was needed. For centuries, it had been legal to sell only white goats. A farmer named $\Delta\omega\lambda\varepsilon\varphi$ got Parliament to pass the decree

77: The sale of black goats is permitted

$\Delta\omega\lambda\varepsilon\varphi$ then instructed his goatherd to sell some black goats to a merchant named $\Sigma\kappa\varepsilon\varepsilon\nu$. As a law-abiding citizen, $\Sigma\kappa\varepsilon\varepsilon\nu$ asked legislator $\Sigma\pi\omega\kappa\mu\varepsilonῖ\rho$ if such a sale would be legal. But $\Sigma\pi\omega\kappa\mu\varepsilonῖ\rho$ had been out of the Chamber and had no entry in his ledger past decree 76. He advised $\Sigma\kappa\varepsilon\varepsilon\nu$ that the sale would be illegal under the current law, so $\Sigma\kappa\varepsilon\varepsilon\nu$ refused to buy the goats.

This incident led to the formulation of the following monotonicity condition on inquiries about the law.

If one inquiry precedes a second inquiry, then the second inquiry cannot reveal an earlier state of the law than the first.

If a citizen learns that a particular decree has been passed, then the process of acquiring that knowledge is considered to be an implicit inquiry to which this condition applies. As we will see, the interpretation of the monotonicity condition changed over the years.

Initially, the monotonicity condition was achieved by passing a decree for each inquiry. If $\Sigma\delta\nu\iota\delta\varepsilon\rho$ wanted to know the current tax on olives, he would get Parliament to pass a decree such as

87: Citizen $\Sigma\delta\nu\iota\delta\varepsilon\rho$ is reading the law

He would then read any ledger complete at least through decree 86 to learn the olive tax as of that decree. If citizen $\Gamma\rho\varepsilon\varepsilon\varsigma$ then inquired about the olive tax, the decree for his inquiry was proposed after decree 87 was passed, so the decree-ordering property (Section 3.2.1) implies that it received a decree number greater than 87. Therefore, $\Gamma\rho\varepsilon\varepsilon\varsigma$ could not obtain an earlier value of the olive tax than $\Sigma\delta\nu\iota\delta\varepsilon\rho$.

This method of reading the law satisfied the monotonicity condition when precedes was interpreted to mean that inquiry A precedes inquiry B iff A finished at an earlier time than B began.

Passing a decree for every inquiry soon proved too cumbersome. The Paxons realized that a simpler method was possible if they weakened the monotonicity condition by changing the interpretation of precedes. They decided that for one event to precede another, the first event not only had to happen at an earlier time, but it had to be able to causally affect the second event. The weaker monotonicity condition prevents the problem first encountered by farmer ∆ωλφ and merchant Σκν because there is a causal chain of events between the end of the implicit inquiry by ∆ωλφ and the beginning of the inquiry by Σκν.

The weaker monotonicity condition was met by using decree numbers in all business transactions and inquiries. For example, farmer ∆ωλφ, whose flock included many nonwhite goats, got Parliament to pass the decree

277: The sale of brown goats is permitted

When selling his brown goats to Σκν, he informed the merchant that the sale was legal as of decree number 277. Σκν then asked legislator Στωκµῐρ if the sale were legal under the law through at least decree 277. If Στωκµῐρ’s ledger was not complete through decree 277, he would either wait until it was or else tell Σκν to ask someone else. If Στωκµῐρ’s ledger went through decree 298, then he would tell Σκν that the sale was legal as of decree number 298. Merchant Σκν would remember the number 298 for use in his next business transaction or inquiry about the law.

The Paxons had satisfied the monotonicity condition, but ordinary citizens disliked having to remember decree numbers. Again, the Paxons solved the problem by re-interpreting the monotonicity condition—this time, by changing the meaning of state of the law. They divided the law into separate areas, and a legislator was chosen as specialist for each area. The current state of each area of the law was determined by that specialist’s ledger. For example, suppose decree 1517 changed the tariff law and decree 1518 changed the tax law. The tax law would change first if the tax-law specialist learned of both decrees before the tariff-law specialist learned of either, yielding a state of the law that could not be obtained by enacting the decrees in numerical order.

To avoid conflicting definitions of the current state, the Paxons required that there be at most one specialist at a time for any area. This requirement was satisfied by using the same method to choose specialists that was used to choose bureaucrats (see Section 3.3.3). If each inquiry involved only a single area of the law, monotonicity was then achieved by directing the inquiry to that area’s specialist, who answered it from his ledger. Since learning that a law had passed constituted the result of an implicit inquiry, the Paxons required that a decree change at most one area of the law, and that notification of the decree’s passage could come only from the area’s specialist.

Inquiries involving multiple areas were not hard to handle. When merchant Λισκωφ asked if the tariff on an imported golden fleece was higher than the sales tax on one purchased locally, the tax-law and tariff-law specialists had to cooperate to provide an answer. For example, the tax specialist could answer Λισκωφ by first asking the tariff specialist for the tariff on golden fleeces, so long as he made no changes to his ledger before receiving a reply.

This method proved satisfactory until it became necessary to make a sweeping change to several areas of the law at one time. The Paxons then realized that the necessary requirement for maintaining monotonicity was not that a decree affect only a single area, but that every area it affects have the same specialist. Parliament could change several areas of the law with a single decree by first appointing a single legislator to be the specialist for all those areas. Moreover, the same area could have multiple specialists, so long as that area of the law was not allowed to change. Just before income taxes were due, Parliament would appoint several tax-law specialists to handle the seasonal flood of inquiries about the tax law.

3.3.5 Dishonest Legislators and Honest Mistakes Despite official assertions to the contrary, there must have been a few dishonest legislators in the history of Paxos. When caught, they were probably exiled. By sending contradictory messages, a malicious legislator could cause different legislators’ ledgers to be inconsistent. Inconsistency could also result from a lapse of memory by an honest legislator or messenger.

When inconsistencies were recognized, they could easily be corrected by passing decrees. For example, disagreement about the current olive tax could be eliminated by passing a new decree declaring the tax to have a certain value. The difficult problem lay in correcting inconsistent ledgers even if no one was aware of the inconsistency.

The existence of dishonesty or mistakes by legislators can be inferred from the redundant decrees that began appearing in ledgers several years after the founding of Parliament. For example, the decree

2605: The olive tax is 9 drachmas per ton was passed even though decree 2155 had already set the olive tax to 9 drachmas per ton, and no intervening decree had changed it. Parliament apparently cycled through its laws every six months so that even if legislators’ ledgers were initially inconsistent, all legislators would agree on the current law of the land within six months. It is believed that by the use of these redundant decrees, the Paxons made their Parliament self-stabilizing. (Self-stabilizing is a modern term due to Dijkstra [Dijkstra 1974].)

It is not clear precisely what self-stabilization meant in a Parliament with legislators coming and going at will. The Paxons would not have been satisfied with a definition that required all legislators to be in the Chamber at one time before consistency could be guaranteed. However, achieving consistency required that if one legislator had an entry in his ledger for a certain decree number and another did not, then the second legislator would eventually fill in that entry.

Unfortunately, we don’t know exactly what sort of self-stabilization property the Paxon Parliament possessed or how it was achieved. Paxon mathematicians undoubtedly addressed the problem, but their work has not yet been found. I hope that future archaeological expeditions to Paxos will give high priority to the search for manuscripts on self-stabilization.

3.3.6 Choosing New Legislators At first, membership in Parliament was hereditary, passing from parent to child. When the elder statesman Παρνας retired, he gave his ledger to his son, who carried on without interruption. It made no difference to other legislators which Παρνας they communicated with.

As old families emigrated and new ones immigrated, this system had to change. The Paxons decided to add and remove members of Parliament by decree. This posed a circularity problem: membership in Parliament was determined by which decrees were passed, but passing a decree required knowing what constituted a majority set, which in turn depended upon who was a member of Parliament. The circularity was broken by letting the membership of Parliament used in passing decree n be specified by the law as of decree n − 3. A president could not try to pass decree 3255 until he knew all decrees through decree 3252. In practice, after passing the decree

3252: Στρωνγ is now a legislator the president would immediately pass the “olive-day” decree as decrees 3253 and 3254.

Changing the composition of Parliament in this way was dangerous and had to be done with care. The consistency and progress conditions would always hold. However, the progress condition guaranteed progress only if a majority set was in the Chamber; it did not guarantee that a majority set would ever be there. In fact, the mechanism for choosing legislators led to the downfall of the Parliamentary system in Paxos. Because of a scribe’s error, a decree that was supposed to honor sailors who had drowned in a shipwreck instead declared them to be the only members of Parliament. Its passage prevented any new decrees from being passed— including the decrees proposed to correct the mistake. Government in Paxos came to a halt. A general named Λαµπσων took advantage of the confusion to stage a coup, establishing a military dictatorship that ended centuries of progressive government. Paxos grew weak under a series of corrupt dictators, and was unable to repel an invasion from the east that led to the destruction of its civilization.
