class Solution:
    def shortestBeautifulSubstring(self, s, k):
        ones = []

        for i in range(len(s)):
            if s[i] == '1':
                ones.append(i)

        if len(ones) < k:
            return ""

        ans = ""

        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]

            candidate = s[start:end + 1]

            if ans == "":
                ans = candidate
            elif len(candidate) < len(ans):
                ans = candidate
            elif len(candidate) == len(ans) and candidate < ans:
                ans = candidate

        return ans