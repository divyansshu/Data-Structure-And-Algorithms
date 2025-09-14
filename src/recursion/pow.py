def power(b, e):
    # Handle the case where both base and exponent are zero
    if e == 0 and b == 0:
        return 0
    # Any number to the power of 0 is 1
    if e == 0:
        return 1
    # Work with the absolute value of exponent for calculation
    p = abs(e)
    # Helper function to compute power using recursion and exponentiation by squaring
    def mypow(result, b, p):
        # Base case: exponent is zero
        if p == 0:
            return result
        # If exponent is odd, multiply result by base
        if p % 2 == 1:
            result = result * b
        # Square the base and halve the exponent
        b *= b
        return mypow(result, b, p // 2)
    # Start recursion with result=1
    result = mypow(1, b, p)
    # If exponent was negative, take reciprocal
    if e < 0:
        return (1 / result)
    # Round result to 2 decimal places
    return round(result, 2)

# Test cases
print(power(2.00000, 10))    # 1024.0
print(power(2.10000, 3))     # 9.26
print(power(2.00000, -2))    # 0.25