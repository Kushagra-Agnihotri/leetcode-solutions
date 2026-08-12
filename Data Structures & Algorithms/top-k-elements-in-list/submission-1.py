from _heapq import heapify
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1+count.get(num, 0)
        h = []
        for num in count.keys():
            heapq.heappush(h, (count[num], num))
            if len(h) > k:
                heapq.heappop(h)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(h)[1])
        return res

