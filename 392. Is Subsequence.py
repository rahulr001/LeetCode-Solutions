s = "twn"
t = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxtxxxxxxxxxxxxxxxxxxxxwxxxxxxxxxxxxxxxxxxxxxxxxxn"


def isSubsequence(s: str, t: str) -> bool:
    b = 0
    j = 0
    for i, _ in enumerate(s):
        while j in range(0, len(t)):
            if s[i] == t[j]:
                b += 1
                t = t[j+1:]
                j = 0
                break
            j+=1
    return b == len(s)

print(isSubsequence(s,t))