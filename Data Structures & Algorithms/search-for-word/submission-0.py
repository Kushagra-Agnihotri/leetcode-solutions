class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        print(visited)
        def dfs(i , j , k):
            if k == len(word):
                return True
            if (min(i,j) < 0 or 
                i >= len(board) or
                j >= len(board[0]) or 
                word[k] != board[i][j] or 
                visited[i][j]):
                return False
            visited[i][j] = True
            res = (dfs(i+1, j, k+1) or
                    dfs(i-1, j, k+1) or
                    dfs(i, j+1, k+1) or
                    dfs(i, j-1, k+1))
            visited[i][j] = False
            return res
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False
