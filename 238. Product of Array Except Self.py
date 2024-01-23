nums = [1, 2, 3, 4]
# nums = [0, 0]
# nums = [-1, 1, 0, -3, 3]


def productExceptSelf(nums):
    res = [1]*len(nums)
    for i in range(1, len(nums)):
        res[i] = res[i-1] * nums[i-1]

    right = nums[-1]
    for i in range(len(nums) - 2, -1, -1):
        res[i] *= right
        right *= nums[i]
    return res


print(productExceptSelf(nums))

