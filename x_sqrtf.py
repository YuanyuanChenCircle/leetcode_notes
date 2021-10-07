class Solution:
    def mySqrt(self, x):

        l = 1

        r = x

        while l <= r:

            mid = (l + r) // 2
            # print(mid)
            # print("mid")

            temp = mid ** 2


            if temp < x:

                l = mid + 1
            elif temp > x:

                r = mid - 1
            else:
                return mid
            # print(l)
            # print(r)

        return l

so = Solution()
print(so.mySqrt(8))