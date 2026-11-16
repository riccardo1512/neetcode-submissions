class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(openN, closeN, cur):
            if openN == closeN == n:
                res.append(''.join(cur))
                return
            
            if openN < n:
                cur.append('(')
                dfs(openN + 1, closeN, cur)
                cur.pop()
            if closeN < openN:
                cur.append(')')
                dfs(openN, closeN + 1, cur)
                cur.pop()
        
        dfs(0, 0, [])
        return res
        