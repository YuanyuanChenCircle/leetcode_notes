class Solution:
    def maxAreaOfIsland(self, grid):

        area = 0

        for i in range(len(grid)):

            for j in range(len(grid[0])):

                if grid[i][j] == 1:



                    area = max(area, self.dfs(grid, i, j))
        return area


    def dfs(self, grid, x, y):

        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != 1:
            return 0

        grid[x][y] = 0

        nums = 1
        nums += self.dfs(grid, x + 1, y)

        nums += self.dfs(grid, x - 1, y)

        nums += self.dfs(grid, x, y + 1)

        nums += self.dfs(grid, x, y - 1)

        return nums


