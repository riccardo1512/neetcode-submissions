class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        in_degree = [0] * numCourses
        for crs, pre in prerequisites:
            in_degree[crs] += 1
            adj[pre].append(crs)
        
        queue = deque([crs for crs in range(numCourses) if in_degree[crs] == 0])
        order = []
        while queue:
            crs = queue.popleft()
            order.append(crs)

            for nei in adj[crs]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)
        
        return order if len(order) == numCourses else []