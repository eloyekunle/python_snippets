def longestPrefixSuffix(S) :
    n = len(S)
    lps = [0] * n
    l = 0
    i = 1
    
    while i < n:
        print(i, l, lps)
        if S[i] == S[l]:
            l = l + 1
            lps[i] = l
            i = i + 1
        else :
            if l != 0:
                l = lps[l-1]
            else :
                lps[i] = 0
                i = i + 1

    return l


s = "abbabba"
print(longestPrefixSuffix(s)) 