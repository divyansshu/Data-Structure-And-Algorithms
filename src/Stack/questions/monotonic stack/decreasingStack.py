from collections import deque

def decreasingStack(nums):
    # Initialize an empty deque to use as a stack
    stack = deque()
    
    # Iterate through each number in the input list
    for num in nums:
        # Initialize a temporary deque to hold elements that are popped from the stack
        temp = deque()
        
        # While the stack is not empty and the top element of the stack is less than the current number
        while stack and stack[-1] < num:
            # Pop the top element from the stack and append it to the temporary deque
            temp.append(stack.pop())
        
        # Append the current number to the stack
        stack.append(num)
        
        # Push all elements from the temporary deque back to the stack
        while temp:
            stack.append(temp.pop())
    
    # Return the modified stack
    return stack        

# Example usage
nums = [7, 5, 9, 4]
print(decreasingStack(nums))