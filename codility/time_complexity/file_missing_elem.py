def solution(A):
    """
    Problem statement: https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/
    :param A:
    :return:
    """
    length = len(A)
    xor_sum = 0
    for i in range(length):
        xor_sum = xor_sum ^ A[i] ^ (i + 1)
    return xor_sum ^ (length + 1)

if __name__ == '__main__':
    assert solution([2, 3, 1, 5]) == 4
