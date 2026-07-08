# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checkIfSame(p,q):
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return checkIfSame(p.right,q.right) and checkIfSame(p.left,q.left)
            else:
                return False
        if not root and subRoot:
            return False
        if not subRoot:
            return True
        if checkIfSame(root,subRoot):
            return True
        return self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)
        
