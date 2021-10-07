class Solution:
    def waysToChange(self, n):

        w = [1, 5, 10, 25]


        dp = [[0] * (n + 1) for _ in range(len(w) + 1)]

        for i in range(len(dp[0])):

            dp[0][i] = 0

        for j in range(len(dp)):

            dp[j][0] = 1



        for i in range(1, len(w) + 1):

            for j in range(1, n + 1):

                if w[i - 1] <= j:

                    dp[i][j] = dp[i - 1][j] + dp[i][j - w[i - 1]]
                else:

                    dp[i][j] = dp[i - 1][j]

        # 找出种类数量
        return dp[-1][n] % 1000000007






