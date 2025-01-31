def findSatisfied_children(greed, cookies):
    # Sort the greed and cookies arrays
    greed.sort()
    cookies.sort()
    
    # Initialize pointers for children and cookies
    child = cookie = 0
    # Initialize the count of satisfied children
    satisfied_child_count = 0
    
    # Iterate through both arrays until we reach the end of one of them
    while child < len(greed) and cookie < len(cookies):
        # If the current cookie can satisfy the current child's greed
        if cookies[cookie] >= greed[child]:
            # Increment the count of satisfied children
            satisfied_child_count += 1
            # Move to the next child
            child += 1
        # Move to the next cookie
        cookie += 1
    
    # Return the total number of satisfied children
    return satisfied_child_count


# Example usage
greed = [1, 2, 3]
cookies = [1, 1]
print(findSatisfied_children(greed, cookies))  # Output: 1      