class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        if not s:
            return 0
        win  = s[l:r+1]
        n = 1
        while l<=r and r < len(s)-1:
            #print(l , r,win, n)
            if s[r+1] not in win:
                r=r+1                
            else:                
                l = r = l+1
            win = s[l:r+1]            
            n = max(n, r-l+1)
        return n
