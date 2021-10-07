class Solution:
    def spiralOrder(self, matrix):

        u = 0
        d = len(matrix) - 1

        l = 0
        r = len(matrix[0]) - 1

        ans = []

        while True:

            for i in range(l, r + 1):

                ans.append(matrix[u][i])

            u += 1

            if u > d:
                break

            for j in range(u,d + 1):

                ans.append(matrix[j][r])

            r -= 1

            if r < l:
                break


            for k in range(r, l - 1, -1):

                ans.append(matrix[d][k])

            d -= 1

            if d < u:
                break

            for m in range(d, u - 1, -1):

                ans.append(matrix[m][l])

            l += 1

            if l > r:
                break

        return ans












