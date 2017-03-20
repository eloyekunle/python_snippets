def insertion_sort(nums_array):
    for i in range(1, len(nums_array)):
        print(nums_array)
        j = 0

        while nums_array[i] > nums_array[j]:
            j += 1

        temp = nums_array[i]

        for k in range(i - j):
            # print(nums_array)
            nums_array[i - k] = nums_array[i - k - 1]

        nums_array[j] = temp

    print(nums_array)

nums = list(map(int, input("Enter numbers, separated by space: ").split()))
insertion_sort(nums)
