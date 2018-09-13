#!/bin/python
from collections import defaultdict
from data_structures import heap

def calc_median(a, x):
    pqlocators_min = defaultdict(list)
    pqlocators_max = defaultdict(list)
    min_heap = heap.MinHeapPriorityQueue(False)
    max_heap = heap.MaxHeapPriorityQueue(False)
    medians = []

    def cur_median():
        while abs(len(min_heap) - len(max_heap)) > 1:
            if len(min_heap) > len(max_heap):
                big, small = min_heap, max_heap
                big_pq_loc, small_pq_loc = pqlocators_min, pqlocators_max
            else:
                big, small = max_heap, min_heap
                big_pq_loc, small_pq_loc = pqlocators_max, pqlocators_min

            removed_loc = big.top_loc()
            big.remove_top()
            big_pq_loc[removed_loc._key] = [x for x in big_pq_loc[removed_loc._key] if x._index != removed_loc._index]
            if len(big_pq_loc[removed_loc._key]) == 0:
                del big_pq_loc[removed_loc._key]
            new_loc = small.add(removed_loc._key)
            small_pq_loc[new_loc._key].append(new_loc)

        if len(min_heap) == 0 and len(max_heap) == 0:
            return 'Wrong!'
        elif (len(min_heap) + len(max_heap)) % 2 == 0:
            median = (min_heap.top() + max_heap.top()) / 2
        elif len(min_heap) > len(max_heap):
            median = min_heap.top()
        else:
            median = max_heap.top()

        medians.append(median)
        return int(median) if median % 1 == 0 else median

    for j in range(N):
        val = x[j]
        if a[j] == 'a':
            if len(medians) == 0 or val > medians[-1]:
                new_loc = min_heap.add(val)
                pqlocators_min[val].append(new_loc)
            else:
                new_loc = max_heap.add(val)
                pqlocators_max[val].append(new_loc)
            print(cur_median())
        else:
            if val in pqlocators_min:
                min_heap.remove(pqlocators_min[val].pop())
                if len(pqlocators_min[val]) == 0:
                    del pqlocators_min[val]
                print(cur_median())
            elif val in pqlocators_max:
                max_heap.remove(pqlocators_max[val].pop())
                if len(pqlocators_max[val]) == 0:
                    del pqlocators_max[val]
                print(cur_median())
            else:
                print('Wrong!')

f = open('../../data/median-002.txt')
N = int(f.readline())
s = []
x = []
for i in range(0, N):
    tmp = f.readline().strip().split(' ')
    a, b = [xx for xx in tmp]
    s.append(a)
    x.append(int(b))

calc_median(s,x)