class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # 10,6,5,6,4

        res = 0

        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):

                res = max(res, prices[j] - prices[i])
        return res
        