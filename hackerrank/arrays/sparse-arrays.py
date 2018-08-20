from collections import Counter

def matchingStrings(strings, queries):
    """
    Problem: https://www.hackerrank.com/challenges/sparse-arrays/problem
    :param strings:
    :param queries:
    :return:
    """
    occurs = Counter(strings)
    return [occurs[query] for query in queries]
