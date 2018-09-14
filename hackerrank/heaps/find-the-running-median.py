#!/usr/bin/python3

import os
import sys
from data_structures import heap

def runningMedian(a):
    medians = []
    min_heap = heap.MinHeapPriorityQueue(False)
    max_heap = heap.MaxHeapPriorityQueue(False)

    for num in a:
        if len(medians) == 0 or num >= medians[-1]:
            min_heap.add(num)
        else:
            max_heap.add(num)

        while not -1 <= (len(min_heap) - len(max_heap)) <= 1:
            if len(min_heap) > len(max_heap):
                max_heap.add(min_heap.remove_top())
            else:
                min_heap.add(max_heap.remove_top())

        if (len(min_heap) + len(max_heap)) % 2 == 0:
            median = (min_heap.top() + max_heap.top()) / 2
        elif len(min_heap) > len(max_heap):
            median = min_heap.top()
        else:
            median = max_heap.top()

        medians.append(median)
    return medians

def runningMedianNaive(a):
    medians = []
    for i in range(1, len(a) + 1):
        array = a[:i]
        array.sort()
        if i % 2 == 0:
            median = (array[(i // 2) - 1] + array[i // 2]) / 2
        else:
            median = array[i // 2]
        medians.append(median)
    return medians

if __name__ == '__main__':
    f = open('../data/find-the-running-median-001.txt')
    a_count = int(f.readline())
    s = open('../data/find-the-running-median-001.sol.txt').readlines()
    a = []

    for _ in range(a_count):
        a_item = float(f.readline())
        a.append(a_item)

    result = runningMedian(a)
    print(result)