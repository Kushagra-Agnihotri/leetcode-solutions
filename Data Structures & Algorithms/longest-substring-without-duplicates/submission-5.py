class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        w_count = defaultdict(int)
        ans = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            while w_count[s[r]] >= 1:
                w_count[s[l]] -=1
                l+=1
            w_count[s[r]] +=1
            ans = max(ans, r-l+1)
        print(ans)
        return ans
            