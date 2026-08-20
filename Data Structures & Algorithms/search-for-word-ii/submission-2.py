class TreeNode:
    def __init__(self) -> None:
        self.children = dict()
        self.word = False

class PreFixTree:
    def __init__(self) -> None:
        self.root = TreeNode()

    def add(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TreeNode()
            cur = cur.children[c]
        cur.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tree = PreFixTree()
        for word in words:
            tree.add(word)
        
        res = set()
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c, node, word):
            if r < 0 or c < 0 or r == rows or c == cols or \
               (r, c) in visited or board[r][c] not in node.children:
                return

            visited.add((r, c))
            char = board[r][c]
            next_node = node.children[char]
            word += char
            if next_node.word:
                res.add(word)

            dfs(r + 1, c, next_node, word)
            dfs(r - 1, c, next_node, word)
            dfs(r, c + 1, next_node, word)
            dfs(r, c - 1, next_node, word)
            
            visited.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, tree.root, "")
        
        return list(res)