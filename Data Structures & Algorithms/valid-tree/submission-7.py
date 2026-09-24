class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graphMap = {i:[] for i in range(n)}
        visited = set()

        for a, b in edges:
            graphMap[a].append(b)
            graphMap[b].append(a)
        
        def dfs(i, parent):
            if i in visited:
                return False
            
            visited.add(i)
            for j in graphMap[i]:
                if j != parent and not dfs(j, i):
                    return False
            return True
        
        if not dfs(0, -1):
            return False
        
        for i in graphMap:
            if i not in visited:
                return False
        return True