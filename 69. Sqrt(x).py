x = 8


def mySqrt(x):
    if x == 0:
        return 0
    i = 1
    while i < x + 1:
        if i * i == x:
            return i
        elif i * i > x:
            return i - 1
        i += 1


print((mySqrt(x)))
