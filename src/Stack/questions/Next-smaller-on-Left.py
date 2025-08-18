def leftSmaller(arr):
    res = []  # Result list to store answers
    st = []   # Stack to keep track of potential "smaller on left" elements
    for num in arr:
        # Pop elements from stack that are greater than or equal to current number
        while st and st[-1] >= num:
            st.pop()
        
        # If stack is empty, no smaller element on left
        if not st:
            res.append(-1)
        else:
            # Top of stack is the next smaller on left
            res.append(st[-1])
        # Push current number onto stack
        st.append(num)
    return res

# Example usage
print(leftSmaller([1, 6, 2]))
print(leftSmaller([1, 5, 0, 3, 4, 5]))
