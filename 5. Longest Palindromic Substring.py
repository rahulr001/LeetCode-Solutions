s = "babad"


def longestPalindrome(s):
    if len(s) <= 1:
        return s

    res = s[0]
    max_len = 1

    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if j-i+1 > max_len and s[i:j+1] == s[i:j+1][::-1]:
                max_len = j-i+1
                res = s[i:j+1]

    return res


print(longestPalindrome(s))

