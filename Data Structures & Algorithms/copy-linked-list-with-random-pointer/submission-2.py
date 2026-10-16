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
        dummy = Node(0)
        d = {} # old : new
        
        cur = dummy
        while head:
            if head in d:
                cur.next = d[head]
            else:
                d[head] = Node(head.val, None, None)
                cur.next = d[head]
            
            if head.random and head.random in d:
                cur.next.random = d[head.random]
            elif head.random:
                d[head.random] = Node(head.random.val, None, None)
                cur.next.random = d[head.random]
            
            head = head.next
            cur = cur.next
        
        return dummy.next
        