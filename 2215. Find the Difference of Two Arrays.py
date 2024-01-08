nums1 = [1,2,3]
nums2 = [2,4,6]

def findDifference(nums1, nums2):
    return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]


print(findDifference(nums1, nums2))