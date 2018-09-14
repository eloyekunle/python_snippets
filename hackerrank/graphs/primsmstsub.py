#!/bin/python3

import math
import os
import random
import re
import sys
from data_structures import heap

class Graph:
    class Edge:
        __slots__ = '_origin', '_destination', '_element'

        def __init__(self, u, v, x):
            self._origin = u
            self._destination = v
            self._element = x

        def element(self):
            return self._element

        def endpoints(self):
            return self._origin, self._destination

        def opposite(self, v):
            return self._destination if v == self._origin else self._origin

        def __hash__(self):  # will allow edge to be a map/set key
            return hash((self._origin, self._destination))

        def __str__(self):
            return '({0},{1})'.format(self._origin, self._destination)

    def __init__(self):
        self._outgoing = {}

    def _validate_vertex(self, v):
        if v not in self._outgoing:
            raise ValueError('Vertex does not belong to this graph.')

    def vertices(self):
        return self._outgoing.keys()

    def get_edge(self, u, v):
        self._validate_vertex(u)
        self._validate_vertex(v)
        return self._outgoing[u].get(v)  # returns None if v not adjacent

    def incident_edges(self, v):
        self._validate_vertex(v)
        adj = self._outgoing
        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, x=None):
        self._outgoing[x] = {}

    def insert_edge(self, u, v, x=None):
        if self.get_edge(u, v) is not None and self.get_edge(u, v).element() < x:  # includes error checking
            return
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self._outgoing[v][u] = e

# Complete the prims function below.
def prims(n, edges, start):
    d = {}
    pq = heap.MinHeapPriorityQueue()
    pqlocator = {}
    tree = []
    g = Graph()

    for i in range(1, n + 1):
        if i == start:
            d[start] = 0
        else:
            d[i] = math.inf
        pqlocator[i] = pq.add(d[i], (i, None))
        g.insert_vertex(i)

    for j in range(m):
        g.insert_edge(*edges[j])

    while not pq.is_empty():
        k,v = pq.remove_top()
        u,e = v
        del pqlocator[u]
        if e is not None:
            tree.append(e)
        for edge in g.incident_edges(u):
            v = edge.opposite(u)
            if v in pqlocator:
                wt = edge.element()
                if wt < d[v]:
                    d[v] = wt
                    pq.update(pqlocator[v], d[v], (v, edge))
    return sum(edge.element() for edge in tree)

if __name__ == '__main__':
    f = open('../data/primsmstsub-002.txt')

    nm = f.readline().split()

    n = int(nm[0])

    m = int(nm[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, f.readline().rstrip().split())))

    start = int(f.readline())

    result = prims(n, edges, start)

    print(result)