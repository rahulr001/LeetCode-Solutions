digits = [1, 2, 9]


def plusOne(digits):
    n = ''
    for i in digits:
        n += str(i)
    n = int(n) + 1
    n = [int(i) for i in str(n)]
    return n


print((plusOne(digits)))
