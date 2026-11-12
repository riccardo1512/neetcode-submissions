class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))

        minHeap = [(0, k)] # distance, start
        shortest_paths = {}

        while minHeap:
            cur_distance, node = heapq.heappop(minHeap)

            if node in shortest_paths:
                continue
            
            shortest_paths[node] = cur_distance

            for nei, cost in adj[node]:
                if nei not in shortest_paths:
                    heapq.heappush(minHeap, (cur_distance + cost, nei))
        
        if len(shortest_paths) != n:
            return -1
        
        return max(shortest_paths.values())
        