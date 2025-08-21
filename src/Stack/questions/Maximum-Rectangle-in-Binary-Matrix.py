from typing import List

# Find Next Smaller Element to the Right for each element in arr
def find_NSE_Right(arr):
    st = []
    right = []
    # Traverse from right to left
    for i in range(len(arr) - 1, -1, -1):
        # Pop elements from stack while they are greater or equal to current
        while st and arr[st[-1]] >= arr[i]:
            st.pop()
        # If stack is empty, no smaller element to the right
        if not st:
            right.append(len(arr))
        else:
            right.append(st[-1])
        st.append(i)
    # Reverse to match original order
    return list(reversed(right))

# Find Next Smaller Element to the Left for each element in arr
def find_NSE_Left(arr):
    st = []
    left = []
    # Traverse from left to right
    for i in range(len(arr)):
        # Pop elements from stack while they are greater or equal to current
        while st and arr[st[-1]] >= arr[i]:
            st.pop()
        # If stack is empty, no smaller element to the left
        if not st:
            left.append(-1)
        else:
            left.append(st[-1])
        st.append(i)
    return left

# Calculate the maximum area of rectangle in histogram
def getMaxArea(arr):
    right = find_NSE_Right(arr)
    left = find_NSE_Left(arr)
    width = [0] * len(arr)
    max_area = 0
    for i in range(len(arr)):
        # Width is distance between next smaller to right and left minus 1
        width[i] = right[i] - left[i] - 1
        area = arr[i] * width[i]
        max_area = max(area, max_area)
    return max_area

# Main function to find maximum rectangle of 1's in a binary matrix
def maximumRectangle(matrix: List[List[str]])-> int:
    max_area = 0
    # Initialize previous row as zeros
    prev_row = [0] * len(matrix[0])
    for row in matrix:
        # Convert string row to integer row
        row = list(map(int, row))
        # Build up the histogram: add to previous row if current is 1, else 0
        height = [a + b if b != 0 else 0 for a, b in zip(prev_row, row)]
        # Get max area for current histogram
        area = getMaxArea(height)
        max_area = max(area, max_area)
        # Update previous row for next iteration
        prev_row = height 
    return max_area

# Test cases
print(maximumRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(maximumRectangle([["0"]]))
print(maximumRectangle([["1"]]))