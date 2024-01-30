from collections import Counter

word1 = "abc"
word2 = "bca"


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return ((cnt1 := Counter(word1)).keys() == (cnt2 := Counter(word2)).keys()
                 and sorted(cnt1.values()) == sorted(cnt2.values()))


print(Solution().closeStrings(word1, word2))
