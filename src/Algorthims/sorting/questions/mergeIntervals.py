def merge(intervals):
    # Sort the intervals based on the starting value of each interval
    intervals.sort(key=lambda x: x[0])
    
    # Initialize the merged list with the first interval
    merged = [intervals[0]]
    
    # Iterate through the remaining intervals
    for current in intervals[1:]:
        # Get the last interval in the merged list
        last = merged[-1]
        
        # Check if the current interval overlaps with the last merged interval
        if current[0] <= last[1]:
            # If they overlap, merge them by updating the end of the last interval
            last[1] = max(last[1], current[1])
        else:
            # If they don't overlap, add the current interval to the merged list
            merged.append(current)
    
    # Return the merged list of intervals
    return merged            

# Test cases to verify the functionality of the merge function
print(merge([[1,3],[2,6],[8,10],[15,18]]))  # Expected output: [[1, 6], [8, 10], [15, 18]]
print(merge([[5, 6], [1, 4], [3, 5]]))      # Expected output: [[1, 6]]