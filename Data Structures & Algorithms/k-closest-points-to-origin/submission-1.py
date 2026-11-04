class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for p in points:
            x1, y1 = p
            distance = (x1 ** 2 + y1 ** 2)

            heapq.heappush(heap, (-distance, p))

            while len(heap) > k:
                heapq.heappop(heap)
        
        return [p[1] for p in heap]