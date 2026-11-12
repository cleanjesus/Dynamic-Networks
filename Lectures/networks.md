# Networks in Their Surrounding Contexts

Source: `Networks in Their Surrounding(1).pdf`

This deck studies context outside the node-edge structure: homophily, affiliation networks, triadic/focal/membership closure, and empirical link formation. The slide image is retained for every page because node colors, edge placement, and staged graph changes carry meaning.

> Preservation note: Every slide is represented by searchable extracted text **and** an embedded raster of the original slide. The image is authoritative for graph geometry, colors, labels, edge direction/placement, and staged highlights. Graph notes below explain the intended operation without replacing the original visual.

## Slide-by-slide content

### Slide 1

![Original slide 1](assets/networks/page-01.jpg)

**Extracted slide text:**

```text
NETWORKS IN THEIR
SURROUNDING
CONTEXTS
CECS 427 DYNAMIC NETWORKS
```

### Slide 2

![Original slide 2](assets/networks/page-02.jpg)

**Graph / visual semantics:** Graph meaning: blue and red node colors represent a contextual attribute. The surrounding context is information outside the edge set; homophily is the tendency for connected nodes to be similar.

**Extracted slide text:**

```text
NETWORK SURROUNDING CONTEXT

• Context outside of nodes and edges
• Homophily: The principle that we tend to be similar to our friends
```

### Slide 3

![Original slide 3](assets/networks/page-03.jpg)

**Graph / visual semantics:** Graph meaning: the example contains 9 nodes: 6 blue and 3 red, so p(blue)=6/9=2/3 and p(red)=3/9=1/3.

**Extracted slide text:**

```text
HOMOPHILY TEST

• What is the proportion p of blue nodes and proportion of red nodes?

p = 6/9=2/3
1-p = 3/9=1/3
```

### Slide 4

![Original slide 4](assets/networks/page-04.jpg)

**Graph / visual semantics:** Graph meaning: under no homophily, an edge is expected to be blue-blue with probability p^2, red-red with probability (1-p)^2, or cross-color with probability p(1-p) in each direction. The total cross-color probability is 2p(1-p).

**Extracted slide text:**

```text
HOMOPHILY TEST

• If no homophily is present, the number of edges that we expect to see is:
                                                p2

                                                p(1-p)

                                                p(1-p)

                                                (1-p)2
```

### Slide 5

![Original slide 5](assets/networks/page-05.jpg)

**Extracted slide text:**

```text
HOMOPHILY TEST

• Consider any edge (i, j) ∈ E
• Consider the random variable Xij = 1 if it is a cross-edge, and Xij = 0 otherwise.
• Then Xij is a Bernoulli random variable such that
    • P(Xij = 1) = 2p(1 − p).
    • µ0 = E[Xij] = 2p(1 − p)
    • σ0 = 2p(1 − p)(1 − 2p(1 − p))
```

### Slide 6

![Original slide 6](assets/networks/page-06.jpg)

**Graph / visual semantics:** Graph meaning: the displayed network has 18 edges, of which 5 are cross-color. The observed cross-color fraction is 5/18, compared with the null expectation 2(1/3)(2/3)=4/9=8/18; the lower observed fraction is evidence of homophily.

**Extracted slide text:**

```text
HOMOPHILY TEST

• Homophily Test: If the fraction of cross-color edges is significantly less that 2p(1-p)
```

### Slide 7

![Original slide 7](assets/networks/page-07.jpg)

**Extracted slide text:**

```text
HOMOPHILY TEST

• 18 edges 5 of them cross-color. Therefore 5/18 edges are cross color

• 2p(1-p) = 2 (1/3)(2/3) = 4/9 = 8/18
• 5/18 < 8/18 therefore there is evidence of homophily
```

### Slide 8

![Original slide 8](assets/networks/page-08.jpg)

**Extracted slide text:**

```text
HOMOPHILY STATISTICAL TEST
T-STUDENT TEST
• What does it mean “significantly less than”? It can be a standard measures of statistical
  significance
• Null Hypothesis: mu ≥ µ0
• Alternate Hypothesis: mu < µ0
    • µ0 = 2p(1-p)
    • σ0 = 2p(1 − p)(1 − 2p(1 − p))
    • Using the Student t-Test (How many standard errors mu is away from the hypothesized mean
      𝜇 )
         • Accept if |mu - µ0 | √𝑛 / (σ0) > table value with n-1 degree of freedom and given p-value (regularly 0.05)
```

### Slide 9

![Original slide 9](assets/networks/page-09.jpg)

**Extracted slide text:**

```text
Error Type I     Error Type II
False Positive   False Negative
```

### Slide 10

![Original slide 10](assets/networks/page-10.jpg)

**Extracted slide text:**

```text
TEST YOUR KNOWLEDGE

• Determine if the graph before has evidence of Homophily using one tailed t-student
  test with 0.05 significance level.
• Use a table from the web (https://www.sjsu.edu/faculty/gerstman/StatPrimer/t-
  table.pdf). It should be 1.740
```

### Slide 11

![Original slide 11](assets/networks/page-11.jpg)

**Extracted slide text:**

```text
HOMOPHILY STATISTICAL TEST

from scipy import stats
import numpy as np

#non crossing edges
x = (1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
# Population Mean
p = 4/9
mu = 2 * p * (1 - p)
# Using the Stats library, compute t-statistic and p-value
res = stats.ttest_1samp(a=x, popmean = mu, alternative="less")
ci = res.confidence_interval()
print(f"Alternate Hypothesis is {mu} < {ci.high} = {mu < ci.high}") # True
```

### Slide 12

![Original slide 12](assets/networks/page-12.jpg)

**Extracted slide text:**

```text
AFFILIATION NETWORKS

• We have networks that are based on similar characteristics of the nodes
• Although they are outside of the network, it’s possible to put these contexts inside
• We will take a very general view of the notion of an “activity”
• we’ll refer to such activities as foci — that is, “focal points”
```

### Slide 13

![Original slide 13](assets/networks/page-13.jpg)

**Graph / visual semantics:** Graph meaning: a bipartite affiliation network connects people {Frank, Anna, Stephany, Brian} to activities/foci {CECS 427, CECS 491A, ACM, MAES, CECS 478}. Person-to-focus edges encode participation, not friendship.

**Extracted slide text:**

```text
AN AFFILIATION NETWORK

       Frank             CECS 427

                         CECS 491A
       Anna
                           ACM

      Stephany
                           MAES

       Brian             CECS 478
```

### Slide 14

![Original slide 14](assets/networks/page-14.jpg)

**Graph / visual semantics:** Graph meaning: a social-affiliation network combines people and a focus. Shared participation in CECS 427 or ACM creates an indirect basis for social connections among people.

**Extracted slide text:**

```text
A SOCIAL-AFFILIATION NETWORK

  Brian

 Stephany    Anna       CECS 427

             ACM          Frank
```

### Slide 15

![Original slide 15](assets/networks/page-15.jpg)

**Graph / visual semantics:** Graph meaning: triadic closure: Brian and Anna become linked because both are connected to Stephany, closing a three-person triangle.

**Extracted slide text:**

```text
TRIADIC CLOSURE

        Brian                Anna

                  Stephany
```

### Slide 16

![Original slide 16](assets/networks/page-16.jpg)

**Graph / visual semantics:** Graph meaning: focal closure: Frank and Anna become linked because both participate in the same focus, CECS 427.

**Extracted slide text:**

```text
FOCAL CLOSURE

        Frank              Anna

                CECS 427
```

### Slide 17

![Original slide 17](assets/networks/page-17.jpg)

**Graph / visual semantics:** Graph meaning: membership closure: Stephany and Anna become linked because both belong to ACM.

**Extracted slide text:**

```text
MEMBERSHIP CLOSURE

         Stephany           ACM

                     Anna
```

### Slide 18

![Original slide 18](assets/networks/page-18.jpg)

**Graph / visual semantics:** Graph meaning: Snapshot 1 is the earlier bipartite/social-affiliation state used to identify unconnected pairs and their common neighbors or foci.

**Extracted slide text:**

```text
TRACKING LINK FORMATION IN ON-LINE DATA
SNAPSHOT 1

      Brian

     Stephany    Anna      CECS 427

                 ACM         Frank
```

### Slide 19

![Original slide 19](assets/networks/page-19.jpg)

**Graph / visual semantics:** Graph meaning: Snapshot 2 is the later state. New red edges show links that formed between snapshots, enabling empirical measurement of link formation.

**Extracted slide text:**

```text
TRACKING LINK FORMATION IN ON-LINE DATA
SNAPSHOT 2

      Brian

     Stephany    Anna      CECS 427

                 ACM         Frank
```

### Slide 20

![Original slide 20](assets/networks/page-20.jpg)

**Extracted slide text:**

```text
LIKELY FRIENDS

1.   We take two snapshots of the network at different times
2.   For each k, we identify all pairs of nodes who have exactly k friends in common in the first
     snapshot, but who are not directly connected by an edge.
3.   We define T(k) to be the fraction of these pairs that have formed an edge by the time of
     the second snapshot.
4.   T(k) is the empirical estimate for the probability that a link will form between two people
     with k friends in common.
5.   We can plot T(k) as a function of k to illustrate the effect of common friends on the
     formation of links.
```

### Slide 21

![Original slide 21](assets/networks/page-21.jpg)

**Graph / visual semantics:** Graph meaning: in the example, candidate pairs with k=1 and k=2 common friends are tracked from S1 to S2. T(1)=1/2 and T(2)=1/2 for the shown candidates.

**Extracted slide text:**

```text
EXAMPLE

              S1                            S2

              e                             e
          a                         a
                         b                       b
f                            f

          c   d                     c       d

    k=1            k=2
    f,a            e,d           T(1) = ½
    c,d            a,b           T(2) = ½
```

### Slide 22

![Original slide 22](assets/networks/page-22.jpg)

**Extracted slide text:**

```text
HOW MUCH MORE LIKELY IS A LINK TO FORM IF IT
HAS THE EFFECT OF CLOSING A TRIANGLE?
• Suppose that for some small probability p, each common friend that two people have
  gives them an independent probability p of forming a link each day.
• If two people have k friends in common, the probability they fail to form a link on any
  given day is (1−p)k
• The probability that it does form, is
                  Tbaseline(k) = 1 − (1 − p)k
```

### Slide 23

![Original slide 23](assets/networks/page-23.jpg)

**Graph / visual semantics:** Graph meaning: the same S1/S2 example illustrates the baseline model. If each common friend independently creates a daily link probability p, then T_baseline(k)=1-(1-p)^k; with p=1/2, T_baseline(1)=1/2 and T_baseline(2)=3/4.

**Extracted slide text:**

```text
EXAMPLE

              S1                            S2

              e                             e
          a                         a
                         b                        b
f                            f

          c   d                     c       d

    k=1            k=2                           Tbaseline(1) = 1 − (1 − 1/2)
    f,a            e,d           T(1) = ½
    c,d            a,b                           Tbaseline(2) = 1 − (1 − 1/2)2
                                 T(2) = ½
```

