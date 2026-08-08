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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)
        dsu = DSU(n)
        for u, v in edges:
            if not dsu.union(u, v):
                return[u, v]
        
