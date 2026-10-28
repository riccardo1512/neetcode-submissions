# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, v):
            if not node:
                return 0
            
            l = dfs(node.left, max(v, node.val))
            r = dfs(node.right, max(v, node.val))
        
            return (1 if node.val >= v else 0) + l + r
        
        return dfs(root, root.val)


        