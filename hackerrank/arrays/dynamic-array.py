def dynamicArray(n, queries):
    """
    Problem statement: https://www.hackerrank.com/challenges/dynamic-array/problem
    :param n:
    :param queries:
    :return:
    """
    seqList = [[] for i in range(n)]
    lastAnswer = 0
    array = []
    for query in queries:
        query_type = query[0]
        x = query[1]
        y = query[2]
        print((x^lastAnswer) % n)
        if query_type == 1:
            seqList[(x^lastAnswer) % n].append(y)
        elif query_type == 2:
            seq = seqList[(x^lastAnswer) % n]
            lastAnswer = seq[y % len(seq)]
            array.append(lastAnswer)

    return array
