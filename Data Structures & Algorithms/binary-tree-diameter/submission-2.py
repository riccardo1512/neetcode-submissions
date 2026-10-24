# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def dfs(node):
            if not node:
                return (0, 0)
            
            l = dfs(node.left)
            r = dfs(node.right)

            path1 = 1 + max(l[0], r[0])
            path2 = max(l[0] + r[0], l[1], r[1])
            
            return (path1, path2)

        return dfs(root)[1]