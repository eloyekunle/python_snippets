# The selection sort begins by finding the least element in the list. This element is moved to the front. Then the least
# element among the remaining elements is found and put into the second position. This procedure is repeated until the
# entire list has been sorted.


def selection_sort(numbers):
    length = len(numbers)
    for i in range(length):
        least = numbers[i]
        least_index = i

        # Get least
        for j in range(i + 1, length):
            if numbers[j] < least:
                least = numbers[j]
                least_index = j

        for k in range(least_index - i):
            numbers[least_index - k] = numbers[least_index - k - 1]
        numbers[i] = least
        # Uncomment following line to view iterations.
        # print(numbers)

    print(numbers)


nums = list(map(int, input("Enter space-separated integers: ").split()))
selection_sort(nums)
