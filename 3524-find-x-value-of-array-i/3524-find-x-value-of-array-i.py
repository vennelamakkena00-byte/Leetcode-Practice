class Solution(object):
    def resultArray(self, nums, k):
        # dp[r] = number of subarrays ending at the previous position
        # whose product % k == r
        dp = [0] * k

        # ans[r] = number of all subarrays whose product % k == r
        ans = [0] * k

        for num in nums:
            x = num % k

            # New subarray consisting only of nums[i]
            new_dp = [0] * k
            new_dp[x] += 1

            # Extend every previous subarray by nums[i]
            for r in range(k):
                if dp[r] > 0:
                    new_r = (r * x) % k
                    new_dp[new_r] += dp[r]

            # Add all subarrays ending at this position
            for r in range(k):
                ans[r] += new_dp[r]

            dp = new_dp

        return ans