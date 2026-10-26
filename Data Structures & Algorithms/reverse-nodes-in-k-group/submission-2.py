# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:


        def reverse(node):
            prev = None
            curr = node
            for i in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                
            node.next = curr
            return prev

        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next

        dummy = ListNode()

        prev = dummy
        curr = head
        while count >= k:
            tail = curr
            prev.next = reverse(curr)

            prev = tail
            curr = prev.next
            count -= k

        return dummy.next