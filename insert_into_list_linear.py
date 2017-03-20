# an algorithm based on the linear search for determining the correct position in which to insert a new
# element in an already sorted list.


def insert_linear(key, numbers):
    i = 0
    numbers.append(key)
    length = len(numbers)
    while i < length and key > numbers[i]:
        i += 1
    if i < length:
        # Push all other numbers to the right
        for k in range(1, length - i):
            numbers[length - k] = numbers[length - k - 1]
    print("The element will be inserted at index", i)
    numbers[i] = key
    print(numbers)


nums = list(map(int, input("Enter space-separated integers: ").split()))
to_insert = int(input("Enter integer to insert: "))
insert_linear(to_insert, nums)
