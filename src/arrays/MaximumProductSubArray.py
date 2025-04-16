'''
# brute force:

   def maxProduct(self,arr):
        
        maxProd = float('-inf')
        for i in range(len(arr)):
            product = 1
            for j in range(i, len(arr)):
                product *= arr[j]  
                maxProd = max(maxProd, product)
                if product == 0:
                    break
        return maxProd 
'''
   
   
# Function to find the maximum product subarray
def maxProduct(arr):
    n = len(arr)
    # If the array has only one element, return that element
    if n == 1:
        return arr[0]
    
    # Initialize variables to track the maximum product so far, 
    # the maximum product ending at the current position, 
    # and the minimum product ending at the current position
    max_so_far = arr[0]
    min_ending_here = arr[0]
    max_ending_here = arr[0]
    
    # Iterate through the array starting from the second element
    for i in range(1, n):
        # Calculate the maximum and minimum products at the current position
        # This considers three cases:
        # 1. The current element itself
        # 2. The product of the current element and the maximum product so far
        # 3. The product of the current element and the minimum product so far
        temp_max = max(arr[i], arr[i] * max_ending_here, arr[i] * min_ending_here)
        temp_min = min(arr[i], arr[i] * max_ending_here, arr[i] * min_ending_here)
        
        # Update the maximum and minimum products ending at the current position
        max_ending_here = temp_max
        min_ending_here = temp_min
        
        # Update the overall maximum product if the current maximum product is greater
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
    
    # Return the maximum product found
    return max_so_far        

# Test cases to verify the function
print(maxProduct([-2, 6, -3, -10, 0, 2]))  # Output: 180
print(maxProduct([-1, -3, -10, 0, 6]))     # Output: 6
print(maxProduct([2, 3, 4]))               # Output: 24