class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, cur):
            if len(cur) >= len(nums):
                res.append(cur.copy())
            
            for j in range(0, len(nums)):
                if j > len(nums) or nums[j] in cur:
                    continue
                
                cur.append(nums[j])
                dfs(j + 1, cur)
                cur.pop()
        dfs(0, [])
        return res