# Naiive insertion sort
def insertion_sort(nums_array):
    for i in range(1, len(nums_array)):
        # print(nums_array)
        j = 0

        while j <= i and nums_array[i] > nums_array[j]:
            j += 1

        temp = nums_array[i]

        for k in range(i - j):
            # print(nums_array)
            nums_array[i - k] = nums_array[i - k - 1]

        nums_array[j] = temp

    print(nums_array)


# a variation of the insertion sort that uses a linear search technique that inserts the j th element in the
# correct place by first comparing it with the (j − 1)st element, then the (j − 2)th element if necessary, and so on.
def smart_insertion_sort(nums_array):
    for i in range(1, len(nums_array)):
        key = nums_array[i]
        j = i
        while j > 0 and nums_array[j - 1] > key:
            j -= 1

        print("\n", nums_array[i], "will be inserted at", j)

        for k in range(i - j):
            nums_array[i - k] = nums_array[i - k - 1]

        nums_array[j] = key
        print(nums_array)


nums = list(map(int, input("Enter numbers, separated by space: ").split()))
# with open('/home/playmice/MyCode/Python/python_snippets/hackerrank/data/8Kints.txt') as f:
#     nums = [int(i) for i in f]

smart_insertion_sort(nums)
