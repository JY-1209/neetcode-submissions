class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        min_price = prices[0]

        for price in prices:
            min_price = min(price, min_price)

            cur_profit = price - min_price

            max_profit = max(cur_profit, max_profit)
        
        return max_profit