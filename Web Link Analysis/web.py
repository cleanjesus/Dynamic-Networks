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

import math
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
        # Some files have node ids but no labels: fall back to the ids.
        try:
            G = nx.read_gml(path, label=None)
        except Exception:
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
    fig, ax = plt.subplots(figsize=(13, 10))
    ax.axis("off")
    return fig, ax


def min_distance(pos):
    """Smallest distance between any two nodes in a layout."""
    points = list(pos.values())
    return min(
        math.dist(p, q)
        for i, p in enumerate(points) for q in points[i + 1:]
    ) if len(points) > 1 else 0.0


def layout(G):
    """Spring layout with fixed seeds (same picture every run).

    Tries a few seeds and keeps the one whose closest two nodes are
    farthest apart, so labels overlap as little as possible.
    """
    n = G.number_of_nodes()
    seeds = range(427, 447) if n <= 60 else [427]
    layouts = [
        nx.spring_layout(G, seed=s, k=5 / math.sqrt(n), iterations=300)
        for s in seeds
    ]
    return max(layouts, key=min_distance)


def draw_digraph(G, ax, colors, sizes, labels, font_size=8):
    """Draw a directed graph with arrows, using the same layout every run.

    colors, sizes and labels are dicts keyed by node.
    """
    pos = layout(G)
    nodes = sorted(G.nodes())
    node_sizes = [sizes[n] for n in nodes]
    nx.draw_networkx_nodes(
        G, pos, ax=ax, nodelist=nodes,
        node_color=[colors[n] for n in nodes], node_size=node_sizes,
    )
    nx.draw_networkx_edges(
        G, pos, ax=ax, nodelist=nodes, edge_color="gray", arrows=True,
        arrowsize=15, node_size=node_sizes, connectionstyle="arc3,rad=0.1",
    )
    nx.draw_networkx_labels(G, pos, ax=ax, labels=labels, font_size=font_size)


def finish(lines, fig, output):
    """Save the PNG, then print the result lines and GRAPH_IMAGE."""
    try:
        fig.savefig(output, format="png", bbox_inches="tight")
    except OSError as error:
        fail(f"cannot write {output}: {error}")
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


def normalize(scores):
    """Scale scores so they sum to 1 (left unchanged if they sum to 0)."""
    total = sum(scores.values())
    if total == 0:
        return scores
    return {n: v / total for n, v in scores.items()}


def top_node(scores):
    """Node with the highest score; ties go to the alphabetically first node."""
    best = max(scores.values())
    return min(
        n for n, v in scores.items()
        if math.isclose(v, best, rel_tol=1e-9, abs_tol=1e-12)
    )


def cmd_hits(args):
    G = load_graph(args[0])
    k = parse_k(args[1])
    output = args[2]

    nodes = sorted(G.nodes())
    auth = {n: 1.0 for n in nodes}
    hub = {n: 1.0 for n in nodes}

    for _ in range(k):
        # Authority Update Rule: sum of the hub scores of the pages linking in.
        auth = {p: sum(hub[q] for q in G.predecessors(p)) for p in nodes}
        auth = normalize(auth)
        # Hub Update Rule: sum of the (new) authority scores of the pages
        # it links to.
        hub = {q: sum(auth[p] for p in G.successors(q)) for q in nodes}
        hub = normalize(hub)

    top_auth = top_node(auth)
    top_hub = top_node(hub)

    lines = [
        f"NODES {G.number_of_nodes()}",
        f"ITERATIONS {k}",
        " ".join(["AUTHORITIES"] + [f"{n}:{fmt6(auth[n])}" for n in nodes]),
        " ".join(["HUBS"] + [f"{n}:{fmt6(hub[n])}" for n in nodes]),
        f"TOP_AUTHORITY {top_auth}",
        f"TOP_HUB {top_hub}",
    ]

    # Node size is proportional to the authority score (with a small
    # minimum so nodes with authority 0 stay visible).
    colors = {n: "orange" if n == top_auth else "lightblue" for n in nodes}
    sizes = {n: max(700, 12000 * auth[n]) for n in nodes}
    labels = {
        n: f"{n}\nauth {fmt6(auth[n])}\nhub {fmt6(hub[n])}" for n in nodes
    }

    fig, ax = new_figure()
    draw_digraph(G, ax, colors, sizes, labels, font_size=7)
    ax.set_title(
        f"HITS after {k} updates (size = authority, "
        f"top authority {top_auth} in orange)"
    )

    finish(lines, fig, output)


def cmd_pagerank(args):
    G = load_graph(args[0])
    k = parse_k(args[1])
    s = parse_s(args[2])
    output = args[3]

    nodes = sorted(G.nodes())
    n = len(nodes)
    rank = {v: 1 / n for v in nodes}

    for _ in range(k):
        # Basic PageRank Update Rule: each page divides its PageRank equally
        # across its outgoing links; a page with no outgoing links passes all
        # of its PageRank to itself.
        shares = {v: 0.0 for v in nodes}
        for v in nodes:
            out = list(G.successors(v))
            if out:
                for u in out:
                    shares[u] += rank[v] / len(out)
            else:
                shares[v] += rank[v]
        # Scaling Down: multiply by s, then give every page (1 - s) / n.
        rank = {v: s * shares[v] + (1 - s) / n for v in nodes}

    top_page = top_node(rank)

    lines = [
        f"NODES {G.number_of_nodes()}",
        f"ITERATIONS {k}",
        f"SCALE {fmt6(s)}",
        " ".join(["PAGERANK"] + [f"{v}:{fmt6(rank[v])}" for v in nodes]),
        f"TOP_PAGE {top_page}",
    ]

    # Node size is proportional to PageRank (scaled by n so a typical node
    # has about the same size on any graph, with a small minimum).
    colors = {v: "orange" if v == top_page else "lightblue" for v in nodes}
    sizes = {v: max(300, 1200 * n * rank[v]) for v in nodes}
    labels = {v: f"{v}\n{fmt6(rank[v])}" for v in nodes}

    fig, ax = new_figure()
    draw_digraph(G, ax, colors, sizes, labels)
    ax.set_title(
        f"Scaled PageRank after {k} updates, s={fmt6(s)} "
        f"(size = PageRank, top page {top_page} in orange)"
    )

    finish(lines, fig, output)


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
