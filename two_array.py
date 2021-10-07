class Solution:
    def findNumberIn2DArray(self, matrix, target):

        if len(matrix) == 0:
            return False


        i = 0

        j = len(matrix[0]) - 1


        while i < len(matrix) and j >= 0:


            if target == matrix[i][j]:

                return True


            elif target > matrix[i][j]:

                i += 1

            else:

                j -= 1

                print(j)



        return False

