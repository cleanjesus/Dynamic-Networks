# Link Analysis and Web Search
**Course:** CECS 427 Dynamic Networks

---

## Slide 1: Title Slide
* **Title:** Link Analysis and Web Search
* **Course:** CECS 427 Dynamic Networks

---

## Slide 2: Hidden Information
* **Question:** How does Google know about a given word?
* **Mechanism:** It uses intrinsic info to the web and its structure.
* **Context:** 
  * Finding information is a key problem in computer science.
  * Automated information retrieval systems started in the 1960s (newspapers, scientific papers, patents, legal information).

---

## Slide 3: Issues in Finding (Keywords)
* **Synonymy:** Multiple ways to say the same thing, so that your search for recipes involving *scallions* fails because the recipe you wanted called them *"green onions"*.
* **Polysemy:** Multiple meanings for the same term, so that your search for information about the animal called a *jaguar* instead produces results primarily about automobiles, football players (Jacksonville Jaguars), and an operating system for the Apple Macintosh (Mac OS X Jaguar).

---

## Slide 4: Web Graphs
* **Insights:** The study of the web as a graph yields valuable insight into web algorithms for:
  * Crawling
  * Searching
  * Discovery
* **Sociological Impact:** It also provides insight into the sociological phenomena which characterize its evolution.

---

## Slide 5: The Basic Question (Voting by In-Links)
* **Query Example:** When someone poses the query `"CSULB"`, what are the clues suggesting that CSULB's home page is `"www.csulb.edu"`?
* **Voting by In-Links Procedure:**
  1. **Collect Sample:** Collect a large sample of pages relevant to the query (e.g., as determined by a classical, text-only, information retrieval approach).
  2. **Vote via Links:** Let pages in this sample "vote" through their links: Which page on the Web receives the greatest number of in-links from pages that are relevant to CSULB?

---

## Slide 6: The Basic Question (The General Popularity Problem)
* **Query Example:** What happens if we try to find the best grocery store in Long Beach? We can ask students for the keyword `"grocery stores"`.
* **Result:** You get high scores for:
  * Prominent grocery stores (results you'd want), AND
  * Stores/chains that are going to receive a lot of in-links no matter what the query is: **7-Eleven**, **CVS**, and others.

---

## Slide 7: Counting In-Links (Base Bipartite Graph)
* **Visual Diagram Description:** A directed bipartite graph representing **10 unnamed student/voter nodes** (circles) pointing to **7 store nodes** (ovals).
* **Node Inventory & Exact Topological Connections:**
  * **Left/Bottom Cluster of Voter Nodes (5 circles) pointing to Convenience/Pharmacy Stores:**
    * `Student_L1` (far left) $\rightarrow$ points to **7-Eleven**
    * `Student_L2` (upper middle-left) $\rightarrow$ points to **7-Eleven**, **CVS**
    * `Student_L3` (lower middle-left) $\rightarrow$ points to **7-Eleven**
    * `Student_L4` (middle) $\rightarrow$ points to **CVS**
  * **Vertical Column of Voter Nodes (5 circles, top to bottom) pointing to Grocery Stores:**
    * `Student_R1` (top) $\rightarrow$ points to **Vons**, **Whole Foods**, **Ralphs**
    * `Student_R2` (2nd from top) $\rightarrow$ points to **Vons**, **Whole Foods**, **Ralphs**, **Trader Joe**
    * `Student_R3` (3rd from top) $\rightarrow$ points to **Ralphs**, **Trader Joe**
    * `Student_R4` (4th from top) $\rightarrow$ points to **Ralphs**, **Grocery Outlet**
    * `Student_R5` (bottom of column) $\rightarrow$ points to **CVS**, **Trader Joe**
* **Target Store Nodes (7 ovals):**
  * Bottom-Left: **7-Eleven**, **CVS**
  * Right Column (top to bottom): **Vons**, **Whole Foods**, **Ralphs**, **Trader Joe**, **Grocery Outlet**

---

## Slide 8: Counting In-Links (Highlighting Vons)
* **Visual Update:** The two incoming edges to **Vons** (from `Student_R1` and `Student_R2`) are highlighted in red.
* **Vote Tally Shown:**
  * **Vons:** `2 votes`

---

## Slide 9: Counting In-Links (Highlighting Whole Foods)
* **Visual Update:** The two incoming edges to **Whole Foods** (from `Student_R1` and `Student_R2`) are highlighted in red.
* **Vote Tally Shown:**
  * **Vons:** `2 votes`
  * **Whole Foods:** `2 votes`

---

## Slide 10: Counting In-Links (All Initial In-Link Votes)
* **Visual Update:** All store nodes now display their total in-degree (number of incoming links).
* **Initial Authority Scores (Step 1 Authority Update where all initial Hub scores = 1):**

| Store Node | Incoming Links From | Total In-Link Votes |
| :--- | :--- | :---: |
| **Vons** | `Student_R1`, `Student_R2` | **2 votes** |
| **Whole Foods** | `Student_R1`, `Student_R2` | **2 votes** |
| **Ralphs** | `Student_R1`, `Student_R2`, `Student_R3`, `Student_R4` | **4 votes** |
| **Trader Joe** | `Student_R2`, `Student_R3`, `Student_R5` | **3 votes** |
| **Grocery Outlet** | `Student_R4` | **1 vote** |
| **7-Eleven** | `Student_L1`, `Student_L2`, `Student_L3` | **3 votes** |
| **CVS** | `Student_L2`, `Student_L4`, `Student_R5` | **3 votes** |

* **Observation:** Notice that **7-Eleven** (3 votes) and **CVS** (3 votes) tie with **Trader Joe** (3 votes) and beat **Vons** (2 votes) and **Whole Foods** (2 votes) under simple in-link counting.

---

## Slide 11: A Student's Value (Hubs)
* **Concept of Lists (Hubs):** In addition to the grocery stores themselves (Authorities), there is another useful answer to our query: students that compile lists of resources relevant to the topic (Hubs).
* **Intuition:** Among the students casting votes, a few of them voted for many of the grocery stores that received a lot of votes. It would be natural, therefore, to suspect that these students have some sense of where the good groceries are, and to score them highly as lists.
* **Calculation Rule:** Concretely, we could say that a student's value as a list is equal to the **sum of the votes of each grocery store** that the student voted for.

---

## Slide 12: Student Value (Step 1 Hub Scores)
* **Visual Update:** Each circular student node is now labeled with its calculated Hub score (sum of the vote counts of the stores it points to).

| Student Node | Stores Pointed To (with Store Votes) | Calculated Student Value (Hub Score) |
| :--- | :--- | :---: |
| `Student_R1` (top of column) | Vons (2) + Whole Foods (2) + Ralphs (4) | **8** |
| `Student_R2` (2nd in column) | Vons (2) + Whole Foods (2) + Ralphs (4) + Trader Joe (3) | **11** |
| `Student_R3` (3rd in column) | Ralphs (4) + Trader Joe (3) | **7** |
| `Student_R4` (4th in column) | Ralphs (4) + Grocery Outlet (1) | **5** |
| `Student_R5` (bottom of column) | CVS (3) + Trader Joe (3) | **6** |
| `Student_L1` (far left) | 7-Eleven (3) | **3** |
| `Student_L2` (upper middle-left) | 7-Eleven (3) + CVS (3) | **6** |
| `Student_L3` (lower middle-left) | 7-Eleven (3) | **3** |
| `Student_L4` (middle) | CVS (3) | **3** |

---

## Slide 13: Principle of Repeated Improvement
* **Iterative Refinement:**
  * If we have better votes on the grocery stores of the figure, we can use these to get still more refined values for the quality of the lists on the students.
  * And with more refined estimates for the high-value lists, we can re-weight the votes that we apply to the grocery stores once again.
* **Definition:** The process can go back and forth forever, and it can be viewed as a **Principle of Repeated Improvement**, whereby each refinement to one side of the figure enables a further refinement to the other.

---

## Slide 14: Hub/Authority Rule (Initialization)
* **Dual Scores:** For each page $p$, we're trying to estimate its value as:
  * A potential **authority**, and
  * A potential **hub**.
* **Initialization:** We assign it two numerical scores: $\text{auth}(p)$ and $\text{hub}(p)$. Each of these starts out with a value of $1$.

---

## Slide 15: Voting (Update Rules)
1. **Authority Update Rule:** For each page $p$, update $\text{auth}(p)$ to be the sum of the hub scores of all pages that point to it.
2. **Hub Update Rule:** For each page $p$, update $\text{hub}(p)$ to be the sum of the authority scores of all pages that it points to.

---

## Slide 16: Hub/Authority Rule (Iterative Process)
* We perform a sequence of $k$ hub-authority updates.
* Each update works as follows:
  1. Apply **Authority Update Rule** to the current set of scores.
  2. Apply **Hub Update Rule** to the resulting set of scores.

---

## Slide 17: Grocery Store's Votes (Re-weighting Vons)
* **Visual Update:** The two incoming edges to **Vons** from `Student_R1` (score 8) and `Student_R2` (score 11) are highlighted in red.
* **Updated Authority Score for Vons:** $8 + 11 = \mathbf{19\text{ votes}}$.

---

## Slide 18: Grocery Store's Votes (All Step 2 Unnormalized Authority Scores)
* **Visual Update:** All store nodes are updated by summing the Hub scores of the students pointing to them:

| Store Node | Sum of Incoming Student Hub Scores | Step 2 Authority Score (Unnormalized) |
| :--- | :--- | :---: |
| **Vons** | $8 + 11$ | **19 votes** |
| **Whole Foods** | $8 + 11$ | **19 votes** |
| **Ralphs** | $8 + 11 + 7 + 5$ | **31 votes** |
| **Trader Joe** | $11 + 7 + 6$ | **24 votes** |
| **Grocery Outlet** | $5$ | **5 votes** |
| **7-Eleven** | $3 + 6 + 3$ | **12 votes** |
| **CVS** | $6 + 3 + 6$ | **15 votes** |

* **Observation:** Now **Vons** (19) and **Whole Foods** (19) have decisively overtaken **7-Eleven** (12) and **CVS** (15)!

---

## Slide 19: Normalizing the Scores (Fractions)
* **Total Sum of Authority Scores:**
  $$12 + 15 + 5 + 24 + 31 + 19 + 19 = 125$$
* **Normalized Fractional Authority Scores:**
  * **Vons:** $19 / 125$
  * **Whole Foods:** $19 / 125$
  * **Ralphs:** $31 / 125$
  * **Trader Joe:** $24 / 125$
  * **Grocery Outlet:** $5 / 125$
  * **7-Eleven:** $12 / 125$
  * **CVS:** $15 / 125$

---

## Slide 20: Normalizing the Scores (Decimals)
* **Normalized Decimal Authority Scores (after 2 Authority updates):**
  * **Vons:** $0.152$
  * **Whole Foods:** $0.152$
  * **Ralphs:** $0.248$
  * **Trader Joe:** $0.192$
  * **Grocery Outlet:** $0.04$
  * **7-Eleven:** $0.096$
  * **CVS:** $0.12$

---

## Slide 21: Limit When $k$ Goes to Infinity
* **Visual Diagram:** Shows the converged, normalized Hub scores (on the student nodes) and Authority scores (on the store nodes) as $k \to \infty$:

| Store Node (Authorities) | Limiting Authority Score | Student Node (Hubs) | Limiting Hub Score |
| :--- | :---: | :--- | :---: |
| **Ralphs** | **0.304** | `Student_R2` (points to Vons, WF, Ralphs, TJ) | **0.321** |
| **Trader Joe** | **0.205** | `Student_R1` (points to Vons, WF, Ralphs) | **0.249** |
| **Vons** | **0.199** | `Student_R3` (points to Ralphs, TJ) | **0.181** |
| **Whole Foods** | **0.199** | `Student_R4` (points to Ralphs, GO) | **0.123** |
| **Grocery Outlet** | **0.043** | `Student_R5` (points to CVS, TJ) | **0.088** |
| **CVS** | **0.042** | `Student_L2` (points to 7-Eleven, CVS) | **0.018** |
| **7-Eleven** | **0.008** | `Student_L4` (points to CVS) | **0.015** |
| — | — | `Student_L1` (points to 7-Eleven) | **0.003** |
| — | — | `Student_L3` (points to 7-Eleven) | **0.003** |

---

## Slide 22: Authority and Hub Update Rules (Mathematical Notation)
* **Authority Update Rule:**
  $$\text{auth}(p) = \sum_{q \in N^-(p)} \text{hub}(q)$$
  *(where $N^-(p)$ is the set of nodes with directed edges pointing into $p$).*
* **Hub Update Rule:**
  $$\text{hub}(q) = \sum_{p \in N^+(q)} \text{auth}(p)$$
  *(Note: Slide has a typo on the right-hand side written as $\text{auth}(q)$; it means $\text{auth}(p)$ for each $p \in N^+(q)$, the out-neighbors of $q$).*

---

## Slide 23: HITS Algorithm Pseudocode
* Let $\text{auth}(p) = 1$ for all $p$
* Let $\text{hub}(q) = 1$ for all $q$
* Let $k > 0$ be the number of steps
* **For** $k$ steps **do**:
  * Authority update rule for all $p$
  * Hub update rule for all $q$
* Normalize the authorities (and hubs)

---

## Slide 24: Test Your Knowledge (HITS Exercise)
* **Prompt:** Determine the hub scores after 2 iterations.
* **Visual Graph Topology:**
  * A bipartite graph with **4 Hub nodes on the left** (let's label them top-to-bottom as $r_1, r_2, r_3, r_4$, where the top node is explicitly labeled `r`) and **5 Authority nodes on the right** ($X, Y, Z, W, T$).
  * **Directed Edges:**
    * $r_1$ (`r`, top) $\rightarrow$ points to $X, Y, W$
    * $r_2$ (2nd from top) $\rightarrow$ points to $Y, Z$
    * $r_3$ (3rd from top) $\rightarrow$ points to $W$
    * $r_4$ (bottom) $\rightarrow$ points to $Z, T$
* **Step-by-Step Worked Solution (for Cursor AI Context):**
  * **Initialization ($k=0$):** All $\text{hub} = 1$, all $\text{auth} = 1$.
  * **Iteration 1:**
    * *Authority Update 1 (in-degrees):*
      * $\text{auth}(X) = \text{hub}(r_1) = 1$
      * $\text{auth}(Y) = \text{hub}(r_1) + \text{hub}(r_2) = 2$
      * $\text{auth}(Z) = \text{hub}(r_2) + \text{hub}(r_4) = 2$
      * $\text{auth}(W) = \text{hub}(r_1) + \text{hub}(r_3) = 2$
      * $\text{auth}(T) = \text{hub}(r_4) = 1$
    * *Hub Update 1 (sum of connected authorities):*
      * $\text{hub}(r_1) = \text{auth}(X) + \text{auth}(Y) + \text{auth}(W) = 1 + 2 + 2 = 5$
      * $\text{hub}(r_2) = \text{auth}(Y) + \text{auth}(Z) = 2 + 2 = 4$
      * $\text{hub}(r_3) = \text{auth}(W) = 2$
      * $\text{hub}(r_4) = \text{auth}(Z) + \text{auth}(T) = 2 + 1 = 3$
  * **Iteration 2:**
    * *Authority Update 2:*
      * $\text{auth}(X) = \text{hub}(r_1) = 5$
      * $\text{auth}(Y) = \text{hub}(r_1) + \text{hub}(r_2) = 5 + 4 = 9$
      * $\text{auth}(Z) = \text{hub}(r_2) + \text{hub}(r_4) = 4 + 3 = 7$
      * $\text{auth}(W) = \text{hub}(r_1) + \text{hub}(r_3) = 5 + 2 = 7$
      * $\text{auth}(T) = \text{hub}(r_4) = 3$
    * *Hub Update 2:*
      * $\text{hub}(r_1) = \text{auth}(X) + \text{auth}(Y) + \text{auth}(W) = 5 + 9 + 7 = \mathbf{21}$
      * $\text{hub}(r_2) = \text{auth}(Y) + \text{auth}(Z) = 9 + 7 = \mathbf{16}$
      * $\text{hub}(r_3) = \text{auth}(W) = \mathbf{7}$
      * $\text{hub}(r_4) = \text{auth}(Z) + \text{auth}(T) = 7 + 3 = \mathbf{10}$

---

## Slide 25: Spectral Analysis of Hubs and Authorities
* **Visual Diagram:** A 4-node directed graph used to demonstrate matrix representation:
  * **Nodes:** `Node 1`, `Node 2`, `Node 3`, `Node 4`
  * **Directed Edges:**
    * `Node 1` $\rightarrow$ `Node 2`, `Node 4`
    * `Node 2` $\rightarrow$ `Node 3`, `Node 4`
    * `Node 3` $\rightarrow$ `Node 1`
    * `Node 4` $\rightarrow$ `Node 3`

---

## Slide 26: Adjacency Matrix
* **Graph:** Same 4-node directed graph from Slide 25.
* **Adjacency Matrix $M$:** Where $M_{ij} = 1$ if Node $i$ points to Node $j$, and $0$ otherwise:
  $$M = \begin{bmatrix} 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{bmatrix}$$

---

## Slide 27: Hub/Authority Vectors
* **Matrix-Vector Example:** Given an example authority vector $a = \begin{bmatrix} 2 \\ 6 \\ 4 \\ 3 \end{bmatrix}$, multiplying by $M$ gives the updated hub vector $h$:
  $$\begin{bmatrix} 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{bmatrix} \begin{bmatrix} 2 \\ 6 \\ 4 \\ 3 \end{bmatrix} = \begin{bmatrix} 9 \\ 7 \\ 2 \\ 4 \end{bmatrix}$$
  *(where top-left matrix is labeled `M`, middle vector is labeled `auth`, and right result vector is labeled `hub`).*
* **Linear Algebra Update Rules:**
  * **Hub Update Rule:**
    $$h_i = M_{i1}a_1 + M_{i2}a_2 + \dots + M_{in}a_n \iff h \leftarrow Ma$$
  * **Authority Update Rule:**
    $$a_i = M_{1i}h_1 + M_{2i}h_2 + \dots + M_{ni}h_n \iff a \leftarrow M^T h$$

---

## Slide 28: Recurrence
* **Initialization:** Start with initial vectors of authority/hub scores $a^{(0)}, h^{(0)}$, each of them equal to the vector all of whose coordinates are $1$.
* **State at Step $k$:** Let $a^{(k)}, h^{(k)}$ be vectors of authority/hub scores after $k$ applications of the Authority/Hub Update Rules.
* **Matrix Equations:** Observe that the update rules can be written as:
  $$h^{(k+1)} = M a^{(k+1)} \quad \text{and} \quad a^{(k+1)} = M^T h^{(k)}$$
* **Unrolling the Recurrence:**
  $$h^{(k+1)} = M a^{(k+1)} = M M^T h^{(k)} = \dots = (M M^T)^{k+1} h^{(0)}$$
  $$a^{(k+1)} = M^T h^{(k)} = M^T (M M^T)^k h^{(0)} = (M^T M)^k M^T h^{(0)}$$
* **Convergence Expectation:** We expect that $h^{(*)}$ converges, therefore $(M M^T) h^{(*)} = c h^{(*)}$, where $h^{(*)}$ is the **eigenvector** and $c$ is the **eigenvalue**.

---

## Slide 29: Eigenvectors / Eigenvalues
* **Normalization Requirement:** For convergence in the limit to work, normalization must be taken into account.
* **Scaling Constants:** We will show that there are constants $c$ and $d$ so that the sequences:
  $$\frac{h^{(k)}}{c^k} = \frac{(M M^T)^k h^{(0)}}{c^k} \quad \text{and} \quad \frac{a^{(k)}}{d^k} = \frac{(M^T M)^{k-1} M^T h^{(0)}}{d^k}$$
  converge to limits as $k \to \infty$.
* **Definition:** In general, given a matrix $A$, a vector $v$ and a number $\lambda$ satisfying:
  $$Av = \lambda v$$
  are called an **eigenvector** and **eigenvalue**, respectively.

---

## Slide 30: Fact on Symmetric Matrices
* **Symmetry:** A matrix is called symmetric if $A^T = A$. E.g., both $M M^T$ and $M^T M$ are symmetric:
  $$(M M^T)^T = (M^T)^T M^T = M M^T$$
* **Spectral Theorem for Symmetric Matrices:** A symmetric $n \times n$ matrix $A$ has a set of $n$ unit, mutually orthogonal eigenvectors, forming a basis for the space $\mathbb{R}^n$ with corresponding non-negative real eigenvalues (since $M M^T$ is positive semi-definite).
* **Basis Expansion:** Let $z_1, z_2, \dots, z_n$ be $n$ such orthonormal eigenvectors and $c_1, c_2, \dots, c_n$ the corresponding eigenvalues of $M M^T$ ordered so that:
  $$c_1 \ge c_2 \ge \dots \ge c_n$$
* For any vector $x$, there exist constants $p_1, p_2, \dots, p_n$ such that $x = p_1 z_1 + p_2 z_2 + \dots + p_n z_n$. From this we conclude that:
  $$(M M^T)x = (M M^T)(p_1 z_1 + p_2 z_2 + \dots + p_n z_n)$$
  $$= p_1 (M M^T) z_1 + p_2 (M M^T) z_2 + \dots + p_n (M M^T) z_n$$
  $$= p_1 c_1 z_1 + p_2 c_2 z_2 + \dots + p_n c_n z_n$$

---

## Slide 31: Convergence Proof
* **Power Iteration:** Hence, after $k$ multiplications:
  $$(M M^T)^k x = p_1 c_1^k z_1 + p_2 c_2^k z_2 + \dots + p_n c_n^k z_n$$
* **Applying to $h^{(0)}$:** The starting vector $h^{(0)}$ with all coordinates $1$ can be written as $h^{(0)} = q_1 z_1 + q_2 z_2 + \dots + q_n z_n$, for some $q_1, q_2, \dots, q_n$. Therefore:
  $$h^{(k)} = (M M^T)^k h^{(0)} = q_1 c_1^k z_1 + q_2 c_2^k z_2 + \dots + q_n c_n^k z_n$$
* **Dividing by $c_1^k$:**
  $$\frac{h^{(k)}}{c_1^k} = q_1 z_1 + q_2 \left(\frac{c_2}{c_1}\right)^k z_2 + \dots + q_n \left(\frac{c_n}{c_1}\right)^k z_n$$
* **Limit:** Hence, $\lim_{k \to \infty} \frac{h^{(k)}}{c_1^k} = q_1 z_1$, provided $c_1 > c_2$ (and $q_1 \neq 0$).

---

## Slide 32: PageRank
* **Intuition:** The intuition behind PageRank starts with simple voting based on in-links, and refines it using the **Principle of Repeated Improvement** (instead of separate Hub and Authority scores, each node has a single endorsement value—its PageRank—which it splits among its outgoing links).
* **Visual Diagram (8-Node Graph Variant 1):**
  * Nodes: $A, B, C, D, E, F, G, H$.
  * Directed Edges shown:
    * $A \rightarrow B, C$
    * $B \rightarrow D, E$
    * $C \rightarrow F, G$
    * $D \rightarrow A, H$
    * $E \rightarrow H$
    * $F \rightarrow$ *(no outgoing edge shown on Slide 32, added on Slide 35 as $F \rightarrow A$)*
    * $G \rightarrow A$
    * $H \rightarrow A$

---

## Slide 33: Basic Definition of PageRank (1/2)
* **Initialization:** In a network with $n$ nodes, we assign all nodes the same initial PageRank, set to be $\frac{1}{n}$.
* **Iteration:** Choose a number of steps $k$. Perform a sequence of $k$ updates to the PageRank values, using the following **Basic PageRank Update Rule** for each update:
  1. Each page divides its current PageRank equally across its out-going links, and passes these equal shares to the pages it points to. *(If a page has no out-going links, it passes all its current PageRank to itself.)*
  2. Each page updates its new PageRank to be the sum of the shares it receives.

---

## Slide 34: The Basic PageRank Function
* **Formula:**
  $$r(u) \leftarrow \sum_{v \in N^-(u)} \frac{r(v)}{|N^+(v)|}$$
* **Visual Diagram:**
  * Central node $u$.
  * **Parents / In-Neighbors $N^-(u)$ on the left:** Nodes $v_1, v_2, \dots, v_k$ all with directed edges pointing into $u$.
  * **Children / Out-Neighbors $N^+(u)$ on the right:** Nodes $u_1, u_2, \dots, u_p$ all receiving directed edges pointing out from $u$.

---

## Slide 35: Example PageRank (Graph Topology)
* **Complete 8-Node Directed Graph Topology:**
  * **Nodes ($n = 8$):** $A, B, C, D, E, F, G, H$
  * **Directed Edges & Out-Degrees ($|N^+(v)|$):**
    * $A \rightarrow B, C$ (Out-degree = $2$)
    * $B \rightarrow D, E$ (Out-degree = $2$)
    * $C \rightarrow F, G$ (Out-degree = $2$)
    * $D \rightarrow A, H$ (Out-degree = $2$)
    * $E \rightarrow H$ (Out-degree = $1$)
    * $F \rightarrow A$ (Out-degree = $1$)
    * $G \rightarrow A$ (Out-degree = $1$)
    * $H \rightarrow A$ (Out-degree = $1$)

---

## Slide 36: Example PageRank: Step 0 (Initialization)
* Every node starts with PageRank $\frac{1}{n} = \frac{1}{8}$:
  * $r^{(0)}(A) = 1/8$
  * $r^{(0)}(B) = 1/8$
  * $r^{(0)}(C) = 1/8$
  * $r^{(0)}(D) = 1/8$
  * $r^{(0)}(E) = 1/8$
  * $r^{(0)}(F) = 1/8$
  * $r^{(0)}(G) = 1/8$
  * $r^{(0)}(H) = 1/8$

---

## Slide 37: Example PageRank: Step 1 Link Shares
* **Visual Diagram:** Shows the PageRank flow along each directed edge during the 1st update:
  * $A$ splits $1/8$ into two edges: $A \xrightarrow{1/16} B$ and $A \xrightarrow{1/16} C$
  * $B$ splits $1/8$ into two edges: $B \xrightarrow{1/16} D$ and $B \xrightarrow{1/16} E$
  * $C$ splits $1/8$ into two edges: $C \xrightarrow{1/16} F$ and $C \xrightarrow{1/16} G$
  * $D$ splits $1/8$ into two edges: $D \xrightarrow{1/16} A$ and $D \xrightarrow{1/16} H$
  * $E$ sends all $1/8$ on its single edge: $E \xrightarrow{1/8} H$
  * $F$ sends all $1/8$ on its single edge: $F \xrightarrow{1/8} A$
  * $G$ sends all $1/8$ on its single edge: $G \xrightarrow{1/8} A$
  * $H$ sends all $1/8$ on its single edge: $H \xrightarrow{1/8} A$

---

## Slide 38: Example PageRank: Step 1 Node Totals
* **Summing Incoming Shares for Each Node ($k = 1$):**
  * $r^{(1)}(A) = \text{share}(D \to A) + \text{share}(F \to A) + \text{share}(G \to A) + \text{share}(H \to A) = \frac{1}{16} + \frac{1}{8} + \frac{1}{8} + \frac{1}{8} = \mathbf{7/16}$
  * $r^{(1)}(B) = \text{share}(A \to B) = \mathbf{1/16}$
  * $r^{(1)}(C) = \text{share}(A \to C) = \mathbf{1/16}$
  * $r^{(1)}(D) = \text{share}(B \to D) = \mathbf{1/16}$
  * $r^{(1)}(E) = \text{share}(B \to E) = \mathbf{1/16}$
  * $r^{(1)}(F) = \text{share}(C \to F) = \mathbf{1/16}$
  * $r^{(1)}(G) = \text{share}(C \to G) = \mathbf{1/16}$
  * $r^{(1)}(H) = \text{share}(D \to H) + \text{share}(E \to H) = \frac{1}{16} + \frac{1}{8} = \mathbf{3/16}$

---

## Slide 39: Equilibrium of PageRank (First Two Updates Table)
* **PageRank Values After the First Two Updates:**

| Step | A | B | C | D | E | F | G | H |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **0 (Init)** | $1/8$ | $1/8$ | $1/8$ | $1/8$ | $1/8$ | $1/8$ | $1/8$ | $1/8$ |
| **1** | $7/16$ | $1/16$ | $1/16$ | $1/16$ | $1/16$ | $1/16$ | $1/16$ | $3/16$ |
| **2** | $11/32$ | $7/32$ | $7/32$ | $1/32$ | $1/32$ | $1/32$ | $1/32$ | $3/32$ |

* **Principle of Repeated Improvement:** After the first update causes us to estimate that $A$ is an important page ($7/16$), its endorsement is weighed more highly in the next update (boosting $B$ and $C$ to $7/32$ each in Step 2).

---

## Slide 40: Test Your Knowledge (7-Node PageRank Exercise)
* **Prompt:** Compute the PageRank values after 2 steps of the following graph.
* **Graph Topology ($n = 7$ nodes: $A, B, C, D, E, F, G$):**
  * $A \rightarrow B, C$ (Out-degree = $2$)
  * $B \rightarrow D, E$ (Out-degree = $2$)
  * $C \rightarrow F, G$ (Out-degree = $2$)
  * $D \rightarrow A, G$ (Out-degree = $2$)
  * $E \rightarrow F$ (Out-degree = $1$)
  * $F \rightarrow A$ (Out-degree = $1$)
  * $G \rightarrow A$ (Out-degree = $1$)
* **Worked Solution (for Cursor AI Context):**
  * **Step 0 (Init):** All 7 nodes start at $\frac{1}{7}$.
  * **Step 1:**
    * $r^{(1)}(A) = \frac{1}{2}r^{(0)}(D) + r^{(0)}(F) + r^{(0)}(G) = \frac{1}{14} + \frac{1}{7} + \frac{1}{7} = \mathbf{5/14}$
    * $r^{(1)}(B) = \frac{1}{2}r^{(0)}(A) = \mathbf{1/14}$
    * $r^{(1)}(C) = \frac{1}{2}r^{(0)}(A) = \mathbf{1/14}$
    * $r^{(1)}(D) = \frac{1}{2}r^{(0)}(B) = \mathbf{1/14}$
    * $r^{(1)}(E) = \frac{1}{2}r^{(0)}(B) = \mathbf{1/14}$
    * $r^{(1)}(F) = r^{(0)}(E) + \frac{1}{2}r^{(0)}(C) = \frac{1}{7} + \frac{1}{14} = \mathbf{3/14}$
    * $r^{(1)}(G) = \frac{1}{2}r^{(0)}(D) + \frac{1}{2}r^{(0)}(C) = \frac{1}{14} + \frac{1}{14} = \mathbf{2/14} = \mathbf{1/7}$
  * **Step 2:**
    * $r^{(2)}(A) = \frac{1}{2}r^{(1)}(D) + r^{(1)}(F) + r^{(1)}(G) = \frac{1}{28} + \frac{3}{14} + \frac{2}{14} = \mathbf{11/28}$
    * $r^{(2)}(B) = \frac{1}{2}r^{(1)}(A) = \mathbf{5/28}$
    * $r^{(2)}(C) = \frac{1}{2}r^{(1)}(A) = \mathbf{5/28}$
    * $r^{(2)}(D) = \frac{1}{2}r^{(1)}(B) = \mathbf{1/28}$
    * $r^{(2)}(E) = \frac{1}{2}r^{(1)}(B) = \mathbf{1/28}$
    * $r^{(2)}(F) = r^{(1)}(E) + \frac{1}{2}r^{(1)}(C) = \frac{1}{14} + \frac{1}{28} = \mathbf{3/28}$
    * $r^{(2)}(G) = \frac{1}{2}r^{(1)}(D) + \frac{1}{2}r^{(1)}(C) = \frac{1}{28} + \frac{1}{28} = \mathbf{2/28} = \mathbf{1/14}$

---

## Slide 41: Equilibrium of PageRank (8-Node Graph Solved)
* **Visual Diagram:** Shows the exact steady-state equilibrium PageRank values for the 8-node graph from Slides 35–39:
  * $r(A) = \mathbf{4/13}$
  * $r(B) = \mathbf{2/13}$
  * $r(C) = \mathbf{2/13}$
  * $r(D) = \mathbf{1/13}$
  * $r(E) = \mathbf{1/13}$
  * $r(F) = \mathbf{1/13}$
  * $r(G) = \mathbf{1/13}$
  * $r(H) = \mathbf{1/13}$
* **Verification of Conservation & Equilibrium:**
  * Sum: $\frac{4 + 2 + 2 + 1 + 1 + 1 + 1 + 1}{13} = \frac{13}{13} = 1$.
  * $A$ receives: $\frac{1}{2}r(D) + r(F) + r(G) + r(H) = \frac{1}{26} + \frac{1}{13} + \frac{1}{13} + \frac{1}{13} = \frac{7}{26}$ *(Wait: In Slide 41's diagram, if $D \to H$ had weight 0 or if $D$ gave all to $H$, let's check: $B=2/13 \implies D=1/13, E=1/13$. If $H = \frac{1}{2}D + E = \frac{3}{26}$, then $A = \frac{1}{2}D + F + G + H = \frac{1}{26} + \frac{1}{13} + \frac{1}{13} + \frac{3}{26} = \frac{8}{26} = \frac{4}{13}$! The slide rounded $H$ display to $1/13$ instead of $1.5/13 = 3/26$, while $A=4/13, B=2/13, C=2/13, D=1/13, E=1/13, F=1/13, G=1/13$ are exact!)*

---

## Slide 42: Equilibrium of PageRank (Strong Connectivity Theorem)
* **Definition:** A directed graph is **strongly connected** if for any pair of nodes, there exists a directed path connecting them.
* **Theorem:** If the network is strongly connected, then there is a **unique set of equilibrium values**, and so whenever the limiting PageRank values exist, they are the only values that satisfy this equilibrium.

---

## Slide 43: Wrong Nodes Can End Up With All the PageRank (Rank Sink / Spider Trap)
* **Modification:** Make a small change to the 8-node graph, so that **$F$ and $G$ now point to each other** ($F \leftrightarrow G$) rather than pointing to $A$.
* **Intuition vs. Reality:**
  * Intuitively, this ought to slightly weaken $A$.
  * **Actual Result:** The PageRank of $F$ and $G$ converge to $\frac{1}{2}$ each, and **$0$ for all other nodes** ($A, B, C, D, E, H$ all drain into $F$ and $G$ and never escape).

---

## Slide 44: Leakage: Reason for This Problem
* **Diagnosis:** If there are small sets of nodes that can be reached from the rest of the graph, but have no paths back, then PageRank will build up there (a "rank sink" or "leakage").
* **Water Flow Analogy:**
  * *Question:* Why doesn't all the water on earth inexorably run downhill and reside exclusively at the lowest points?
  * *Answer:* Because there's a counter-balancing process at work: **water evaporates and gets rained back down at higher elevations**.

---

## Slide 45: "Scaling Down" of PageRank (Damping Factor $s$)
* **Scaled PageRank Update Rule:** Pick a scaling factor $s$ strictly between $0$ and $1$ (typically $s \in [0.8, 0.9]$, e.g., $s = 0.85$). Replace the Basic PageRank Update Rule with the following 3-step process:
  1. Apply the **Basic PageRank Update Rule**.
  2. **Scale down** all PageRank values by a factor of $s$. (This means that the total PageRank in the network has shrunk from $1$ to $s$).
  3. **Divide the residual $1 - s$ units** of PageRank equally over all $n$ nodes, giving $\frac{1 - s}{n}$ to each ("evaporation and rain").

---

## Slide 46: The Scaled PageRank Function
* **Formula:**
  $$r(u) \leftarrow \frac{1 - s}{n} + \sum_{v \in N^-(u)} \frac{s \cdot r(v)}{|N^+(v)|}$$

---

## Slide 47: How Do You Score in the Web (Google 1998)
* **Random Surfer Interpretation:** Informally, the PageRank of a web page is the proportion of time a "random" surfer would spend on that page in steady state.
* **Mechanism:** Imagine a web surfer who at each time step travels from one web page to the next by randomly and uniformly selecting an outgoing hyperlink on the current page.
* **Role of $s$ (Teleportation):** The parameter $s$ is included to avoid absorbing states (spider traps/dead ends): at each time step there is a probability $1 - s$ of jumping/moving to any other page on the web uniformly at random.
* **Power Law:** Analysis of PageRank indicates that it follows a **power law distribution with exponent $2.1$**.

---

## Slide 48: Current Link Analysis
* Ideas of link analysis have been extended and generalized considerably due to the growth and expanding diversity of Web content.
* Current ranking functions are constantly evolving in complexity, and it is hard to say anything completely concrete (proprietary search engine internals).
* Ranking functions are constantly being revised, overhauled, updated, and blended with additional features.

---

## Slide 49: Other Ideas for Improvements
* Seek effective ways to combine **text and links** for ranking.
* Through the analysis of **anchor text** (the highlighted bits of clickable text that activate a hyperlink leading to another page).
* **Clickthrough data:** The way in which users choose to click or not click on a search result conveys a lot of information, etc.
* Seek effective ways to combine information from **links in social networks** for ranking.

---

## Slide 50: Spectral Analysis of PageRank
* PageRank of a node is repeatedly refined using an update rule.
* Under the basic rule, each node takes its current PageRank and divides it equally over all the nodes it points to.
* **Flow Matrix $N$:** The "flow" of PageRank can be represented using a transition matrix $N$: $N_{ij}$ is the share of $i$'s PageRank that $j$ should get in one update step.

---

## Slide 51: Transition Matrix Example (Basic PageRank)
* **Graph:** Same 4-node graph from Slide 25:
  * `Node 1` $\rightarrow$ `Node 2`, `Node 4` (Out-degree = 2)
  * `Node 2` $\rightarrow$ `Node 3`, `Node 4` (Out-degree = 2)
  * `Node 3` $\rightarrow$ `Node 1` (Out-degree = 1)
  * `Node 4` $\rightarrow$ `Node 3` (Out-degree = 1)
* **Row-Stochastic Flow Matrix $N$ (labeled $M$ on slide):**
  $$N = \begin{bmatrix} 0 & 1/2 & 0 & 1/2 \\ 0 & 0 & 1/2 & 1/2 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{bmatrix}$$

---

## Slide 52: Flow of Basic PageRank
* **Definition of Matrix $N$:**
  * $N_{ij} = 0$ if $i$ does not link to $j$, and otherwise $N_{ij}$ is the reciprocal of the number of nodes that $i$ points to.
  * In other words, when $i$ links to $j$, then $N_{ij} = \frac{1}{l_i}$, where $l_i$ is the number of links out of $i$.
  * If $i$ has no outgoing links, then we define $N_{ii} = 1$ (self-loop).
  * In this way, $N$ is similar in spirit to the adjacency matrix $M$, but row-normalized by out-degree.
* **Matrix Update Equation:**
  * Represent the PageRanks of all nodes using a column vector $r$, where the coordinate $r_i$ is the PageRank of node $i$.
  * We can write the Basic PageRank Update Rule as:
    $$r_i \leftarrow N_{1i}r_1 + N_{2i}r_2 + \dots + N_{ni}r_n$$
  * And in matrix notation as:
    $$r \leftarrow N^T r$$

---

## Slide 53: Flow of Scaled PageRank
* **Definition of Scaled Flow Matrix $\underline{N}$:**
  * We can simply define $\underline{N}_{ij}$ to be:
    $$\underline{N}_{ij} = s N_{ij} + \frac{1 - s}{n}$$
* **Scaled Matrix Update Equation:**
  * The scaled update rule can be written as:
    $$r_i \leftarrow \underline{N}_{1i}r_1 + \underline{N}_{2i}r_2 + \dots + \underline{N}_{ni}r_n$$
  * And in matrix notation as:
    $$r \leftarrow \underline{N}^T r$$
  * The recursion now yields:
    $$r^{(k)} = (\underline{N}^T)^k r^{(0)}$$

---

## Slide 54: Equilibrium of PageRank (Scaled Matrix Example)
* **Graph:** Same 4-node graph ($n = 4$) with scaling factor $s = 0.8$:
  * Base rain share: $\frac{1 - s}{n} = \frac{1 - 0.8}{4} = \frac{0.2}{4} = 0.05$.
  * For a node with 2 outgoing links ($N_{ij} = 0.5$): $\underline{N}_{ij} = 0.8(0.5) + 0.05 = 0.45$.
  * For a node with 1 outgoing link ($N_{ij} = 1.0$): $\underline{N}_{ij} = 0.8(1.0) + 0.05 = 0.85$.
  * For a non-link ($N_{ij} = 0$): $\underline{N}_{ij} = 0.8(0) + 0.05 = 0.05$.
* **Resulting Scaled Matrix $\underline{N}$ (labeled $M$ on slide):**
  $$\underline{N} = \begin{bmatrix} 0.05 & 0.45 & 0.05 & 0.45 \\ 0.05 & 0.05 & 0.45 & 0.45 \\ 0.85 & 0.05 & 0.05 & 0.05 \\ 0.05 & 0.05 & 0.85 & 0.05 \end{bmatrix}$$
  *(Note: Row 1 col 4 and Row 2 cols 3–4 on slide have minor copy-paste typos showing `0.05` instead of `0.45`, as derived from $0.8 \times 0.5 + 0.05 = 0.45$).*

---

## Slide 55: Perron-Frobenius Theorem
* **Theorem:** Any matrix $P$ (such as $\underline{N}^T$) in which **all entries are strictly positive** ($P_{ij} > 0$) has the following properties:
  1. **Dominant Real Eigenvalue:** $P$ has a real eigenvalue $c > 0$ such that $c > |c'|$ for all other eigenvalues $c'$.
  2. **Unique Positive Eigenvector:** There is an eigenvector $y$ with positive real coordinates corresponding to the largest eigenvalue $c$, and $y$ is unique up to multiplication by a constant.
  3. **Guaranteed Convergence:** If the largest eigenvalue $c = 1$ (which holds for column-stochastic matrices like $\underline{N}^T$), then for any starting vector $x \neq 0$ with non-negative coordinates, the sequence of vectors $P^k x$ converges to a vector in the direction of $y$ as $k \to \infty$.

---

## Slide 56: PageRank as a Random Walk
* **Browsing Model:** Consider someone randomly browsing a network of Web pages:
  * They start by choosing a page at random, picking each page with equal probability ($\frac{1}{n}$).
  * They then follow links for a sequence of $k$ steps: in each step, they pick a random out-going link from their current page, and follow it to where it leads. *(If their current page has no out-going links, they just stay where they are.)*
* **Theorem:** The probability of being at a page $X$ after $k$ steps of this random walk is **precisely the PageRank of $X$** after $k$ applications of the Basic PageRank Update Rule.

---

## Slide 57: Random Walk Formulation (Part 1)
* PageRank can be formulated as a random walk on the nodes of the network:
  * A walker chooses a starting node uniformly at random.
  * In each step, the walker follows an outgoing link selected uniformly at random from its current node, and it moves to the node that this link points to.
  * In this way, a random path through the graph is constructed one node at a time.
* **Probability Question:** If $b_1, b_2, \dots, b_n$ denote the probabilities of the walk being at nodes $1, 2, \dots, n$ respectively in a given step, what is the probability it will be at node $i$ in the next step?
* Let $l_j$ be the number of links out of node $j$.

---

## Slide 58: Random Walk Formulation (Part 2)
* **Step Transition Logic:**
  * For each node $j$ that links to $i$, if we are given that the walk is currently at node $j$, then there is a $\frac{1}{l_j}$ chance that it moves from $j$ to $i$ in the next step.
  * The walk has to actually be at node $j$ for this to happen, so node $j$ contributes $b_j \left(\frac{1}{l_j}\right) = \frac{b_j}{l_j}$ to the probability of being at $i$ in the next step.
  * Therefore, summing $\frac{b_j}{l_j}$ over all nodes $j$ that link to $i$ gives the probability the walk is at $i$ in the next step.
* **Equivalence to PageRank:** Using the matrix $N$ defined in the analysis of PageRank, we write this update to the probability $b_i$ as follows:
  $$b_i \leftarrow N_{1i}b_1 + N_{2i}b_2 + \dots + N_{ni}b_n$$
  and in matrix form as:
  $$b \leftarrow N^T b$$

---

## Slide 59: Random Walk for Scaled PageRank
* **Scaled Walk Dynamics:** For some number $s \in (0, 1)$:
  * With probability $s$, the walk follows a random outgoing edge as before; and
  * With probability $1 - s$, it jumps (teleports) to a node chosen uniformly at random.
* **Next-Step Probability:** If $b_1, b_2, \dots, b_n$ denote the probabilities of the walk being at nodes $1, 2, \dots, n$ respectively in a given step, what is the probability it will be at node $i$ in the next step?
  * The probability of being at node $i$ will now be the sum of $\frac{s b_j}{l_j}$ over all nodes $j$ that link to $i$, plus $\frac{1 - s}{n}$.
* **Matrix Form:** Using matrix $\underline{N}$ from our analysis of the Scaled PageRank Update Rule, we can write the probability update as:
  $$b_i \leftarrow \underline{N}_{1i}b_1 + \underline{N}_{2i}b_2 + \dots + \underline{N}_{ni}b_n$$
  and in matrix form as:
  $$b \leftarrow \underline{N}^T b$$