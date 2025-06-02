import math

def minEatingSpeed(piles, h):
    # Initialize the search range for Koko's eating speed
    low = 1
    high = max(piles)
    
    # Binary search to find the minimum eating speed
    while low < high:
        k = (low + high) // 2  # Middle speed to test
        hr = 0  # Total hours needed at speed k
        
        # Calculate total hours needed to eat all piles at speed k
        for pile in piles:
            hr += math.ceil(pile / k)
    
        # If Koko can finish within h hours, try a slower speed
        if hr <= h:
            high = k
        # Otherwise, increase the speed
        else:
            low = k + 1
    # The lowest speed at which Koko can finish in h hours
    return low

# Example test cases
print(minEatingSpeed(piles = [3,6,7,11], h = 8))            
print(minEatingSpeed(piles = [30,11,23,4,20], h = 5))            
print(minEatingSpeed(piles = [30,11,23,4,20], h = 6))            