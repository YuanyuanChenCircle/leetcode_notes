class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        res = []
        p = 0
        q = 0

        while p < len(nums1) and q < len(nums2):

            if nums1[p] < nums2[q]:

                res.append(nums1[p])
                p += 1

            else:

                res.append(nums2[q])
                q += 1


        if p == len(nums1):

            while q < len(nums2):


                res.append(nums2[q])
                q += 1
        if q == len(nums2):

            while p < len(nums1):

                res.append(nums1[p])
                p += 1


        if len(res)% 2 == 0:

            return (res[len(res)//2 - 1] + res[len(res)//2])/2
        else:
            return res[len(res)//2]


