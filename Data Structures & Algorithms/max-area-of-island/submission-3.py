class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        row = len(grid)
        col = len(grid[0])
        visited = set()
        def dfs(i,j):
            if min(i, j) <0 or i>=row or j>= col or (i, j) in visited or grid[i][j] == 0:
                return 0

            visited.add((i, j))
            temp = 1
            for dx , dy in dirc:
                temp += dfs(i+dx, j+dy)

            return temp
        ans = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] ==1 :
                    ans = max(ans, dfs(r, c))
        return ans


