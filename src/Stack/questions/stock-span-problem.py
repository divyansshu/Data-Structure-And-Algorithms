def calculateSpan(arr):
    # Initialize result list with 1 for the first day (span is always 1)
    res = [1]
    # Stack to store indices of days
    st = [0]
        
    # Iterate over the price array starting from the second element
    for i in range(1, len(arr)):
        # Pop elements from stack while stack is not empty and
        # the price at the top of the stack is less than or equal to current price
        while st and arr[st[-1]] <= arr[i]:
            st.pop()
        # If stack is empty, all previous prices are less than current price
        if not st:
            res.append(i + 1)
        else:
            # Else, span is the difference between current day and last higher price's day
            res.append(i - st[-1])
        # Push current day index onto stack
        st.append(i)
        
    return res

# Example usage
print(calculateSpan([100, 80, 60, 70, 60, 75, 85]))
print(calculateSpan([10, 4, 5, 90, 120, 80]))