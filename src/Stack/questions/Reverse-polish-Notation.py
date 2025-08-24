from typing import List

def evalRPN(tokens: List[str]) -> int:
    s = []  # Stack to store operands
    for token in tokens:
        # If the token is a number (including negative numbers)
        if token.lstrip('-').isdigit():
            s.append(int(token))  # Push number onto stack
        else:
            # Pop the top two numbers for the operation
            num2 = s.pop()
            num1 = s.pop()
            # Perform the operation based on the token
            if token == '+':
                s.append(num1 + num2)
            elif token == '-':
                s.append(num1 - num2)
            elif token == '*':
                s.append(num1 * num2)
            else:
                # For division, convert result to int (truncate towards zero)
                s.append(int(num1 / num2))
    # The final result is the only item left on the stack
    return s.pop()

# Example usages
print(evalRPN(["2","1","+","3","*"]))           # Output: 9
print(evalRPN(["4","13","5","/","+"]))          # Output: 6
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))  # Output: 22