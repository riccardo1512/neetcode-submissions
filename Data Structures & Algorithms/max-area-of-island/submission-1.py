class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1:
                return 0

            queue = deque([(r, c)])
            area = 0
            grid[r][c] = -1

            while queue:
                r, c = queue.popleft()
                area += 1
            
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        queue.append((nr, nc))
                        grid[nr][nc] = -1
                
            return area

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = bfs(r, c)
                    res = max(area, res)
        return res