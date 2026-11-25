class Solution:
    def smallestUniqueSubarray(self, nums):
        n = len(nums)

        MOD1 = 1000000007
        MOD2 = 1000000009
        BASE1 = 911382323
        BASE2 = 972663749

        h1 = [0] * (n + 1)
        h2 = [0] * (n + 1)
        p1 = [1] * (n + 1)
        p2 = [1] * (n + 1)

        for i in range(n):
            x = nums[i]

            h1[i + 1] = (h1[i] * BASE1 + x) % MOD1
            h2[i + 1] = (h2[i] * BASE2 + x) % MOD2

            p1[i + 1] = (p1[i] * BASE1) % MOD1
            p2[i + 1] = (p2[i] * BASE2) % MOD2

        def check(length):
            freq = {}
            unique = 0

            for i in range(n - length + 1):
                j = i + length

                a = (h1[j] - h1[i] * p1[length]) % MOD1
                b = (h2[j] - h2[i] * p2[length]) % MOD2

                key = (a, b)

                count = freq.get(key, 0)

                if count == 0:
                    unique += 1
                elif count == 1:
                    unique -= 1

                freq[key] = count + 1

            return unique > 0

        left, right = 1, n

        while left < right:
            mid = (left + right) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left