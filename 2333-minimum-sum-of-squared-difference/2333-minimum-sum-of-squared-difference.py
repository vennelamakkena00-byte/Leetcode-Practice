class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diffs = sorted(
            [abs(a - b) for a, b in zip(nums1, nums2)],
            reverse=True
        )

        k = k1 + k2

        if sum(diffs) <= k:
            return 0

        diffs.append(0)

        for i in range(len(diffs) - 1):
            count = i + 1
            need = (diffs[i] - diffs[i + 1]) * count

            if k >= need:
                k -= need
            else:
                level = diffs[i] - k // count
                remainder = k % count

                return (
                    sum((level - 1) ** 2 for _ in range(remainder))
                    + sum(level ** 2 for _ in range(count - remainder))
                    + sum(d * d for d in diffs[count:-1])
                )

        return 0