class Solution:
    def permute(self, nums):

        n = len(nums)
        res = []

        self.dfs([], nums, res,n)

        return res






    def dfs(self, temp, nums, res, n):


        if len(temp) == n:
            
            res.append(temp)
            print(res)


        for i in range(len(nums)):

            temp.append(nums[i])

            self.dfs(temp, nums[0:i] + nums[i + 1:], res, n)

            temp.remove(nums[i])












