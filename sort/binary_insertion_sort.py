# The binary insertion sort is a variation of the insertion sort that uses a binary search technique rather
# than a linear search technique to insert the ith element in the correct place among the previously sorted elements.


def binary_insertion_sort(numbers):
    length = len(numbers)
    for i in range(1, length):
        j = 0
        k = i
        key = numbers[i]        # Here's our key for now
        # print("Trying to insert", numbers[i])
        while j < k:
            mid = (j + k) // 2
            # print(numbers[j:k+1])
            if key > numbers[mid]:
                j = mid + 1
            else:
                k = mid
        if key <= numbers[j]:
            for l in range(i - j):
                numbers[i - l] = numbers[i - l - 1]
            numbers[j] = key
    # print()
    print(numbers)


nums = list(map(int, input("Enter the space-separated integers: ").split()))
# with open('/home/playmice/MyCode/Python/python_snippets/data/8Kints.txt') as f:
#     nums = [int(i) for i in f]

binary_insertion_sort(nums)
