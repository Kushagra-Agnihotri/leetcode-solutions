class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        resIdx = (0, 0)
        memo = {}
        def dfs(i, j):
            nonlocal resLen, resIdx
            if (i, j) in memo: return memo[(i, j)]
            if i >= j:
                is_pal = True
            elif s[i] == s[j] and (j - i == 1 or dfs(i + 1, j - 1)):
                is_pal = True
            else:
                is_pal = False
            
            if is_pal:
                if j - i + 1 > resLen:
                    resLen = j - i + 1
                    resIdx = (i, j)
            else:
                dfs(i + 1, j)
                dfs(i, j - 1)
            memo[(i, j)] = is_pal
            return is_pal
        dfs(0, len(s) - 1)
        x, y = resIdx
        return s[x:y+1]