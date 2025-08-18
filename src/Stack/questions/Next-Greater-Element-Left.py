def nextGreaterElement(arr):
    st = []      # Stack to keep track of elements for comparison
    res = []     # Result list to store next greater elements to the left

    for num in arr:
        # Pop elements from stack while stack is not empty and
        # top of stack is less than or equal to current number
        while st and st[-1] <= num:
            st.pop()
        
        # If stack is empty, no greater element to the left
        if not st:
            res.append(-1)
        else:
            # Top of stack is the next greater element to the left
            res.append(st[-1])
        
        # Push current number onto stack for next iterations
        st.append(num)
    return res

# Example usages
print(nextGreaterElement([1, 3, 2, 4]))         # Output: [-1, -1, 3, -1]
print(nextGreaterElement([6, 8, 0, 1, 3]))      # Output: [-1, -1, 8, 8, 8]
print(nextGreaterElement([10, 20, 30, 50]))     # Output: [-1, -1, -1, -1]
print(nextGreaterElement([50, 40, 30, 10]))     # Output: [-1, 50, 40, 30]