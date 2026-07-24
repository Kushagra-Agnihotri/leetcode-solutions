class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [nums[0]]
        suf = [nums[-1]]

        for i in range(1, len(nums)):
            pre.append(pre[-1] * nums[i])
        for i in range(1, len(nums)):
            suf.append(suf[-1] * nums[-i-1])
        print(suf, pre)
        res = []
        res.append(suf[-2])
        for i in range(len(nums)-2):
            res.append(pre[i] * suf[-3-i])
        res.append(pre[-2])
        return res
