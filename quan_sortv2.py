class Solution:
    def permuteUnique(self, nums):

        # 返回不重复的全排列

        res = []
        n = len(nums)

        self.dfs( [], nums, res, n)

        return res


    def dfs(self, res_temp, nums, res, n):

        

        # print(res_temp)

        if len(res_temp) == n and res_temp not in res:


            # print(res_temp)

            # print("########")

            res.append(res_temp)

            return

        for i in range(len(nums)):

            if i != 0 and nums[i] == nums[i - 1]:
                continue


            # print(res_temp)


            self.dfs(res_temp + [nums[i]], nums[:i] + nums[i + 1:], res, n)




