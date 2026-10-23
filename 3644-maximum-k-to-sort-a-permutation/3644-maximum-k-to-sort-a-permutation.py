class Solution(object):
    def sortPermutation(self, nums):
        k = -1
        for i, val in enumerate(nums):
            if val != i:
                if k == -1:
                    k = val
                else:
                    k &= val
                    
        # If no elements are out of place, the array is already sorted
        return k if k != -1 else 0