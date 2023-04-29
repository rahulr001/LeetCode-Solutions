strs = ["cr", "car"]


def longestCommonPrefix(strs):
    result = ''
    for i, a in enumerate(zip(*strs)):

        if len(set(a)) == 1:
            result += a[i]
        elif len(set(a)) > 1:
            break
        else:
            result
    return result


print(longestCommonPrefix(strs))
