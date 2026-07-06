class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i , j =0, 0
        if not s:
            return True
        for i in range(len(t)):
            if t[i] == s[j]:
                j+=1
            if j >= len(s):
                break
        return j == len(s)