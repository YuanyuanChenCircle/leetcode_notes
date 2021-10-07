class Solution:
    def findKthLargest(self, nums, k):
        start = 0
        end = len(nums) - 1
            # pivot_index = partition(arr, start, end)
        while start <= end:
            pivot_index = self.partition(nums, start, end)

            if pivot_index == len(nums) - k:

                return nums[pivot_index]

            elif pivot_index > len(nums) - k:

                end = pivot_index - 1
            else:
                start = pivot_index + 1

    def partition(self, arr, start, end):

            pivot = arr[start]
            left = start
            right = end

            index = start
            # 坑的位置，初始等于pivot的位置
            while right >= left:

                # right指针从右向左进行比较

                while right >= left:

                    if arr[right] < pivot:

                        arr[left] = arr[right]
                        index = right
                        left += 1
                        break
                    right -= 1

                # left指针从左向右比较
                while right >= left:

                    if arr[left] > pivot:

                        arr[right] = arr[left]
                        index = left
                        right -= 1
                        break
                    left += 1

                arr[index] = pivot
            return index
        



if __name__ == '__main__':

    arr = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6]
    so = Solution()
    print(so.findKthLargest(arr, 2))




        


    











