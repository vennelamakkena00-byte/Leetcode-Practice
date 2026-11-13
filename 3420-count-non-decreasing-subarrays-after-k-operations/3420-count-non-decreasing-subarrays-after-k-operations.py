from collections import deque

class Solution(object):
    def countNonDecreasingSubarrays(self, nums, k):
        n = len(nums)
        dq = deque()   # [max_value, run_length]; front run is nearest to l
        cost = 0       # sum of (prefix max - nums[i]) over window [l, r]
        r = n - 1
        ans = 0
        for l in range(n - 1, -1, -1):
            v = nums[l]
            length = 1
            # nums[l] raises the prefix max of every run it dominates
            while dq and dq[0][0] <= v:
                val, ln = dq.popleft()
                cost += (v - val) * ln
                length += ln
            dq.appendleft([v, length])
            # shrink from the right until the cost fits
            while cost > k:
                run = dq[-1]
                cost -= run[0] - nums[r]
                run[1] -= 1
                if run[1] == 0:
                    dq.pop()
                r -= 1
            ans += r - l + 1
        return ans