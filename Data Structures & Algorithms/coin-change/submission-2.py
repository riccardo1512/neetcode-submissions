class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {} # sum : min remaining

        def dfs(amount):
            if amount == 0:
                return 0
            
            res = float("inf")
            for c in coins:
                if amount - c >= 0:
                    if amount - c in dp:
                        res = min(res, 1 + dp[amount - c])
                    else:
                        res = min(res, 1 + dfs(amount - c))
            
            dp[amount] = res
            return res

        res = dfs(amount) 
        return -1 if res >= float("inf") else res