class Solution:
    def spiralOrder(self, matrix):

        if len(matrix) == 0:
            return []


        u = 0

        d = len(matrix) - 1

        l = 0

        r = len(matrix[0]) - 1

        res = []



        while True:


            for i in range(l, r + 1):

                res.append(matrix[u][i])

            u += 1

            if u > d:
                break

            for j in range(u, d + 1):

                res.append(matrix[j][r])

            r -= 1
            if r < l:
                break

            for l in range(r, l - 1, -1):

                res.append(matrix[d][l])

            d -= 1

            if d < u:
                break


            for k in range(d, u - 1, -1):

                res.append(matrix[k][l])

            l += 1

            if l > r:
                break
        return res


