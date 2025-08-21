def find_NSE_Right(arr):
    # Find index of Next Smaller Element to the right for each element
    st = []  # Stack to keep indices
    right = []  # Result list
    for i in range(len(arr) - 1, -1, -1):  # Traverse from right to left
        # Pop elements from stack while they are greater or equal to current
        while st and arr[st[-1]] >= arr[i]:
            st.pop()
        # If stack is empty, no smaller element to the right
        if not st:
            right.append(len(arr))
        else:
            right.append(st[-1])  # Index of next smaller element
        st.append(i)  # Push current index to stack
    return list(reversed(right))  # Reverse to match original order
            

def find_NSE_Left(arr):
    # Find index of Next Smaller Element to the left for each element
    st = []  # Stack to keep indices
    left = []  # Result list
    for i in range(len(arr)):  # Traverse from left to right
        # Pop elements from stack while they are greater or equal to current
        while st and arr[st[-1]] >= arr[i]:
            st.pop()
        # If stack is empty, no smaller element to the left
        if not st:
            left.append(-1)
        else:
            left.append(st[-1])  # Index of next smaller element
        st.append(i)  # Push current index to stack
    return left
        

def getMaxArea(arr):
    # Main function to calculate maximum area in histogram
    right = find_NSE_Right(arr)  # Indices of next smaller to right
    left = find_NSE_Left(arr)    # Indices of next smaller to left
    width = [0] * len(arr)       # Width for each bar
    max_area = float('-inf')     # Initialize max area
    for i in range(len(arr)):
        # Width is distance between next smaller to right and left minus 1
        width[i] = right[i] - left[i] - 1
        area = arr[i] * width[i]  # Area with current bar as smallest
        max_area = max(area, max_area)  # Update max area
    return max_area

# Example usage
print(getMaxArea([60, 20, 50, 40, 10, 50, 60]))
print(getMaxArea([3, 5, 1, 7, 5, 9]))
print(getMaxArea([3]))