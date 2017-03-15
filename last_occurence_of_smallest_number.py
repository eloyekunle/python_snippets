# an algorithm that locates the last occurrence of the smallest element in a finite list of integers, where the
# integers in the list are not necessarily distinct.


def last_occurence(numbers):
    smallest = numbers[0]
    index = 0
    length = len(numbers)
    for i in range(1, length - 1):
        if numbers[i] <= smallest:
            smallest = numbers[i]
            index = i

    return smallest, index


nums = list(map(int, input("Enter space-separated numbers: ").split()))
last_occur = last_occurence(nums)
print("The last occurence of", last_occur[0], "is at", last_occur[1])
