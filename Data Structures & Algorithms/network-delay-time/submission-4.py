class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {x:[] for x in range(1, n+1)}

        for u, v, w in times:
            adj[u].append((v, w))

        dist = {node: float("inf") for node in range(1, n+1) }
        dist[k] = 0


        visited = set()
        last_visited = k
        pq = [(0, k)]
        while pq:
            d , node = heapq.heappop(pq)
    
            if node in visited:
                continue
            last_visited = node
            visited.add(node)
            for nei, w in adj[node]:
                nd = dist[node] + w
                if nd < dist.get(nei, float("inf")):
                    dist[nei] = nd
                    heapq.heappush(pq, (nd, nei))
        print(dist, visited)
        if len(visited) < n or  dist[last_visited] == float("inf"): return -1
        return dist.get(last_visited, -1)
        