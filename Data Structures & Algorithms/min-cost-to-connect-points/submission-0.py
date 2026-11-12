class DSU:

    def __init__(self, n : int):
        self.parents = list(range(n))
        self.rank = [1] * n
        self.components = n

    def find(self, node : int) -> int:
        cur = node
        while self.parents[cur] != cur:
            self.parents[cur] = self.parents[self.parents[cur]]
            cur = self.parents[cur]
        return cur

    def union(self, u : int, v : int) -> bool:
        pu, pv = self.find(u), self.find(v)

        if pu == pv:
            return False

        if self.rank[pv] > self.rank[pu]:
            pu, pv = pv, pu

        self.parents[pv] = pu
        self.rank[pu] += self.rank[pv]
        self.components -= 1

        return True 

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)

        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                xi, yi = points[i][0], points[i][1]
                xj, yj = points[j][0], points[j][1]

                distance = abs(xi - xj) + abs(yi - yj)

                edges.append((i, j, distance)) # non dobbiamo aggiungere anche (j, i, distance), usiamo edges, non adj
        edges.sort(key = lambda x : x[2])

        dsu = DSU(n)
        mst_edges = []
        total_cost = 0

        for u, v, c in edges:
            if dsu.union(u, v):
                mst_edges.append((u, v, c))
                total_cost += c

                if len(mst_edges) == n - 1:
                    break
        return total_cost