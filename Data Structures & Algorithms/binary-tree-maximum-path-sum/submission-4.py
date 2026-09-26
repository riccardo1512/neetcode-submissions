# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = root.val

        def dfs(node):
            nonlocal res

            if not node:
                return 0

            leftSum = max(dfs(node.left), 0)
            rightSum = max(dfs(node.right), 0)

            res = max(res, leftSum + node.val + rightSum)
            return max(leftSum + node.val, rightSum + node.val)

        dfs(root)
        return res