class Solution:
    def __init__(self) -> None:
        self.dp1 = {}
        self.dp2 = {}
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n1 , n2 = nums[1:] , nums[:-1]

        return max(self.dfs(0,len(n1), n1 , True), self.dfs(0, len(n2), n2, False))

    def dfs(self, i,n ,  nums, flag):
        if i >= n:
            return 0
        if flag:
            if i in self.dp1:
                return self.dp1[i]
            self.dp1[i] = max(nums[i] + self.dfs(i+2, n , nums, flag), self.dfs(i+1, n , nums, flag))


            return self.dp1[i]
        else:
            if i in self.dp2:
                return self.dp2[i]
            self.dp2[i] = max(nums[i] + self.dfs(i+2, n , nums, flag), self.dfs(i+1, n , nums, flag))


            return self.dp2[i]
        