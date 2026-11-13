class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {}

        def dfs(i, cur_sum):
            
            if cur_sum == target and i >= len(nums):
                return 1
            
            if i >= len(nums):
                return 0

            if (i, cur_sum) in dp:
                return dp[(i, cur_sum)]

        
            add = dfs(i + 1, cur_sum + nums[i])
            substract = dfs(i + 1, cur_sum - nums[i])

            res = add + substract

            dp[(i, cur_sum)] = res
            return res

        return dfs(0, 0)
        