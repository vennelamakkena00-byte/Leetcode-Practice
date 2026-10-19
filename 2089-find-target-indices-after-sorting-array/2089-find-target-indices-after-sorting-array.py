class Solution(object):
    def targetIndices(self, nums, target):
        less = equal = 0

        for x in nums:
            if x < target:
                less += 1
            elif x == target:
                equal += 1

        return list(range(less, less + equal))