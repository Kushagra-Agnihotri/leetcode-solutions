class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hs = {}
        for i in range(len(nums)):
            hs[nums[i]] = i
        for i in range(len(nums)):
            t= target - nums[i]
            if t in hs and hs[t]!= i:
                return [i, hs[t]]
        print(hs)
        return []
