s = "aA"


def reverseVowels(s):
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    r = []
    for i in range(len(s)):
        if s[i] in vowels:
            r.append(s[i])
            s = s.replace(s[i], "*", 1)
    for i in range(len(s)):
        if s[i] == "*" and r:
            s = s.replace(s[i], r.pop(), 1)  
    return s
    
    
print(reverseVowels(s))