# An algorithm that inserts an integer x in the appropriate position into the list a 1 , a 2 , . . . , a n of integers
# that are in increasing order.


def insert_into_sequence(number_to_insert, numbers):
    i = 0
    length = len(numbers)
    while i < length:
        if number_to_insert > numbers[i]:
            i += 1
        else:
            temp = numbers[length - 1]
            numbers.append(temp)
            j = 0
            while j < length - i:
                numbers[length - j] = numbers[length - j - 1]
                j += 1
            numbers[i] = number_to_insert
            return numbers


def insert_into_sequence2(number_to_insert, numbers):
    numbers.append(number_to_insert)
    i = 0
    length = len(numbers)
    while number_to_insert > numbers[i]:
        i += 1
    for j in range(1, length - i):
        numbers[length - j] = numbers[length - j - 1]
    numbers[i] = number_to_insert
    return numbers


nums = list(map(int, input("Enter space-separated sequence: ").split()))
to_insert = int(input("Enter number to insert: "))
print(insert_into_sequence2(to_insert, nums))
