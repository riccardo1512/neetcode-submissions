class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        candidates.sort()

        def dfs(i, total):
            if total == target:
                res.append(cur.copy())
                return
            
            for j in range(i, len(candidates)):
                if total + candidates[j] > target:
                    break
                
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                
                cur.append(candidates[j])
                dfs(j + 1, total + candidates[j])
                cur.pop()

        dfs(0, 0)
        return res
        