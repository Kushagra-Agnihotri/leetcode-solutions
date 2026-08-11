class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        path = {x:[] for x in range(n)}
        for u, v in edges:
            path[u].append(v)
            path[v].append(u)
        
        visited = set()
        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for nei in path[i]:
                dfs(nei)
        
        dfs(0)
        return len(visited) == n