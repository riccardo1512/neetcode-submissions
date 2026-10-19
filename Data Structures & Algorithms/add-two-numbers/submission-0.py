# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()

        cur = head
        remain = 0
        while l1 or l2:
            s = 0
            if l1 and l2:
                s = l1.val + l2.val + remain
            elif l1:
                s = l1.val + remain
            elif l2:
                s = l2.val + remain
            
            cur.next = ListNode(s % 10)
            remain = s // 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
            cur = cur.next
        
        if remain:
            cur.next = ListNode(remain)

        return head.next