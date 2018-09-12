#!/bin/python3

import math
import os
import random
import re
import sys
class PriorityQueueBase:
    class _Item:
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key

    def is_empty(self):
        return len(self) == 0

class HeapPriorityQueue(PriorityQueueBase):
    def _left(self, j):
        return 2*j + 1

    def _right(self, j):
        return 2*j + 2

    def _has_right(self, j):
        return self._right(j) < len(self)

    def _has_left(self, j):
        return self._left(j) < len(self)

    def _parent(self, j):
        return (j - 1) // 2

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[j] > self._data[small_child]:
                self._swap(j, small_child)
                self._downheap(small_child)

    def _swap(self, n, m):
        self._data[n], self._data[m] = self._data[m], self._data[n]

    __slots__ = '_data'

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def min(self):
        if self.is_empty():
            raise IndexError('PQ is empty.')
        min_val = self._data[0]
        return min_val._key, min_val._value

    def remove_min(self):
        if self.is_empty():
            raise IndexError('PQ is empty.')
        self._swap(0, len(self) - 1)
        item = self._data.pop()
        self._downheap(0)
        return item._key, item._value

    def add(self, key, value):
        item = self._Item(key, value)
        self._data.append(item)
        self._upheap(len(self) - 1)

class AdaptableHeapPriorityQueue(HeapPriorityQueue):
    class Locator(HeapPriorityQueue._Item):
        __slots__ = '_index'

        def __init__(self, k, v, j):
            super().__init__(k, v)
            self._index = j

    def _swap(self, n, m):
        super()._swap(n, m)
        self._data[n]._index = n
        self._data[m]._index = m

    def _bubble(self, j):
        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)

    def add(self, key, value):
        token = self.Locator(key, value, len(self._data))
        self._data.append(token)
        self._upheap(len(self._data) - 1)
        return token

    def update(self, loc : Locator, newkey, newvalue):
        j = loc._index
        if not (0 <= j < len(self) and self._data[j] == loc):
            raise ValueError('Invalid Locator')
        self._data[j]._key = newkey
        self._data[j]._value = newvalue
        self._bubble(j)

    def remove(self, loc : Locator):
        j = loc._index
        if not (0 <= j < len(self) and self._data[j] == loc):
            raise ValueError('Invalid Locator')
        if j == len(self) - 1:
            self._data.pop()
        else:
            self._swap(j, len(self) - 1)
            self._data.pop()
            self._bubble(j)
        return loc._key, loc._value

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
    pq = AdaptableHeapPriorityQueue()
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
        k,v = pq.remove_min()
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
    f = open('../../data/primsmstsub-002.txt')

    nm = f.readline().split()

    n = int(nm[0])

    m = int(nm[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, f.readline().rstrip().split())))

    start = int(f.readline())

    result = prims(n, edges, start)

    print(result)