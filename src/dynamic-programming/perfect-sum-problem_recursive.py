'''
problem link: https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/0
'''

def perfectSum(arr, target):
    n = len(arr)
    def backtrack(i, total):
        if i == n:
            return 1 if total == target else 0
        
        if total > target:
            return 0
        
        cnt1 = backtrack(i+1, total+arr[i])
        cnt2 = backtrack(i+1, total)
        return cnt1 + cnt2	   
	
    return backtrack(0,0)

print(perfectSum([5, 2, 3, 10, 6, 8], target = 10))
print(perfectSum( [2, 5, 1, 4, 3], target = 10))
print(perfectSum([5, 7, 8], target = 3))
print(perfectSum([35, 2, 8, 22], target = 0))