a = "1010"
b = "1011"


# Output: "10101"

def addBinary(a, b):
    n1 = list(a)
    n2 = list(b)
    carry = 0
    result = ''
    while n1 or n2 or carry == 1:
        if n1:
            carry += int(n1.pop())
        if n2:
            carry += int(n2.pop())
        result += str(carry % 2)
        carry = carry // 2
    return result[::-1]


print(addBinary(a, b))
