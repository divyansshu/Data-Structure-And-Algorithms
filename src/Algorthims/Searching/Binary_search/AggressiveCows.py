'''
time complexity: O(n*(max-min)):
where n is the size of the array, MAX is the maximum element in the array and MIN is minimum
element in the array.

space complexity: O(1)
'''
def aggressiveCows(stalls, k):
    # Number of stalls
    n = len(stalls)
    # Sort the stall positions
    stalls.sort()
    # Maximum possible distance between cows
    max_dis = stalls[-1] - stalls[0]
    # Start with minimum possible distance
    dis = 1
    # Store the last valid distance
    last_dis = 0

    # Try all possible distances from 1 to max_dis
    while dis <= max_dis:
        cows_placed = 1  # Place the first cow in the first stall
        last_pos = stalls[0]  # Position of last placed cow
        
        # Try to place the rest of the cows
        for i in range(1, n):
            # If the current stall is at least 'dis' away from last cow
            if stalls[i] - last_pos >= dis:
                cows_placed += 1
                last_pos = stalls[i]
                # If all cows are placed, break
                if cows_placed == k:
                    break
            
        # If we could place all cows, try for a bigger distance
        if cows_placed >= k:
            last_dis = dis
            dis += 1
        else:
            # If not possible, stop searching
            break    
    return last_dis 

'''
time complexity: O(n*log(max-min)):
where n is the size of the array, MAX is the maximum element in the array and MIN is minimum
element in the array.

space complexity: O(1)
'''

def aggressiveCows_binarySearch(stalls, k):
    # Number of stalls
    n = len(stalls)
    # Sort the stall positions
    stalls.sort()
    last_dis = 0  # Store the last valid distance
    # Binary search range for the answer
    low, high = 0, (stalls[-1] - stalls[0])
    
    # Binary search for the largest minimum distance
    while low <= high:
        mid = (low+high) // 2  # Try middle distance
        cows_placed = 1  # Place the first cow
        last_pos = stalls[0]  # Position of last placed cow
        
        # Try to place the rest of the cows
        for i in range(1, n):
            # If the current stall is at least 'mid' away from last cow
            if stalls[i] - last_pos >= mid:
                cows_placed += 1
                last_pos = stalls[i]
            
        # If we could place all cows, try for a bigger distance
        if cows_placed >= k:
            last_dis = mid
            low = mid + 1
        else:
            # Otherwise, try for a smaller distance
            high = mid - 1
    return last_dis        
           

# Test cases
print(aggressiveCows(stalls = [1, 2, 4, 8, 9], k = 3))            
print(aggressiveCows(stalls = [10, 1, 2, 7, 5], k = 3))            
print(aggressiveCows(stalls = [2, 12, 11, 3, 26, 7], k = 5)) 

print(aggressiveCows_binarySearch(stalls = [1, 2, 4, 8, 9], k = 3))  
print(aggressiveCows_binarySearch(stalls = [10, 1, 2, 7, 5], k = 3))            
print(aggressiveCows_binarySearch(stalls = [2, 12, 11, 3, 26, 7], k = 5))          