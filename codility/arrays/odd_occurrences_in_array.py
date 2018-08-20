def solution(A):
    """
    Problem Statement: https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/
    """
    result = 0
    for number in A:
        result ^= number
    return result


if __name__ == '__main__':
    assert solution([9, 3, 9, 3, 9, 7, 9]) == 7
    assert solution([1]) == 1
