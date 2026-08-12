class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            t = target - nums[i]
            for j in range(i+1,len(nums)):
                if nums[j] == t:
                    res.append(i)
                    res.append(j)
                    break
        return res