class Solution:
    def fourSum(self, nums, target):

        # 有很多种的组合

        res_nums = []
        nums.sort() # 从小到大排序
        # print(nums)


        # 初始化操作
        if len(nums) <= 3:
            return []


        for i in range(len(nums) - 3):


            if i >= 1 and nums[i] == nums[i - 1]:

                continue

            j = i + 1


            for k in range(j, len(nums) - 2):

                if k >= j + 1 and nums[k] == nums[k - 1]:
                    continue

                l = k + 1

                m = len(nums) - 1

                while l < m:
                    

                    if nums[i] + nums[k] + nums[l] + nums[m] == target:

                        res_nums.append([nums[i]] + [nums[k]] + [nums[l]] + [nums[m]])

                        l += 1

                        m -= 1
                        while l < m and nums[m] == nums[m + 1] :
                            m -= 1
                        while l < m and nums[l] == nums[l - 1]:

                            l += 1


                    elif nums[i] + nums[k] + nums[l] + nums[m] > target:

                        m -= 1

                        while l < m and nums[m] == nums[m + 1]:
                            m -= 1

                    elif nums[i] + nums[k] + nums[l] + nums[m] < target:

                        l += 1

                        while l < m and nums[l] == nums[l - 1]:

                            l += 1

        return res_nums

