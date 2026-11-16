class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, cur_sum):
            if cur_sum == target:
                res.append(cur.copy())
                return
            
            for j in range(i, len(nums)):
                if cur_sum + nums[j] > target:
                    continue

                cur.append(nums[j])
                dfs(j, cur, cur_sum + nums[j])
                cur.pop()

        dfs(0, [], 0)
        return res
        