nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]


def removeDuplicates(num):
    if len(num) == 0:
        return 0
    i = 0
    j = 1
    while j < len(num):
        if num[i] == num[j]:
            j += 1
        else:
            i += 1
            num[i] = num[j]
            j += 1
    return i+1


print(removeDuplicates(nums))
