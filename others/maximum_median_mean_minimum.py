# a naiive algorithm that produces the maximum, median, mean, and minimum of a set of three integers.


def statistics(numbers):
    x = numbers[0]
    y = numbers[1]
    z = numbers[2]
    mean = (x + y + z) / 3
    if x <= y <= z:
        minimum = x
        maximum = z
        median = y
    elif x <= z <= y:
        minimum = x
        maximum = y
        median = z
    elif y <= x <= z:
        minimum = y
        maximum = z
        median = x
    elif y <= z <= x:
        minimum = y
        maximum = x
        median = z
    elif z <= x <= y:
        minimum = z
        maximum = y
        median = x
    elif z <= y <= x:
        minimum = z
        maximum = x
        median = y

    return mean, minimum, maximum, median


nums = list(map(int, input("Enter three space-separated integers: ").split()))
mean, minimum, maximum, median = statistics(nums)
print("Mean:", mean, "\nMinimum:", minimum, "\nMaximum:", maximum, "\nMedian", median)
