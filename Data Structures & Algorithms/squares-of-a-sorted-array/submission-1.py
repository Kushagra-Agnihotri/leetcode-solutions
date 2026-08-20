class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        negarr=deque()
        posarr = deque()
        for c in nums:
            if c>=0:
                posarr.append(c)
            else:
                negarr.append(c)
        negarr = deque(list(negarr)[::-1])
        print(negarr)
        ans = []
        while posarr and negarr:
            if posarr[0] ** 2 <  negarr[0] ** 2:
                ans.append(posarr.popleft() ** 2)
            else:
                ans.append(negarr.popleft() ** 2)
        
        if posarr:
            while posarr:
                ans.append(posarr.popleft() ** 2)
        else:
            while negarr:
                ans.append(negarr.popleft() ** 2)
        print(ans)
        return ans
        
