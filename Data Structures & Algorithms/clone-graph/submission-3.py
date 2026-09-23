"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        
        oldToNew = {}
        q = deque([node])
    
        while q:

            cur = q.popleft()

            if cur not in oldToNew:
                oldToNew[cur] = Node(cur.val)

            for n in cur.neighbors:
                if n not in oldToNew:
                    oldToNew[n] = Node(n.val)
                    q.append(n)
                oldToNew[cur].neighbors.append(oldToNew[n])
        return oldToNew[node]