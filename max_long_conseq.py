class Solution:
    def longestConsecutive(self, nums):

        if len(nums) == 0:
            return 0

        temp = set(nums)

        maxlen = 1

        for x in temp:

            l = 1

            # 因为是找到最小的，所以对一些进行过滤
            if x - 1 in temp:
                continue


            while x + 1 in temp: # 思想是遍历所有的数字，直到找到最小的数字，这样就可以加入一些过滤条件，进行过滤

                l += 1

                x += 1

            maxlen = max(maxlen, l)

        return maxlen


