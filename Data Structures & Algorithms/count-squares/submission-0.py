class CountSquares:

    def __init__(self):
        self.pts_count = defaultdict(int)
        self.points = []
        

    def add(self, point: List[int]) -> None:
        p = (point[0], point[1])
        self.pts_count[p] += 1
        self.points.append(p)
        

    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0

        for x, y in self.points:
            if abs(px - x) != abs(py - y) or px == x or py == y:
                continue
            
            corner1 = (px, y)
            corner2 = (x, py)

            res += self.pts_count[corner1] * self.pts_count[corner2]
        
        return res
        
