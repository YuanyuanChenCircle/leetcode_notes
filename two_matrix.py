class Solution:
    def searchMatrix(self, matrix, target):

        x = 0
        y = len(matrix[0]) - 1


        while x < len(matrix) and y >= 0:

            if target == matrix[x][y]:

                return True

            elif target > matrix[x][y]:

                x += 1
            else:

                y -= 1

        return False

