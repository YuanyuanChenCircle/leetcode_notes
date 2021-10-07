class Solution:
    def solveNQueens(self, n):
    	# 本题目找出所有的结果
    	# 首先需要创建一个棋盘

    	grid = [['.'] * n for _ in range(n)]

    	res = []
    	temp = []

    	self.queen_dfs(grid, 0, temp, res)

    	return res


    def queen_dfs(self, grid, index, temp, res):

    	if index == len(grid):

    		solution = []

    		for i in range(len(temp)):
    			solution.append('.' * temp[i] + 'Q' + '.' * (len(grid[0]) - temp[i] - 1))


    		# print("######")
    		# print(solution)
    		res.append(solution)


    		return


    	for i in range(len(grid[0])):


	    	if self.queen_ok(grid, index, i):
	    		
	    		temp.append(i)

	    		grid[index][i] = 'Q'

	    		self.queen_dfs(grid, index + 1, temp, res)

	    		temp.pop()

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










    	



















