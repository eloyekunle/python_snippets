def getWays(n, c):
    """
    Problem: https://www.hackerrank.com/challenges/coin-change/problem
    :param n:
    :param c:
    :return:
    """
    c.sort(reverse=True)
    if n == 0:
        return 1
    elif (n < 0) or (len(c) == 0):
        return 0
    else:
        return getWays(n, c[1:]) + getWays(n - c[0], c)


from collections import defaultdict


def get_ways_memoized(n, c, ways):
    if n == 0:
        return 1
    elif (n < 0) or (len(c) == 0):
        return 0
    elif n in ways and len(c) in ways[n]:
        return ways[n][len(c)]
    else:
        way = get_ways_memoized(n, c[1:], ways) + get_ways_memoized(n - c[0], c, ways)
        ways[n][len(c)] = way
        return way


if __name__ == '__main__':
    # assert getWays(4, [1, 2, 3]) == 4
    # assert getWays(10, [2, 5, 3, 6]) == 5
    assert get_ways_memoized(4, [1, 2, 3], defaultdict(dict)) == 4
    assert get_ways_memoized(10, [2, 5, 3, 6], defaultdict(dict)) == 5
