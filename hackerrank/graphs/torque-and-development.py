#!/bin/python3

class Graph:
    class Edge:
        __slots__ = '_origin', '_destination', '_element'

        def __init__(self, u, v, x):
            self._origin = u
            self._destination = v
            self._element = x

        def endpoints(self):
            return self._origin, self._destination

        def opposite(self, v):
            return self._destination if v is self._origin else self._origin

        def element(self):
            return self._element

        def __hash__(self):  # will allow edge to be a map/set key
            return hash((self._origin, self._destination))

        def __str__(self):
            return '({0},{1},{2})'.format(self._origin, self._destination, self._element)

    def __init__(self):
        self._outgoing = {}

    def _validate_vertex(self, v):
        if v not in self._outgoing:
            raise ValueError('Vertex does not belong to this graph.')

    def vertex_count(self):
        return len(self._outgoing)

    def vertices(self):
        return self._outgoing.keys()

    def edge_count(self):
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total // 2

    def edges(self):
        result = set()  # avoid double-reporting edges of undirected graph
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())  # add edges to resulting set
        return result

    def get_edge(self, u, v):
        self._validate_vertex(u)
        self._validate_vertex(v)
        return self._outgoing[u].get(v)  # returns None if v not adjacent

    def degree(self, v):
        self._validate_vertex(v)
        adj = self._outgoing
        return len(adj[v])

    def incident_edges(self, v):
        self._validate_vertex(v)
        adj = self._outgoing
        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, x=None):
        self._outgoing[x] = {}

    def insert_edge(self, u, v, x=None):
        if self.get_edge(u, v) is not None:  # includes error checking
            raise ValueError('u and v are already adjacent')
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e


def dfs(g : Graph, u, discovered):
    for e in g.incident_edges(u):
        v = e.opposite(u)
        if v not in discovered:
            discovered[u] = e
            dfs(g, v, discovered)

def dfs_complete(g : Graph):
    forest = {}
    for u in g.vertices():
        if u not in forest:
            forest[u] = None
            dfs(g, u, forest)
    return forest

# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    v = dfs_complete(cities)
    return v


if __name__ == '__main__':
    fptr = open('../../data/torque-and-development-001.txt')

    q = int(fptr.readline())
    graph = Graph()

    for q_itr in range(q):
        nmC_libC_road = fptr.readline().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        for i in range(n):
            graph.insert_vertex(i)

        for _ in range(m):
            cities = list(map(int, fptr.readline().rstrip().split()))
            graph.insert_edge(cities[0] - 1, cities[1] - 1)

        result = roadsAndLibraries(n, c_lib, c_road, graph)

        print(result)