# Social Network Properties

CECS 427 (Network Analysis) assignment: analyze structural properties of social networks read from GML files and visualize the results.

## Features

| Command | What it does |
| --- | --- |
| `ties` | Clustering coefficient per node, neighborhood overlap per edge, and Triadic Closure Property violations for networks with strong/weak ties. |
| `balance` | Structural balance of a complete signed (+/−) graph: counts balanced and unbalanced triangles. |
| `homophily` | Tests a group for homophily by comparing the cross-group edge fraction against the expected `2p(1−p)`. |
| `partition` | Divisive graph partitioning: repeatedly removes the highest edge-betweenness edge until the graph has K components. |

Each command prints its results to stdout and saves a PNG visualization. Invalid input (unknown command, wrong argument count, missing file, directed graph, bad attributes, invalid `K`, etc.) exits with a nonzero status. There are no interactive prompts.

## Requirements

- Python 3
- [NetworkX](https://networkx.org/)
- [Matplotlib](https://matplotlib.org/)

```bash
pip install networkx matplotlib
```

## Usage

```bash
python3 relationships.py ties GRAPH.gml OUTPUT.png
python3 relationships.py balance GRAPH.gml OUTPUT.png
python3 relationships.py homophily GRAPH.gml GROUP OUTPUT.png
python3 relationships.py partition GRAPH.gml K OUTPUT.png
```

Examples using the included sample graphs:

```bash
python3 relationships.py ties samples/ties.gml ties.png
python3 relationships.py balance samples/signed.gml balance.png
python3 relationships.py homophily samples/groups.gml blue homophily.png
python3 relationships.py partition samples/network.gml 3 partitions.png
```

### Visualizations

- **ties** – strong edges solid red, weak edges dashed gray, overlap as edge labels, clustering coefficients next to node labels.
- **balance** – positive edges green, negative edges red, structural-balance result in the title.
- **homophily** – nodes colored by group, same-group edges solid gray, cross-group edges dashed red.
- **partition** – each partition in its own color, remaining edges solid gray, removed edges dashed red.

## Project Structure

| Path | Description |
| --- | --- |
| `relationships.py` | Main program |
| `samples/` | Sample GML inputs (`ties`, `signed`, `groups`, `network`) |
| `*.png` | Example output images |
| `ASSIGNMENT.md` | Original assignment instructions |

## Generative AI Disclosure

Generative AI (Cursor IDE agent) was used to help map lecture definitions to the required output and plan the program layout. See the header of `relationships.py` for details.
