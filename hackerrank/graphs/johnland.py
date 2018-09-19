import os
import sys
import math
from collections import defaultdict
from data_structures.heap import MinHeapPriorityQueue
from data_structures.graph_no_vertice_object import Graph

def roadsInHackerland(n, edges, start=1):
    def dfs(u):
        total = 1

        if u in tree:
            for edge in tree[u]:
                v = edge.opposite(u)
                d_edges[edge] = dfs(v)
                total += d_edges[edge]

        return total

    d = {}
    pq = MinHeapPriorityQueue()
    pqlocator = {}
    tree = defaultdict(list)
    g = Graph()
    mst = []

    for i in range(1, n + 1):
        if i == start:
            d[start] = 0
        else:
            d[i] = math.inf
        pqlocator[i] = pq.add(d[i], (i, None))
        g.insert_vertex(i)

    for j in range(m):
        g.insert_edge(*edges[j])

    # PRIM's MST
    while not pq.is_empty():
        k,v = pq.remove_top()
        u,e = v
        del pqlocator[u]
        if e is not None:
            tree[e.opposite(u)].append(e)
            mst.append(e)
        for edge in g.incident_edges(u):
            v = edge.opposite(u)
            if v in pqlocator:
                wt = edge.element()
                if wt < d[v]:
                    d[v] = wt
                    pq.update(pqlocator[v], d[v], (v, edge))

    d_edges = {x:0 for x in mst}

    dfs(1)

    results = [(d_edges[e] * (n - d_edges[e])) for e in mst]

    sum = 0
    for i in range(len(results)):
        sum += results[i] * (2 ** mst[i].element())

    return bin(sum)[2:]

if __name__ == '__main__':
    f = open('../data/johnland-002.txt')

    nm = f.readline().split()

    n = int(nm[0])

    m = int(nm[1])

    edges = []

    for _ in range(m):
        edges.append([int(x) for x in f.readline().split()])

    result = roadsInHackerland(n, edges)

    print(result)
