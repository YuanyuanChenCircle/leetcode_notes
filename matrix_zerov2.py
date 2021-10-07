class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # 用第0行和第0列来记录矩阵的该行和该列是否需要进行置为0
        # 怎么设置标置位

        row_flag = 1
        col_flag = 1


        for i in range(len(matrix[0])):

            if matrix[0][i] == 0:

                row_flag = 0

        for j in range(len(matrix)):

            if matrix[j][0] == 0:

                col_flag = 0


        # 记录为需要置换为0的行和列

        for i in range(1, len(matrix)):

            for j in range(1, len(matrix[0])):

                if matrix[i][j] == 0:

                    matrix[i][0] = 0

                    matrix[0][j] = 0


        # 赋值为0
        for i in range(1, len(matrix)):

            for j in range(1, len(matrix[0])):

                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        for i in range(len(matrix[0])):

            if row_flag == 0:
                matrix[0][i] = 0

        for i in range(len(matrix)):

            if col_flag == 0:

                matrix[i][0] = 0

        return matrix






