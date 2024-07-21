from typing import Any
from topics.graphs.bfs import Graph

def _process_queries(n: int, edges: list[tuple[int, int]], start: int) -> Any:
    graph = Graph(n)
    for u, v in edges:
        graph.connect(u - 1, v - 1)  # Convert to 0-based index
    result = graph.find_all_distances(start - 1)
    return result

def test_bfs():
    test_edges = [(4, 2), (1, 2), (1, 3)]
    test_n = 4
    test_start = 1
    assert _process_queries(test_n, test_edges, test_start) == [6, 6, 12]