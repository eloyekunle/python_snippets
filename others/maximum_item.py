nums = list(map(int, input("Enter numbers, separated by space\n").split()))

def find_max(array):
    max_num = 0
    for num in nums:
        if num > max_num:
            max_num = num
            # print("Current max is:" + str(max_num))

    return max_num

maximum = find_max(nums)
print ("Max is:", maximum)
