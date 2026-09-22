# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True

        stackP = [p] if p else []
        stackQ = [q] if q else []

        while stackP and stackQ:

            if len(stackP) != len(stackQ):
                return False

            nodeP = stackP.pop()
            nodeQ = stackQ.pop()
            
            if nodeP.val != nodeQ.val:
                return False

            if (not nodeP.left and nodeQ.left) or (nodeP.left and not nodeQ.left) or (not nodeP.right and nodeQ.right) or (nodeP.right and not nodeQ.right):
                return False

            if nodeP.left:
                stackP.append(nodeP.left)
            if nodeP.right:
                stackP.append(nodeP.right)
            if nodeQ.left:
                stackQ.append(nodeQ.left)
            if nodeQ.right:
                stackQ.append(nodeQ.right)
        if stackP or stackQ:
            return False
        return True
        