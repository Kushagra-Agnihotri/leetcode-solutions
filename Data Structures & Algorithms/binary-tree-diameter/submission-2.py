# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia = 0
        def dfs(root):
            nonlocal dia
            if not root:
                return 0
   
            d = dfs(root.right)+dfs(root.left)
            dia = max(d, dia)
            return 1+max(dfs(root.right),dfs(root.left))
        dfs(root)
        return dia