class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        

        heap = []

        for n, f in count.items():
            heapq.heappush(heap, (f, n))
            if len(heap) > k:
                heapq.heappop(heap)


        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
        