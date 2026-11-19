class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        dp = {}

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or obstacleGrid[r][c] == 1:
                return 0
            if r == ROWS - 1 and c == COLS - 1:
                return 1

            if (r, c) in dp:
                return dp[(r, c)]
            
            res = dfs(r + 1, c) + dfs(r, c + 1)
            dp[(r, c)] = res
            return res
        

        return dfs(0, 0)