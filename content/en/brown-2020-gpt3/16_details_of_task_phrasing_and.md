---
paper: brown-2020-gpt3
title: Language Models are Few-Shot Learners
authors:
  - Tom B. Brown
  - Benjamin Mann
  - Nick Ryder
  - Melanie Subbiah
  - Jared Kaplan
  - Prafulla Dhariwal
  - Arvind Neelakantan
  - Pranav Shyam
  - Girish Sastry
  - Amanda Askell
year: 2020
venue: NeurIPS
field: ai-ml
section: G
section_title: Details of Task Phrasing and Specifications
tag: "0205"
kind: appendix
lang: en
source: arxiv:2005.14165
pdf_sha256: 97fd272f1fdfc18677462d0292f5fbf26ca86b4d1b485c2dba03269b643a0e83
pdf_pages: 50-62
extraction: vision
extraction_model: gpt-5
content_sha256: 8c1805dd37edf3e3c962a55620b8381d5fbdf5e5ddf5415a162d40f7c59b76dc
prompt_sha256: e1b070d511afab62a45db64b491e759e38eaa12f6c7943b773a942f4f2f70935
---

The following figures illustrate the formatting and phrasing of all the tasks included in the paper. All data comes from the ground truth datasets in this section, and no samples from GPT-3 are included here.

| Context → | Article: Informal conversation is an important part of any business relationship. Before you start a discussion, however, make sure you understand which topics are suitable and which are considered taboo in a particular culture. Latin Americans enjoy sharing information about their local history, art and customs. You may expect questions about your family, and be sure to show pictures of your children. You may feel free to ask similar questions of your Latin American friends. The French think of conversation as an art form, and they enjoy the value of lively discussions as well as disagreements. For them, arguments can be interesting and they can cover pretty much or any topic ---- as long as they occur in are respectful and intelligent manner. In the United States, business people like to discuss a wide range of topics, including opinions about work, family, hobbies, and politics. In Japan, China, and Korea, however, people are much more private. They do not share much about their thoughts, feelings, or emotions because they feel that doing so might take away from the harmonious business relationship they’re trying to build. Middle Easterners are also private about their personal lives and family matters. It is considered rude, for example, to ask a businessman from Saudi Arabia about his wife or children. As a general rule, it’s best not to talk about politics or religion with your business friends. This can get you into trouble, even in the United States, where people hold different religious views. In addition, discussing one’s salary is usually considered unsuitable. Sports is typically a friendly subject in most parts of the world, although be careful not to criticize national sport. Instead, be friendly and praise your host’s team. Q: What shouldn’t you do when talking about sports with colleagues from another country? A: Criticizing the sports of your colleagues’ country. Q: Which is typically a friendly topic in most places according to the author? A: Sports. Q: Why are people from Asia more private in their conversation with others? A: They don’t want to have their good relationship with others harmed by informal conversation. Q: The author considers politics and religion _ . A: |
| --- | --- |
| Correct Answer → | taboo |
| Incorrect Answer → | cheerful topics |
| Incorrect Answer → | rude topics |
| Incorrect Answer → | topics that can never be talked about |

Figure G.1: Formatted dataset example for RACE-h. When predicting, we normalize by the unconditional probability of each answer as described in 2.

| Context | anli 2: anli 2: The Gold Coast Hotel & Casino is a hotel and casino located in Paradise, Nevada. This locals’ casino is owned and operated by Boyd Gaming. The Gold Coast is located one mile (~ 1.6km) west of the Las Vegas Strip on West Flamingo Road. It is located across the street from the Palms Casino Resort and the Rio All Suite Hotel and Casino. Question: The Gold Coast is a budget-friendly casino. True, False, or Neither? |
| --- | --- |
| Correct Answer | Neither |
| Incorrect Answer | True |
| Incorrect Answer | False |

Figure G.2: Formatted dataset example for ANLI R2

| Context | Article: Mrs. Smith is an unusual teacher. Once she told each student to bring along a few potatoes in plastic bag. On each potato the students had to write a name of a person that they hated And the next day, every child brought some potatoes. Some had two potatoes; some three; some up to five. Mrs. Smith then told the children to carry the bags everywhere they went, even to the toilet, for two weeks. As day after day passed, the children started to complain about the awful smell of the rotten potatoes. Those children who brought five potatoes began to feel the weight trouble of the bags. After two weeks, the children were happy to hear that the game was finally ended. Mrs. Smith asked,"How did you feel while carrying the potatoes for two weeks?" The children started complaining about the trouble loudly. Then Mrs. Smith told them why she asked them to play the game. She said,"This is exactly the situation when you carry your hatred for somebody inside your heart. The terrible smell of the hatred will pollute your heart and you will carry something unnecessary with you all the time. If you cannot stand the smell of the rotten potatoes for just two weeks, can you imagine how heavy it would be to have the hatred in your heart for your lifetime? So throw away any hatred from your heart, and you’ll be really happy." Q: Which of the following is True according to the passage? A: If a kid hated four people, he or she had to carry four potatoes. Q: We can learn from the passage that we should _ . A: throw away the hatred inside Q: The children complained about _ besides the weight trouble. A: the smell Q: Mrs. Smith asked her students to write _ on the potatoes. A: |
| --- | --- |
| Correct Answer | names |
| Incorrect Answer | numbers |
| Incorrect Answer | time |
| Incorrect Answer | places |

Figure G.3: Formatted dataset example for RACE-m. When predicting, we normalize by the unconditional probability of each answer as described in 2.

| Context | How to apply sealant to wood. |
| --- | --- |
| Correct Answer | Using a brush, brush on sealant onto wood until it is fully saturated with the sealant. |
| Incorrect Answer | Using a brush, drip on sealant onto wood until it is fully saturated with the sealant. |

Figure G.4: Formatted dataset example for PIQA

| Context | My body cast a shadow over the grass because |
| --- | --- |
| Correct Answer | the sun was rising. |
| Incorrect Answer | the grass was cut. |

Figure G.5: Formatted dataset example for COPA

| Context | (CNN) Yuval Rabin, whose father, Yitzhak Rabin, was assassinated while serving as Prime Minister of Israel, criticized Donald Trump for appealing to "Second Amendment people" in a speech and warned that the words that politicians use can incite violence and undermine democracy. "Trump’s words are an incitement to the type of political violence that touched me personally," Rabin wrote in USAToday. He said that Trump’s appeal to "Second Amendment people" to stop Hillary Clinton -- comments that were criticized as a call for violence against Clinton, something Trump denied -- "were a new level of ugliness in an ugly campaign season." - The son of a former Israeli Prime Minister who was assassinated wrote an op ed about the consequence of violent political rhetoric. - Warns of "parallels" between Israel of the 1990s and the U.S. today. |
| --- | --- |
| Correct Answer | - Referencing his father, who was shot and killed by an extremist amid political tension in Israel in 1995, Rabin condemned Donald Trump’s aggressive rhetoric. |
| Correct Answer | - Referencing his father, who was shot and killed by an extremist amid political tension in Israel in 1995, Rabin condemned Trump’s aggressive rhetoric. |
| Incorrect Answer | - Referencing his father, who was shot and killed by an extremist amid political tension in Israel in 1995, Rabin condemned Hillary Clinton’s aggressive rhetoric. |
| Incorrect Answer | - Referencing his father, who was shot and killed by an extremist amid political tension in Israel in 1995, Rabin condemned U.S.’s aggressive rhetoric. |
| Incorrect Answer | - Referencing his father, who was shot and killed by an extremist amid political tension in Israel in 1995, Rabin condemned Yitzhak Rabin’s aggressive rhetoric. |

Figure G.6: Formatted dataset example for ReCoRD. We consider the context above to be a single ”problem” because this is how the task is presented in the ReCoRD dataset and scored in the ReCoRD evaluation script.

| Context | anli 1: anli 1: Fulton James MacGregor MSP is a Scottish politician who is a Scottish National Party (SNP) Member of Scottish Parliament for the constituency of Coatbridge and Chryston. MacGregor is currently Parliamentary Liaison Officer to Shona Robison, Cabinet Secretary for Health & Sport. He also serves on the Justice and Education & Skills committees in the Scottish Parliament. Question: Fulton James MacGregor is a Scottish politician who is a Liaison officer to Shona Robison who he swears is his best friend. True, False, or Neither? |
| --- | --- |
| Correct Answer | Neither |
| Incorrect Answer | True |
| Incorrect Answer | False |

Figure G.7: Formatted dataset example for ANLI R1

| Context | Organisms require energy in order to do what? |
| --- | --- |
| Correct Answer | mature and develop. |
| Incorrect Answer | rest soundly. |
| Incorrect Answer | absorb light. |
| Incorrect Answer | take in nutrients. |

Figure G.8: Formatted dataset example for OpenBookQA. When predicting, we normalize by the unconditional probability of each answer as described in 2.

| Context | Making a cake: Several cake pops are shown on a display. A woman and girl are shown making the cake pops in a kitchen. They |
| --- | --- |
| Correct Answer | bake them, then frost and decorate. |
| Incorrect Answer | taste them as they place them on plates. |
| Incorrect Answer | put the frosting on the cake as they pan it. |
| Incorrect Answer | come out and begin decorating the cake as well. |

Figure G.9: Formatted dataset example for HellaSwag

| Context | anli 3: anli 3: We shut the loophole which has American workers actually subsidizing the loss of their own job. They just passed an expansion of that loophole in the last few days: \$43 billion of giveaways, including favors to the oil and gas industry and the people importing ceiling fans from China. Question: The loophole is now gone True, False, or Neither? |
| --- | --- |
| Correct Answer | False |
| Incorrect Answer | True |
| Incorrect Answer | Neither |

Figure G.10: Formatted dataset example for ANLI R3

| Context | Question: George wants to warm his hands quickly by rubbing them. Which skin surface will produce the most heat? Answer: |
| --- | --- |
| Correct Answer | dry palms |
| Incorrect Answer | wet palms |
| Incorrect Answer | palms covered with oil |
| Incorrect Answer | palms covered with lotion |

Figure G.11: Formatted dataset example for ARC (Challenge). When predicting, we normalize by the unconditional probability of each answer as described in 2.

| Context | lull is to trust as |
| --- | --- |
| Correct Answer | cajole is to compliance |
| Incorrect Answer | balk is to fortitude |
| Incorrect Answer | betray is to loyalty |
| Incorrect Answer | hinder is to destination |
| Incorrect Answer | soothe is to passion |

Figure G.12: Formatted dataset example for SAT Analogies

| Correct Context | Grace was happy to trade me her sweater for my jacket. She thinks the sweater |
| --- | --- |
| Incorrect Context | Grace was happy to trade me her sweater for my jacket. She thinks the jacket |
| Target Completion | looks dowdy on her. |

Figure G.13: Formatted dataset example for Winograd. The 'partial' evaluation method we use compares the probability of the completion given a correct and incorrect context.

| Correct Context → | Johnny likes fruits more than vegetables in his new keto diet because the fruits |
| --- | --- |
| Incorrect Context → | Johnny likes fruits more than vegetables in his new keto diet because the vegetables |
| Target Completion → | are saccharine. |

Figure G.14: Formatted dataset example for Winogrande. The ‘partial’ evaluation method we use compares the probability of the completion given a correct and incorrect context.

| Context → | READING COMPREHENSION ANSWER KEY While this process moved along, diplomacy continued its rounds. Direct pressure on the Taliban had proved unsuccessful. As one NSC staff note put it, "Under the Taliban, Afghanistan is not so much a state sponsor of terrorism as it is a state sponsored by terrorists." In early 2000, the United States began a high-level effort to persuade Pakistan to use its influence over the Taliban. In January 2000, Assistant Secretary of State Karl Inderfurth and the State Department’s counterterrorism coordinator, Michael Sheehan, met with General Musharraf in Islamabad, dangling before him the possibility of a presidential visit in March as a reward for Pakistani cooperation. Such a visit was coveted by Musharraf, partly as a sign of his government’s legitimacy. He told the two envoys that he would meet with Mullah Omar and press him on Bin Laden. They left, however, reporting to Washington that Pakistan was unlikely in fact to do anything," given what it sees as the benefits of Taliban control of Afghanistan." President Clinton was scheduled to travel to India. The State Department felt that he should not visit India without also visiting Pakistan. The Secret Service and the CIA, however, warned in the strongest terms that visiting Pakistan would risk the President’s life. Counterterrorism officials also argued that Pakistan had not done enough to merit a presidential visit. But President Clinton insisted on including Pakistan in the itinerary for his trip to South Asia. His one-day stopover on March 25, 2000, was the first time a U.S. president had been there since 1969. At his meeting with Musharraf and others, President Clinton concentrated on tensions between Pakistan and India and the dangers of nuclear proliferation, but also discussed Bin Laden. President Clinton told us that when he pulled Musharraf aside for a brief, one-on-one meeting, he pleaded with the general for help regarding Bin Laden." I offered him the moon when I went to see him, in terms of better relations with the United States, if he’d help us get Bin Laden and deal with another issue or two." The U.S. effort continued. Who did The State Department feel should visit both India and Pakistan? |
| --- | --- |
| Correct Answer → | - [False] Bin Laden |
| Incorrect Answer → | - [True] Bin Laden |

Figure G.15: Formatted dataset example for MultiRC. There are three levels within MultiRC: (1) the passage, (2) the questions, and (3) the answers. During evaluation, accuracy is determined at the per-question level, with a question being considered correct if and only if all the answers within the question are labeled correctly. For this reason, we use $K$ to refer to the number of **questions** shown within the context.

| Context → | Question: Which factor will most likely cause a person to develop a fever? Answer: |
| --- | --- |
| Correct Answer → | a bacterial population in the bloodstream |
| Incorrect Answer → | a leg muscle relaxing after exercise |
| Incorrect Answer → | several viral particles on the skin |
| Incorrect Answer → | carbohydrates being digested in the stomach |

Figure G.16: Formatted dataset example for ARC (Easy). When predicting, we normalize by the unconditional probability of each answer as described in 2.

| Context → | Bob went to the gas station to fill up his car. His tank was completely empty and so was his wallet. The cashier offered to pay for his gas if he came back later to pay. Bob felt grateful as he drove home. |
| --- | --- |
| Correct Answer → | Bob believed that there were good people in the world. |
| Incorrect Answer → | Bob contemplated how unfriendly the world was. |

Figure G.17: Formatted dataset example for StoryCloze

| Context → | Helsinki is the capital and largest city of Finland. It is in the region of Uusimaa, in southern Finland, on the shore of the Gulf of Finland. Helsinki has a population of , an urban population of , and a metropolitan population of over 1.4 million, making it the most populous municipality and urban area in Finland. Helsinki is some north of Tallinn, Estonia, east of Stockholm, Sweden, and west of Saint Petersburg, Russia. Helsinki has close historical connections with these three cities. The Helsinki metropolitan area includes the urban core of Helsinki, Espoo, Vantaa, Kauniainen, and surrounding commuter towns. It is the world’s northernmost metro area of over one million people, and the city is the northernmost capital of an EU member state. The Helsinki metropolitan area is the third largest metropolitan area in the Nordic countries after Stockholm and Copenhagen, and the City of Helsinki is the third largest after Stockholm and Oslo. Helsinki is Finland’s major political, educational, financial, cultural, and research center as well as one of northern Europe’s major cities. Approximately 75% of foreign companies that operate in Finland have settled in the Helsinki region. The nearby municipality of Vantaa is the location of Helsinki Airport, with frequent service to various destinations in Europe and Asia. Q: what is the most populous municipality in Finland? A: Helsinki Q: how many people live there? A: 1.4 million in the metropolitan area Q: what percent of the foreign companies that operate in Finland are in Helsinki? A: 75% Q: what towns are a part of the metropolitan area? A: |
| --- | --- |
| Target Completion → | Helsinki, Espoo, Vantaa, Kauniainen, and surrounding commuter towns |

Figure G.18: Formatted dataset example for CoQA

| Context → | Please unscramble the letters into a word, and write that word: asinoc = |
| --- | --- |
| Target Completion → | casino |

Figure G.19: Formatted dataset example for Cycled Letters

| Context → | Passage: Saint Jean de Brébeuf was a French Jesuit missionary who travelled to New France in 1625. There he worked primarily with the Huron for the rest of his life, except for a few years in France from 1629 to 1633. He learned their language and culture, writing extensively about each to aid other missionaries. In 1649, Brébeuf and another missionary were captured when an Iroquois raid took over a Huron village. Together with Huron captives, the missionaries were ritually tortured and killed on March 16, 1649. Brébeuf was beatified in 1925 and among eight Jesuit missionaries canonized as saints in the Roman Catholic Church in 1930. Question: How many years did Saint Jean de Brébeuf stay in New France before he went back to France for a few years? Answer: |
| --- | --- |
| Target Completion → | 4 |

Figure G.20: Formatted dataset example for DROP

| Context → | Fill in blank: She held the torch in front of her. She caught her breath. "Chris? There’s a step." "What?" "A step. Cut in the rock. About fifty feet ahead." She moved faster. They both moved faster. "In fact," she said, raising the torch higher, "there’s more than a _____. -> |
| --- | --- |
| Target Completion → | step |

Figure G.21: Formatted dataset example for LAMBADA

| Context → | Please unscramble the letters into a word, and write that word: skicts = |
| --- | --- |
| Target Completion → | sticks |

Figure G.22: Formatted dataset example for Anagrams 1 (A1)

| Context → | Please unscramble the letters into a word, and write that word: volwskagen = |
| --- | --- |
| Target Completion → | volkswagen |

Figure G.23: Formatted dataset example for Anagrams 2

| Context → | Q: Who played tess on touched by an angel? A: |
| --- | --- |
| Target Completion → | Delloreese Patricia Early (July 6, 1931 { November 19, 2017), known professionally as Della Reese |

Figure G.24: Formatted dataset example for Natural Questions

Context → TITLE: William Perry (American football) - Professional career
PARAGRAPH: In 1985, he was selected in the first round of the 1985 NFL Draft by the Chicago Bears; he had been hand-picked by coach Mike Ditka. However, defensive coordinator Buddy Ryan, who had a highly acrimonious relationship with Ditka, called Perry a "wasted draft-pick". Perry soon became a pawn in the political power struggle between Ditka and Ryan. Perry’s "Refrigerator" nickname followed him into the NFL and he quickly became a favorite of the Chicago Bears fans. Teammates called him "Biscuit," as in "one biscuit shy of 350 pounds." While Ryan refused to play Perry, Ditka decided to use Perry as a fullback when the team was near the opponents’ goal line or in fourth and short situations, either as a ball carrier or a lead blocker for star running back Walter Payton. Ditka stated the inspiration for using Perry as a fullback came to him during five-yard sprint exercises. During his rookie season, Perry rushed for two touchdowns and caught a pass for one. Perry even had the opportunity to run the ball during Super Bowl XX, as a nod to his popularity and contributions to the team’s success. The first time he got the ball, he was tackled for a one-yard loss while attempting to throw his first NFL pass on a halfback option play. The second time he got the ball, he scored a touchdown (running over Patriots linebacker Larry McGrew in the process). About halfway through his rookie season, Ryan finally began to play Perry, who soon proved that he was a capable defensive lineman. His Super Bowl ring size is the largest of any professional football player in the history of the event. His ring size is 25, while the ring size for the average adult male is between 10 and 12. Perry went on to play for ten years in the NFL, retiring after the 1994 season. In his ten years as a pro, he regularly struggled with his weight, which hampered his performance at times. He played in 138 games, recording 29.5 sacks and five fumble recoveries, which he returned for a total of 71 yards. In his offensive career he ran five yards for two touchdowns, and had one reception for another touchdown. Perry later attempted a comeback, playing an unremarkable 1996 season with the London Monarchs of the World League of American Football (later NFL Europa).

Q: what team did he play for?

A:

Target Completion → the Chicago Bears

Figure G.25: Formatted dataset example for QuAC

Context → Please unscramble the letters into a word, and write that word:
r e!c.i p r o.c a/l =

Target Completion → reciprocal

Figure G.26: Formatted dataset example for Symbol Insertion

Context → Please unscramble the letters into a word, and write that word:
taefed =

Target Completion → defeat

Figure G.27: Formatted dataset example for Reversed Words

Context → Title: The Blitz

Background: From the German point of view, March 1941 saw an improvement. The Luftwaffe flew 4,000 sorties that month, including 12 major and three heavy attacks. The electronic war intensified but the Luftwaffe flew major inland missions only on moonlit nights. Ports were easier to find and made better targets. To confuse the British, radio silence was observed until the bombs fell. X- and Y-Gerät beams were placed over false targets and switched only at the last minute. Rapid frequency changes were introduced for X-Gerät, whose wider band of frequencies and greater tactical flexibility ensured it remained effective at a time when British selective jamming was degrading the effectiveness of Y-Gerät.

Q: How many sorties were flown in March 1941?

A: 4,000

Q: When did the Luftwaffe fly inland missions?

A:

Target Completion → only on moonlit nights

Figure G.28: Formatted dataset example for SQuADv2

Context → Normal force -- In a simple case such as an object resting upon a table, the normal force on the object is equal but in opposite direction to the gravitational force applied on the object (or the weight of the object), that is, N = m g (\displaystyle N=mg), where m is mass, and g is the gravitational field strength (about 9.81 m/s on Earth). The normal force here represents the force applied by the table against the object that prevents it from sinking through the table and requires that the table is sturdy enough to deliver this normal force without breaking. However, it is easy to assume that the normal force and weight are action-reaction force pairs (a common mistake). In this case, the normal force and weight need to be equal in magnitude to explain why there is no upward acceleration of the object. For example, a ball that bounces upwards accelerates upwards because the normal force acting on the ball is larger in magnitude than the weight of the ball.
question: is the normal force equal to the force of gravity?
answer:

Target Completion → yes

Figure G.29: Formatted dataset example for BoolQ

Context → The trend toward lower rents may seem surprising given that some communities in New York are bemoaning the loss of favorite local businesses to high rents. But, despite the recent softening, for many of these retailers there’s still been too big a jump from the rental rates of the late 1970s, when their leases were signed. Certainly, the recent drop in prices doesn’t mean Manhattan comes cheap.
question: Manhattan comes cheap. true, false, or neither?
answer:

Target Completion → false

Figure G.30: Formatted dataset example for CB

| Context → | The bet, which won him dinner for four, was regarding the existence and mass of the top quark, an elementary particle discovered in 1995. question: The Top Quark is the last of six flavors of quarks predicted by the standard model theory of particle physics. True or False? answer: |
| --- | --- |
| Target Completion → | False |

Figure G.31: Formatted dataset example for RTE

| Context → | An outfitter provided everything needed for the safari. Before his first walking holiday, he went to a specialist outfitter to buy some boots. question: Is the word 'outfitter' used in the same way in the two sentences above? answer: |
| --- | --- |
| Target Completion → | no |

Figure G.32: Formatted dataset example for WiC

| Context → | Final Exam with Answer Key Instructions: Please carefully read the following passages. For each passage, you must identify which noun the pronoun marked in *bold* refers to. ===== Passage: Mr. Moncrieff visited Chester’s luxurious New York apartment, thinking that it belonged to his son Edward. The result was that Mr. Moncrieff has decided to cancel Edward’s allowance on the ground that he no longer requires *his* financial support. Question: In the passage above, what does the pronoun "*his*" refer to? Answer: |
| --- | --- |
| Target Completion → | mr. moncrieff |

Figure G.33: Formatted dataset example for WSC

| Context → | Q: 'Nude Descending A Staircase' is perhaps the most famous painting by which 20th century artist? A: |
| --- | --- |
| Target Completion → | MARCEL DUCHAMP |
| Target Completion → | r mutt |
| Target Completion → | duchamp |
| Target Completion → | marcel duchamp |
| Target Completion → | R.Mutt |
| Target Completion → | Marcel duChamp |
| Target Completion → | Henri-Robert-Marcel Duchamp |
| Target Completion → | Marcel du Champ |
| Target Completion → | henri robert marcel duchamp |
| Target Completion → | Duchampian |
| Target Completion → | Duchamp |
| Target Completion → | duchampian |
| Target Completion → | marcel du champ |
| Target Completion → | Marcel Duchamp |
| Target Completion → | MARCEL DUCHAMP |

Figure G.34: Formatted dataset example for TriviaQA. TriviaQA allows for multiple valid completions.

| Context → | Q: What school did burne hogarth establish? |
| --- | --- |
|  | A: |
| Target Completion → | School of Visual Arts |

Figure G.35: Formatted dataset example for WebQA

| Context → | Keinesfalls dürfen diese für den kommerziellen Gebrauch verwendet werden. = |
| --- | --- |
| Target Completion → | In no case may they be used for commercial purposes. |

Figure G.36: Formatted dataset example for De→En. This is the format for one- and few-shot learning, for this and other langauge tasks, the format for zero-shot learning is “Q: What is the {language} translation of {sentence} A: {translation}.”

| Context → | In no case may they be used for commercial purposes. = |
| --- | --- |
| Target Completion → | Keinesfalls dürfen diese für den kommerziellen Gebrauch verwendet werden. |

Figure G.37: Formatted dataset example for En→De

| Context → | Analysis of instar distributions of larval I. verticalis collected from a series of ponds also indicated that males were in more advanced instars than females. = |
| --- | --- |
| Target Completion → | L’analyse de la distribution de fréquence des stades larvaires d’I. verticalis dans une série d’étangs a également démontré que les larves mâles étaient à des stades plus avancés que les larves femelles. |

Figure G.38: Formatted dataset example for En→Fr

| Context → | L’analyse de la distribution de fréquence des stades larvaires d’I. verticalis dans une série d’étangs a également démontré que les larves mâles étaient à des stades plus avancés que les larves femelles. = |
| --- | --- |
| Target Completion → | Analysis of instar distributions of larval I. verticalis collected from a series of ponds also indicated that males were in more advanced instars than females. |

Figure G.39: Formatted dataset example for Fr→En

| Context → | The truth is that you want, at any price, and against the wishes of the peoples of Europe, to continue the negotiations for Turkey’s accession to the European Union, despite Turkey’s continuing refusal to recognise Cyprus and despite the fact that the democratic reforms are at a standstill. = |
| --- | --- |
| Target Completion → | Adevărul este că vă doriți, cu orice preț și împotriva dorinței europenilor, să continuați negocierile de aderare a Turciei la Uniunea Europeană, în ciuda refuzului continuu al Turciei de a recunoaște Ciprul și în ciuda faptului că reformele democratice au ajuns într-un punct mort. |

Figure G.40: Formatted dataset example for En→Ro

| Context → | Adevărul este că vă doriți, cu orice preț și împotriva dorinței europenilor, să continuați negocierile de aderare a Turciei la Uniunea Europeană, în ciuda refuzului continuu al Turciei de a recunoaște Ciprul și în ciuda faptului că reformele democratice au ajuns într-un punct mort. |
| --- | --- |
| Target Completion → | The truth is that you want, at any price, and against the wishes of the peoples of Europe, to continue the negotiations for Turkey’s accession to the European Union, despite Turkey’s continuing refusal to recognise Cyprus and despite the fact that the democratic reforms are at a standstill. |

Figure G.41: Formatted dataset example for Ro→En

| Context → | Q: What is (2 * 4) * 6? A: |
| --- | --- |
| Target Completion → | 48 |

Figure G.42: Formatted dataset example for Arithmetic 1DC

| Context → | Q: What is 17 minus 14? A: |
| --- | --- |
| Target Completion → | 3 |

Figure G.43: Formatted dataset example for Arithmetic 2D-

| Context → | Q: What is 98 plus 45? A: |
| --- | --- |
| Target Completion → | 143 |

Figure G.44: Formatted dataset example for Arithmetic 2D+

| Context → | Q: What is 95 times 45? A: |
| --- | --- |
| Target Completion → | 4275 |

Figure G.45: Formatted dataset example for Arithmetic 2Dx

| Context → | Q: What is 509 minus 488? A: |
| --- | --- |
| Target Completion → | 21 |

Figure G.46: Formatted dataset example for Arithmetic 3D-

| Context → | Q: What is 556 plus 497? A: |
| --- | --- |
| Target Completion → | 1053 |

Figure G.47: Formatted dataset example for Arithmetic 3D+

| Context → | Q: What is 6209 minus 3365? A: |
| --- | --- |
| Target Completion → | 2844 |

Figure G.48: Formatted dataset example for Arithmetic 4D-

| Context → | Q: What is 9923 plus 617? A: |
| --- | --- |
| Target Completion → | 10540 |

Figure G.49: Formatted dataset example for Arithmetic 4D+

| Context → | Q: What is 40649 minus 78746? A: |
| --- | --- |
| Target Completion → | -38097 |

Figure G.50: Formatted dataset example for Arithmetic 5D–

| Context → | Q: What is 65360 plus 16204? A: |
| --- | --- |
| Target Completion → | 81564 |

Figure G.51: Formatted dataset example for Arithmetic 5D+
