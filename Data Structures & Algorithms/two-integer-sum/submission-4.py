class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for c in range(len(nums)-1):
            t = target -nums[c]
            for s in range(c+1, len(nums)):
                if nums[s] == t:
                    return [c, s]
        
