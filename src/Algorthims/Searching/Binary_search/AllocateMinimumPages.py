'''
time complexity: O(n*(maxpagelimit-minpagelimit))
space complexity: O(1)
'''

# Function to find the minimum possible maximum number of pages allocated to a student using linear search
def allocate(arr, k):
    # If there are fewer books than students, allocation is not possible
    if len(arr) < k:
        return -1
    
    maxPageLimit = sum(arr)  # The highest possible page limit (all books to one student)
    minPageLimit = max(arr)  # The lowest possible page limit (largest single book)
    
    # Try every possible page limit from minPageLimit to maxPageLimit
    for pageLimit in range(minPageLimit, maxPageLimit + 1):
        count = 1      # Number of students required for current pageLimit
        pageSum = 0    # Current sum of pages allocated to a student
        
        # Allocate books to students without exceeding pageLimit
        for pages in arr:
            if pageSum + pages > pageLimit:
                # Assign books to next student if adding current book exceeds pageLimit
                count += 1
                pageSum = pages
            else:
                # Add book to current student's allocation
                pageSum += pages
        
        # If exactly k students are used, return this pageLimit as answer
        if count == k:
            return pageLimit
    # If allocation is not possible, return -1
    return -1

'''
time complexity: O(n*log(maxpagelimit-minpagelimit))
space complexity: O(1)
'''

# Function to find the minimum possible maximum number of pages allocated to a student using binary search
def allocate_using_BS(arr, k):
    # If there are fewer books than students, allocation is not possible
    if len(arr) < k:
        return -1
    
    maxPageLimit = sum(arr)  # The highest possible page limit (all books to one student)
    minPageLimit = max(arr)  # The lowest possible page limit (largest single book)
    lastPageLimit = -1       # Stores the best (minimum maximum) page limit found
    
    # Binary search between minPageLimit and maxPageLimit
    while minPageLimit <= maxPageLimit:
        pageLimit = (minPageLimit + maxPageLimit) // 2  # Midpoint as current page limit to test

        count = 1      # Number of students required for current pageLimit
        pageSum = 0    # Current sum of pages allocated to a student
        
        # Allocate books to students without exceeding pageLimit
        for pages in arr:
            if pageSum + pages > pageLimit:
                # Assign books to next student if adding current book exceeds pageLimit
                count += 1
                pageSum = pages
            else:
                # Add book to current student's allocation
                pageSum += pages
        
        if count <= k:
            # If allocation is possible with k or fewer students, try for a better (smaller) pageLimit
            lastPageLimit = pageLimit
            maxPageLimit = pageLimit - 1
        else:
            # If more than k students are needed, increase the pageLimit
            minPageLimit = pageLimit + 1
            
    # Return the minimum possible maximum page limit found
    return lastPageLimit        
        
# Example usage and test cases
print(allocate([12,34,67,90], 2))         # Output: 113
print(allocate([15,17,20], 5))            # Output: -1
print(allocate([22, 23, 67], 1))          # Output: 112

print(allocate_using_BS([12,34,67,90], 2))  # Output: 113
print(allocate_using_BS([15,17,20], 5))     # Output: -1
print(allocate_using_BS([22, 23, 67], 1))   # Output: 112