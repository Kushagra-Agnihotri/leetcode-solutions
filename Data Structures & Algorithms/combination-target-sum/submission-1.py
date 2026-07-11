class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        current = []
        def dfs(i):
            nonlocal current,res

            if i >= len(nums):
                return
            if sum(current) == target:
                res.append(current.copy())
                return 
            if sum(current) > target:
                return
            current.append(nums[i])
            dfs(i)
            current.pop()
            dfs(i+1)
        dfs(0)
        return res
            
