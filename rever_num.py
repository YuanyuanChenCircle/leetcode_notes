class Solution:

    def __init__(self):

        self.count = 0

    def reversePairs(self, nums):

        # 求逆序对，进行归并排序

        # 归并排序就是先进行拆分，再进行组合的过程

        self.merge_chaifen(nums, 0, len(nums) - 1)
        return self.count


    def merge_chaifen(self, nums, start, end):

        if start < end:

            mid = (start + end) // 2

            self.merge_chaifen(nums, start, mid)
            self.merge_chaifen(nums, mid + 1, end)

            self.merge(nums, start, mid, end)


    def merge(self, nums, start, mid, end):
        

        de = [0] * (end - start + 1)

        p1 = start

        p2 = mid + 1

        p = 0

        while p1 <= mid and p2 <= end:

            if nums[p1] <= nums[p2]:

                de[p] = nums[p1]
                p += 1
                p1 += 1

            else:

                de[p] = nums[p2]
                p += 1
                p2 += 1

                # 记录逆
                self.count += (mid - p1 + 1)
                # 因为mid到p1是有序的

        # 左侧小集合还有剩余，依次放入大集合

        while p1 <= mid:

            de[p] = nums[p1]
            p += 1
            p1 += 1

        while p2 <= end:

            de[p] = nums[p2]
            p += 1
            p2 += 1

        # 把大集合的元素复制回原来的数组
        for i in range(len(de)):

            nums[i + start] = de[i]



















