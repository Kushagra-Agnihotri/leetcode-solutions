class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        h= {nums[i]: i for i in range(len(nums))}
        print(h)
        for i in range(len(nums)):
            t = target - nums[i]
            if t in h and h[t] != i:
                res = [i, h[t]]
                break
        return res