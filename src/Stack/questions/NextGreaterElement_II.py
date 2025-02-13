
'''
Time Complexity: O(n^2)
# The outer loop runs n times, and for each element, the inner loop can run up to n times in the worst case.
# Therefore, the overall time complexity is O(n^2).

# Space Complexity: O(n)
# The space complexity is O(n) due to the result array which stores the next greater element for each input element.
''' 
def nextGreaterElements_bruteForce(nums):
    # Initialize the result array with -1, indicating no greater element found yet
    result = [-1] * len(nums)
    n = len(nums)
    
    # Iterate through each element in the array
    for i in range(n):
        # Start checking from the next element in a circular manner
        j = (i + 1) % n
        while i != j:
            # If a greater element is found, update the result and break the loop
            if nums[j] > nums[i]:
                result[i] = nums[j]
                break
            else:
                # Move to the next element in a circular manner
                j = (j + 1) % n
    
    return result

'''
Time Complexity: O(n)
# The outer loop runs 2n times, but each element is pushed and popped from the stack at most once.
# Therefore, the overall time complexity is O(n).

# Space Complexity: O(n)
# The space complexity is O(n) due to the result array and the stack which can store up to n elements.
'''

def nextGreaterElements_optimized(nums):
    n = len(nums)
    # Initialize the result array with -1, indicating no greater element found yet
    result = [-1] * n
    # Stack to keep track of indices whose next greater element is not found yet
    stack = []
    
    # Iterate through the array twice to simulate the circular nature
    for i in range(2 * n):
        curr_index = i % n
        
        # Check if the current element is greater than the element at the index stored in the stack
        while stack and nums[stack[-1]] < nums[curr_index]:
            prev_index = stack.pop()
            result[prev_index] = nums[curr_index]
        
        # Only append the index of the first pass through the array
        if i < n:
            stack.append(i)  
    
    return result           

# Example usage
nums = [1, 2, 3, 4, 3]
print(nextGreaterElements_bruteForce(nums))
print(nextGreaterElements_optimized(nums))


