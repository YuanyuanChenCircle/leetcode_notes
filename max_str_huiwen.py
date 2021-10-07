class Solution:
    def longestPalindrome(self, s):

        if len(s) == 0:
            return ""

        # 状态转移方程的含义表示从i到j是否是回文的；是不是回文用True表示

        ans = ''

        max_len = 0

        dp = [[False] * len(s) for _ in range(len(s))]

        # 初始化

        # 自己到自己本身肯定是回文的

        for i in range(len(s)):

            # 包括第i个字符串

            for j in range(i + 1):

                if s[i] == s[j]:

                    if i - j < 2:

                        dp[j][i] = True

                    else:

                        dp[j][i] = dp[j + 1][i - 1]


                else:

                    dp[j][i] = False


                if dp[j][i]:

                    if max_len < len(s[j:i + 1]):

                        ans = s[j:i + 1]
                        max_len = len(s[j:i + 1])
        return ans











