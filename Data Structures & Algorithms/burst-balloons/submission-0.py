class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        nums = [1] + nums + [1]
        dp = {}
        def dfs(nums):
            
            if len(nums) == 2:
                return 0
            if str(nums) in dp:
                return dp[str(nums)]

            mcoins = 0
            for i in range(1, len(nums)-1):
                coins  = nums[i-1] * nums[i] * nums[i+1]
                coins += dfs(nums[:i] + nums[i+1:])
                mcoins = max(mcoins, coins)
            dp[str(nums)] = mcoins
            return mcoins
        return dfs(nums)




        