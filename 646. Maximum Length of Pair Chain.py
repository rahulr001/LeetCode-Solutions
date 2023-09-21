pairs = [[1,2],[2,3],[3,4]]



def findLongestChain(pairs) -> int:
    res = []
    i = 0
    j = 1
    while i < len(pairs):
        if pairs[i][1] < pairs[j][0]:
            res.append(pairs[i])
            i+=1
        elif pairs[i][1] == pairs[i+1][0]:
            pairs.pop(i+1)
            i=0
        
    return res

print(findLongestChain(pairs))