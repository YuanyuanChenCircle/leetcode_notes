

class Solution:
    def maxProfit(self, prices):

        if len(prices) == 0:
            return 0

        dp = [[[0] * 3 for i in range(2)] for j in range(len(prices))]

        # 第一天不买
        dp[0][0][0] = 0

        # 第一天买入
        dp[0][1][0] = -prices[0]

        # 第一天不可能卖出
        dp[0][0][1] = float('-inf')
        dp[0][0][2] = float('-inf')

        dp[0][1][1] = float('-inf')
        dp[0][1][2] = float('-inf')


        for i in range(1, len(prices)):# 两次

            # 未持股，未卖出，即从来没有进行过买卖
            dp[i][0][0] = 0

            # 未持股，卖出过一次。可能是今天卖的，也可能是之前卖的
            dp[i][0][1] = max(dp[i - 1][1][0] + prices[i], dp[i - 1][0][1])

            # 未持股，卖出过两次，可能是今天卖的，可能是之前卖的

            dp[i][0][2] = max(dp[i - 1][1][1] + prices[i], dp[i - 1][0][2])


            # 持股，未卖出，可能是今天买的，也可能是之前买的
            dp[i][1][0] = max(dp[i - 1][0][0] - prices[i], dp[i - 1][1][0])

            # 持股，卖出过一次，可能是今天买的，也可能是之前买的
            dp[i][1][1] = max(dp[i - 1][0][1] - prices[i], dp[i - 1])






            




        return dp[-1][0]

