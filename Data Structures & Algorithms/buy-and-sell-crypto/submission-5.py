class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        if len(prices) <= 1:
            return 0
        
        l = 0
        r = 1

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                res = max(res, profit)
            else:
                l = r
            r += 1
        
        return res