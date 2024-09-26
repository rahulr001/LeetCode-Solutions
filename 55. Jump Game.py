nums = [2,3,1,1,4]


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        start_index = 0
        for i in nums:
            if start_index < 0:
                return False
            elif i > start_index:
                start_index = i
            start_index -= 1
        return True 
        
        
print(Solution().canJump(nums))