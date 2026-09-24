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
            if not graphMap[i]:
                return True
            
            visited.add(i)
            while graphMap[i]:
                j = graphMap[i].pop()
                if j != parent and not dfs(j, i):
                    return False
            
            return True
        
        if not dfs(0, -1):
            return False
        
        for i in graphMap:
            if graphMap[i]:
                return False
        return True