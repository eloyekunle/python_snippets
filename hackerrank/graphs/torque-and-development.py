#!/bin/python3

class Graph:
    class Edge:
        __slots__ = '_origin', '_destination'

        def __init__(self, u, v):
            self._origin = u
            self._destination = v

        def endpoints(self):
            return self._origin, self._destination

        def opposite(self, v):
            return self._destination if v is self._origin else self._origin

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

    def insert_edge(self, u, v):
        if self.get_edge(u, v) is not None:  # includes error checking
            raise ValueError('u and v are already adjacent')
        e = self.Edge(u, v)
        self._outgoing[u][v] = e
        self._outgoing[v][u] = e


def dfs(g : Graph, u, discovered, cur_vertices=None):
    if cur_vertices is None:
        cur_vertices = set()

    cur_vertices.add(u)
    for e in g.incident_edges(u):
        v = e.opposite(u)
        if v not in cur_vertices:
            discovered[v] = e
            dfs(g, v, discovered, cur_vertices)

    return len(cur_vertices)

# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib < c_road:
        return c_lib * n
    forest = {}
    cost = 0
    for u in cities.vertices():
        if u not in forest:
            forest[u] = None
            cluster = dfs(cities, u, forest) - 1
            cost += cluster * c_road + c_lib
    return cost


if __name__ == '__main__':
    fptr = open('/home/elijah/Downloads/input05.txt')

    q = int(fptr.readline())

    for q_itr in range(q):
        graph = Graph()
        nmC_libC_road = fptr.readline().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        for i in range(1, n + 1):
            graph.insert_vertex(i)

        for _ in range(m):
            cities = list(map(int, fptr.readline().rstrip().split()))
            graph.insert_edge(cities[0], cities[1])

        result = roadsAndLibraries(n, c_lib, c_road, graph)

        print(result)