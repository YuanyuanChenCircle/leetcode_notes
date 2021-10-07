class Solution:
    def totalNQueens(self, n):

        # 本题目找出所有的结果
        # 首先需要创建一个棋盘

        grid = [['.'] * n for _ in range(n)]

        res = []

        self.queen_dfs(grid, 0, res)

        return len(res)


    def queen_dfs(self, grid, index, res):

        if index == len(grid):

            res.append(0)


            return


        for i in range(len(grid[0])):


            if self.queen_ok(grid, index, i):
                
                # temp.append(i)

                grid[index][i] = 'Q'

                self.queen_dfs(grid, index + 1, res)

                # temp.pop()

                grid[index][i] = '.'




    def queen_ok(self, grid, x, y):

        # 首先纵向判断
        x1 = x - 1
        y1 = y
        
        while x1 >= 0:
            
            if grid[x1][y1] == 'Q':
                return False
            x1 -= 1

        # 主对角线进行判断
        x1 = x - 1
        y1 = y - 1
        
        
        while x1 >= 0 and y1 >= 0:

            

            if grid[x1][y1] == 'Q':
                return False

            x1 -= 1
            y1 -= 1

        # 副对角线进行判断
        x1 = x - 1
        y1 = y + 1


        while x1 >= 0 and y1 < len(grid[0]):

            if grid[x1][y1] == 'Q':

                return False
            x1 -= 1
            y1 += 1

        return True