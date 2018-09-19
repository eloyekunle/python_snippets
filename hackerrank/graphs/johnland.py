import os
import sys
import math
from collections import defaultdict

from data_structures.partition_min import Partition

class Edge:
    __slots__ = '_origin', '_destination', '_element'

    def __init__(self, u, v, x):
        self._origin = u
        self._destination = v
        self._element = x   # sometimes acts as weight for weighted graphs

    def endpoints(self):
        return self._origin, self._destination  # Order matters yo!

    def opposite(self, v):
        return self._destination if v == self._origin else self._origin

    def element(self):
        return self._element

    def __hash__(self):  # will allow edge to be a map/set key
        return hash((self._origin, self._destination))

def roadsInHackerland(n, edges):
    def dfs(u, parent=None):
        total = 1

        for edge in tree[u]:
            if parent is not None and parent in edge.endpoints():
                continue
            v = edge.opposite(u)
            d_edges[edge] = dfs(v, u)
            total += d_edges[edge]

        return total

    mst = []
    tree = defaultdict(list)

    while len(mst) != m - 1 and len(edges) != 0:
        u,v,w = edges.pop()
        edge = Edge(u,v,w)
        a = forest.find(position[u])
        b = forest.find(position[v])

        if a != b:
            mst.append(edge)
            tree[u].append(edge)
            tree[v].append(edge)
            forest.union(a,b)

    d_edges = {x:0 for x in mst}

    dfs(next(iter(tree)))

    results = [(d_edges[e] * (n - d_edges[e])) for e in mst]

    sum = 0
    for i in range(len(results)):
        sum += results[i] * (1 << mst[i].element())     # 1 << n  ==  2 ** n

    return bin(sum)[2:]

if __name__ == '__main__':
    f = open('../data/johnland-001.txt')

    nm = f.readline().split()

    n = int(nm[0])

    m = int(nm[1])

    edges = []

    forest = Partition()
    position = {}
    for i in range(m):
        position[i+1] = forest.make_group(i+1)
        edges.append([int(x) for x in f.readline().split()])

    result = roadsInHackerland(n, sorted(edges, key=lambda edge: edge[2], reverse=True))

    print(result)
