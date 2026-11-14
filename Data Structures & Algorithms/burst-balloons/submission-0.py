class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = {}
        nums = [1] + nums + [1]

        def dfs(l, r):
            if l > r:
                return 0
            
            if (l, r) in dp:
                return dp[(l, r)]

            max_coins = 0
            for k in range(l, r + 1):
                coins = (nums[l - 1] * nums[k] * nums[r + 1]) + dfs(l, k - 1) + dfs(k + 1, r)
                max_coins = max(max_coins, coins)
            dp[(l, r)] = max_coins
            
            return max_coins

        return dfs(1, len(nums) - 2)

            
        