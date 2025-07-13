def subarraysWithKDistinct(nums, k):
    n = len(nums)
    # Helper function to count subarrays with at most k distinct integers
    def atMost(k):
        i = j = 0
        mp = {}  # Dictionary to store the count of each integer in the current window
        cnt = 0
        while j < n:
            # Add nums[j] to the window
            mp[nums[j]] = mp.get(nums[j], 0) + 1

            # If there are more than k distinct integers, shrink the window from the left
            while len(mp) > k:
                mp[nums[i]] -= 1
                if mp[nums[i]] == 0:
                    del mp[nums[i]]
                i += 1
            
            # Count the number of subarrays ending at j with at most k distinct integers
            cnt += (j - i + 1)
            j += 1
        return cnt
        
    # The number of subarrays with exactly k distinct integers is the difference
    # between the number with at most k and at most (k-1) distinct integers
    return atMost(k) - atMost(k-1)

print(subarraysWithKDistinct([1,2,1,2,3], k = 2))  # Output: 7
print(subarraysWithKDistinct([1,2,1,3,4], k = 3))  # Output: 3