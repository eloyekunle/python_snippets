def bubble_sort(nums_array):
    array_length = len(nums_array)
    for i in range(1, array_length):
        print("\n" + str(i), "Pass\n")
        print(nums_array)
        print("\n")
        for j in range(array_length - i):
            if nums_array[j] < nums_array[j+1]:
                temp = nums_array[j]
                nums_array[j] = nums_array[j+1]
                nums_array[j+1] = temp
                print(i, j, nums_array)


nums = list(map(int, input("Enter numbers, separated by space: ").split()))
bubble_sort(nums)
