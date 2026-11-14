class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = {}

        def dfs(i, opened):
            if i >= len(s) and opened == 0:
                return True
            if i >= len(s) or opened < 0:
                return False
            
            if (i, opened) in dp:
                return dp[(i, opened)]
            
            res = False
            if s[i] == '(':
                res = dfs(i + 1, opened + 1)
            elif s[i] == ')':
                res = dfs(i + 1, opened - 1)
            else:
                res = dfs(i + 1, opened - 1)
                res = res or dfs(i + 1, opened + 1)
                res = res or dfs(i + 1, opened)

            dp[(i, opened)] = res
            return res

        return dfs(0, 0)