def climbStairs(n):
    if n < 0: return 0
    if n == 0:
        return 1 
    return climbStairs(n-1) + climbStairs(n-2)
    
print(climbStairs(3))
print(climbStairs(4))