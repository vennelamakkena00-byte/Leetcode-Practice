class Solution:
    def uniformArray(self, nums1):
        min_odd = float('inf')
        min_even = float('inf')

        for x in nums1:
            if x % 2 == 0:
                min_even = min(min_even, x)
            else:
                min_odd = min(min_odd, x)

        # All numbers are even
        if min_odd == float('inf'):
            return True

        # All numbers are odd
        if min_even == float('inf'):
            return True

        # We need every number to become odd.
        return min_odd < min_even