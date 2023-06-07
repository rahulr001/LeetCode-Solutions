n = 2

def climbStairs(n):
    prev = 1
    prev1 = 0
    for i in range(1, n+1):
        steps = prev1 + prev
        prev1 = prev
        prev = steps
    return prev


print((climbStairs(n)))