class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0:0}
        def dfs(amount):
            if amount in dp:
                return dp[amount]
            m = 1e9
            for c in coins:
                if c<=amount:
                    m = min(m, 1+dfs(amount -c))
            print(m)
            dp[amount] = m
            return dp[amount]
        x = dfs(amount)
        return x if x < 1e9 else -1

