class Solution:
    def solveNQueens(self, n):
        # N皇后问题的解法

        grid = [['.'] * n for i in range(n)]

        queen = set()

        output = []

        self.queenDFS(grid, 0, n, queen, output)

        return output

    def isQueenOK(self, grid, row, col):

        # 纵向合法性校验
        for i in range(row):

            if grid[i][col] == 'Q':

                return False

        # 主对角线合法性校验
        x = row - 1
        y = col - 1

        while x >= 0 and y >= 0:

            if grid[x][y] == 'Q':

                return False

            x -= 1
            y -= 1


        # 副对角线合法性校验
        x = row - 1
        y = col + 1

        while x >= 0 and y < len(grid[0]):

            if grid[x][y] == 'Q':

                return False

            x -= 1
            y += 1
        return True

    def queenDFS(self, grid, index, n, queen, output):

        if index == n:

            solution = []
            for _, col in sorted(queen):

                solution.append('.' * col + 'Q' + '.' * (n - col - 1))

            output.append(solution)
            return


        for i in range(n):

            if(self.isQueenOK(grid, index, i)):

                queen.add((index, i))

                grid[index][i] = 'Q'

                self.queenDFS(grid, index + 1, n, queen, output)

                grid[index][i] = '.'
                queen.remove((index, i))




