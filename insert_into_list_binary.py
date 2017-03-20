# an algorithm based on the binary search for determining the correct position in which to insert a new
# element in an already sorted list.


def insert_binary(key, numbers):
    i = 0
    j = len(numbers) - 1

    while i < j:
        middle = (i + j) // 2
        if key > middle:
            i = middle + 1
        else:
            j = middle
