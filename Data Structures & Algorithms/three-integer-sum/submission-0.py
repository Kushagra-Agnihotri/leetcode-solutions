class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for i in range(len(nums)):
            t = - nums[i]
  
            h = {}
            for j in range(i+1, len(nums)):
                n =nums[j]
                d = t - nums[j]
                if d in h:
                    res.add(tuple(sorted([nums[i], nums[h[d]],nums[j]])))
                h[n] = j
        return list(list(i) for i in res)