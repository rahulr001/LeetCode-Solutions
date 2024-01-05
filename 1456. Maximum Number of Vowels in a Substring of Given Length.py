s = "weallloveyou"
k = 7

def maxVowels(s: str, k: int) -> int:
    vowels = 'aeiou'
    found = count = j = 0

    for i in range(k):
        if s[i] in vowels:
            count += 1
    found = max(found, count)

    i = k
    while i < len(s):
        if s[i] in vowels:
            count += 1
        if s[j] in vowels:
            count -= 1
        
        found = max(found, count)
        i += 1
        j += 1  
    return found

print(maxVowels(s, k))