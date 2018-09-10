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

if __name__ == '__main__':
    input_stack = Stack()
    output_stack = Stack()
    for _ in range(int(input())):
        ops = input().split()
        op = int(ops[0])
        if op == 1:
            input_stack.push(ops[1])
        else:
            if output_stack.is_empty():
                for _ in range(len(input_stack)):
                    output_stack.push(input_stack.pop())
            if op == 2:
                output_stack.pop()
            else:
                print(output_stack.top())