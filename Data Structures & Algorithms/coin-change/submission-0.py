class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = []
        dp.append(0)
        for i in range(1, amount+1):
            dp.append(amount+1)

        for coin in coins:

            for i in range(coin , amount +1):
                dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[amount] if dp[amount] != amount+1 else -1