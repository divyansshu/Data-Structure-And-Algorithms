def permute(nums):
    res = []  # List to store all permutations
    n = len(nums)
    idx = 0

    def get_permutations(nums, idx):
        # Base case: if the current index is at the end, add a copy of nums to result
        if idx == n:
            res.append(nums[:])
            return

        # Iterate through the array and swap each element with the current index
        for i in range(idx, n):
            nums[i], nums[idx] = nums[idx], nums[i]  # Swap to fix one element at idx
            get_permutations(nums, idx+1)            # Recurse for the next index
            nums[i], nums[idx] = nums[idx], nums[i]  # Backtrack to restore original order

    get_permutations(nums, idx)
    return res        

print(permute([1,2,3]))