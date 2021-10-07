class Solution:
    def maxDistance(self, grid):

        depth = 0

        stack = []

        # 利用bfs进行实现

        # 首先需要找到所有的的源节点
        for i in range(len(grid)):

            for j in range(len(grid[0])):


                if grid[i][j] == 1:

                    stack.append((i, j))

        if len(stack) == 0 or len(stack) == (len(grid) * len(grid[0])):
            return -1

        while len(stack) > 0:

            


            n = len(stack)

            for i in range(n):

                x, y = stack.pop(0)

                if (x + 1) < len(grid) and grid[x + 1][y] == 0:

                    grid[x + 1][y] = 2

                    stack.append((x + 1, y))

                if x - 1 >= 0 and grid[x - 1][y] == 0:

                    grid[x - 1][y] = 2
                    stack.append((x - 1, y))

                if y + 1 < len(grid[0]) and grid[x][y + 1] == 0:

                    grid[x][y + 1] = 2

                    stack.append((x, y + 1))


                if y - 1 >= 0 and grid[x][y - 1] == 0:

                    grid[x][y - 1] = 2

                    stack.append((x, y - 1))

            if len(stack) > 0:

                depth += 1

        return depth


