class Solution:
    def numWays(self, n, k):

        dp = [[0] * 2 for _ in range(n + 1)]

        # 初始化
        dp[1][0], dp[1][1] = 0, k

        # 迭代

        for i in range(2, n + 1):

            dp[i][0] = dp[i - 1][1]

            dp[i][1] = (dp[i - 1][0] + dp[i - 1][1]) * (k - 1)

        return dp[n][0] + dp[n][1]