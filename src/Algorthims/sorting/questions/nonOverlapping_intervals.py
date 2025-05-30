def eraseOverlapIntervals(intervals):
    # Sort intervals by their end time to maximize the number of non-overlapping intervals
    intervals.sort(key=lambda x: x[1])
    prevEnd = intervals[0][1]  # End time of the first interval
    count = 1  # At least one interval can be included
    n = len(intervals)
    for i in range(1, n):
        # If the current interval does not overlap with the previous selected interval
        if intervals[i][0] >= prevEnd:
            count += 1  # Include this interval
            prevEnd = intervals[i][1]  # Update the end time to the current interval's end
    # The minimum number of intervals to remove is total intervals minus the count of non-overlapping intervals
    return n - count

# Test cases
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))        
print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))        
print(eraseOverlapIntervals([[1,2],[2,3]]))
print(eraseOverlapIntervals([[1, 2], [5, 10], [18, 35], [40, 45]]))
print(eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))