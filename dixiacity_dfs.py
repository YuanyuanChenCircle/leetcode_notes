class Solution:
    def calculateMinimumHP(self, dungeon):


        if len(dungeon) == 0:
            return 0

        dp = [[-1] * len(dungeon[0]) for _ in range(len(dungeon))]


        return self.dfs(0, 0, len(dungeon), len(dungeon[0]), dungeon, dp) + 1



    def dfs(self, x, y, row, col, dungeon, dp):

        

        if x >= row or y >= col:

            return float("inf")

        if dp[x][y] != -1:
            return dp[x][y]



        # 退出条件
        if x == row - 1 and y == col - 1:

            if dungeon[x][y] >= 0:

                return 0

            else:

                return (-1) * dungeon[x][y]


        rightMin = self.dfs(x, y + 1, row, col, dungeon, dp)

        downMin = self.dfs(x + 1, y, row, col, dungeon, dp)

        needMin = min(rightMin, downMin) - dungeon[x][y]

        res = 0

        if needMin < 0:

            res = 0

        else:

             res = needMin

        # print()

        dp[x][y] = res

        return res

