class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def dfs(cur):
            if len(cur) >= len(nums):
                res.append(cur.copy())
                return
            
            for j in range(0, len(nums)):
                if used[j]:
                    continue
                
                cur.append(nums[j])
                used[j] = True
                dfs(cur)

                cur.pop()
                used[j] = False
        dfs([])
        return res