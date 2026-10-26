# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next

        dummy = ListNode()
        dummy.next = head
        group_prev = dummy

        while count >= k:
            prev, curr = None, group_prev.next
            group_tail = curr

            for i in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            group_prev.next = prev
            group_tail.next = curr
            group_prev = group_tail
            count -= k

        return dummy.next