import math
import os
import random
import re
import sys
from collections import deque
from data_structures import graph_no_vertice_object as graph

# Complete the bfs function below.
def bfs(n, m, g, s):
    distances = {s: 0}
    discovered = deque([s])

    while len(discovered) != 0:
        u = discovered.popleft()
        for e in g.incident_edges(u):
            v = e.opposite(u)
            if v not in distances:
                distances[v] = distances[u] + 1
                discovered.append(v)

    output = []
    for i in range(1, n + 1):
        if i != s:
            if i in distances:
                output.append(distances[i] * 6)
            else:
                output.append(-1)
    return output

if __name__ == '__main__':
    f = open('../../data/bfsshortreach-001.txt')
    sol = [list(map(int, y.rstrip().split())) for y in open('../../data/bfsshortreach-001.sol.txt').readlines()]

    q = int(f.readline())

    for q_itr in range(q):
        g = graph.Graph()
        nm = f.readline().split()

        n = int(nm[0])

        m = int(nm[1])

        for i in range(n):
            g.insert_vertex_simple(i + 1)

        for _ in range(m):
            edges = list(map(int, f.readline().rstrip().split()))
            g.insert_edge(*edges)

        s = int(f.readline())

        result = bfs(n, m, g, s)
        cur_sol = sol[q_itr]
        print(result)
        assert result == cur_sol