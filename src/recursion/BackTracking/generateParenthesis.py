def generateParenthesis(n):
    res = []  # List to store all valid combinations
    stack = []  # Stack to build the current parenthesis string

    def backtrack(open, close):
        # If the number of open and close parentheses used equals n, we have a valid combination
        if open == close == n:
            res.append(''.join(stack))  # Add the current combination to the result
            return
        # If we can still add an open parenthesis, do so and recurse
        if open < n:
            stack.append('(')
            backtrack(open+1, close)
            stack.pop()  # Backtrack: remove the last added '('
        # If we can add a close parenthesis (i.e., there are unmatched open ones), do so and recurse
        if close < open:
            stack.append(')')
            backtrack(open, close+1)
            stack.pop()  # Backtrack: remove the last added ')'

    backtrack(0, 0)  # Start the recursion with 0 open and 0 close parentheses
    return res

print(generateParenthesis(3))    
print(generateParenthesis(1))    