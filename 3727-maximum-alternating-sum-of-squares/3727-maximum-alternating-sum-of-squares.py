class Solution:
    def maxAlternatingSum(self, nums):
        squares = sorted(x * x for x in nums)
        n = len(squares)
        k = (n + 1) // 2

        return sum(squares[n-k:]) - sum(squares[:n-k])