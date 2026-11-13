# CASCADING BEHAVIOR IN NETWORKS
**CECS 427 DYNAMIC NETWORKS**[cite: 33]
**OSCAR MORALES PONCE**[cite: 33]

## Objectives
* Understand how behaviors spread through networks[cite: 34]
* Explore coordination games and thresholds[cite: 34]
* Analyze clusters and barriers to diffusion[cite: 34]
* Discuss cascade capacity and its limits[cite: 34]

## Diffusion
* An individual's choices depend on what other people do.[cite: 35]
* Two conceptually different levels of resolution for analyzing diffusion:[cite: 35]
    1. View the network as an amorphous population of individuals, and look at effects in aggregate;[cite: 35]
    2. Look at how individuals are influenced by their particular network neighbors by moving closer to the fine structure of the network as a graph.[cite: 35]
* We focus to the network level.[cite: 35]
* Understanding local/global interactions;[cite: 35]
* Considering individual choices with explicit network structure.[cite: 35]

## Diffusion of Innovations
* How do new behaviors, practices, opinions, conventions, and technologies spread from person to person through a social network, as people influence their friends to adopt new ideas?[cite: 36]
* Is it direct-benefit effects?[cite: 36]
* Is it informational effects?[cite: 36]
* Success of innovations depends on: Complexity, Observability (becoming aware), Trialability (adapting gradually and incrementally), Compatibility.[cite: 36]

## Modeling Diffusion Through a Network
* Underlying model of individual decision-making: as individuals make decisions based on the choices of their neighbors, a particular pattern of behavior can begin to spread across the links of the network.[cite: 37]
* As a guide we can employ informational effects or direct-benefit effects.[cite: 37]
* We focus on direct-benefit effects.[cite: 37]

## A Networked Coordination Game
* Assume two possible behaviors, labeled A and B.[cite: 38]
* Each node has a choice between A and B.[cite: 38]
* If nodes $v$ and $w$ are linked by an edge, then there is an incentive for them to have their behaviors match.[cite: 38]
* Represent this using a game in which $v$ and $w$ are the players and A and B are the possible strategies.[cite: 38]
    * if $v$ and $w$ both adopt A, they each get payoff $a > 0$;[cite: 38]
    * if $v$ and $w$ both adopt B, they each get a payoff of $b > 0$;[cite: 38]
    * if they adopt opposite behaviors, they each get a payoff of 0.[cite: 38]

## Coordinating Neighbors
* Each node $v$ is playing a copy of this game with each of its neighbors, and its payoff is the sum of its payoffs in the games played on each edge.[cite: 39]
* *(Diagram Note: Node $v$ is centrally located, connected via edges to 3 nodes using behavior A (representing $pd$ neighbors) and 3 nodes using behavior B (representing $(1-p)d$ neighbors). Dashed lines visually divide the two groups.)*[cite: 39]
* Hence $v$'s choice of strategy will be based on the choices made by all of its neighbors, taken together.[cite: 39]

## Decision Rule for Node v
* Suppose that $p$ fraction of $v$'s neighbors have behavior A, and $1-p$ fraction have behavior B;[cite: 40]
* if $v$ has $d$ neighbors, then $pd$ adopt A and $(1-p)d$ adopt B.[cite: 40]
* So if $v$ chooses A, it gets a payoff of $pda$, and if it chooses B, it gets a payoff of $(1-p)db$.[cite: 40]
* Threshold Formula: A is the better choice if $pda \ge (1-p)db$: $p \ge q := b / (a+b)$ after rearranging terms.[cite: 40]
* Break ties in favor of A.[cite: 40]

## Cascading
* In any network, there are two obvious equilibria to this network-wide coordination game: one in which everyone adopts A, and another in which everyone adopts B.[cite: 41]
* Guided by diffusion questions, we want to understand how easy it is, in a given situation, to "tip" the network from one of these equilibria to the other.[cite: 41]
* What other "intermediate" equilibria look like: states of coexistence where A is adopted in some parts of the network and B is adopted in others.[cite: 41]

## Switching from B to A
* Consider the coordination game with $a=3$, $b=2$.[cite: 42]
* Using the threshold formula, nodes will switch from B to A if at least a $q = 2 / (3+2) = 2/5$ fraction of their neighbors are using A.[cite: 42]
* *(Diagram Note: A network graph containing 6 nodes (r, s, t, u, v, w) showing the progression of nodes adopting behavior A. Initially, only nodes v and w are highlighted red (adopting A).*[cite: 43] *After one step, nodes r and t adopt behavior A (now red) because the $2/5$ threshold requirement is met.*[cite: 44, 45] *After a second step, nodes s and u finally cross the threshold and turn red, meaning everyone has adopted behavior A.)*[cite: 46]

## Cascading: Larger
* Suppose that in the A-B coordination game, we have $a=3$ and $b=2$, leading to a threshold of $q = 2/5$.[cite: 47]
* *(Diagram Note: The 17-node network from earlier is shown again. First as a blank network, and then with nodes 7 and 8 highlighted to represent the start of the cascade from initial adopters.)*[cite: 47, 48]

## Cascading Behavior and "Viral Marketing"
* Previous example illustrates an important point: tightly-knit communities in the network can work to hinder the spread of an innovation.[cite: 49]

## Adopting and Switching: Thresholds
* Consider a set of initial adopters who start with a new behavior A, every other node starts with behavior B.[cite: 50]
* Nodes then repeatedly evaluate the decision to switch from B to A using a threshold of $q$.[cite: 50]
* If the resulting cascade of adoptions of A eventually causes every node to switch from B to A, then we say that the set of initial adopters causes a complete cascade at threshold $q$.[cite: 50]

## Cascades and Clusters
* The spread of a new behavior can stall when it tries to break in to a tightly-knit community within the network.[cite: 51]
* This will in fact provide a way of formalizing a qualitative principle: homophily can often serve as a barrier to diffusion, by making it hard for innovations to arrive from outside densely connected communities.[cite: 51]
* A key property of such communities is that when you belong to a community, many of your friends also tend to belong too.[cite: 51]

## Example: Clusters
* A cluster of density $p$ is a set of nodes such that each node in the set has at least a $p$ fraction of its network neighbors in the set.[cite: 52]
* *(Diagram Note: A graph consisting of 12 nodes (a through l) grouped into three distinct diamond-shaped blocks of 4. Nodes a,b,c,d form a cluster of density 2/3. Nodes e,f,g,h and i,j,k,l each form clusters of density 2/3 as well.)*[cite: 52]
* *(Diagram Note: The 17-node network is shown again, this time with dashed loops outlining two specific clusters of density 2/3: one encompassing nodes 1, 2, 3 and the other encompassing nodes 11 through 17.)*[cite: 53, 54]

## Relationship Between Clusters and Cascades
* A cascade comes to a stop when it runs into a dense cluster; and furthermore, that this is the only thing that causes cascades to stop.[cite: 54]
* Theorem. Consider a set of initial adopters of behavior A, with a threshold of $q$ for nodes in the remaining network to adopt behavior A. If the remaining network contains a cluster of density greater than $1-q$, then the set of initial adopters will not cause a complete cascade.[cite: 54]
* Moreover, whenever a set of initial adopters does not cause a complete cascade with threshold $q$, the remaining network must contain a cluster of density greater than $1-q$.[cite: 54]

## Proof of Part 1
* Consider an arbitrary network in which behavior A is spreading with threshold $q$, starting from a set of initial adopters.[cite: 55]
* *(Diagram Note: Diagram shows initial adopters with bold outlines attempting to spread the behavior into a large circular area labeled "cluster". Node $v$ sits inside the cluster boundary.)*[cite: 55]
* Suppose that the remaining network contains a cluster of density greater than $1-q$. We argue that no node inside the cluster will ever adopt A.[cite: 55]
* Assume the opposite, i.e., that some node inside the cluster does eventually adopt A, and consider the earliest time step $t$ at which some node inside the cluster does so.[cite: 56, 57]
* Let $v$ be the name of a node in the cluster that adopts A at time $t$.[cite: 56, 57]
* At the time that $v$ adopted A, its decision was based on the set of nodes who had adopted A by the end of the previous time step, $t-1$.[cite: 56, 57]
* Since no node in the cluster adopted before $v$ did, the only neighbors of $v$ that were using A at the time it decided to switch were outside the cluster.[cite: 56, 57]
* But since the cluster has density greater than $1-q$, more than a $1-q$ fraction of $v$'s neighbors are inside the cluster, and hence less than a $q$ fraction of $v$'s neighbors are outside the cluster.[cite: 58]
* Since these are the only neighbors who could have been using A, and since the threshold rule requires at least a $q$ fraction of neighbors using $v$, this is a contradiction.[cite: 58]
* Hence our original assumption, that some node in the cluster adopted A at some point in time, must be false.[cite: 58]

## Proof of Part 2
* We show that whenever a set of initial adopters fails to cause a complete cascade with threshold $q$, there is a cluster in the remaining network of density greater than $1-q$.[cite: 59]
* *(Diagram Note: Diagram illustrates nested sets: a small inner set of "initial adopters", surrounded by a larger set of "nodes that eventually switch to A", and then an outermost boundary containing node $w$ representing "nodes that don't eventually switch to A".)*[cite: 59]
* This is not difficult: consider running the process by which A spreads, starting from the initial adopters, until it stops.[cite: 59]
* It stops because there are still nodes using B, but none of the nodes in this set want to switch.[cite: 60]
* Let $S$ denote the set of nodes using B at the end of the process. We claim that $S$ is a cluster of density $> 1-q$, which will finish the proof.[cite: 60]
* Consider any node $w$ in this set $S$. Since $w$ doesn't want to switch to A, it must be that the fraction of its neighbors using A is less than $q$ - and hence that the fraction of its neighbors using B is greater than $1-q$.[cite: 60]
* But the only nodes using B in the whole network belong to the set $S$, so the fraction of $w$'s neighbors belonging to $S$ is greater than $1-q$.[cite: 60]
* Since this holds for all nodes in $S$, it follows that $S$ is a cluster of density greater than $1-q$.[cite: 60]

## From Awareness to Adoption & Role of Weak Ties
* There is a crucial difference between learning about a new idea and actually deciding to adopt it.[cite: 61]
* The strength of weak ties is rooted in the idea that weak social connections, to people we see infrequently, often form local bridges in a social network.[cite: 61]
* Therefore, they provide access to sources of information - things like new job opportunities - that reside in parts of the network we otherwise wouldn't have access to.[cite: 61]
* *(Diagram Note: Network graph featuring three distinct dense clusters connected sparsely by central node $w$, which acts as a bridge. Nodes $u$ and $v$ connect to $w$ from their respective clusters).*[cite: 62]
* The edges $u-w$ and $v-w$ span tightly-knit communities that wouldn't otherwise be able to communicate.[cite: 62]
* We expect $v$, for example, to receive information from his edge to $w$ that he wouldn't get from his other edges.[cite: 62]
* Important aspect of bridges/local bridges in a social network: they convey awareness of new things, but they are weak at transmitting behaviors that are in some way risky or costly to adopt - behaviors where you need to see a higher threshold of neighbors doing it before you do it as well.[cite: 63]
* Nodes $u$ and $v$ have strong advantages over other members of their respective tightly-knit communities: they can learn from node $w$ about a new behavior currently spreading in $w$'s community, but for behaviors with higher thresholds they will still want to align themselves with others in their own community.[cite: 63]

## Extensions of Cascade Model: Heterogeneous Thresholds
* For each node $v$, define a payoff $a_v$ that it receives when it coordinates with someone on behavior A, and a payoff $b_v$ that it receives when it coordinates with someone on behavior B.[cite: 64]
* When two nodes $v$ and $w$ interact across an edge in the network, they are thus playing a coordination game.[cite: 64]
* If $v$ has $d$ neighbors, of whom a $p$ fraction have behavior A and a $1-p$ fraction have behavior B, then the payoff from choosing A is $pda_v$, while the payoff from choosing B is $(1-p)db_v$.[cite: 64]
* Thus, A is the better choice if $p \ge q_v := b_v / (a_v + b_v)$.[cite: 64]

## Knowledge, Thresholds, and Collective Action
* We consider situations where coordination across a large segment of the population is important, and the underlying social network is serving to transmit information about people's willingness to participate.[cite: 65]
* Assume you are living in such a society, and you are aware of a public demonstration against the government planned for tomorrow.[cite: 65]
* If an enormous number of people show up, then the government will be seriously weakened, and everyone in society - including the demonstrators - will benefit.[cite: 66]
* But if only a few hundred show up, then the demonstrators will simply all be arrested (or worse), and it would have been better had everyone stayed home.[cite: 66]
* This is a collective action problem, where an activity produces benefits only if enough people participate.[cite: 67]
* Pluralistic ignorance is the phenomenon in which people have wildly erroneous estimates about the prevalence of certain opinions in the population at large.[cite: 67]
* It is possible that a large fraction of the population is strong enough in its opposition to be willing to take extreme measures, but that most of these people believe they're in a small minority - and hence view opposition as too risky.[cite: 67]

## A Model
* Each person in a social network knows about a potential upcoming protest against the government, and she has a personal threshold which encodes her willingness to participate.[cite: 68]
* Threshold $k$ means: "I will show up for the protest if I am sure that at least $k$ people in total (including myself) will show up."[cite: 68]
* The links in the social network encode strong ties, where the two endpoints of link trust each other.[cite: 68]
* Thus, we assume that each person in the network knows the thresholds of all her neighbors in the network but does not know the thresholds of anyone else.[cite: 68]
* Given a network with a set of thresholds, how should we reason about what is likely to happen?[cite: 68]

## Can an Uprising Occur?
* Each node has a threshold (integer) for participation in a protest, but only knows the threshold of itself and its neighbors.[cite: 69]
* I will join the protest if there is reasonable support from others![cite: 69]
* Depending on the configuration, nodes may have to reason what other nodes know in order to decide what they will do.[cite: 69]
* A broad range of social institutions can help build common knowledge and facilitate reasoning![cite: 69]
* *(Diagram Note: Three small network diagrams demonstrate failure scenarios. In the left picture, nodes u, v, and w have thresholds 2, 3, and 4 respectively. Since there are only 3 nodes, node w (threshold 4) will never join. Node v knows w's threshold and knows w won't join, so v (threshold 3) won't join. Node u (threshold 2) infers the others won't join and stays home too, resulting in no uprising.)*[cite: 70]

## Cascade Capacity
* Given a network, what is the maximum threshold at which any "small" set of initial adopters can cause a complete cascade?[cite: 71]
* This maximum threshold is an inherent property of the network, indicating the outer limit on its ability to support cascades.[cite: 71]
* The cascade capacity is the maximum threshold at which a finite set of nodes can cause a complete cascade.[cite: 71]
* The simplest way to define "small" is to make it equivalent to "finite" in an infinite network all of whose nodes have finite degree.[cite: 71]

## Cascades on Infinite Networks
* A finite set $S$ of nodes has behavior A (this is the small set of early adopters), and all other nodes adopt B.[cite: 72]
* Time runs forward in steps $t=1,2,3,...$[cite: 72]
* In each step $t$, each node other than those in $S$ uses the decision rule with threshold $q$ to decide whether to adopt behavior A or B.[cite: 72]
* Set $S$ causes a complete cascade if, starting from $S$ as the early adopters of A, every node in the network eventually switches permanently to A.[cite: 72]
* The cascade capacity of the network is the largest value of the threshold $q$ for which some finite set of early adopters can cause a complete cascade.[cite: 72]
* Infinite Path: With two early adopters of behavior A (black) and that all other nodes start out adopting B. *(Diagram Note: An infinite straight line of nodes stretching outwards).*[cite: 73] If $q \le 1/2$, for each node, there will come some time at which it chooses to switch permanently to A.[cite: 73] If $q > 1/2$, no finite set of initial adopters can get any node to their right to switch to A, and so A clearly cannot spread to all nodes.[cite: 73]

## Infinite Grid Network
* *(Diagram Note: A grid network containing nodes labeled a through p, with a central 3x3 block of nodes colored black to represent the early adopters of A).*[cite: 74]
* $3/8$ is the cascade capacity of the infinite grid.[cite: 75]
* Given any finite set of initial adopters, they are contained in some rectangle of the grid, and if $q > 3/8$, no node outside this rectangle will ever choose to adopt A.[cite: 75]

## How Large Can the Cascade Capacity Be?
* Theorem. There is no network in which the cascade capacity exceeds $1/2$.[cite: 75]
* This has a subtle but natural interpretation: Regardless of the structure of the underlying network, if a new behavior requires 51% of someone's friends to adopt it before they do, then it can't spread very far through the population.[cite: 75]
* We need to show that if $q > 1/2$ then regardless of what the underlying network looks like, a new behavior starting at a finite set of nodes will not spread to every other node.[cite: 75]

## Looking at the Interface
* Suppose behavior A spreads from a finite initial set $S$ with threshold $q > 1/2$.[cite: 76]
* As time moves forward in steps $t=1,2,3,...$ potentially larger and larger sets become adopters of A.[cite: 76]
* At any given point in time, each edge in the network can be described as an A-A edge (connecting two adopters of A), a B-B edge (connecting two adopters of B), or an A-B edge (connecting an adopter of A to an adopter of B).[cite: 76]
* We define the interface to be the set of A-B edges.[cite: 76]
* We're going to show that, in each step, the size of the interface - i.e., the number of edges it contains - must strictly decrease.[cite: 76]
* *(Diagram Note: A network is divided by a dark thick oval ring representing the interface. Nodes inside the oval have adopted A, nodes outside are using B).*[cite: 77]
* One step of the process: $v$ and $w$ adopt A: after they adopt, the size of the interface has strictly decreased.[cite: 78]
* The size of the interface clearly starts at some number $I_0$; since there is some finite set of initial adopters $S$, and since each of these has a finite set of neighbors, the set of A-B edges is finite, and has some size $I_0$.[cite: 79]
* The size of the interface is always a non-negative whole number, so if it strictly decreases in each step, the spread of A can run for at most $I_0$ steps before terminating.[cite: 79]
* Since each step only results in a finite number of nodes converting to A, the process will terminate with only a finite set of nodes having adopted A.[cite: 79]
* *(Diagram Note: The interface oval expands to absorb nodes $v$ and $w$ into the adopted group. Lines connecting $v$ and $w$ to the rest of the outside network represent the new A-B edges).*[cite: 80]
* When a node $w$ switches from B to A, its edges to nodes that remain with B change from being B-B edges to being A-B edges - so this causes them to join the interface.[cite: 80]
* Edges from $w$ to nodes that were already with A change from being A-B edges to being A-A edges; in other words, they leave the interface.[cite: 81]
* Each edge that joins or leaves the interface in this step can be accounted for in this way by exactly one node that switches from B to A.[cite: 81]
* Consider a node $w$ that switches; suppose that before the switch, it had $a$ edges to nodes that were already adopters of A, and $b$ edges to nodes that will remain adopters of B at the end of the step. So node $w$ accounts for $b$ edges joining the interface and $a$ edges leaving it.[cite: 81]
* Since $q > 1/2$, and node $w$ decided to switch to A in this step, it must be that $w$ had more edges to adopters of A than to adopters of B - so $a > b$, and hence $w$ accounts for more edges leaving the interface than edges joining the interface.[cite: 81]
* But this is true for each node that switches in this step, and so the overall size of the interface goes down.[cite: 81]

## Fake News
* Oleg Yasinsky main responsable (RT, Telesur): Russian-led digital disinformation campaign.[cite: 82]
* Mentions: Social Design Agency (SDA), Structura National Technologies, Institute for Internet Development (IID).[cite: 82]
* Individuals/Outlets listed: Carlos Déniz, Jesús López Almejo, Pressenza, El Ciudadano, Resumen Latinoamericano, Desinformemonos, Telesur, Estrategia, Barão de Itararé, Peoples Dispatch, Clacpi, Dialogos Do Sul, Liberation, En la Pirqa, Colombia Informa, La Pluma, Veritas Press, Sociología Crítica, Globatium, Malaga al Día y Luis Emilio Recabarren.[cite: 82]