from collections import defaultdict

# Complete the longestCommonSubsequence function below.
def longestCommonSubsequence(a, b):
    len_a = len(a)
    len_b = len(b)
    c = defaultdict(lambda: defaultdict(int))
    for i in range(1, len_a + 1):
        for j in range(1, len_b + 1):
            if a[i-1] == b[j-1]:
                val = c[i-1][j-1] + 1
            else:
                val = max(c[i-1][j], c[i][j-1])
            c[i][j] = val

    return constructLCS(c, a, b, i, j, [])

def constructLCS(c, a, b, i, j, w):
    if c[i][j] == 0:
        return
    if a[i-1] == b[j-1]:
        constructLCS(c, a, b, i-1, j-1, w)
        w.append(a[i-1])
    elif c[i][j-1] > c[i-1][j]:
        constructLCS(c, a, b, i, j-1, w)
    else:
        constructLCS(c, a, b, i-1, j, w)
    return w

if __name__ == '__main__':
    f = open('/home/elijah/MyCode/python_snippets/data/dynamic-programming-classics-the-longest-common-subsequence-001.txt')
    nm = f.readline().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, f.readline().rstrip().split()))

    b = list(map(int, f.readline().rstrip().split()))

    result = longestCommonSubsequence(a, b)

    print(' '.join(map(str, result)))
