nums = [3,3,4]


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counts = {}
        num_set = set(nums)

        for n in num_set:
            counts[nums.count(n)] = n
        return counts[list({key: counts[key] for key in sorted(counts, reverse=True)}.keys())[0]]


print(Solution().majorityElement(nums))