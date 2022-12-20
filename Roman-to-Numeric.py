s = 'IV'
nums = {'I': 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
result = 0
prev = None
for char in s:
    result += nums[char]
    if nums.get(prev):
        if nums[prev] < nums[char]:
            result -= 2 * nums[prev]
    prev = char
print(result)
