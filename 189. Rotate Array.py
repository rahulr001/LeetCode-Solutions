nums = [1,2,3,4,5,6,7]
k = 3


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        for i in range(k):
            nums.insert(0, nums.pop())


print(Solution().rotate(nums, k))
        