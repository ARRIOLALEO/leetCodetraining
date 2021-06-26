class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = []
        for price in range(len(prices) -1):
            if prices[price] < prices[price + 1]:
                profit.append(prices[price + 1] - prices[price])
        return sum(profit)
