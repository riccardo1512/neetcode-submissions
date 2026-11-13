class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        minHeap = [(grid[0][0], 0, 0)] # cur_height, r, c
        visited = set()


        while minHeap:
            cur_height, r, c = heapq.heappop(minHeap)

            if (r, c) in visited:
                continue
            
            if r == n - 1 and c == n - 1:
                return cur_height

            visited.add((r, c))
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    heapq.heappush(minHeap, (max(cur_height, grid[nr][nc]), nr, nc))
