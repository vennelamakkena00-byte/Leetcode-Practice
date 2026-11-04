class Solution:
    def minOperations(self, nums, x, k):
        n = len(nums)
        m = n - x + 1

        # coordinate compression
        vals = sorted(set(nums))
        pos_of = {v: i + 1 for i, v in enumerate(vals)}
        M = len(vals)

        cnt = [0] * (M + 1)   # Fenwick tree: counts
        sm = [0] * (M + 1)    # Fenwick tree: sums

        LOG = 1
        while (1 << LOG) <= M:
            LOG += 1

        # ---- Step 1: window costs (distance to median) ----
        cost = [0] * m
        total = 0
        need = (x + 1) // 2   # median is the need-th smallest

        for i in range(n):
            # add nums[i]
            v = nums[i]
            p = pos_of[v]
            while p <= M:
                cnt[p] += 1
                sm[p] += v
                p += p & -p
            total += v

            # remove nums[i - x]
            if i >= x:
                v = nums[i - x]
                p = pos_of[v]
                while p <= M:
                    cnt[p] -= 1
                    sm[p] -= v
                    p += p & -p
                total -= v

            if i >= x - 1:
                # find need-th smallest via binary descent
                pos = 0
                rem = need
                for b in range(LOG, -1, -1):
                    nxt = pos + (1 << b)
                    if nxt <= M and cnt[nxt] < rem:
                        pos = nxt
                        rem -= cnt[nxt]
                med = vals[pos]   # pos is 0-based index of the answer

                # prefix count/sum of elements <= med
                p = pos + 1
                cl = 0
                sl = 0
                while p > 0:
                    cl += cnt[p]
                    sl += sm[p]
                    p -= p & -p

                cost[i - x + 1] = (med * cl - sl) + ((total - sl) - med * (x - cl))

        # ---- Step 2: choose k non-overlapping windows ----
        INF = float('inf')
        prev = [0] * (n + 1)
        for _ in range(k):
            cur = [INF] * (n + 1)
            for i in range(1, n + 1):
                best = cur[i - 1]
                if i >= x:
                    c = prev[i - x] + cost[i - x]
                    if c < best:
                        best = c
                cur[i] = best
            prev = cur
        return prev[n]