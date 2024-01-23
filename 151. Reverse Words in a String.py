s = "  hello world  "


def reverseWords(s):
    return " ".join(s.split()[::-1])
    
    
    
print(reverseWords(s))