class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dp = {}

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return 0

            if (r, c) in dp:
                return dp[(r, c)]


            neiMax = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < ROWS and 0 <= nc < COLS and matrix[nr][nc] > matrix[r][c]:
                    neiMax = max(neiMax, dfs(nr, nc))
            res = neiMax + 1

            dp[(r, c)] = res
            return res
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c))
        
        return res