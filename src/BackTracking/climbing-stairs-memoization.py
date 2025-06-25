memo = {}
def climbStairs(n):
    if n in memo:
        return memo[n]
    if n < 0: return 0
    if n == 0:
        return 1
    
    memo[n] =  climbStairs(n-1) + climbStairs(n-2)
    return memo[n]
    
print(climbStairs(3))