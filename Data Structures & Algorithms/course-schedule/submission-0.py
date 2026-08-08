
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
# Given a directed acyclical graph, return a valid
# topological ordering of the graph.
        adj = {x:[] for x in range(numCourses)}
        indeg = [0] * numCourses
        for u, v in prerequisites:
            adj[u].append(v)
            indeg[v]+=1
        q = deque()
        for node in adj:
            if indeg[node] == 0:
                q.append(node)
        print(q)
        current = 0

        while q:
            node = q.popleft()
            current+=1
            print(node)
            for nei in adj[node]:
                indeg[nei] -=1
                if indeg[nei] == 0:
                    q.append(nei)
        return current == numCourses

            