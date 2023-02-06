import math
from data_structures.graph_no_vertice_object import Graph
from typing import List, Dict


# Takes in graph and builds FW Multi-Dim matrix m, then passes m to floyd_warshall which takes in the matrix.
# Because in some cases, we won't actually need to build a graph before we're able to compute so this saves
# some compute.
def floyd_warshall_g(g: Graph) -> List:
    v = g.vertices()  # Expects 1...n styled vertices.
    num_v = len(v)
    m = [[math.inf] * num_v for _ in range(num_v)]

    for edge in g.edges():
        w = edge.element()
        origin, destination = edge.endpoints()
        m[origin][destination] = w

    for k in v:
        m[k][k] = 0

    return floyd_warshall(m)


def floyd_warshall(m: List) -> List:
    n = len(m)

    for k in range(n):
        kk = m[k]
        for i in range(n):
            ii = m[i]
            ik = ii[k]
            if ik == math.inf:
                continue
            for j in range(n):
                kj = kk[j]
                if kj == math.inf:
                    continue
                m[i][j] = min(ii[j], ik + kj)

    return m
