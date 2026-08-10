class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW  = len(grid)
        COL = len(grid[0])
        tchests = []
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    tchests.append((i, j, 0))

        queue = deque(tchests)
        dirc = [(0, 1), (0, -1), (1, 0),(-1, 0)]
        while queue:
            x, y, dis = queue.popleft()
            for dx ,dy in dirc:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= ROW or ny >= COL or grid[nx][ny] <= dis + 1:
                    continue
                grid[nx][ny] = dis + 1
                queue.append((nx, ny, dis + 1))