class Solution:
    def longestPalindrome(self, s):

        if len(s) == 0:

            return ""


        dp = [[False]*len(s) for _ in range(len(s))]

        maxlen = 0

        for i in range(len(dp)):

            dp[i][i] = True


        for i in range(len(s)):

            for j in range(i + 1):

                if s[i] == s[j]:

                    if i - j < 2:

                        dp[j][i] = True 

                    else:

                        dp[j][i] = dp[j + 1][i - 1]

                else:

                    dp[j][i] = False

                if dp[j][i]:

                    if maxlen < len(s[j:i+1]):

                        ans = s[j:i+1]

                        maxlen = len(s[j:i + 1])

        return ans










