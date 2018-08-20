def solution(A):
    """
    https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/
    :param A:
    :return:
    """
    length = len(A)
    perms = [0] * length
    for el in A:
        if not 1 <= el <= length:
            return 0
        else:
            if perms[el - 1] != 0:
                return 0
            perms[el - 1] = 1
    return 1


if __name__ == '__main__':
    assert solution([4, 1, 3, 2]) == 1
    assert solution([4, 1, 3]) == 0
