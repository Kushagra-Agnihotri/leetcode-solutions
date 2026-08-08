class DSU:
    def __init__(self, n) -> None:
        self.par =[i for i in range(n)]
        self.rank = [1] * n

    def find(self, n):
        if n!=  self.par[n]:
            self.par[n] = self.find(self.par[n])
            n = self.par[n]
        return n

    def union(self, n1 , n2):
        p1 , p2 = self.find(n1), self.find(n2)

        if  p1 == p2 : return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] =p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU(len(accounts))
        emails = {}
        for i, acc in enumerate(accounts):
            for e in acc[1:]:
                if e in emails:
                    dsu.union(i, emails[e])
                else:
                    emails[e] = i
        print(emails)

        ans = defaultdict(list)  
        for e, i in emails.items():
            leader = dsu.find(i)
            print(accounts[leader][0])
            ans[leader].append(e)

        res = []
        for i , e in ans.items():
            name = accounts[i][0]
            res.append([name]+sorted(ans[i]))
        return res
        