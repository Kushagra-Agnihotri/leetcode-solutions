class Solution:
    ans = set()
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res  = []
        def dfs(i, current):
            if i >= len(nums):
                res.append(current)
                return 
            dfs(i+1, current + [nums[i]])
            dfs(i+1, current)
        dfs(0, [])
        return res