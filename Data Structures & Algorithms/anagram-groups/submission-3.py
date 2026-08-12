class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list )

        for s in strs:
            #key = "".join(sorted(s)) 
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1     
            group[tuple(key)].append(s)
                  
        return list(group.values())

