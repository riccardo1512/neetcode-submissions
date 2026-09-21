# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        res = False

        node = head

        # val += 1000 on all of the nodes, check for already incremented nodes
        while node:
            if node.val > 1000:
                res = True
                break
            else:
                node.val += 1000
                node = node.next

        node = head

        # restore the linked list values and return res
        while node:
            if node.val <= 1000:
                break
            else:
                node.val -= 1000
                node = node.next
        
        return res