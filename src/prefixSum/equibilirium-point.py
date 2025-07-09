'''
time complexity: O(n)
space complexity: O(n)
'''
def find_equilibrium(arr):
    n = len(arr)
    # Create prefix sum array
    prefSum = [0] * n
    prefSum[0] = arr[0]
    for i in range(1, n):
        prefSum[i] = prefSum[i-1] + arr[i]
    
    # Create suffix sum array
    suffSum = [0] * n
    suffSum[n-1] = arr[n-1]
    for j in range(n-2, -1, -1):
        suffSum[j] = suffSum[j+1] + arr[j]
    
    # Find the index where prefix sum equals suffix sum
    for i in range(n):
        if prefSum[i] == suffSum[i]:
            return i
    return -1

'''
time complexity: O(n)
space complexity: O(1)
'''
def findEquilibrium(arr):
    n = len(arr)
    prefSum = 0  # Sum of elements to the left of current index
    total = sum(arr)  # Total sum of array
    for pivot in range(n):
        # suffSum is total sum minus prefix sum and current element
        suffSum = total - prefSum - arr[pivot]
        if suffSum == prefSum:
            return pivot
        prefSum += arr[pivot]  # Update prefix sum for next iteration
    return -1

# Test cases
print(find_equilibrium([1, 2, 0, 3]))
print(find_equilibrium([1, 1, 1, 1]))
print(find_equilibrium([-7, 1, 5, 2, -4, 3, 0]))

print(findEquilibrium([1, 2, 0, 3]))
print(findEquilibrium([1, 1, 1, 1]))
print(findEquilibrium([-7, 1, 5, 2, -4, 3, 0]))