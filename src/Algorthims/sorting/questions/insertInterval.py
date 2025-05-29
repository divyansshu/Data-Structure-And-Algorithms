def insert(intervals, newInterval):
    result = []
    idx = 0
    n = len(intervals)
    
    # Add all intervals ending before newInterval starts (no overlap)
    while idx < n and intervals[idx][1] < newInterval[0]:
        result.append(intervals[idx])
        idx += 1
    
    # Merge all overlapping intervals with newInterval
    while idx < n and intervals[idx][0] <= newInterval[1]:
        newInterval[0] = min(intervals[idx][0], newInterval[0])
        newInterval[1] = max(intervals[idx][1], newInterval[1])
        idx += 1
    result.append(newInterval)  # Add the merged interval
    
    # Add the remaining intervals (no overlap)
    while idx < n:
        result.append(intervals[idx])   
        idx += 1 

    return result

# Test cases
print(insert([[1,3],[6,9]], [2,5]))  
print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))  
print(insert([[1,3], [4,5], [6,7], [8,10]], [5,6]))  
print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,9]))    