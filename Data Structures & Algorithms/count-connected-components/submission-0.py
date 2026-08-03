class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node):
            for nei in adj[node]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)
        adj = [ [] * n for _  in range(n)]
        visited = [False] * n

        for u, v in edges:
            adj[u].append(v)        
            adj[v].append(u)       
        res = 0 
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                res +=1
        return res

      