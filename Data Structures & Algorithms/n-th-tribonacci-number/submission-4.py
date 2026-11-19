class Solution:
    def tribonacci(self, n: int) -> int:
        dp = {}
        
        def dfs(i):
            if i <= 2:
                if i == 0:
                    return 0
                else:
                    return 1
            
            if i in dp:
                return dp[i]

            dp[i] = dfs(i - 1) + dfs(i - 2) + dfs(i - 3)
            return dp[i]

        return dfs(n)