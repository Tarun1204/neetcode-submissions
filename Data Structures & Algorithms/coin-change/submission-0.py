class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        im = amount +1
        dp = [im] * (amount+1)
        dp[0] = 0

        for a in range(1 , amount +1):
            for coin in coins:
                if coin <=a :
                    c_n = 1 + dp[a - coin]
                    if c_n < dp[a]:
                        dp[a] = c_n
        result = -1 if dp[amount] == im else dp[amount]
        return result

        