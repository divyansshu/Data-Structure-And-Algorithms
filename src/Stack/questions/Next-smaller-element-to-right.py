def leftSmaller(arr):
    res = []   # This will store the result for each element
    st = []    # Stack to keep track of potential next smaller elements

    # Traverse the array from right to left
    for i in range(len(arr) - 1, -1, -1):

        # Pop elements from the stack that are greater than or equal to current element
        while st and st[-1] >= arr[i]:
            st.pop()

        # If stack is empty, there is no smaller element to the right
        if not st:
            res.append(-1)
        else:
            # The top of the stack is the next smaller element to the right
            res.append(st[-1])

        # Push the current element onto the stack
        st.append(arr[i])

    # Reverse the result to match the original array's order
    return list(reversed(res))

print(leftSmaller([1, 6, 2]))
print(leftSmaller([1, 5, 0, 3, 4, 5]))