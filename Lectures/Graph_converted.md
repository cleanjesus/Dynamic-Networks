# CECS 427 Dynamic Networks - Graphs

## Purpose of this conversion

This document is a context-preserving Markdown transcription of the 28-slide deck **Graphs** for CECS 427, Dynamic Networks. It includes:

- the text on every slide;
- explanations of diagrams, maps, colors, arrows, and animation states;
- the exact graph structures used in the examples;
- the BFS levels shown across the animated slides;
- the mathematical statements and proof steps in Markdown/LaTeX;
- clarifying notes where the original slide wording is abbreviated or contains a likely typo.

The deck is primarily an introduction to graph/network terminology, connected components, breadth-first search, two basic theorems for undirected graphs, and the Erdos-Renyi random graph model.

---

## Slide 1 - Title

**Title:** GRAPHS  
**Course:** CECS 427 DYNAMIC NETWORKS

The slide is a title slide with no additional technical content.

---

## Slide 2 - Graphs

### Slide text

- **What is a Network/Graph?**
- A generalization of the simple concept of a set of dots, links, edges, or arcs.
- Representation: a graph `G = (V, E)` consists of a set of vertices denoted by `V` and a set of edges denoted by `E`.
- Example: in the Facebook graph, each user is a vertex (or node).
- Example: in the Facebook graph, a friend relationship is an edge.

### Meaning

A graph is a mathematical model for objects and relationships. The objects are represented by vertices/nodes, and the relationships between objects are represented by edges/links/arcs.

`G = (V, E)` means:

- `V` is the collection of vertices;
- `E` is the collection of edges connecting pairs of vertices.

For a social network, users are vertices and friendships are edges. The same abstraction can model routers and communication links, web pages and hyperlinks, or proteins and biological interactions.

---

## Slide 3 - Type of Edges

### Directed edges

- A directed edge is an **ordered pair** of vertices.
- It is written `(u, v)` and points from vertex `u` to vertex `v`.
- The direction matters: `(u, v)` and `(v, u)` are different directed edges.

### Undirected edges

- An undirected edge is an **unordered pair** of vertices.
- It is written `{u, v}`.
- Direction is disregarded, so the two endpoints are interchangeable: `{u, v} = {v, u}`.

### Diagram description

The slide shows two vertices, `A` and `B`:

- the directed example has an arrow from `A` to `B`;
- the undirected example has a line connecting `A` and `B` without an arrowhead.

---

## Slide 4 - Examples of directed and undirected graphs

The slide compares the same four-vertex structure in two forms.

### Undirected example

Vertices: `{A, B, C, D}`

Edges:

```text
{A, B}, {B, C}, {B, D}, {C, D}
```

The lines have no direction. For example, traveling from `C` to `D` is equivalent to traveling from `D` to `C`.

### Directed example

Vertices: `{A, B, C, D}`

The visible directed edges are:

```text
A -> B
B -> C
C -> D
D -> B
```

The arrows matter. For instance, `D -> B` does not imply `B -> D` unless a second arrow is explicitly present.

---

## Slide 5 - Applications

### Slide text

- Large graphs/networks are all around us.
- **Internet:** vertices are routers/switches and edges are links.
- **World Wide Web:** vertices are webpages, and edges are URL links on one webpage pointing to another webpage.
- **Social networks:** Facebook, Twitter, LinkedIn.
- **Biological networks:** DNA interaction graphs, ecosystem graphs, and so forth.

### Meaning

Graph theory is useful because many systems can be reduced to the same structure: entities plus relationships. The interpretation of a vertex and an edge changes by application, but graph algorithms can often be reused.

---

## Slide 6 - Network structure

### Slide text

- “Six degrees of Kevin Bacon.”
- Milgram’s experiment in 1970.
- Recent work shows similarities between the structures of the Internet, the World Wide Web, human social networks, peer-to-peer overlays, the electric power grid, and protein networks.
- These networks have “evolved naturally.”
- Many of these are **small-world networks**.

### Meaning

The “six degrees” idea suggests that people in a large social network can often be connected by a surprisingly short chain of acquaintances. Milgram’s experiment is presented as historical motivation for studying short paths and network structure.

The key observation is that very different systems may share structural properties, such as short average path lengths, clusters of closely connected vertices, and a small number of long-range links. Such systems are commonly called small-world networks.

---

## Slide 7 - Paths and cycles

### Path

The slide defines a path `P_n`, for `n >= 3`, as consisting of `n` vertices

```text
v_1, v_2, v_3, ..., v_n
```

and edges

```text
{v_1, v_2}, {v_2, v_3}, {v_3, v_4}, ..., {v_{n-1}, v_n}
```

In a **simple path**, a vertex does not repeat.

### Cycle

The slide defines a cycle `C_n`, for `n >= 3`, as the path above plus the closing edge `{v_n, v_1}`:

```text
{v_1, v_2}, {v_2, v_3}, ..., {v_{n-1}, v_n}, {v_n, v_1}
```

A cycle is therefore a closed simple path: it returns to its starting vertex after visiting the other vertices without repetition.

### Walk

A **walk** is a sequence of vertices and edges in a graph. Unlike a simple path, edges and vertices may be repeated.

### Giant component

A **giant component** is a connected component containing at least `n/2` nodes, where `n` is the total number of vertices in the graph.

### Degree

The degree of a vertex `u`, written `deg(u)`, is the number of edges for which `u` is a terminal endpoint/vertex. For an undirected graph, this is the number of edges incident to `u`.

---

## Slide 8 - Map as a network example

This slide contains a large campus-style map with many labeled locations, roads, walkways, parking areas, buildings, and paths. It is an image-only example illustrating that a physical map can be interpreted as a graph.

### Graph interpretation of the map

- A **vertex** could represent a building, intersection, campus location, or destination.
- An **edge** could represent a road, walkway, path, or other traversable connection between two locations.
- The map contains many possible vertices and edges, making it a much larger network than the small diagrams used in the other slides.
- Depending on the application, edges could be undirected if movement is possible in both directions, or directed if a road/path is one-way.

The exact map labels are not necessary for the graph-theory concept; the important point is that a real geographic environment can be converted into a network model.

---

## Slide 9 - Components

### Slide text

- **Connected component:** There is a path connecting every two nodes of the component.
- **Connected graph:** Consists of a single connected component.

### Diagram description

The graph has three separate components:

1. A two-vertex component containing `A` and `B`, connected by edge `{A, B}`.
2. A larger component containing `F, G, H, I, J, K, L, M`.
3. A three-vertex component containing `C, D, E`, with edges `{C, D}`, `{C, E}`, and `{D, E}`.

Because there is no path from one displayed component to another, the entire graph is disconnected. Each component individually is connected.

### Edge list for the middle component

```text
{F, H}, {F, G}, {H, I}, {H, J}, {G, J}, {G, M},
{I, K}, {J, K}, {J, L}, {K, L}, {L, M}
```

---

## Slide 10 - Breadth-first search

> The slide title says “BREATH-FIRST SEARCH”; the standard term is **BREADTH-FIRST SEARCH**, abbreviated BFS.

### Slide text

- **Distance between `u` and `v`:** the length of the shortest path connecting `u` and `v`.
- **Breadth-First Search from `u`:** the shortest path from `u` to all nodes.
  1. All actual neighbors of `u` are at distance 1.
  2. Then all neighbors of all the neighbors at distance 1.
  3. Then all neighbors of all the neighbors at distance 2.
  4. Continue this process.
- BFS can organize the structure according to distances.

### Meaning

BFS explores a graph in layers. Starting at a source vertex `u`:

- layer 0 contains `u`;
- layer 1 contains vertices one edge away;
- layer 2 contains previously unseen vertices two edges away;
- layer 3 contains previously unseen vertices three edges away;
- and so on.

For an unweighted graph, the first time BFS discovers a vertex, it has found a shortest path to that vertex.

---

## Slides 11-20 - BFS from A

These slides animate BFS on the same graph. The colors indicate the current BFS frontier/layers:

- **red**: the source or the newly highlighted layer in the current animation state;
- **blue**: previously reached/processed layers or the current contrasting layer;
- **light gray**: not yet highlighted in that frame.

The underlying graph has vertices

```text
A, B, C, D, E, F, G, H, I, J, K, L, M
```

and edges

```text
{A, B}, {A, F},
{B, I},
{F, H}, {F, G}, {F, C},
{H, I},
{G, M},
{C, D}, {C, E},
{D, E},
{E, M},
{I, K},
{K, J}, {K, L},
{J, L},
{L, M}
```

The important shortest-path distances from `A` are:

```text
distance 0: A
distance 1: B, F
distance 2: I, H, G, C
distance 3: K, M, D, E
distance 4: J, L
```

### Slide 11 - Initial graph with A as source

The complete graph is shown. Vertex `A` is colored red, identifying it as the BFS source. All other vertices are unhighlighted.

### Slide 12 - Distance 0

Only `A` is shown. This represents the starting BFS layer:

```text
L_0 = {A}
```

### Slide 13 - Distance 1

`A` remains red, and its immediate neighbors `B` and `F` are colored blue:

```text
L_1 = {B, F}
```

Both vertices are exactly one edge from `A`.

### Slide 14 - BFS tree/layer view after discovering B and F

The graph is displayed as a layered tree-like arrangement. The visible hierarchy is approximately:

```text
        A
      /   \
     B     F
```

This frame emphasizes that BFS begins by expanding the source and recording its immediate neighbors.

### Slide 15 - Distance 2

The next layer is highlighted red while the distance-1 layer remains blue:

```text
L_2 = {I, H, G, C}
```

These vertices are discovered from the distance-1 vertices:

- `I` is reached through `B` or `H`;
- `H` is reached through `F`;
- `G` is reached through `F`;
- `C` is reached through `F`.

### Slide 16 - BFS tree/layer view after discovering distance-2 vertices

The diagram is reorganized into a tree-like BFS layout. It shows the source and first two layers, with branches from `B` and `F` to the newly discovered vertices.

One valid shortest-path parent assignment is:

```text
A -> B
A -> F
B -> I
F -> H
F -> G
F -> C
```

The parent assignment is not necessarily unique when a vertex has multiple shortest paths. For example, `I` can be reached through `B` or `H`.

### Slide 17 - Distance 3

The distance-3 vertices are colored blue, while the distance-2 vertices are red:

```text
L_3 = {K, M, D, E}
```

They are reached as follows:

- `K` from `I`;
- `M` from `G`;
- `D` from `C`;
- `E` from `C` or `M`.

### Slide 18 - BFS tree/layer view after discovering distance-3 vertices

The graph is shown in a layered/tree-like arrangement with the newly reached vertices added below the distance-2 vertices. A representative parent assignment is:

```text
I -> K
G -> M
C -> D
C -> E
```

### Slide 19 - Distance 4

The final newly reached vertices are colored red, and the previous layer is blue:

```text
L_4 = {J, L}
```

They are reached from the distance-3 vertices:

- `J` from `K`;
- `L` from `K` or `M`.

### Slide 20 - Completed BFS tree/layer view

The graph is displayed in a complete layered arrangement. All vertices have now been reached from `A`.

The BFS distance summary is:

| BFS layer | Vertices | Distance from A |
|---|---|---:|
| `L_0` | `A` | 0 |
| `L_1` | `B, F` | 1 |
| `L_2` | `I, H, G, C` | 2 |
| `L_3` | `K, M, D, E` | 3 |
| `L_4` | `J, L` | 4 |

Therefore, the eccentricity of `A` in this graph is 4: the farthest vertices from `A` are `J` and `L`, at distance 4.

---

## Slide 21 - Check your understanding: BFS from L

The slide asks the viewer to perform **breadth-first search from `L`** on the same graph.

### Correct BFS distances from L

Using the edge list above:

```text
distance 0: L
distance 1: K, J, M
distance 2: I, H, G, E
distance 3: B, F, C, D
distance 4: A
```

### One valid parent structure

```text
L -> K
L -> J
L -> M
K -> I
M -> G
M -> E
I -> B
J -> H
H -> F
E -> C
E -> D
B -> A
```

Some parent choices can vary because there may be multiple shortest paths. The distances do not change.

### Layer table

| Layer | Vertices | Meaning |
|---|---|---|
| `L_0` | `L` | source |
| `L_1` | `K, J, M` | one edge from `L` |
| `L_2` | `I, H, G, E` | two edges from `L` |
| `L_3` | `B, F, C, D` | three edges from `L` |
| `L_4` | `A` | four edges from `L` |

---

## Slide 22 - Theorems: undirected graphs, Theorem 1

### The Handshaking Theorem

The slide states:

$$
2e = \sum_{v \in V} \deg(v)
$$

where `e` is the number of edges and `deg(v)` is the degree of vertex `v`.

### Explanation

Every undirected edge connects exactly two vertices. Therefore, when all vertex degrees are added, each edge is counted twice: once at each endpoint. The total degree is consequently `2e`.

### Example

If an undirected graph has 5 edges, then:

$$
\sum_{v \in V} \deg(v) = 2(5) = 10.
$$

The individual degrees can differ, but their sum must be even and must equal twice the number of edges.

---

## Slide 23 - Theorems: undirected graphs, Theorem 2

### Statement

An undirected graph has an **even number of vertices with odd degree**.

### Proof structure from the slide

Let:

- `V_1` be the set of even-degree vertices;
- `V_2` be the set of odd-degree vertices.

By the Handshaking Theorem:

$$
2e = \sum_{v \in V} \deg(v)
    = \sum_{u \in V_1} \deg(u) + \sum_{v \in V_2} \deg(v).
$$

The left side, `2e`, is even. Every term in

$$
\sum_{u \in V_1} \deg(u)
$$

is even, so that sum is even. Therefore, the remaining sum

$$
\sum_{v \in V_2} \deg(v)
$$

must also be even.

Every degree in `V_2` is odd. A sum of odd numbers is even only when there are an even number of odd terms. Thus, `|V_2|` must be even.

### Important conclusion

Odd-degree vertices always occur in pairs, even if the graph has many vertices and edges.

---

## Slide 24 - Erdos-Renyi graph

### Slide text

- `G_{n,p}`: a random graph with `n` vertices where each edge `{u, v} in E` exists independently with probability `p`.
- Does `G_{n,p}` have a giant component?

### Diagram description

The diagram shows five vertices labeled `a`, `b`, `c`, `d`, and `e`.

- Solid red edges represent edges that exist in the sampled graph.
- Dashed blue lines represent possible edges that are absent in this particular sample.
- Every potential pair of vertices is considered independently with probability `p`.

For five vertices, there are

$$
\binom{5}{2} = 10
$$

possible undirected edges. The random graph chooses each of those 10 edges independently.

### Meaning of the question

The lecture asks when the random graph is likely to contain a connected component containing at least half of all vertices. That is the giant-component question.

---

## Slide 25 - Erdos-Renyi theorem and claim

### Theorem (Erdos-Renyi, 1961)

Assuming

$$
p \geq \frac{\ln 64}{n},
$$

the random graph `G_{n,p}` has a giant component of size `X` with high probability; specifically,

$$
\Pr\left[X > \frac{n}{2}\right] \geq 1 - 2^{-n/8}.
$$

Here `X` denotes the size of the largest connected component.

### Claim used in the proof

If

$$
X \leq \frac{n}{2},
$$

then there exists a partition of the vertex set into two sets `A` and `B` such that:

$$
\frac{n}{4} \leq |A| \quad\text{and}\quad |B| \leq \frac{3n}{4},
$$

and there are **no edges between `A` and `B`**.

The proof bounds the probability of this undesirable separation and shows that it is very small.

---

## Slide 26 - Proof of the claim

Assume the connected-component sizes are

$$
n_1, n_2, \ldots, n_k
$$

in some order, not necessarily distinct. Since these components partition the `n` vertices:

$$
\sum_{i=1}^{k} n_i = n.
$$

If `X <= n/2`, then every component satisfies

$$
n_i \leq \frac{n}{2}.
$$

Because no individual component is larger than `n/2`, we can find an index `m < k` such that:

$$
\frac{n}{4} \leq \sum_{i=1}^{m} n_i \leq \frac{3n}{4}
$$

and simultaneously

$$
\frac{n}{4} \leq \sum_{i=m+1}^{k} n_i \leq \frac{3n}{4}.
$$

Now choose:

- `A` to be the union of the connected components with sizes `n_1, ..., n_m`;
- `B` to be the union of the remaining connected components.

Since `A` and `B` are made from separate connected components, there can be no edges between them. This proves the claim.

---

## Slide 27 - Bounding the probability of a good pair

The slide calls a pair `(A, B)` a **good pair** when:

- `A` and `B` have the required sizes;
- there are no edges between `A` and `B`.

### Number of possible pairs

The number of good pairs cannot exceed `2^n`, because there are at most `2^n` subsets of an `n`-vertex set.

### Probability calculation from the slide

The slide gives the following union-bound calculation:

$$
\Pr\left[X \leq \frac{n}{2}\right]
\leq 2^n \sup_{(A,B)\text{ is good}}
\Pr[\text{there are no edges between A and B}]
$$

If `|A| = m` and `|B| = n-m`, then there are `m(n-m)` possible edges crossing from `A` to `B`. Each edge is absent with probability `(1-p)`, so:

$$
\Pr[\text{no edges between A and B}] = (1-p)^{m(n-m)}.
$$

Therefore:

$$
\Pr\left[X \leq \frac{n}{2}\right]
\leq
2^n \sup_{n/4 \leq m \leq 3n/4}(1-p)^{m(n-m)}.
$$

Because `m` lies between `n/4` and `3n/4`, the product `m(n-m)` is bounded below by:

$$
m(n-m) \geq \frac{3n^2}{16}.
$$

Using this lower bound in the exponent gives:

$$
\Pr\left[X \leq \frac{n}{2}\right]
\leq
2^n(1-p)^{3n^2/16}.
$$

### Substitute the hypothesis for `p`

The hypothesis is

$$
p \geq \frac{\ln 64}{n}.
$$

Replacing `p` by this lower bound gives the slide's next line:

$$
2^n\left(1-\frac{\ln 64}{n}\right)^{3n^2/16}.
$$

Using the standard approximation `(1-x)^r <= e^{-xr}` for the relevant range:

$$
2^n\left(e^{-\ln 64}\right)^{3n/16}
= 2^n(2^{-6})^{3n/16}.
$$

Since

$$
(2^{-6})^{3n/16} = 2^{-18n/16} = 2^{-9n/8},
$$

we obtain:

$$
2^n(2^{-9n/8}) = 2^{-n/8}.
$$

Thus:

$$
\Pr\left[X \leq \frac{n}{2}\right] \leq 2^{-n/8}.
$$

Equivalently:

$$
\Pr\left[X > \frac{n}{2}\right] \geq 1 - 2^{-n/8}.
$$

This is the high-probability giant-component result stated on Slide 25.

---

## Slide 28 - Erdos-Renyi connectivity threshold

### Theorem

Let

$$
p = c\frac{\ln n}{n},
$$

where `c > 0` is a constant. Then:

$$
\lim_{n\to\infty} \Pr[G_{n,p}\text{ is connected}]
=
\begin{cases}
1, & c > 1,\\
0, & c < 1.
\end{cases}
$$

### Interpretation

There is a sharp asymptotic threshold near

$$
p = \frac{\ln n}{n}.
$$

- If `c > 1`, the probability that the graph is connected approaches 1 as `n` grows.
- If `c < 1`, the probability that the graph is connected approaches 0 as `n` grows.
- The theorem concerns full connectivity, which is stronger than merely having a giant component.

### Homework instruction on the slide

Calculate `p` according to:

$$
p = c\frac{\ln n}{n}.
$$

---

# Consolidated reference sheet

## Core definitions

| Concept | Meaning |
|---|---|
| Graph | `G = (V, E)`, a set of vertices and edges |
| Vertex/node | An object/entity in the network |
| Edge/link/arc | A relationship or connection between vertices |
| Directed edge | Ordered pair `(u, v)`; direction matters |
| Undirected edge | Unordered pair `{u, v}`; endpoints are interchangeable |
| Path | Sequence of vertices connected by edges, normally without repetition for a simple path |
| Cycle | Closed simple path with an edge from the last vertex back to the first |
| Walk | Vertex-edge sequence where repetition is allowed |
| Degree | Number of incident edges at a vertex in an undirected graph |
| Connected component | Maximal set in which every two vertices have a connecting path |
| Connected graph | Graph with exactly one connected component |
| Giant component | Component containing at least `n/2` vertices |
| Distance | Length of the shortest path between two vertices |

## BFS procedure

1. Select a source vertex.
2. Put the source in layer 0.
3. Visit all undiscovered neighbors of the source and put them in layer 1.
4. Visit undiscovered neighbors of layer-1 vertices and put them in layer 2.
5. Continue layer by layer until all reachable vertices are discovered.
6. The layer number is the shortest-path distance from the source in an unweighted graph.

## Important formulas

### Handshaking theorem

$$
2|E| = \sum_{v \in V}\deg(v)
$$

### Odd-degree theorem

The number of odd-degree vertices in an undirected graph is even.

### Erdos-Renyi random graph

$$
G_{n,p}:\quad n\text{ vertices, each possible edge present independently with probability }p.
$$

### Giant-component result used in the deck

If

$$
p \geq \frac{\ln 64}{n},
$$

then

$$
\Pr\left[X > \frac{n}{2}\right] \geq 1 - 2^{-n/8}.
$$

### Connectivity threshold

For

$$
p = c\frac{\ln n}{n},
$$

the probability of connectivity approaches 1 when `c > 1` and approaches 0 when `c < 1`.

## Common distinctions to remember

- A **walk** may repeat vertices and edges; a **simple path** does not repeat vertices.
- A **cycle** is closed; a path does not need to return to its start.
- A **connected component** can exist inside a disconnected graph.
- A **connected graph** has only one connected component.
- A **giant component** is large, but the graph can still have smaller disconnected components.
- A **giant component** is not the same as full connectivity.
- In an undirected graph, `{u, v}` and `{v, u}` represent the same edge.
- In a directed graph, `(u, v)` and `(v, u)` are different unless both directed edges exist.
- BFS gives shortest-path distances in an unweighted graph because it processes vertices in nondecreasing distance order.
