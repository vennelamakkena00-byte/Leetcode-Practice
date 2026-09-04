class Solution:
    def firstStableIndex(self, nums, k):
        n = len(nums)

        suffixMin = [0] * n
        suffixMin[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            suffixMin[i] = min(nums[i], suffixMin[i + 1])

        max_so_far = nums[0]

        for i in range(n):
            max_so_far = max(max_so_far, nums[i])

            if max_so_far - suffixMin[i] <= k:
                return i

        return -1