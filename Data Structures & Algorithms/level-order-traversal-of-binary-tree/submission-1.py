# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        ans = []
        if not root:
            return []
        while q:
            l = len(q)
            level =[]
            for i in range(l):
                current = q.popleft()
                print(current.val)

                level.append(current.val)
                lf = current.left
                rt = current.right
                if lf:
                    q.append(lf)
                if rt:
                    q.append(rt)
            print(level)
            ans.append(level)

        return ans