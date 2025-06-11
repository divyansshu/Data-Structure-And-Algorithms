def letterCombination(digits):
    # Mapping of digits to corresponding letters on a phone keypad
    mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    res = []  # List to store all possible combinations

    def backtrack(i, curStr):
        # If the current combination is the same length as digits, add to result
        if len(curStr) == len(digits):
            res.append(curStr)
            return
        
        # Iterate over all possible letters for the current digit
        for c in mapping[digits[i]]:
            # Recurse to the next digit with the current letter added
            backtrack(i+1, curStr+c)

    # Start backtracking only if digits is not empty
    if digits:
        backtrack(0, "")
    return res        

# Example usages
print(letterCombination('23'))  # Output: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
print(letterCombination(''))    # Output: []
print(letterCombination('2'))   # Output: ['a', 'b', 'c']