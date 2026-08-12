class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        h1= {x:s.count(x) for x in set(s)} 
        h2= {x:t.count(x) for x in set(t)} 

        return h1 == h2
