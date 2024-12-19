from typing import List

def maxProfit(prices: List[int]) -> int:
    max_profit = 0
    left = 0

    for right in range(1, len(prices)):
        if prices[right] > prices[left]:
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
        else:
            left = right

    return max_profit

print(maxProfit(prices=[7, 1, 5, 3, 6, 4]))