
def solution(A):
    N = len(A)
    for target in A:
        while target != A[target]:
            target, A[target] = A[target], target

    for cursor in range(N):
        if A[cursor] != cursor:
            return cursor
    return N


if __name__ == '__main__':
    assert solution([1, 3, 6, 4, 1, 2]) == 5
