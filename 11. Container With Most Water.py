height = [1,8,6,2,5,4,8,3,7]


def maxArea(height) -> int:
    left = 0
    right = len(height) - 1
    max_area = min(height[left], height[right]) * right

    while left < right:
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
        current_area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, current_area)  
    return max_area



print(maxArea(height))