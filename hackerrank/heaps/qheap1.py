class HeapPriorityQueue:
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

    def is_empty(self):
        return len(self) == 0

    def min(self):
        if self.is_empty():
            raise IndexError('PQ is empty.')
        return self._data[0]

    def remove_min(self):
        if self.is_empty():
            raise IndexError('PQ is empty.')
        self._swap(0, len(self) - 1)
        item = self._data.pop()
        self._downheap(0)
        return item

    def add(self, key):
        self._data.append(key)
        self._upheap(len(self) - 1)

class AdaptableHeapPriorityQueue(HeapPriorityQueue):
    class Locator:
        __slots__ = '_index', '_key'

        def __init__(self, k, j):
            self._key = k
            self._index = j

        def __lt__(self, other):
            return self._key < other._key

    def _swap(self, n, m):
        super()._swap(n, m)
        self._data[n]._index = n
        self._data[m]._index = m

    def _bubble(self, j):
        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)

    def add(self, key):
        token = self.Locator(key, len(self._data))
        self._data.append(token)
        self._upheap(len(self._data) - 1)
        return token

    def update(self, loc : Locator, newkey):
        j = loc._index
        if not (0 <= j < len(self) and self._data[j] == loc):
            raise ValueError('Invalid Locator')
        self._data[j]._key = newkey
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
        return loc._key

h = AdaptableHeapPriorityQueue()
locators = {}
for _ in range(int(input())):
    ops = [int(val) for val in input().split()]
    op_type = ops[0]

    if op_type == 1:
        val = ops[1]
        locators[val] = h.add(val)
    elif op_type == 2:
        val = ops[1]
        h.remove(locators[val])
    else:
        print(h.min()._key)