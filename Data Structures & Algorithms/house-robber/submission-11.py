class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        if n ==2 : return max(nums)
        dp = [0] * (n+1)

        dp[-1] = nums[-1]
        dp[-2] = nums[-2]
        i = n-3
        while i >=0:
            print(i, dp, nums[i], dp[i+2], dp[i+1])
            dp[i-n] = max(nums[i] + dp[i+2-n], dp[i+1-n])
            i-=1
        return dp[1]