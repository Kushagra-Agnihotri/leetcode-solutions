class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {x: [] for x in range(numCourses)}

        for u, v in prerequisites:
            adj[u].append(v)
        visited = set()
        dp ={}
        def dfs(node):
            if node in visited:
                return False
            if node in dp:
                return dp[node]
            visited.add(node)

            for nei in adj[node]:
                if not dfs(nei):
                    dp[node] = False
                    return False
            visited.remove(node)
            dp[node] = True
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
