class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # 这个题就考验计算能力, 记录下需要置换为0的行和列索引即可


        rowset = set()

        colset = set()


        for i in range(len(matrix)):

            for j in range(len(matrix[0])):

                if matrix[i][j] == 0:

                    rowset.add(i)
                    colset.add(j)

        for i in range(len(matrix)):

            for j in range(len(matrix[0])):


                if i in rowset:
                    matrix[i][j] = 0
                if j in colset:
                    matrix[i][j] = 0

        return matrix






