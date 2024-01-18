s = "leet**cod*e"



def removeStars(s: str) -> str:
    res = []
    for i in s:
        if i != "*":
            res.append(i)
        else:
            res.pop()
    return ''.join(res)




print(removeStars(s))