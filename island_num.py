class Solution:
    def numIslands(self, grid):

        count = 0

        for i in range(len(grid)):

            for j in range(len(grid[0])):

                if grid[i][j] == '1':

                    self.dfs(grid, i, j)
                    count += 1
        return count




    def dfs(self, grid, x, y):

        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == '0':

            return

        grid[x][y] = '0'

        self.dfs(grid, x - 1, y)
        self.dfs(grid, x + 1, y)
        self.dfs(grid, x, y - 1)
        self.dfs(grid, x, y + 1)





