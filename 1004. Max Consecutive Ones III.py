nums = [1,1,1,0,0,0,1,1,1,1,0]
# nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 2


def longestOnes(nums, k) -> int:
    i = j = 0

    while j < len(nums):
        if nums[j] == 0:
            k -= 1
        if k < 0:
            if nums[i] == 0:
                k += 1
            i += 1
        j += 1

    return j - i







print(longestOnes(nums, k))