class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {x : [] for x in range(len(points))}

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dist = abs(points[j][1]- points[i][1]) + abs(points[j][0] - points[i][0])
                adj[i].append((j, dist))
                adj[j].append((i, dist))
        #print(adj)

        minHeap = []
        visit = set([0])
        mst = []
        min_cost = 0
        for nei, w in adj[0]:
            heapq.heappush(minHeap, (w, 0, nei))
        
        while len(visit) < len(points):
            w, n1, n2 = heapq.heappop(minHeap)
            if n2 in visit:
                continue
            min_cost += w
            mst.append([n1, n2])
            visit.add(n2)
            for nei, w in adj[n2]:
                if nei not in visit:
                    heapq.heappush(minHeap, (w, n2, nei))
        print(visit, mst)
        return min_cost





    

