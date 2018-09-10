class Stack:
    def __init__(self):
        self._items = []
    def __len__(self):
        return len(self._items)
    def push(self, x):
        self._items.append(x)
    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty.')
        return self._items.pop()
    def top(self):
        if self.is_empty():
            raise IndexError('Stack is empty.')
        return self._items[-1]
    def is_empty(self):
        return len(self._items) == 0