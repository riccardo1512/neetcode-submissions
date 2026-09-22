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


        queuep = deque([p]) if p else None
        queueq = deque([q]) if q else None

        while queuep and queueq:

            level_length_p = len(queuep)
            level_length_q = len(queueq)
            if level_length_p != level_length_q:
                return False

            
            for _ in range(level_length_p):
                nodep = queuep.popleft()
                nodeq = queueq.popleft()

                if nodep.val != nodeq.val:
                    return False
                
                if (not nodep.left and nodeq.left) or (nodep.left and not nodeq.left) or (not nodep.right and nodeq.right) or (nodep.right and not nodeq.right):
                    return False

                if nodep.left:
                    queuep.append(nodep.left)
                if nodep.right:
                    queuep.append(nodep.right)
                if nodeq.left:
                    queueq.append(nodeq.left)
                if nodeq.right:
                    queueq.append(nodeq.right)
        
        if queuep or queueq:
            return False
        return True
        