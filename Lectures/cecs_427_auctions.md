# CECS 427: Dynamic Networks — Auctions

---

## Slide 1: Title
* **Course:** CECS 427 Dynamic Networks
* **Topic:** Auctions

---

## Slide 2: Overview of Auctions
* **When Auctions are Used:**
  * Sellers are in situations where they do not have a good estimate of the buyers' true values for an item.
  * Buyers do not know each other's true values.
* **4 Basic Types of Auctions:**
  1. **Open Ascending-Bid Auction** (English Auction)
  2. **Open Descending-Bid Auction** (Dutch Auction)
  3. **1st-Price Sealed-Bid Auction**
  4. **2nd-Price Sealed-Bid Auction** (Vickrey Auction)
* *Note:* There are several other kinds of auctions, but all fall into one of these categories or combinations thereof.

---

## Slide 3: Core Assumptions (Independent Private Values)
* Each bidder knows their own true value ($v_i$).
* The values are **independent** across different bidders.
* Bidders are **not concerned** with how much the item is worth to anyone else (purely private valuation).

---

## Slide 4: Open Ascending-Bid Auctions (English Auction)
* Normally interactive in real-time.
* **Auction Process:**
  * The seller (or buyers) gradually raises the price.
  * Bidders drop out one by one as the price increases until finally only one bidder remains.
  * That remaining bidder wins the object at the final price.
* **Bidding Mechanism:**
  * Bidders can shout out the prices in person or submit them electronically.

---

## Slide 5: Open Descending-Bid Auctions (Dutch Auction)
* Normally interactive in real-time.
* **Auction Process:**
  * The seller starts at some very high initial value and gradually lowers the price.
  * It continues until the first moment when some bidder accepts and pays the current price.

---

## Slide 6: 1st-Price Sealed-Bid Auctions
* **Auction Process:**
  * Bidders simultaneously submit a private "sealed bid" to the seller.
  * The highest bidder wins the object and pays the exact value of their own bid.

---

## Slide 7: 2nd-Price Sealed-Bid Auctions (Vickrey Auction)
* **Auction Process:**
  * Bidders simultaneously submit a private "sealed bid" to the seller.
  * The highest bidder wins the object and pays the value of the **second-highest bid**.

---

## Slide 8: Equivalence: Descending-Bid and 1st-Price Sealed-Bid Auctions
* **Descending-Bid Dynamics:**
  * Bidders learn nothing while the auction is running (because no one speaks until the auction ends).
  * For each bidder $i$, there is a threshold price $b_i$ at which they plan to accept the item if no one else has accepted yet.
* **1st-Price Sealed-Bid Equivalence:**
  * Threshold price $b_i$ plays the exact role of bidder $i$'s sealed bid.
  * The highest threshold bid wins and pays $b_{\text{highest}}$.

| Feature | Descending-Bid Auction | 1st-Price Sealed-Bid Auction |
| :--- | :--- | :--- |
| **Bidder $i$'s Action** | Threshold price $b_i$ to accept | Sealed bid $b_i$ |
| **Winning Condition** | First to accept | Highest bid ($b_{\text{highest}}$) |
| **Payment** | $b_{\text{highest}}$ | $b_{\text{highest}}$ |

---

## Slide 9: Equivalence: Ascending-Bid and 2nd-Price Sealed-Bid Auctions (Part 1)
* In ascending-bid auctions, bidders gradually drop out as the seller steadily raises the price.
* The winner of the auction is the last bidder remaining, and they pay the price at which the **second-to-last bidder** drops out.
* **Strategic Questions:**
  * *Does it ever make sense to stay in the auction after the price reaches your true value?* **No**, you risk winning and paying more than $v_i$ (negative payoff).
  * *Does it ever make sense to drop out before the price reaches your true value for the item?* **No**, you might forfeit a positive payoff.
* **Conclusion:** You should stay in an ascending-bid auction up to the exact moment the price reaches your true value $v_i$.

---

## Slide 10: Equivalence: Ascending-Bid and 2nd-Price Sealed-Bid Auctions (Part 2)
* We can reformulate the ascending-bid auction as follows:
  * Each bidder decides on a drop-out price (their bid).
  * The person with the highest bid stays in the longest.
  * They win the item and pay the price at which the second-to-last person dropped out.
* Thus, the item goes to the highest bidder at a price equal to the second-highest bid.
* **Result:** It is strategically equivalent to the $2^{\text{nd}}$-price sealed-bid auction.

---

## Slide 11: 2nd-Price Sealed-Bid Auctions in Practice
* **Examples in Use:**
  * **eBay** (proxy bidding system)
  * **Keyword-based advertising** (Generalized Second Price / VCG variants in search engines)
* **An Important Result in Auction Theory:**
  * With independent, private values, **bidding your true value is a dominant strategy** in a second-price sealed-bid auction.
  * The best choice of bid is exactly what the object is worth to you ($b_i = v_i$).

---

## Slide 12: 2nd-Price Sealed-Bid Auctions as Games
* **Game Formulation:**
  * **Players:** The bidders.
  * **True Value:** Let $v_i$ be bidder $i$'s true value for the object.
  * **Strategy:** Bidder $i$'s strategy is to bid an amount $b_i$ as a function of their true value $v_i$.
* **Payoff Function:** In a $2^{\text{nd}}$-price sealed-bid auction, the payoff to bidder $i$ with value $v_i$ and bid $b_i$ is defined as:
  * If $b_i$ is **not** the winning bid, then the payoff to $i$ is $0$.
  * If $b_i$ **is** the winning bid, and some other $b_j$ is the second-place bid, then the payoff to $i$ is:
    $$\text{Payoff}_i = v_i - b_j$$
* *Tie-breaking rule:* Ties are broken by the order in which bids were submitted.

---

## Slide 13: Test Your Knowledge — 2nd-Price Auction Payoffs
* **Scenario:** Suppose three grocery stores want to buy 200 pounds of tomatoes from a producer:
  * **Grocery 1:** $v_1 = 70$
  * **Grocery 2:** $v_2 = 65$
  * **Grocery 3:** $v_3 = 80$

* **Case 1: Determine the payoffs if $b_1 = v_1 = 70$, $b_2 = v_2 = 65$, and $b_3 = v_3 = 80$.**
  * *Analysis:* Grocery 3 has the highest bid ($b_3 = 80$) and wins. The second-highest bid is Grocery 1 ($b_1 = 70$).
  * *Payoffs:*
    * $\text{Payoff}_1 = 0$
    * $\text{Payoff}_2 = 0$
    * $\text{Payoff}_3 = v_3 - b_1 = 80 - 70 = 10$

* **Case 2: Determine the payoffs if $b_1 = v_1 + 20 = 90$, $b_2 = v_2 = 65$, and $b_3 = v_3 = 80$.**
  * *Analysis:* Grocery 1 overbids ($b_1 = 90$) and wins. The second-highest bid is Grocery 3 ($b_3 = 80$).
  * *Payoffs:*
    * $\text{Payoff}_1 = v_1 - b_3 = 70 - 80 = -10$ (Grocery 1 suffers a loss by overbidding!)
    * $\text{Payoff}_2 = 0$
    * $\text{Payoff}_3 = 0$

* **Case 3: Determine the payoffs if $b_1 = v_1 = 70$, $b_2 = v_2 = 65$, and $b_3 = v_3 - 12 = 68$.**
  * *Analysis:* Grocery 3 underbids ($b_3 = 68$). Grocery 1 now has the highest bid ($b_1 = 70$) and wins. Second-highest bid is $b_3 = 68$.
  * *Payoffs:*
    * $\text{Payoff}_1 = v_1 - b_3 = 70 - 68 = 2$
    * $\text{Payoff}_2 = 0$
    * $\text{Payoff}_3 = 0$ (Grocery 3 loses out on a payoff of $10$ by shading its bid too low!)

---

## Slide 14: Truthful Bidding in 2nd-Price Sealed-Bid Auctions (Theorem)
* **Theorem:** In a $2^{\text{nd}}$-price sealed-bid auction, it is a **dominant strategy** for each bidder $i$ to choose a bid $b_i := v_i$, where $v_i$ is bidder $i$'s true value for the object.
* **Proof Strategy:** We need to show that if bidder $i$ bids $b_i := v_i$, then no deviation from this bid would improve their payoff, regardless of what strategy everyone else is using.

---

## Slide 15: Truthful Bidding Proof — Key Observations
* There are two cases of deviation to consider:
  1. Deviations in which $i$ **raises** their bid ($b'_i > v_i$).
  2. Deviations in which $i$ **lowers** their bid ($b''_i < v_i$).
* **Key Observation in Both Cases:**
  * The value of $i$'s bid **only affects whether $i$ wins or loses**.
  * It **never affects how much $i$ pays** in the event that they win (the amount paid is determined entirely by the largest among the *other* bids, $b_j = \max_{k \neq i} b_k$).
* Since all other bids remain the same when $i$ changes their bid, a change to $i$'s bid only affects their payoff if it **changes their win/loss outcome**.

---

## Slides 16–18: Visual Diagram of Bid Deviations
* **Diagram Representation:** Payoff is only affected if the highest other bid falls strictly between the truthful bid and the alternate bid.

```
Price Scale (Vertical Axis)
  ^
  |   --- Alternate Raised Bid: b'_i  (Slide 17)
  |    |  [Zone A: If highest other bid b_j is here, raising bid causes i to
  |    |   turn a loss into a win, but i pays b_j > v_i -> Negative Payoff!]
  |   === Truthful Bid: b_i = v_i     (Slide 16)
  |    |  [Zone B: If highest other bid b_k is here, lowering bid causes i to
  |    |   turn a win into a loss, losing out on v_i - b_k >= 0 -> Lower Payoff!]
  |   --- Alternate Lowered Bid: b''_i (Slide 18)
  |
```

---

## Slide 19: Case 1 — Choose Bid Higher Than $v_i$ ($b'_i > v_i$)
* Suppose that instead of bidding $v_i$, bidder $i$ chooses a higher bid $b'_i > v_i$.
* This only affects bidder $i$'s payoff if $i$ would **lose** with bid $v_i$ but would **win** with bid $b'_i$.
* In order for this to happen, the highest other bid $b_j$ must lie between $v_i$ and $b'_i$:
  $$v_i \le b_j \le b'_i$$
* In this case:
  * Truthful payoff (losing): $0$.
  * Deviating payoff (winning at price $b_j$): $v_i - b_j \le 0$.
* **Conclusion:** This upward deviation to bid $b'_i$ does not improve $i$'s payoff.

---

## Slide 20: Case 2 — Choose Bid Lower Than $v_i$ ($b''_i < v_i$)
* Suppose that instead of bidding $v_i$, bidder $i$ chooses a lower bid $b''_i < v_i$.
* This only affects bidder $i$'s payoff if $i$ would **win** with bid $v_i$ but would **lose** with bid $b''_i$.
* Before deviating, $v_i$ was the winning bid, and the second-place (highest other) bid $b_k$ was between $b''_i$ and $v_i$:
  $$b''_i \le b_k \le v_i$$
* In this case:
  * Truthful payoff (winning at price $b_k$): $v_i - b_k \ge 0$.
  * Deviating payoff (losing): $0$.
* **Conclusion:** Therefore, lowering the bid to $b''_i$ does not improve $i$'s payoff.

---

## Slide 21: 1st-Price Sealed-Bid Auctions as Games
* In a $1^{\text{st}}$-price sealed-bid auction, the value of your bid not only affects whether you win, **but also how much you pay**.
* Bidders are players, and each bidder's strategy is an amount to bid as a function of their true value: $b_i = s(v_i)$.
* **Payoff Function:** The payoff to bidder $i$ with value $v_i$ and bid $b_i$ is:
  * If $b_i$ is **not** the winning bid, then the payoff to $i$ is $0$.
  * If $b_i$ **is** the winning bid, then the payoff to $i$ is:
    $$\text{Payoff}_i = v_i - b_i$$

---

## Slide 22: Test Your Knowledge — 1st-Price Auction Payoffs
* **Scenario:** Two non-profit organizations participate in a 1st-price auction to buy 100 pieces of bread from a bakery:
  * **Non-profit Organization 1:** $v_1 = 30$
  * **Non-profit Organization 2:** $v_2 = 28$

* **Question 1: Determine the payoffs if $b_1 = 28.5$ and $b_2 = v_2 = 28$.**
  * *Analysis:* Organization 1 wins ($28.5 > 28$) and pays its own bid ($28.5$).
  * $\text{Payoff}_1 = v_1 - b_1 = 30 - 28.5 = 1.5$
  * $\text{Payoff}_2 = 0$

* **Question 2: Determine the payoffs if $b_1 = 27.5$ and $b_2 = v_2 = 28$.**
  * *Analysis:* Organization 2 wins ($28 > 27.5$) and pays its own bid ($28$).
  * $\text{Payoff}_1 = 0$
  * $\text{Payoff}_2 = v_2 - b_2 = 28 - 28 = 0$

* **Question 3: What would be the bids that have the maximum payoffs (assuming complete information)?**
  * Organization 1 wants to bid just barely above Organization 2's bid ($b_1 = b_2 + \epsilon$, or equal to $b_2$ if tie-breaking favors Org 1). If $b_2 = 28$, Org 1 maximizes payoff by bidding $28 + \epsilon \approx 28$, yielding a payoff approaching $30 - 28 = 2$.

---

## Slide 23: Strategic Trade-offs in 1st-Price Auctions (Part 1)
* **Bidding your true value ($b_i = v_i$) is no longer a dominant strategy:**
  * You get a payoff of $0$ if you lose (as usual), AND
  * You also get a payoff of $v_i - v_i = 0$ if you win (you pay exactly what it was worth to you).
* **Optimal Approach ("Bid Shading"):**
  * The optimal way to bid in a $1^{\text{st}}$-price auction is to **"shade" your bid slightly downward** ($b_i < v_i$) so that if you win, you will get a strictly positive payoff ($v_i - b_i > 0$).

---

## Slide 24: Strategic Trade-offs in 1st-Price Auctions (Part 2)
* Determining how much to shade your bid involves balancing a **trade-off between two opposing forces**:
  1. **Bid too close to $v_i$:** Your probability of winning is high, but your payoff ($v_i - b_i$) won't be very large in the event that you win.
  2. **Bid too far below $v_i$:** Your payoff if you win is large, but you drastically reduce your chance of being the highest bid and hence your chance of winning at all.
* Finding the optimal trade-off between these two factors is a complex problem that depends on knowledge of the other bidders and their **probability distribution of possible values**.

---

## Slide 25: Equilibrium Bidding in 1st-Price Auctions — Model Setup
* **Common Knowledge Assumptions:**
  * Two bidders ($n = 2$), each with a private value $v_i$ that is **independently and uniformly distributed** on the interval $[0, 1]$.
* **Strategy Function:**
  * A strategy for a bidder is a function $s: [0, 1] \to \mathbb{R}_{\ge 0}$ where $s(v) = b$ maps their true value $v$ to a non-negative bid $b$.
* **Assumptions on $s(v)$:**
  1. $s$ is a **strictly increasing, differentiable function** of $v$:
     * If two bidders have different values ($v \neq v'$), then they will produce different bids ($s(v) \neq s(v')$), and higher value means higher bid.
  2. $s(v) \le v$ for all $v$:
     * Bidders can shade their bids down, but they will never bid above their true values.
     * Since bids are non-negative ($s(v) \ge 0$), this also implies that **$s(0) = 0$**.

---

## Slide 26: Equilibrium Bidding in 1st-Price Auctions — Theorem (2 Bidders)
* **Examples of Strategy Functions:**
  * Bidding your true value: $s(v) = v$.
  * Shading your bid downward by a constant factor $c < 1$: $s(v) = cv$.
  * Non-linear strategies such as $s(v) = v^2$ are allowed by the model, although they are not optimal.
* **Theorem:** If two bidders know they are competing against each other and know that each has a private value drawn uniformly at random from the interval $[0, 1]$, then it is a symmetric **Nash equilibrium** for each to shade their bid down by a factor of $2$:
  $$s(v) = \frac{1}{2}v$$

---

## Slide 27: Deriving Equilibrium with 2 Bidders (Step 1: Expected Payoff)
* **Assumption 1** ($s$ is strictly increasing and differentiable) guarantees that the bidder with the higher true value will also produce the higher bid and win the auction.
* If bidder $i$ has a true value of $v_i$:
  * Since the competitor's value is drawn uniformly from $[0, 1]$, the probability that $v_i$ is higher than the competitor's value is exactly $v_i$:
    $$\mathbb{P}(\text{Bidder } i \text{ wins}) = \mathbb{P}(v_{\text{competitor}} < v_i) = v_i$$
  * If $i$ does win, $i$ receives a payoff of $v_i - s(v_i)$.
* **Expected Payoff:** Putting all this together, bidder $i$'s expected payoff is:
  $$g(v_i) = v_i \cdot (v_i - s(v_i))$$

---

## Slide 28: Deriving Equilibrium with 2 Bidders (Step 2: Reasoning About Deviations)
* **What does it mean for $s(\cdot)$ to be an equilibrium strategy?**
  * For each bidder $i$, there is no incentive for $i$ to deviate from strategy $s$ if $i$'s competitor is also using strategy $s$.
* **How do we reason about deviations to an arbitrary strategy?**
  * Rather than switching to an entirely different function, bidder $i$ can implement any valid deviation by **keeping the strategy function $s(\cdot)$ but supplying a different "fake" value $v$ to it**.

---

## Slide 29: Deriving Equilibrium with 2 Bidders (Step 3: Range of Bids)
* If $i$'s competitor is using strategy $s(\cdot)$, the maximum possible bid the competitor will ever make is $s(1)$.
* Therefore, $i$ should never announce a bid $b > s(1)$, since $i$ is already guaranteed to win with bid $s(1)$ and gets a strictly higher payoff with $s(1)$ than with any $b > s(1)$.
* Thus, in any rational deviation by $i$, the bid they actually report will lie between $s(0) = 0$ and $s(1)$.
* Since $s(\cdot)$ is continuous and strictly increasing on $[0, 1]$, any bid $b \in [0, s(1)]$ can be written as $b = s(v'_i)$ for some $v'_i \in [0, 1]$.
* Therefore, bidder $i$ can simulate any deviation by pretending her true value is $v'_i$ rather than $v_i$, and applying $s(v'_i)$.

---

## Slide 30: Deriving Equilibrium with 2 Bidders (Step 4: The Revelation Principle)
* **Revelation Principle Concept:** Deviations in the bidding strategy function can instead be viewed as deviations in the "reported value" $v \in [0, 1]$ that bidder $i$ supplies to her current strategy function $s(\cdot)$.
* If bidder $i$ (with true value $v_i$) supplies fake value $v$, she bids $s(v)$ and wins whenever the competitor's true value is less than $v$ (which happens with probability $v$).
* **Equilibrium Condition:** Bidder $i$ does not want to deviate from reporting $v_i$ if and only if:
  $$v_i(v_i - s(v_i)) \ge v(v_i - s(v)) \quad \text{for all } v \in [0, 1]$$
* **Verification:** It is easy to check that $s(v) = \frac{v}{2}$ satisfies this inequality.

---

## Slide 31: Deriving Equilibrium with 2 Bidders (Step 5: Algebraic Verification)
* Substitute $s(v) = \frac{v}{2}$ into the equilibrium inequality:
  * **Left-Hand Side (Truthful $v_i$):**
    $$v_i\left(v_i - \frac{v_i}{2}\right) = \frac{v_i^2}{2}$$
  * **Right-Hand Side (Deviating $v$):**
    $$v\left(v_i - \frac{v}{2}\right) = v v_i - \frac{v^2}{2}$$
* Comparing LHS and RHS:
  $$\frac{v_i^2}{2} \ge v v_i - \frac{v^2}{2}$$
* Moving all terms to the left-hand side:
  $$\frac{1}{2}\left(v^2 - 2v v_i + v_i^2\right) \ge 0 \iff \frac{1}{2}(v - v_i)^2 \ge 0$$
* Since a squared real number is always non-negative, the inequality holds for all $v \in [0, 1]$ and is uniquely maximized at $v = v_i$.
* **Conclusion:** Bidding half your true value ($s(v_i) = \frac{v_i}{2}$) is optimal for 2 bidders.

---

## Slide 32: Deriving the Two-Bidder Equilibrium via Calculus
* **How do we discover $s(\cdot)$ directly without guessing?**
* For fixed true value $v_i$, define the expected payoff as a function of the reported value $v$:
  $$g(v) = v(v_i - s(v)) = v v_i - v s(v)$$
* For $g(v)$ to be maximized at $v = v_i$, its first derivative with respect to $v$ must equal $0$ at $v = v_i$:
  $$g'(v_i) = 0$$
* By the Product Rule:
  $$g'(v) = v_i - s(v) - v s'(v)$$
* Setting $g'(v_i) = 0$ gives the first-order linear differential equation:
  $$v_i - s(v_i) - v_i s'(v_i) = 0 \implies s'(v_i) = 1 - \frac{s(v_i)}{v_i} \quad (\text{or } (v_i s(v_i))' = v_i)$$
* Integrating both sides with respect to $v_i$ and using boundary condition $s(0) = 0$:
  $$v_i s(v_i) = \frac{v_i^2}{2} + C \implies s(v_i) = \frac{v_i}{2}$$

---

## Slide 33: Equilibrium with $n \ge 2$ Bidders (Setup)
* Suppose there are $n \ge 2$ bidders, and each bidder $i$ draws her true value $v_i$ independently and uniformly at random from $[0, 1]$.
* **Probability of Winning:**
  * Since $s(\cdot)$ is strictly increasing, the bidder with the highest true value produces the highest bid and wins.
  * For bidder $i$ with true value $v_i$ to win (or if reporting value $v$), **all $n - 1$ other bidders** must have values below $v_i$.
  * Since values are independent and uniform on $[0, 1]$, the probability that a single competitor's value is $\le v_i$ is $v_i$.
  * The probability that all $n - 1$ competitors have values $\le v_i$ is:
    $$\mathbb{P}(\text{Win with value } v_i) = v_i^{n-1}$$
* **Expected Payoff:**
  $$G(v_i) = v_i^{n-1}(v_i - s(v_i))$$

---

## Slide 34: Equilibrium with $n \ge 2$ Bidders (Derivation)
* Using the Revelation Principle, supplying a "fake" value $v \in [0, 1]$ yields expected payoff $g(v) = v^{n-1}(v_i - s(v))$.
* **Equilibrium Condition:**
  $$v_i^{n-1}(v_i - s(v_i)) \ge v^{n-1}(v_i - s(v)) \quad \text{for all } v \in [0, 1]$$
* **Calculus Derivation:**
  * Differentiate $g(v) = v^{n-1}v_i - v^{n-1}s(v)$ with respect to $v$:
    $$g'(v) = (n-1)v^{n-2}v_i - (n-1)v^{n-2}s(v) - v^{n-1}s'(v)$$
  * Set $g'(v_i) = 0$ and divide by $v_i^{n-2}$:
    $$(n-1)v_i - (n-1)s(v_i) - v_i s'(v_i) = 0 \implies \frac{d}{dv_i}\left(v_i^{n-1} s(v_i)\right) = (n-1)v_i^{n-1}$$
  * Integrating with $s(0) = 0$ gives the optimal equilibrium strategy:
    $$s(v_i) = \left(\frac{n-1}{n}\right)v_i$$
* *Insight:* As the number of bidders $n$ increases, competition intensifies, and bidders shade their bids less ($\frac{n-1}{n} \to 1$ as $n \to \infty$).

---

## Slide 35: General Distributions with $n \ge 2$ Bidders
* Suppose each bidder's value is drawn independently from an arbitrary probability distribution over $[0, \infty)$:
  * **CDF:** $F(x) = \mathbb{P}(\text{value} \le x)$ (assumed differentiable).
  * **PDF:** $f(x) = F'(x)$.
* If bidder $i$ reports value $v$, the probability that all $n - 1$ other bidders have values $\le v$ is $F(v)^{n-1}$.
* Expected payoff when reporting $v$:
  $$g(v) = F(v)^{n-1}(v_i - s(v))$$
* Taking the derivative $g'(v) = 0$ at $v = v_i$:
  $$(n-1)F(v_i)^{n-2}f(v_i)(v_i - s(v_i)) - F(v_i)^{n-1}s'(v_i) = 0$$
* Solving for $s'(v_i)$ yields the general differential equation:
  $$s'(v_i) = \frac{(n-1)\left(f(v_i)v_i - f(v_i)s(v_i)\right)}{F(v_i)}$$
* Finding $s(v_i)$ depends on the explicit formulas for $f$ and $F$ (equals $\frac{n-1}{n}v_i$ for the uniform distribution).

---

## Slide 36: Common Values & The Winner's Curse
* **Scenario:** Bidders intend to resell the item (or extract natural resources like oil rights), and the true common amount it will generate is unknown in advance.
* **Model:**
  $$V_i = V + X_i$$
  * $V$: The true (unknown) common value of the object.
  * $X_i$: A random error term representing bidder $i$'s private estimate noise (typically $\mathbb{E}[X_i] = 0$).
* *Implication (Winner's Curse):* The person who wins the auction is usually the one with the largest positive estimation error $X_i$, meaning if they bid naively without accounting for this, they will likely overpay relative to $V$.

---

## Slide 37: Seller Expected Revenue & Revenue Equivalence
* **Order Statistics Fact:** Suppose $n$ random numbers are independently and uniformly distributed on $[0, 1]$. When sorted in ascending order ($V_{(1)} \le V_{(2)} \le \dots \le V_{(n)}$), the expected value of the $k$-th position is:
  $$\mathbb{E}[V_{(k)}] = \frac{k}{n + 1}$$
  * Highest true value ($k = n$): $\mathbb{E}[V_{(n)}] = \frac{n}{n + 1}$
  * Second-highest true value ($k = n - 1$): $\mathbb{E}[V_{(n-1)}] = \frac{n - 1}{n + 1}$

* **2nd-Price Sealed-Bid Auction Expected Revenue:**
  * Everyone bids truthfully ($b_i = v_i$). The winner pays the second-highest bid ($k = n - 1$).
  $$\mathbb{E}[\text{Revenue}_{\text{2nd}}] = \mathbb{E}[V_{(n-1)}] = \frac{n - 1}{n + 1}$$

* **1st-Price Sealed-Bid Auction Expected Revenue:**
  * By our equilibrium theorem, the winning bid is $\left(\frac{n-1}{n}\right)$ times the highest true value $V_{(n)}$.
  $$\mathbb{E}[\text{Revenue}_{\text{1st}}] = \left(\frac{n - 1}{n}\right) \cdot \mathbb{E}[V_{(n)}] = \left(\frac{n - 1}{n}\right) \cdot \left(\frac{n}{n + 1}\right) = \frac{n - 1}{n + 1}$$

* **Revenue Equivalence Principle:** Both 1st-price and 2nd-price auctions yield the exact same expected revenue $\frac{n-1}{n+1}$ to the seller!