class Solution:
    def sortedSquares(self, nums):


        temp_nums = [x**2 for x in nums]

        res = [0] * len(nums)
        index = len(nums) - 1

        # 
        left = 0
        right = len(nums) - 1

        while left <= right:

            if temp_nums[left] < temp_nums[right]:

                res[index] = temp_nums[right]

                right -= 1
                index -= 1
            else:

                res[index] = temp_nums[left]
                left += 1
                index -= 1
    
        return res