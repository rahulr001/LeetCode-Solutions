nums = [3, 2, 3]
target = 6


def twoSum(nums, target):
    for i in range(len(nums)):
        result = target - nums[i]
        if result in nums:
            index = nums.index(result)
            if i != index:
                return([i, index])
    return []


print(twoSum(nums, target))