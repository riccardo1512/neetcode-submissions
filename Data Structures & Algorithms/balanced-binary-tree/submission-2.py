# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def rec(node):
            if not node:
                return 0
            
            left = rec(node.left)
            right = rec(node.right)

            if abs(left - right) > 1:
                return float("inf")
            
            return max(left, right) + 1
        
        return False if rec(root) == float("inf") else True
        