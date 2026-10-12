class Solution(object):
    def maxSum(self, nums, k):
        MOD = 10**9 + 7
        cnt = [0] * 30

        # Count how many numbers have each bit set
        for x in nums:
            for b in range(30):
                if x & (1 << b):
                    cnt[b] += 1

        ans = 0
        for _ in range(k):
            cur = 0
            for b in range(30):
                if cnt[b] > 0:
                    cur |= (1 << b)
                    cnt[b] -= 1
            ans = (ans + cur * cur) % MOD

        return ans