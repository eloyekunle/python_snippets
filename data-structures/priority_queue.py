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