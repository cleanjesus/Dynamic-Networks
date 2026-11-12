Commands
Your program must support these four commands:

python3 relationships.py ties GRAPH.gml OUTPUT.png

python3 relationships.py balance GRAPH.gml OUTPUT.png

python3 relationships.py homophily GRAPH.gml GROUP OUTPUT.png

python3 relationships.py partition GRAPH.gml K OUTPUT.png
Examples:

python3 relationships.py ties ties.gml ties.png

python3 relationships.py balance signed.gml balance.png

python3 relationships.py homophily groups.gml blue homophily.png

python3 relationships.py partition network.gml 3 partitions.png
Every command must read a GML graph, print the required results, and create the requested PNG file.

Do not use plt.show().

1. Strong and Weak Ties
python3 relationships.py ties GRAPH.gml OUTPUT.png
Refer to the Clustering Coefficient, Neighborhood Overlap, Strong and Weak Ties, and Triadic Closure Property slides.

Each edge has:

strength "strong"
or:

strength "weak"
Calculate:

clustering coefficient of every node;

neighborhood overlap of every edge;

number of Triadic Closure Property violations.

For edge (A,B):

I = number of common neighbors of A and B
T = number of nodes neighboring A or B, excluding A and B
overlap = I / T
If T = 0, use 0.

A Triadic Closure Property violation occurs at node A when A has strong ties to both B and C, but no edge exists between B and C.

Print values to three decimal places.

Required output:

NODES <number>
EDGES <number>
CLUSTERING <node:value ...>
OVERLAP <edge:value ...>
TRIADIC_CLOSURE_VIOLATIONS <number>
GRAPH_IMAGE <filename>
Nodes and edges must appear alphabetically.

Visualization
Display:

node labels and clustering coefficients;

strong edges as solid red lines;

weak edges as dashed gray lines;

neighborhood overlap as edge labels.

2. Positive and Negative Relationships
python3 relationships.py balance GRAPH.gml OUTPUT.png
Refer to the Structural Balance slides.

The graph must be complete. Every edge has:

sign "+"
or:

sign "-"
A triangle is balanced if:

all three edges are positive, or

exactly one edge is positive.

Print:

NODES <number>
TRIANGLES <number>
BALANCED_TRIANGLES <number>
UNBALANCED_TRIANGLES <number>
STRUCTURAL_BALANCE <YES|NO>
GRAPH_IMAGE <filename>
The complete graph is structurally balanced only when every triangle is balanced.

Visualization
Display:

positive edges in green;

negative edges in red;

+ or - as edge labels;

structural-balance result in the title.

3. Homophily
python3 relationships.py homophily GRAPH.gml GROUP OUTPUT.png
Refer to the Homophily Test slides.

Every node contains:

group "<value>"
For the requested group calculate:

p = nodes in GROUP / total nodes
Count cross-group edges and calculate:

cross_fraction = cross_edges / total_edges
expected = 2 * p * (1 - p)
For this assignment, report evidence of homophily when:

cross_fraction < expected
Required output:

NODES <number>
EDGES <number>
GROUP <group>
GROUP_PROPORTION <value>
CROSS_EDGES <number>
CROSS_EDGE_FRACTION <value>
EXPECTED_CROSS_FRACTION <value>
HOMOPHILY <YES|NO>
GRAPH_IMAGE <filename>
Print fractions to three decimal places.

Visualization
Display:

different colors for different groups;

node label and group;

same-group edges as solid gray;

cross-group edges as dashed red;

homophily result in the title.

4. Graph Partition
python3 relationships.py partition GRAPH.gml K OUTPUT.png
Refer to the Betweenness and graph-partitioning material in the Strong and Weak Ties slides.

K is the requested number of connected components.

Use the divisive procedure from the lecture:

Calculate edge betweenness.

Find an edge having maximum edge betweenness.

Remove that edge.

Recalculate edge betweenness.

Repeat until the graph contains K connected components.

Use:

nx.edge_betweenness_centrality(
    G,
    normalized=False
)
When multiple edges have the same maximum betweenness, choose the alphabetically first edge. Alphabetize the two endpoints first.

For example:

A-D
A-F
B-C
would select A-D.

Required output:

NODES <number>
EDGES <original number>
REQUESTED_PARTITIONS <K>
PARTITIONS <number>
REMOVED_EDGES <u-v ...>
PARTITION_1 <nodes ...>
PARTITION_2 <nodes ...>
...
GRAPH_IMAGE <filename>
Nodes within each partition must be alphabetical.

Order partitions according to the alphabetically first node in each partition.

Visualization
The PNG must display:

each final partition using a different node color;

node labels;

edges remaining after partitioning as solid gray;

removed edges as dashed red edges.

The title must contain:

Graph Partition: K=<number>
Error Handling
Terminate with a nonzero exit status for:

unknown commands;

incorrect number of arguments;

nonexistent GML files;

directed graphs;

missing or invalid strength;

missing or invalid sign;

a non-complete graph passed to balance;

missing group;

a requested homophily group that does not exist;

K < 1;

K > number of nodes;

an input graph that already contains more than K components.

Submit  (do not submit zip files):
relationships.py
All operations must use command-line arguments. Interactive menus and input() are prohibited.