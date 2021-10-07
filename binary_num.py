class Solution:
    def search(self, nums, target):

        l = 0
        r = len(nums) - 1

        # mid在中间，肯定又一边是有序的，另一边可能有序，可能无序

        while l <= r:

            mid = (l + r) // 2

            if nums[mid] == target:

                return mid


            if nums[l] <= nums[mid]: # 通过这个条件确定是否有序，如果小于，就是有序，否则无序

                if target < nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1


            else: #
            

                if target <= nums[r] and target > nums[mid]:

                    l = mid + 1

                else:
                    
                    r = mid - 1

        return -1

