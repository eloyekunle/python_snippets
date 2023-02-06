from typing import Set


class Graph:
    class Edge:
        __slots__ = "_origin", "_destination", "_element"

        def __init__(self, u, v, x):
            self._origin = u
            self._destination = v
            self._element = x  # sometimes acts as weight for weighted graphs

        def endpoints(self):
            return self._origin, self._destination  # Order matters yo!

        def opposite(self, v):
            return self._destination if v == self._origin else self._origin

        def element(self):
            return self._element

        def __hash__(self):  # will allow edge to be a map/set key
            return hash((self._origin, self._destination))

    def __init__(self, directed=False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        return self._incoming is not self._outgoing  # directed if maps are distinct

    def vertex_count(self):
        return len(self._outgoing)

    def vertices(self):
        return self._outgoing.keys()

    def edge_count(self):
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed() else total // 2

    def edges(self, outgoing=True) -> Set[Edge]:
        result = set()  # avoid double-reporting edges of undirected graph
        adj = self._outgoing if outgoing else self._incoming
        for secondary_map in adj.values():
            result.update(secondary_map.values())  # add edges to resulting set
        return result

    def get_edge(self, u, v):
        return self._outgoing[u].get(v)

    def degree(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, v=None):
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}  # need distinct map for incoming edges
        return v

    def insert_edge(self, u, v, x=None):
        edge = self.get_edge(u, v)
        if edge is not None and edge.element() < x:  # includes error checking
            return
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e
