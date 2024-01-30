n = 10


class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0
        r = n
        while l < r:
            m = (l + r) >> 1
            if guess(m) == 1:
                return m
            elif guess(m) == -1:
                l = m - 1
            else:
                r = m + 1


print(Solution().guessNumber(n))