def twoStacks(x, a, b):
    total_sum = i = j = 0
    stack_a = []
    len_a = len(a)
    while i < len_a and (total_sum + a[-1]) <= x:
        el = a.pop()
        total_sum += el
        stack_a.append(el)
        i += 1

    count = i
    stack_b = []
    len_b = len(b)
    while j < len_b and i >= 0:
        el = b.pop()
        total_sum += el
        stack_b.append(el)
        j += 1
        while total_sum > x and i > 0:
            i -= 1
            total_sum -= stack_a[i]
            stack_a[i] = None
        if total_sum <= x and i+j > count:
            count = i + j
    return count


if __name__ == '__main__':
    assert twoStacks(91,
                     [18, 14, 13, 12, 0, 8, 16, 1, 17, 3, 3, 2, 4],
                     [3, 2, 19, 3, 7, 2, 14, 10, 10, 2, 16, 8, 13, 6, 0, 1, 10, 14, 16, 3, 0, 17, 17, 7, 13, 16, 7, 17, 3, 10, 1, 0, 15, 17, 17, 17, 12, 19, 2, 1, 9, 10, 8, 0, 15, 14, 13, 7, 14]) == 12
