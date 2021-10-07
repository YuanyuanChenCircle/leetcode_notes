class Solution:
    def threeSum(self, nums):

        if len(nums) == 0:
            return []

        nums.sort()

        res = []


        for i in range(len(nums)):




            if nums[i] > 0:

                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue


            l = i + 1

            r = len(nums) - 1

            while l < r:

                if nums[i] + nums[l] + nums[r] == 0:

                    res.append([nums[i]] + [nums[l]] + [nums[r]])
                    l += 1
                    r -= 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

                    while nums[r] == nums[r + 1] and l < r:
                        r -= 1
                
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1

        return res









