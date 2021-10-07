class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # 先按照对角线进行翻转，限制列的数量

        for i in range(len(matrix)):

            for j in range(i, len(matrix[0])):

                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]

                matrix[j][i] = temp

        for i in range(len(matrix)):

            for j in range(len(matrix[0])//2):

                # 左右进行交换

                temp = matrix[i][j]
                matrix[i][j] = matrix[i][len(matrix) -1 - j]
                matrix[i][len(matrix) -1 - j] = temp

        return matrix





