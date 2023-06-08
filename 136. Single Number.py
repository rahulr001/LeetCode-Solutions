nums = [4, 1, 2, 1, 2, 6, 7, 8, 8, 5, 4, 6, 7, 5, 9]


# def singleNumber(nums):
#     for _ in range(0, len(nums)):
#         for j in range(1, len(nums)):
#             try:
#                 if nums[0] == nums[j]:
#                     m = nums[j]
#                     nums.remove(nums[0])
#                     nums.remove(m)
#                     break
#             except:
#                 ...
#     return nums[0]

def singleNumber(nums):
    temp = set()
    for num in nums:
        if num in temp:
            temp.remove(num)
        else:
            temp.add(num)
    return temp.pop()

print(singleNumber(nums))
