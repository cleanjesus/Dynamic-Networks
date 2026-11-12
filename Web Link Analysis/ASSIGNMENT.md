Web Link Analysis
Due: Sat Nov 14, 2026 11:59pm
5 Points Possible
Unlimited Attempts Allowed

Submit:

web.py

Interactive menus and input() are prohibited.

Commands
python3 web.py structure GRAPH.gml OUTPUT.png

python3 web.py hits GRAPH.gml K OUTPUT.png

python3 web.py pagerank GRAPH.gml K S OUTPUT.png

Examples:

python3 web.py structure web.gml structure.png

python3 web.py hits web.gml 5 hits.png

python3 web.py pagerank web.gml 10 0.85 pagerank.png

1. structure
python3 web.py structure GRAPH.gml OUTPUT.png

Refer to the Web Pages, In-Degree, Out-Degree, Graph Structure in the Web, and Bow-Tie Structure slides. Web links are directed edges.

Calculate:

number of nodes;

number of directed edges;

in-degree of every node;

out-degree of every node;

number of strongly connected components;

sizes of the strongly connected components;

nodes in the largest strongly connected component.

Required output:

NODES <number>
EDGES <number>
IN_DEGREES <node:value ...>
OUT_DEGREES <node:value ...>
SCC_COUNT <number>
SCC_SIZES <sizes>
LARGEST_SCC <nodes>
GRAPH_IMAGE <filename>

Sort nodes alphabetically. Sort component sizes from largest to smallest.

Display
The PNG must show:

directed edges;

node labels;

in-degree and out-degree in the node label;

largest strongly connected component in orange;

remaining nodes in light blue.

2. hits
python3 web.py hits GRAPH.gml K OUTPUT.png

Refer to the Hub/Authority Rule, Authority Update Rule, Hub Update Rule, and Principle of Repeated Improvement slides. Authority is obtained from hubs pointing to a page; hub value comes from authorities pointed to by a page.

Initialize:

authority = 1 for every node
hub = 1 for every node

Perform exactly K updates. For every update:

1. Calculate new authority scores from the current hub scores.
2. Normalize authority scores so their sum is 1.
3. Calculate new hub scores using the new authority scores.
4. Normalize hub scores so their sum is 1.

Print scores to six decimal places.

Required output:

NODES <number>
ITERATIONS <K>
AUTHORITIES <node:value ...>
HUBS <node:value ...>
TOP_AUTHORITY <node>
TOP_HUB <node>
GRAPH_IMAGE <filename>

For ties, select the alphabetically first node.

Display
Show:

directed edges;

each node's authority and hub scores;

node size proportional to authority score;

highest-authority node in orange.

3. pagerank
python3 web.py pagerank GRAPH.gml K S OUTPUT.png

Refer to the Basic Definition of PageRank, Scaling Down of PageRank, and Random Walk for Scaled PageRank slides.

K is the number of iterations and S is the scaling factor:

0 < S < 1

Initialize every node to:

1/n

For each iteration:

1. Each node divides its PageRank equally among its outgoing links.
2. A node with no outgoing links passes its PageRank to itself.
3. Multiply the resulting values by S.
4. Add (1 - s)/n to every node.

This follows the scaled PageRank rule in the slides.

Required output:

NODES <number>
ITERATIONS <K>
SCALE <S>
PAGERANK <node:value ...>
TOP_PAGE <node>
GRAPH_IMAGE <filename>

Print S and PageRank values to six decimal places.

Display
Show:

directed edges;

PageRank in each node label;

node size proportional to PageRank;

highest-ranked page in orange.

Error Handling
Exit with a nonzero status for:

unknown command;

missing or extra arguments;

nonexistent GML file;

undirected graph;

empty graph;

k < 1;

s <= 0 or s >= 1.

Rubric (Assignment 5)
Structure: degrees and SCC analysis               1.25 pts
HITS authority scores                             0.75 pts
HITS hub scores and top pages                     0.75 pts
Scaled PageRank and top page                      1.25 pts
PNG displays, CLI, exact output, error handling   1 pt
Total                                             5 pts
