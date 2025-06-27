def sumClosest(arr, target):
    n = len(arr)
    arr.sort()  # Sort the array to use two-pointer technique
    minDiff = float('inf')  # Initialize minimum difference as infinity
    l = 0  # Left pointer
    r = n - 1  # Right pointer
    res = []  # To store the result pair

    while l < r:
        currSum = arr[l] + arr[r]  # Sum of elements at left and right pointers
        closeness = abs(target - currSum)  # How close the sum is to the target

        if closeness < minDiff:
            minDiff = closeness  # Update minimum difference
            res = [arr[l], arr[r]]  # Update result with current pair

        if currSum > target:
            r -= 1  # Move right pointer left to decrease sum
        elif currSum < target:
            l += 1  # Move left pointer right to increase sum
        else:
            return res  # Exact match found, return immediately

    return res  # Return the closest pair found

# Example usage
print(sumClosest([10, 30, 20, 5], target=25))
print(sumClosest([5, 2, 7, 1, 4], target=10))
print(sumClosest([10], target=10))