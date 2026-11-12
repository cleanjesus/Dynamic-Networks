#!/usr/bin/env python3
"""CECS 427 - Web Link Analysis assignment.

Usage:
    python3 web.py structure GRAPH.gml OUTPUT.png
    python3 web.py hits GRAPH.gml K OUTPUT.png
    python3 web.py pagerank GRAPH.gml K S OUTPUT.png

---------------------------------------------------------------------------
Generative AI Disclosure (Syllabus Section 16)
---------------------------------------------------------------------------
The following generative AI tools were used in this assignment:
    Cursor IDE agent (Claude)

Usage of AI:
    - Used AI to map the lecture slide definitions (The Structure of the Web,
      Link Analysis and Web Search) to the required output fields and plan
      the program layout.
---------------------------------------------------------------------------
"""

import os
import sys

import matplotlib.pyplot as plt
import networkx as nx

plt.switch_backend("Agg")


def fail(message):
    """Print an error to stderr and exit with a nonzero status."""
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def load_graph(path):
    """Read a directed, non-empty graph from a GML file.

    Node labels are converted to strings so they sort alphabetically.
    """
    if not os.path.isfile(path):
        fail(f"file not found: {path}")
    try:
        G = nx.read_gml(path)
    except Exception as error:
        fail(f"cannot read GML file {path}: {error}")
    if not G.is_directed():
        fail("graph must be directed")
    if G.is_multigraph():
        fail("graph must not contain repeated edges")
    if G.number_of_nodes() == 0:
        fail("graph is empty")
    return nx.relabel_nodes(G, {n: str(n) for n in G.nodes()})


def parse_k(text):
    """K is the number of iterations: an integer of at least 1."""
    try:
        k = int(text)
    except ValueError:
        fail(f"K must be an integer: {text}")
    if k < 1:
        fail("K must be at least 1")
    return k


def parse_s(text):
    """S is the scaling factor: a number strictly between 0 and 1."""
    try:
        s = float(text)
    except ValueError:
        fail(f"S must be a number: {text}")
    if not 0 < s < 1:
        fail("S must satisfy 0 < S < 1")
    return s


def fmt6(x):
    return f"{x:.6f}"


def new_figure():
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.axis("off")
    return fig, ax


def finish(lines, fig, output):
    """Save the PNG, then print the result lines and GRAPH_IMAGE."""
    fig.savefig(output, format="png", bbox_inches="tight")
    plt.close(fig)
    for line in lines:
        print(line)
    print(f"GRAPH_IMAGE {output}")


def cmd_structure(args):
    load_graph(args[0])
    fail("structure is not implemented yet")


def cmd_hits(args):
    load_graph(args[0])
    parse_k(args[1])
    fail("hits is not implemented yet")


def cmd_pagerank(args):
    load_graph(args[0])
    parse_k(args[1])
    parse_s(args[2])
    fail("pagerank is not implemented yet")


COMMANDS = {
    "structure": (2, cmd_structure, "GRAPH.gml OUTPUT.png"),
    "hits": (3, cmd_hits, "GRAPH.gml K OUTPUT.png"),
    "pagerank": (4, cmd_pagerank, "GRAPH.gml K S OUTPUT.png"),
}


def main():
    if len(sys.argv) < 2:
        fail("usage: web.py structure|hits|pagerank ...")

    command = sys.argv[1]
    args = sys.argv[2:]

    if command not in COMMANDS:
        fail(f"unknown command: {command}")

    expected, handler, usage = COMMANDS[command]
    if len(args) != expected:
        fail(f"usage: web.py {command} {usage}")

    handler(args)


if __name__ == "__main__":
    main()
