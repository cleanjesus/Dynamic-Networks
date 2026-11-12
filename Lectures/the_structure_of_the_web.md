# The Structure of the Web
**Course:** CECS 427 Dynamic Networks

---

## Slide 1: Title Slide
* **Title:** The Structure of the Web
* **Course:** CECS 427 Dynamic Networks

---

## Slide 2: Retrieving Useful Information
* Retrieving useful information is extremely important across many domains:
  * Precedents in the court
  * Scientific results
  * Finding previous patents
  * Everyday life

---

## Slide 3: Information Networks
* **Nodes:** Pieces of information (e.g., web pages, documents, articles).
* **Links:** Join pieces of information (e.g., hyperlinks, citations, cross-references).
* **WWW (World Wide Web):** Is the largest information network.
  * The web lets users share info.
  * It organizes the info using a network metaphor.

---

## Slides 4–7: Web Pages (Incremental Directed Graph Build)
* *(Slides 4, 5, 6, and 7 progressively build a directed graph of 5 web pages starting from the `CECS 427` course page).*
* **Complete Graph Topology (Slide 7):**
  * **Nodes (5 Web Pages shown as rounded rectangles):**
    1. `CECS 427`
    2. `Wiki "Social Network"`
    3. `Wiki: "Random Graph"`
    4. `Wiki "Network Theory"`
    5. `Wiki "Computer Science"`
  * **Directed Edges (Hyperlinks):**
    * `CECS 427` $\rightarrow$ `Wiki "Social Network"`
    * `CECS 427` $\rightarrow$ `Wiki: "Random Graph"`
    * `CECS 427` $\rightarrow$ `Wiki "Network Theory"`
    * `CECS 427` $\rightarrow$ `Wiki "Computer Science"`
    * `Wiki "Social Network"` $\rightarrow$ `Wiki: "Random Graph"`
    * `Wiki "Social Network"` $\rightarrow$ `Wiki "Network Theory"`
    * `Wiki: "Random Graph"` $\rightarrow$ `Wiki "Network Theory"`
    * `Wiki "Network Theory"` $\rightarrow$ `Wiki "Computer Science"`

---

## Slides 8–9: Intellectual Precursors of Hypertext (Scholarly Citations)
* **Concept:** The concept of citation among scholarly books and articles.
* **Graph Structure:** A citation structure naturally forms a **directed graph** (specifically, an acyclic directed graph / DAG moving backward in time), with nodes representing books and articles, and directed edges representing citations from one work to another.
* **Visual Diagram (Slide 9):**
  * Node 1 (Paper B): `"Patrolling a Path Connecting a Set of Points with Unbalanced Frequencies of Visits"`
  * Node 2 (Paper A): `"Visiting Infinitely Often the Unit Interval While Minimizing the Idle Time of High Priority Segments"`
  * **Directed Edge:** Paper B $\rightarrow$ cites Paper A.

---

## Slide 10: Intellectual Precursors of Hypertext (Other Domains)
* A similar directed network structure arises among:
  * **Patents:** Which provide citations to prior work and earlier inventions.
  * **Legal Decisions:** Which provide citations to earlier decisions that are being used as precedents, or are being distinguished from the present case.
  * **Encyclopedias:** Cross-references within a printed encyclopedia or similar reference work.

---

## Slide 11: Wikipedia Articles on Topics in Game Theory, With Connections
* **Visual Diagram Description:** A directed graph of **9 Wikipedia articles** (ovals) showing how topical clusters (Game Theory vs. Film/Space) bridge together via biographical and institutional nodes.
* **Nodes (9):**
  1. `Nash Equilibrium`
  2. `Game Theory`
  3. `John Forbes Nash`
  4. `RAND`
  5. `A Beautiful Mind (film)`
  6. `Apollo 13 (film)`
  7. `Ron Howard`
  8. `Conspiracy Theories`
  9. `NASA`
* **Exact Directed Edges:**
  * `Nash Equilibrium` $\leftrightarrow$ `Game Theory` (bidirectional: links both ways)
  * `Nash Equilibrium` $\leftrightarrow$ `John Forbes Nash` (bidirectional)
  * `Game Theory` $\leftrightarrow$ `John Forbes Nash` (bidirectional)
  * `John Forbes Nash` $\leftrightarrow$ `RAND` (bidirectional)
  * `John Forbes Nash` $\leftrightarrow$ `A Beautiful Mind (film)` (bidirectional)
  * `A Beautiful Mind (film)` $\rightarrow$ `Nash Equilibrium` (unidirectional)
  * `A Beautiful Mind (film)` $\rightarrow$ `Game Theory` (unidirectional)
  * `A Beautiful Mind (film)` $\leftrightarrow$ `Ron Howard` (bidirectional)
  * `Apollo 13 (film)` $\rightarrow$ `A Beautiful Mind (film)` (unidirectional)
  * `Apollo 13 (film)` $\leftrightarrow$ `Ron Howard` (bidirectional)
  * `Apollo 13 (film)` $\leftrightarrow$ `NASA` (bidirectional)
  * `RAND` $\rightarrow$ `Conspiracy Theories` (unidirectional)
  * `Conspiracy Theories` $\rightarrow$ `NASA` (unidirectional)

---

## Slide 12: Graph Structure in the Web (Broder et al. Study)
* **Study Overview:** Broder et al. (2000) report on experiments on local and global properties of the web graph using two **AltaVista** crawls, each with over **200 Million pages** and **1.5 Billion links**.
* **Key Finding:** Their pioneering study indicates that the macroscopic structure of the web is considerably more intricate than suggested by earlier experiments on a smaller scale.

---

## Slide 13: Degree Sequences and Power Laws
* **Empirical Observation:** Their first experiment verified earlier observations that the in- and out-degree distributions on the web are distributed according to **power laws**.
* **Power Law Distribution Formula:**
  $$y = x^{-\alpha}$$
* **Log-Log Linearization (How to Plot):**
  * Take the logarithm of both sides:
    $$\log(y) = \log(x^{-\alpha}) = -\alpha \log(x)$$
  * Rename $\log(y)$ as $Y$ and $\log(x)$ as $X$:
    $$Y = -\alpha X$$
    *(Produces a straight line with slope $-\alpha$ on a log-log plot).*
* **Validation:** Experiment ran on both the May and October crawls of the web.

---

## Slide 14: In-Degree Distribution Plot
* **Plot Title:** `In-degree (total, remote-only) distr.`
* **Axes (Log-Log Scale):**
  * **X-axis:** `in-degree` (ranging from $1$ to $>100,000$)
  * **Y-axis:** `number of pages` (ranging from $1$ to $1\text{e+}10$)
* **Series Plotted & Power Law Exponents:**
  1. **Total in-degree** (red squares): Fitted with **Power law, exponent $\alpha = 2.09$**.
  2. **Remote-only in-degree** (blue crosses, counting only links from different host domains): Fitted with **Power law, exponent $\alpha = 2.1$**.

---

## Slide 15: Out-Degree Distribution Plot
* **Plot Title:** `Out-degree (total, remote-only) distr.`
* **Axes (Log-Log Scale):**
  * **X-axis:** `out-degree` (ranging from $1$ to $>1,000$)
  * **Y-axis:** `number of pages` (ranging from $1$ to $1\text{e+}10$)
* **Series Plotted & Power Law Exponents:**
  1. **Total out-degree** (red squares): Fitted with **Power law, exponent $\alpha = 2.72$**.
  2. **Remote-only out-degree** (blue crosses): Fitted with **Power law, exponent $\alpha = 2.67$**.

---

## Slide 16: The Bow-Tie Structure of the Web
* **Visual Diagram Description:** The famous Broder et al. macroscopic "Bow-Tie" diagram of the Web graph, partitioning the ~200 million pages of the crawl into distinct topological regions based on directed reachability relative to the central core:

```
          [Tendrils]                              [Tendrils]
             ^                                        |
             |                                        v
   +-------------------+   +-----------+   +-------------------+
   |        IN         |   |    SCC    |   |        OUT        |
   | 44 Million nodes  |-->| 56M nodes |-->| 44 Million nodes  |
   +-------------------+   +-----------+   +-------------------+
      |         |    \                       ^          ^
      v         v     \_______[Tubes]_______/           |
  [Tendrils] [Tendrils]                             [Tendrils]

                                    ( ) ( )
                                    ( ) ( ) <-- [Disconnected components]
```

* **Detailed Component Breakdown:**
  1. **SCC (Strongly Connected Component - Central Knot of the Bow-Tie):**
     * **Size:** **56 Million nodes** (~28% of the web).
     * **Property:** Every page in the SCC can reach every other page in the SCC via a directed path of hyperlinks.
  2. **IN (Left Wing of the Bow-Tie):**
     * **Size:** **44 Million nodes** (~21% of the web).
     * **Property:** Pages that can reach the **SCC** via directed paths, but **cannot be reached from** the SCC (e.g., new web pages that link to popular sites in the core, but haven't been linked back to yet).
  3. **OUT (Right Wing of the Bow-Tie):**
     * **Size:** **44 Million nodes** (~21% of the web).
     * **Property:** Pages that **can be reached from** the **SCC** via directed paths, but **cannot reach back into** the SCC (e.g., corporate websites, PDF repositories, or dead-end informational pages that only contain internal links or no out-links).
  4. **Tendrils:**
     * **Size:** **44 Million nodes** (~21% of the web, combined with Tubes).
     * **Property:** Pages that cannot reach the SCC and cannot be reached from the SCC, but are attached to **IN** or **OUT**:
       * *Tendrils hanging off IN:* Can be reached by directed paths from **IN**, but cannot reach the SCC.
       * *Tendrils leading into OUT:* Can reach **OUT** via directed paths, but cannot be reached from the SCC.
  5. **Tubes:**
     * **Property:** Directed paths that pass directly from **IN** to **OUT** (via tendrils) **without** passing through the central **SCC**.
  6. **Disconnected Components:**
     * **Size:** Remaining ~16–17 Million nodes (~8–9% of the web).
     * **Property:** Isolated islands of pages that have no directed or undirected connections to the main bow-tie structure at all (even if link directions are ignored).