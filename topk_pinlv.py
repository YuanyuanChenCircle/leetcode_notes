class Solution:
    def topKFrequent(self, nums, k):

        res = {}

        ans = []

        for i in range(len(nums)):

            if nums[i] not in res:

                res[nums[i]] = 1
            else:

                res[nums[i]] += 1


        res = sorted(res.items(), key = lambda x: x[1], reverse=True)

        for i in range(k):

            ans.append(res[i][0])



        

        return ans



