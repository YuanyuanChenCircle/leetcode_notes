class Solution:
    def maxProfit(self, prices):

        # 每天有两种选择，选或者不选

        # 二维度

        dp = [[0] * 2 for i in range(len(prices))]

        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, len(prices)):

            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])

            dp[i][1] = max(- prices[i], dp[i - 1][1])

        return dp[-1][0]

