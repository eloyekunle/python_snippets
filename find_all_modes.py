def find_modes(numbers):
    modecount = 0
    length = len(numbers)
    i = 0
    modes = []
    while i < length:
        count = 1
        value = numbers[i]

        while i < length and numbers[i] == value:
            i += 1
            count += 1

        if count >= modecount:
            if count > modecount:
                mode = value
                modes = [mode]
                modecount = count
            elif count == modecount:
                mode = value
                modes.append(mode)

    return modes


nums = list(map(int, input("Enter space-separated integers: ").split()))
the_mode = find_modes(nums)
print("The modes are:", the_mode)
