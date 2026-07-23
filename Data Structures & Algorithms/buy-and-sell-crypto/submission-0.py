class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_ptr, right_ptr = 0, 1
        cur_profit = 0
        
        while right_ptr < len(prices):
            profit = prices[right_ptr] - prices[left_ptr]

            if profit > 0:
                cur_profit = max(profit, cur_profit)
            else:
                left_ptr = right_ptr

            right_ptr += 1
        
        return cur_profit


            