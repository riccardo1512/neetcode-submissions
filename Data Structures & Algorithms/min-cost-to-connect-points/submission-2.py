class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = defaultdict(list)

        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                xi, yi = points[i][0], points[i][1]
                xj, yj = points[j][0], points[j][1]

                distance = abs(xi - xj) + abs(yi - yj)

                adj[i].append((j, distance))
                adj[j].append((i, distance))


        minHeap = [(0, 0, -1)] # cost, node, parent
        visited = set()
        mst_edges = []
        total_cost = 0

        while minHeap and len(visited) < n:
            cost, node, parent = heapq.heappop(minHeap)

            if node in visited:
                continue

            visited.add(node)
            total_cost += cost
            if parent != -1:
                mst_edges.append((parent, node, cost))

            for nei, edj_cost in adj[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, (edj_cost, nei, node))
        
        # if len(visited) != n:
            # return -1, []

        # return total_ost, mst_edges

        return total_cost