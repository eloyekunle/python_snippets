class HeapPriorityQueueBase:
    class Locator:
        __slots__ = "_key", "_value", "_index"

        def __init__(self, k, v, j):
            self._key = k
            self._value = v
            self._index = j

        def __lt__(self, other):
            return self._key < other._key

    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2

    def _has_right(self, j):
        return self._right(j) < len(self)

    def _has_left(self, j):
        return self._left(j) < len(self)

    def _parent(self, j):
        return (j - 1) // 2

    def _swap(self, n, m):
        self._data[n], self._data[m] = self._data[m], self._data[n]
        self._data[n]._index = n
        self._data[m]._index = m

    def _bubble(self, j):
        raise NotImplementedError("Implement, Yo!")

    __slots__ = "_data", "_kv"

    def __init__(self, kv=True):
        self._data = []
        self._kv = kv

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self) == 0

    def remove(self, loc: Locator):
        j = loc._index
        if not (0 <= j < len(self) and self._data[j] == loc):
            raise ValueError("Invalid Locator")
        if j == len(self) - 1:
            self._data.pop()
        else:
            self._swap(j, len(self) - 1)
            self._data.pop()
            self._bubble(j)
        if not self._kv:
            return loc._key
        return loc._key, loc._value

    def update(self, loc: Locator, newkey, newvalue=None):
        j = loc._index
        if not (0 <= j < len(self) and self._data[j] == loc):
            raise ValueError("Invalid Locator")
        self._data[j]._key = newkey
        if newvalue is not None:
            self._data[j]._value = newvalue
        self._bubble(j)

    def add(self, key, value=None):
        token = self.Locator(key, value, len(self._data))
        self._data.append(token)
        self._bubble(len(self._data) - 1)
        return token

    def top_loc(self):
        if self.is_empty():
            raise IndexError("PQ is empty.")
        return self._data[0]

    def top(self):
        val = self.top_loc()
        if not self._kv:
            return val._key
        return val._key, val._value

    def remove_top(self):
        if self.is_empty():
            raise IndexError("PQ is empty.")
        self._swap(0, len(self) - 1)
        item = self._data.pop()
        self._bubble(0)
        if not self._kv:
            return item._key
        return item._key, item._value


class MinHeapPriorityQueue(HeapPriorityQueueBase):
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

    def _bubble(self, j):
        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)


class MaxHeapPriorityQueue(HeapPriorityQueueBase):
    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] > self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            big_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] > self._data[left]:
                    big_child = right
            if self._data[j] < self._data[big_child]:
                self._swap(j, big_child)
                self._downheap(big_child)

    def _bubble(self, j):
        if j > 0 and self._data[j] > self._data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)
