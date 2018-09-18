import math
from data_structures.graph_no_vertice_object import Graph
from typing import List, Dict

# Takes in graph and builds FW Multi-Dim matrix m, then passes m to floyd_warshall which takes in the matrix.
# Because in some cases, we won't actually need to build a graph before we're able to compute so this saves
# some compute.
def floyd_warshall_g(g: Graph) -> List:
    v = g.vertices()    # Expects 1...n styled vertices.
    num_v = len(v)
    m = [[math.inf] * num_v for _ in range(num_v)]

    for edge in g.edges():
        w = edge.element()
        origin, destination = edge.endpoints()
        m[origin][destination] = w

    for k in v:
        m[k][k] = 0

    return floyd_warshall(m)


# Can be modified later to return another matrix from which we can compute the path.
def floyd_warshall(m: List) -> List:
    n = len(m)
    d_matrices : Dict[int, List] = {0: m}

    for k in range(1, n + 1):
        m_cur = d_matrices[k] = [[] for _ in range(n)]
        m_prev = d_matrices[k-1]
        for i in range(n):
            for j in range(n):
                m_cur[i].append(min(m_prev[i][j], m_prev[i][k] + m_prev[k][j]))

        # Space efficiency.
        del d_matrices[k-1]

    return d_matrices[n]