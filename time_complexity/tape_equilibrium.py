def solution(A):
    left = A[0]
    right = sum(A) - left

    least_diff = abs(right - left)
    for i in range(1, len(A) - 1):
        left += A[i]
        right -= A[i]
        diff = abs(right - left)
        if diff < least_diff:
            least_diff = diff

    return least_diff


if __name__ == '__main__':
    assert solution([3, 1, 2, 4, 3]) == 1
