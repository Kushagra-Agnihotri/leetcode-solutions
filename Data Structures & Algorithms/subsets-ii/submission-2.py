class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res  = set()
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.add(tuple(sorted(subset.copy())))
                
                return 
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs(0)
        res = [list(x) for x in res]
        return res