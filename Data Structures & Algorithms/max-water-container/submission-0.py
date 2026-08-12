class Solution: 
    def maxArea(self, h: List[int]) -> int: 
        n = len(h) 
        l, r = 0, n - 1
        
        res = 0
        while l < r:
            width = r - l
            height = min(h[l], h[r])
            res = max(res, width * height)

            if h[l] < h[r]:
                l += 1
            else:
                r -= 1
        return res