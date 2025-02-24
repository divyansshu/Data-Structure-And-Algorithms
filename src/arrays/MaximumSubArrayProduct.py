def maxProduct(nums):
    n = len(nums)
    if n == 0:
        return nums[0]  # Return the first element if the list is empty
    
    # Initialize maxProd, minProd, and result with the first element of the array
    maxProd = minProd = result = nums[0]
    
    # Iterate through the array starting from the second element
    for i in range(1, n):
        if nums[i] < 0:
            # Swap maxProd and minProd if the current element is negative
            maxProd, minProd = minProd, maxProd
        
        # Update maxProd to be the maximum of the current element or the product of the current element and maxProd
        maxProd = max(nums[i], nums[i] * maxProd)
        
        # Update minProd to be the minimum of the current element or the product of the current element and minProd
        minProd = min(nums[i], nums[i] * minProd)
        
        # Update result to be the maximum of result or maxProd
        result = max(result, maxProd)
    
    return result  # Return the maximum product found

# Test cases
nums = [2,3,0,-1,6]
print(maxProduct(nums))  # Output the maximum product of the subarray
print(maxProduct([2, 3, 0, -2, 4]))  # Output the maximum product of the subarray
print(maxProduct([3, -1, 4]))  # Output the maximum product of the subarray
print(maxProduct([-1, -2, 3, 4]))  # Output the maximum product of the subarray