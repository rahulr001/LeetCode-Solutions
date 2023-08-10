list = [1, 3, 2, 5, 4, 6, 7]


def BubbleSort(list):
    for i in range(len(list)):
        swapped = False
        for j in range(0, len(list) - i - 1):
            if list[j] > list[j + 1]:
                swapped = True
                list[j], list[j+1] = list[j+1], list[j]
        if not swapped:
            break
    return list


print(BubbleSort(list))
