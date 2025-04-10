# Mutlitple transaction are allowed

def maximumProfit(prices):
    # Get the number of days (length of the prices list)
    n = len(prices)
    # Initialize profit to 0
    profit = 0
    # Loop through the prices list from the first day to the second-to-last day
    for i in range(0, n-1):
        # If the price on the next day is higher than the current day
        if prices[i+1] > prices[i]:
            # Add the difference to the profit (simulate buying on the current day and selling on the next day)
            profit += prices[i+1] - prices[i]
    # Return the total profit
    return profit

# Test cases
# Example 1: Calculate maximum profit for the given price list
print(maximumProfit([86, 92, 24, 5, 34, 72, 68, 52, 27, 95, 41, 28, 35]))        
# Example 2: Calculate maximum profit for another price list
print(maximumProfit([4, 2, 2, 2, 4]))        