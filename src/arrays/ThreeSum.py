def threeSum(nums):
    n = len(nums)  # Get the length of the input list
    triplets = []  # Initialize an empty list to store the triplets

    # Iterate through each element in the list
    for i in range(n):
        # Iterate through each element after the current element
        for j in range(i+1, n):
            # Iterate through each element after the second element
            for k in range(j+1, n):
                # Check if the sum of the three elements is zero
                if nums[i] + nums[j] + nums[k] == 0:
                    # Sort the triplet to avoid duplicates
                    triplet = sorted([nums[i], nums[j], nums[k]])
                    
                    # Add the triplet to the list if it's not already present
                    if triplet not in triplets:
                        triplets.append(triplet)               

    # Print the list of triplets
    print(triplets)             

# Call the function with a sample input
threeSum([-1,0,1,2,-1,-4])    
