# An algorithm that takes as input a list of n integers in nondecreasing order and produces the list of all
# values that occur more than once.


def count_occurences(numbers):
    occurences = {}
    i = 0
    while i < len(numbers) - 1:
        occurences[numbers[i]] = 1  # Every num has at least an occurence
        while numbers[i] == numbers[i + 1]:     # Compare with following number
            occurences[numbers[i]] += 1
            i += 1
        if occurences[numbers[i]] == 1:     # Delete every number that has a single occurence
            del occurences[numbers[i]]
        i += 1

    return occurences


numbers = list(map(int, input("Enter a nondecreasing list of numbers, separated by a space: ").split()))
occurences = count_occurences(numbers)
for key, value in occurences.items():
    print(key, "=", value, "times.")
