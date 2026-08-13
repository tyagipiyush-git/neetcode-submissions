class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        min_price = prices[0]

        for i in range(len(prices)):
            price = prices[i]
            if price < min_price:
                min_price = price

            profit = prices[i] - min_price

            max_profit = max(profit, max_profit)
        return max_profit        