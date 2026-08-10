class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])

        rotten = []
        n = 0

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    n+=1
                if grid[i][j] == 2:
                    rotten.append((i, j, 0))
        q = deque(rotten)
        dirc = [(0, 1), (0, -1),(1, 0) , (-1, 0)]
        max_time = 0
        while q:
            x, y , time = q.popleft()
            for dx , dy in dirc:
                nx , ny = x+dx, y+dy
                if min(nx, ny) <0 or nx >= ROW or ny >= COL or grid[nx][ny] in [0, 2]:
                    continue
                print(x, y, nx, ny, time)
                n-=1
                q.append((nx, ny, time+1))
                max_time = max(max_time, time+1)
                grid[nx][ny] = 2
        if n: return -1
        return max_time
