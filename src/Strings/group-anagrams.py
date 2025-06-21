from collections import defaultdict

'''
time complexity: O(N x k*logk)
space complexity: O(N x K)
'''
def anagrams(arr):
    # res will store the grouped anagrams
    res = []
    # map will store the mapping from sorted string to index in res
    map = {}
        
    for s in arr:
        # Sort the string to get the key for anagrams
        key = ''.join(sorted(s))
        # If this key is not in map, create a new group
        if key not in map:
            map[key] = len(res)
            res.append([])
        # Append the string to the correct group
        res[map[key]].append(s)
    return res

'''
time complexity: O(N x k)
space complexity: O(N x K)
'''
def anagrams_method2(arr):
    # ans will map character count tuple to list of anagrams
    ans = defaultdict(list)
    for s in arr:
        # Create a count of each character (assuming lowercase a-z)
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        # Use the tuple of counts as the key
        ans[tuple(count)].append(s)
    # Return the grouped anagrams as a list of lists
    return list(ans.values())

# Test cases
print(anagrams( ["act", "god", "cat", "dog", "tac"]))  # [['act', 'cat', 'tac'], ['god', 'dog']]
print(anagrams(["no", "on", "is"]))                    # [['no', 'on'], ['is']]
print(anagrams(["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"])) # [['listen', 'silent', 'enlist'], ['abc', 'cab', 'bac'], ['rat', 'tar', 'art']]

print(anagrams_method2( ["act", "god", "cat", "dog", "tac"]))  # [['act', 'cat', 'tac'], ['god', 'dog']]
print(anagrams_method2(["no", "on", "is"]))                    # [['no', 'on'], ['is']]
print(anagrams_method2(["listen", "silent", "enlist", "abc", "cab", "bac", "rat", "tar", "art"])) # [['listen', 'silent', 'enlist'], ['abc', 'cab', 'bac'], ['rat', 'tar', 'art']]
