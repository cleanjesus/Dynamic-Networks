# Strong and Weak Ties

Source: `Strong and Weak Ties(2).pdf`

This deck explains triadic closure, clustering coefficient, local bridges, the strength of weak ties, neighborhood overlap, graph partitioning, and betweenness. Each slide image is retained because the evolving graph states and highlighted nodes/edges are part of the explanation.

> Preservation note: Every slide is represented by searchable extracted text **and** an embedded raster of the original slide. The image is authoritative for graph geometry, colors, labels, edge direction/placement, and staged highlights. Graph notes below explain the intended operation without replacing the original visual.

## Slide-by-slide content

### Slide 1

![Original slide 1](assets/strong-weak/page-01.jpg)

**Extracted slide text:**

```text
STRONG AND WEAK
TIES
CECS 427 DYNAMIC NETWORKS
```

### Slide 2

![Original slide 2](assets/strong-weak/page-02.jpg)

**Extracted slide text:**

```text
STRONG AND WEAK TIES

• Offering explanations for how simple process at local level has a global impact
• How people that recently changed employers learn how they discovered their new jobs
• 1960 Mark Granovette interviewed people to understand the problem
```

### Slide 3

![Original slide 3](assets/strong-weak/page-03.jpg)

**Graph / visual semantics:** Graph meaning: the initial social network has people as nodes and acquaintance/friendship links as edges. Candidate edges are evaluated through common neighbors.

**Extracted slide text:**

```text
TRIADIC CLOSURE

• Consider different snapshot over time        G

• How the network evolves over time
    • Path, Components, Distance, etc.
                                               B
• Consider the following social network
    • nodes are people, a link exists if
    they know each other                   F       A       C

• What edges do form or disappear?

                                               E       D
```

### Slide 4

![Original slide 4](assets/strong-weak/page-04.jpg)

**Extracted slide text:**

```text
TRIADIC CLOSURE

• If 2 people have a friend in common, then there is an increased likelihood that they
  become friends themselves at some point in the future
```

### Slide 5

![Original slide 5](assets/strong-weak/page-05.jpg)

**Graph / visual semantics:** Graph meaning: the highlighted candidate edge CB has a common neighbor A, so adding CB would close triangle ABC.

**Extracted slide text:**

```text
TRIADIC CLOSURE

• What edges do form or disappear?       G

                                         B

                                     F       A       C

                                         E       D
```

### Slide 6

![Original slide 6](assets/strong-weak/page-06.jpg)

**Extracted slide text:**

```text
TRIADIC CLOSURE

• What edges do form or disappear?        G

• Edge CB has a higher chance to appear
    overtime                              B
• ABC will form a triangle

                                     F        A       C

                                          E       D
```

### Slide 7

![Original slide 7](assets/strong-weak/page-07.jpg)

**Graph / visual semantics:** Graph meaning: both CB and ED are plausible future edges because each pair has a common neighbor; the graph can evolve by adding such edges.

**Extracted slide text:**

```text
TRIADIC CLOSURE

• What edges do form or disappear?           G

• Edge CB has a higher chance to appear
    Overtime. ABC will form a triangle       B
• Edge ED has also higher chance to appear
    overtime
                                         F       A       C
• List some of the possible new edges
    that may appear overtime

                                             E       D
```

### Slide 8

![Original slide 8](assets/strong-weak/page-08.jpg)

**Graph / visual semantics:** Graph meaning: a long-range edge such as GD can arise through intermediate paths or changing relationships even when the endpoints are not initially close.

**Extracted slide text:**

```text
TRIADIC CLOSURE

• Sometimes edges far apart may appear         G

• Can you explain the reason that GD appear?

                                               B

                                     F             A       C

                                               E       D
```

### Slide 9

![Original slide 9](assets/strong-weak/page-09.jpg)

**Graph / visual semantics:** Clustering coefficient: for node A, it is the probability that two randomly selected neighbors of A are adjacent; it measures how clique-like A’s neighborhood is.

**Extracted slide text:**

```text
CLUSTERING COEFFICIENT

• The clustering coefficient represents the likelihood that two friends of a node are also
  friends with each other.
    • How "clique-like" is the neighborhood around a node?
    • Are my friends also friends with each other?

• The clustering coefficient of node A is the probability that two randomly selected friends
  of A are friends with each other
• In other words, it is the fraction of pairs of A’s friends that are connected to each other
  by edges.
```

### Slide 10

![Original slide 10](assets/strong-weak/page-10.jpg)

**Extracted slide text:**

```text
CLUSTERING COEFFICIENT

• How many possible edges can be formed with the friends of A

                                              A
```

### Slide 11

![Original slide 11](assets/strong-weak/page-11.jpg)

**Extracted slide text:**

```text
CLUSTERING COEFFICIENT

• How many possible edges can be formed with the friends of A
• Consider only the friends of A
```

### Slide 12

![Original slide 12](assets/strong-weak/page-12.jpg)

**Extracted slide text:**

```text
CLUSTERING COEFFICIENT

• How many possible edges can be formed with the friends of A
• Consider only the n friends of A
• Each node can be paired with n -1
```

### Slide 13

![Original slide 13](assets/strong-weak/page-13.jpg)

**Extracted slide text:**

```text
CLUSTERING COEFFICIENT

• How many possible edges can be formed with the friends of A
• Consider only the n friends of A
• Each node can be paired with n -1
• We have n nodes, therefore
    • n(n-1) pairs
```

### Slide 14

![Original slide 14](assets/strong-weak/page-14.jpg)

**Graph / visual semantics:** Formula meaning: if A has n neighbors, there are n(n-1)/2 possible edges among those neighbors. CC(A)=actual edges among A’s neighbors divided by n(n-1)/2.

**Extracted slide text:**

```text
CLUSTERING COEFFICIENT

• How many possible edges can be formed with the friends of A
• Consider only the n friends of A
• Each node can be paired with n -1
• We have n nodes, therefore
    • n(n-1) pairs

• However, each edge is counted
    twice
• Therefore, n(n-1)/2
```

### Slide 15

![Original slide 15](assets/strong-weak/page-15.jpg)

**Extracted slide text:**

```text
CLUSTERING COEFFICIENT

• The clustering coefficient is then the number of actual edges of A’s friends divided by
  n(n-1)/2
• In the example we have 5 friends
• Therefore, CC = 3/10
```

### Slide 16

![Original slide 16](assets/strong-weak/page-16.jpg)

**Extracted slide text:**

```text
CLUSTERING COEFFICIENT

• Observe that
    • if A’s friend’s do no have any edge, then the probability is 0
    • if A’s friend’s have an edge to each other, then the probability is 1
```

### Slide 17

![Original slide 17](assets/strong-weak/page-17.jpg)

**Graph / visual semantics:** Local bridge meaning: removing BA increases the distance between its endpoints from 2 to more than 2 (shown as 4). BA is a local bridge even though removing it does not disconnect the graph.

**Extracted slide text:**

```text
LOCAL BRIDGE

• The distance from GA is two       G

                                    B

                                F       A       C

                                    E       D
```

### Slide 18

![Original slide 18](assets/strong-weak/page-18.jpg)

**Extracted slide text:**

```text
LOCAL BRIDGE

• The distance from GA is two             G

• By removing BA the distance increases
to 4                                      B

• BA is a local bridge
• An edge is a local bridge if the   F        A       C
removal of the edge increases > 2

                                          E       D
```

### Slide 19

![Original slide 19](assets/strong-weak/page-19.jpg)

**Graph / visual semantics:** Bridge meaning: removing the edge disconnects the graph. A bridge is a special local bridge whose endpoint distance becomes infinity after removal.

**Extracted slide text:**

```text
LOCAL BRIDGE AND BRIDGE

• A bridge is an edge that the removal         G

splits the graph
• A bridge is a special case of local bridge       B

where the distance increase to infinity

                                          F            E       C

                                                           D
```

### Slide 20

![Original slide 20](assets/strong-weak/page-20.jpg)

**Graph / visual semantics:** Tie-strength legend: weak ties represent acquaintances; strong ties represent close friends.

**Extracted slide text:**

```text
WEAK AND STRONG TIES

• We can assign two attributes to the links
    • Weak: An acquaintance
    • Strong: A close friend

      B              C           B            C        B           C

    Weak           Weak        Strong         Weak   Strong       Strong

             A                          A                     A
```

### Slide 21

![Original slide 21](assets/strong-weak/page-21.jpg)

**Graph / visual semantics:** Triadic closure property: if A has strong ties to both B and C, then B and C must have some tie, weak or strong.

**Extracted slide text:**

```text
TRIADIC CLOSURE PROPERTY

 • Triadic closure property: If A has two strong ties with B and C, then there is a tie
   between B and C (weak or strong)

                                                                  Strong/
                                                                  Weak
     B            C            B            C               B                C

  Weak           Weak        Strong        Weak          Strong             Strong

           A                          A                              A
```

### Slide 22

![Original slide 22](assets/strong-weak/page-22.jpg)

**Extracted slide text:**

```text
STRONG TRIADIC CLOSURE

                    W
            S            S

                S       W

                             S
```

### Slide 23

![Original slide 23](assets/strong-weak/page-23.jpg)

**Graph / visual semantics:** Power of weak ties: if every node satisfies triadic closure and every node has at least one strong tie, then every local bridge must be weak.

**Extracted slide text:**

```text
POWER OF WEAK TIES

• If all nodes of G satisfies the triadic closure property and each node has a strong tie,
  then all local bridges are weak.

                                                Weak
                                            A          B
                               Strong
                                        C
```

### Slide 24

![Original slide 24](assets/strong-weak/page-24.jpg)

**Extracted slide text:**

```text
POWER OF WEAK TIES

• Suppose by contradiction that AB is strong tie

                                               Strong
                                           A            B
                              Strong
                                       C
```

### Slide 25

![Original slide 25](assets/strong-weak/page-25.jpg)

**Graph / visual semantics:** Contradiction argument: assuming a local bridge AB is strong, A’s other strong tie to C forces BC by triadic closure, contradicting AB being a local bridge.

**Extracted slide text:**

```text
POWER OF WEAK TIES

• Suppose by contradiction that AB is strong tie
• Then CB must exist by triadic closure and AB is not a weak Tie. A contradiction!

                                               Strong
                                           A            B
                              Strong
                                       C
```

### Slide 26

![Original slide 26](assets/strong-weak/page-26.jpg)

**Graph / visual semantics:** Neighborhood overlap: I is the number of shared neighbors of A and B, excluding A and B; T is the number of neighbors of A or B, also excluding them; NO=I/T.

**Extracted slide text:**

```text
NEIGHBORHOOD OVERLAP

• In practice we can rank the strengths of the links using the neighborhood overlap
• I = # of nodes who are neighbors of A AND B (excluding A and B)
• T = # of nodes who are neighbors of A OR B (excluding A and B)
• Neighborhood Overlap NO= I/T
```

### Slide 27

![Original slide 27](assets/strong-weak/page-27.jpg)

**Graph / visual semantics:** The displayed example computes neighborhood overlap as NO=2/5.

**Extracted slide text:**

```text
NEIGHBORHOOD OVERLAP

• Neighborhood Overlap NO= 2/5

                     A           B
```

### Slide 28

![Original slide 28](assets/strong-weak/page-28.jpg)

**Extracted slide text:**

```text
NEIGHBORHOOD OVERLAP

• Neighborhood Overlap NO= 0/3 (Local Bridge)

                      A                   B
```

### Slide 29

![Original slide 29](assets/strong-weak/page-29.jpg)

**Graph / visual semantics:** Partitioning overview: graph partition methods divide nodes into groups while trying to keep strongly related nodes together and/or minimize cross-group edges.

**Extracted slide text:**

```text
TEST YOUR UNDERSTANDING

                          Clustering Coefficient:
                          A
                          B
                          C
                     C    D

       A      B           Neighborhood overlap:
                          AB
                     D    BC
                          BD

                          Who has more advantages
                          of learning opening positions
```

### Slide 30

![Original slide 30](assets/strong-weak/page-30.jpg)

**Extracted slide text:**

```text
PARTITION METHODS

• Divisible Method
• Agglomerative Method
```

### Slide 31

![Original slide 31](assets/strong-weak/page-31.jpg)

**Graph / visual semantics:** Agglomerative partitioning: begin with many small groups and merge groups iteratively according to a similarity or linkage rule.

**Extracted slide text:**

```text
PARTITION METHODS: AGGLOMERATIVE
```

### Slide 32

![Original slide 32](assets/strong-weak/page-32.jpg)

**Extracted slide text:**

```text
PARTITION METHODS: AGGLOMERATIVE
```

### Slide 33

![Original slide 33](assets/strong-weak/page-33.jpg)

**Extracted slide text:**

```text
PARTITION METHODS: AGGLOMERATIVE
```

### Slide 34

![Original slide 34](assets/strong-weak/page-34.jpg)

**Extracted slide text:**

```text
PARTITION METHODS: AGGLOMERATIVE
```

### Slide 35

![Original slide 35](assets/strong-weak/page-35.jpg)

**Graph / visual semantics:** Divisive partitioning: begin with one graph and split it recursively into smaller groups.

**Extracted slide text:**

```text
PARTITION METHODS: DIVISIBLE
```

### Slide 36

![Original slide 36](assets/strong-weak/page-36.jpg)

**Extracted slide text:**

```text
PARTITION METHODS: DIVISIBLE
```

### Slide 37

![Original slide 37](assets/strong-weak/page-37.jpg)

**Graph / visual semantics:** Divisive/Newman-style graph meaning: the graph is repeatedly separated using edge-importance information; highlighted edges/nodes show the current split.

**Extracted slide text:**

```text
PARTITION METHODS: DIVISIBLE
```

### Slide 38

![Original slide 38](assets/strong-weak/page-38.jpg)

**Extracted slide text:**

```text
BETWEENNESS

• Betweenness of an edge: Total Amount of flow it carries, counting the flow between all
  pairs of nodes using this edge
                 1                                            A

            2         3                                  9         B

                                 7           8

            4         6                                  C         D

                 5                                            E
```

### Slide 39

![Original slide 39](assets/strong-weak/page-39.jpg)

**Extracted slide text:**

```text
BETWEENNESS OF (7,8) IS 98 = 49+49

• Every path from 1, 2, 3, 4, 5,6 to 8, 9, A, B, C, D,E uses (7,8). then, 7*7=49 units
• Every path from 8, 9, A, B, C D, E to 1, 2, 3, 4, 5,6 uses (7,8). then, 7*7=49 units
                  1                                               A

             2         3                                    9          B

                                   7           8

             4         6                                    C          D

                  5                                               E
```

### Slide 40

![Original slide 40](assets/strong-weak/page-40.jpg)

**Extracted slide text:**

```text
TEST YOUR UNDERSTANDING

• Betweenness of (3,7), (6,7), (8,9), (8,C), (1,2), (1,3), (2,3)

                   1                                               A

             2          3                                      9       B

                                     7           8

             4          6                                      C       D

                   5                                               E
```

### Slide 41

![Original slide 41](assets/strong-weak/page-41.jpg)

**Graph / visual semantics:** Betweenness meaning: edge/node betweenness counts how often an edge or node lies on shortest paths between other pairs. High-betweenness elements connect regions and are candidates for removal when partitioning.

**Extracted slide text:**

```text
PARTITION METHODS: DIVISIBLE (THE GIRVAN-
NEWMAN METHOD)
• Remove the edges with highest betweenness (7,8)

                1                                       A

           2         3                              9       B

                               7          8

           4         6                              C       D

                5                                       E
```

### Slide 42

![Original slide 42](assets/strong-weak/page-42.jpg)

**Extracted slide text:**

```text
PARTITION METHODS: DIVISIBLE (THE GIRVAN-
NEWMAN METHOD)
• Remove the next edges with highest betweenness (6,7) if there is a tie, break it arbitrarily

                  1                                             A

            2          3                                  9          B

                                  7           8

            4          6                                  C         D

                  5                                             E
```

### Slide 43

![Original slide 43](assets/strong-weak/page-43.jpg)

**Extracted slide text:**

```text
PARTITION METHODS: DIVISIBLE (THE GIRVAN-
NEWMAN METHOD)
• Remove the edges with highest betweenness (3,7), (8,9), (8C) and stop when the number
  of components is the desired
                 1                                         A

           2         3                                9         B

                                7          8

           4         6                                C         D

                 5                                         E
```

### Slide 44

![Original slide 44](assets/strong-weak/page-44.jpg)

**Extracted slide text:**

```text
COMPUTE BETWEENNESS VALUES

• For each node u
    • Perform the BFS of G from u
    • Determine the number of shortest paths from u to each other node
    • Determine the amount of flow from u to all other node that uses that edge

• Sum all the values for each node
```

### Slide 45

![Original slide 45](assets/strong-weak/page-45.jpg)

**Graph / visual semantics:** Betweenness algorithm: compute the contribution of the selected node to shortest paths, then propagate dependencies through the shortest-path tree.

**Extracted slide text:**

```text
CONSIDER NODE A

     F

B    C    I

A   D     G       K

E   H     J
```

### Slide 46

![Original slide 46](assets/strong-weak/page-46.jpg)

**Graph / visual semantics:** Flow/shortest-path graph meaning: the red node is the source under consideration; the graph shows its shortest-path structure to other nodes.

**Extracted slide text:**

```text
COMPUTE BFS FROM A

    F
                     A

B   C     I

A   D     G      K

E   H     J
```

### Slide 47

![Original slide 47](assets/strong-weak/page-47.jpg)

**Extracted slide text:**

```text
COMPUTE BFS FROM A

    F
                             A

                     B   C       D   E
B   C     I

A   D     G      K

E   H     J
```

### Slide 48

![Original slide 48](assets/strong-weak/page-48.jpg)

**Extracted slide text:**

```text
COMPUTE BFS FROM A

    F
                                 A

                     B       C           D       E
B   C     I

A   D     G     K        F           G       H

E   H     J
```

### Slide 49

![Original slide 49](assets/strong-weak/page-49.jpg)

**Graph / visual semantics:** The shortest paths from A are counted in the first graph, then compared with the expanded graph on the right. The highlighted red node is the current source.

**Extracted slide text:**

```text
COMPUTE BFS A

     F
                                A

                    B       C           D       E
B   C     I

A   D     G     K       F           G       H

                            I           J
E   H     J
```

### Slide 50

![Original slide 50](assets/strong-weak/page-50.jpg)

**Extracted slide text:**

```text
COMPUTE THE NUMBER OF SHORTEST PATHS
FROM A
    F
                                           A

                       1   B       C   1           1   D       E   1
B   C     I

A   D     G     K              F               G           H

                                   I                   J
E   H     J

                                               K
```

### Slide 51

![Original slide 51](assets/strong-weak/page-51.jpg)

**Extracted slide text:**

```text
COMPUTE BFS AND THE NUMBER OF SHORTEST
PATHS FROM A
    F
                                                    A

                            1       B       C   1           1   D       E   1
B   C     I

                    A-B-F                                                   A-D-H
A   D     G     K               2       F       1       G           H   2   A-E-H
                    A-C-F

                                            I                   J
E   H     J

                                                        K
```

### Slide 52

![Original slide 52](assets/strong-weak/page-52.jpg)

**Extracted slide text:**

```text
COMPUTE BFS AND THE NUMBER OF SHORTEST
PATHS FROM A
    F
                                                A

                        1       B       C   1           1   D             E   1
B   C     I

A   D     G     K           2       F       1       G               H    2

                      A-B-F-I                                           A-D-G-J
                      A-C-F-I       3   I                   J   3       A-D-H-J
E   H     J           A-D-G-I                                           A-E-H-J

                                                    K
```

### Slide 53

![Original slide 53](assets/strong-weak/page-53.jpg)

**Graph / visual semantics:** The slide aggregates shortest-path counts from the selected source. These counts feed the betweenness calculation.

**Extracted slide text:**

```text
COMPUTE BFS AND THE NUMBER OF SHORTEST
PATHS FROM A
    F
                                               A

                       1       B       C   1           1   D           E   1
B   C     I

A   D     G     K          2       F       1       G               H   2

                                   3   I                   J   3
E   H     J
                       All paths A-*-I +
                       All paths A-*-J   6         K
```

### Slide 54

![Original slide 54](assets/strong-weak/page-54.jpg)

**Graph / visual semantics:** Flow interpretation: the amount of flow from A to other nodes is divided across shortest paths; the image shows the accumulation step.

**Extracted slide text:**

```text
DETERMINE THE AMOUNT OF FLOW FROM A TO
ALL OTHER NODE IN G
    F
                                                          A

                                1       B         C   1           1   D             E   1
B   C     I

A   D    G       K                  2       F         1       G                 H   2

                                            3     I                    J    3
E   H     J
                K sends 3/6 of 1 unit to        1/2                   1/2
                I and J                                       K
                                                      6
```

### Slide 55

![Original slide 55](assets/strong-weak/page-55.jpg)

**Extracted slide text:**

```text
DETERMINE THE AMOUNT OF FLOW FROM A TO
ALL OTHER NODE IN G
    F
                                                    A

                               1    B       C   1           1   D     E   1
B   C     I

A   D    G        K                  2   F        1    G          H   2
               I received ½ plus 1
                                           1        1/2 1/2      1
               for a total of 3/2.
               F receives 2/3 of 3/2 and 3      I             J 3
E   H     J
               G receives 1/3 of the 3/2     1/2            1/2
                                                6       K
```

### Slide 56

![Original slide 56](assets/strong-weak/page-56.jpg)

**Graph / visual semantics:** The final diagram displays accumulated flow/dependency values on the graph, which are used to compute betweenness for the source node.

**Extracted slide text:**

```text
DETERMINE THE AMOUNT OF FLOW FROM A TO
ALL OTHER NODE IN G
    F
                                                     A
                                  2                                       2
                                                2         4
                      1       B             C   1             1     D             E       1
B   C     I
                          1                 1                 2      1                1

A   D    G      K         2       F             1         G                   H   2
                                      1             1/2       1/2         1
                                  3         I                        J    3
E   H     J
                                          1/2                       1/2
                                                6         K
```

### Slide 57

![Original slide 57](assets/strong-weak/page-57.jpg)

**Graph / visual semantics:** Final algorithm step: repeat the shortest-path/flow calculation for each node and sum contributions to obtain betweenness scores.

**Extracted slide text:**

```text
REPEAT THE PROCESS FOR EACH NODE.
THE BETWEENNESS OF EACH EDGE IS THE SUM
     F

B    C     I

A    D    G       K

E    H     J
```

### Slide 58

![Original slide 58](assets/strong-weak/page-58.jpg)

**Graph / visual semantics:** Knowledge check: apply the complete betweenness procedure to the shown graph.

**Extracted slide text:**

```text
TEST YOUR KNOWLEDGE: COMPUTE THE
BETWEENNESS VALUE FROM B
     F

B    C    I

A    D    G      K

E    H    J
```

