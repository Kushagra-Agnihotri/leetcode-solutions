# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)
        out = []
        while q:
            l = len(q)
            level =[]
            for i in range(l):
                current = q.popleft()
                if current:
                    q.append(current.left)
                    q.append(current.right)
                    level.append(current.val)
            print(level)
            if level:
                out.append(level[-1])
        return out
