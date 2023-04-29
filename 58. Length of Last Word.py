s = "Hello World"


def lengthOfLastWord(s):
    result = 0
    i = len(s) - 1
    while i >= 0 and s[i] == ' ':
        i -= 1

    while i >= 0 and s[i] != ' ':
        result += 1
        i -= 1
    return result


print(lengthOfLastWord(s))
