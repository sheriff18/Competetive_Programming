

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for curr_price in prices[1:]:
            max_profit = max(max_profit, curr_price - min_price)
            min_price = min(min_price, curr_price)
        return max_profit

	
  

        
