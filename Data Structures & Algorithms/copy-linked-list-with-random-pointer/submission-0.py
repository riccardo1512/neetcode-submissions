"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        d = {}
        
        curr = head
        while curr:
            d[curr] = Node(curr.val)
            curr = curr.next
            
        curr = head
        while curr:
            if curr.next:
                d[curr].next = d[curr.next]
            if curr.random:
                d[curr].random = d[curr.random]
            curr = curr.next
            
        return d[head]