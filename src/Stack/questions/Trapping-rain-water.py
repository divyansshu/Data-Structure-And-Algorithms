'''
Time: O(n)
space: O(n)
'''
def maxWater(arr):
    n = len(arr)
    # maxL[i] stores the maximum height to the left of i (including i)
    maxL = [0] * n
    maxL[0] = arr[0]
    for i in range(1, n):
        maxL[i] = max(arr[i], maxL[i-1])
        
    # maxR[i] stores the maximum height to the right of i (including i)
    maxR = [0] * n
    maxR[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        maxR[i] = max(arr[i], maxR[i+1])
        
    total = 0
    # Water trapped at each index is min(maxL[i], maxR[i]) - arr[i]
    for i in range(n):
        total += min(maxR[i], maxL[i]) - arr[i]
    return total

'''
time: O(n)
space: O(1)
'''
def maxWater_two_pointer(arr):
    n = len(arr)
    left, right = 0, n - 1
    left_max, right_max = 0, 0
    total = 0
    
    # Use two pointers to traverse from both ends
    while left <= right:
        # If left bar is smaller, process left side
        if arr[left] <= arr[right]:
            if arr[left] > left_max:
                # Update left_max if current bar is higher
                left_max = arr[left]
            else:
                # Water trapped is left_max - current bar
                total += left_max - arr[left]
            left += 1
        else:
            # Process right side
            if arr[right] > right_max:
                # Update right_max if current bar is higher
                right_max = arr[right]
            else:
                # Water trapped is right_max - current bar
                total += right_max - arr[right]
            right -= 1
    return total

# Test cases
print(maxWater([3, 0, 2, 0, 4]))
print(maxWater([1, 2, 3, 4]))
print(maxWater([2, 1, 5, 3, 1, 0, 4]))

print(maxWater_two_pointer([3, 0, 2, 0, 4]))
print(maxWater_two_pointer([1, 2, 3, 4]))
print(maxWater_two_pointer([2, 1, 5, 3, 1, 0, 4]))