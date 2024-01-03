nums = [1,12,-5,-6,50,3]
k = 4

def findMaxAverage(nums, k) -> float:
    avg_sum = current_sum = sum(nums[:k])

    for i in range(k, len(nums)):
        current_sum = current_sum - nums[i - k] + nums[i]
        avg_sum = max(avg_sum, current_sum)
    return avg_sum / k


print(findMaxAverage(nums, k))