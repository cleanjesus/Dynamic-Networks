#!/usr/bin/env python3
"""CECS 427 - Diffusion assignment.

Usage:
    python3 diffusion.py epidemic GRAPH.gml P INFECTIOUS_PERIOD SEED INITIAL OUTPUT.png
    python3 diffusion.py behavior GRAPH.gml A B INITIAL OUTPUT.png
    python3 diffusion.py information GRAPH.gml OUTPUT.png
    python3 diffusion.py smallworld GRAPH.gml OUTPUT.png

---------------------------------------------------------------------------
Generative AI Disclosure (Syllabus Section 16)
---------------------------------------------------------------------------
The following generative AI tools were used in this assignment:
    Cursor IDE agent

Usage of AI:
    - Used AI to map the lecture definitions for SIR epidemics, networked
      coordination games, information cascades, and small-world networks to
      the required commands and output fields.
    - Reused the CLI, graph-loading, BFS, and drawing patterns from earlier
      course assignments.
---------------------------------------------------------------------------
"""

import os
import random
import sys
from collections import deque
from decimal import Decimal, InvalidOperation

import matplotlib.pyplot as plt
import networkx as nx

plt.switch_backend("Agg")


def fail(message):
    """Print an error to stderr and exit with a nonzero status."""
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def load_graph(path, require_undirected=False):
    """Read a non-empty GML graph and convert node labels to strings."""
    if not os.path.isfile(path):
        fail(f"file not found: {path}")
    try:
        graph = nx.read_gml(path)
    except Exception as error:
        try:
            graph = nx.read_gml(path, label=None)
        except Exception:
            fail(f"cannot read GML file {path}: {error}")
    if require_undirected and graph.is_directed():
        fail("graph must be undirected")
    if graph.is_multigraph():
        fail("graph must not contain repeated edges")
    if graph.number_of_nodes() == 0:
        fail("graph is empty")
    return nx.relabel_nodes(graph, {node: str(node) for node in graph.nodes()})


def parse_decimal(text, name, positive=False):
    """Parse a finite decimal number, optionally requiring it to be positive."""
    try:
        value = Decimal(text)
    except InvalidOperation:
        fail(f"{name} must be a number: {text}")
    if not value.is_finite():
        fail(f"{name} must be a finite number")
    if positive and value <= 0:
        fail(f"{name} must be greater than 0")
    return value


def parse_int(text, name):
    """Parse an integer argument."""
    try:
        return int(text)
    except ValueError:
        fail(f"{name} must be an integer: {text}")


def parse_initial(text, graph):
    """Parse a comma-separated, non-empty list of existing node names."""
    names = [name.strip() for name in text.split(",")]
    if not names or any(not name for name in names):
        fail("INITIAL must be a comma-separated list of node names")
    missing = sorted(set(names) - set(graph.nodes()))
    if missing:
        fail(f"initial node not in graph: {missing[0]}")
    return sorted(set(names))


def fmt3(value):
    return f"{float(value):.3f}"


def sorted_edges(graph):
    """Return undirected edges with alphabetized endpoints."""
    return sorted(tuple(sorted((str(u), str(v)))) for u, v in graph.edges())


def bfs_distances(graph, source):
    """Find unweighted shortest-path distances by BFS, as in graph.py."""
    distances = {source: 0}
    queue = deque([source])
    while queue:
        node = queue.popleft()
        for neighbor in sorted(graph.neighbors(node)):
            if neighbor not in distances:
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)
    return distances


def is_connected(graph):
    """A graph is connected when BFS from one node reaches every node."""
    start = min(graph.nodes())
    return len(bfs_distances(graph, start)) == graph.number_of_nodes()


def average_path_length(graph):
    """Average BFS distance over all ordered pairs of distinct nodes."""
    nodes = sorted(graph.nodes())
    if len(nodes) == 1:
        return 0.0
    distance_sum = 0
    for source in nodes:
        distances = bfs_distances(graph, source)
        distance_sum += sum(distances[target] for target in nodes if target != source)
    return distance_sum / (len(nodes) * (len(nodes) - 1))


def average_clustering(graph):
    """Average the lecture's local clustering coefficient over all nodes."""
    coefficients = []
    for node in graph.nodes():
        neighbors = list(graph.neighbors(node))
        count = len(neighbors)
        if count < 2:
            coefficients.append(0.0)
            continue
        actual = sum(
            1
            for i, first in enumerate(neighbors)
            for second in neighbors[i + 1:]
            if graph.has_edge(first, second)
        )
        possible = count * (count - 1) / 2
        coefficients.append(actual / possible)
    return sum(coefficients) / len(coefficients)


def new_figure():
    fig, axis = plt.subplots(figsize=(13, 10))
    axis.axis("off")
    return fig, axis


def layout(graph):
    """Use the same fixed-seed layout approach as previous assignments."""
    return nx.spring_layout(graph, seed=427)


def finish(lines, fig, output):
    """Save the PNG, print result lines, then print GRAPH_IMAGE."""
    try:
        fig.savefig(output, format="png", bbox_inches="tight")
    except OSError as error:
        fail(f"cannot write {output}: {error}")
    finally:
        plt.close(fig)
    for line in lines:
        print(line)
    print(f"GRAPH_IMAGE {output}")


def cmd_epidemic(args):
    graph = load_graph(args[0], require_undirected=True)
    p_decimal = parse_decimal(args[1], "P")
    if not 0 <= p_decimal <= 1:
        fail("P must satisfy 0 <= P <= 1")
    p = float(p_decimal)
    period = parse_int(args[2], "INFECTIOUS_PERIOD")
    if period < 1:
        fail("INFECTIOUS_PERIOD must be at least 1")
    seed = parse_int(args[3], "SEED")
    initial = parse_initial(args[4], graph)
    output = args[5]

    nodes = sorted(graph.nodes())
    states = {node: "S" for node in nodes}
    remaining = {}
    for node in initial:
        states[node] = "I"
        remaining[node] = period

    rng = random.Random(seed)
    ever_infected = set(initial)
    steps = 0
    while remaining:
        newly_infected = set()
        susceptible_at_start = {node for node in nodes if states[node] == "S"}
        for node in sorted(remaining):
            for neighbor in sorted(graph.neighbors(node)):
                if neighbor in susceptible_at_start:
                    if rng.random() < p:
                        newly_infected.add(neighbor)

        for node in list(remaining):
            remaining[node] -= 1
            if remaining[node] == 0:
                states[node] = "R"
                del remaining[node]
        for node in newly_infected:
            states[node] = "I"
            remaining[node] = period
        ever_infected.update(newly_infected)
        steps += 1

    average_degree = 2 * graph.number_of_edges() / graph.number_of_nodes()
    r_zero = p * average_degree
    lines = [
        f"NODES {graph.number_of_nodes()}",
        f"EDGES {graph.number_of_edges()}",
        f"P {fmt3(p)}",
        f"INFECTIOUS_PERIOD {period}",
        f"R0 {fmt3(r_zero)}",
        " ".join(["INITIAL_INFECTED"] + initial),
        f"STEPS {steps}",
        f"SUSCEPTIBLE {sum(states[node] == 'S' for node in nodes)}",
        f"REMOVED {sum(states[node] == 'R' for node in nodes)}",
        " ".join(["EVER_INFECTED"] + sorted(ever_infected)),
    ]

    pos = layout(graph)
    fig, axis = new_figure()
    nx.draw_networkx_nodes(
        graph, pos, ax=axis, nodelist=nodes,
        node_color=["lightblue" if states[node] == "S" else "red" for node in nodes],
        node_size=900,
    )
    nx.draw_networkx_edges(graph, pos, ax=axis, edge_color="gray")
    nx.draw_networkx_labels(graph, pos, ax=axis)
    axis.set_title(f"SIR Epidemic Final State (R0 = {fmt3(r_zero)})")
    finish(lines, fig, output)


def cmd_behavior(args):
    graph = load_graph(args[0], require_undirected=True)
    payoff_a = parse_decimal(args[1], "A", positive=True)
    payoff_b = parse_decimal(args[2], "B", positive=True)
    initial = parse_initial(args[3], graph)
    output = args[4]

    nodes = sorted(graph.nodes())
    initial_set = set(initial)
    adopters = set(initial)
    rounds = 0
    while True:
        added = set()
        for node in nodes:
            degree = graph.degree(node)
            if node in adopters or degree == 0:
                continue
            neighbors_a = sum(neighbor in adopters for neighbor in graph.neighbors(node))
            if Decimal(neighbors_a) * (payoff_a + payoff_b) >= payoff_b * degree:
                added.add(node)
        if not added:
            break
        adopters.update(added)
        rounds += 1

    threshold = payoff_b / (payoff_a + payoff_b)
    complete = "YES" if len(adopters) == len(nodes) else "NO"
    lines = [
        f"NODES {graph.number_of_nodes()}",
        f"EDGES {graph.number_of_edges()}",
        f"THRESHOLD {fmt3(threshold)}",
        " ".join(["INITIAL_ADOPTERS"] + initial),
        f"ROUNDS {rounds}",
        " ".join(["FINAL_ADOPTERS"] + sorted(adopters)),
        f"ADOPTER_COUNT {len(adopters)}",
        f"COMPLETE_CASCADE {complete}",
    ]

    colors = []
    for node in nodes:
        if node in initial_set:
            colors.append("red")
        elif node in adopters:
            colors.append("orange")
        else:
            colors.append("lightblue")
    pos = layout(graph)
    fig, axis = new_figure()
    nx.draw_networkx_nodes(
        graph, pos, ax=axis, nodelist=nodes, node_color=colors, node_size=900,
    )
    nx.draw_networkx_edges(graph, pos, ax=axis, edge_color="gray")
    nx.draw_networkx_labels(graph, pos, ax=axis)
    axis.set_title(
        f"Behavior Cascade (threshold = {fmt3(threshold)}, "
        f"complete cascade = {complete})"
    )
    finish(lines, fig, output)


def information_people(graph):
    """Validate information-cascade node attributes and return ordered people."""
    orders = {}
    signals = {}
    for node, data in graph.nodes(data=True):
        order = data.get("order")
        if isinstance(order, bool) or not isinstance(order, int):
            fail(f"node {node} has missing or invalid order")
        signal = data.get("signal")
        if signal not in ("H", "L"):
            fail(f"node {node} has missing or invalid signal")
        orders[node] = order
        signals[node] = signal
    if len(set(orders.values())) != len(orders):
        fail("order values must be unique")
    people = sorted(graph.nodes(), key=lambda node: orders[node])
    return people, orders, signals


def cmd_information(args):
    graph = load_graph(args[0])
    output = args[1]
    people, orders, signals = information_people(graph)

    evidence = 0
    cascade_start = None
    cascade_action = None
    decisions = {}
    for node in people:
        if abs(evidence) < 2:
            decisions[node] = "ACCEPT" if signals[node] == "H" else "REJECT"
            evidence += 1 if signals[node] == "H" else -1
        else:
            if cascade_start is None:
                cascade_start = orders[node]
                cascade_action = "ACCEPT" if evidence >= 2 else "REJECT"
            decisions[node] = cascade_action

    lines = [
        f"PEOPLE {len(people)}",
        " ".join(["SIGNALS"] + [f"{node}:{signals[node]}" for node in people]),
        " ".join(
            ["DECISIONS"] + [f"{node}:{decisions[node]}" for node in people]
        ),
        f"CASCADE_START {cascade_start if cascade_start is not None else 'NONE'}",
        f"CASCADE_ACTION {cascade_action if cascade_action is not None else 'NONE'}",
    ]

    display = nx.DiGraph()
    display.add_nodes_from(graph.nodes())
    if graph.is_directed():
        display.add_edges_from(graph.edges())
    else:
        for first, second in graph.edges():
            if orders[first] < orders[second]:
                display.add_edge(first, second)
            else:
                display.add_edge(second, first)

    pos = layout(display)
    nodes = sorted(display.nodes())
    after_cascade = {
        node
        for node in nodes
        if cascade_start is not None and orders[node] >= cascade_start
    }
    fig, axis = new_figure()
    nx.draw_networkx_nodes(
        display, pos, ax=axis, nodelist=nodes,
        node_color=["lightgreen" if signals[node] == "H" else "lightcoral"
                    for node in nodes],
        edgecolors=["orange" if node in after_cascade else "black" for node in nodes],
        linewidths=[3 if node in after_cascade else 1 for node in nodes],
        node_size=1800,
    )
    nx.draw_networkx_edges(
        display, pos, ax=axis, edge_color="gray", arrows=True, arrowsize=16,
        node_size=1800, connectionstyle="arc3,rad=0.08",
    )
    labels = {
        node: f"{node}\norder {orders[node]}\n{signals[node]} / {decisions[node]}"
        for node in nodes
    }
    nx.draw_networkx_labels(display, pos, ax=axis, labels=labels, font_size=7)
    axis.set_title("Sequential Information Cascade")
    finish(lines, fig, output)


def cmd_smallworld(args):
    graph = load_graph(args[0], require_undirected=True)
    output = args[1]

    for first, second, data in graph.edges(data=True):
        if data.get("type") not in ("local", "weak"):
            fail(f"edge {first}-{second} has missing or invalid type")
    if not is_connected(graph):
        fail("small-world graph must be connected")

    local = nx.Graph()
    local.add_nodes_from(graph.nodes())
    local.add_edges_from(
        (first, second)
        for first, second, data in graph.edges(data=True)
        if data["type"] == "local"
    )
    if not is_connected(local):
        fail("small-world local-only graph must be connected")

    full_clustering = average_clustering(graph)
    local_clustering = average_clustering(local)
    full_path = average_path_length(graph)
    local_path = average_path_length(local)
    reduction = local_path - full_path
    weak_edges = [
        edge for edge in sorted_edges(graph) if graph.edges[edge]["type"] == "weak"
    ]
    local_edges = [
        edge for edge in sorted_edges(graph) if graph.edges[edge]["type"] == "local"
    ]
    lines = [
        f"NODES {graph.number_of_nodes()}",
        f"EDGES {graph.number_of_edges()}",
        f"WEAK_TIES {len(weak_edges)}",
        f"FULL_CLUSTERING {fmt3(full_clustering)}",
        f"LOCAL_CLUSTERING {fmt3(local_clustering)}",
        f"FULL_AVG_PATH {fmt3(full_path)}",
        f"LOCAL_AVG_PATH {fmt3(local_path)}",
        f"PATH_REDUCTION {fmt3(reduction)}",
    ]

    pos = layout(graph)
    fig, axis = new_figure()
    nx.draw_networkx_nodes(
        graph, pos, ax=axis, node_color="lightblue", node_size=900,
    )
    nx.draw_networkx_edges(
        graph, pos, ax=axis, edgelist=local_edges,
        edge_color="gray", style="solid", width=1.5,
    )
    nx.draw_networkx_edges(
        graph, pos, ax=axis, edgelist=weak_edges,
        edge_color="red", style="dashed", width=2,
    )
    nx.draw_networkx_labels(graph, pos, ax=axis)
    axis.set_title(
        f"Small World (full avg path = {fmt3(full_path)}, "
        f"local-only avg path = {fmt3(local_path)})"
    )
    finish(lines, fig, output)


COMMANDS = {
    "epidemic": (
        6, cmd_epidemic,
        "GRAPH.gml P INFECTIOUS_PERIOD SEED INITIAL OUTPUT.png",
    ),
    "behavior": (5, cmd_behavior, "GRAPH.gml A B INITIAL OUTPUT.png"),
    "information": (2, cmd_information, "GRAPH.gml OUTPUT.png"),
    "smallworld": (2, cmd_smallworld, "GRAPH.gml OUTPUT.png"),
}


def main():
    if len(sys.argv) < 2:
        fail("usage: diffusion.py epidemic|behavior|information|smallworld ...")

    command = sys.argv[1]
    args = sys.argv[2:]
    if command not in COMMANDS:
        fail(f"unknown command: {command}")

    expected, handler, usage = COMMANDS[command]
    if len(args) != expected:
        fail(f"usage: diffusion.py {command} {usage}")
    handler(args)


if __name__ == "__main__":
    main()
