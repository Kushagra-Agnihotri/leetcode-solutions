# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = [root]
        while queue:
            current =  queue.pop()
            temp = TreeNode()
            if current.right:
                queue.append(current.right)
            if current.left:
                queue.append(current.left)
            temp = current.right
            current.right = current.left
            current.left = temp


        return root
        