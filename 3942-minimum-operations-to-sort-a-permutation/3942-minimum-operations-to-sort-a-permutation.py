class Solution:
    def minOperations(self, nums):
        n = len(nums)
        best = float('inf')

        # Case 1: rotation of increasing array
        k = nums[0]
        if all(nums[i] == (k + i) % n for i in range(n)):
            t = (n - k) % n
            if t == 0:
                best = 0
            else:
                best = min(best, t, n - t + 2)

        # Case 2: rotation of decreasing array
        if all(nums[i] == (k - i) % n for i in range(n)):
            t = (n - nums[-1]) % n
            best = min(best, min(t, n - t) + 1)

        return -1 if best == float('inf') else best