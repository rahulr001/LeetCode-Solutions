word1 = "abc"
word2 = "pqr"


def mergeAlternately(word1: str, word2: str) -> str:
    res = ''
    n1 = 0
    n2 = 0
    for w1, w2 in  word1, word2:
        res+= w1+w2

    




print(mergeAlternately(word1, word2))