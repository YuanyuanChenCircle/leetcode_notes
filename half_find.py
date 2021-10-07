class Solution:
    def search(self, nums, target):


        if len(nums) == 0:

            return -1


        left = 0
        right = len(nums) - 1

        mid = (left + right) // 2


        while left <= right:



            if nums[mid] == target:
                return mid

            elif nums[mid] > target:

                right = mid - 1

            else:

                left = mid + 1
            mid = (left + right) // 2


        return -1






