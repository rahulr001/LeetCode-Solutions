nums = [0,1,0,3,12]

def moveZeroes(nums: list) -> None:
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            i+=1
    print(nums)

moveZeroes(nums)

