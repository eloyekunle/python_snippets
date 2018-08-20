from itertools import accumulate

def arrayManipulation(n, queries):
    """
    Problem: https://www.hackerrank.com/challenges/crush/problem
    :param n:
    :param queries:
    :return:
    """
    array = [0 for i in range(n+1)]
    for query in queries:
        x,y,additive = query
        array[x-1] += additive
        array[y] -= additive
    return max(accumulate(array))
