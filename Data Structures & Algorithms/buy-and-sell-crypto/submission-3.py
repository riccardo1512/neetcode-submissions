class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0

        l, r = 0, 0

        while l < len(prices) and r < len(prices):

            if prices[r] > prices[l]:
                res = max(res, prices[r] - prices[l])
            else:
                l = r
            
            r += 1

        return res
        