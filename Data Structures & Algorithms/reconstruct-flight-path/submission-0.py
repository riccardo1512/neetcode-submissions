class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        tickets.sort(reverse = True)
        
        adj = defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)
        
        res = []

        def dfs(node):
            while adj[node]:
                nei = adj[node].pop()
                dfs(nei)
            
            res.append(node)
        
        dfs("JFK")
        return res[::-1]