class Solution(object):
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        B1 = [0] * (n + 2)
        B2 = [0] * (n + 2)

        def upd(B, i, v):
            while i <= n + 1:
                B[i] += v
                i += i & -i

        def qry(B, i):
            s = 0
            while i > 0:
                s += B[i]
                i -= i & -i
            return s

        def range_add(l, r, v):  # 1-indexed, inclusive
            upd(B1, l, v)
            upd(B1, r + 1, -v)
            upd(B2, l, v * (l - 1))
            upd(B2, r + 1, -v * r)

        def prefix(i):
            return qry(B1, i) * i - qry(B2, i)

        last = {}
        cur = 0
        ans = 0
        for r, x in enumerate(nums):
            a = last.get(x, -1) + 1          # 0-indexed start of range
            L, R = a + 1, r + 1              # 1-indexed
            s = prefix(R) - prefix(L - 1)    # sum of d over [a, r] before the add
            cur += 2 * s + (R - L + 1)
            range_add(L, R, 1)
            last[x] = r
            ans = (ans + cur) % MOD
        return ans