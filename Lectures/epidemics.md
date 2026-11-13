# EPIDEMICS
**CECS 427 DYNAMIC NETWORKS**[cite: 1]
**OSCAR MORALES PONCE**[cite: 1]

## Epidemic Diseases
* They are contagious diseases caused by biological pathogens (influenza, measles, and sexually transmitted diseases) spreading from person to person.[cite: 2]
* They can pass explosively through a population, or persist over long time periods at low levels.[cite: 2]
* They can experience sudden flare-ups or even wave-like cyclic patterns of increasing and decreasing prevalence.[cite: 2]
* A single disease outbreak can have significant effect on a whole civilization.[cite: 2]
* Examples: Epidemics caused by arrival of Europeans in the Americas; Bubonic plague that killed 20% of the population of Europe over a seven-year period in the 1300s.[cite: 2]

## Network Model: Epidemic Patterns
* Epidemic patterns depend on properties of the pathogen (including its contagiousness, the length of its infectious period, and its severity).[cite: 3]
* Epidemic patterns also depend on network structures within the population it is affecting.[cite: 3]
* Opportunities for a disease to spread are given by a contact network.[cite: 3]
* Social network within a population determines a lot about how the disease is likely to spread from one person to another.[cite: 3]
* There is a node for each person, and an edge if two people come into contact with each other in a way that makes it possible for the disease to spread from one to the other.[cite: 3]

## Pathogens and Contact Network Models
* The pathogen and the network are closely intertwined.[cite: 4]
* For a highly contagious disease, involving airborne transmission based on coughs and sneezes, the contact network will include a huge number of links.[cite: 4]
* Similarly, a piece of software infecting computers across the Internet will have a much broader contact network than one that spreads by short-range wireless communication between nearby mobile devices.[cite: 4]
* Modeling the underlying network is crucial to understanding the spread of an epidemic.[cite: 4]
* Contact networks are important in understanding how diseases spread through animal populations.[cite: 4]

## Diffusion of Ideas and Behaviors
* Diseases and ideas spread from person to person, across networks connecting people; similar structural mechanisms (contagion) are exhibited.[cite: 5]
* The biggest difference between biological and social contagion lies in the process by which one person "infects" another.[cite: 5]
* In social contagion, people are making decisions to adopt a new idea or innovation.[cite: 5]
* In diseases, there is no decision-making in the transmission from one person to another and the process is sufficiently complex and unobservable at the person-to-person level that it is most useful to model it as random.[cite: 5]
* Assumption: when two people are linked in the contact network, and one of them has the disease, there is a given probability that he or she will pass it to the other.[cite: 5]

## Branching Processes as a Model of Contagion
* 1st Wave: A person carrying a new disease enters a population of $k$ people, and transmits it to each person he meets independently with a probability of $p$.[cite: 6]
* 2nd Wave: Each person in the first wave goes out into the population and meets $k$ different people, resulting in a second wave of $k \cdot k = k^2$ people and transmit disease to each person they meet independently with probability $p$.[cite: 6]
* Subsequent Waves: are formed in the same way.[cite: 6]

*(Diagram Note: A tree diagram illustrates this branching process. It shows a single root node at the top connecting downwards to three child nodes. Each of those three nodes then connects to three additional nodes, demonstrating the outward branching multiplication effect of contagion waves.)*[cite: 7]

*(Diagram Note: A second tree diagram displays a "High Contagion Probability" scenario. It shows the same branching structure, but uses thick, bolded black lines to represent successful transmissions, showing the infection actively spreading deep into the network through multiple continuous paths.)*[cite: 8]

*(Diagram Note: A third tree diagram displays a "Low Contagion Probability" scenario. It features the branching structure but with only a few sparse, bolded lines, indicating that the infection fails to pass on to the majority of branches and dies out quickly.)*[cite: 9]

## Basic Reproductive Number
* Two possibilities in the branching process model: either the disease reaches a wave where it infects no one, thus dying out after a finite number of steps; or the disease continues to infect people in every wave, proceeding infinitely through the contact network.[cite: 10]
* Basic reproductive number, $R_0$, is the expected number of new cases of the disease caused by a single individual.[cite: 10]
* If everyone meets $k$ new people and infects each with probability $p$, the basic reproductive number is $R_0 = pk$.[cite: 10]
* Theorem. If $R_0 < 1$, then with probability 1, the disease dies out after a finite number of waves. If $R_0 > 1$ then with probability greater than 0 the disease persists by infecting at least one person in each wave.[cite: 10]

## Dichotomy and a Critical Value
* $R_0 = 1$ is the critical value: it can be worth investing large amounts of effort even to produce small shifts in the basic reproductive number.[cite: 11]
* In a branching process $R_0 = pk$: if $R_0$ is slightly below 1, and we increase the contagion probability $p$ by a little bit the result could push $R_0$ above 1, resulting in a positive probability of outbreak.[cite: 11]
* Same effect in reverse direction: slightly reducing the contagiousness of a disease to push $R_0$ below 1 can eliminate the risk of a large epidemic.[cite: 11]
* Two basic kinds of public-health measures: quarantining people (reduce $k$), and encouraging behavioral measures (sanitary practices to reduce spread of germs, which reduces $p$).[cite: 11]

## Examples
*(Diagram Note: A microscopic image depicting the Ebola virus structure.)*[cite: 12]

| Disease | $R_0$ |
| :--- | :--- |
| Covid 19 Alpha | 1.22 |
| Covid 19 Beta | 1.19 |
| Covid 19 Gamma | 1.21 |
| Covid 19 Delta | 1.38 |
| Covid Omicron | 1.90 |
| Ebola | 1.5-20 |
| Polio | 5-7 |
| Smallpox | 5-7 |
| Measles | 12-18 |
| Seasonal Influenza | 0.9-2.1 |
*All data from table.*[cite: 12]

## SIR Epidemic Model: Principle
* Individual nodes in branching process model go through three potential stages during the course of epidemic:[cite: 13]
* Susceptible (S): Before node has caught the disease, it is susceptible to infection from its neighbors.[cite: 13]
* Infectious (I): Once node has caught the disease, it is infectious and has some probability of infecting each of its susceptible neighbors.[cite: 13]
* Removed (R): After node has experienced the full infectious period, it is removed from consideration, since it no longer poses a threat of future infection.[cite: 13]
* Using this three-stage life-cycle for the disease at each node, we can define a model for epidemics on networks.[cite: 13]

## SIR Epidemic Model: General Contact Structure
* Given a directed graph representing the contact network.[cite: 14]
* Each node has the potential to go through the S-I-R cycle.[cite: 14]
* Progress of the epidemic is controlled by the contact network structure, $p$ (the probability of contagion), and $t_1$ (the length of the infection).[cite: 14]
* Initially, some nodes are in the I state, and all others are in the S state.[cite: 15]
* Each node $v$ that enters the I state remains infectious for a fixed number of steps $t_1$.[cite: 15]
* During each of these $t_1$ steps, $v$ has a probability $p$ of passing the disease to each of its susceptible neighbors.[cite: 15]
* After $t_1$ steps, node $v$ is no longer infectious or susceptible to further bouts of the disease; node is described as removed (R), since it is now an inert node in the contact network that can no longer either catch or transmit the disease.[cite: 15]

## SIR Epidemic Example
* Each node remains infectious for a number of steps equal to $t_1 = 1$.[cite: 16]
* *(Diagram Note: A network graph consisting of nodes labeled r, s, t, u, v, w, x, y, and z connected by paths.)*[cite: 16]
* Initially infected: nodes y, z. *(Diagram Note: Nodes y and z are highlighted in red).*[cite: 17]
* Nodes y, z are removed, and x and v are infected. *(Diagram Note: Nodes y and z are now shaded gray for 'removed', while nodes x and v are highlighted in red).*[cite: 18]
* Nodes r is infected. *(Diagram Note: Node x is now gray, node r is highlighted in red. Node v also changes to gray).*[cite: 19]
* Nodes r is removed. *(Diagram Note: Node r is now shaded gray. All previously infected nodes are now in the removed state).*[cite: 20]

## Extensions to the SIR Model
* SIR model is most appropriate for a disease individuals catch only once in their lifetime; after infection, node removed either because it has acquired lifetime immunity or because the disease has killed it.[cite: 21]
* Two generalizations: Assign separate probability $P_{v,w}$ to each pair of nodes $v, w$ for which $v$ links to $w$ in directed contact network.[cite: 21]
* Model infectious period as random in length, by assuming that an infected node has a probability $q$ of recovering in each step while it is infected.[cite: 21]
* More elaborate extensions to the model involve separating the I state into a sequence of several states.[cite: 21]

## Percolation
* It is equivalent static view of SIR epidemic process with $t_1 = 1$.[cite: 22]
* Consider time when a node $v$ has just become infectious, and it has a susceptible neighbor $w$: $v$ has one chance to infect $w$ (since $t_1 = 1$) and succeeds with probability $p$.[cite: 22]
* Outcome of this random event determined by flipping a coin: probability $p$ of coming up "heads" and observing the outcome.[cite: 22]
* For each edge ($v, w$) in contact network a coin with "heads probability" $p$ is flipped at the very beginning of the process (independently of the coins for all other pairs of neighbors), and result is stored so that it can be later checked in the event that $v$ becomes infectious while $w$ is susceptible.[cite: 22]

## SIR Epidemic and Percolation
* *(Diagram Note: The network graph of nodes r-z is shown with directed arrows. Nodes y and z are highlighted in red as infected).*[cite: 23]
* Edges in the contact network for which the coin flip is successful are declared to be open; remaining blocked. *(Diagram Note: Specific directed paths between nodes are highlighted with red arrows to signify open pathways, while others are black for blocked).*[cite: 24]
* Percolation View: A node $v$ will become infected during the epidemic if and only if there is a path to $v$ from one of the initially infected nodes that consists entirely of open edges. *(Diagram Note: The diagram shows how the infection successfully follows the red 'open' paths from the source nodes to infect r, v, and x, leaving them red, while others are gray).*[cite: 25]

## SIS Epidemic Model
* Simple variation of SIR, allowing nodes to be reinfected multiple times.[cite: 26]
* Initially, some nodes are in the I state and all others are in the S state.[cite: 26]
* Each node $v$ that enters the I state remains infectious for a fixed number of steps $t_1$.[cite: 26]
* During each of these $t_1$ steps, $v$ has a probability $p$ of passing the disease to each of its susceptible neighbors.[cite: 26]
* After $t_1$ steps, node $v$ is no longer infectious, and it returns to the S state.[cite: 26]

## SIS Epidemics
* *(Diagram Note: A sequence of network graphs illustrates the SIS model. First, nodes y and z are red (infected). Next, the infection spreads to x and v (red). Unlike SIR, nodes y and z return to a susceptible white state rather than turning gray. Next, the infection jumps to node r, leaving x and v white. Finally, the infection can bounce back up the graph, re-infecting node z, demonstrating the cyclical nature of SIS.)*[cite: 27, 28, 29, 30]

## Test Your Knowledge
* *(Diagram Note: A complex network graph containing 17 numbered nodes interconnected by undirected edges. Nodes 7 and 8 are highlighted with thick black outlines.)*[cite: 31]
* Suppose 7 and 8 get infected $p = 0.25$, the infection last 2 steps.[cite: 31]
* Use a random generator.[cite: 31]
* Using the SIR model simulate for 10 steps.[cite: 31]
* Using the SIS model simulate for 10 steps.[cite: 31]

## Extensions
* Temporary Immunity[cite: 32]
* Quarantine[cite: 32]
* Vaccination[cite: 32]