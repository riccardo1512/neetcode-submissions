class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for n in nums:
            for s in range(target, n - 1, -1):
                dp[s] = dp[s] or dp[s - n]
        return dp[target]
                
