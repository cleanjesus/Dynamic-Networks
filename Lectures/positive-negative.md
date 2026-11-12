# Positive and Negative Relationships

Source: `Positive and Negative Relationships(1).pdf`

This deck develops structural balance for signed complete graphs, then extends the ideas to weak balance, non-complete graphs, and an algorithm for testing approximate balance. Positive and negative edge labels are preserved visually in every slide image.

> Preservation note: Every slide is represented by searchable extracted text **and** an embedded raster of the original slide. The image is authoritative for graph geometry, colors, labels, edge direction/placement, and staged highlights. Graph notes below explain the intended operation without replacing the original visual.

## Slide-by-slide content

### Slide 1

![Original slide 1](assets/positive-negative/page-01.jpg)

**Extracted slide text:**

```text
POSITIVE AND NEGATIVE
RELATIONSHIPS
CECS 427 DYNAMIC NETWORKS
```

### Slide 2

![Original slide 2](assets/positive-negative/page-02.jpg)

**Graph / visual semantics:** Signed-graph legend: + means a positive relationship/friendship; - means a negative relationship/antagonism. The deck treats the complete graph as the social setting.

**Extracted slide text:**

```text
POSITIVE AND NEGATIVE RELATIONSHIPS

• Suppose social network network that everybody knows each other (Complete Graphs)
• Each link has positive or negative attributes
    • Positive links represent friendship
    • Negative links represent antagonist

• The relation may create stress
• An important problem is to understand the tension between these two forces.
```

### Slide 3

![Original slide 3](assets/positive-negative/page-03.jpg)

**Graph / visual semantics:** Graph meaning: the triangle has three positive edges, so all three people are mutually friendly and the triangle is balanced.

**Extracted slide text:**

```text
NOTION OF STRUCTURAL BALANCE

                    A

                +       +

            B               C
                    +
```

### Slide 4

![Original slide 4](assets/positive-negative/page-04.jpg)

**Extracted slide text:**

```text
NOTION OF STRUCTURAL BALANCE

                                           A

                                 +             +

                             B                     C
                                           +

• A, B and C are friends. It is balanced
```

### Slide 5

![Original slide 5](assets/positive-negative/page-05.jpg)

**Graph / visual semantics:** Graph meaning: two positive edges and one negative edge create a stressed, unbalanced triangle: A is friendly with B and C, but B and C are antagonists.

**Extracted slide text:**

```text
NOTION OF STRUCTURAL BALANCE

                    A

                +       +

            B               C
                    -
```

### Slide 6

![Original slide 6](assets/positive-negative/page-06.jpg)

**Extracted slide text:**

```text
NOTION OF STRUCTURAL BALANCE

                                          A

                                  +               +

                              B                       C
                                          -
• A is friend of B and C, but B and C do not get along. Source of Stress and it is no balanced
```

### Slide 7

![Original slide 7](assets/positive-negative/page-07.jpg)

**Graph / visual semantics:** Graph meaning: one positive edge and two negative edges form a balanced triangle: A and B are friends, and both oppose C.

**Extracted slide text:**

```text
NOTION OF STRUCTURAL BALANCE

                    A

                +       -

            B               C
                    -
```

### Slide 8

![Original slide 8](assets/positive-negative/page-08.jpg)

**Extracted slide text:**

```text
NOTION OF STRUCTURAL BALANCE

                                        A

                                 +               -

                             B                       C
                                         -

• A and B are friends, but they don’t get along with C. No source of stress. It is Balance
```

### Slide 9

![Original slide 9](assets/positive-negative/page-09.jpg)

**Graph / visual semantics:** Graph meaning: three negative edges create an unbalanced triangle under strong balance; everyone is antagonistic toward everyone else.

**Extracted slide text:**

```text
NOTION OF STRUCTURAL BALANCE

                    A

                -       -

            B               C
                    -
```

### Slide 10

![Original slide 10](assets/positive-negative/page-10.jpg)

**Extracted slide text:**

```text
NOTION OF STRUCTURAL BALANCE

                                        A

                                 -              -

                             B                      C
                                        -

• No one gets along with any other. Source of stress. It is no Balance
```

### Slide 11

![Original slide 11](assets/positive-negative/page-11.jpg)

**Graph / visual semantics:** Graph meaning: the four possible signed triangle types are shown. Strong balance occurs when the triangle has either 3 positive edges or exactly 1 positive edge, equivalently an odd number of positive edges.

**Extracted slide text:**

```text
NOTION OF STRUCTURAL BALANCE

           A                            A                  A                      A

    +             +           +             +        -             -       -           -

B                     C   B                 C    B                     C   B                C
           +                        -                      +                       -

        Balance                   No Balance             Balance               No Balance

• What is the relation between the minus (plus) and the balance?
```

### Slide 12

![Original slide 12](assets/positive-negative/page-12.jpg)

**Graph / visual semantics:** Core rule: a signed complete graph is structurally balanced iff every triangle is balanced: all three edges are +, or exactly one edge is +.

**Extracted slide text:**

```text
DEFINING STRUCTURAL BALANCE

• We can generalize this to complete graphs, with edges labeled by +s and –s
• A labeled complete graph is balanced if every one of its triangles is balanced, i.e.
• Structural Balance Property: For every set of three nodes, if we consider the three
  edges connecting them,
    • either all three of these edges are labeled +, or
    • else exactly one of them is labeled +.
    • That is, every triangle must have an odd number of +s.
```

### Slide 13

![Original slide 13](assets/positive-negative/page-13.jpg)

**Extracted slide text:**

```text
EXAMPLES

              A                                   A

              +                               -
      -                   -           +                   -
              B                                   B
          -           -                   +           +

  D                           C   D                           C
                  +                               -
```

### Slide 14

![Original slide 14](assets/positive-negative/page-14.jpg)

**Graph / visual semantics:** Global characterization: a balanced complete graph is either one all-friends group, or two internally friendly groups with every cross-group edge negative.

**Extracted slide text:**

```text
A BALANCE LABEL COMPLETE GRAPH

• A label complete graph is balanced if every triangle is balanced according to the following
  rule:
    • Structural Balance Property: For every set of three nodes, if we consider the three edges
      connecting them either
         • All three of these edges are label “+” or
         • Exactly one of them is labeled “+”
```

### Slide 15

![Original slide 15](assets/positive-negative/page-15.jpg)

**Extracted slide text:**

```text
HOW DOES IT LOOK LIKE A LABELED COMPLETE
BALANCED GRAPH
1.   Either everybody likes each other or
2.   The world consists of two groups of mutual friends with complete antagonism
     between the groups
```

### Slide 16

![Original slide 16](assets/positive-negative/page-16.jpg)

**Extracted slide text:**

```text
CHARACTERIZATION OF A LABELED COMPLETE
BALANCED GRAPH

• If a complete graph can be divided into 2 sets of mutual friends with complete mutual antagonism
  between the two sets, then it is balanced

                      Mutual          Mutual                 Mutual
                      friends         antagonism             friends
                     inside X         between sets          inside Y

                      Set X                                 Set Y
```

### Slide 17

![Original slide 17](assets/positive-negative/page-17.jpg)

**Graph / visual semantics:** Balanced theorem: local triangle balance implies the global two-faction structure. If any negative edge exists, choose a node u; X is u plus its friends and Y is its enemies.

**Extracted slide text:**

```text
BALANCED THEOREM

• Theorem. If a label complete graph is balanced, then
    1. Either all pairs of nodes are friends
    2. Or else the nodes can be divided into two groups X and Y such that every pair of nodes in X
       (Y) like each other and, every node in X is enemy of everyone in Y.

• Local property implies Global property
• Proof: Let G be a label balanced complete graph.
    • If there are any edges with “-” label, then done.
    • Otherwise, pick any node u and define X to be u and all its friends and Y all its enemies
```

### Slide 18

![Original slide 18](assets/positive-negative/page-18.jpg)

**Graph / visual semantics:** Proof graph meaning: nodes are partitioned relative to u. The + and - relations from u constrain the signs among the nodes in X and Y.

**Extracted slide text:**

```text
PROOF

        v               x
            +       -
            +   u   -
        w               y
```

### Slide 19

![Original slide 19](assets/positive-negative/page-19.jpg)

**Extracted slide text:**

```text
PROOF

                    ?
            v               x
                +       -
        ?           u           ?
                +       -
            w               y
```

### Slide 20

![Original slide 20](assets/positive-negative/page-20.jpg)

**Extracted slide text:**

```text
APPLICATIONS: INTERNATIONAL RELATIONS,
TRUST, DISTRUST, ON-LINE RATING
```

### Slide 21

![Original slide 21](assets/positive-negative/page-21.jpg)

**Graph / visual semantics:** Weak balance changes the allowed configurations and is introduced as a relaxation of strong structural balance.

**Extracted slide text:**

```text
WEAKLY BALANCED

                    A                             A

          +             +                 -           -

         B              C                 B           C
                -                             -

• Which one is stronger form of stress?
```

### Slide 22

![Original slide 22](assets/positive-negative/page-22.jpg)

**Extracted slide text:**

```text
WEAK STRUCTURAL BALANCE PROPERTY

• Weak Structural Balance Property: There is no set of three nodes such that the edges among them
  consist of exactly two positive edges and one negative edge.

                                         A

                                  +           +

                                   B          C
                                         -

• A labeled, complete graph is weakly Balanced if the weak structural Balance property holds
```

### Slide 23

![Original slide 23](assets/positive-negative/page-23.jpg)

**Graph / visual semantics:** Weak-balance characterization: the relevant partition may contain more than two mutually friendly groups, with antagonistic relations between groups, depending on the precise weak-balance definition used in the deck.

**Extracted slide text:**

```text
CHARACTERIZATION

                                  Y
                       mutual
                       friends
        mutual         inside V
    W   friends                              mutual     X
        inside                               friends
                       Mutual                inside X
        W
                     Antagonism
                   between all sets

        mutual                        mutual
    Y   friends                       friends
        inside Y                      inside Z      Z
```

### Slide 24

![Original slide 24](assets/positive-negative/page-24.jpg)

**Extracted slide text:**

```text
WEAKLY BALANCED THEOREM

• Theorem (Weakly Balanced Theorem): If a labeled complete graph is weakly balanced, then its
  nodes can be divided into groups in such a way that every two nodes belonging to the same
  group are friends, and every two nodes belonging to different groups are enemies.
• Proof:           X                           G \ X (Complete graph)

                   v                                    x
                         +                       -
                         +            u           -
                   w                                    y
```

### Slide 25

![Original slide 25](assets/positive-negative/page-25.jpg)

**Extracted slide text:**

```text
WEAKLY BALANCED THEOREM

• Proof:

               X           G \ X (Complete graph)

                       ?
               v                    x
                   +         -
           ?       +   u     -
               w                    y
```

### Slide 26

![Original slide 26](assets/positive-negative/page-26.jpg)

**Extracted slide text:**

```text
GENERALIZING STRUCTURAL BALANCE

• So far with the studied concepts, we have the following drawback
    • Only complete graphs
    • Triangle assumption applies to all triangles

• We can relax the following assumptions:
    • The graph assumption to non-complete graph?
    • The triangle assumption to say that if most triangles are balanced, then the world can be
      approximately divided into fractions?
```

### Slide 27

![Original slide 27](assets/positive-negative/page-27.jpg)

**Graph / visual semantics:** Non-complete graph meaning: missing edges represent absent/unknown relationships, so not every triple is a signed triangle. The later method reasons over observed edges and paths.

**Extracted slide text:**

```text
NON-COMPLETE NETWORKS: BFS METHOD

                                 1
                             +            +
                                 +
                         2                    3
                 -           +                         -
                                                                        +
            4                    5                         6                     8
                                              -
        -            -                                              -
                                                                                 -
                                                           -
    9                    7                    10                        11

                     +                                 -                             -
        +                            +
            12                       13                        15                        14
                             +                     -                         -
```

### Slide 28

![Original slide 28](assets/positive-negative/page-28.jpg)

**Extracted slide text:**

```text
NON-COMPLETE GRAPHS

• How to verify that a graph is weakly balanced?

                         -       1     +

                    1                          1

                    +                      -
                             1        1
                                 +
```

### Slide 29

![Original slide 29](assets/positive-negative/page-29.jpg)

**Graph / visual semantics:** Local-view graph meaning: inspect signed triangles or local neighborhoods around one node to find violations of balance.

**Extracted slide text:**

```text
LOCAL VIEW

• Treat balance for non-complete labeled graph as a problem of filling in “missing edges”
• A non-complete labeled graph is balanced if it can be complete by adding edges to form a
  signed complete graph that is balanced
                         -       1     +

                     1                         1

                     +                     -
                             1        1
                                 +
```

### Slide 30

![Original slide 30](assets/positive-negative/page-30.jpg)

**Graph / visual semantics:** Global-view graph meaning: evaluate the signed network as a whole and compare its connected structure with a balanced partition.

**Extracted slide text:**

```text
GLOBAL VIEW

• Partition the graph in two sets X,Y such that nodes in X(resp Y) are all mutual friends;
  and nodes in X are all enemies of each node in Y

                          -       1     +

                     1                          1

                     +                      -
                              1        1
                                  +
```

### Slide 31

![Original slide 31](assets/positive-negative/page-31.jpg)

**Extracted slide text:**

```text
THE FIRST DEFINITION AND THE SECOND
DEFINITION ARE EQUIVALENT.
• If a signed graph is balanced under the first definition,
    • then after filling in all the missing edges appropriately, we have a signed complete graph
    • We can apply the Balance Theorem.

• If a signed graph is balanced under the second definition,
    • After finding a division of the nodes into sets X and Y, we can fill in positive edges inside X and
      inside Y, and fill in negative edges between X and Y, and then we can check that all triangles will
      be balanced.
    • So this gives a filling-in that satisfies the first definition.
```

### Slide 32

![Original slide 32](assets/positive-negative/page-32.jpg)

**Extracted slide text:**

```text
CHARACTERIZATION (GLOBAL VIEW)

• A signed graph containing a cycle with an odd number of negative edges cannot be
  balanced.

                        -       1     +

                    1                         1

                    -                     -
                            1        1
                                +
```

### Slide 33

![Original slide 33](assets/positive-negative/page-33.jpg)

**Extracted slide text:**

```text
ALGORITHM

• First, find the connected components using only positive edges and declare each of these
  components to be supernodes
    • Nodes connected with “+” belong to the same set
    • Supernodes are connected using only positive edges
    • If any supernode contains a negative edge between two nodes, we have a cycle of odd number
      of “-”
```

### Slide 34

![Original slide 34](assets/positive-negative/page-34.jpg)

**Graph / visual semantics:** Algorithm graph meaning: the deck begins an approximate-balance procedure on a non-complete signed graph, using a selected node and propagated sign constraints.

**Extracted slide text:**

```text
NON-COMPLETE NETWORKS: BFS METHOD

                                 1
                             +            +
                                 +
                         2                    3
                 -           +                         -
                                                                        +
            4                    5                         6                     8
                                              -
        -            -                                              -
                                                                                 -
                                                           -
    9                    7                    10                        11

                     +                                 -                             -
        +                            +
            12                       13                        15                        14
                             +                     -                         -
```

### Slide 35

![Original slide 35](assets/positive-negative/page-35.jpg)

**Graph / visual semantics:** Algorithm first step: select an initial node/seed and use its signed relationships to establish provisional group membership or sign labels.

**Extracted slide text:**

```text
ALGORITHM (FIRST STEP)

                                  1
                              +            +
                                  +
                          2                    3
                  -           +                         -
                                                                         +
             4                    5                         6                     8
                                               -
         -            -                                              -
                                                                                  -
                                                            -
     9                    7                    10                        11

                      +                                 -                             -
         +                            +
             12                       13                        15                        14
                              +                     -                         -
```

### Slide 36

![Original slide 36](assets/positive-negative/page-36.jpg)

**Extracted slide text:**

```text
• If a supernode contains two nodes connected with a “-” link, we have a cycle if odd
  numbers of “-”.
• Otherwise, there is no internal problem.
```

### Slide 37

![Original slide 37](assets/positive-negative/page-37.jpg)

**Graph / visual semantics:** Algorithm second step: propagate labels through the graph. Green highlighting marks the currently examined/assigned node or constraint.

**Extracted slide text:**

```text
ALGORITHM (SECOND STEP)

                        A           1
                                +            +                                                         A
                                    +
                            2                    3
                    -                                                C
                                +                      -
                                                                                                               C
       B                                                                 +                     B
               4                    5                       6                     8
                                                 -
           -            -                                            -
   D                                                                              -                            E
                                                            - E
       9                    7                    10                      11                        D
                        +                              -                              -                    F       G
           +                            +
               12                       13                      15                        14
                                +                     - F                     -
                                                                                  G
```

### Slide 38

![Original slide 38](assets/positive-negative/page-38.jpg)

**Extracted slide text:**

```text
ALGORITHM (SECOND STEP)

                   A

                           C
           B

                           E
               D
                       F       G
```

### Slide 39

![Original slide 39](assets/positive-negative/page-39.jpg)

**Graph / visual semantics:** Algorithm second step, complete graph: the traversal continues until all nodes are assigned or a contradiction is found.

**Extracted slide text:**

```text
ALGORITHM (SECOND STEP)
COMPUTE BFS FROM G
                  G
```

### Slide 40

![Original slide 40](assets/positive-negative/page-40.jpg)

**Extracted slide text:**

```text
ALGORITHM (SECOND STEP)
ALL NODES AT DISTANCE 1
                   G

               E       F
```

### Slide 41

![Original slide 41](assets/positive-negative/page-41.jpg)

**Extracted slide text:**

```text
ALGORITHM (SECOND STEP)
ALL NODES AT DISTANCE 2
                   G

               F       E

                   D       C
```

### Slide 42

![Original slide 42](assets/positive-negative/page-42.jpg)

**Extracted slide text:**

```text
ALGORITHM (SECOND STEP)
ALL NODES AT DISTANCE 3
                   G

               F       E

                   D       C

                   B       A
```

### Slide 43

![Original slide 43](assets/positive-negative/page-43.jpg)

**Extracted slide text:**

```text
ALGORITHM (SECOND STEP)

• If all edges are between adjacent layers, the graph is bipartite.
• We can find a partition of two sets, i.e.,
    • All nodes at odd distance from the root are in set X
    • All nodes at even distance from the root are in set Y

• Otherwise, there exists an edge connecting two nodes of the same layer and the graph
  has a cycle of odd length. Therefore, the graph is not balanced.
```

### Slide 44

![Original slide 44](assets/positive-negative/page-44.jpg)

**Extracted slide text:**

```text
ALGORITHM (SECOND STEP)

                   G

                               Same length, say k
               F       E

                   D       C

                   B       A
```

### Slide 45

![Original slide 45](assets/positive-negative/page-45.jpg)

**Extracted slide text:**

```text
ALGORITHM (SECOND STEP)

                            G

                        F       E

Cycle of length 2k +1
G-E-D-B                     D       C
G-F-C-A
B-A                                     The graph is not balanced

                            B       A
```

### Slide 46

![Original slide 46](assets/positive-negative/page-46.jpg)

**Graph / visual semantics:** Test graph: the signed network is checked for consistency of implied labels and for edges that violate the proposed partition.

**Extracted slide text:**

```text
TEST YOUR KNOWLEDGE 1/2

                                  1
                              +            +
                                  +
                          2                    3
                  +           +                         -
                                                                     +
             4                    5                         6                 8
                                               -
         -            -                                         -
                                                                              -
                                                            -
     9                    7                    10                        11

                  +                   +                 -
         +                                                                -
             12                       13                            14
                              +                     -
```

### Slide 47

![Original slide 47](assets/positive-negative/page-47.jpg)

**Extracted slide text:**

```text
TEST YOUR KNOWLEDGE 2/2

                                  1
                              +            +
                                  +
                          2                    3
                  +           +                         -
                                                                     +
             4                    5                         6                 8
                                               -
         -            -                                         -
                                                                              -
                                                            -
     9                    7                    10                        11

                  +                   +                 -
         +                                                                +
             12                       13                            14
                              +                     -
```

### Slide 48

![Original slide 48](assets/positive-negative/page-48.jpg)

**Graph / visual semantics:** Approximate balance in complete graphs: the deck frames the objective as minimizing the number of unbalanced triangles or disagreements.

**Extracted slide text:**

```text
APPROXIMATELY BALANCED NETWORKS IN
COMPLETE GRAPHS (ORIGINAL THEOREM)
• Theorem. If a label complete graph is balanced, then
     1. Either all pairs of nodes are friends
     2. Or else the nodes can be divided into two groups X and Y such that every pair of nodes in X
        (Y) like each other and, every node in X is enemy of everyone in Y.

• The conditions of this theorem are fairly extreme, in that we require every single triangle to be
  balanced

• What if we only know that most triangles are balanced?
```

### Slide 49

![Original slide 49](assets/positive-negative/page-49.jpg)

**Graph / visual semantics:** Approximate balance in complete graphs: the complete-graph setting allows every triple to be evaluated, so triangle counting provides a direct score.

**Extracted slide text:**

```text
APPROXIMATELY BALANCED NETWORKS IN
COMPLETE GRAPHS
• Theorem. If at least 99% of all the triangles in a label complete graph are balanced, then
    1. Either there is a set consisting of at least 90% of the nodes in which at least 90% of all pairs
       are friends, or else
    2. The nodes can be divided into two groups, X and Y , such that
         (i) at least 90% of the pairs in X like each other,
         (ii) at least 90% of the pairs in Y like each other, and
         (iii) at least 90% of the pairs with one end in X and the other end in Y are enemies.
```

### Slide 50

![Original slide 50](assets/positive-negative/page-50.jpg)

**Extracted slide text:**

```text
APPROXIMATELY BALANCED NETWORKS IN
COMPLETE GRAPHS
• Theorem. Let ε be any number such that 0 ≤ ε < 1/8 , and define δ = 3√ε. If at least 1 − ε of all triangles
  in a labeled complete graph are balanced, then
     1.   Either there is a set consisting of at least 1−δ of the nodes in which at least 1−δ of all pairs are friends, or else
     2.   the nodes can be divided into two groups, X and Y , such that
           (i) at least 1 − δ of the pairs in X like each other,
           (ii) at least 1 − δ of the pairs in Y like each other, and
           (iii) at least 1−δ of the pairs with one end in X and the other end in Y are enemies.

• Notice that the Balance Theorem is the case in which ε = 0, and the other claim above is the
  case in which ε = .001 (since in this latter case, δ = 3√ε = .1).
```

### Slide 51

![Original slide 51](assets/positive-negative/page-51.jpg)

**Graph / visual semantics:** Proof graph meaning: count triangles by considering how each node participates in triples; the diagram illustrates the combinatorial decomposition.

**Extracted slide text:**

```text
PROOF (NUMBER OF TRIANGLES)

• How many triangles are in a complete graph
    • There are N ways to pick the first corner,
         • Then N-1 ways to select the second corner
         • And N-2 ways to select the third corner
    • But a triangle with corners A,B,C will appear in six times
         • ABC,ACB,BAC,BCA,CAB, and CBA.
    • In general, each triangle will appear six times in this list, and so the total number of triangles is
         • N(N − 1)(N − 2)/6
```

### Slide 52

![Original slide 52](assets/positive-negative/page-52.jpg)

**Graph / visual semantics:** Proof graph meaning: count unbalanced triangles by classifying the sign patterns that violate the balance rule.

**Extracted slide text:**

```text
PROOF (AVERAGE NUMBER OF UNBALANCED
TRIANGLES OF A NODE)
• By hypothesis
    • #balanced Triangles is εN (N − 1)(N − 2)/6
• Define weight of a node to be the number of unbalanced triangles that it is a part of
    • A node of low weight will have relatively few unbalanced triangles.
• The total weight of all nodes is at most 3εN(N − 1)(N − 2)/6 = εN(N − 1)(N − 2)/2.
• There are N nodes, so the average weight of a node is at most ε(N − 1)(N − 2)/2.
• There must exist one node whose weight is equal to the average or below (Pigeon hole
  principle)
```

### Slide 53

![Original slide 53](assets/positive-negative/page-53.jpg)

**Extracted slide text:**

```text
PROOF

• Let’s pick one such node and call it A (good node)
• The weight of A is at most ε(N − 1)(N − 2)/2.
• Taking an upper bound ε(N − 1)(N − 2)/2 < εN2/2
```

### Slide 54

![Original slide 54](assets/positive-negative/page-54.jpg)

**Graph / visual semantics:** Partition proof: splitting the graph according to a selected/good node creates two groups whose internal and cross-group signs can be tested.

**Extracted slide text:**

```text
PROOF (SPLITTING THE GRAPH ACCORDING TO
THE GOOD NODE)

                X                      Y
                        Mainly
                        negative
                B                      D
                    +              -       Mainly
     Mainly
                          A                positive
     positive       +              -
                C                      E
```

### Slide 55

![Original slide 55](assets/positive-negative/page-55.jpg)

**Extracted slide text:**

```text
PROOF (HOW MANY DISTINCT EDGES THAT FORM
UNBALANCED TRIANGLES?)
• Each negative edge connecting two nodes in X creates a distinct unbalanced triangle
  involving node A.
    • Since there are at most εN2/2 unbalanced triangles involving A, there are at most εN2/2
      negative edges inside X.
• A closely analogous argument applies to Y and there are at most εN2/2 unbalanced
  triangles.
• Edges with one end in X and the other end in Y.
    • Each such edge that is positive creates a distinct unbalanced triangle involving A, and so there
      are at most εN2/2 positive edges with one end in X and the other end in Y .
```

### Slide 56

![Original slide 56](assets/positive-negative/page-56.jpg)

**Graph / visual semantics:** Counting result: either X or Y contains almost all of the graph under the relevant partition argument; the slide image preserves the exact theorem statement and diagram.

**Extracted slide text:**

```text
EITHER X OR Y CONSISTS OF ALMOST THE ENTIRE
GRAPH (FINDING THE PROPORTION)
• Let x be the number of nodes in X and y be the number of nodes in Y.
    • Suppose that x≥(1−δ)N (by hypothesis)
     • Since ε <1/8 and δ = 3√ε, it follows that δ<1/2, and x>N/2.
     • X has x nodes, so it has x(x − 1)/2 edges.
     • Since x > N/2 this number of edges is at least (N/2 + 1)(N/2)/2 ≥ (N/2)2/2 = N2/8.
     • There are at most εN2/2 negative edges inside X, and so the fraction of negative edges inside X is at most
          • εN2/2/N2/8 =4ε=4δ3 <δ
     where we use the facts that ε = δ3 and δ < 1/2
     • We thus conclude that if X contains at least (1 − δ)N nodes, then it is a set containing at least a (1−δ)
       fraction of the nodes in which at least 1 − δ of all pairs are friends, satisfying part (i) in the conclusion of
       the claim.
```

### Slide 57

![Original slide 57](assets/positive-negative/page-57.jpg)

**Graph / visual semantics:** Final counting statement: the number of nodes/triangles is bounded by a non-negligible proportion, completing the approximate-balance argument.

**Extracted slide text:**

```text
X AND Y CONTAIN A NON-NEGLIGIBLE NUMBER OF
NODES (FINDING THE PROPORTION)
• Suppose max(x,y)<(1−δ)N. Of all the edges with one end in X and the other in Y, what fraction are positive?
     • there are x ways to choose the end in X, and then y ways to choose the end in Y , for a total of xy
• Since each of x and y are less than (1 − δ)N, and they add up to N, this product xy is at least (δN)(1 − δ)N = δ(1 −
  δ)N2 ≥ δN2/2 since δ < 1/2
• There are at most εN2/2 positive edges with one end in X and the other in Y, so as a fraction of the total this is
  at most
     • εN2/2/ δN2/2 = ε/ δ = δ2 < δ
• Finally, what fraction of edges inside each of X and Y are negative?
• Consider X (Y is analogous): There are x(x − 1)/2 edges inside X in total, and since x > δN, this total number of
  edges is at least (δN + 1)(δN)/2 ≥ (δN)2/2 = δ2N2/2.
• There are at most εN2/2 negative edges inside X, so as a fraction of the total this is at most
     • εN2/2/ δ2N2/2 = ε/δ2 = δ
```

