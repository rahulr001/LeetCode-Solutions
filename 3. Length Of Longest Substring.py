s = "pwwkew"


def lengthOfLongestSubstring(s):
    res = 0
    d = {}
    i = 0
    for a in range(0, len(s)):
        if s[a] in d:
            i = max(i, d[s[a]] + 1)
        res = max(res, (a - i + 1))
        d[s[a]] = a
    return res


print(lengthOfLongestSubstring(s))
