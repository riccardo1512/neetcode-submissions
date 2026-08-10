class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0

        for i in range(len(prices) - 1):

            for j in range(i+1, len(prices)):

                profit = -prices[i] + prices[j]
                res = max(res, profit)
        
        return res


        