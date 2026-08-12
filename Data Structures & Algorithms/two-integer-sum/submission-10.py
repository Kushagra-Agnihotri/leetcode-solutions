class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, n in enumerate(nums):

            d = target - nums[i]
            if d in h:
                return [h[d],i]
            h[n] = i