from collections import Counter


def string_construction(s):
    return len(Counter(s))


if __name__ == '__main__':
    assert (string_construction('abcd') == 4)
    assert (string_construction('abab') == 2)
    assert (string_construction('hello') == 4)
    assert (string_construction('maximumumimu') == 5)
