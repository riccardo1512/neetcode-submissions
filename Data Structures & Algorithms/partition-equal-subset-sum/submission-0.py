class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) // 2

        memo = {}

        def dfs(i, cur_sum):
            if cur_sum == target:
                return True
            
            if i >= len(nums) or cur_sum > target:
                return False

            if (i, cur_sum) in memo:
                return memo[(i, cur_sum)]

            prendi = dfs(i + 1, cur_sum + nums[i])
            salta = dfs(i + 1, cur_sum)

            res = prendi or salta
            memo[(i, cur_sum)] = res

            return res

        return dfs(0, 0)