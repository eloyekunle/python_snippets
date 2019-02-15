import os

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

        def __len__(self):
            return self._size

        def __lt__(self, other):
            return len(self) < len(other)

    def __init__(self):
        self._data = {}

    def __len__(self):
        return len(self._data)

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')

    def make_group(self, e):
        position = self.Position(self, e)
        self._data[e] = position
        return position

    def find(self, p):
        self._validate(p)
        if p._parent != p:
            p._parent = self.find(p._parent)    # overwrite p._parent after recursion
        return p._parent

    def positions(self):
        return self._data.values()

    def union(self, p, q):
        a = self.find(p)
        b = self.find(q)
        if a is not b:                        # only merge if different groups
            if a > b:
                b._parent = a
                a._size += b._size
                if b.element() in self._data:
                    del self._data[b.element()]
            else:
                a._parent = b
                b._size += a._size
                if a.element() in self._data:
                    del self._data[a.element()]

# Complete the journeyToMoon function below.
def journeyToMoon(n, astronaut):
    forest = Partition()
    p = {}
    for i in range(n):
        p[i] = forest.make_group(i)

    for a in astronaut:
        forest.union(forest.find(p[a[0]]), forest.find(p[a[1]]))

    vs = [len(x) for x in forest.positions()]

    c_sum = 0
    result = 0
    for s in vs:
        result += c_sum*s
        c_sum += s
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    np = input().split()

    n = int(np[0])

    p = int(np[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
