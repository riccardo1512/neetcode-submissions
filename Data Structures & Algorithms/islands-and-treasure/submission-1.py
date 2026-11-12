class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))


        while queue:
            r, c = queue.popleft()
             
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))
        
