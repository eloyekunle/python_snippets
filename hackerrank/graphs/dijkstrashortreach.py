#!/bin/python3

import math
import os
import random
import re
import sys
from data_structures import heap, graph_no_vertice_object as graph

# Complete the shortestReach function below.
def shortestReach(n, g, s):
    cloud = {}
    distances[s] = 0
    pq.update(pq_loc[s], 0)

    while not pq.is_empty():
        k,u = pq.remove_top()
        cloud[u] = k
        del pq_loc[u]
        for e in g.incident_edges(u):
            v = e.opposite(u)
            if v not in cloud:
                dist = e.element() + distances[u]
                if dist < distances[v]:
                    distances[v] = dist
                    pq.update(pq_loc[v], dist)

    output = []
    for i in range(1, n + 1):
        if i != s:
            if distances[i] != math.inf:
                output.append(distances[i])
            else:
                output.append(-1)

    return output

if __name__ == '__main__':
    f = open('../data/dijkstrashortreach-001.txt')

    t = int(f.readline())

    for t_itr in range(t):
        g = graph.Graph()

        nm = f.readline().split()

        n = int(nm[0])

        m = int(nm[1])

        pq = heap.MinHeapPriorityQueue()

        pq_loc = {}

        distances = {}

        for i in range(1, n + 1):
            g.insert_vertex(i)
            distances[i] = math.inf
            pq_loc[i] = pq.add(distances[i], i)

        for _ in range(m):
            # Submission replaced input() with sys.stdin.readline() to optimize I/O, otherwise getting timeout.
            g.insert_edge(*map(int, f.readline().rstrip().split()))

        s = int(f.readline())

        result = shortestReach(n, g, s)

        print(' '.join(map(str, result)))
