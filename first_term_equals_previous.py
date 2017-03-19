# an algorithm that finds the first term of a sequence of integers that equals some previous term in the sequence.


# Searches previous numbers using linear search
def first_duplicate(numbers):
    i = 0
    location = 0
    length = len(numbers)
    while i < length and location == 0:
        j = 0
        while j < i and location == 0:
            if numbers[i] == numbers[j]:
                location = i
            else:
                j += 1
        i += 1

    return location


nums = list(map(int, input("Enter space-separated numbers: ").split()))
first_term_equals_previous_term = first_duplicate(nums)
if first_term_equals_previous_term == 0:
    print("No duplicate found")
else:
    print("First duplicate found at:", first_term_equals_previous_term)
