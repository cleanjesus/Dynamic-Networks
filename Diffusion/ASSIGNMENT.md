Diffusion
Due: Tue Dec 1, 2026 11:59pm
5 Points Possible
Unlimited Attempts Allowed

Submit:

diffusion.py

Interactive menus and input() are prohibited.

Commands
python3 diffusion.py epidemic GRAPH.gml P INFECTIOUS_PERIOD SEED INITIAL OUTPUT.png

python3 diffusion.py behavior GRAPH.gml A B INITIAL OUTPUT.png

python3 diffusion.py information GRAPH.gml OUTPUT.png

python3 diffusion.py smallworld GRAPH.gml OUTPUT.png

Examples:

python3 diffusion.py epidemic contact.gml 0.40 2 427 A epidemic.png

python3 diffusion.py behavior social.gml 3 2 A,B behavior.png

python3 diffusion.py information signals.gml information.png

python3 diffusion.py smallworld smallworld.gml smallworld.png

INITIAL is a comma-separated list of node names.

1. epidemic
python3 diffusion.py epidemic GRAPH.gml P INFECTIOUS_PERIOD SEED INITIAL OUTPUT.png

Refer to the Contact Network, SIR Epidemic Model, and Basic Reproductive Number slides. The slides model people as nodes, disease-spreading contacts as edges, and nodes as Susceptible, Infectious, or Removed. Use a synchronous SIR simulation.

At each step:

Every infectious node attempts to infect each susceptible neighbor independently with probability P;

Use random.Random(SEED);

Process nodes and neighbors alphabetically;

An infectious node becomes removed after INFECTIOUS_PERIOD steps;

Newly infected nodes begin spreading in the next step;

Stop when no infectious nodes remain.

Report:

R0 = P * average_degree

Print P and R0 to three decimal places.

Required output:

NODES <number>
EDGES <number>
P <value>
INFECTIOUS_PERIOD <number>
R0 <value>
INITIAL_INFECTED <nodes>
STEPS <number>
SUSCEPTIBLE <number>
REMOVED <number>
EVER_INFECTED <nodes>
GRAPH_IMAGE <filename>

Display
Show final states:

Susceptible in light blue;

Removed (previously infected) in red;

Node labels;

A title containing the R0 value.

2. behavior
python3 diffusion.py behavior GRAPH.gml A B INITIAL OUTPUT.png

Refer to the Networked Coordination Game, Decision Rule, and Switching from B to A slides.

Threshold:

q = b / (a + b)

Nodes listed in INITIAL start with behavior A. All other nodes start with behavior B.

At every synchronous round, a B node permanently adopts A if:

(neighbors using A) / (number of neighbors) >= q

Break equality in favor of A. Stop when no additional node changes. A complete cascade means every node adopts A.

Print THRESHOLD to three decimal places.

Required output:

NODES <number>
EDGES <number>
THRESHOLD <value>
INITIAL_ADOPTERS <nodes>
ROUNDS <number>
FINAL_ADOPTERS <nodes>
ADOPTER_COUNT <number>
COMPLETE_CASCADE <YES|NO>
GRAPH_IMAGE <filename>

Display
Show:

Initial adopters in red;

Nodes added by the cascade in orange;

Remaining B nodes in light blue;

A title containing the threshold and complete-cascade result.

3. information
python3 diffusion.py information GRAPH.gml OUTPUT.png

Refer to the Simple Cascade Model, Signals, and Information Cascades slides. People make sequential decisions from private information and earlier decisions. Signals are H and L.

Each node contains:

order <integer>
signal "H" or "L"

Order values must be unique.

Use the symmetric cascade model:

Start with public evidence 0;

An observed H contributes +1;

An observed L contributes -1;

While public evidence is between -1 and 1, each person follows their private signal;

Once public evidence reaches +2, later people choose ACCEPT regardless of their signals;

Once public evidence reaches -2, later people choose REJECT regardless of their signals;

Decisions made after a cascade begins do not contribute new evidence.

People must appear sorted by increasing order.

Required output:

PEOPLE <number>
SIGNALS <node:H|L ...>
DECISIONS <node:ACCEPT|REJECT ...>
CASCADE_START <order|NONE>
CASCADE_ACTION <ACCEPT|REJECT|NONE>
GRAPH_IMAGE <filename>

Display
Show:

Directed observation edges;

H nodes in light green;

L nodes in light red;

Node labels containing order, signal, and decision;

Orange borders on nodes that act after a cascade begins.

4. smallworld
python3 diffusion.py smallworld GRAPH.gml OUTPUT.png

Refer to the Watts–Strogatz Model, Homophily, and Weak Ties slides. Dense local connections create triangles; long-range weak ties produce short paths.

Every edge contains:

type "local"
or:

type "weak"

Calculate:

average clustering coefficient and average shortest-path length on the full graph;

the same two values after removing all weak edges.

PATH_REDUCTION = LOCAL_AVG_PATH - FULL_AVG_PATH

Print values to three decimal places.

Required output:

NODES <number>
EDGES <number>
WEAK_TIES <number>
FULL_CLUSTERING <value>
LOCAL_CLUSTERING <value>
FULL_AVG_PATH <value>
LOCAL_AVG_PATH <value>
PATH_REDUCTION <value>
GRAPH_IMAGE <filename>

Display
Show:

Local edges as solid gray;

Weak ties as dashed red;

Node labels;

A title containing the full and local-only average path lengths.

Error Handling
Terminate with a nonzero status for:

invalid commands;

missing arguments;

nonexistent files;

directed graphs where an undirected graph is required;

invalid P;

invalid infectious period;

nonexistent initial nodes;

invalid A or B;

invalid signals/orders;

disconnected small-world graphs;

missing edge type;

a small-world local-only graph that is disconnected.

Rubric (Assignment 6)
SIR epidemic simulation and R0                        1.25 pts
Behavioral threshold cascade                          1.25 pts
Sequential information cascade                        1 pt
Small-world clustering/path analysis                  0.75 pts
PNG display, CLI, output format, error handling       0.75 pts
Total                                                 5 pts
