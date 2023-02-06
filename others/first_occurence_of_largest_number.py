# an algorithm that locates the first occurrence of the largest element in a finite list of integers, where the
# integers in the list are not necessarily distinct.


def first_occurence(numbers):
    largest = numbers[0]
    index = 0
    length = len(numbers)
    for i in range(1, length):
        if numbers[i] > largest:
            largest = numbers[i]
            index = i
    return largest, index


nums = list(map(int, input("Enter space separated integers: ").split()))
first_occurence_in_sequence = first_occurence(nums)
print(
    "The first occurence of",
    first_occurence_in_sequence[0],
    "is index",
    first_occurence_in_sequence[1],
)
