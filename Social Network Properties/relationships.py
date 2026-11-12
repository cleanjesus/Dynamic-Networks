#!/usr/bin/env python3
"""CECS 427 - Social Network Properties assignment.

Usage:
    python3 relationships.py ties GRAPH.gml OUTPUT.png
    python3 relationships.py balance GRAPH.gml OUTPUT.png
    python3 relationships.py homophily GRAPH.gml GROUP OUTPUT.png
    python3 relationships.py partition GRAPH.gml K OUTPUT.png

---------------------------------------------------------------------------
Generative AI Disclosure (Syllabus Section 16)
---------------------------------------------------------------------------
The following generative AI tools were used in this assignment:
    Cursor IDE agent (Claude)

Usage of AI:
    - Used AI to map the lecture slide definitions (Strong and Weak Ties,
      Positive and Negative Relationships, Networks in Their Surrounding
      Contexts) to the required output fields and plan the program layout.
---------------------------------------------------------------------------
"""

import math
import os
import sys
from itertools import combinations

import matplotlib
import matplotlib.pyplot as plt
import networkx as nx

plt.switch_backend("Agg")


def fail(message):
    """Print an error to stderr and exit with a nonzero status."""
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def load_graph(path):
    """Read an undirected graph from a GML file."""
    if not os.path.isfile(path):
        fail(f"file not found: {path}")
    G = nx.read_gml(path)
    if G.is_directed():
        fail("graph must be undirected")
    return G


def sorted_edges(G):
    """All edges with alphabetized endpoints, in alphabetical order."""
    return sorted(tuple(sorted(e)) for e in G.edges())


def fmt3(x):
    return f"{x:.3f}"


def distinct_colors(count):
    """One distinct color per category, even past the 10 colors of tab10."""
    if count <= 10:
        return [matplotlib.colormaps["tab10"](i) for i in range(count)]
    return [matplotlib.colormaps["hsv"](i / count) for i in range(count)]


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


def cmd_ties(args):
    G = load_graph(args[0])
    output = args[1]

    for u, v, data in G.edges(data=True):
        if data.get("strength") not in ("strong", "weak"):
            fail(f"edge {u}-{v} has missing or invalid strength")

    nodes = sorted(G.nodes())
    edges = sorted_edges(G)
    clustering = nx.clustering(G)

    overlap = {}
    for a, b in edges:
        na = set(G.neighbors(a))
        nb = set(G.neighbors(b))
        common = len((na & nb) - {a, b})
        total = len((na | nb) - {a, b})
        overlap[(a, b)] = common / total if total else 0.0

    violations = 0
    for a in nodes:
        strong = sorted(
            n for n in G.neighbors(a) if G[a][n]["strength"] == "strong"
        )
        for b, c in combinations(strong, 2):
            if not G.has_edge(b, c):
                violations += 1

    lines = [
        f"NODES {G.number_of_nodes()}",
        f"EDGES {G.number_of_edges()}",
        " ".join(["CLUSTERING"]
                 + [f"{n}:{fmt3(clustering[n])}" for n in nodes]),
        " ".join(["OVERLAP"]
                 + [f"{a}-{b}:{fmt3(overlap[(a, b)])}" for a, b in edges]),
        f"TRIADIC_CLOSURE_VIOLATIONS {violations}",
    ]

    strong_edges = [e for e in edges if G.edges[e]["strength"] == "strong"]
    weak_edges = [e for e in edges if G.edges[e]["strength"] == "weak"]

    pos = nx.spring_layout(G, seed=427)
    fig, ax = new_figure()
    nx.draw_networkx_nodes(
        G, pos, ax=ax, node_color="lightblue", node_size=900,
    )
    nx.draw_networkx_labels(
        G, pos, ax=ax, font_size=8,
        labels={n: f"{n}\n{fmt3(clustering[n])}" for n in nodes},
    )
    nx.draw_networkx_edges(
        G, pos, ax=ax, edgelist=strong_edges,
        edge_color="red", style="solid", width=2,
    )
    nx.draw_networkx_edges(
        G, pos, ax=ax, edgelist=weak_edges,
        edge_color="gray", style="dashed", width=1.5,
    )
    nx.draw_networkx_edge_labels(
        G, pos, ax=ax, font_size=7,
        edge_labels={e: fmt3(overlap[e]) for e in edges},
    )
    ax.set_title(
        "Strong and Weak Ties (node: clustering, edge: neighborhood overlap)\n"
        "strong = solid red, weak = dashed gray"
    )

    finish(lines, fig, output)


def cmd_balance(args):
    G = load_graph(args[0])
    output = args[1]

    for u, v, data in G.edges(data=True):
        if data.get("sign") not in ("+", "-"):
            fail(f"edge {u}-{v} has missing or invalid sign")

    nodes = sorted(G.nodes())
    for u, v in combinations(nodes, 2):
        if not G.has_edge(u, v):
            fail(f"graph is not complete: missing edge {u}-{v}")

    triangles = 0
    balanced = 0
    for a, b, c in combinations(nodes, 3):
        triangles += 1
        positives = sum(
            1 for u, v in ((a, b), (a, c), (b, c)) if G[u][v]["sign"] == "+"
        )
        if positives in (1, 3):
            balanced += 1
    unbalanced = triangles - balanced
    result = "YES" if unbalanced == 0 else "NO"

    lines = [
        f"NODES {G.number_of_nodes()}",
        f"TRIANGLES {triangles}",
        f"BALANCED_TRIANGLES {balanced}",
        f"UNBALANCED_TRIANGLES {unbalanced}",
        f"STRUCTURAL_BALANCE {result}",
    ]

    edges = sorted_edges(G)
    positive_edges = [e for e in edges if G.edges[e]["sign"] == "+"]
    negative_edges = [e for e in edges if G.edges[e]["sign"] == "-"]

    pos = nx.circular_layout(G)
    fig, ax = new_figure()
    nx.draw_networkx_nodes(
        G, pos, ax=ax, node_color="lightblue", node_size=700,
    )
    nx.draw_networkx_labels(G, pos, ax=ax)
    nx.draw_networkx_edges(
        G, pos, ax=ax, edgelist=positive_edges, edge_color="green", width=2,
    )
    nx.draw_networkx_edges(
        G, pos, ax=ax, edgelist=negative_edges, edge_color="red", width=2,
    )
    nx.draw_networkx_edge_labels(
        G, pos, ax=ax, font_size=16, font_weight="bold",
        edge_labels={e: G.edges[e]["sign"] for e in edges},
    )
    ax.set_title(f"Structural Balance: {result}")

    finish(lines, fig, output)


def cmd_homophily(args):
    G = load_graph(args[0])
    group = args[1]
    output = args[2]

    groups = {}
    for n, data in G.nodes(data=True):
        if "group" not in data:
            fail(f"node {n} is missing group")
        groups[n] = data["group"]

    if group not in groups.values():
        fail(f"group does not exist in graph: {group}")

    n_total = G.number_of_nodes()
    m_total = G.number_of_edges()
    edges = sorted_edges(G)

    p = sum(1 for g in groups.values() if g == group) / n_total
    cross_edges = [
        (u, v) for u, v in edges
        if (groups[u] == group) != (groups[v] == group)
    ]
    cross_fraction = len(cross_edges) / m_total
    expected = 2 * p * (1 - p)
    result = "YES" if cross_fraction < expected else "NO"

    lines = [
        f"NODES {n_total}",
        f"EDGES {m_total}",
        f"GROUP {group}",
        f"GROUP_PROPORTION {fmt3(p)}",
        f"CROSS_EDGES {len(cross_edges)}",
        f"CROSS_EDGE_FRACTION {fmt3(cross_fraction)}",
        f"EXPECTED_CROSS_FRACTION {fmt3(expected)}",
        f"HOMOPHILY {result}",
    ]

    same_edges = [e for e in edges if e not in cross_edges]

    pos = nx.spring_layout(G, seed=427)
    fig, ax = new_figure()
    group_values = sorted(set(groups.values()))
    for value, color in zip(group_values, distinct_colors(len(group_values))):
        members = [n for n in G.nodes() if groups[n] == value]
        nx.draw_networkx_nodes(
            G, pos, ax=ax, nodelist=members, node_size=900,
            node_color=[color], label=value,
        )
    nx.draw_networkx_labels(
        G, pos, ax=ax, font_size=8,
        labels={n: f"{n}\n({groups[n]})" for n in G.nodes()},
    )
    nx.draw_networkx_edges(
        G, pos, ax=ax, edgelist=same_edges,
        edge_color="gray", style="solid", width=1.5,
    )
    nx.draw_networkx_edges(
        G, pos, ax=ax, edgelist=cross_edges,
        edge_color="red", style="dashed", width=1.5,
    )
    ax.legend(title="group", scatterpoints=1, markerscale=0.4)
    ax.set_title(f"Homophily ({group}): {result}")

    finish(lines, fig, output)


def cmd_partition(args):
    G = load_graph(args[0])
    k = int(args[1])
    output = args[2]

    n_total = G.number_of_nodes()
    if k < 1:
        fail("K must be at least 1")
    if k > n_total:
        fail(f"K must not exceed the number of nodes ({n_total})")
    if nx.number_connected_components(G) > k:
        fail("graph already contains more than K components")

    H = G.copy()
    removed = []
    while nx.number_connected_components(H) < k:
        betweenness = nx.edge_betweenness_centrality(H, normalized=False)
        best = max(betweenness.values())
        candidates = [
            tuple(sorted(e)) for e, value in betweenness.items()
            if math.isclose(value, best, rel_tol=1e-9, abs_tol=1e-9)
        ]
        u, v = min(candidates)
        H.remove_edge(u, v)
        removed.append((u, v))

    partitions = sorted(sorted(c) for c in nx.connected_components(H))

    lines = [
        f"NODES {n_total}",
        f"EDGES {G.number_of_edges()}",
        f"REQUESTED_PARTITIONS {k}",
        f"PARTITIONS {len(partitions)}",
        " ".join(["REMOVED_EDGES"] + [f"{u}-{v}" for u, v in removed]),
    ]
    for i, part in enumerate(partitions, start=1):
        lines.append(" ".join([f"PARTITION_{i}"] + part))

    pos = nx.spring_layout(G, seed=427)
    fig, ax = new_figure()
    colors = distinct_colors(len(partitions))
    for i, (part, color) in enumerate(zip(partitions, colors), start=1):
        nx.draw_networkx_nodes(
            G, pos, ax=ax, nodelist=part, node_size=700,
            node_color=[color], label=f"Partition {i}",
        )
    nx.draw_networkx_labels(G, pos, ax=ax)
    nx.draw_networkx_edges(
        H, pos, ax=ax, edgelist=sorted_edges(H),
        edge_color="gray", style="solid", width=1.5,
    )
    nx.draw_networkx_edges(
        G, pos, ax=ax, edgelist=removed,
        edge_color="red", style="dashed", width=2,
    )
    ax.legend(scatterpoints=1, markerscale=0.4)
    ax.set_title(f"Graph Partition: K={k}")

    finish(lines, fig, output)


COMMANDS = {
    "ties": (2, cmd_ties, "GRAPH.gml OUTPUT.png"),
    "balance": (2, cmd_balance, "GRAPH.gml OUTPUT.png"),
    "homophily": (3, cmd_homophily, "GRAPH.gml GROUP OUTPUT.png"),
    "partition": (3, cmd_partition, "GRAPH.gml K OUTPUT.png"),
}


def main():
    if len(sys.argv) < 2:
        fail("usage: relationships.py ties|balance|homophily|partition ...")

    command = sys.argv[1]
    args = sys.argv[2:]

    if command not in COMMANDS:
        fail(f"unknown command: {command}")

    expected, handler, usage = COMMANDS[command]
    if len(args) != expected:
        fail(f"usage: relationships.py {command} {usage}")

    handler(args)


if __name__ == "__main__":
    main()
