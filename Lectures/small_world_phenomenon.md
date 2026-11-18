# SMALL WORLD PHENOMENON

**CECS 427 DYNAMIC NETWORKS**
**OSCAR MORALES-PONCE**

## Six Degrees of Separation
* Why can groups be connected by very short paths through a social network?
* "Six degrees of separation" has long been the subject of both anecdotal and scientific fascination.
* Milgram's experiment demonstrated two striking facts about large social networks:
    * there are many short paths, and
    * people, without any "global map" of the network, can be effective at collectively finding these short paths.
* The real global friendship network contains enough clues about how people fit together in larger structures — both geographic and social — to allow search to focus in on distant targets.

## Models for the Existence of Short Paths
* If each of us knows more than 100 other people on a first-name basis...
* This would bring us to more than $100^3 = 1,000,000$ people who in principle could be three steps away.
* *(Diagram Note: A simple tree diagram shows a root node labeled "you", connecting to a second tier of nodes labeled "your friends", which branch out further to a third tier of nodes labeled "friends of your friends".)*

## What is Wrong with this Reasoning?
* Social networks abound in triangles – sets of three people who mutually know each other — and in particular, many of your 100 friends will know each other.
* *(Diagram Note: The tree diagram from the previous slide is updated. In addition to the hierarchical connections, there are now lateral edges (chords) connecting nodes within the "your friends" tier and the "friends of your friends" tier, illustrating the presence of triangles and closed loops rather than pure outward branching.)*

## Watts-Strogatz Model
* Can we make up a simple model that exhibits both many closed triads, but also very short paths?
* Such a model follows naturally from a combination of two basic social-network ideas: homophily and weak ties.
* Homophily creates many triangles.
* Weak ties produce a widely branching structure that reaches many nodes in a few steps.
* Suppose that everyone lives on a two-dimensional grid.
* Create a network by giving each node two kinds of links:
    * those explainable purely by homophily, and
    * those that constitute weak ties.
* *(Diagram Note: An image shows a basic, empty 2-dimensional grid consisting of 24 circular nodes arranged in 4 rows and 6 columns, with no edges connecting them yet.)*

## Watts-Strogatz Model: Homophily
* This is captured by having each node form a link to all other nodes that lie within a radius of up to $r$ grid steps away, for some constant value of $r$.
* *(Diagram Note: The 2D grid of 24 nodes is now fully connected locally. Every node has straight-line edges connecting it to its immediate horizontal, vertical, and diagonal neighbors, forming a dense lattice of triangles.)*

## Watts-Strogatz Model: Weak Ties
* For some constant $k$, each node also forms a link to $k$ other nodes selected uniformly at random from the grid.
* *(Diagram Note: The dense 2D grid is shown. A single node near the bottom center is highlighted in red. Long, curved black arrows extend outward from this red node to distant, randomly selected nodes across the grid, representing the weak ties.)*

## Watts-Strogatz Model: (Continued)
* The network has many triangles: any two neighboring nodes (or nearby nodes) will have many common friends, where their neighborhoods of radius $r$ overlap.
* *(Diagram Note: The 2D grid is shown again. Now, several different nodes have long, curved black arrows projecting out to distant locations across the network, showing that many nodes possess these long-range random weak ties.)*
* There are with high probability very short paths connecting every pair of nodes in the network.
* Start tracing paths outward from a starting node $v$, using only the $k$ random weak ties out of each node.
* Since these edges link to nodes chosen uniformly at random, we are very unlikely to ever see a node twice in the first few steps outward from $v$.
* In these first few steps almost surely there is no triadic closure, and so a huge number of nodes are reached in a small number of steps.
* Thus, introducing a tiny amount of randomness – in the form of long-range weak ties — is enough to make the world "small," with short paths between every pair of nodes.

## Decentralized Search
* Consider the Watts and Strogatz model and suppose that a starting node $s$ is given a message that it must forward to a target node $t$.
* Initially $s$ only knows the location of $t$ on the grid, but, crucially, it does not know the random edges out of any node other than itself.
* Each intermediate node along the path has this partial information as well, and it must choose which of its neighbors to send the message to next.
* Given this set-up, one can prove that decentralized search in the Watts-Strogatz model will necessarily require a large number of steps to reach a target.

## Controlling Scales Spanned by Long-Range Weak Ties
* We have a grid and each node has edges to each other node within $r$ grid steps.
* Each of its $k$ random edges is generated in a way that decays with distance, controlled by a clustering exponent $q$ as follows.
* For two nodes $v$ and $w$, let $d(v,w)$ denote the number of grid steps between them.
* In generating a random edge out of $v$, we have this edge link to $w$ with probability proportional to $d(v,w)^{-q}$.
* We have a different model for each value of $q$. The original grid-based Watts-Strogatz model corresponds to $q=0$, since then the links are chosen uniformly at random.

## Various Clustering Exponents
* When $q$ is very small, the long-range links are "too random," and can't be used effectively for decentralized search.
* *(Diagram Note: The 2D grid is overlaid with long, chaotic, curved arrows that jump wildly across the entire span of the network, illustrating a very small clustering exponent where distance does not strongly constrain the random links.)*
* When $q$ is large, the long-range links are "not random enough" to provide enough of the long-distance jumps that create a small world.
* *(Diagram Note: The 2D grid is overlaid with short, localized curved arrows that only reach nodes very close by, illustrating a large clustering exponent where long-distance weak ties are highly suppressed.)*

## Most Efficient Decentralized Search
* In the limit of large network size, decentralized search is most efficient when $q=2$.
* Organize distances into different "scales of resolution": something can be around the world, across the country, across the state, across town, or down the block.
* A reasonable way to think about these scales of resolution in a network model is to consider the groups of all nodes at increasingly large ranges of distance from $v$: nodes at distance 2 to 4, 4 to 8, 8 to 16, and so forth.
* Consider the group of nodes lying at distances between $d$ and $2d$ from $v$. What is the probability that $v$ forms a link to some node inside this group?

## Concentric Scales of Resolution Around a Given Node
* The total number of nodes in this group is proportional to $d^2$.
* For $u \in A$, $Pr[v \text{ links to } u]$ varies depending on exactly how far out it is, but each individual probability is proportional to $d^{-2}$.
* *(Diagram Note: A visual representation of a central node $v$ surrounded by two concentric circles. The inner circle has a radius denoted as $d$, and the outer circle has a radius denoted as $2d$. Text notes that the "Number of nodes is proportional to $d^2$" and the "Probability of linking to each is proportional to $d^{-2}$".)*

## Generalized Models
* Additional refined models have been investigated.
* Geographic Data on Friendship
* Rank-Based Friendship
* Social Foci and Social Distance
* Search as an Instance of Decentralized Problem-Solving

## Analysis of Decentralized Search in 1 Dimension
* To make the calculations a bit simpler, we place the nodes in one dimension rather than two.
* *(Diagram Note: An image displays a 1-dimensional ring structure, formed by 22 circular nodes connected in a simple continuous loop.)*
* In general, the best exponent for search in a domain is equal to the dimension.
* In our one-dimensional analysis we will be using an exponent of $q=1$ rather than $q=2$.
* $n$ nodes are arranged on a 1-dim ring; each node connected by directed edges to the two others immediately adjacent to it.
* Each node $v$ also has a single directed edge to some other node on the ring; the probability that $v$ links to any particular node $w$ is proportional to $d(v,w)^{-1}$, where $d(v,w)$ is their distance.

## Test Your Knowledge
* Create a ring with 10 nodes ordered and for each node $v$ add a link to node $w$ with probability $d(v,w)^{-1}$.
* *(Diagram Note: An illustration of a 1-dimensional ring with 22 nodes labeled 'a' through 'v'. The interior of the ring is filled with numerous curved, chordal black arrows pointing between various distant nodes, representing the long-range weak ties based on the $1/distance$ probability.)*

## Myopic Search
* Choose a random start node $s$ and a random target node $t$ on the augmented ring.
* The goal is to forward a message from the start to the target, with each intermediate node on the way only knowing the locations of its own neighbors, and the location of $t$, but nothing else about the full network.
* Myopic search can be performed even by nodes that know nothing about the network other than the locations of their friends and the location of $t$.
* We will show that the expected number of hops in from any search is $O(\log^2 n)$.

## Myopic Search (A Forwarding Strategy)
* Forward Strategy: As far as you can from a to m without passing m.
* *(Diagram Note: The full 22-node ring with chordal edges is shown again, serving as the map for the forwarding strategy.)*
* A'S VIEW: *(Diagram Note: An isolated view of node 'a', showing its outgoing edges: short connections to neighbors 'b' and 'v', and a long-range edge jumping directly to node 'e'.)*
* E'S VIEW: *(Diagram Note: An isolated view of node 'e', showing an incoming edge from 'd', a short outgoing edge to 'f', and a long-range edge jumping directly to node 'j'.)*
* J'S VIEW: *(Diagram Note: An isolated view of node 'j', showing short outgoing edges to 'i' and 'k', and a long-range edge jumping directly to node 'r'.)*
* K'S VIEW: *(Diagram Note: An isolated view of node 'k', showing an incoming edge from 'j', a short outgoing edge to 'l', and a long-range edge jumping directly to node 'v'.)*
* L'S VIEW: *(Diagram Note: An isolated view of node 'l', showing an incoming edge from 'k', a short outgoing edge to 'm', and a long-range edge jumping directly to node 't'.)*

## Test Your Knowledge
* From the ring you have created find the path from 1 to 8 using the myopic search.

## Myopic Search (A Forwarding Strategy) - Continued
* From a to m.
* *(Diagram Note: The 22-node ring with chords is shown. A path is highlighted with thick red arrows tracing the myopic search from node 'a' to node 'm'. The path is: $a \rightarrow e \rightarrow j \rightarrow k \rightarrow l \rightarrow m$.)*
* In phase $j$ of the search the distance to m is between a factor $2^{-j}$ and $2^{-(j+1)}$ of the original distance.
* *(Diagram Note: A simplified view of the ring, showing only the perimeter and the specific path taken ($a \rightarrow e \rightarrow j \rightarrow k \rightarrow l \rightarrow m$), highlighting how the distance to the target 'm' progressively shrinks with each step.)*

## Phases
* Every phase it reduces the distance by half.
* Therefore, the number of different phases is at most $\log n$.

## Expected Number of Steps
* Let $X_i$ be the random variable counting the number of steps in phase $j$.
* $$X = X_1 + X_2 + \dots + X_{\log n}$$
* The expected number of steps is:
* $$E[X] = E[X_1 + X_2 + \dots + X_{\log n}] = E[X_1] + E[X_2] + \dots + E[X_{\log n}]$$
* It is enough to show that:
* $$E[X_j] \in O(\log n), \forall j \le \log n$$

## Constant of Proportionality
* Node $v$ forms its long-range link to $w$ with probability proportional to $d(v,w)^{-1}$.
* What is the constant of proportionality?
* The fraction $1/Z$ gives the constant of proportionality, where:
* $$Z = \sum_{w \ne v} d(v,w)^{-1}$$
* There are two nodes at distance 1 from $v$, two at distance 2, and more generally two at each distance $d$ up to $n/2$. If $n$ is even, there is also a single node at distance $n/2$ from $v$. So:
* $$Z \le 2(1 + \frac{1}{2} + \frac{1}{3} + \dots + \frac{1}{n/2}) \approx 2 \ln(n/2) \le 2 \log n$$
* It follows that $d(v,w)^{-1}/Z \ge d(v,w)^{-1}/(2 \log n)$.

## Time Spent in One Phase of Myopic Search
* Choose a particular phase $j$ of the search, when the message is at a node $v$ whose distance to the target $t$ is some number $d$ between $2^j$ and $2^{j+1}$.
* The phase will come to an end once the distance to the target decreases below $2^j$, and we want to show that this will happen relatively quickly.
* One way for the phase to come to an end immediately would be for $v$'s long-range contact $w$ to be at distance $\le d/2$ from $t$.
* In this case, $v$ would necessarily be the last node to belong to phase $j$.
* We show that this immediate halving of the distance in fact happens with reasonably large probability.
* What is the probability of each node in an Interval $I$ to be the long-range contact of $v$?
* $v$ can be at the center of the interval or in an end point.
* *(Diagram Note: A simple linear diagram shows a point $v$. A distance $d$ away is a bracketed interval of length $d/2$. The text indicates that the maximum distance from $v$ to any node in this interval $I$ is $3d/2$.)*
* Therefore, the max distance from $v$ to any node in $I$ is at most $3d/2$ from $v$.
* Each node $w$ in $I$ has probability of being the long-range contact of $v$ of at least:
* $$\frac{d(v,w)^{-1}}{2\log n} > \frac{1}{2\log n}\frac{1}{3d/2} = \frac{1}{3d\log n}$$
* Since there are more than $d$ nodes in $I$, the probability that one of them is the long-range contact of $v$ is at least:
* $$\frac{d}{3d \log n} = \frac{1}{3 \log n}$$
* If one of these nodes is the long-range contact of $v$, then phase $j$ ends immediately in this step.
* Therefore, in each step that it proceeds, phase $j$ has a probability of at least $1/(3 \log n)$ of coming to an end, independently of what has happened so far.
* To run for at least $i$ steps, phase $j$ has to fail to come to an end $i-1$ times in a row, and so the probability that phase $j$ runs for at least $i$ steps is at most:
* $$(1 - \frac{1}{3 \log n})^{i-1}$$
* In each step phase $j$ has a probability of at least $1/(3 \log n)$ of coming to an end.
* It follows that:
* $$E[X_j] = \sum_i Pr[X_j \ge i]$$
* $$\le \sum_i (1 - \frac{1}{3 \log n})^{i-1}$$
* $$\le \frac{1}{1 - (1 - \frac{1}{3 \log n})}$$
* $$= 3 \log n$$
* Geometric Series reference formulas:
* $$\sum_{k=0}^{n} ar^k = a\left(\frac{1 - r^{n+1}}{1 - r}\right)$$
* $$\sum_{k=0}^{\infty} ar^k = \frac{a}{1 - r}$$

## Cow Path Problem
* *(Diagram Note: A photograph of a brown and white cow standing in a grassy field behind a white wooden fence.)*
* Suppose a cow wants to access to a tasty grass field but it does not where the entry is.
* What should it do?
* Move $a_1$ to one direction, then $a_2$ to the next direction, then $a_3$ the the other direction, etc. Suppose that $d > a_n$.
* $$Total \text{ time} = \sum_{i}^{n+1} 2 a_i + d$$

## Suppose a Geometric Increasing
* $$Total \text{ time} = \sum_{i}^{n+1} 2 a_i + d$$
* Let us assume that $a_i$ is geometric and $d$ is at distance $a_n$.
* Total time = $2\sum_i^{n+1} a_i + a_n$.
* Since it is a geometric series, we have that:
* $$a^n + 2\left(\frac{a^{n+2}-1}{a-1}\right)$$

## How to Measure its Efficiency
* Consider the Competitive Ratio metric, i.e., how bad is the solution compared with the solution that has full knowledge.
* $$CR = \frac{a^n + 2\left(\frac{a^{n+2}-1}{a-1}\right)}{a^n} = 1 + \frac{2\left(\frac{a^{n+2}-1}{a-1}\right)}{a^n} \le 1 + 2\left(\frac{a^2}{a-1}\right)$$
* We have to find $a$ that minimizes $CR$.
* $$CR = \min_a 1 + 2\left(\frac{a^2}{a-1}\right)$$

## Minimizing CR
* $$f(a) = 1 + 2\left(\frac{a^2}{a-1}\right)$$
* To find the minimum, first we derive with respect to $a$ and then solve it to 0, i.e., $f'(a) = 0$.
* $$f'(a) = \left(\frac{4a}{a-1}\right) - \left(\frac{2a^2}{(a-1)^2}\right)$$
* Therefore, $\left(\frac{4a}{a-1}\right) = \left(\frac{2a^2}{(a-1)^2}\right)$
* $$2a - 2 = a$$
* $$a = 2$$
* Therefore, $CR = 1 + 2(4) = 9$.

## Lower Bound
* Is there another algorithm with competitive ratio less than 9?
* How to show that it is not possible design a more efficient algorithm?
* The strategy is to use a planar cone diagram.
* *(Diagram Note: A simple coordinate system with a horizontal line representing "Position" and a vertical line representing "Time".)*
* Show that there exists a time where the cone contains all the turning points of the cow.
* Consider the minimum slop.
* The adversary can place the entry at epsilon distance from a turning point.
* The cow will move to the other point before visiting the entry.
* This gives a $CR$ that we minimize as before.
* *(Diagram Note: A V-shaped planar cone is drawn on the Position/Time graph. A point on the right boundary of the cone is labeled with time 't'. Below the horizontal axis, the equation $|position| = t/\beta$ is shown. Text states "There is a time when the cow is at cone boundary".)*
* $$CR = 1 + \frac{(\beta+1)^2}{\beta-1}$$
* Minimum is 9 achieved at $\beta = 3$.