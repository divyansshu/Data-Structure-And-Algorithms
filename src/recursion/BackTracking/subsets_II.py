def subsetsWithDup(nums):
    # Sort the input to group duplicates together
    nums.sort()
    all_subsets = []

    def uniqueSubsets(current, i):
        # Base case: if we've considered all elements, add the current subset
        if i == len(nums):
            all_subsets.append(current[:])
            return

        # Include nums[i] in the current subset
        current.append(nums[i])
        uniqueSubsets(current, i+1)

        # Backtrack: remove the last element before exploring the next possibility
        current.pop()
            
        # Skip over duplicates to avoid duplicate subsets
        idx = i+1
        while idx < len(nums) and nums[idx] == nums[idx-1]:
            idx += 1

        # Exclude nums[i] and move to the next unique element
        uniqueSubsets(current, idx)    
        
    # Start recursion with an empty subset and index 0
    uniqueSubsets([], 0)        
    return all_subsets

# Example usage
print(subsetsWithDup([1,2,2]))