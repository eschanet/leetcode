class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_profit = prices[0], 0
        
        for curr_price in prices:
            min_price = min(min_price, curr_price)
            max_profit = max(curr_price - min_price, max_profit)
            
        return max_profit