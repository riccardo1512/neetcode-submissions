class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        used = [False] * len(nums)
        nums.sort()

        def dfs(i, cur):
            if i >= len(nums):
                res.add(tuple(cur))
                return

            cur.append(nums[i])
            used[i] = True
            dfs(i + 1, cur)

            cur.pop()
            used[i] = False
            dfs(i + 1, cur)
        dfs(0, [])
        return list(res)