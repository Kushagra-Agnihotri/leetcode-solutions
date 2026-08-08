class DSU:
    def __init__(self, n) -> None:
        self.par = list(range(n+1))
        self.rank = [1] * (n+1)
    def find(self, n):
        if n !=  self.par[n]:
            self.par[n] =  self.find(self.par[n])
        return self.par[n]
    def union(self, n1 , n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2: return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] +=1
        return True
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                edges.append((dist, i, j))
        edges.sort()
        #print(edges)
        dsu = DSU(len(points))      
        cost = 0
        for w , u, v in edges:
            if dsu.union(u, v):
                cost+=w
        return cost
        