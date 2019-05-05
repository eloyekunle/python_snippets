# an algorithm that finds the first term of a sequence of positive integers that is less than the immediately preceding
# term of the sequence.


def find_decrease(nums):
    location = 0
    i = 1
    length = len(nums)
    while i < length and location == 0:
        if nums[i] < nums[i - 1]:
            location = i
        else:
            i += 1

    return location


the_numbers = list(map(int, input("Enter space-separated integers: ").split()))
decrease = find_decrease(the_numbers)
print("The first decrease is at index", decrease)
