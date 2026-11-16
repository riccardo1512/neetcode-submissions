class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def dfs(i, cur):
            if i >= len(nums):
                res.append(cur.copy())
                return

            for j in range(0, len(nums)):
                if used[j]:
                    continue
                
                cur.append(nums[j])
                used[j] = True

                dfs(i + 1, cur)
                
                cur.pop()
                used[j] = False
        
        dfs(0, [])
        return res
        