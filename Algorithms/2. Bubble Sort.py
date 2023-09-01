list = [1, 3, 2, 5, 4, 6, 7]

def BubbleSort(list):
    for i in len(list):
        swapped = False
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j],list[j+1] = list[j+1],list[j]
                swapped = True
        if not swapped:
            return "Array is already in sorted order"
    return list

print(BubbleSort(list))