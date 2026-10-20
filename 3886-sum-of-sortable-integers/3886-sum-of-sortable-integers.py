class Solution:
    def sortableIntegers(self, nums):
        n = len(nums)
        target = sorted(nums)

        def is_rotation(a, b):
            k = len(a)

            # Build LPS array for KMP
            lps = [0] * k
            j = 0
            for i in range(1, k):
                while j > 0 and b[i] != b[j]:
                    j = lps[j - 1]
                if b[i] == b[j]:
                    j += 1
                lps[i] = j

            text = a + a
            j = 0

            for x in text:
                while j > 0 and x != b[j]:
                    j = lps[j - 1]

                if x == b[j]:
                    j += 1

                if j == k:
                    return True

            return False

        ans = 0

        divisors = []
        d = 1
        while d * d <= n:
            if n % d == 0:
                divisors.append(d)
                if d * d != n:
                    divisors.append(n // d)
            d += 1

        for k in divisors:
            ok = True

            for start in range(0, n, k):
                a = nums[start:start + k]
                b = target[start:start + k]

                if not is_rotation(a, b):
                    ok = False
                    break

            if ok:
                ans += k

        return ans