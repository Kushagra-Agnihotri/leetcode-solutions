class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in range(len(strs)):
            key = str(sorted(strs[i]))
            if key not in res:
                res[key] = [strs[i]]
            else:
                res[key].append(strs[i])
        print(res)
        return  list(res.values())

