def wordBreak(s, wordDict):
    memo = {}
    def backtrack(start):
        if start == len(s):
            return True
        
        for end in range(start+1, len(s)+1):
            if s[start: end] in wordDict:
                
                backtrack(end)
                return True
        return False
    return backtrack(0)

print(wordBreak(s = "leetcode", wordDict = ["leet","code"]))
    