class DSU:

    def __init__(self, n : int):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.components = n

    def find(self, node : int) -> int:
        cur = node
        while self.parent[cur] != cur:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur

    def union(self, u : int, v : int) -> bool:
        pu, pv = self.find(u), self.find(v)

        if pu == pv:
            return False

        if self.rank[pv] > self.rank[pu]:
            pu, pv = pv, pu
        
        self.parent[pv] = pu
        self.rank[pu] += self.rank[pv]
        self.components -= 1

        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges) + 1)
        for u, v in edges:
            if not dsu.union(u, v):
                return [u, v]
        return []
        