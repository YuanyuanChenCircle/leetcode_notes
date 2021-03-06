class Solution:
    def coinChange(self, coins, amount):


        dp = [[amount + 1] * (amount + 1) for i in range(len(coins) + 1)]


        # for i in range(len(dp[0])):

        #     dp[0][i] = 0

        for i in range(len(dp)):

            dp[i][0] = 0

        for i in range(1, len(coins) + 1):

            for j in range(1, amount + 1):

                if coins[i - 1] <= j:

                    dp[i][j] = min(dp[i - 1][j], dp[i][j - coins[i - 1]] + 1)

                else:


                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]







