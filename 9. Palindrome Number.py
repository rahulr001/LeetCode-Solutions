x = 121


def isPalindrome(x):
    list_x = str(x)
    reverse_x = list_x[::-1]
    if list_x == reverse_x:
        return True
    else:
        return False


print(isPalindrome(x))
