"""
https://www.hackerrank.com/challenges/merging-communities/problem
"""
from data_structures.partition_min import Partition

n,q = map(int, input().split())
forest = Partition()
p = {}

for i in range(1, n + 1):
    p[i] = forest.make_group(i)

for _ in range(q):
    op = input().split()
    if op[0] == 'Q':
        print(len(forest.find(p[int(op[1])])))
    else:
        forest.union(forest.find(p[int(op[1])]), forest.find(p[int(op[2])]))