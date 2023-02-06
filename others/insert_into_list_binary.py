# an algorithm based on the binary search for determining the correct position in which to insert a new
# element in an already sorted list.


def insert_binary(key, numbers):
    i = 0
    numbers.append(key)
    length = len(numbers)
    j = length - 1

    while i < j:
        middle = (i + j) // 2
        if key > numbers[middle]:
            i = middle + 1
            print(numbers[i : j + 1])
        else:
            j = middle
            print(numbers[i : j + 1])
    if key <= numbers[i]:
        location = i
        for k in range(1, length - 1):
            numbers[length - k] = numbers[length - k - 1]
        numbers[i] = key
    else:
        location = i + 1
    print("Element will be inserted at", location)
    print(numbers)


nums = list(map(int, input("Enter numbers, separated by space: ").split()))
insert_key = int(input("Enter number to insert: "))
insert_binary(insert_key, nums)
