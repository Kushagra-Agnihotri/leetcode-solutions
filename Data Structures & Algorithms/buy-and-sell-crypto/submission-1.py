class Solution:
    def maxProfit(self, s: List[int]) -> int:
        i= 0
        ans = 0
        while i < len(s)-1:
            if s[i+1] < s[i] :
                i+=1
                continue
            for j in range(i+1,len(s)):
                ans = max(ans,s[j]-s[i])
            i+=1
        return ans