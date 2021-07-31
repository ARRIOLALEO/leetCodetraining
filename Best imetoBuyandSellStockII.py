class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        
        for price in range(1,len(prices)):
            if buy < prices[price]:
                profit += prices[price] - buy
                buy = prices[price]
            else:
                buy = prices[price]
                
        return profit
