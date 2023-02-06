class Stack:
    def __init__(self):
        self._items = []

    def __len__(self):
        return len(self._items)

    def push(self, x):
        self._items.append(x)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self._items.pop()

    def top(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self._items[-1]

    def is_empty(self):
        return len(self) == 0


class Queue:
    def __init__(self):
        self._input_stack = Stack()
        self._output_stack = Stack()

    def __len__(self):
        return len(self._input_stack) + len(self._output_stack)

    def enqueue(self, x):
        self._input_stack.push(x)

    def dequeue(self):
        self._validate_output_stack()
        return self._output_stack.pop()

    def first(self):
        self._validate_output_stack()
        return self._output_stack.top()

    def is_empty(self):
        return len(self) == 0

    def _validate_output_stack(self):
        if self._output_stack.is_empty():
            for _ in range(len(self._input_stack)):
                self._output_stack.push(self._input_stack.pop())
