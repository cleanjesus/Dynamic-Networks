# Information Cascades
**Course:** CECS 427 Dynamic Networks  
**Instructor:** Oscar Morales Ponce

---

## Slide 1: Title Slide
* **Title:** Information Cascades
* **Course:** CECS 427 Dynamic Networks
* **Author:** Oscar Morales Ponce

---

## Slide 2: Fashion Trends: Herding and Cascades
* **Core Concept:** Fashion trends often catch on simply because others are wearing them, not necessarily because they are appealing initially.
* **Visual Context:** An image of an ornate, unconventional floral-patterned high-heeled shoe with an orange ribbon lace, illustrating a distinctive fashion item that might spread via herding behavior rather than intrinsic initial appeal.

---

## Slide 3: Political and Social Movements
* **Core Concept:** Large-scale political movements often emerge as individuals join because they observe widespread participation.
* **Visual Context:** 
  1. Left Image: Multiple raised hands of different skin tones with "ME TOO" and "#metoo" written on the palms.
  2. Right Image: A crowd of protesters wearing masks holding signs reading "BLACK LIVES MATTER".

---

## Slide 4: Following the Crowd
* **Core Concept:** When people are connected by a network, it becomes possible for them to influence each other's behavior and decisions:
  * In the opinions they hold
  * The products they buy
  * The political positions they support
  * The activities they pursue
  * The technologies they use
* **Key Question:** Why do such influences occur?
* **Visual Context:** 
  1. A pink network graph icon showing 6 user nodes connected by edges (representing network structure).
  2. An icon of two purple user silhouettes with a question mark speech bubble above them (representing interpersonal inquiry/influence).

---

## Slide 5: Choosing a Restaurant: Information Cascade Example
* **Scenario:** Imagine you're traveling to a new city and looking for dinner. Your research suggests Restaurant A is excellent, but when you arrive, it's empty while Restaurant B next door is packed. Trusting the collective judgment of others, you follow the crowd to Restaurant B.
* **Visual Context:** Screenshots of online review interfaces (Google Reviews showing a 4.2-star rating summary and a "Write a review" button; a mobile restaurant photo gallery and review interface), illustrating private research vs. public crowd observation.

---

## Slide 6: Information Cascades: Imitation
* **Core Concept:** 
  * Individuals in a cascade are imitating the behavior of others.
  * Imitation may also occur due to social pressure to conform, without any underlying informational cause.

---

## Slide 7: Observing the Sky: Herding Behavior Example
* **Core Concept:** When people on a street start looking upward, passersby follow, even if nothing is there.
* **Visual Context:** 
  1. Top Image: A group of 8 diverse people staring intently upward at the sky.
  2. Bottom Image: A TikTok compilation screenshot titled "DANCE CHALLENGE" showing multiple groups of teenagers performing synchronized choreography.

---

## Slide 8: Explanations / Interpretations
* **Social Force:** A social force for conformity that grows stronger as the group conforming to the activity becomes larger.
* **Mechanism:** A possible mechanism giving rise to the conformity observed in this kind of situation is rooted in the idea of **information cascades**.
* **Examples of Herding:**
  * Fashions and fads
  * Voting for popular candidates
  * Success of books placed highly on best-seller lists
  * Spread of technological choice by consumers and firms
  * Localized nature of crime and political movements, etc.

---

## Slide 9: Technology Adoption: Cascades in Tech
* **Core Concept:** Technological products or services often spread rapidly due to visibility and peer adoption.
* **Visual Context:** 
  1. Top Image: The Discord logo on a dark blue background.
  2. Bottom Image: A smartphone displaying a WhatsApp integration with OpenAI's ChatGPT, showing automated recipe generation.

---

## Slide 10: Why Imitate the Behavior of Others?
* **Direct-Benefit Effects (Network Effects):**
  * Because there is a direct benefit to you from aligning your behavior with their behavior.
  * *Examples:* Mac or Windows, Social network apps (Discord).
  * The actions of others are affecting payoffs directly, rather than indirectly by changing information.
* **Combined Effects:** Many decisions exhibit both **information** and **direct-benefit** effects.

---

## Slide 11: A Herding Experiment
* **Setup:** A simple herding experiment is performed in a classroom with a large group of students where a decision is to be made.
* **Rules / Conditions:**
  1. **Sequential Decisions:** People make the decision sequentially, and each person can observe the choices made by those who acted earlier.
  2. **Private Information:** Persons have some private information guiding their decision.
  3. **Inference from Actions:** A person cannot directly observe the private information that other people know, but can make inferences about this private information from what they do.

---

## Slide 12: A Herding Experiment (Urn Setup)
* **Physical Setup:** Experimenter puts an urn at the front of the room with 3 marbles hidden in it.
* **Prior Distribution:** Announces that there is:
  * A $50\%$ chance that the urn contains two red marbles and one blue marble (**"majority-red" urn**), and
  * A $50\%$ chance the urn contains two blue marbles and one red marble (**"majority-blue" urn**).
* **Visual Diagram (Urn Configurations):**
  * **Left Box (Majority-Red Urn):** Contains 1 Blue circle and 2 Red circles.
  * **Right Box (Majority-Blue Urn):** Contains 2 Blue circles and 1 Red circle.

---

## Slide 13: Assumptions
* **Process:** One by one, each student comes to the front of the room; draws a marble from the urn; looks at the color and then places it back in the urn without showing it to the rest of the class.
* **Action:** The student then guesses whether the urn is majority-red or majority-blue and publicly announces this guess to the class.
* **Information Asymmetry (Key to the set-up):** The students who have not yet had their turn do not get to see which colors the earlier students draw, but they do get to hear the guesses that are being made.
* **Rationality Assumption:** We also assume that all students reason correctly about what to do when it is their turn to guess, using everything they have heard so far.

---

## Slide 14: Power of Rationality: What Do We Expect to Happen?
* **Question:** Is there a decision-making model to argue under uncertainty?
* **Sequential Student Logic:**
  * **1st Student:** If he sees a red marble, it is better to guess that the urn is majority-red; and if he sees a blue marble, it is better to guess that the urn is majority-blue.
  * **2nd Student:** If she sees the same color as the 1st, then she guesses this color as well; else she is indifferent (typically breaks tie in favor of her own private draw).
  * **3rd Student:** If the first two students have guessed opposite colors, then she should guess the color she sees; **else she should guess the color chosen by the previous two, regardless of which color she draws from the urn** (Cascade begins!).
  * **$k$-th Student:** Follows the cascade logic, etc.
* **Key Question:** How do we justify the answers above?

---

## Slide 15: Conditional Probability
* **Mathematical Question:** To understand what happens we must answer mathematically the question: *"What is the probability this is the better restaurant, given the reviews I've read and the crowds I see in each one?"*
* **Formulas:** Conditional Probability for events $A, B$:
  $$\Pr[A \mid B] = \frac{\Pr[A \cap B]}{\Pr[B]}$$
  $$\Pr[B \mid A] = \frac{\Pr[B \cap A]}{\Pr[A]}$$
* **Visual Diagram (Venn Diagram):**
  * Two overlapping circles inside a rectangular sample space.
  * Left circle labeled $A$; right circle labeled $B$.
  * The intersection lens in the middle is shaded and labeled $B \cap A$.

---

## Slide 16: Bayes' Rule
* **Derivation:** For events $A, B$:
  $$\Pr[A \mid B]\Pr[B] = \Pr[A \cap B] = \Pr[B \mid A]\Pr[A]$$
* **Dividing by $\Pr[B]$:**
  $$\Pr[A \mid B] = \frac{\Pr[A]\Pr[B \mid A]}{\Pr[B]}$$
* **Definitions:**
  * $\Pr[A]$: **Prior probability** of $A$
  * $\Pr[A \mid B]$: **Posterior probability** of $A$ now that we know $B$ has occurred

---

## Slide 17: Eyewitness Testimony: Cascades in Legal Contexts
* **Concept:** Witnesses can be influenced by prior testimony, leading to information cascades and potential inaccuracies.
* **Real-life Example:** Misidentification in criminal cases where witnesses align testimonies unintentionally.

---

## Slide 18: Example of Bayes' Rule: Eyewitness Testimony (Setup)
* **Base Rates (Priors):** Suppose that in some city $80\%$ of taxi cabs are black and the remaining $20\%$ are yellow.
* **Incident:** A witness to a hit-and-run accident involving a taxi states that the cab involved was yellow.
* **Witness Accuracy (Likelihoods):** Suppose that eyewitness testimony is imperfect in the sense that witnesses sometimes misidentify the colors of cabs:
  * If a taxi is yellow, then a witness will claim it is yellow after the fact $80\%$ of the time.
  * If it is black, they will claim it is black $80\%$ of the time (meaning they falsely claim it is yellow $20\%$ of the time).
* **Problem:** Interpreting eyewitness testimony is a question of conditional probability: what is the probability the cab is yellow (or black), given that the witness says it is yellow?

---

## Slide 19: Example of Bayes' Rule: Eyewitness Testimony (Formulation)
* **Given Probabilities:**
  * $\Pr[\text{Report} = Y \mid \text{True} = Y] = 0.8$ (accuracy of eyewitness)
  * $\Pr[\text{True} = Y] = 0.2$ (frequency of yellow taxi cabs)
* **Target Probability:**
  $$\Pr[\text{True} = Y \mid \text{Report} = Y] = \frac{\Pr[\text{True} = Y]\Pr[\text{Report} = Y \mid \text{True} = Y]}{\Pr[\text{Report} = Y]}$$
  *(Note: Slide contains a minor typo in the denominator written as $\Pr[\text{Report} = \text{True}]$, which represents $\Pr[\text{Report} = Y]$).*
* **Numerator Calculation:**
  $$\Pr[\text{True} = Y]\Pr[\text{Report} = Y \mid \text{True} = Y] = 0.2 \cdot 0.8 = 0.16$$

---

## Slide 20: Denominator Calculation
* **Total Probability of Reporting Yellow:** There are two ways for a witness to report the cab is yellow:
  1. **The cab is truly yellow:**
     $$\Pr[\text{true} = Y] \cdot \Pr[\text{report} = Y \mid \text{true} = Y] = 0.2 \cdot 0.8 = 0.16$$
  2. **The cab is truly black:**
     $$\Pr[\text{true} = B] \cdot \Pr[\text{report} = Y \mid \text{true} = B] = 0.8 \cdot 0.2 = 0.16$$
* **Sum (Law of Total Probability):** The probability of a report of yellow is the sum of these two probabilities:
  $$\Pr[\text{report} = Y] = \Pr[\text{true} = Y]\Pr[\text{report} = Y \mid \text{true} = Y] + \Pr[\text{true} = B]\Pr[\text{report} = Y \mid \text{true} = B]$$
  $$\Pr[\text{report} = Y] = 0.2 \cdot 0.8 + 0.8 \cdot 0.2 = 0.32$$

---

## Slide 21: Spam Filtering: Bayesian Cascades
* **Concept:** Email filtering systems use Bayesian methods to identify spam based on probability and user feedback.
* **Real-life Example:** Gmail spam detection, continuously learning from user-marked spam or safe emails.

---

## Slide 22: Check Your Knowledge: Spam Filtering (Problem Statement)
* **Scenario:** Suppose you receive a piece of e-mail whose subject line contains the phrase `"check this out"` (a popular phrase among spammers).
* **Question:** Based just on this (and without looking at the sender or the message content), what is the chance the message is spam?
* **Given Data:**
  * $40\%$ of all your e-mail is spam and the remaining $60\%$ is e-mail you want to receive.
  * $1\%$ of all spam messages contain the phrase `"check this out"` in their subject lines, while $0.4\%$ of all non-spam messages contain this phrase.

---

## Slide 23: Everything Together (Eyewitness Conclusion)
* *(Note: This slide concludes the calculation from Slides 18–20)*
* **Final Posterior Calculation:**
  $$\Pr[\text{true} = Y \mid \text{report} = Y] = \frac{\Pr[\text{true} = Y] \cdot \Pr[\text{report} = Y \mid \text{true} = Y]}{\Pr[\text{report} = Y]}$$
  $$= \frac{0.2 \cdot 0.8}{0.32} = 0.5$$

---

## Slide 24: Check Your Knowledge (Spam Filtering Setup)
* **Events:**
  * $S$: Message is spam
  * $C$: Message contains `"check this out"`
* **Probabilities:**
  * $\Pr[S] = 0.4$ (and consequently $\Pr[\sim S] = 0.6$)
  * $\Pr[C \mid S] = 0.01$
  * $\Pr[C \mid \sim S] = 0.004$
* **Formula to Determine:**
  $$\Pr[S \mid C] = \frac{\Pr[S]\Pr[C \mid S]}{\Pr[C]}$$
  *(Supplementary Solution for Context: $\Pr[C] = (0.4)(0.01) + (0.6)(0.004) = 0.004 + 0.0024 = 0.0064$. Thus, $\Pr[S \mid C] = \frac{0.004}{0.0064} = 0.625$ or $62.5\%$.)*

---

## Slide 25: Herding Experiment (Formalizing Probabilities)
* **Goal:** Each student is trying to estimate the conditional probability that the urn is majority-blue or majority-red, given what she has seen and heard.
* **Known Priors and Likelihoods:**
  $$\Pr[\text{Majority-Blue}] = \Pr[\text{Majority-Red}] = \frac{1}{2}$$
  $$\Pr[\text{Blue} \mid \text{Majority-Blue}] = \Pr[\text{Red} \mid \text{Majority-Red}] = \frac{2}{3}$$
* **Event Notation:**
  * $B$: Blue draw, $M\text{-}B$ (or $MB$): Majority-Blue urn
  * $R$: Red draw, $M\text{-}R$ (or $MR$): Majority-Red urn

---

## Slide 26: Herding Experiment (Decision Rule)
* **Optimization Rule:** To maximize her chance for guessing correctly, a student should:
  * Guess **majority-blue** if:
    $$\Pr[\text{Majority-Blue} \mid \text{what she has seen and heard}] > \frac{1}{2}$$
  * Guess **majority-red** if:
    $$\Pr[\text{Majority-Blue} \mid \text{what she has seen and heard}] < \frac{1}{2}$$
  * If the two conditional probabilities are both exactly $\frac{1}{2}$, then it doesn't matter what she guesses.
* **1st Student Scenario:** Suppose that the first student draws a blue marble. He wants to determine $\Pr[M\text{-}B \mid B]$.

---

## Slide 27: Using Bayes' Rule: Decision of 1st Student
* **Calculate Marginal Probability $\Pr[B]$:**
  $$\Pr[B] = \Pr[M\text{-}B]\Pr[B \mid M\text{-}B] + \Pr[M\text{-}R]\Pr[B \mid M\text{-}R]$$
  $$\Pr[B] = \left(\frac{1}{2}\right)\left(\frac{2}{3}\right) + \left(\frac{1}{2}\right)\left(\frac{1}{3}\right) = \frac{1}{2}$$
* **Calculate Posterior Probability $\Pr[M\text{-}B \mid B]$:**
  $$\Pr[M\text{-}B \mid B] = \frac{\Pr[M\text{-}B] \cdot \Pr[B \mid M\text{-}B]}{\Pr[B]} = \frac{\left(\frac{1}{2}\right)\left(\frac{2}{3}\right)}{\frac{1}{2}} = \frac{2}{3}$$
* **Conclusion for 1st Student:** Since $\frac{2}{3} > \frac{1}{2}$, if he sees a blue marble, it is better to guess that the urn is majority-blue, and (similarly), if he sees a red marble, it is better to guess that the urn is majority-red.
* **2nd Student:** Similar argument applies for the 2nd student (their guess reveals their private signal if they break ties by guessing their own draw).

---

## Slide 28: Using Bayes' Rule: Decision of 3rd Student
* **Scenario:** Assume the first two students have announced guesses of **Blue** (from which the 3rd student infers their draws were $B, B$), and the third student draws a **Red** marble ($R$).
* **Goal:** 3rd student wants to know $\Pr[M\text{-}B \mid B, B, R]$.
* **Calculations:**
  * Likelihood given Majority-Blue:
    $$\Pr[B, B, R \mid M\text{-}B] = \left(\frac{2}{3}\right)\left(\frac{2}{3}\right)\left(\frac{1}{3}\right) = \frac{4}{27}$$
  * Total Probability $\Pr[B, B, R]$:
    $$\Pr[B, B, R] = \Pr[M\text{-}B] \cdot \Pr[B, B, R \mid M\text{-}B] + \Pr[M\text{-}R] \cdot \Pr[B, B, R \mid M\text{-}R]$$
    $$= \left(\frac{1}{2}\right)\left(\frac{2}{3}\right)\left(\frac{2}{3}\right)\left(\frac{1}{3}\right) + \left(\frac{1}{2}\right)\left(\frac{1}{3}\right)\left(\frac{1}{3}\right)\left(\frac{2}{3}\right) = \frac{4}{54} + \frac{2}{54} = \frac{6}{54} = \frac{1}{9}$$
  * Posterior Probability:
    $$\Pr[M\text{-}B \mid B, B, R] = \frac{\Pr[M\text{-}B]\Pr[B, B, R \mid M\text{-}B]}{\Pr[B, B, R]} = \frac{\left(\frac{4}{27}\right)\left(\frac{1}{2}\right)}{\frac{1}{9}} = \frac{\frac{2}{27}}{\frac{3}{27}} = \frac{2}{3}$$
* **Result:** Even though the 3rd student drew a Red marble, $\Pr[M\text{-}B \mid B, B, R] = \frac{2}{3} > \frac{1}{2}$, so rational choice dictates guessing **Majority-Blue** (ignoring their own private signal).

---

## Slide 29: A Cascade Model
* **Generalization:** A Simple Cascade Model: Sequential Decision Making.
* **Purpose:** Formulate a model whereby people are making decisions sequentially, basing these decisions on:
  * A combination of their own private information, and
  * Observations of what earlier people have done.
* **Structure:** A group of people (numbered $1, 2, 3, \dots$) make decisions sequentially.
* **Three Main Ingredients of the Model:**
  1. **States**
  2. **Payoffs**
  3. **Signals**

---

## Slide 30: Ingredient 1: States
* **World States:** Each individual knows the world is either in state:
  * $G$ (**Good**), or
  * $B$ (**Bad**).
* **Prior Probabilities:**
  * It is in state $G$ with probability $p$.
  * It is in state $B$ with probability $1 - p$.
  * Formally:
    $$\Pr[G] = p$$
    $$\Pr[B] = 1 - \Pr[G] = 1 - p$$

---

## Slide 31: Ingredient 2: Payoffs
* **Decision:** Each individual chooses either the **reject** option or the **accept** option. Payoff for accepting depends on the option being a good or bad idea.
* **Valuations ($v_g, v_b$):**
  * If individual chooses the **reject** option: she receives payoff $0$.
  * If individual chooses the **accept** option:
    * If option is a good idea (State $G$), then payoff is a positive number: $v_g > 0$.
    * If option is a bad idea (State $B$), then payoff is a negative number: $v_b < 0$.

---

## Slide 32: Expected Payoffs
* **Formula:** The expected payoff of accepting prior to receiving any signal is:
  $$E[\text{Payoff}] := v_g p + v_b(1 - p)$$
* **Indifference Assumption:** We assume that the expected payoff from accepting in the absence of other information is equal to $0$.
  * That is, before an individual gets any additional information, the expected payoff from accepting is the same as the payoff from rejecting.
  * Formally:
    $$v_g p + v_b(1 - p) = 0$$

---

## Slide 33: Ingredient 3: Signals
* **Role of Signals:** Signals model the effect of private information.
* **Mechanism:** Each individual gets a private signal that provides information about whether accepting is a good idea or a bad idea.
* **Two Possible Signals:**
  * $H$ (**High**): suggesting that accepting is a good idea.
  * $L$ (**Low**): suggesting that accepting is a bad idea.

---

## Slide 34: Signals (Conditional Probabilities)
* **Signal Accuracy ($q$):**
  * If accepting is a **good idea ($G$)**, then high signals are more frequent than low:
    $$\Pr[H \mid G] = q > \frac{1}{2}, \quad \Pr[L \mid G] = 1 - q < \frac{1}{2}$$
  * If accepting is a **bad idea ($B$)**, then low signals are more frequent than high:
    $$\Pr[L \mid B] = q > \frac{1}{2}, \quad \Pr[H \mid B] = 1 - q < \frac{1}{2}$$
* **Summary Matrix (Signal vs. State Likelihoods):**

| Signals \ States | State $B$ (Bad) | State $G$ (Good) |
| :--- | :---: | :---: |
| **Signal $L$ (Low)** | $q$ | $1 - q$ |
| **Signal $H$ (High)** | $1 - q$ | $q$ |

---

## Slide 35: Herding in the Cascade Model (Mapping the Experiment)
* **Mapping Urn Experiment to the General Cascade Model:**
  * **States:** The two possible states of the world are that the urn placed at the front of the room was $MB$ (Majority-Blue), or that it was $MR$ (Majority-Red).
  * **Action:** We can think of "accepting" as guessing $MB$; this is a good idea ($G$) if the true urn really is $MB$ and a bad idea ($B$) otherwise.
  * **Prior ($p$):** The prior probability of accepting being a good idea is $p = \frac{1}{2}$.
  * **Signal ($H/L$) and Precision ($q$):** The private information in the experiment is the color of the ball the individual draws; it's a "high" signal ($H$) if it is Blue, and:
    $$\Pr[H \mid G] = \Pr[B \mid M\text{-}B] = q = \frac{2}{3}$$

---

## Slide 36: How Do We Make Individual Decisions? (Part 1)
* **Scenario:** Suppose that a person gets a high signal ($H$).
* **Payoff Shift:** This shifts their expected payoff from:
  $$v_g \Pr[G] + v_b \Pr[B] = 0$$
  to:
  $$v_g \Pr[G \mid H] + v_b \Pr[B \mid H]$$

---

## Slide 37: How Do We Make Individual Decisions? (Part 2)
* **Posterior Probability of State $G$ Given Signal $H$:** Using Bayes' Rule:
  $$\Pr[G \mid H] = \frac{\Pr[G]\Pr[H \mid G]}{\Pr[H]}$$
  $$= \frac{\Pr[G]\Pr[H \mid G]}{\Pr[G] \cdot \Pr[H \mid G] + \Pr[B] \cdot \Pr[H \mid B]} = \frac{pq}{pq + (1 - p)(1 - q)}$$
* **Inequality Comparison:**
  $$\frac{pq}{pq + (1 - p)(1 - q)} > p = \Pr[G]$$
  where the last inequality is true because:
  $$pq + (1 - p)(1 - q) < pq + (1 - p)q = q \iff (1 - p)(1 - q) < (1 - p)q \iff 1 - q < q \iff q > \frac{1}{2}$$

---

## Slide 38: How Do We Make Individual Decisions? (Part 3)
* **Posterior Probability of State $B$ Given Signal $H$:** Using Bayes' Rule:
  $$\Pr[B \mid H] = \frac{\Pr[B]\Pr[H \mid B]}{\Pr[H]}$$
  $$= \frac{\Pr[B] \cdot \Pr[H \mid B]}{\Pr[G] \cdot \Pr[H \mid G] + \Pr[B] \cdot \Pr[H \mid B]} = \frac{(1 - p)(1 - q)}{pq + (1 - p)(1 - q)}$$
* **Inequality Comparison:**
  $$\frac{(1 - p)(1 - q)}{pq + (1 - p)(1 - q)} < 1 - p = \Pr[B]$$
  *(Note: Slide text displays a typo `> 1 - p = Pr[B]`, but mathematically and contextually on Slide 39, $\Pr[B \mid H] < 1 - p$ because $\Pr[G \mid H] + \Pr[B \mid H] = 1$ and $\Pr[G \mid H] > p$. The slide's justification line below confirms the denominator is larger than $(1-q)$:)*
  $$p(1 - q) + (1 - p)(1 - q) < pq + (1 - p)q \iff q > \frac{1}{2}$$

---

## Slide 39: How Do We Make Individual Decisions? (Conclusion)
* **Decision Summary:**
  * A high signal ($H$) is more likely to occur if the option is good than if it is bad; the expected payoff shifts from $0$ to **positive** (so the individual should **accept**).
  * Similarly, if the individual receives a low signal ($L$), the expected payoff shifts to **negative**, so they should **reject** the option.

---

## Slide 40: Multiple Signals
* **Reasoning Over Sequences:** Using Bayes' Rule, one can reason about an individual's decision when observing multiple signals.
* **Recall Signal Probabilities:**
  * Good idea ($G$): $\Pr[H \mid G] = q > \frac{1}{2}, \quad \Pr[L \mid G] = 1 - q < \frac{1}{2}$
  * Bad idea ($B$): $\Pr[L \mid B] = q > \frac{1}{2}, \quad \Pr[H \mid B] = 1 - q < \frac{1}{2}$
* **Sequence Definition:** Suppose that an individual gets a sequence $S$ of independently generated signals $H, L$ consisting of:
  * $a$ **high signals** ($H$), and
  * $b$ **low signals** ($L$), interleaved in some fashion (e.g., `H H L H H L H H L`).

---

## Slide 41: Multiple Signals: Theorem 1
* **Theorem 1:**
  1. The posterior probability $\Pr[G \mid S]$ is **greater** than the prior $\Pr[G]$ when $a > b$.
  2. The posterior probability $\Pr[G \mid S]$ is **less** than the prior $\Pr[G]$ when $a < b$.
  3. The two probabilities $\Pr[G \mid S]$ and $\Pr[G]$ are **equal** when $a = b$.
* **Application of Bayes' Rule:**
  $$\Pr[G \mid S] = \frac{\Pr[G]\Pr[S \mid G]}{\Pr[S]} \quad \text{and} \quad \Pr[B \mid S] = \frac{\Pr[B] \cdot \Pr[S \mid B]}{\Pr[S]}$$

---

## Slide 42: Calculations (Multiple Signals - Part 1)
* **Independence of Signals:** Since the signals are generated independently:
  $$\Pr[S \mid G] = q^a(1 - q)^b \quad \text{and} \quad \Pr[S \mid B] = (1 - q)^a q^b$$
* **Computing Marginal $\Pr[S]$:** We consider that $S$ can arise if the option is a good idea or a bad idea, so:
  $$\Pr[S] = \Pr[G]\Pr[S \mid G] + \Pr[B]\Pr[S \mid B]$$
  $$\Pr[S] = p q^a(1 - q)^b + (1 - p)(1 - q)^a q^b$$

---

## Slide 43: Calculations (Multiple Signals - Part 2)
* **Posterior Expression:**
  $$\Pr[G \mid S] = \frac{\Pr[G] \cdot \Pr[S \mid G]}{\Pr[S]} = \frac{p q^a(1 - q)^b}{p q^a(1 - q)^b + (1 - p)(1 - q)^a q^b}$$
* **Comparison to Prior $p := \Pr[G]$:**
  * If we replace the second term in the denominator above by $(1 - p)q^a(1 - q)^b$, the fraction becomes:
    $$\frac{p q^a(1 - q)^b}{p q^a(1 - q)^b + (1 - p)q^a(1 - q)^b} = p$$

---

## Slide 44: Calculations (Multiple Signals - Part 3)
* **Equivalence Chain:** We have:
  $$\Pr[G \mid S] > \Pr[G]$$
  $$\iff (1 - p)q^a(1 - q)^b > (1 - p)(1 - q)^a q^b$$
  $$\iff q^a(1 - q)^b > (1 - q)^a q^b$$
  $$\iff \left(\frac{q}{1 - q}\right)^a > \left(\frac{q}{1 - q}\right)^b$$
  *(Note: Slide formats the exponents $a$ and $b$ inline as $(\frac{q}{1-q})a > (\frac{q}{1-q})b$, which algebraically represents raising $\frac{q}{1-q}$ to powers $a$ and $b$).*
* **Conclusion:** Since $q > \frac{1}{2}$, we know $\frac{q}{1 - q} > 1$. Therefore, we have the following:
  1. If $a > b$, then since $q > \frac{1}{2}$ we have $\Pr[G \mid S] > p = \Pr[G]$.
  2. If $a < b$, then since $q > \frac{1}{2}$ we have $\Pr[G \mid S] < p = \Pr[G]$ *(Slide typo says $= \Pr[B]$, means $\Pr[G]$)*.
  3. If $a = b$, then we have $\Pr[G \mid S] = p = \Pr[G]$.

---

## Slide 45: Lessons from Cascades
1. **Cascades can be wrong:** (e.g., If the first two students draw blue marbles from a majority-red urn—which happens with probability $\frac{1}{3} \times \frac{1}{3} = \frac{1}{9}$—everyone subsequent will guess Majority-Blue).
2. **Cascades can be based on very little information:** (Public signals stop accumulating once a cascade begins, so a crowd of 1,000 people in a cascade contains no more independent information than the first 2 people).
3. **Cascades are fragile:** (Because they are based on very little information, revealing just a small amount of new public information—such as a student publicly showing their marble—can easily shatter the cascade).

---

## Slide 46: Summary: Key Points
* Information cascades occur when decisions rely heavily on observing others.
* Herding can lead to rapid adoption but also propagate misinformation.
* Real-world examples include restaurant choices, fashion, tech adoption, political movements, and even spam filtering.
* Understanding cascades can help improve decision-making and avoid pitfalls.