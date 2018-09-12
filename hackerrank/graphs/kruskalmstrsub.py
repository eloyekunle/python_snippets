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

def kruskalmstrsub(edges):
    tree = []

    while len(tree) != g_edges - 1 and not len(edges) == 0:
        u,v,w = edges.pop()
        a = forest.find(position[u])
        b = forest.find(position[v])

        if a != b:
            tree.append((u,v,w))
            forest.union(a,b)
    return sum(item[2] for item in tree)

if __name__ == '__main__':
    f = open('/home/elijah/Downloads/input04.txt')
    g_nodes, g_edges = map(int, f.readline().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges
    forest = Partition()
    position = {}

    for i in range(g_edges):
        position[i+1] = forest.make_group(i+1)
        g_from[i], g_to[i], g_weight[i] = map(int, f.readline().split())

    result = kruskalmstrsub(sorted(zip(g_from, g_to, g_weight), key=lambda edge: edge[2], reverse=True))
    print(result)
