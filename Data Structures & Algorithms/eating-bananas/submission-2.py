class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n, m  = len(piles), max(piles)
        l , r = 1, m
        ans = m
        while l <= r:
            k = (l+r) // 2
            val = sum(math.ceil(p / k) for p in piles)
            if val <= h:
                ans = k
                r = k - 1
            else:
                l = k + 1
        return ans