flowerbed = [1, 0, 0, 0, 1]
n = 1


def canPlaceFlowers(flowerbed, n):
    if n == 0:
        return True
    flowerbed.append(0)
    i = j = 0

    while i < len(flowerbed) - 1:
        if flowerbed[i+1] == 0:
            if flowerbed[i] == 0:
                j += 1
                if j == n:
                    return True
            i += 2
        else:
            i += 3
    return False


print(canPlaceFlowers(flowerbed, n))
