class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."]*n for _ in range(n)]
        print(board)

        
        def check(i,j, board):
            row = board[i]
            col = [board[x][j] for x in range(n)]
            # Upper-left diagonal
            ldia = [board[i-x-1][j-x-1] for x in range(min(i,j))]
            # Upper-right diagonal
            rdia = [board[i-x-1][j+x+1] for x in range(min(i, n-1-j))]
            
            if "Q" in col+row+ldia+rdia:
                return False
            return True

        def dfs(k):
            nonlocal board
            
            if k==n:
                res.append(["".join(row) for row in board])
                return
            for j in range(n):
                if check(k,j, board):           

                    board[k][j] = "Q"
                    dfs(k+1)
                    board[k][j] = "."
        dfs(0)
        return res
