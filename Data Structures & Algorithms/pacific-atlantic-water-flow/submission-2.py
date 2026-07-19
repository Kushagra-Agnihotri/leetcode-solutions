class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atl = set()
        pac = set()
        ROWS = len(heights)
        COLS = len(heights[0])

        def dfs(i, j, visited , prev):
            if min(i, j) < 0 or i>=ROWS or j>=COLS or (i, j) in visited or heights[i][j] < prev:
                return 
            prev = heights[i][j]
            visited.add((i, j))

            dfs(i+1, j, visited, prev)
            dfs(i, j+1, visited, prev)
            dfs(i-1, j, visited, prev)
            dfs(i, j-1, visited, prev)

        for c in range(COLS):
            dfs(0, c , pac, heights[0][c])
            dfs(ROWS -1, c, atl , heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r, 0 , pac, heights[r][0])
            dfs(r, COLS-1, atl , heights[r][COLS-1])
        res = []
        for a in range(ROWS):
            for b in range(COLS):
                if (a,b) in atl and (a, b) in pac:
                    res.append([a, b])
        return res



