candies = [2,3,5,1,3]
extraCandies = 3

def kidsWithCandies(candies, extraCandies):
    new_candies = [i + extraCandies for i in candies]
    result = []
    for cand in new_candies:
        if cand >= max(candies):
            result.append(True)
        else:
            result.append(False)
    return result


print(kidsWithCandies(candies, extraCandies))