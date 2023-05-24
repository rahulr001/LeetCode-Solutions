list = [1, 3, 2, 5, 4, 6, 7]
key = 6


def BinarySearch(list, key):
    list.sort()
    start = 0
    end = len(list)-1
    fount = False
    while not fount and start <= end:
        mid = (start+end) // 2
        if list[mid] == key:
            fount = True
            return list.index(list[mid])
        elif list[mid] > key:
            end = mid - 1
        elif list[mid] < key:
            start = mid + 1


print(BinarySearch(list, key))
