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
        
        cur  = head
        while cur:
            newNode = Node(cur.val)
            newNode.next  = cur.random
            cur.random = newNode
            cur = cur.next
        
        cur = head
        while cur:
            newNode = cur.random
            newNode.random = newNode.next.random if newNode.next else None
            cur = cur.next
        
        newHead = head.random
        cur = head
        while cur:
            newNode = cur.random
            cur.random = newNode.next
            newNode.next = cur.next.random if cur.next else None
            cur = cur.next
        
        return newHead