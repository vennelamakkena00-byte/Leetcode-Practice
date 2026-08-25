class Solution:
    def missingMultiple(self, nums, k):
        nums_set = set(nums)
        multiple = k

        while multiple in nums_set:
            multiple += k

        return multiple