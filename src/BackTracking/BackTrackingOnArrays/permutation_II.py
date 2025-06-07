def permuteUnique(nums):
    res = []  # This will store the final list of unique permutations
    perms = []  # This will store the current permutation being built
    count = {i:0 for i in nums}  # Dictionary to count occurrences of each number in nums
    for i in nums:
        count[i] += 1  # Count each number's frequency
    
    def permutations():
        # If the current permutation is the same length as nums, it's complete
        if len(perms) == len(nums):
            res.append(perms[:])  # Add a copy of the current permutation to results
            return
        
        # Try to use each unique number that still has remaining count
        for i in count:
            if count[i] > 0:
                perms.append(i)  # Add number to current permutation
                count[i] -= 1  # Decrease its count
                permutations()  # Recurse to build the next position
                count[i] += 1  # Backtrack: restore count
                perms.pop()  # Backtrack: remove last number from current permutation

    permutations()  # Start the recursive process
    return res  # Return all unique permutations

print(permuteUnique([1,1,2]))