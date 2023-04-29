nums = [1, 3, 5, 6]
target = 5


def searchInsert(nums, target):
    if not nums:
        return 0
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        nums.sort()
        return nums.index(target)


print(searchInsert(nums, target))
