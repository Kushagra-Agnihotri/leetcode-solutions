# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0
            return 1+ max(dfs(root.right),dfs(root.left))
        ms = 0
        def func(root):
            nonlocal ms
            if not root:
                return 0
            lf = dfs(root.left)
            rt = dfs(root.right)
            print(lf,rt)
            ms = max(ms, abs(lf-rt))
            func(root.right)
            func(root.left)
        func(root)
        return ms <2