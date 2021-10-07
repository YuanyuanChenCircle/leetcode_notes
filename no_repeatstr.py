class Solution:
    def lengthOfLongestSubstring(self, s):

        if len(s) == 1 or len(s) == 0:
            return len(s)



        left = 0
        right = 1
        temp = [s[0]]
        max_str = 0

        while left <= right and right < len(s):

            while s[right] in temp and left <= right:

                left += 1
                temp.pop(0)

            temp.append(s[right])

            right += 1

            max_str = max(max_str, len(temp))

        return max_str



