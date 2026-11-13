class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = {}

        def dfs(i, rem):
            if rem == 0:
                return 1
            if rem < 0 or i >= len(coins):
                return 0

            if (i, rem) in dp:
                return dp[(i, rem)]
           
            take = dfs(i, rem - coins[i])
            skip = dfs(i + 1, rem)

            combinations = take + skip
            dp[(i, rem)] = combinations
            return combinations
        
        return dfs(0, amount)
        