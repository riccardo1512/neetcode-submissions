# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        
        l = 0
        node = head
        while node:
            l += 1
            node = node.next
        
        # n - l
        
        i = 0
        node = dummy
        while i < l - n:
            node = node.next
            i += 1
        node.next = node.next.next

        return dummy.next