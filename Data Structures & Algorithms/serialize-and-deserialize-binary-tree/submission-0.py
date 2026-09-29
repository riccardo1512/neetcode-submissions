# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ""

        def dfs(node):
            nonlocal res
            if not node:
                res += "[None]"
                return
            
            res += f"[{node.val}]"

            dfs(node.left)
            dfs(node.right)
            return
        
        dfs(root)
        return res

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        i = 0
        def dfs():
            nonlocal i

            j = i
            while data[j] != ']':
                j += 1
            
            subString = data[i + 1 : j]

            i = j + 1
            if subString == "None":
                return None
            
            node = TreeNode(int(subString))
            
            
            node.left = dfs()
            node.right = dfs()

            return node
        
        return dfs()