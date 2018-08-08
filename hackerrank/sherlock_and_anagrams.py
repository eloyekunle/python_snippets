"""
Problem Statement: https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem

Given a string, find the number of pairs of substrings of the string which are anagrams of each other.
"""
def sherlockAndAnagrams(string):
    # For every single possible combination of strings (length >= 1), their hashcodes are saved in 'hash_table' with a
    # value that corresponds to the occurrences of *their* possible combinations.
    hash_table = dict()

    hashes = dict()

    # Hash function.
    # Input: Single char
    # Output: Unique hash code int
    def prime_map(c):
        primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101)
        return primes[ord(c) - ord('a')]

    # Computes Hash Code for a string. Uses 'prime_map' to hash each character, and multiplies them together.
    # Anagrams will *ALWAYS* have the same hash with this strategy. This is the key to the whole thing.
    # Optimization: It saves the hash for each string processed (in global 'hashes' dict declared above) to avoid recomputation.
    def get_hash(s):
        if s in hashes:
            hash_val = hashes[s]
        else:
            hash_val = 1

            for c in s:
                hash_val *= prime_map(c)

            hashes[s] = hash_val

        return hash_val

    # Inputs:
    #   hash_val1   - hash of string to compare with 's'
    #           s   - string
    # If hash already exists in 'hash_table', then we've seen an anagram before so it increments the value.
    # Otherwise, it adds a new entry with a value of '1'.
    def save_hash(hash_val1, s):
        hash_val = get_hash(s)
        if hash_val1 == hash_val:
            if hash_val in hash_table:
                hash_table[hash_val] += 1
            else:
                hash_table[hash_val] = 1

    lenS = len(string)
    for length in range(1, lenS):
        for i in range(0, lenS - length):
            substr1 = string[i:i+length]
            hash1 = get_hash(substr1)
            for j in range(i + 1, lenS - length + 1):
                substr2 = string[j:j+length]
                save_hash(hash1, substr2)

    return sum([v for (k, v) in hash_table.items()])


if __name__ == '__main__':
    assert(sherlockAndAnagrams('abba') == 4)
    assert(sherlockAndAnagrams('abcd') == 0)
    assert(sherlockAndAnagrams('ifailuhkqq') == 3)
    assert(sherlockAndAnagrams('kkkk') == 10)
    assert(sherlockAndAnagrams('cdcd') == 5)