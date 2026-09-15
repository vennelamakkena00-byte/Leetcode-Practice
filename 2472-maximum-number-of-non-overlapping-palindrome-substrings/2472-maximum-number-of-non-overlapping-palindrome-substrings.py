class Solution(object):

    def maxPalindromes(self, s, k):

        n = len(s)

        pal = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or pal[i + 1][j - 1]):
                    pal[i][j] = True

        dp = [0] * (n + 1)

        for i in range(n):
            dp[i + 1] = max(dp[i + 1], dp[i])

            for j in range(i + k - 1, n):
                if pal[i][j]:
                    dp[j + 1] = max(dp[j + 1], dp[i] + 1)

        return dp[n]