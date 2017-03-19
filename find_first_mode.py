# an algorithm that finds a mode in a list of nondecreasing integers.


def find_mode(numbers):
    mode = None
    count = 1
    length = len(numbers) - 1
    i = 0
    while i < length:
        old_mode = mode
        old_count = count
        count = 1
        mode = numbers[i]
        j = 1

        while (i + j) <= length and numbers[i] == numbers[i + j]:
            j += 1
            count += 1

        if count <= old_count:
            mode = old_mode
            count = old_count

        i += j

    return mode


def find_mode2(numbers):
    modecount = 0
    length = len(numbers) - 1
    i = 0
    while i < length:
        count = 1
        value = numbers[i]

        while i <= length and numbers[i] == value:
            i += 1
            count += 1

        if count > modecount:
            mode = value
            modecount = count

    return mode


nums = list(map(int, input("Enter space-separated integers: ").split(", ")))
the_mode = find_mode2(nums)
if the_mode is None:
    message = "No mode found"
else:
    message = "The mode is " + str(the_mode)
print(message)
