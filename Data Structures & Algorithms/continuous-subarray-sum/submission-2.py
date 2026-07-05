class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        for i in range(len(nums)):
            s = nums[i]
            for j in range(i+1,len(nums)):
                s+= nums[j]

                if s%k == 0:
                    return True
        return False