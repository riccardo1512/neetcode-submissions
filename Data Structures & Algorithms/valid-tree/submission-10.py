class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: # così non ho bisogno di controllare i cicli, controllo dopo solo se raggiungo tutti da 0
            return False
        
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
        
            for nei in adj[node]:
                dfs(nei)

        dfs(0)
        
        return len(visited) == n