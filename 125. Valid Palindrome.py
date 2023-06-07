s = "A man, a plan, a canal: Panama"


def isPalindrome(s):
    temp = ''
    symbol = [' ',',',':',"'",'"','!','@','#','$','%','^','&','*','(',')','_','+','=','-',']','[','}','{','|',';','/','?','<','>','.',',','`']
    for str in s:
        if str not in symbol:
            temp += str

    temp = temp.lower()
    reversed = temp[::-1]

    if reversed == temp:
        return True
    else:
        return False


print(isPalindrome(s))
