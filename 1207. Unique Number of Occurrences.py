arr = [1,2,2,1,1,3]


def uniqueOccurrences(arr):
    count = []

    for i in set(arr):
        count.append(arr.count(i))

    return len(count) == len(set(count))



print(uniqueOccurrences(arr))