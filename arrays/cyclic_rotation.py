"""
Problem statement: https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation
"""


def solution(A, K):
    len_a = len(A)
    if len_a:
        i = len_a - (K % len_a)
        return A[i:] + A[:i]
    else:
        return A


if __name__ == '__main__':
    assert solution([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8]
    assert solution([1, 2, 3, 4], 4) == [1, 2, 3, 4]
