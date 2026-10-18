class Solution:
    def numOfWays(self, nums):
        MOD = 1000000007
        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][0] = 1
            dp[i][i] = 1

            for j in range(1, i):
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % MOD

        def solve(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]

            left = left[1:] if left and left[0] == root else left
            right = right[1:] if right and right[0] == root else right

            left_ways = solve(left)
            right_ways = solve(right)

            total = dp[len(arr) - 1][len(left)]

            return (total * left_ways * right_ways) % MOD

        return (solve(nums) - 1) % MOD