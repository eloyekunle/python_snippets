def bubble_sort(nums_array):
    array_length = len(nums_array)
    for i in range(1, array_length):
        print("\n" + str(i), "Pass\n")
        print(nums_array)
        print("\n")
        for j in range(array_length - i):
            if nums_array[j] > nums_array[j+1]:
                nums_array[j], nums_array[j+1] = nums_array[j+1], nums_array[j]
                print(i, j, nums_array)


# The smart bubble sort quits if no swaps were made in the last pass. This means that the sequence is sorted already.
def smart_bubble_sort(nums_array):
    length = len(nums_array)
    swap = True
    i = 1
    while i < length and swap:
        print("\n" + str(i), "Pass\n")
        print(nums_array)
        print("\n")
        swap = False
        for j in range(length - i):
            if nums_array[j] > nums_array[j+1]:
                nums_array[j], nums_array[j+1] = nums_array[j+1], nums_array[j]     # Swap
                swap = True
                print(i, j, nums_array)

nums = list(map(int, input("Enter numbers, separated by space: ").split()))
smart_bubble_sort(nums)
