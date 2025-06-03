def countGoodNumbers(n):
    mod = 10**9 + 7  # Large prime for modulo operations to prevent overflow
    even = (n + 1) // 2  # Number of even-indexed positions (0-based indexing)
    odd = n // 2         # Number of odd-indexed positions
    # For even positions, 5 choices (0,2,4,6,8); for odd positions, 4 choices (prime digits: 2,3,5,7)
    # Total ways = 5^even * 4^odd (modulo mod)
    return (pow(5, even, mod) * pow(4, odd, mod)) % mod

print(countGoodNumbers(4))  # Example usage
print(countGoodNumbers(5))
print(countGoodNumbers(1))