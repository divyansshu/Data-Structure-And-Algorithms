def sort012(arr):
    # Initialize pointers for red (0s), white (1s), and blue (2s)
    red = 0
    blue = len(arr) - 1
    white = 0
    
    # Traverse the array until the white pointer crosses the blue pointer
    while white <= blue:
        if arr[white] == 1:
            # If the current element is 1, just move the white pointer forward
            white += 1
        elif arr[white] == 0:
            # If the current element is 0, swap it with the element at the red pointer
            # Move both the white and red pointers forward
            arr[white], arr[red] = arr[red], arr[white]
            white += 1
            red += 1
        else:
            # If the current element is 2, swap it with the element at the blue pointer
            # Move the blue pointer backward
            arr[white], arr[blue] = arr[blue], arr[white]
            blue -= 1
    return arr
            
# Test cases to verify the function
print(sort012([0, 1, 2, 0, 1, 2]))            
print(sort012([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]))            