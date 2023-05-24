nums1 = [1,2]
nums2 = [3,4]


def findMedianSortedArrays(nums1, nums2):
    nums = nums1+nums2
    nums.sort()
    n = len(nums)
    if n % 2 != 0:
        return nums[n // 2]
    else:
        return (nums[n//2-1]+nums[n//2])/2


print(findMedianSortedArrays(nums1, nums2))
