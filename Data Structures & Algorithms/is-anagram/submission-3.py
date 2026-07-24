class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 , c2 = {}, {}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] not in c1:
                c1[s[i]] = 1
            else:
                c1[s[i]] += 1   
            if t[i] not in c2:
                c2[t[i]] = 1
            else:
                c2[t[i]] += 1        
        for val in c1:
            if val not in c2 or c1[val] != c2[val]:
                return False
        return True      
            