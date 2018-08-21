"""
Problem: https://www.hackerrank.com/challenges/maximum-element/problem
"""
stack = []
items = int(input())
for _ in range(items):
    query = list(map(int, input().split()))
    type = query[0]
    if type == 1:
        if len(stack) == 0:
            stack.append(query[1])
        else:
            stack.append(max(stack[-1], query[1]))
    elif type == 2:
        stack.pop()
    elif type == 3:
        print(stack[-1])
