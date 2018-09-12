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

    def _downheap(self, j):

    def _swap(self, n, m):
        self._data[n], self._data[m] = self._data[m], self._data[n]

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def min(self):
        min_val = self._data[0]
        return min_val._key, min_val._value

    def remove_min(self):

    def add(self, key, value):


class AdaptableHeapPriorityQueue(HeapPriorityQueue):
    pass