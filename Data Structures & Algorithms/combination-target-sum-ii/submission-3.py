class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        current = []
        def dfs(i):
            nonlocal current,res
            if sum(current) == target:
                print("appended : ", current)
                res.append(current.copy())
                return 
            if i == len(nums) or sum(current) > target:
                return

            current.append(nums[i])
            dfs(i+1)
            current.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            dfs(i+1)
        dfs(0)
        return res