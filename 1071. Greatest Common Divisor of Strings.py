str1 = "ABCABC"
str2 = "ABC"

def gcdOfStrings(str1: str, str2: str) -> str:
    len1, len2  = len(str1), len(str2)

    for i in range(min(len1, len2), 0, -1):
        if len1 % i or len2 % i:
            continue
        n1, n2 = len1 // i, len2 // i
        base = str1[:i]
        if str1 == n1 * base and str2 == n2 * base:
            return base
    else:
        return ''

print(gcdOfStrings(str1, str2))