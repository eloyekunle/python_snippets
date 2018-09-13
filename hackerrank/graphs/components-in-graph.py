#!/bin/python3

import os
import sys
from collections import defaultdict

class Partition:
    class Position:
        __slots__ = '_container', '_element', '_size', '_parent'

        def __init__(self, container, e):
            self._container = container         # reference to Partition instance
            self._element = e
            self._size = 1
            self._parent = self                 # convention for a group leader

        def element(self):
            return self._element

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')

    def make_group(self, e):
        return self.Position(self, e)

    def find(self, p):
        self._validate(p)
        if p._parent != p:
            p._parent = self.find(p._parent)    # overwrite p._parent after recursion
        return p._parent

    def union(self, p, q):
        a = self.find(p)
        b = self.find(q)
        if a is not b:                        # only merge if different groups
            if a._size > b._size:
                b._parent = a
                a._size += b._size
            else:
                a._parent = b
                b._size += a._size

class Graph:
    class Edge:
        __slots__ = '_origin', '_destination'

        def __init__(self, u, v):
            self._origin = u
            self._destination = v

        def endpoints(self):
            return self._origin, self._destination

        def opposite(self, v):
            return self._destination if v == self._origin else self._origin

        def __hash__(self):  # will allow edge to be a map/set key
            return hash((self._origin, self._destination))

        def __str__(self):
            return '({0},{1})'.format(self._origin, self._destination)

    def __init__(self):
        self._outgoing = defaultdict(dict)

    def vertices(self):
        return self._outgoing.keys()

    def get_edge(self, u, v):
        return self._outgoing[u].get(v)  # returns None if v not adjacent

    def incident_edges(self, v):
        adj = self._outgoing
        for edge in adj[v].values():
            yield edge

    def insert_edge(self, u, v):
        if self.get_edge(u, v) is not None:  # includes error checking
            raise ValueError('u and v are already adjacent')
        e = self.Edge(u, v)
        self._outgoing[u][v] = e
        self._outgoing[v][u] = e
#
# Complete the componentsInGraph function below.
#
def componentsInGraph(gb):
    forest = Partition()
    p = {}
    for v in gb.vertices():
        p[v] = forest.make_group(v)

    for

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    gb = Graph()

    for _ in range(n):
        gb.insert_edge(*map(int, input().rstrip().split()))

    result = componentsInGraph(gb)

    fptr.write(' '.join(map(str, SPACE)))
    fptr.write('\n')

    fptr.close()
