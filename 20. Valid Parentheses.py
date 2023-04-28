s = "()[]{}"


def isValid(s):
    result = []
    for i in s:
        if i in ['(', '[', '{']:
            result.append(i)
        else:
            if not result:
                return False
            last = result.pop()
            if i == ')' and last != '(':
                return False
            elif i == ']' and last != '[':
                return False
            elif i == '}' and last != '{':
                return False
    return not result


print(isValid(s))
