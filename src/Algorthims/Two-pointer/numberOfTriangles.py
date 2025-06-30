def triangleNumber(arr):
    n = len(arr)
    arr.sort()  # Sort the array to make it easier to apply the two-pointer technique
    res = 0
    # Fix the third side (the largest side of the triangle)
    for i in range(2, n):
        l, r = 0, i-1  # Initialize two pointers
        while l < r:
            # If the sum of the two smaller sides is greater than the largest side,
            # then all elements between l and r can form a triangle with arr[i]
            if arr[l] + arr[r] > arr[i]:
                res += r - l  # Count all valid pairs
                r -= 1  # Move the right pointer to check for other possibilities
            else:
                l += 1  # Move the left pointer to increase the sum
    return res

print(triangleNumber([4,6,3,7]))