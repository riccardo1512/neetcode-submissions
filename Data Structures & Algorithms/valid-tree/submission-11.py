class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: # così non ho bisogno di controllare i cicli, controllo dopo solo se raggiungo tutti da 0
            return False
        
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        visited = set()
        visited.add(0)
        
        queue = deque([(0, -1)])
        while queue:
            node, parent = queue.popleft()

            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False

                visited.add(nei)
                queue.append((nei, node))
        return len(visited) == n
        