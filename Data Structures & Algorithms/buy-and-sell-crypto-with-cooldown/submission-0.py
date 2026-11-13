class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = {}

        def dfs(i, buying):

            if i >= len(prices):
                return 0

            if (i, buying) in dp:
                return dp[(i, buying)]


            if buying:
                take = -prices[i] + dfs(i + 1, False)
                skip = dfs(i + 1, True)

                profit = max(take, skip)
                dp[(i, buying)] = profit
                return profit
            else:

                sell = + prices[i] + dfs(i + 2, True)
                notSell = dfs(i + 1, False)

                profit = max(sell, notSell)

                dp[(i, buying)] = profit
                return profit

        return dfs(0, True)

        