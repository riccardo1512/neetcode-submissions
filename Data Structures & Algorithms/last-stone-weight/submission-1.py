class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        
        while len(heap) >= 2:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)

            remaining = abs(first - second)

            if remaining:
                heapq.heappush(heap, -remaining)

        if heap:
            return -heapq.heappop(heap)
        
        return 0