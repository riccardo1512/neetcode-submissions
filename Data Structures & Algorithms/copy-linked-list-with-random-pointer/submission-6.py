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

        cur = head
        while cur:
            newNode = Node(cur.val)
            newNode.next = cur.next
            cur.next = newNode
            cur = cur.next.next
        
        newHead = head.next

        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        cur = head
        while cur:
            newCur = cur.next
            cur.next = newCur.next
            if newCur.next:
                newCur.next = newCur.next.next
            cur = cur.next
        return newHead