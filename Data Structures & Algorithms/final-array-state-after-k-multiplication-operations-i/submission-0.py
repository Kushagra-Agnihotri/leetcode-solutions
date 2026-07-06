class Solution:
    def getFinalState(self, nums: List[int], k: int, mul: int) -> List[int]:
       import heapq as hq

       pq = [(num, i) for i, num in enumerate(nums)]
       hq.heapify(pq)
       print(pq)
       for _ in range(k):
            x, i = hq.heappop(pq)
            nums[i] = x*mul
            hq.heappush(pq, (nums[i], i))

       return nums
