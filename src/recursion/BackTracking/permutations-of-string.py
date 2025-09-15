def findPermutation(s):
    # Result list to store all unique permutations
    res = []
    n = len(s)
    # Visited array to keep track of used characters
    visited = [False] * n
    # Sort characters to handle duplicates
    char = sorted(s)
        
    def backtrack(path):
        # If path length equals string length, add to result
        if len(path) == n:
            res.append("".join(path))
            return
            
        for i in range(n):
            # Skip already used characters
            if visited[i]:
                continue
                
            # Skip duplicate characters to avoid duplicate permutations
            if i > 0 and char[i] == char[i-1] and not visited[i-1]:
                continue
                
            # Mark character as used
            visited[i] = True
            # Recurse with current character added to path
            backtrack(path + [char[i]])
            # Backtrack: unmark character
            visited[i] = False

    # Start backtracking with empty path
    backtrack([])
    return res

# Test cases
print(findPermutation("ABC"))
print(findPermutation("ABSG"))
print(findPermutation("AAA"))