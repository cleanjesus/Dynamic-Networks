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


def draw_digraph(G, ax, colors, sizes, labels, font_size=8):
    """Draw a directed graph with arrows, using the same layout every run.

    colors, sizes and labels are dicts keyed by node.
    """
    pos = nx.spring_layout(G, seed=427)
    nodes = sorted(G.nodes())
    node_sizes = [sizes[n] for n in nodes]
    nx.draw_networkx_nodes(
        G, pos, ax=ax, nodelist=nodes,
        node_color=[colors[n] for n in nodes], node_size=node_sizes,
    )
    nx.draw_networkx_edges(
        G, pos, ax=ax, edge_color="gray", arrows=True, arrowsize=15,
        node_size=node_sizes, connectionstyle="arc3,rad=0.1",
    )
    nx.draw_networkx_labels(G, pos, ax=ax, labels=labels, font_size=font_size)


def finish(lines, fig, output):
    """Save the PNG, then print the result lines and GRAPH_IMAGE."""
    fig.savefig(output, format="png", bbox_inches="tight")
    plt.close(fig)
    for line in lines:
        print(line)
    print(f"GRAPH_IMAGE {output}")


def cmd_structure(args):
    G = load_graph(args[0])
    output = args[1]

    nodes = sorted(G.nodes())
    in_degree = dict(G.in_degree())
    out_degree = dict(G.out_degree())

    # Strongly connected components: every page can reach every other page
    # in the component by following links (the central core of the bow-tie).
    components = [sorted(c) for c in nx.strongly_connected_components(G)]
    components.sort(key=lambda c: (-len(c), c))
    largest = components[0]

    lines = [
        f"NODES {G.number_of_nodes()}",
        f"EDGES {G.number_of_edges()}",
        " ".join(["IN_DEGREES"] + [f"{n}:{in_degree[n]}" for n in nodes]),
        " ".join(["OUT_DEGREES"] + [f"{n}:{out_degree[n]}" for n in nodes]),
        f"SCC_COUNT {len(components)}",
        " ".join(["SCC_SIZES"] + [str(len(c)) for c in components]),
        " ".join(["LARGEST_SCC"] + largest),
    ]

    colors = {n: "orange" if n in largest else "lightblue" for n in nodes}
    sizes = {n: 1400 for n in nodes}
    labels = {n: f"{n}\nin:{in_degree[n]} out:{out_degree[n]}" for n in nodes}

    fig, ax = new_figure()
    draw_digraph(G, ax, colors, sizes, labels)
    noun = "component" if len(components) == 1 else "components"
    ax.set_title(
        f"Web Structure: {len(components)} strongly connected {noun} "
        f"(largest SCC in orange, size {len(largest)})"
    )

    finish(lines, fig, output)


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
