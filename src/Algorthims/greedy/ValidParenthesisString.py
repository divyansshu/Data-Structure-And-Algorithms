from collections import deque

'''
time complexity: O(n)
space complexity: O(n)
'''
def validParenthesis_String(s):
    stack = deque()  # Stack to store indices of '('
    stack2 = deque()  # Stack to store indices of '*'
    
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)  # Push index of '(' onto stack
        elif s[i] == '*':
            stack2.append(i)  # Push index of '*' onto stack2
        else:
            if len(stack) > 0:
                stack.pop()  # Pop from stack if there is a '(' to match ')'
            elif len(stack2) > 0:
                stack2.pop()  # Pop from stack2 if there is a '*' to match ')'
            else:
                return False  # No matching '(' or '*' for ')', return False
    
    while stack and stack2:
        if stack[-1] < stack2[-1]:
            stack.pop()  # Pop from stack if '(' index is less than '*' index
            stack2.pop()  # Pop from stack2
        else:
            return False  # '(' index is greater than '*' index, return False
    
    return len(stack) == 0  # Return True if all '(' are matched

print(validParenthesis_String("(*))"))
